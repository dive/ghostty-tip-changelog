> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 20, 2026 at 16:13 UTC.

## October 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39352155221)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`b58ef1d`](https://github.com/ghostty-org/ghostty/commit/b58ef1d678be2747c830bc1b1e6c0a086afecf9a) Update VOUCHED list ([#14772](https://github.com/ghostty-org/ghostty/issues/14772)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14418#discussioncomment-19055528)
  from @jcollie.
  
  Vouch: @neobrain
  ```

## October 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39261955893), [2](https://github.com/ghostty-org/ghostty/actions/runs/39185729191), [3](https://github.com/ghostty-org/ghostty/actions/runs/39178943848)  
Summary: 3 runs • 17 commits • 6 authors

### Changes

- [`152bdbc`](https://github.com/ghostty-org/ghostty/commit/152bdbc68075ee4bc5b4745fb908598a16fc628c) formatter: restore blank cells and erased backgrounds in VT output ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output wrote the empty cells of a gap between text as spaces, in the
  pen of the text before the gap, so replaying it turned them into text
  and painted that text's background into the gap. Cells that only carry
  a background (erased while a background color was set) were written as
  spaces too, and rows of only those were dropped as blank, losing the
  color.
  
  VT output now steps over the empty cells of a gap with CUF. Cells that
  only carry a background are recreated as they were made: a run of the
  same background is erased with ECH under that background, then stepped
  over. Rows of them are no longer treated as blank. Blanks carried over
  from a wrapped row when unwrapping can't be stepped over, since CUF
  stops at the end of the row, so they are still spaces, but no longer in
  the pen of the text before them.
  
  An open hyperlink is no longer closed and reopened around a gap: stepping
  over the cells doesn't write them, so the link doesn't reach them.
  ```
