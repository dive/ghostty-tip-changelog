#!/usr/bin/env python3

"""Generate changelogs between sequential successful workflow runs.

Example:
  ./ghostty-tip-daily-changelog.py
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = "ghostty-org/ghostty"
WORKFLOW = "release-tip.yml"
FETCH_RUNS_PER_DAY = 30


@dataclass(frozen=True)
class WorkflowRun:
    database_id: int
    head_sha: str
    created_at: str
    url: str


def parse_workflow_run(entry: object) -> WorkflowRun | None:
    if not isinstance(entry, dict):
        return None

    database_id = entry.get("databaseId")
    head_sha = entry.get("headSha")
    created_at = entry.get("createdAt")
    url = entry.get("url")
    if not all([database_id, head_sha, created_at, url]):
        return None

    return WorkflowRun(
        database_id=int(database_id),
        head_sha=str(head_sha),
        created_at=str(created_at),
        url=str(url),
    )


def gh_json(args: list[str]) -> object:
    cmd = ["gh", *args]
    try:
        proc = subprocess.run(
            cmd,
            check=True,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        print("error: gh CLI is not installed or not in PATH", file=sys.stderr)
        sys.exit(127)
    except subprocess.CalledProcessError as exc:
        err = exc.stderr.strip() or exc.stdout.strip() or "unknown error"
        print(f"error: {' '.join(cmd)} failed: {err}", file=sys.stderr)
        sys.exit(exc.returncode or 1)

    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        print(f"error: failed to parse JSON output from {' '.join(cmd)}: {exc}", file=sys.stderr)
        sys.exit(1)


def fetch_successful_runs(limit: int, created_filter: str) -> list[WorkflowRun]:
    raw = gh_json(
        [
            "run",
            "list",
            "--repo",
            REPO,
            "--workflow",
            WORKFLOW,
            "--status",
            "success",
            "--created",
            created_filter,
            "--limit",
            str(limit),
            "--json",
            "databaseId,headSha,createdAt,url",
        ]
    )

    if not isinstance(raw, list):
        print("error: unexpected response from gh run list", file=sys.stderr)
        sys.exit(1)

    runs: list[WorkflowRun] = []
    for entry in raw:
        run = parse_workflow_run(entry)
        if run is not None:
            runs.append(run)

    return sorted(runs, key=lambda r: r.created_at)


def fetch_previous_successful_run(before_date: str) -> WorkflowRun | None:
    raw = gh_json(
        [
            "run",
            "list",
            "--repo",
            REPO,
            "--workflow",
            WORKFLOW,
            "--status",
            "success",
            "--created",
            f"<{before_date}",
            "--limit",
            "1",
            "--json",
            "databaseId,headSha,createdAt,url",
        ]
    )
    if not isinstance(raw, list) or len(raw) == 0:
        return None

    return parse_workflow_run(raw[0])


def first_line(message: str) -> str:
    for line in message.splitlines():
        trimmed = line.strip()
        if trimmed:
            return trimmed
    return "(no commit title)"


def commit_details(message: str) -> list[str]:
    lines = message.splitlines()
    subject_index: int | None = None
    for idx, line in enumerate(lines):
        if line.strip():
            subject_index = idx
            break
    if subject_index is None:
        return []

    details: list[str] = []
    for line in lines[subject_index + 1 :]:
        raw = line.rstrip()
        lowered = raw.strip().lower()
        if lowered.startswith("co-authored-by:") or lowered.startswith("signed-off-by:"):
            continue
        details.append(raw)

    while details and not details[0].strip():
        details.pop(0)
    while details and not details[-1].strip():
        details.pop()

    return details


def link_github_shortcuts(text: str) -> str:
    pattern = re.compile(r"(?<!\w)#(\d+)\b")
    return pattern.sub(rf"[#\1](https://github.com/{REPO}/issues/\1)", text)


def parse_utc_datetime(created_at: str) -> dt.datetime | None:
    try:
        return dt.datetime.fromisoformat(created_at.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except ValueError:
        return None


def day_key(created_at: str) -> str:
    when = parse_utc_datetime(created_at)
    if when is None:
        return created_at
    return when.date().isoformat()


def format_day(day: str) -> str:
    try:
        parsed = dt.date.fromisoformat(day)
        return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"
    except ValueError:
        return day


def commit_author(commit: dict[str, object], commit_data: dict[str, object]) -> tuple[str, str | None]:
    author_obj = commit.get("author")
    if isinstance(author_obj, dict):
        login = author_obj.get("login")
        html_url = author_obj.get("html_url")
        if login:
            if isinstance(html_url, str) and html_url:
                return f"@{login}", html_url
            return f"@{login}", f"https://github.com/{login}"

    commit_author_obj = commit_data.get("author")
    if isinstance(commit_author_obj, dict):
        name = commit_author_obj.get("name")
        if name:
            return str(name), None

    return "unknown", None


def fetch_compare(base_sha: str, head_sha: str) -> dict[str, object]:
    raw = gh_json(["api", f"repos/{REPO}/compare/{base_sha}...{head_sha}"])
    if not isinstance(raw, dict):
        print(f"error: unexpected compare response for {base_sha}...{head_sha}", file=sys.stderr)
        sys.exit(1)
    return raw


def note_block_lines() -> list[str]:
    return [
        "> [!NOTE]",
        "> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.",
        "> Entries are grouped by UTC day and combine commits across all successful runs for each day.",
        "",
    ]


@dataclass
class DayChangelog:
    runs: list[WorkflowRun]
    commits: list[tuple[dict[str, object], dict[str, object], str, list[str]]]
    seen_shas: set[str]


def render_markdown(runs: list[WorkflowRun]) -> str:
    lines: list[str] = note_block_lines()

    if len(runs) < 2:
        lines.append("Not enough successful runs to compare (need at least 2).")
        return "\n".join(lines) + "\n"

    by_day: dict[str, DayChangelog] = {}

    for older, newer in reversed(list(zip(runs, runs[1:]))):
        compare = fetch_compare(older.head_sha, newer.head_sha)
        raw_commits = compare.get("commits")
        if not isinstance(raw_commits, list):
            raw_commits = []

        commits: list[tuple[dict[str, object], dict[str, object], str, list[str]]] = []
        for item in raw_commits:
            if not isinstance(item, dict):
                continue
            commit_data = item.get("commit")
            if not isinstance(commit_data, dict):
                commit_data = {}
            message_obj = commit_data.get("message")
            message = message_obj if isinstance(message_obj, str) else ""
            subject = first_line(message)
            details = commit_details(message)
            commits.append((item, commit_data, subject, details))

        if len(commits) == 0:
            continue

        key = day_key(newer.created_at)
        bucket = by_day.get(key)
        if bucket is None:
            bucket = DayChangelog(runs=[], commits=[], seen_shas=set())
            by_day[key] = bucket
        bucket.runs.append(newer)

        for commit, commit_data, subject, details in commits:
            sha = str(commit.get("sha", ""))
            if sha and sha in bucket.seen_shas:
                continue
            if sha:
                bucket.seen_shas.add(sha)
            bucket.commits.append((commit, commit_data, subject, details))

    if len(by_day) == 0:
        lines.append("No changelog entries found in fetched successful runs.")
        return "\n".join(lines) + "\n"

    for key, bucket in by_day.items():
        lines.append(f"## {format_day(key)}")
        lines.append("")
        run_links = ", ".join(
            f"[{idx}]({run.url})" for idx, run in enumerate(bucket.runs, start=1)
        )
        lines.append(f"Runs: {run_links}")
        lines.append("")
        lines.append("### Changes")
        lines.append("")

        for commit, commit_data, subject, details in bucket.commits:
            sha = str(commit.get("sha", ""))
            html_url = str(commit.get("html_url", ""))
            short_sha = sha[:7] if sha else "unknown"
            author_name, author_url = commit_author(commit, commit_data)
            author = f"[{author_name}]({author_url})" if author_url else author_name
            subject_text = link_github_shortcuts(subject)
            if html_url:
                lines.append(f"- [`{short_sha}`]({html_url}) {subject_text} ({author})")
            else:
                lines.append(f"- `{short_sha}` {subject_text} ({author})")
            if details:
                lines.append("  ```text")
                for detail in details:
                    lines.append(f"  {detail}")
                lines.append("  ```")

        lines.append("")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"Generate daily changelog from successful runs of {WORKFLOW} in {REPO}."
    )
    parser.add_argument(
        "--days",
        type=int,
        default=7,
        help="Number of UTC calendar days to include, counting today (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write markdown output to a file instead of stdout",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.days < 1:
        print("error: --days must be at least 1", file=sys.stderr)
        sys.exit(2)

    today = dt.datetime.now(dt.timezone.utc).date()
    start_date = today - dt.timedelta(days=args.days - 1)
    start_date_str = start_date.isoformat()
    created_filter = f">={start_date_str}"

    # Fetch enough successful runs to cover expected nightly run volume.
    fetch_limit = max(args.days * FETCH_RUNS_PER_DAY, FETCH_RUNS_PER_DAY)
    in_range_runs = fetch_successful_runs(fetch_limit, created_filter)
    if len(in_range_runs) == 0:
        lines = note_block_lines()
        lines.append("No successful runs found for selected days.")
        markdown = "\n".join(lines) + "\n"
    else:
        runs = list(in_range_runs)
        baseline_run = fetch_previous_successful_run(start_date_str)
        if baseline_run is not None:
            runs.insert(0, baseline_run)
        runs = sorted(runs, key=lambda run: run.created_at)
        markdown = render_markdown(runs)

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
