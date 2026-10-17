> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 17, 2026 at 17:42 UTC.

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

## October 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38485309003), [2](https://github.com/ghostty-org/ghostty/actions/runs/38469057359), [3](https://github.com/ghostty-org/ghostty/actions/runs/38466036257), [4](https://github.com/ghostty-org/ghostty/actions/runs/38440102147), [5](https://github.com/ghostty-org/ghostty/actions/runs/38436006247), [6](https://github.com/ghostty-org/ghostty/actions/runs/38420934652), [7](https://github.com/ghostty-org/ghostty/actions/runs/38416363692), [8](https://github.com/ghostty-org/ghostty/actions/runs/38414684379), [9](https://github.com/ghostty-org/ghostty/actions/runs/38331089399)  
Summary: 9 runs • 53 commits • 12 authors

### Changes

- [`ffaaf5d`](https://github.com/ghostty-org/ghostty/commit/ffaaf5d7a9951886d72f2c0dd8ba7380c1aea92c) renderer: only start and stop the CVDisplayLink on the main thread ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  The render thread started and stopped its CVDisplayLink directly.
  Turns out this is NOT SAFE TO DO!
  
  I actually couldn't find any docs or anything to point this out to me
  and I had to rely on Fable-assistance disassembling CoreVideo frameworks
  to confirm the behavior. I read the disassembly myself and can confirm
  the reading matches what I'd see.
  
  CoreVideo performs the very same stop and start on the main thread
  inside its display reconfiguration callback, which fires on display sleep
  and wake, resolution changes, etc.
  
  CVDisplayLinkStop clears the link's running flag and then waits, once
  and unconditionally, for the IO thread to notice and exit. The link's
  mutex is released during that wait. If CVDisplayLinkStart lands in
  that window, the flag is set again and a second IO thread is created.
  The first IO thread wakes, sees the flag set, and keeps looping, so
  the waiting stop is never signaled. Whichever side lost was stuck in
  CVDisplayLinkStop forever.
  
  In the reports that was sometimes our render thread and sometimes
  CoreVideo's own call on the main thread. Either way the main thread
  eventually waited on the renderer (focus change, tab close, quit) and the
  whole app froze with no "Not Responding" indication. The spindumps all show
  one CVDisplayLink object with two live IO threads, which is exactly this
  problem.
  ```
- [`8159838`](https://github.com/ghostty-org/ghostty/commit/81598385d608dda4946093d6d6a234d204a2f225) renderer: only start and stop the CVDisplayLink on the main thread ([#14691](https://github.com/ghostty-org/ghostty/issues/14691)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  The render thread started and stopped its CVDisplayLink directly. Turns
  out this is NOT SAFE TO DO!
  
  I actually couldn't find any docs or anything to point this out to me
  and I had to rely on Fable-assistance disassembling CoreVideo frameworks
  to confirm the behavior. I read the disassembly myself and can confirm
  the reading matches what I'd see.
  
  CoreVideo performs the very same stop and start on the main thread
  inside its display reconfiguration callback, which fires on display
  sleep and wake, resolution changes, etc.
  
  CVDisplayLinkStop clears the link's running flag and then waits, once
  and unconditionally, for the IO thread to notice and exit. The link's
  mutex is released during that wait. If CVDisplayLinkStart lands in that
  window, the flag is set again and a second IO thread is created. The
  first IO thread wakes, sees the flag set, and keeps looping, so the
  waiting stop is never signaled. Whichever side lost was stuck in
  CVDisplayLinkStop forever.
  
  In the reports that was sometimes our render thread and sometimes
  CoreVideo's own call on the main thread. Either way the main thread
  eventually waited on the renderer (focus change, tab close, quit) and
  the whole app froze with no "Not Responding" indication. The spindumps
  all show one CVDisplayLink object with two live IO threads, which is
  exactly this problem.
  ```
- [`0c234a0`](https://github.com/ghostty-org/ghostty/commit/0c234a04d86fddc252dab727eb550ec3c304155e) macos: refuse to execute files with control characters in the path ([@mitchellh](https://github.com/mitchellh))
  ```text
  Opening a file with Ghostty, such as with `open -a Ghostty <file>`,
  runs it by typing its shell-quoted path into a new terminal as
  `initialInput`.
  
  This meant a file named `/tmp/Foo<Ctrl-U>ls<CR>` showed up as
  `/tmp/Fools` in the confirmation dialog, but clicking Allow erased the
  quoted path with Ctrl-U and ran `ls` with CR instead. Anything that can
  get Ghostty to open a crafted filename could run an arbitrary command
  behind a misleading confirmation.
  
  Files whose path contains a Unicode control character (U+0000 to
  U+001F, U+007F, and U+0080 to U+009F) are now rejected with an alert
  before the confirmation is shown. No legitimate file needs these, and
  there's no shell-agnostic way to escape them for typed input.
  ```
- [`827d5c8`](https://github.com/ghostty-org/ghostty/commit/827d5c82944a5ec7cf3f5b7594a223f9648c94f3) macos: refuse to execute files with control characters in the path ([#14688](https://github.com/ghostty-org/ghostty/issues/14688)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Opening a file with Ghostty, such as with `open -a Ghostty <file>`, runs
  it by typing its shell-quoted path into a new terminal as
  `initialInput`.
  
  This meant a file named `/tmp/Foo<Ctrl-U>ls<CR>` showed up as
  `/tmp/Fools` in the confirmation dialog, but clicking Allow erased the
  quoted path with Ctrl-U and ran `ls` with CR instead. Anything that can
  get Ghostty to open a crafted filename could run an arbitrary command
  behind a misleading confirmation.
  
  Files whose path contains a Unicode control character (U+0000 to U+001F,
  U+007F, and U+0080 to U+009F) are now rejected with an alert before the
  confirmation is shown. No legitimate file needs these, and there's no
  shell-agnostic way to escape them for typed input.
  ```
- [`f3b16bd`](https://github.com/ghostty-org/ghostty/commit/f3b16bd57761ca390c8199146b749e340fa82572) chore: ensure afl-out exists on build and update build configs ([@paaloeye](https://github.com/paaloeye))
  ```text
  Create the afl-out directory during build initialization so that AFL++
  has an existing destination directory ready for fuzzing session outputs.
  
  Bump minimum_zig_version to 0.16.0 in build.zig.zon (s) to stay in sync with
  the root repository requirement, and update the Homebrew installation
  command in the README to reference the current afl++ formula name.
  ```
- [`f9e8ef0`](https://github.com/ghostty-org/ghostty/commit/f9e8ef02d7d20b79a4a27966e08ed3ddf0f3c57b) macos: treat links from unknown sources as untrusted ([@mitchellh](https://github.com/mitchellh))
  ```text
  Links found by the `link` config (including the default URL regex) were
  sent to the apprt as `unknown` and opened directly with NSWorkspace.
  
  This meant a program could print
  `file:///System/Applications/Calculator.app` and a Cmd+click on it would
  launch Calculator, while the same target as an OSC 8 hyperlink was
  blocked.
  
  The `unknown` kind is now untrusted.
  ```
- [`b612e5b`](https://github.com/ghostty-org/ghostty/commit/b612e5be664e0bdb77375a588e0622236671cfce) build: capture blueprint-compiler's stderr ([@jcollie](https://github.com/jcollie))
  ```text
  Zig 0.16 records anything a run step writes to an uncaptured stderr as
  a diagnostic and fails the step, even when the command exits zero.
  blueprint-compiler 0.20 warns about unused imports and about
  Gtk.ShortcutLabel being deprecated, so every build from a clean cache
  failed in the blueprint step; a warm cache hid it.
  
  Capture the stderr instead. It is still reported when the compiler
  exits nonzero, so a real error in a blueprint shows its message.
  ```
- [`3485823`](https://github.com/ghostty-org/ghostty/commit/34858233fbfa114ac108e7ab41e4cc06efb589ba) pkg/dcimgui: build the test from the public module ([@jcollie](https://github.com/jcollie))
  ```text
  The test made a module of its own from main.zig and never gave it the
  dcimgui_c import, so `zig build test` in pkg/dcimgui failed with "no
  module named 'dcimgui_c'". Use the public module, which already has
  that import, the build options and the library.
  ```
- [`d3906ef`](https://github.com/ghostty-org/ghostty/commit/d3906efe4b62c7bafec570d8271a4d07d7291d48) ci: test pkg/dcimgui alongside pkg/wuffs ([@jcollie](https://github.com/jcollie))
  ```text
  Its test never compiled, and nothing ran it to notice.
  ```
- [`5b41979`](https://github.com/ghostty-org/ghostty/commit/5b4197989bbf1101f6c88a293f03be695522b4f9) ci: also test pkg/dcimgui with -Dfreetype=true ([@jcollie](https://github.com/jcollie))
  ```text
  That is how Ghostty builds it, and it compiles and links code the
  default build leaves out. The matrix moves to include entries so that a
  package can carry build arguments.
  ```
- [`7597e85`](https://github.com/ghostty-org/ghostty/commit/7597e85fd0c9c46716632c1a744f13690c1a3572) build: capture blueprint-compiler's stderr ([#14684](https://github.com/ghostty-org/ghostty/issues/14684)) ([@jcollie](https://github.com/jcollie))
  ```text
  Zig 0.16 records anything a run step writes to an uncaptured stderr as a
  diagnostic and fails the step, even when the command exits zero.
  blueprint-compiler 0.20 warns about unused imports and about
  Gtk.ShortcutLabel being deprecated, so every build from a clean cache
  failed in the blueprint step; a warm cache hid it.
  
  Capture the stderr instead. It is still reported when the compiler exits
  nonzero, so a real error in a blueprint shows its message.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`0125483`](https://github.com/ghostty-org/ghostty/commit/0125483678f4d08c4fc87c454665cb4500620f26) macos: treat links from unknown sources as untrusted ([#14683](https://github.com/ghostty-org/ghostty/issues/14683)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Links found by the `link` config (including the default URL regex) were
  sent to the apprt as `unknown` and opened directly with NSWorkspace.
  
  This meant a program could print
  `file:///System/Applications/Calculator.app` and a Cmd+click on it would
  launch Calculator, while the same target as an OSC 8 hyperlink was
  blocked.
  
  The `unknown` kind is now untrusted.
  ```
- [`cdb19b2`](https://github.com/ghostty-org/ghostty/commit/cdb19b2775097e5180c935374ffae3f31f0bb196) dcimgui: run pkg tests in CI ([#14685](https://github.com/ghostty-org/ghostty/issues/14685)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `dcimgui`'s tests were never run in CI, so they bitrotted.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`a939f77`](https://github.com/ghostty-org/ghostty/commit/a939f771d92d89d16ad7376187e3ec7dda61d191) chore: ensure afl-out exists on build and update build configs ([#14677](https://github.com/ghostty-org/ghostty/issues/14677)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Create the afl-out directory during build initialization so that AFL++
  has an existing destination directory ready for fuzzing session outputs.
  
  Bump minimum_zig_version to 0.16.0 in build.zig.zon (s) to stay in sync
  with the root repository requirement, and update the Homebrew
  installation command in the README to reference the current afl++
  formula name.
  ```
- [`65ff54c`](https://github.com/ghostty-org/ghostty/commit/65ff54c67df3d55e3ebf4dd31c7afa93c4cfb922) terminal: fix use-after-free when scrollback prunes the cursor page ([@mitchellh](https://github.com/mitchellh))
  ```text
  On a one row screen, a line feed at the bottom could free the page the
  cursor was on while the cursor still pointed into it. `PageList.grow`
  enforces the scrollback line limit right after adding the new row, and
  with only one row the old cursor row is already history at that point,
  so its page can be pruned before `cursorDownScroll` moves the cursor.
  The tracked cursor pin moved to the new page, but `cursorDownScroll`
  then took its same-page fast path and marked the cached `page_row`
  dirty, writing into freed memory. The cursor style and hyperlink IDs
  also still referred to the pruned page.
  
  Terminal output alone can trigger this when a scrollback line limit is
  set. For example, reflowing a long hyperlinked line wider can produce a
  page that holds more rows than the limit allows, and filling it with
  line feeds frees it.
  
  Debug builds segfault in `cursorMarkDirty` and release builds write to
  freed memory.
  
  Even without the crash, the next print would use style and hyperlink IDs
  that don't exist on the new page. Larger screens aren't affected because
  the old cursor row is still in the active area after growing, and pruning
  stops at the page containing the active top. Ghostty itself would need
  `scrollback-limit-lines` set and a surface that is one row tall.
  
  Fix this by rebuilding the cursor state on the new page when its page is
  pruned, without touching the old page. `Screen.increaseCapacity` already
  does this when it replaces the cursor page, so its logic moves into a
  shared `cursorPageReplaced` helper. This also clears the garbage flag
  that pruning sets on the cursor pin, since the pin now points exactly
  where the cursor belongs.
  
  Found by a reporter fuzzing libghostty-vt.
  ```
- [`5c9a3d8`](https://github.com/ghostty-org/ghostty/commit/5c9a3d8a90592e85069213489e203fbcdbdc5d67) input: paste protection treats carriage returns like newlines ([@mitchellh](https://github.com/mitchellh))
  ```text
  A user who pastes attacker-controlled text ending in a carriage return
  into a shell without bracketed paste mode executes it without the
  expected confirmation. B
  
  `isSafe` now rejects `\r` as well as `\n` when unbracketed. Inside a
  bracketed paste a carriage return remains fine, the same as a newline.
  This matches the other terminals that warn on multi-line pastes: iTerm2
  and Windows Terminal both search for `\r` or `\n`, and kitty's
  `confirm` paste action flags `\r` as a dangerous C0 code.
  
  Found by a reporter.
  ```
- [`7db25f9`](https://github.com/ghostty-org/ghostty/commit/7db25f9f3df8032b72f80a2aec76046933ed7199) terminal: fix use-after-free when scrollback prunes the cursor page ([#14686](https://github.com/ghostty-org/ghostty/issues/14686)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On a one row screen, a line feed at the bottom could free the page the
  cursor was on while the cursor still pointed into it. `PageList.grow`
  enforces the scrollback line limit right after adding the new row, and
  with only one row the old cursor row is already history at that point,
  so its page can be pruned before `cursorDownScroll` moves the cursor.
  The tracked cursor pin moved to the new page, but `cursorDownScroll`
  then took its same-page fast path and marked the cached `page_row`
  dirty, writing into freed memory. The cursor style and hyperlink IDs
  also still referred to the pruned page.
  
  Terminal output alone can trigger this when a scrollback line limit is
  set. For example, reflowing a long hyperlinked line wider can produce a
  page that holds more rows than the limit allows, and filling it with
  line feeds frees it.
  
  Debug builds segfault in `cursorMarkDirty` and release builds write to
  freed memory.
  
  Even without the crash, the next print would use style and hyperlink IDs
  that don't exist on the new page. Larger screens aren't affected because
  the old cursor row is still in the active area after growing, and
  pruning stops at the page containing the active top. Ghostty itself
  would need `scrollback-limit-lines` set and a surface that is one row
  tall.
  
  Fix this by rebuilding the cursor state on the new page when its page is
  pruned, without touching the old page. `Screen.increaseCapacity` already
  does this when it replaces the cursor page, so its logic moves into a
  shared `cursorPageReplaced` helper. This also clears the garbage flag
  that pruning sets on the cursor pin, since the pin now points exactly
  where the cursor belongs.
  
  Found by a reporter fuzzing libghostty-vt.
  ```
- [`cc53940`](https://github.com/ghostty-org/ghostty/commit/cc53940b4cf97876e48826e5d825833a77471c89) input: paste protection treats carriage returns like newlines ([#14687](https://github.com/ghostty-org/ghostty/issues/14687)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A user who pastes attacker-controlled text ending in a carriage return
  into a shell without bracketed paste mode executes it without the
  expected confirmation. B
  
  `isSafe` now rejects `\r` as well as `\n` when unbracketed. Inside a
  bracketed paste a carriage return remains fine, the same as a newline.
  This matches the other terminals that warn on multi-line pastes: iTerm2
  and Windows Terminal both search for `\r` or `\n`, and kitty's `confirm`
  paste action flags `\r` as a dangerous C0 code.
  
  Found by a reporter.
  ```
- [`539689a`](https://github.com/ghostty-org/ghostty/commit/539689a33bfe045db9da45b336014960b27e7d0e) pkg/dcimgui: link a system freetype through the module ([@jcollie](https://github.com/jcollie))
  ```text
  With freetype from the system, the static dcimgui library was given
  -lfreetype directly. Zig 0.16 then puts libfreetype.so into
  libdcimgui.a, and the final link of ghostty fails on that archive
  member, so any build with -fsys=freetype or --system failed from a
  clean cache.
  
  The static library now gets only freetype's include paths from
  pkg-config, and the shared library is linked through the dcimgui
  module and its test instead.
  ```
- [`f659a86`](https://github.com/ghostty-org/ghostty/commit/f659a86e00260f51937d26190f6d1c8af26ba4b2) snap: use the system freetype, fontconfig, harfbuzz, libpng and zlib ([@jcollie](https://github.com/jcollie))
  ```text
  The snap built without --system, so it statically linked the vendored
  copies of these libraries while GTK loaded Ubuntu's into the same
  process. Build against the system libraries instead; GTK already
  brings their runtime packages into the snap.
  ```
- [`5580df6`](https://github.com/ghostty-org/ghostty/commit/5580df6022d5597e3070370e4b5b2665703b849b) macos: apply paste protection to dragged text ([@mitchellh](https://github.com/mitchellh))
  ```text
  Dragging text into a macOS terminal surface sent it without any paste
  protection. Text containing newlines went straight to the shell with
  no "Potentially Unsafe Paste" prompt, even though pasting the same text
  with Cmd-V would have asked first.
  ```
- [`1a93d53`](https://github.com/ghostty-org/ghostty/commit/1a93d5395071e7fb4a65447d02a7d591f2e8ccf5) terminal/tmux: ignore out of bounds scroll regions in pane state ([@mitchellh](https://github.com/mitchellh))
- [`c440e5b`](https://github.com/ghostty-org/ghostty/commit/c440e5b9467b358e61687f54e86a9c1296b9286c) macos: apply paste protection to dragged text ([#14679](https://github.com/ghostty-org/ghostty/issues/14679)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Dragging text into a macOS terminal surface sent it without any paste
  protection. Text containing newlines went straight to the shell with no
  "Potentially Unsafe Paste" prompt, even though pasting the same text
  with Cmd-V would have asked first.
  ```
- [`bc2cf6f`](https://github.com/ghostty-org/ghostty/commit/bc2cf6fd7946146e5c264332ea5dd825e51020a9) terminal/tmux: ignore out of bounds scroll regions in pane state ([#14680](https://github.com/ghostty-org/ghostty/issues/14680)) ([@mitchellh](https://github.com/mitchellh))
- [`1f80eec`](https://github.com/ghostty-org/ghostty/commit/1f80eec05f24e1ba108d466fb59360729f15c9c2) snap/dcimgui: use system libraries rather than building static vendored libs ([#14682](https://github.com/ghostty-org/ghostty/issues/14682)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  snaps have been building the vendored freetype/fontconfig libraries and
  linking them statically. As seen in non-snap builds, this is problematic
  because GTK links to the system shared libraries. Having two copies
  running at the same time causes crashes as the libraries fight each
  other in memory that they share.
  
  Also fixes a related problem that `dcimgui` would get `libfreetype.so`
  copied into it's static library when built against the system shared
  libraries.
  
  Related to: #14392
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`8a7a91f`](https://github.com/ghostty-org/ghostty/commit/8a7a91fbd6c8220e978cc96bfeef1b8686ed1e3f) terminal/tmux: preserve parser state across output notifications ([@ekusiadadus](https://github.com/ekusiadadus))
- [`f033764`](https://github.com/ghostty-org/ghostty/commit/f033764d7d9d13d31a3b99b725c479e081e0bc64) terminal/tmux: merge main and retain both test suites ([@ekusiadadus](https://github.com/ekusiadadus))
- [`97a2ca6`](https://github.com/ghostty-org/ghostty/commit/97a2ca6ee2b553ea239eda4f89be40f652ed3188) terminal/tmux: preserve parser state across output notifications ([#14676](https://github.com/ghostty-org/ghostty/issues/14676)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The tmux viewer creates a new VT stream for each output notification.
  An escape sequence split across notifications therefore loses its
  partially parsed state. For example, `ESC[32` followed by `mX` should
  produce a green `X`, just like receiving `ESC[32mX` in one notification.
  
  Related to #1935. This isolates the persistent parser-state work
  discussed
  in #11219:
  
  https://github.com/ghostty-org/ghostty/pull/11219#issuecomment-6116176355
  
  ## Related work
  
  #12076 handles octal decoding of control-mode output. This change
  handles
  VT parsing state across already-decoded output notifications.
  
  ## AI disclosure
  
  I used OpenAI Codex for code walkthroughs, implementation guidance,
  review, cleanup, and validation.
  ```
- [`44c4c8f`](https://github.com/ghostty-org/ghostty/commit/44c4c8f55d49e124f19492402a993978949f1326) terminal/kitty: bound memory retained by repeated walias updates ([@mitchellh](https://github.com/mitchellh))
  ```text
  Every OSC 5522 `walias` packet copied its target MIME type into the
  write transaction's arena. Overwriting an existing alias pointed it at
  the new copy, but an arena can't free the old one, so it stayed
  allocated until the transaction ended.
  
  A program could open a write transaction, never commit it, and send
  `walias` packets for the same alias forever. Each packet retained up to
  256 bytes, outside of `clipboard-write-limit-bytes`, which only counts
  decoded clipboard data. Memory grew without bound for as long as the
  transaction stayed open.
  
  Each alias now stores its target in an inline buffer of `max_mime_len`
  bytes that is overwritten on update. Combined with the existing limit
  of 64 aliases, this caps alias target storage at 16 KiB per
  transaction, and it is all freed when the transaction ends.
  ```
- [`66a01d4`](https://github.com/ghostty-org/ghostty/commit/66a01d4f17bd13cdc44da0fbcf69b97fd4a49a27) terminal/kitty: bound memory retained by repeated walias updates ([#14678](https://github.com/ghostty-org/ghostty/issues/14678)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Every OSC 5522 `walias` packet copied its target MIME type into the
  write transaction's arena. Overwriting an existing alias pointed it at
  the new copy, but an arena can't free the old one, so it stayed
  allocated until the transaction ended.
  
  A program could open a write transaction, never commit it, and send
  `walias` packets for the same alias forever. Each packet retained up to
  256 bytes, outside of `clipboard-write-limit-bytes`, which only counts
  decoded clipboard data. Memory grew without bound for as long as the
  transaction stayed open.
  
  Each alias now stores its target in an inline buffer of `max_mime_len`
  bytes that is overwritten on update. Combined with the existing limit of
  64 aliases, this caps alias target storage at 16 KiB per transaction,
  and it is all freed when the transaction ends.
  ```
- [`d432b01`](https://github.com/ghostty-org/ghostty/commit/d432b01a3e10eb396a54d94ea42a95381d482915) terminal: report unsupported ANSI modes as permanently reset in DECRQM ([@deblasis](https://github.com/deblasis))
  ```text
  DECRQM on an ANSI mode Ghostty does not implement answered not_recognized (0), so the twelve permanently-reset esctest cases fail expecting 4. Fixed-reset behavior matches xterm: GATM, SRTM, VEM, HEM, PUM, FEAM, FETM, MATM, TTM, SATM, TSM and EBM now report permanently_reset, next to the existing DECECM 117 special case.
  ```
- [`b21f82c`](https://github.com/ghostty-org/ghostty/commit/b21f82c0eaebadc222ad112c192bd8e8bd927ec8) terminal: assert permanently-reset ANSI modes stay out of the mode table ([@deblasis](https://github.com/deblasis))
- [`19a14dd`](https://github.com/ghostty-org/ghostty/commit/19a14dda360ff69eec184abe3655ef526cac898f) terminal: fix unsupp. ANSI modes as permanently reset in DECRQM ([#14672](https://github.com/ghostty-org/ghostty/issues/14672)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Twelve esctest DECRQM cases fail: ANSI modes Ghostty doesn't implement
  answer not_recognized (0) where the tests expect permanently_reset (4).
  
  xterm reports these fixed-reset. This extends the existing DECECM 117
  special case in getReport to GATM, SRTM, VEM, HEM, PUM, FEAM, FETM,
  MATM, TTM, SATM, TSM and EBM. Settable ANSI modes and the DEC side are
  untouched.
  
  Measured with esctest locally: all twelve pass, full tally 385 passed /
  140 failed against 373 / 152 on current main, no new failures. zig fmt
  --check clean; zig build test-lib-vt passes.
  
  Developed using a mix of agents: glm-5.3, muse 1.3, opus 5.5.
  ```
- [`cd432ba`](https://github.com/ghostty-org/ghostty/commit/cd432ba5cb820544fee1f1303b9d50e1f9a0edb6) terminal/kitty: accept /private/tmp for temporary files on macOS ([@magnussp](https://github.com/magnussp))
  ```text
  On macOS /tmp is a symlink to /private/tmp. Temporary file paths are
  checked in canonical form, so a t=t file in /tmp resolves to
  /private/tmp/... and never matched the /tmp root, and was rejected as
  not in a temp dir. Accept /private/tmp as a platform specific temporary
  directory on Darwin, as the protocol allows.
  ```
- [`46d6c3b`](https://github.com/ghostty-org/ghostty/commit/46d6c3b508fcc3ad2182a6b8c75490b6f91e5fe1) terminal: unescape metadata fields in context signal parser ([@paaloeye](https://github.com/paaloeye))
  ```text
  Per the UAPI.15 OSC 3008 specification, metadata field values can
  escape semicolons and backslashes using `\x3b` and `\x5c` respectively.
  Previously, the parser returned raw string slices directly, which did
  not unescape these byte sequences.
  
  Introduce `UnescapedString` representing a lazily unescaped string slice,
  with an iterator to decode escape sequences on the fly, equality
  comparison, and an allocating conversion helper.
  
  Unit test covering metadata fields with semicolons and backslashes.
  
  AI Disclosure: Initially drafted by 🤖 Antigravity CLI 1.3.3 🧠 Google Gemini 3.8 Flash (Medium).
  Iterated, reviewed, and tested by me.
  
  Agent-Session: 97ccdb8b-15c3-4d9b-9324-59cbb7c6d335
  ```
- [`bae1c01`](https://github.com/ghostty-org/ghostty/commit/bae1c01fc919e0cef911322b3dfd4e0859236531) formatter: restore a pending wrap over a blank cell ([@robmorgan](https://github.com/robmorgan))
  ```text
  The VT formatter restores a pending wrap by moving to the right edge and
  reprinting the cell under the cursor. A blank cell formats to nothing, so
  the wrap was lost and the next character overwrote the last column instead
  of wrapping. The cursor can be over a blank cell with a wrap pending when a
  saved cursor is restored after the line was erased (ESC 7, CSI 2 K, ESC 8).
  
  For a blank cell, print a space to set the wrap, then save the cursor,
  erase the space and restore the cursor, which leaves the wrap pending over
  a blank cell again. This replaces the saved cursor, which the formatter
  does not emit.
  ```
- [`58d23cc`](https://github.com/ghostty-org/ghostty/commit/58d23cc026286f714fbbb9d1c0db13f1005345d8) formatter: restore a pending wrap over a blank cell ([#14670](https://github.com/ghostty-org/ghostty/issues/14670)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  The VT formatter restores a pending wrap by moving to the right edge and
  reprinting the cell under the cursor, since CUP would clear the wrap.
  When that cell happens to be blank, it formats to nothing, so the wrap
  is lost. After replaying the output, the next character overwrites the
  last column instead of starting the next row.
  
  The cursor can sit over a blank cell with a wrap pending when a saved
  cursor is restored after its line was erased (`ESC 7`, `CSI 2 K`, `ESC
  8`).
  
  I've changed it to print a space in place of a blank cell, then save the
  cursor (via `DECSC`), erase the space (`ECH`, which clears the wrap),
  and finally restore the cursor (with `DECRC`). The latter leaves the
  wrap pending over a blank cell. This means the cell stays empty, so
  formatting the restored terminal gives the same output. This replaces
  the saved cursor, which the formatter doesn't omit.
  
  Note: I've tried to match xterm, which saves and restores the pending
  wrap with the cursor and clears it on ECH and EL.
  
  ### Reproduction
  
  Here's a small C program built on libghostty-vt. The bug only shows with
  the cursor extra, which the Ghostty app never turns on.
  
  ```c
  // libghostty-vt's VT formatter loses a pending wrap over a blank cell.
  #include <stdio.h>
  #include <ghostty/vt.h>
  
  int main(void) {
    GhosttyTerminal source, target;
    ghostty_terminal_new(NULL, &source, 4, 2);
    ghostty_terminal_new(NULL, &target, 4, 2);
  
    // Wrap pending at the right edge, cursor saved (ESC 7), line erased,
    // cursor restored (ESC 8): the wrap is pending over a blank cell.
    const char in[] = "abcd\x1b" "7\x1b[2K\x1b" "8";
    ghostty_terminal_vt_write(source, (const uint8_t *)in, sizeof(in) - 1);
  
    // Format it as VT with the cursor, then replay that into another terminal.
    GhosttyFormatterTerminalOptions opts = {
        .size = sizeof(opts),
        .emit = GHOSTTY_FORMATTER_FORMAT_VT,
        .extra = {.size = sizeof(opts.extra),
                  .screen = {.size = sizeof(opts.extra.screen), .cursor = true}},
    };
    GhosttyFormatter f;
    ghostty_formatter_terminal_new(NULL, &f, source, opts);
    uint8_t buf[64];
    size_t len;
    ghostty_formatter_format_buf(f, buf, sizeof(buf), &len);
    ghostty_terminal_vt_write(target, buf, len);
  
    bool before, after;
    ghostty_terminal_get(source, GHOSTTY_TERMINAL_DATA_CURSOR_PENDING_WRAP, &before);
    ghostty_terminal_get(target, GHOSTTY_TERMINAL_DATA_CURSOR_PENDING_WRAP, &after);
    printf("pending wrap: source %d, restored %d\n", before, after);
    return before != after;
  }
  ```
  
  Compile it with:
  
  ```sh
  zig build -Demit-lib-vt -Demit-xcframework=false --prefix out
  cc -o repro repro.c -Iout/include out/lib/libghostty-vt.a && ./repro
  ```
  
  Before: `pending wrap: source 1, restored 0`
  After: `pending wrap: source 1, restored 1`
  
  ### Benchmarks
  
  Since binary snapshot codecs skip the formatter, the only relevant
  benchmark here is `terminal-formatter` with `--formatter=terminal` and
  VT output with every extra. I've done ReleaseFast, hyperfine with 20
  runs, on a 640 KB `ghostty-gen +styled` corpus ending in each cursor
  state, plus the reproduction's input alone with 20,000 formats per run:
  
  | Input | main | this PR |
  |---|---|---|
  | No pending wrap | 50.5 ± 1.2 ms | 49.6 ± 1.1 ms |
  | Pending wrap over text | 49.2 ± 0.6 ms | 50.2 ± 1.5 ms |
  | Pending wrap over a blank cell | 50.4 ± 2.4 ms | 49.1 ± 1.1 ms |
  | Reproduction input, 20,000 formats | 209.6 ± 1.5 ms | 211.4 ± 19.5 ms
  |
  
  The change only runs when the cursor has a wrap pending over a blank
  cell, once per format. `--mode=roundtrip` is `equal=true` for every
  input.
  
  ### Tests
  
  I've added 2 new tests:
  
  - A pending wrap over a blank cell (fails without the fix). It also
  checks that the restored cell stays empty, that formatting the restored
  terminal gives the same output, and that the next character lands in the
  same place.
  - A pending wrap after a wide character, which already worked.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`3fe938d`](https://github.com/ghostty-org/ghostty/commit/3fe938dbc899ea26de09f5f4b14fc3634c951372) terminal/kitty: accept /private/tmp for temporary files on macOS ([#14569](https://github.com/ghostty-org/ghostty/issues/14569)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14567
  
  On macOS `/tmp` is a symlink to `/private/tmp`. Temporary-file (`t=t`)
  paths are checked in canonical form, so a file in `/tmp` resolves to
  `/private/tmp/...`, never matches the `/tmp` root, and is rejected with
  `EINVAL: temporary file not in temp dir`. Only files under `$TMPDIR`
  worked.
  
  This accepts `/private/tmp` as a platform specific temporary directory
  on Darwin, which the protocol allows ("... `/tmp`, `/dev/shm`, `TMPDIR`
  env var if present and any platform specific temporary directories").
  The `isPathInDir` component-boundary check (so `/private/tmp-evil` is
  still rejected), the `tty-graphics-protocol` name check and the `/proc`,
  `/sys`, `/dev` exclusions are unchanged. Other platforms are unaffected.
  
  Test: macOS only, a file in the real `/tmp` loads and is deleted. It
  fails with `TemporaryFileNotInTempDir` without this change.
  
  Tested on macOS 15 (M1 Pro) with `zig build test-lib-vt
  -Dtest-filter="image load"`.
  
  AI disclosure: written with Claude Code, which found the cause, wrote
  the fix and test, and drafted this description; the approach was revised
  after review. I reviewed and understand the change and verified it
  locally.
  ```
- [`554ea65`](https://github.com/ghostty-org/ghostty/commit/554ea65867ffe34bb3e51e09bd016e154a1f9d7a) terminal: unescape metadata fields in context signal parser ([#14667](https://github.com/ghostty-org/ghostty/issues/14667)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Per the UAPI.15 OSC 3008 specification, metadata field values can escape
  semicolons and backslashes using `\x3b` and `\x5c` respectively.
  Previously, the parser returned raw string slices directly, which did
  not unescape these byte sequences.
  
  Introduce `UnescapedString` representing a lazily unescaped string
  slice, with an iterator to decode escape sequences on the fly, equality
  comparison, and an allocating conversion helper.
  
  Unit test covering metadata fields with semicolons and backslashes.
  
  AI Disclosure: Initially drafted by 🤖 Antigravity CLI 1.3.3 🧠 Google
  Gemini 3.8 Flash (Medium). Iterated, reviewed, and tested by me.
  ```
- [`6f3a4fa`](https://github.com/ghostty-org/ghostty/commit/6f3a4fade09d502f694e29fd352cf340d8c75543) terminal/snapshot: validate page capacity hints against max page size ([@Huge](https://github.com/Huge))
  ```text
  The PAGE record payload header contains dimensions and capacity hints
  (columns, rows, styles, hyperlink bytes, grapheme bytes, string bytes).
  Header.pageCapacity() validated non-zero columns and rows, but did not
  verify whether the resulting TerminalPageCapacity exceeds max_page_size.
  
  When unvalidated values (such as grapheme_capacity_bytes = maxInt(u32)
  or string_capacity_bytes = maxInt(u32)) are passed to TerminalPage.init(),
  the page layout exceeds the maximum architectural page size and causes
  an integer overflow panic in OffsetBuf.member during page initialization.
  
  Validate the requested capacity using TerminalPage.layout(cap) in
  Header.pageCapacity(), returning error.PageTooLarge if total_size
  exceeds max_page_size. Add a regression test covering oversized grapheme,
  string, hyperlink, and grid dimensions.
  
  Reported-by: BS.ehlas.cz
  ```
- [`44bdcc6`](https://github.com/ghostty-org/ghostty/commit/44bdcc623f1afa1a6a3970d6a78352b82ef6cb26) macos: add "Close Split" to right-click context menu ([@cmwetherell](https://github.com/cmwetherell))
  ```text
  Add a "Close Split" option to the right-click context menu, allowing
  users to close the focused split pane directly from the context menu.
  ```
- [`ff77956`](https://github.com/ghostty-org/ghostty/commit/ff779564c61de312d402c152c6842f73d3269898) terminal: ED2 at a prompt skips blank rows when finding the prompt ([@jcollie](https://github.com/jcollie))
  ```text
  `ESC [ 2 J` scrolls the screen into scrollback instead of erasing it
  when the last non-empty row of the active area is a prompt, so that ^L
  at a prompt keeps the prior output (#905). Since the row semantic
  prompt state was reduced to none/prompt/prompt_continuation, blank rows
  and command output rows are both `.none`, and the search stopped at the
  first blank row below the prompt. The heuristic therefore only worked
  when the prompt was on the last row of the screen.
  
  Skip rows without text while searching upward so that only a non-empty
  row without prompt cells ends the search.
  
  Fixes: #14660
  Discussion: #14659
  ```
- [`fbda61b`](https://github.com/ghostty-org/ghostty/commit/fbda61b873da5208475c183af160d131ac7a77a3) terminal: answer DECXCPR extended cursor position (CSI ? 6 n) ([@deblasis](https://github.com/deblasis))
  ```text
  CSI ? 6 n was ignored, so DECDSRTests.test_DECDSR_DECXCPR times out waiting for a reply. Answer CSI ? row ; col ; 1 R with the origin-mode-relative position. Ghostty has no page memory, so page is always 1.
  
  Both reply paths (C-API and app) share a small position helper, and the DSR table gains the question-form entry.
  ```
- [`2d2ceb0`](https://github.com/ghostty-org/ghostty/commit/2d2ceb0f8b957eec2d54b6c2808b9a344fc7327e) gtk,opengl: reuse GTK's EGL display when possible ([@pluiedev](https://github.com/pluiedev))
  ```text
  This is to avoid situations where we pick a different GPU from what GTK
  is using and incur massive performance penalties as a result of
  incompatible DMABUF modifiers (you can't manually select the underlying
  texture layout with only OpenGL APIs, either).
  
  See also #14568 which is a similar but arguably much hackier way to do
  this.
  ```
- [`968b2bf`](https://github.com/ghostty-org/ghostty/commit/968b2bf195c73d9889c25faa8e9fbb55b6843625) feat: restore the active screen from pane state ([@ekusiadadus](https://github.com/ekusiadadus))
- [`52f7969`](https://github.com/ghostty-org/ghostty/commit/52f7969ab954896f5798289134997e5271251488) terminal: ED2 at a prompt skips blank rows when finding the prompt ([#14668](https://github.com/ghostty-org/ghostty/issues/14668)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `ESC [ 2 J` scrolls the screen into scrollback instead of erasing it
  when the last non-empty row of the active area is a prompt, so that ^L
  at a prompt keeps the prior output (#905). Since the row semantic prompt
  state was reduced to none/prompt/prompt_continuation, blank rows and
  command output rows are both `.none`, and the search stopped at the
  first blank row below the prompt. The heuristic therefore only worked
  when the prompt was on the last row of the screen.
  
  Skip rows without text while searching upward so that only a non-empty
  row without prompt cells ends the search.
  
  Fixes: #14660
  Discussion: #14659
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`4cd0eb5`](https://github.com/ghostty-org/ghostty/commit/4cd0eb5c18eaf6fdf92b316dc15ada25c167ae59) gtk,opengl: reuse GTK's EGL display when possible ([#14636](https://github.com/ghostty-org/ghostty/issues/14636)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is to avoid situations where we pick a different GPU from what GTK
  is using and incur massive performance penalties as a result of
  incompatible DMABUF modifiers (you can't manually select the underlying
  texture layout with only OpenGL APIs, either).
  
  See also #14568 which is a similar but arguably much hackier way to do
  this.
  ```
- [`32d7741`](https://github.com/ghostty-org/ghostty/commit/32d77414a9cf87e2fb4e79bed27a022097c2e1c5) terminal/snapshot: validate page capacity hints against maximum page size ([#14595](https://github.com/ghostty-org/ghostty/issues/14595)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### Summary
  
  The `PAGE` record payload header includes cell dimensions and
  preallocation hints for the decoded page:
  - `columns` (`u16`)
  - `rows` (`u16`)
  - `style_capacity` (`u16`)
  - `hyperlink_capacity_bytes` (`u16`)
  - `grapheme_capacity_bytes` (`u32`)
  - `string_capacity_bytes` (`u32`)
  
  While `Header.pageCapacity()` previously checked that `columns != 0` and
  `rows != 0`, it did not validate whether the resulting
  `TerminalPageCapacity` fits within the architectural page limit
  `max_page_size`.
  
  ### Root Cause & Impact
  
  When an unvalidated or untrusted payload declares oversized hints (such
  as `grapheme_capacity_bytes = maxInt(u32)` or `string_capacity_bytes =
  maxInt(u32)` or large dimensions), passing this capacity to
  `TerminalPage.init(capacity)` causes
  `TerminalPage.layout(capacity).total_size` to exceed `max_page_size`.
  
  During page initialization in `initBuf`, calculating member offsets
  (`buf.member`) attempts to cast the offset to `OffsetInt` (`u32`).
  Because the offset exceeds `max_page_size`, this triggers an integer
  overflow panic (`integer does not fit in destination type`), terminating
  the process with `SIGABRT`. Similarly, when restoring pages in
  `history.zig` or `screen.zig`, `allocatePage` triggers
  `assert(layout.total_size <= size.max_page_size)`.
  
  ### Fix
  
  1. Add `error.PageTooLarge` to `Header.CapacityError`.
  2. In `Header.pageCapacity()`, compute `TerminalPage.layout(cap)` and
  return `error.PageTooLarge` if `page_layout.total_size > max_page_size`.
  3. Add a regression test in `page.zig` verifying that oversized grapheme
  capacity, string capacity, hyperlink capacity, and dimension hints are
  rejected with `error.PageTooLarge`.
  
  ### Testing
  
  - Verified regression test reproduced the integer overflow panic on the
  unpatched codebase and passes with the fix applied.
  - Added specific test case isolating `hyperlink_capacity_bytes` where
  the grid dimensions fit on their own but exceed `max_page_size` once
  hyperlink capacity is included.
  - Full `test-lib-vt` suite passes (`zig build test-lib-vt`).
  - Formatted and verified with `zig fmt --check
  src/terminal/snapshot/page.zig`.
  
  AI disclosure: written with assistance of Antigravity, which helped
  draft the regression test and fix. Reviewed, verified, and tested on
  Linux (AMD Zen 4) and macOS.
  ```
- [`94ec54a`](https://github.com/ghostty-org/ghostty/commit/94ec54af914021184c6d4c61f4f636d723b29936) macOS: Improve Split Close Behavior ([#11174](https://github.com/ghostty-org/ghostty/issues/11174)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  ## Summary
  - Adds a "Close Split" option to the right-click context menu
  - Adds a `closeSurface` action that triggers `close_surface` via the
  binding action system
  
  Reference discussion:
  https://github.com/ghostty-org/ghostty/discussions/10982
  ```
- [`0550d04`](https://github.com/ghostty-org/ghostty/commit/0550d04894198f4bb922fa2958d7d47e7fdaab42) terminal: answer DECXCPR extended cursor position (CSI ? 6 n) ([#14673](https://github.com/ghostty-org/ghostty/issues/14673)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Thomas Dickey's esctest run in CI has DECDSRTests.test_DECDSR_DECXCPR
  failing: CSI ? 6 n gets no reply, so the test times out waiting.
  
  This answers CSI ? row ; col ; 1 R with the origin-mode-relative cursor
  position. Terminals without page memory report page 1, matching xterm.
  The DSR table gains the question-form entry, and both reply paths share
  a position helper with CPR.
  
  Measured with esctest locally: the test passes, full tally 374 passed /
  151 failed against 373 / 152 on current main, no new failures. zig fmt
  --check clean; zig build test-lib-vt passes.
  
  Developed using a mix of agents: glm-5.3, muse 1.3, opus 5.5.
  ```
- [`adbcb3d`](https://github.com/ghostty-org/ghostty/commit/adbcb3da673407ab79254620536c909b23e32419) terminal/tmux: restore the active screen from pane state ([#14671](https://github.com/ghostty-org/ghostty/issues/14671)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  During tmux viewer startup, capturing the primary and alternate screens
  changes the terminal's active screen. After the final capture, the
  alternate screen remains active.
  
  `receivedPaneState` uses `alternate_on` to choose which screen receives
  cursor state, but did not activate that screen. When tmux reported the
  primary screen as active, subsequent `%output` notifications were
  therefore written to the alternate screen.
  
  Restore the reported active screen with `Terminal.switchScreen` before
  applying cursor state.
  
  The new tests feed raw control-mode responses through the parser and
  viewer for both values of `alternate_on`. They verify that the reported
  screen becomes active, receives subsequent output, and leaves the other
  screen unchanged.
  
  Related to #1935.
  
  ## Validation
  
  Tested on macOS arm64 with Zig 0.16.0, based on main
  `05dcf887ef51ea27821f20979493306ec3a19149`.
  
  ```sh
  zig fmt --check src/terminal/tmux/viewer.zig
  git diff --check
  zig build test \
    -Dtest-filter="tmux raw startup selects" \
    -Dtest-filter="initial flow" \
    -Dtest-filter="two pane flow with pane state" \
    -Demit-macos-app=false \
    --summary all --color off
  ```
  
  All checks passed: 81/81 tests, including unnamed tests.
  
  Validation used synthetic control-mode input. Live tmux, GUI, and SSH
  sessions were not exercised.
  
  ## Related work
  
  - #14273 handles tmux window notifications and active-window state.
    This change restores the active terminal screen within a pane.
  - #14200 synchronizes alternate-screen mode bits in
  `Terminal.switchScreen`.
    This change makes the tmux viewer call that method using the reported
    pane state.
  
  ## AI disclosure
  
  I used OpenAI Codex for code walkthroughs, implementation guidance,
  review, cleanup, and validation.
  ````
- [`0900c8e`](https://github.com/ghostty-org/ghostty/commit/0900c8ee9aa631259d2d5d1d02fef8ac5f3edd36) apprt/gtk: fix command palette colors when `window-theme=ghostty` ([@HeitorAugustoLN](https://github.com/HeitorAugustoLN))
- [`05dcf88`](https://github.com/ghostty-org/ghostty/commit/05dcf887ef51ea27821f20979493306ec3a19149) apprt/gtk: fix command palette colors when `window-theme=ghostty` ([#14662](https://github.com/ghostty-org/ghostty/issues/14662)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14661
  From:
  https://github.com/GNOME/libadwaita/blob/6f337f9cf1249be9dc23a76835521224cc84cd06/src/stylesheet/widgets/_lists.scss#L4-L8
  ```

## October 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38273686698), [2](https://github.com/ghostty-org/ghostty/actions/runs/38210273538), [3](https://github.com/ghostty-org/ghostty/actions/runs/38206984263), [4](https://github.com/ghostty-org/ghostty/actions/runs/38203368652), [5](https://github.com/ghostty-org/ghostty/actions/runs/38195601411)  
Summary: 5 runs • 17 commits • 7 authors

### Changes

- [`9f6a464`](https://github.com/ghostty-org/ghostty/commit/9f6a4640e6bca7a4d65f1b441f2666b151f4d402) Update VOUCHED list ([#14663](https://github.com/ghostty-org/ghostty/issues/14663)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14662#issuecomment-6127780468)
  from @jcollie.
  
  Vouch: @HeitorAugustoLN
  ```
- [`78a89ce`](https://github.com/ghostty-org/ghostty/commit/78a89cebec38846f83c9723aa53b88d011a76afc) gtk: connect tab split tree signals to the window the tab is in ([@thomasfedb](https://github.com/thomasfedb))
- [`1e9e14a`](https://github.com/ghostty-org/ghostty/commit/1e9e14af5df14211892f5fc15fd21a49c7d94868) gtk: connect tab split tree signals to the window the tab is in ([#14474](https://github.com/ghostty-org/ghostty/issues/14474)) ([@jcollie](https://github.com/jcollie))
  ```text
  **Issue**
  A tab's split tree "changed" handler was connected to the window that
  created the tab, and never moved when the tab was dragged out or moved
  with move_tab_to_new_window. Splits created in a moved tab were wired to
  the old window, so toggle_fullscreen from them fullscreened the old
  window.
  
  To reproduce: open a second tab, run move_tab_to_new_window, create a
  split in the moved tab, then run toggle_fullscreen from that split.
  
  **Fix**
  The handler is now connected when a tab is attached to a window and
  disconnected when it's detached.
  
  First pass written with Claude Code (Claude Opus 5.5), reviewed and
  reprompted by me. Tested on Fedora 44.
  ```
- [`edfd83a`](https://github.com/ghostty-org/ghostty/commit/edfd83ad0b19cadb019c3f16be707a931c36f0d8) gtk: fix mouse cursor shape when selecting text ([@dkinzler](https://github.com/dkinzler))
  ```text
  Fixes #14380
  
  Set the mouse cursor shape on the `RenderSurface` widget instead of on
  `Surface`. To find the cursor shape to show, GTK starts at the widget
  under the mouse and walks up the tree to find an ancestor that has a
  cursor shape set. But when pointer grab is active, GTK will stop looking
  at the widget the grab started at. When selecting text, the widget under
  the mouse is `RenderSurface` and pointer grab is active so that lookup
  stops there and the shape set on `Surface` is ignored.
  ```
- [`7685d36`](https://github.com/ghostty-org/ghostty/commit/7685d36c04c36d7cb8a02703b0f04ff1795d74e7) gtk: fix mouse cursor shape when selecting text ([#14558](https://github.com/ghostty-org/ghostty/issues/14558)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14380 where the mouse cursor shape reverts to the default when
  selecting text.
  
  Set the mouse cursor shape on the `RenderSurface` widget instead of on
  `Surface`. To find the cursor shape to show, GTK starts at the widget
  under the mouse and walks up the tree to find an ancestor that has a
  cursor shape set. But when pointer grab is active, GTK will stop looking
  at the widget the grab started at. When selecting text, the widget under
  the mouse is `RenderSurface` and pointer grab is active so that lookup
  stops there and the shape set on `Surface` is ignored.
  
  Manually tested that everything cursor-related still works: hiding the
  cursor with the `mouse-hide-while-typing` option, setting mouse shape
  with OSC22 and other widgets like the search UI still set their own
  shape.
  
  AI Disclosure: Changes and PR written by myself, used AI in researching
  GTK's mouse cursor logic.
  ```
- [`0df8c48`](https://github.com/ghostty-org/ghostty/commit/0df8c48688a15670d76578a068d178ac76eafbdf) terminal: DECSTR turns off ISO character protection ([@jcollie](https://github.com/jcollie))
  ```text
  The screen remembers which protection mode (DEC or ISO) was used most
  recently, because ISO protection (SPA/EPA) makes ED, EL and ECH skip
  protected cells while DEC protection (DECSCA) doesn't. DECSTR cleared the
  cursor's protected attribute but left that mode alone, so after a soft
  reset an ED 2 still left ISO-protected characters on the screen.
  
  xterm resets the protection mode on DECSTR, so do the same. This fixes
  esctest's ED_0, which failed after ECH_respectsISOProtection because
  the protected character survived esctest's reset between tests.
  
  In xterm (patch 412), SPA sets the mode to ISO_PROTECT:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L5367-L5372
  
  DECSTR calls VTReset with full=False, which calls ReallyReset:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L6154-L6156
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14566-L14568
  
  and ReallyReset sets it back to OFF_PROTECT for both RIS and DECSTR,
  before the part that only RIS does:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14428-L14432
  ```
- [`d0c0d40`](https://github.com/ghostty-org/ghostty/commit/d0c0d4008b0beb4a16dba902c59e36e8ebdad5de) terminal: TBC with no parameter clears the tab stop at the cursor ([@jcollie](https://github.com/jcollie))
  ```text
  The parameter of TBC (CSI Ps g) defaults to 0, which clears the tab stop
  at the cursor, but a bare CSI g has no parameters at all, and the stream
  logged it as an invalid tab clear command and dropped it. Treat it as 0.
  
  This fixes esctest's TBC_Default.
  
  In xterm (patch 412), a missing or zero parameter clears the tab stop
  at the cursor:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L4301-L4308
  ```
- [`4af7e19`](https://github.com/ghostty-org/ghostty/commit/4af7e19c716535075b0c27647d665007e61931d4) terminal: match wide char selection rendering to copying ([@fornwall](https://github.com/fornwall))
  ```text
  Fix two cases where a wide char was not rendered as selected when it
  should (that is, it was included when copying):
  
  1. Selecting leftward onto the spacer tail of a wide char.
  2. Selecting rightward onto the spacer head of a wrapped wide char.
  ```
- [`42a6564`](https://github.com/ghostty-org/ghostty/commit/42a65647b0ea99a2fa6cd787f89bfa62e42b44c5) terminal: clear pending wrap when printing with DECAWM off ([@fornwall](https://github.com/fornwall))
  ```text
  Make printing with DECAWM disabled clear the pending wrap flag,
  avoiding an unexpected wrap after DECAWM is re-enabled.
  ```
- [`d3d4c15`](https://github.com/ghostty-org/ghostty/commit/d3d4c15d6aaedf13ca2c1b395744635cc01b424c) terminal: match wide char selection rendering to copying ([#14651](https://github.com/ghostty-org/ghostty/issues/14651)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix two cases where a wide char was not rendered as selected when it
  should (that is, it was included when copying):
  
  1. Selecting leftward onto the spacer tail of a wide char.
  2. Selecting rightward onto the spacer head of a wrapped wide char.
  
  Before:
  <img width="532" height="108" alt="before"
  src="https://github.com/user-attachments/assets/a2287a87-d2a0-4f5c-af96-2691688478f2"
  />
  
  After:
  <img width="532" height="108" alt="after"
  src="https://github.com/user-attachments/assets/4d065ba8-659c-4c4e-bbe8-2a4016882b2b"
  />
  
  AI disclosure: Created using opus 5.5 through claude code. Reviewed,
  modified and tested by me.
  ```
- [`698f8f4`](https://github.com/ghostty-org/ghostty/commit/698f8f4edb6eabb8a5d0d07892aff6fab52000a0) terminal: clear pending wrap when printing with DECAWM off ([#14652](https://github.com/ghostty-org/ghostty/issues/14652)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Make printing with [DECAWM](https://vt100.net/docs/vt510-rm/DECAWM.html)
  disabled clear the pending wrap flag, avoiding an unexpected wrap after
  `DECAWM` is re-enabled.
  
  Test case:
  
  ```sh
  #!/bin/sh
  printf '\033[2J\033[H\033[?7l'     # Clear screen and disable DECAWM
  printf "%$(tput cols)s" | tr ' ' a # Fill row with 'a', setting pending wrap
  printf '\033[Z'                    # Cursor Backward Tabulation (CBT)
  printf 'X\033[?7hY\n'              # Print 'X', enable DECAWM, print 'Y'
  ```
  
  - Before: `Y` appears at the start of the second row.
  - After: `Y` appears immediately after `X` on the first row.
  - Matches the three terminal emulators I tested with: xterm, kitty and
  mac terminal.
  
  AI disclosure: Initially created using opus 5.5 through claude code.
  Iterated on, reviewed and tested by me.
  ````
- [`3434608`](https://github.com/ghostty-org/ghostty/commit/34346087b28c28f2edd3bafd7935f50c4ded8483) terminal: TBC with no parameter clears the tab stop at the cursor ([#14644](https://github.com/ghostty-org/ghostty/issues/14644)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The parameter of TBC (CSI Ps g) defaults to 0, which clears the tab stop
  at the cursor, but a bare CSI g has no parameters at all, and the stream
  logged it as an invalid tab clear command and dropped it. Treat it as 0.
  
  This fixes esctest's TBC_Default.
  
  In xterm (patch 412), a missing or zero parameter clears the tab stop at
  the cursor:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L4301-L4308
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`aeda37b`](https://github.com/ghostty-org/ghostty/commit/aeda37b305ee3d897ff1bfeddfe39d7fa9366a74) terminal: DECSTR turns off ISO character protection ([#14643](https://github.com/ghostty-org/ghostty/issues/14643)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The screen remembers which protection mode (DEC or ISO) was used most
  recently, because ISO protection (SPA/EPA) makes ED, EL and ECH skip
  protected cells while DEC protection (DECSCA) doesn't. DECSTR cleared
  the cursor's protected attribute but left that mode alone, so after a
  soft reset an ED 2 still left ISO-protected characters on the screen.
  
  xterm resets the protection mode on DECSTR, so do the same. This fixes
  esctest's ED_0, which failed after ECH_respectsISOProtection because the
  protected character survived esctest's reset between tests.
  
  In xterm (patch 412), SPA sets the mode to ISO_PROTECT:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L5367-L5372
  
  DECSTR calls VTReset with full=False, which calls ReallyReset:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L6154-L6156
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14566-L14568
  
  and ReallyReset sets it back to OFF_PROTECT for both RIS and DECSTR,
  before the part that only RIS does:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14428-L14432
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`e602944`](https://github.com/ghostty-org/ghostty/commit/e60294498eaa9ad54be67e2509301d75fd326e50) build(deps): bump actions/download-artifact from 8.0.1 to 8.0.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 8.0.1 to 8.0.2.
  - [Release notes](https://github.com/actions/download-artifact/releases)
  - [Commits](https://github.com/actions/download-artifact/compare/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c...9000827ccba6bdab643e8b6fd33ac0654aef8333)
  
  ---
  updated-dependencies:
  - dependency-name: actions/download-artifact
    dependency-version: 8.0.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`fb24459`](https://github.com/ghostty-org/ghostty/commit/fb24459b1698e92c8ace31e4dd9ff30d0cb3cf0a) build(deps): bump actions/upload-artifact from 7.0.1 to 7.0.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 7.0.1 to 7.0.2.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a...cf430e030ddbb5b0abf93d22962f4752f3646cd9)
  
  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-version: 7.0.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`27e1ad9`](https://github.com/ghostty-org/ghostty/commit/27e1ad9436f35121298f5684f198532b6f4035c9) build(deps): bump actions/upload-artifact from 7.0.1 to 7.0.2 ([#14655](https://github.com/ghostty-org/ghostty/issues/14655)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/upload-artifact](https://github.com/actions/upload-artifact)
  from 7.0.1 to 7.0.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/upload-artifact/releases">actions/upload-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Improves artifact download retries when the service returns HTTP 429
  (rate limiting), including honoring valid Retry-After headers.</li>
  <li>Updates <code>@​actions/artifact</code> to v6.3.1.</li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/tunc-d"><code>@​tunc-d</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/821">actions/upload-artifact#821</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/upload-artifact/compare/v7.0.1...v7.0.2">https://github.com/actions/upload-artifact/compare/v7.0.1...v7.0.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/cf430e030ddbb5b0abf93d22962f4752f3646cd9"><code>cf430e0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/822">#822</a>
  from actions/tunc-d-prepare-upload-v7-0-2</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/c2acdedd35a8824a1552c7137f8c18288c3ea469"><code>c2acded</code></a>
  chore: prepare v7.0.2 release</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/4687c1bbaa0a58abb517d90b4bbade6754c80c1a"><code>4687c1b</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/821">#821</a>
  from actions/tunc-d-upload-artifact-package-bump</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/8cbe1bebdb858105d8fdd88f81404d4de4595719"><code>8cbe1be</code></a>
  Bump <code>@​actions/artifact</code> to 6.3.1</li>
  <li>See full diff in <a
  href="https://github.com/actions/upload-artifact/compare/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a...cf430e030ddbb5b0abf93d22962f4752f3646cd9">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/upload-artifact&package-manager=github_actions&previous-version=7.0.1&new-version=7.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`6d53baf`](https://github.com/ghostty-org/ghostty/commit/6d53bafb1739dce288c653743cceedc54bcadedc) build(deps): bump actions/download-artifact from 8.0.1 to 8.0.2 ([#14654](https://github.com/ghostty-org/ghostty/issues/14654)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/download-artifact](https://github.com/actions/download-artifact)
  from 8.0.1 to 8.0.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/download-artifact/releases">actions/download-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v8.0.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update the readme by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/473">actions/download-artifact#473</a></li>
  <li>Improves artifact download retries when the service returns HTTP 429
  (rate limiting), including honoring valid Retry-After headers.</li>
  <li>Update <code>@​actions/artifact</code> to 6.3.1 by <a
  href="https://github.com/tunc-d"><code>@​tunc-d</code></a> in <a
  href="https://redirect.github.com/actions/download-artifact/pull/492">actions/download-artifact#492</a></li>
  <li>Prepare download-artifact v8.0.2 by <a
  href="https://github.com/tunc-d"><code>@​tunc-d</code></a> in <a
  href="https://redirect.github.com/actions/download-artifact/pull/493">actions/download-artifact#493</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/tunc-d"><code>@​tunc-d</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/actions/download-artifact/pull/492">actions/download-artifact#492</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/download-artifact/compare/v8.0.1...v8.0.2">https://github.com/actions/download-artifact/compare/v8.0.1...v8.0.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/download-artifact/commit/9000827ccba6bdab643e8b6fd33ac0654aef8333"><code>9000827</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/493">#493</a>
  from actions/tunc-d-prepare-download-v8-0-2</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/e455989ae00f5bdd4054f05d3e972c6bf8a62dc5"><code>e455989</code></a>
  Prepare download-artifact v8.0.2</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/a00b90c4a2f01d73a8c89552caabca6ea3b43137"><code>a00b90c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/492">#492</a>
  from actions/tunc-d-download-artifact-package-bump</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/29bb7ce6af5345aeab5bb4774ce7249ee3ccc27f"><code>29bb7ce</code></a>
  Update <code>@​actions/artifact</code> to 6.3.1</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/484a0b528fb4d7bd804637ccb632e47a0e638317"><code>484a0b5</code></a>
  Update the readme (<a
  href="https://redirect.github.com/actions/download-artifact/issues/473">#473</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/download-artifact/compare/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c...9000827ccba6bdab643e8b6fd33ac0654aef8333">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/download-artifact&package-manager=github_actions&previous-version=8.0.1&new-version=8.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## October 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38175388089), [2](https://github.com/ghostty-org/ghostty/actions/runs/38165255491), [3](https://github.com/ghostty-org/ghostty/actions/runs/38145817228), [4](https://github.com/ghostty-org/ghostty/actions/runs/38145546635), [5](https://github.com/ghostty-org/ghostty/actions/runs/38104361585)  
Summary: 5 runs • 13 commits • 5 authors

### Changes

- [`1d8215c`](https://github.com/ghostty-org/ghostty/commit/1d8215c95057bade2c77ae4e0b1c22442d5a15cb) Update VOUCHED list ([#14650](https://github.com/ghostty-org/ghostty/issues/14650)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14649#discussioncomment-18869510)
  from @jcollie.
  
  Vouch: @ollieatkinson
  ```
- [`1e5cdb8`](https://github.com/ghostty-org/ghostty/commit/1e5cdb865807abc990181efb8ebfa9122955cce2) Update VOUCHED list ([#14647](https://github.com/ghostty-org/ghostty/issues/14647)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14640#discussioncomment-18868231)
  from @jcollie.
  
  Vouch: @gaborbernat
  ```
- [`8d8b1ce`](https://github.com/ghostty-org/ghostty/commit/8d8b1ce00c5f1a29d5989a2b0b89b6b88f3b8781) terminal: include wide char wrapped onto next page when copying selection ([@fornwall](https://github.com/fornwall))
  ```text
  Copying a selection whose end lands on the spacer head before a wrapped
  wide character (for example an emoji at the right edge) dropped that
  character when the wrapped row started a new page.
  
  PageFormatter only handled the move onto the next row within a page and
  left a TODO for the cross-page case. Move the handling into
  PageListFormatter, which can advance the end pin across pages, and drop
  the in-page code: search, the only other PageFormatter user, always
  formats whole pages, so nothing relied on it.
  ```
- [`b1d9492`](https://github.com/ghostty-org/ghostty/commit/b1d9492cfa5d0d22c534a00e81bea623957113e7) terminal: include wide char wrapped onto next page when copying selection ([#14632](https://github.com/ghostty-org/ghostty/issues/14632)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Copying a selection whose end lands on the spacer head before a wrapped
  wide character (for example an emoji at the right edge) dropped that
  character when the wrapped row started a new page.
  
  `PageFormatter` only handled the move onto the next row within a page
  and left a TODO for the cross-page case. Move the handling into
  `PageListFormatter`, which can advance the end pin across pages, and
  drop the in-page code: search, the only other `PageFormatter` user,
  always formats whole pages, so nothing relied on it.
  
  Testing note (this confused me): The shell line editor (at least for
  zsh) can interfere with creating a spacer head before a wrapped wide
  character, so best to output wide characters directly to the terminal
  outside of the shell line editor.
  
  AI disclosure: Created with gpt-6 astra using codex. Reviewed and
  modified by me.
  ```
- [`2485de9`](https://github.com/ghostty-org/ghostty/commit/2485de98f194200506ff1cd374a9aed652fcccc9) termio: nushell integration documentation clarification ([@paaloeye](https://github.com/paaloeye))
  ```text
  - explicit acknowledgement of the parse-time constant requirement for `source` command in Nushell
  - split from: https://github.com/ghostty-org/ghostty/pull/14616
  ```
- [`3175f67`](https://github.com/ghostty-org/ghostty/commit/3175f67336e5fcd5e20c2a70a1645ec6c6019d27) libghostty-vt: report CSI 8 t window resize requests ([@jcollie](https://github.com/jcollie))
  ```text
  libghostty-vt parsed resize requests and then dropped them, so embedders
  had no way to honor them the way the app now can.
  ```
- [`211149d`](https://github.com/ghostty-org/ghostty/commit/211149dbc05767c4644d6c2591c21b8759c52839) test/esctest: honor resize requests ([@jcollie](https://github.com/jcollie))
  ```text
  Tests that resize the terminal, such as DECCOLM, failed because the
  runner's terminal ignored them.
  ```
- [`6104c78`](https://github.com/ghostty-org/ghostty/commit/6104c78f1a122d769e5dc92b6029197c9f612f40) terminal: support CSI 19 t (report screen size in characters) ([@jcollie](https://github.com/jcollie))
  ```text
  Respond to XTWINOPS CSI 19 t with CSI 9 ; rows ; cols t. Ghostty has no
  knowledge of the physical screen size, so, like VTE, report the size of
  the text area in characters (the same values as CSI 18 t).
  
  This is wired through both the libghostty-vt stream terminal and the
  termio stream handler, and exposed in the C API as
  GHOSTTY_SIZE_REPORT_CSI_19_T.
  ```
- [`226d719`](https://github.com/ghostty-org/ghostty/commit/226d7191f4a58c78bc18948c5b08a273081e09ee) termio: nushell integration documentation clarification ([#14624](https://github.com/ghostty-org/ghostty/issues/14624)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - explicit acknowledgement of the parse-time constant requirement for
  `source` command in Nushell
  - split from: https://github.com/ghostty-org/ghostty/pull/14616
  ```
- [`6408960`](https://github.com/ghostty-org/ghostty/commit/6408960527c0cde4ca47d1af588e172d46356bb6) terminal: support CSI 19 t (report screen size in characters) ([#14633](https://github.com/ghostty-org/ghostty/issues/14633)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Respond to XTWINOPS CSI 19 t with CSI 9 ; rows ; cols t. Ghostty has no
  knowledge of the physical screen size, so, like VTE, report the size of
  the text area in characters (the same values as CSI 18 t).
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`d66a353`](https://github.com/ghostty-org/ghostty/commit/d66a353aa4cd7266d150586dd555c35ecdb06810) libghostty-vt: report CSI 8 t window resize requests ([#14610](https://github.com/ghostty-org/ghostty/issues/14610)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt parsed resize requests and then dropped them, so embedders
  had no way to honor them the way the app now can.
  
  AI disclosure: Claude Code assisted in the implementation of this PR.
  ```
- [`6603157`](https://github.com/ghostty-org/ghostty/commit/66031576b7a8dcafa6d695c0bf23f15ae81aaf26) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`24da727`](https://github.com/ghostty-org/ghostty/commit/24da727f6857b5350b4a502bdcb30ab942b36e81) Update iTerm2 colorschemes ([#14634](https://github.com/ghostty-org/ghostty/issues/14634)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261005-151109-31756e7
  ```