- [`bd1c9cc`](https://github.com/ghostty-org/ghostty/commit/bd1c9cc8cb2cad3cd949fcc566872174f306821b) formatter: keep trailing blank rows in VT output without trimming ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output left out the blank rows at the end of the formatted range,
  even with trimming off. They are part of the screen's layout: a replay
  without them scrolls less, so whenever there is scrollback the rows
  above them end up too low. After clearing below a prompt, say, the
  prompt comes back on the bottom row with older output above it.
  
  VT output without trimming now ends with a newline for each of those
  rows, mapped in the pin map to the row it ends, as between rows. Trimmed
  output and the other formats still drop them.
  ```
- [`1cd6d0b`](https://github.com/ghostty-org/ghostty/commit/1cd6d0b74ec515fc690450732fa3a9f6df8fa758) terminal/kitty: accept shared memory names without a leading slash ([@davidhodge](https://github.com/davidhodge))
  ```text
  Since 090fca451d, `t=s` names must start with a slash and contain no
  other slash. Sandboxed macOS apps can't create such names: the App
  Sandbox only allows POSIX shared memory named `<app group id>/<name>`,
  with no leading slash. So every sandboxed client was refused.
  
  kitty hit the same thing and relaxed it in kovidgoyal/kitty@2efa09d.
  The protocol spec now says terminals must accept names without a
  leading slash and pass them unmodified to shm_open and shm_unlink.
  
  Only reject clearly malformed names: empty, containing NUL, or longer
  than NAME_MAX. Slashes are left to shm_open, since the valid forms are
  platform specific (Darwin's namespace is flat, glibc and musl reject
  any slash after the leading ones).
  
  Fixes #14744
  ```
- [`0bb2c91`](https://github.com/ghostty-org/ghostty/commit/0bb2c910df7308bb1dab743a49c535458783cc67) terminal/kitty: reject a bare slash shm name, document unlink behavior ([@davidhodge](https://github.com/davidhodge))
  ```text
  Reject "/" as a shared memory name again, as before. Also note where
  we unlink the object that Ghostty unlinks whatever name the client
  sends, so a client can remove any shared memory object Ghostty can
  open, including another app group's if it can guess the name. This
  isn't new, but it's worth writing down.
  ```
- [`33111db`](https://github.com/ghostty-org/ghostty/commit/33111db3175e2261bd6ff087836b8532975eae29) core: size click_state to hold every mouse button ([@jcollie](https://github.com/jcollie))
  ```text
  MouseButton.max is the largest enum value (11), not a count, so an
  array of that length has no slot for .eleven. Recording a press or
  release of button 11 indexed past the end, which panics in safe builds.
  
  Size the array max + 1 and correct the doc comment on max that
  suggested using it directly as an array length.
  ```
- [`53fb05c`](https://github.com/ghostty-org/ghostty/commit/53fb05c6eba4e678c9a70f76bd828b74625c32d3) terminal: stop CUB and BS at the left margin ([@jcollie](https://github.com/jcollie))
  ```text
  With reverse wrap off, cursorLeft took a fast path that clamped only at
  column zero and ignored DECSLRM's left margin, so CUB and BS moved the
  cursor past it. Clamp to the left margin there as the reverse-wrap path
  and cursorRight already do, unless the cursor is already left of it.
  
  Fixes esctest's test_BS_StopsAtLeftMargin and
  test_CUB_StopsAtLeftMarginInScrollRegion.
  ```
- [`82df0be`](https://github.com/ghostty-org/ghostty/commit/82df0be2c7522d2285187db863d62e9366fd9c4c) terminal: keep CHA, VPA, HPR and VPR origin-relative ([@jcollie](https://github.com/jcollie))
  ```text
  In origin mode setCursorPos takes coordinates relative to the scrolling
  region, but the stream handlers for CHA/HPA, VPA, HPR and VPR built them
  from the cursor's absolute screen position. The coordinate each meant to
  keep, or move relative to, then had the margin offset added a second
  time.
  
  Add setCursorRow, setCursorCol, cursorRowRelative and cursorColRelative
  to Terminal, which convert the cursor position into origin-relative
  coordinates first, as xterm's CursorRow and CursorCol do, and use them
  from both stream handlers.
  
  Fixes esctest's test_CHA_RespectsOriginMode, test_HPR_IgnoresOriginMode
  and test_VPR_IgnoresOriginMode.
  ```
- [`71c1e67`](https://github.com/ghostty-org/ghostty/commit/71c1e67a00f6919640084e9896b49354a9c9582a) terminal/kitty: address review feedback on the shm round-trip test ([@davidhodge](https://github.com/davidhodge))
  ```text
  Use bufPrintSentinel since bufPrintZ is removed in Zig 0.17. Always
  unlink the test object with a plain defer, and drop an unneeded @as.
  
  Check that the terminal unlinked the object by trying to reopen it
  rather than by unlinking it again, so the check has no side effects.
  fstat can't be used for this because macOS always reports st_nlink 0
  for shared memory objects.
  ```
- [`d7a0bd9`](https://github.com/ghostty-org/ghostty/commit/d7a0bd96fe7dfa09701bb0e768dd8bf418e1dcaa) terminal/kitty: accept shared memory names without a leading slash ([#14750](https://github.com/ghostty-org/ghostty/issues/14750)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14744
  
  Since 090fca451d, `t=s` names must start with `/` and contain no other
  `/`. A sandboxed macOS app can only create POSIX shared memory named
  `<app group id>/<name>`, with no leading slash, so every sandboxed
  client is refused with `EINVAL: invalid data`.
  
  kitty relaxed the same check in kovidgoyal/kitty@2efa09d, and the
  protocol spec now says terminals must accept names without a leading
  slash and pass them unmodified to `shm_open()`/`shm_unlink()`.
  
  `validSharedMemoryName` now only rejects empty names, names containing
  NUL, and names longer than `NAME_MAX`. Slashes are left to `shm_open`,
  because what's valid depends on the platform: Darwin's namespace is
  flat, and glibc and musl reject any slash after the leading ones. This
  matches kitty, which never checked for inner slashes. It also means
  `/a/b` is accepted again, as it was before 090fca451d. On Linux it still
  fails in `shm_open`.
  
  Tests:
  - Updated the name unit test.
  - The NUL case still goes through `LoadingImage.init` and is rejected.
  - New round-trip test: it creates a real shm object
  (`ghostty.test/shm-<pid>` on macOS, `ghostty-test-shm-<pid>` elsewhere),
  loads it with `t=s`, and checks the bytes and that the terminal unlinked
  it. It fails on main with `InvalidData`.
  
  Tested on macOS (M5, Zig 0.16.0) with `zig build test
  -Dtest-filter="shared memory"`, `-Dtest-filter=kitty` and `zig build
  test-lib-vt -Dtest-filter="shared memory"`, plus a full `zig build`. A
  small C program against libghostty-vt sends `a=t,t=s` for
  `F2RRU25WBT.sr/e2e<pid>`. With this change the image is stored with OK;
  on main it gets `EINVAL: invalid data`.
  
  AI disclosure: written with Claude Code. It wrote the fix and tests, ran
  the tests and the libghostty-vt check above, and drafted this
  description; a second Claude Code pass reviewed the diff. I reviewed and
  understand the change.
  ```
- [`7c9b7da`](https://github.com/ghostty-org/ghostty/commit/7c9b7da47f82b97c6b540d72703f7b05534dfec4) core: size click_state to hold every mouse button ([#14759](https://github.com/ghostty-org/ghostty/issues/14759)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  MouseButton.max is the largest enum value (11), not a count, so an array
  of that length has no slot for .eleven. Recording a press or release of
  button 11 indexed past the end, which panics in safe builds.
  
  Size the array max + 1 and correct the doc comment on max that suggested
  using it directly as an array length.
  
  AI disclosure: Claude Code was used in the preparation of this PR
  ```
- [`63fd4ea`](https://github.com/ghostty-org/ghostty/commit/63fd4eab8267b4f307289bbf0a9d1a4b3e35a5b8) terminal: stop CUB and BS at the left margin ([#14761](https://github.com/ghostty-org/ghostty/issues/14761)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With reverse wrap off, cursorLeft took a fast path that clamped only at
  column zero and ignored DECSLRM's left margin, so CUB and BS moved the
  cursor past it. Clamp to the left margin there as the reverse-wrap path
  and cursorRight already do, unless the cursor is already left of it.
  
  Fixes esctest's test_BS_StopsAtLeftMargin and
  test_CUB_StopsAtLeftMarginInScrollRegion.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`746c895`](https://github.com/ghostty-org/ghostty/commit/746c895c6f77a76309783fc1f05c69665219c733) terminal: keep CHA, VPA, HPR and VPR origin-relative ([#14762](https://github.com/ghostty-org/ghostty/issues/14762)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In origin mode setCursorPos takes coordinates relative to the scrolling
  region, but the stream handlers for CHA/HPA, VPA, HPR and VPR built them
  from the cursor's absolute screen position. The coordinate each meant to
  keep, or move relative to, then had the margin offset added a second
  time.
  
  Add setCursorRow, setCursorCol, cursorRowRelative and cursorColRelative
  to Terminal, which convert the cursor position into origin-relative
  coordinates first, as xterm's CursorRow and CursorCol do, and use them
  from both stream handlers.
  
  Fixes esctest's test_CHA_RespectsOriginMode, test_HPR_IgnoresOriginMode
  and test_VPR_IgnoresOriginMode.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`891a4db`](https://github.com/ghostty-org/ghostty/commit/891a4dba5757f7bd4db0e927d0d68032320783ff) formatter: restore blank cells and erased backgrounds in VT output ([#14725](https://github.com/ghostty-org/ghostty/issues/14725)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  VT output loses two kinds of blank cells, so replaying it doesn't
  recreate the original screen properly:
  
  1. **Gaps between text.** Empty cells between two pieces of text on a
  row (left by a cursor movement, for example) are written as spaces, in
  the pen of the text before them. Replaying the output turns them into
  text and paints that text's background into the gap. For example,
  `\x1b[41mred\x1b[0m\x1b[10Gplain` comes back with a red bar between the
  two words.
  2. **Cells that only have a background.** Erasing while a background
  color is set (`EL`, `ED`, `ECH`) leaves cells with no text, only a
  background color. These are written as spaces, and a row made only of
  them is treated as blank and dropped, so a full-width colored status bar
  or a cleared colored screen loses its color.
  
  TUIs are doing this all the time - think status lines, panes,
  highlighted rows in vim/nvim, Claude Code, Codex etc. They are mostly
  colored erases and gaps.
  
  ### Changes
  
  Here's what I've done:
  
  - Gaps are stepped over with CUF (`\x1b[nC`), which moves the cursor
  without writing anything, so the cells stay empty.
  - A run of cells that share one background is recreated the way it was
  made: `ECH` under that background, then CUF over the run. HTML output is
  unchanged and still writes a space in the background's style.
  - Rows of background-only cells are no longer treated as blank in VT
  output.
  - When unwrapping, blanks carried over from the end of a wrapped row
  can't be stepped over, because CUF stops at the end of the row. They are
  still written as spaces, but with the style closed first, so they no
  longer take the pen of the text before them. The same goes for an open
  hyperlink.
  
  Side effect: An open hyperlink is no longer closed and reopened around a
  gap. Why? stepping over the cells doesn't write them, so the link
  doesn't reach them. This changes the expected output of a test I added
  in #14711.
  
  ### Benchmarks
  
  The first two rows use a generated TUI-like corpus with gaps, colored
  `EL` and colored full-row clears. The last two use the output of
  `ghostty-gen +styled`, which has no gaps.
  
  | Corpus | main | this PR | Change |
  |---|---|---|---|
  | TUI-like | 3.91 ms | 3.53 ms | −9.6% |
  | TUI-like, pin map | 5.12 ms | 4.45 ms | −13% |
  | styled | 2.52 ms | 2.50 ms | about the same |
  | styled, pin map | 3.85 ms | 3.79 ms | about the same |
  
  On the TUI-like corpus the output is 21% smaller (962,370 → 762,173
  bytes), since a CUF is shorter than a run of spaces. On corpora without
  gaps or erased backgrounds the output is byte-identical to `main`.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ```
- [`c7cbc9b`](https://github.com/ghostty-org/ghostty/commit/c7cbc9bfd44cb11a9c7eae00f1166624671e363b) formatter: keep trailing blank rows in VT output without trimming ([#14766](https://github.com/ghostty-org/ghostty/issues/14766)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  VT output currently leaves out the blank rows at the end of the
  formatted range, even with trimming off. Because VT is the only output
  that gets replayed into the terminal, it means a replay without them
  scrolls less, so whenever there is scrollback the rows above them end up
  too low.
  
  For example, on a 5-row screen with three lines in scrollback,
  `\x1b[3;1H\x1b[J` (clear below the second row) leaves `4`, `5` and three
  blank rows. Replaying the VT output shows `1 2 3 4 5` instead: the three
  blank rows are missing, so `1` to `3` never scroll off. The same happens
  to a shell prompt after clearing below it and it comes back on the
  bottom row with older output above it.
  
  **Note:** this changes output for existing callers that ask for vT with
  trim off. They will now get line breaks, they didn't before. Personally,
  I think that's the right behavior, since asking for exact layout is the
  point of turning trim off and the description says so.
  
  ### Reproduce
  
  I have a small Go program using Mitchell's SDK. I can also remove the
  middle-man if desired, but I've tested and the bug occurs in `main`:
  
  ```go
  // rowsdemo shows the trailing blank rows bug in the real terminal it runs in.
  //
  //    rowsdemo           # writes the input straight to this terminal (the original)
  //    rowsdemo -replay   # feeds it to libghostty and replays the VT snapshot instead
  //
  // Both clear the screen and scrollback first, then wait for Enter.
  package main
  
  import (
        "bufio"
        "flag"
        "fmt"
        "os"
  
        "go.mitchellh.com/libghostty"
        "golang.org/x/term"
  )
  
  func main() {
        replay := flag.Bool("replay", false, "replay the VT snapshot instead of the input")
        flag.Parse()
  
        cols, rows, err := term.GetSize(int(os.Stdout.Fd()))
        check(err)
  
        // Enough output to fill the screen and push some into scrollback, then
        // clear below the second row and print a prompt, as a shell does after
        // clearing below the cursor.
        var input []byte
        for i := 1; i <= rows+10; i++ {
                input = fmt.Appendf(input, "output line %d\r\n", i)
        }
        input = append(input, "\x1b[3;1H\x1b[J$ the prompt is here"...)
  
        out := input
        if *replay {
                t, err := libghostty.NewTerminal(libghostty.WithSize(uint16(cols), uint16(row
                check(err)
                t.VTWrite(input)
                f, err := libghostty.NewFormatter(t,
                        libghostty.WithFormatterFormat(libghostty.FormatterFormatVT),
                        libghostty.WithFormatterTrim(false),
                        libghostty.WithFormatterUnwrap(false),
                        libghostty.WithFormatterExtraCursor(true),
                        libghostty.WithFormatterExtraStyle(true),
                )
                check(err)
                out, err = f.Format()
                check(err)
        }
  
        os.Stdout.WriteString("\x1b[H\x1b[2J\x1b[3J")
        os.Stdout.Write(out)
        bufio.NewReader(os.Stdin).ReadString('\n')
        os.Stdout.WriteString("\x1b[H\x1b[2J\x1b[3J")
  }
  
  func check(err error) {
        if err != nil {
                fmt.Fprintln(os.Stderr, "rowsdemo:", err)
                os.Exit(2)
        }
  }
  ```
  
  ### Benchmarks
  
  I didn't benchmark this one as the only cost is a few `\r\n` written
  once at the end of the output.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`9860397`](https://github.com/ghostty-org/ghostty/commit/98603976e9cfd643ab5dec78be5fd06ea8dbec74) build(deps): bump cachix/install-nix-action from 31.11.1 to 31.11.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.1 to 31.11.2.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/13d8dd58da0234aa297dedd986986ccb8e7f3e24...448cde739abec1eaf0646249e3d25bb8d9bc7702)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`765ea37`](https://github.com/ghostty-org/ghostty/commit/765ea37ad64f7e3a48f6ac27a70ad7fb6f31b9bb) build(deps): bump cachix/install-nix-action from 31.11.1 to 31.11.2 ([#14765](https://github.com/ghostty-org/ghostty/issues/14765)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.1 to 31.11.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.2 -&gt; 2.35.3 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/282">cachix/install-nix-action#282</a>
  <strong>Security</strong>: Fixes a number of vulnerabilities that could
  be combined to achieve root priviledge escalation.
  See <a
  href="https://discourse.nixos.org/t/security-advisory-for-nix-and-lix-october-2026/80547">https://discourse.nixos.org/t/security-advisory-for-nix-and-lix-october-2026/80547</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.1...v31.11.2">https://github.com/cachix/install-nix-action/compare/v31.11.1...v31.11.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/448cde739abec1eaf0646249e3d25bb8d9bc7702"><code>448cde7</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/282">#282</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/280a41184aaf35a185e673c5fb4412df02ee80e8"><code>280a411</code></a>
  nix: 2.35.2 -&gt; 2.35.3</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/13d8dd58da0234aa297dedd986986ccb8e7f3e24...448cde739abec1eaf0646249e3d25bb8d9bc7702">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.1&new-version=31.11.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
  Dependabot will resolve any conflicts with this PR as long as you don't
  alter it yourself. You can also trigger a rebase manually by commenting
  `@dependabot rebase`.
  
  [//]: # (dependabot-automerge-start)
  [//]: # (dependabot-automerge-end)
  
  ---
  
  <details>
  <summary>Dependabot commands and options</summary>
  <br />
  
  You can trigger Dependabot actions by commenting on this PR:
  - `@dependabot rebase` will rebase this PR
  - `@dependabot recreate` will recreate this PR, overwriting any edits
  that have been made to it
  - `@dependabot show <dependency name> ignore conditions` will show all
  of the ignore conditions of the specified dependency
  - `@dependabot ignore this major version` will close this PR and stop
  Dependabot creating any more for this major version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this minor version` will close this PR and stop
  Dependabot creating any more for this minor version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this dependency` will close this PR and stop
  Dependabot creating any more for this dependency (unless you reopen the
  PR or upgrade to it yourself)
  
  
  </details>
  ```
- [`06d872f`](https://github.com/ghostty-org/ghostty/commit/06d872fa663ba1edab65126ddbb2705c0d565468) Sync CODEOWNERS vouch list ([#14764](https://github.com/ghostty-org/ghostty/issues/14764)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @complexsplit
  - @Pugma
  ```

## October 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39163290389), [2](https://github.com/ghostty-org/ghostty/actions/runs/39155084891), [3](https://github.com/ghostty-org/ghostty/actions/runs/39146825669), [4](https://github.com/ghostty-org/ghostty/actions/runs/39104821716), [5](https://github.com/ghostty-org/ghostty/actions/runs/39100383906), [6](https://github.com/ghostty-org/ghostty/actions/runs/39100309164), [7](https://github.com/ghostty-org/ghostty/actions/runs/39098494353), [8](https://github.com/ghostty-org/ghostty/actions/runs/39084774558)  
Summary: 8 runs • 15 commits • 6 authors

### Changes

- [`72e5434`](https://github.com/ghostty-org/ghostty/commit/72e543435103cdedafb115ec690b8661fb4b6123) gtk: keep IME cursor location updated during preedit ([@moonward](https://github.com/moonward))
  ```text
  Add updateImePosition(), the only place that reports the cursor
  location to GTK.
  
  - Call updateImePosition() on preedit start/change and focus-in, in
    addition to key events.
  - Report a rectangle that spans the full cell height.
  - Correct the position from imePoint() for the gtk-xft-dpi scale.
  
  Details: https://github.com/ghostty-org/ghostty/discussions/14066
  ```
- [`6417d30`](https://github.com/ghostty-org/ghostty/commit/6417d3023e57151a2e5ec01d150b8145c9454aae) gtk: use imePointScaled to get widget coordinates ([@moonward](https://github.com/moonward))
  ```text
  Add imePointScaled(), which divides our sizes by the given scale
  instead of the content scale. imePoint() calls it with the content
  scale, so its result does not change.
  
  Make updateImePosition() call imePointScaled() with the surface scale,
  so it no longer has to undo the font DPI scale.
  ```
- [`d8619f1`](https://github.com/ghostty-org/ghostty/commit/d8619f1bce383090260221dab5f62fc953d1280b) gtk: keep IME cursor location updated during preedit on Wayland ([#14729](https://github.com/ghostty-org/ghostty/issues/14729)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR is to fix the issues of IME candidate window placement on
  Wayland as discussed in:
  
  https://github.com/ghostty-org/ghostty/discussions/14066#discussioncomment-18851489
  
  ### Fix
  Add updateImePosition() as the single place that reports the correct
  cursor location to GTK.
  Changes are:
  - Call updateImePosition() on preedit start/change and focus-in, in
  addition to key events.
  - Report a rectangle that spans full cell height so a candidate window
  flipped above the cursor does not cover the line being edited.
  - Correct the position from imePoint() for gtk-xft-dpi scale.
  
  ### Verification
  Unpatched builds reproduce the issues, and with the patch the candidate
  window appears next to the preedit without covering it, on Hyprland
  (fcitx5: mozc, hazkey, Rime), KWin (fcitx5, ibus) and GNOME (ibus), all
  on CachyOS. (refer to Examples section in the above link.)
  
  ### Related
  #13396, #13395, #5645 (X11, i3), #13015 (Xft.dpi=120). #5645 looks like
  the bottom-row case and #13015 like the text-scaling case, but I have
  not tested on a native X11 session. tomocrafter independently proposed
  the same full-cell-height change in #14267.
  
  ### AI Disclosure
  I used Claude Code (Fable 5 / Sonnet 5.5) to help with investigation,
  implementation and testing, Opus 5.5 for code review, and GPT5.6/6 sol
  for some automated tests. I reviewed the code, tested on real devices,
  and edited this text myself.
  ```
- [`189af86`](https://github.com/ghostty-org/ghostty/commit/189af86eac5e91e1b282bdaf371f369c3863591f) Update VOUCHED list ([#14760](https://github.com/ghostty-org/ghostty/issues/14760)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14755#discussioncomment-19022050)
  from @jcollie.
  
  Vouch: @aredmondd
  ```
- [`431126c`](https://github.com/ghostty-org/ghostty/commit/431126c215dc324a53ef6f054264e951a4b21604) Update VOUCHED list ([#14756](https://github.com/ghostty-org/ghostty/issues/14756)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14723#discussioncomment-19020874)
  from @pluiedev.
  
  Denounce: @gotar
  ```
- [`c8c481c`](https://github.com/ghostty-org/ghostty/commit/c8c481c1750033ad21f4f34718f5d0b1906ec251) fix(nix): prioritize pinned Zig in the macOS dev shell ([@ekusiadadus](https://github.com/ekusiadadus))
- [`d2865b8`](https://github.com/ghostty-org/ghostty/commit/d2865b8f578fa4e85e2f2b85ef97f5ef69de951f) nix: prioritize pinned Zig in the macOS dev shell ([#14692](https://github.com/ghostty-org/ghostty/issues/14692)) ([@jcollie](https://github.com/jcollie))
  ```text
  The macOS shell hook prepends Homebrew directories to PATH ahead of
  the Nix-provided tools. When Zig is also installed through Homebrew,
  the dev shell uses that version instead of the version pinned by the
  flake, which can cause builds to fail.
  
  Prepend `${zig}/bin` to PATH so the dev shell uses the project's pinned
  Zig while preserving the existing precedence for LLVM and Apple tools.
  
  Verified on macOS with Homebrew Zig 0.17.0 installed:
  - Before: `direnv exec . zig version` returned `0.17.0`.
  - After: the same command returned the pinned `0.16.0`.
  ```
- [`f44c678`](https://github.com/ghostty-org/ghostty/commit/f44c67817d1869cd1ff3cbd648552e4c7ac9ba23) Update VOUCHED list ([#14748](https://github.com/ghostty-org/ghostty/issues/14748)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14734#discussioncomment-19012178)
  from @jcollie.
  
  Vouch: @locriani
  ```
- [`0e6afb2`](https://github.com/ghostty-org/ghostty/commit/0e6afb2600d4f8be736ec94b44a21ba8d608921e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`5c93856`](https://github.com/ghostty-org/ghostty/commit/5c93856710d09f313aae515aaac207981f64a528) Update iTerm2 colorschemes ([#14740](https://github.com/ghostty-org/ghostty/issues/14740)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261012-151317-d3e95e4
  ```
- [`fb3373c`](https://github.com/ghostty-org/ghostty/commit/fb3373c8b52ffdd0669ae2d585ed0f9f7f1107fa) Update VOUCHED list ([#14747](https://github.com/ghostty-org/ghostty/issues/14747)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14690#discussioncomment-19012170)
  from @jcollie.
  
  Vouch: @Davey-Hughes
  ```
- [`8f77be7`](https://github.com/ghostty-org/ghostty/commit/8f77be73d2b525dff30f1d1a50c3523a27a3d095) Update VOUCHED list ([#14745](https://github.com/ghostty-org/ghostty/issues/14745)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14743#discussioncomment-19011080)
  from @jcollie.
  
  Vouch: @zzznu
  ```
- [`71970ee`](https://github.com/ghostty-org/ghostty/commit/71970eee87936dfe16ccc7cddceee07fcc7aa64b) Update VOUCHED list ([#14746](https://github.com/ghostty-org/ghostty/issues/14746)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14742#discussioncomment-19011082)
  from @jcollie.
  
  Vouch: @davidhodge
  ```
- [`23dd1b7`](https://github.com/ghostty-org/ghostty/commit/23dd1b723e8314e34f56042e2af1e7653f47b2e5) gtk: stop progress bar pulse animation ([@dkinzler](https://github.com/dkinzler))
  ```text
  Fixes #14704.
  
  Explicitly stop the pulse animation when the progress bar of a Surface
  widget is removed. Previously its tick callback kept running and
  continuously queued redraws. This kept the GTK main loop busy even when
  the progress bar was not visible and the window not focused.
  ```
- [`73e4ff1`](https://github.com/ghostty-org/ghostty/commit/73e4ff10fb2b30d1ab6e6f7f52ef33f3a0593dcc) gtk: stop progress bar pulse animation ([#14738](https://github.com/ghostty-org/ghostty/issues/14738)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14704.
  
  Explicitly stop the pulse animation when the progress bar of a Surface
  widget is removed. Previously its tick callback kept running and
  continuously queued redraws. This kept the GTK main loop busy even when
  the progress bar was not visible and the window not focused.
  
  The issue can be reproduced by sending ConEmu OSC 9;4 progress reports.
  First one with state "undetermined" (`printf '\e]9;4;3\e\x5c'`) to show
  the progress bar and start the pulse animation, then one with "inactive"
  (`printf '\e]9;4;0\e\x5c'`) to remove it. Unfocus the window and observe
  the amount of main loop iterations e.g. with debug logs in the `run`
  function in `apprt/gtk/class/application.zig`. With the fix there is ~1
  iteration per second, without it there are lots.
  
  AI Disclosure: no AI used on this one.
  ```

## October 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38951024014), [2](https://github.com/ghostty-org/ghostty/actions/runs/38943108606), [3](https://github.com/ghostty-org/ghostty/actions/runs/38936269574)  
Summary: 3 runs • 3 commits • 3 authors

### Changes

- [`e3ebb1d`](https://github.com/ghostty-org/ghostty/commit/e3ebb1d1bf772cf5d1bc70b5ae19e6943e33a110) Catalan translation of command palette ([#13776](https://github.com/ghostty-org/ghostty/issues/13776)) ([@francescarpi](https://github.com/francescarpi))
- [`22d623f`](https://github.com/ghostty-org/ghostty/commit/22d623f38aeea55deb6191ca64c7b9d02922980e) I18n: update `id_ID` translations for v1.4 ([#13905](https://github.com/ghostty-org/ghostty/issues/13905)) ([@halosatrio](https://github.com/halosatrio))
- [`949149d`](https://github.com/ghostty-org/ghostty/commit/949149d5791a0eb08412ad05cd8fd484ad134481) i18n: complete missing Japanese translations ([#14575](https://github.com/ghostty-org/ghostty/issues/14575)) ([@ekusiadadus](https://github.com/ekusiadadus))
  ```text
  Fill 181 untranslated entries while preserving existing translations.
  Validate the catalog against the current template with gettext.
  ```

## October 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38812465411), [2](https://github.com/ghostty-org/ghostty/actions/runs/38705285984), [3](https://github.com/ghostty-org/ghostty/actions/runs/38683778451), [4](https://github.com/ghostty-org/ghostty/actions/runs/38680434974)  
Summary: 4 runs • 9 commits • 6 authors

### Changes

- [`508cfad`](https://github.com/ghostty-org/ghostty/commit/508cfade5e5f62a3ee35b65938c7080de19f4441) benchmark: convert prints to log ([@jcollie](https://github.com/jcollie))
  ```text
  Zig really doesn't like tests to print anything to stderr while
  running tests. Convert some stray std.debug.print statements into log
  statements. Log statements below `warn` will be suppressed when running
  tests, keeping Zig happy.
  ```
- [`b3dc3d7`](https://github.com/ghostty-org/ghostty/commit/b3dc3d794513c11633e7c3347935693957744e83) benchmark: convert prints to log ([#14718](https://github.com/ghostty-org/ghostty/issues/14718)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig really doesn't like tests to print anything to stderr while running
  tests. Convert some stray std.debug.print statements into log
  statements. Log statements below `warn` will be suppressed when running
  tests, keeping Zig happy.
  ```
- [`22fa134`](https://github.com/ghostty-org/ghostty/commit/22fa134a07f5749edd9e92c6bc17d8aaf61843be) Update VOUCHED list ([#14722](https://github.com/ghostty-org/ghostty/issues/14722)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14721#discussioncomment-18944491)
  from @trag1c.
  
  Denounce: @KooshaPari
  ```
- [`510b253`](https://github.com/ghostty-org/ghostty/commit/510b253dbc52d77b9f842ab6b8cba9ef046cea11) formatter: emit the hyperlinks of cells in VT output ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output only emitted the cursor's hyperlink (with the hyperlink extra),
  not the hyperlinks of text on the screen, so replaying it lost them. HTML
  output already wraps linked cells in anchors.
  
  Emit OSC 8 around linked cells in VT output, with the explicit id when
  there is one, using the same transition tracking as HTML. Opening a
  hyperlink replaces the open one, so the close is only written when no
  hyperlink follows. Blank cells have no hyperlink, so an open hyperlink is
  closed before the spaces written for them. Pages without hyperlinks, the
  common case, take a copy of the cell run loop that never checks for them.
  ```
- [`a2e4403`](https://github.com/ghostty-org/ghostty/commit/a2e440396403385680008e456a741a7776091412) formatter: emit the hyperlinks of cells in VT output ([#14711](https://github.com/ghostty-org/ghostty/issues/14711)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  VT output drops the hyperlinks of text on the screen, so replaying it
  loses them and the hyperlink extra only restores the cursor's open
  hyperlink. The HTML output already wraps linked cells in anchors and
  I've found a comment in the formatter notes that VT should do the same
  with OSC 8.
  
  This PR emits OSC 8 around linked cells in VT output, using the same
  transition tracking as HTML:
  
  - The explicit id is kept when there is one (`OSC 8 ; id=… ; URI ST`).
  - A hyperlink stays open across line breaks, so a link that continues on
  the next row is written once.
  - Blank cells have no hyperlink, so an open one is closed before the
  spaces written for them. Otherwise, the spaces would come back linked.
  - Opening a hyperlink replaces the open one, so switching between two
  links writes no close.
  - Pages without hyperlinks use a copy of the cell run loop that never
  checks for them.
  
  Cell hyperlinks are emitted like cell styles (always in VT, like HTML).
  I've left it so the `hyperlink` extra still covers only the cursor's
  hyperlink, the same way `style` only covers the cursor's style. This
  means "copy as VT" and `write_screen_file` with VT now include links. If
  you'd rather they be opt-in, then I can put them behind an option.
  
  ### Reproduction
  
  Small C program:
  
  ```c
  // libghostty-vt's VT formatter drops the hyperlinks (OSC 8) of text.
  #include <stdio.h>
  #include <ghostty/vt.h>
  
  int main(void) {
    GhosttyTerminal t;
    ghostty_terminal_new(NULL, &t, 20, 2);
  
    const char in[] = "\x1b]8;;https://example.com\x1b\\link\x1b]8;;\x1b\\ text";
    ghostty_terminal_vt_write(t, (const uint8_t *)in, sizeof(in) - 1);
  
    GhosttyFormatterTerminalOptions opts = {
        .size = sizeof(opts),
        .emit = GHOSTTY_FORMATTER_FORMAT_VT,
        .trim = true,
        .extra = {.size = sizeof(opts.extra),
                  .screen = {.size = sizeof(opts.extra.screen)}},
    };
    GhosttyFormatter f;
    ghostty_formatter_terminal_new(NULL, &f, t, opts);
    uint8_t buf[256];
    size_t len;
    ghostty_formatter_format_buf(f, buf, sizeof(buf), &len);
  
    // Print the output with ESC visible.
    for (size_t i = 0; i < len; i++) {
      if (buf[i] == 0x1b) fputs("\\e", stdout);
      else putchar(buf[i]);
    }
    putchar('\n');
    return 0;
  }
  ```
  
  ```sh
  zig build -Demit-lib-vt -Demit-xcframework=false --prefix out
  cc -o repro repro.c -Iout/include out/lib/libghostty-vt.a && ./repro
  ```
  
  Before: `link text`
  After: `\e]8;;https://example.com\e\link\e]8;;\e\ text`
  
  ### Benchmarks
  
  Note: Things get slower, but the cost only applies to linked text. On
  the `0.5` corpus, a third of it is one hyperlink lookup per linked cell,
  a tenth is the OSC 8 output, and the rest is leaving the fast cell loop
  at each link's start and end. Handling link changes inside the fast loop
  is measured as slower. Removing the lookups would take a per-page array
  of hyperlink ids, which seemed like too much for this PR.
  `--mode=roundtrip` gives `equal=true` for every corpus.
  
  I ran `ghostty-bench +terminal-formatter --formatter=terminal`, on 640
  KB `ghostty-gen +styled` corpora, with `--osc8-rate` setting how many
  cells are linked. Time per format, from `hyperfine` (main run twice
  agreed within 0.5%):
  
  | Corpus | VT output | main | this PR | Change |
  |---|---|---|---|---|
  | No hyperlinks | unchanged | 2.50 ms | 2.54 ms | +1.5% |
  | `--osc8-rate=0.1` | +19% bytes | 2.06 ms | 3.17 ms | +54% |
  | `--osc8-rate=0.5` | +69% bytes | 1.39 ms | 3.03 ms | +118% |
  | `--osc8-rate=0.5`, `--pin-map=true` | +68% bytes | 2.12 ms | 4.02 ms |
  +89% |
  
  One known limit: an implicit hyperlink that is closed and reopened,
  around a gap or at a page boundary, comes back as two implicit
  hyperlinks with the same URI.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`9689532`](https://github.com/ghostty-org/ghostty/commit/9689532cfff16b486eeab69c2194c7b3e3797c3a) core: report the release of a tracked click on a prompt ([@fornwall](https://github.com/fornwall))
  ```text
  When the cursor is at a prompt that declared click_events=1 or cl=,
  a left release ran the prompt click before the mouse report. Under
  mouse tracking the press had already been reported, so the release
  was replaced by a synthetic SGR press or arrow keys. Ghostty's own
  shell integration hits this whenever a widget runs a mouse-tracking
  program from the prompt, such as fzf's Ctrl-R binding.
  
  The selection gesture is reset when a press is reported, so a zero
  click count on release means the press reached the program. Skip the
  prompt click then and report the release too. Shift+click under
  tracking still records a gesture and moves the cursor.
  ```
- [`5dd2ee1`](https://github.com/ghostty-org/ghostty/commit/5dd2ee119db9d65aefc65fce830bbc69f55b17b2) build(deps): bump actions/create-github-app-token from 3.2.0 to 3.3.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 3.2.0 to 3.3.0.
  - [Release notes](https://github.com/actions/create-github-app-token/releases)
  - [Changelog](https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/create-github-app-token/compare/bcd2ba49218906704ab6c1aa796996da409d3eb1...64ab729a6294000f5aa4a4bc0b73d1f32bc45510)
  
  ---
  updated-dependencies:
  - dependency-name: actions/create-github-app-token
    dependency-version: 3.3.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`9d1b234`](https://github.com/ghostty-org/ghostty/commit/9d1b234d97469b821dc6223bb9bcfdff7d625611) build(deps): bump actions/create-github-app-token from 3.2.0 to 3.3.0 ([#14713](https://github.com/ghostty-org/ghostty/issues/14713)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
  from 3.2.0 to 3.3.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.3.0</h2>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.2.0...v3.3.0">3.3.0</a>
  (2026-10-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e">a47236f</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb">12461a3</a>)</li>
  <li><strong>deps:</strong> bump the production-dependencies group across
  1 directory with 3 updates (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/395">#395</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807">a69c19d</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md">actions/create-github-app-token's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.2.0...v3.3.0">3.3.0</a>
  (2026-10-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e">a47236f</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb">12461a3</a>)</li>
  <li><strong>deps:</strong> bump the production-dependencies group across
  1 directory with 3 updates (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/395">#395</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807">a69c19d</a>)</li>
  </ul>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.1.1...v3.2.0">3.2.0</a>
  (2026-05-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>add support for enterprise-level GitHub Apps (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/263">#263</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/952a2a7073df6bfa5f49bc469ec895b6ec1acea4">952a2a7</a>)</li>
  <li>support full repository names in <code>repositories</code> input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/372">#372</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/85eb8dd41472213aed25d1a126460e0069138ab6">85eb8dd</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump <code>@​actions/core</code> from 3.0.0
  to 3.0.1 in the production-dependencies group (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/364">#364</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/43e5c345bfd4d4f3ecea019ad0042001a09dd857">43e5c34</a>)</li>
  <li>validate private-key input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/376">#376</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/f24bbd89643991c0de27ae823c01791b2c6bafdd">f24bbd8</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/64ab729a6294000f5aa4a4bc0b73d1f32bc45510"><code>64ab729</code></a>
  chore(main): release 3.3.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/402">#402</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/f3a828e4b91180d3a46ac1f4b43fa8384b0dea07"><code>f3a828e</code></a>
  ci: create signed dist commits in release workflow (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/404">#404</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/655017ffa7c6b0c6e4210729fa6bce35cacd8ca0"><code>655017f</code></a>
  docs: clarify when owner grants access to all repositories (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/378">#378</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb"><code>12461a3</code></a>
  fix(deps): bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e"><code>a47236f</code></a>
  feat: update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807"><code>a69c19d</code></a>
  fix(deps): bump the production-dependencies group across 1 directory
  with 3 u...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/d5cb7ae41d64331820d88810a4878e0942ec992a"><code>d5cb7ae</code></a>
  build(deps): bump actions/checkout from 6 to 7 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/384">#384</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/575da866bd0a42d7f234a8645831d55573252b09"><code>575da86</code></a>
  build(deps): bump stefanzweifel/git-auto-commit-action from 7.1.0 to
  7.2.0 in...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/e85f677b44da0d1f08115ce52cdfd8fd2c69874a"><code>e85f677</code></a>
  test: omit stack traces from snapshots (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/401">#401</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/9419396df4d5672241cfb593dadc19758e54a204"><code>9419396</code></a>
  build(deps-dev): bump c8 from 11.0.0 to 12.0.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/400">#400</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/create-github-app-token/compare/bcd2ba49218906704ab6c1aa796996da409d3eb1...64ab729a6294000f5aa4a4bc0b73d1f32bc45510">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=3.2.0&new-version=3.3.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
  Dependabot will resolve any conflicts with this PR as long as you don't
  alter it yourself. You can also trigger a rebase manually by commenting
  `@dependabot rebase`.
  
  [//]: # (dependabot-automerge-start)
  [//]: # (dependabot-automerge-end)
  
  ---
  
  <details>
  <summary>Dependabot commands and options</summary>
  <br />
  
  You can trigger Dependabot actions by commenting on this PR:
  - `@dependabot rebase` will rebase this PR
  - `@dependabot recreate` will recreate this PR, overwriting any edits
  that have been made to it
  - `@dependabot show <dependency name> ignore conditions` will show all
  of the ignore conditions of the specified dependency
  - `@dependabot ignore this major version` will close this PR and stop
  Dependabot creating any more for this major version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this minor version` will close this PR and stop
  Dependabot creating any more for this minor version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this dependency` will close this PR and stop
  Dependabot creating any more for this dependency (unless you reopen the
  PR or upgrade to it yourself)
  
  
  </details>
  ```
- [`a9139e5`](https://github.com/ghostty-org/ghostty/commit/a9139e56c3e99209648d25063c60c4c9f61b3645) core: report the release of a tracked click on a prompt ([#14710](https://github.com/ghostty-org/ghostty/issues/14710)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the cursor is at a prompt with click-to-move (OSC 133
  [click_events](https://sw.kovidgoyal.net/kitty/shell-integration/#notes-for-shell-developers)
  or
  [cl=](https://gitlab.freedesktop.org/Per_Bothner/specifications/blob/master/proposals/semantic-prompts.md))
  and a program started from that prompt tracks the mouse, a left click
  reaches the program as a press without a release (the release is instead
  replaced by the prompt click).
  
  A release whose press went to the program now goes to the program too,
  instead of becoming a prompt click.
  
  Steps to reproduce:
  1. Use [ghostty shell
  integration](https://ghostty.org/docs/features/shell-integration).
  2. Use [fzf shell
  integration](https://junegunn.github.io/fzf/shell-integration/#setting-up-shell-integration),
  for example `source <(fzf --zsh)` under zsh. Tested with zsh; bash uses
  the same `cl=line` mark and fish uses `click_events=1`, so both should
  take the same path.
  3. Press `Ctrl-R` to open the fzf history search.
  4. Double click on a history item to select it.
  
  Results:
  - Before: The history item is not inserted into the shell prompt, since
  fzf only completes a double click on the release event it never
  receives.
  - After: The history item is inserted into the shell prompt.
  
  AI disclosure: Created with opus 5.5 through claude code. Reviewed and
  tested by me.
  ```

## October 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38633740617), [2](https://github.com/ghostty-org/ghostty/actions/runs/38631379696), [3](https://github.com/ghostty-org/ghostty/actions/runs/38542450833), [4](https://github.com/ghostty-org/ghostty/actions/runs/38515836993)  
Summary: 4 runs • 31 commits • 6 authors

### Changes

- [`f2571a3`](https://github.com/ghostty-org/ghostty/commit/f2571a3ec1ee8d77473a12f96c1a5eae63ba06d9) termio: synchronize pty and terminal resizing ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  #14701
  
  Hold the terminal state lock before resizing the pty. This prevents shell redraws triggered by SIGWINCH from being parsed before the terminal dimensions are updated.
  ```
- [`ad97d33`](https://github.com/ghostty-org/ghostty/commit/ad97d331459a0762f7aea5f56fe86748e03b860f) termio: synchronize pty and terminal resizing ([#14706](https://github.com/ghostty-org/ghostty/issues/14706)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Hold the terminal state lock before resizing the pty. This prevents
  shell redraws triggered by SIGWINCH from being parsed before the
  terminal dimensions are updated.
  
  Part of #14701
  AI disclosure: GPT-6 Astra helped to debug the issue and fix it.
  
  Related discussion:
  https://github.com/ghostty-org/ghostty/discussions/13629
  ```
- [`079f5d2`](https://github.com/ghostty-org/ghostty/commit/079f5d2025ef6d654989ddbadad1d72c49528bbd) osc: rename context signal to hierarchical context (HC) ([@paaloeye](https://github.com/paaloeye))
  ```text
  Rename context signal to hierarchical context (HC) across the OSC parser,
  terminal stream, and C headers to align naming with the UAPI
  spec. Update identifiers, parser namespaces, and tests accordingly.
  
  Per spec, _signal_ is a possible field in the _end_ sequence.
  Besides that, _signal_ could be confused with POSIX signals.
  
  Ref: https://uapi-group.org/specifications/specs/osc_context/
  
  AI Disclosure: Initially drafted by 🤖 Antigravity CLI 1.3.3 🧠 Google Gemini 3.8 Flash (Medium).
  Iterated, reviewed, and tested by me.
  ```
- [`049014d`](https://github.com/ghostty-org/ghostty/commit/049014df16c49d0e313f2bcb3fb62edd62fab8f2) gtkNg → gtk: eliminate the last vestiges of the great rewrite ([@jcollie](https://github.com/jcollie))
- [`9573ecd`](https://github.com/ghostty-org/ghostty/commit/9573ecd0307327b4b79f859198c796c8fdec608a) gtk: bump the required blueprint compiler version to 0.20 ([@jcollie](https://github.com/jcollie))
- [`97fb364`](https://github.com/ghostty-org/ghostty/commit/97fb3640294c0faa1ef2fd798eeaa63ef894ca34) gtk: enforce minimum versions of gtk and libadwaita. gobject bindings are required. ([@jcollie](https://github.com/jcollie))
- [`9ae5fb0`](https://github.com/ghostty-org/ghostty/commit/9ae5fb04eb81db9b3905d558cd8482d5b8b68db8) gtk: drop the pre-1.5 Adwaita dialog fallbacks ([@jcollie](https://github.com/jcollie))
  ```text
  Ghostty 1.4 requires libadwaita 1.7, so the AdwMessageDialog shim and the
  blueprint variants behind it were dead. They also cost a warning on every
  build: blueprint-compiler counts an import as used only when a type name
  mentions it, so the Adw import that the `responses` block needs to
  typecheck against an extern parent was reported as unused.
  ```
- [`9b7a4d5`](https://github.com/ghostty-org/ghostty/commit/9b7a4d54075913017ae4a0fb9234b37ff13d2785) gtk: finish removing the pre-1.7 Adwaita branches ([@jcollie](https://github.com/jcollie))
  ```text
  The build only refused libadwaita older than the newest blueprint, so the
  1.7 floor went unenforced and the branches below it stayed reachable on
  paper: a GtkAboutDialog for pre-1.5, and an empty child-exited widget that
  made libghostty fall back to the text message for pre-1.3.
  ```
- [`f6b89be`](https://github.com/ghostty-org/ghostty/commit/f6b89be89f2c2c100a4ea5f51f8c3616c24e764e) gtk: remove anything that was conditional on no-longer-supported versions ([@jcollie](https://github.com/jcollie))
- [`1ae5da9`](https://github.com/ghostty-org/ghostty/commit/1ae5da994a3ef2da369cde70f9cd9dc1967ebb3e) gtk: file each blueprint under the libadwaita it actually needs ([@jcollie](https://github.com/jcollie))
  ```text
  The directory names the oldest libadwaita a blueprint compiles against,
  but most were filed under the version that happened to be current when
  they were written. Ten need nothing newer than 1.0, and the two using
  AdwToolbarView need 1.4.
  ```
- [`128d4b3`](https://github.com/ghostty-org/ghostty/commit/128d4b3e1c41c01f5aa58497e19f90ca3e14b7d7) gtk: sort list of blueprints ([@jcollie](https://github.com/jcollie))
- [`e7348d6`](https://github.com/ghostty-org/ghostty/commit/e7348d658092b9d54c195c565f445cae147f90cc) gtk: update translations ([@jcollie](https://github.com/jcollie))
  ```text
  Note: There are no new messages to be translated. The messages just
  moved to different line numbers or were the original file was renamed.
  ```
- [`2fa57fc`](https://github.com/ghostty-org/ghostty/commit/2fa57fc45fc8f3f813347fa1c211278d920de4ac) osc: rename context signal to hierarchical context (HC) ([#14700](https://github.com/ghostty-org/ghostty/issues/14700)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename context signal to hierarchical context (HC) across the OSC
  parser, terminal stream, and C headers to align naming with the UAPI
  spec. Update identifiers, parser namespaces, and tests accordingly.
  
  Per spec, _signal_ is a possible field in the _end_ sequence. Besides
  that, _signal_ could be confused with POSIX signals.
  
  Ref: https://uapi-group.org/specifications/specs/osc_context/
  
  AI Disclosure: Initially drafted by 🤖 Antigravity CLI 1.3.3 🧠 Google
  Gemini 3.8 Flash (Medium). Iterated, reviewed, and tested by me.
  ```
- [`0711907`](https://github.com/ghostty-org/ghostty/commit/0711907b2026c1a0590c32aa5e606494ab5a46d8) Update VOUCHED list ([#14709](https://github.com/ghostty-org/ghostty/issues/14709)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14708#discussioncomment-18933493)
  from @jcollie.
  
  Vouch: @Pyre909
  ```
- [`81c344b`](https://github.com/ghostty-org/ghostty/commit/81c344bf311ac643f17109d54b126d123665abba) Require GTK 4.18 and libadwaita 1.7 ([#14330](https://github.com/ghostty-org/ghostty/issues/14330)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Debian 13 has [GTK 4.18](https://packages.debian.org/source/stable/gtk4)
  and [libadwaita
  1.7](https://packages.debian.org/source/stable/libadwaita-1). This PR
  remove any code or workarounds for any previous versions. There are
  still places where we have code conditioned on GTK or libadwaita
  versions, but only for newer versions.
  
  AI disclosure: Claude Code was used for some of the larger mechanical
  edits.
  ```
- [`b9bc79d`](https://github.com/ghostty-org/ghostty/commit/b9bc79de252c4ee0920454ce607790eccbf5e261) Add config option to move the close button position ([@ollieatkinson](https://github.com/ollieatkinson))
- [`b327d8d`](https://github.com/ghostty-org/ghostty/commit/b327d8d8eb689f43fe0b9684088478985dec4083) feedback, move to window, add to overview ([@ollieatkinson](https://github.com/ollieatkinson))
- [`1eccd66`](https://github.com/ghostty-org/ghostty/commit/1eccd66c3c42404e8f781811f8cf26606d51d1a1) formatting... ([@ollieatkinson](https://github.com/ollieatkinson))
- [`f781b42`](https://github.com/ghostty-org/ghostty/commit/f781b42db0f02c76e1f6d1ecb236392c6b69054d) improve doc comment and add availbility ([@ollieatkinson](https://github.com/ollieatkinson))
- [`3474a57`](https://github.com/ghostty-org/ghostty/commit/3474a576fda2a2f7b11ecde6e4c560f9c2d7e0e6) zig fmt ([@ollieatkinson](https://github.com/ollieatkinson))
- [`9ba928a`](https://github.com/ghostty-org/ghostty/commit/9ba928a3df1985e05a081f8d2418a6a77ed322a5) trailing comma ([@ollieatkinson](https://github.com/ollieatkinson))
- [`291fd05`](https://github.com/ghostty-org/ghostty/commit/291fd050b9e9c293c8adb6a140742649b7e42d3a) gtk: Add config option to move the position of the close button ([#14657](https://github.com/ghostty-org/ghostty/issues/14657)) ([@jcollie](https://github.com/jcollie))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/14649
  
  | | `inverted: false` | `inverted: true` |
  | - | - | - |
  | **overview** | <img width="824" height="472"
  alt="01-inverted-false-overview"
  src="https://github.com/user-attachments/assets/9cf58ed6-7864-4006-9e4b-ec7865df367b"
  /> | <img width="824" height="472" alt="03-inverted-true-overview"
  src="https://github.com/user-attachments/assets/2ba3d9d1-2777-4618-b4e6-9bfce9a3af94"
  /> |
  | **tab** | <img width="824" height="472" alt="02-inverted-false-tabs"
  src="https://github.com/user-attachments/assets/d7d0aea4-16cf-4b61-a983-c127017f9875"
  /> | <img width="824" height="472" alt="04-inverted-true-tabs"
  src="https://github.com/user-attachments/assets/342a6cc2-9f8a-44d5-9ebb-e29b8d36eb01"
  /> |
  
  I used codex to help me figure out where the changes needed to be made,
  I added the code and comments myself
  ```
- [`8b7a2d6`](https://github.com/ghostty-org/ghostty/commit/8b7a2d6fb49d79badcf0557d38c6af9e5520b775) gtk: clear surface notifications on focus and close ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  GTK notifications previously used their body as the GApplication ID and
  weren't tracked after delivery. As a result, they could remain visible
  after the originating surface was focused or closed.
  
  Derive stable IDs from the surface ID and notification content, and keep
  a bounded per-surface tracker so notifications can be withdrawn. Clear
  them on focus and disposal, and expire notifications delivered to an
  already-focused surface after three seconds to match macOS behavior.
  
  Keep the existing surface activation target and add unit coverage for
  replacement, eviction, removal, and independent surface tracking.
  ```
- [`44ebe02`](https://github.com/ghostty-org/ghostty/commit/44ebe02ed60589098d3bbf6299e50006228eade2) gtk: clean up notification tracking ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Moved notification tracking out of surface.zig and it now uses an array hash map to keep the implementation simpler.
  ```
- [`051e4ba`](https://github.com/ghostty-org/ghostty/commit/051e4bacfd3a2c0178cc98ea2b8d8129352e434c) gtk: move notification handling out of surface.zig ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Keep sending, tracking, timers, and cleanup together in desktop_notifications.zig. Simplify the map helpers and IDformatting, and include the module's tests in the GTK test suite.
  ```
- [`1da6610`](https://github.com/ghostty-org/ghostty/commit/1da6610ebde4c935f2fad4c1530f7e7e18a061f6) gtk: clear surface notifications on focus and close ([@EriksRemess](https://github.com/EriksRemess))
- [`ec353ec`](https://github.com/ghostty-org/ghostty/commit/ec353ec7f8debae031fced89c48679140c8f6066) gtk: send notifications even when tracking fails ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Continue sending notifications if tracking fails, logging the error instead of dropping the notification. Only schedule a timeout when tracking succeeds.
  ```
- [`dfac443`](https://github.com/ghostty-org/ghostty/commit/dfac44398a6a5203f4358cc3ea54fb44222d49e4) gtk: simplify desktop notification tracking ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Store notification hashes and optional timers in an ArrayList instead of copying titles and bodies into a deque.
  ```
- [`ce63844`](https://github.com/ghostty-org/ghostty/commit/ce638447a2efbf3a753d1f489d13e85fd7642a7a) gtk: simplify notification hashing and cleanup ([@EriksRemess](https://github.com/EriksRemess))
- [`5415ed5`](https://github.com/ghostty-org/ghostty/commit/5415ed541d55583bc6d905e536c4de3a4afe173a) gtk: fix desktop notification test expectations ([@EriksRemess](https://github.com/EriksRemess))
- [`9f13eb7`](https://github.com/ghostty-org/ghostty/commit/9f13eb7526cc070a2b829f2aae41a44d5cce12bf) gtk: clear surface notifications on focus and close ([#14108](https://github.com/ghostty-org/ghostty/issues/14108)) ([@jcollie](https://github.com/jcollie))
  ```text
  GTK notifications could remain visible after their originating surface
  was focused or closed. macOS already clears them in these cases.
  This tracks notifications per surface and withdraws them on focus or
  close. Notifications sent while the surface is already focused are
  removed after three seconds, just like on macOS.
  Repeated notifications with the same text replace each other, while
  notifications from different surfaces remain independent. Clicking a
  notification still focuses the originating surface.
  
  AI disclosure: Codex 5.6 Sol helped with most of the implementation.
  ```

