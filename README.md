> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 19, 2026 at 16:07 UTC.

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

## October 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38485309003), [2](https://github.com/ghostty-org/ghostty/actions/runs/38469057359), [3](https://github.com/ghostty-org/ghostty/actions/runs/38466036257), [4](https://github.com/ghostty-org/ghostty/actions/runs/38440102147), [5](https://github.com/ghostty-org/ghostty/actions/runs/38436006247), [6](https://github.com/ghostty-org/ghostty/actions/runs/38420934652), [7](https://github.com/ghostty-org/ghostty/actions/runs/38416363692), [8](https://github.com/ghostty-org/ghostty/actions/runs/38414684379), [9](https://github.com/ghostty-org/ghostty/actions/runs/38331089399)  
Summary: 9 runs • 166 commits • 27 authors

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
- [`6fbb560`](https://github.com/ghostty-org/ghostty/commit/6fbb560cd3bff42fe06af60aef320526b62a8004) cli: include the port in the ssh-terminfo cache key ([@stepankandrushin](https://github.com/stepankandrushin))
  ```text
  The ssh-terminfo cache keyed destinations as user@hostname from `ssh -G`,
  ignoring the port. Two machines behind one address on different ports
  (e.g. user@host:2221 and user@host:2218) shared a key, so once the first
  was cached the terminfo install was skipped for the second, which still
  got TERM=xterm-ghostty without the terminfo installed.
  
  The key now carries the port when it isn't 22: user@host:port, or
  user@[addr]:port for IPv6. Port 22 keeps the old user@host form, so
  existing caches stay valid.
  
  `+ssh-cache` accepts the new form: a bare `host` query matches that host
  on every port, a bare `host:port` query that port for any user, and
  `user@host:port` one exact entry.
  
  AI disclosure: the cause was found and the patch written with Claude
  Code (Claude Opus 5.5). Reviewed and tested by me.
  ```
- [`78a89ce`](https://github.com/ghostty-org/ghostty/commit/78a89cebec38846f83c9723aa53b88d011a76afc) gtk: connect tab split tree signals to the window the tab is in ([@thomasfedb](https://github.com/thomasfedb))
- [`9272a2f`](https://github.com/ghostty-org/ghostty/commit/9272a2f7c24a9282541dba8a3b361ae98bde81bc) terminal: support DECRQCRA and XTCHECKSUM ([@jcollie](https://github.com/jcollie))
  ```text
  Programs such as terminal test suites use DECRQCRA to check what is on
  the screen. Since it also lets any program read the screen back, it is
  off unless vt-xt-checksum-report is set.
  ```
- [`00a19db`](https://github.com/ghostty-org/ghostty/commit/00a19db51aeee5253c83fecc5b647c0358573b5f) config: add vt-xt-checksum-extension ([@jcollie](https://github.com/jcollie))
  ```text
  RIS resets the DECRQCRA checksum calculation, so a program like
  esctest that needs xterm's other calculations had no way to keep it.
  This is the equivalent of xterm's checksumExtension resource.
  ```
- [`7e2d179`](https://github.com/ghostty-org/ghostty/commit/7e2d1793da7f3e1d00b27abe5fe03bb04a0fb474) lib-vt: add GHOSTTY_TERMINAL_OPT_XT_CHECKSUM_EXTENSION ([@jcollie](https://github.com/jcollie))
  ```text
  Embedders had no way to choose the DECRQCRA checksum calculation that
  survives RIS, which vt-xt-checksum-extension gives the app.
  ```
- [`25b04b4`](https://github.com/ghostty-org/ghostty/commit/25b04b410463b97dbc91ec4d24da500a66f4b962) lib-vt: export xt_checksum and device_attributes ([@jcollie](https://github.com/jcollie))
  ```text
  Zig users couldn't name the types needed to set a default checksum or
  answer device attribute queries.
  ```
- [`edcaf66`](https://github.com/ghostty-org/ghostty/commit/edcaf66707f1164030872c0d7a463035af9fc29a) test/esctest: enable DECRQCRA ([@jcollie](https://github.com/jcollie))
  ```text
  esctest reads the screen back with DECRQCRA, so every test that checks
  screen contents failed while the runner left it off.
  ```
- [`cc02767`](https://github.com/ghostty-org/ghostty/commit/cc02767783543f53420c0adf139b5fe6b2471a78) terminal: link to xterm's checksum implementation ([@jcollie](https://github.com/jcollie))
  ```text
  The checksum is modeled on xterm's, so point at its source for comparison.
  ```
- [`5f0d4fe`](https://github.com/ghostty-org/ghostty/commit/5f0d4febc3ac8686ac911aa4a209a4e3d8a48131) terminal: use a rectangle selection for DECRQCRA ([@jcollie](https://github.com/jcollie))
  ```text
  The checksum had its own rectangle type and row walk, duplicating what
  Selection and the pin iterators already provide.
  ```
- [`b2f557c`](https://github.com/ghostty-org/ghostty/commit/b2f557c6c142a5787774c59dd8cb88a58fabc5d0) terminal: inline the checksum test helper ([@jcollie](https://github.com/jcollie))
  ```text
  Each test now shows the selection and flags it checks directly.
  ```
- [`01b9f49`](https://github.com/ghostty-org/ghostty/commit/01b9f4958d9d952cdbbe2473c31dfc7695d3c421) terminal: link to xterm's checksumExtension source ([@jcollie](https://github.com/jcollie))
  ```text
  xterm's documentation for these bits disagrees with its code, so
  point at both to show which one the flags follow.
  ```
- [`e8b858c`](https://github.com/ghostty-org/ghostty/commit/e8b858cc66971aa55376866b149fe304e958fc3b) terminal/tmux: don't count unstored bytes against max_bytes ([@jcollie](https://github.com/jcollie))
  ```text
  A line that filled the control mode buffer exactly couldn't be
  terminated: the newline ending a notification or block, and the '%'
  starting the next notification, were rejected as exceeding the limit
  even though none of them are stored. The parser then broke and dropped
  all further control mode output.
  
  Fixes #11935
  ```
- [`1360297`](https://github.com/ghostty-org/ghostty/commit/136029788c13c8bff81506571ab0009dcc095da2) macos: honor window-save-state=never for restorable windows ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Normal terminal windows remain eligible for native AppKit restoration
  when window-save-state is never, allowing background window snapshots
  to contend with window updates.
  
  Apply the setting when creating a terminal window and assign its
  restoration class and identifier only when restoration is enabled.
  ```
- [`e55c687`](https://github.com/ghostty-org/ghostty/commit/e55c687a4bdf46a4a7a9f51f040798fc11e62154) input: encode ctrl+alt+shift+backspace in legacy mode ([@fornwall](https://github.com/fornwall))
  ```text
  The legacy backspace table, taken from foot's keymap.h, was missing
  foot's Shift+Alt+Ctrl row. The chord fell through to the unmodified
  entry and sent a bare DEL (BS under DECBKM), dropping both the Alt
  prefix and Ctrl. Send ESC BS like Alt+Ctrl and Shift+Alt+Ctrl+Super.
  ```
- [`83edd49`](https://github.com/ghostty-org/ghostty/commit/83edd491e3024ae5e50393d62877b8897da1cccd) Update VOUCHED list ([#14510](https://github.com/ghostty-org/ghostty/issues/14510)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14507#discussioncomment-18705479)
  from @jcollie.
  
  Vouch: @mlabbe
  ```
- [`934ef81`](https://github.com/ghostty-org/ghostty/commit/934ef81401f0c0d27740c44810eede26011a18da) macos: update window restoration on config reload ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Existing terminal windows retained their creation-time restoration
  policy after configuration changes.
  
  Refresh that policy on global config reload and share setup with window
  creation, preserving the custom-command exclusion.
  ```
- [`0e75d01`](https://github.com/ghostty-org/ghostty/commit/0e75d015fe085772b8ecffdba672b60c04af73fe) macos: simplify window restoration setup ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Let isRestorable control preservation while assigning the restoration
  class and identifier consistently for every terminal window.
  
  Remove the restoration test fixture that creates AppKit windows and
  broadcasts configuration changes through the shared test host.
  ```
- [`f523504`](https://github.com/ghostty-org/ghostty/commit/f523504ea5c9f41d150d1eb93cc7a748b90f9361) macos: honor window-save-state=never for restorable windows ([#14506](https://github.com/ghostty-org/ghostty/issues/14506)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  With `window-save-state = never`, normal terminal windows are still
  marked `isRestorable`. Ghostty disables saving through
  `NSQuitAlwaysKeepsWindows`, but AppKit continued taking persistent-UI
  window snapshots in my reproduction on macOS 27.2 (26B5091g).
  
  Make `TerminalController.windowDidLoad()` also honor `never` when
  setting `window.isRestorable`, and only assign the restoration class and
  identifier when that flag is enabled. This adds no work to move, resize,
  or rendering callbacks.
  
  For newly created windows, `default` and `always` retain the existing
  behavior, including the exclusion of windows launched with a custom
  command. The follow-up commit also covers windows that are already open:
  on config reload, each terminal window re-syncs its restoration state
  through the same path used at window creation. Windows started with a
  custom command stay excluded.
  
  ### Reproduction and measurements
  
  I reproduced intermittent roughly 500 ms stalls while repeatedly
  focusing left/right between several Ghostty windows and other
  applications in OmniWM's Niri layout. `window-save-state = never` was
  set before restarting Ghostty.
  
  The issue reproduced on 1.3.1 and an unmodified build of `76895d97b`. In
  the latter, paired process samples showed
  `NSPersistentUIWindowSnapshotter` waiting through
  `SLSConnectionSynchronizeSLSCATransaction`, alongside Ghostty's main
  thread waiting on the connection lock under
  `SLSConnectionSetLastSLSCATransaction`.
  
  Comparing unmodified and patched builds of the same commit over two
  approximately 20-second navigation captures:
  
  | Measurement | Unmodified | Patched |
  | --- | ---: | ---: |
  | Focus presses | 113 | 129 |
  | Successful Ghostty AX frame-write attempts | 2,155 | 2,995 |
  | Ghostty AX frame-write attempts around 500 ms | 5 | 0 |
  | Slowest Ghostty AX frame-write attempt | 539.8 ms | 22.5 ms |
  | Ghostty main-thread samples in the CA/SkyLight connection-lock wait |
  2,205 / 12,544 | 0 / 12,173 |
  
  The persistent-UI snapshot worker was absent from the patched sample,
  and navigation feels noticeably smoother. These are aggregate samples
  from one before/after pair with different input counts, not a controlled
  end-to-end latency benchmark. Both Ghostty builds used ReleaseLocal with
  the same ReleaseFast core, while OmniWM remained the same instrumented
  Debug process.
  
  ### Validation
  
  - `macos/build.nu --action test`: 275 passed, 1 skipped, 0 failed.
  - New `macos/Tests/Terminal/TerminalControllerRestorationTests.swift`:
  reload flips restoration on an open window between `never`, `default`
  and `always`; custom-command windows stay non-restorable across reloads;
  surface-level config changes leave it alone.
  - `macos/build.nu --configuration ReleaseLocal`: passed.
  - Strict SwiftLint on both changed files: passed.
  - Manual navigation reproduction with the patched build: noticeably
  smoother, with the results above.
  
  ### AI disclosure
  
  I used OpenAI Codex to assist with diagnosis, implement the two-line
  change, run verification, analyze the captures, and draft this
  description. I reproduced the issue and tested the patched app
  interactively.
  ```
- [`82ae67b`](https://github.com/ghostty-org/ghostty/commit/82ae67b9f41a009b131f4e336895cb2cce299dfd) libghostty: document allocator alignment as a bit count ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The alloc callback's alignment was documented as a power of two between
  1 and 16, but every vtable call passes @intFromEnum of a
  std.mem.Alignment: the number of low address bits that must be zero,
  not a byte count. An allocator written to the header would align a
  16-byte request to 4 bytes. The range was also wrong: snapshot export
  asks the terminal's allocator for page-aligned memory through
  pagePreservingState.
  
  Document the encoding the implementation already uses, with examples.
  ```
- [`dfd7baf`](https://github.com/ghostty-org/ghostty/commit/dfd7bafcd3a0c34a0557f68c383bb56486a62eab) cli: address review feedback on the ssh-cache port ([@stepankandrushin](https://github.com/stepankandrushin))
  ```text
  - matchesQuery treats a missing port as port 22.
  - isValidPort uses std.ascii.isDigit and rejects leading zeros, so
    host:22 and host:022 can't become distinct keys.
  ```
- [`f5a7f70`](https://github.com/ghostty-org/ghostty/commit/f5a7f706f0ef8751b9f47397b1c12880572b2330) Update VOUCHED list ([#14520](https://github.com/ghostty-org/ghostty/issues/14520)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14517#discussioncomment-18722576)
  from @pluiedev.
  
  Denounce: @davidpmclaughlin
  ```
- [`822e842`](https://github.com/ghostty-org/ghostty/commit/822e84272f60e320526e6c2c223ccdf786d334c9) Update VOUCHED list ([#14522](https://github.com/ghostty-org/ghostty/issues/14522)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14066#discussioncomment-18724022)
  from @jcollie.
  
  Vouch: @moonward
  ```
- [`befcdfd`](https://github.com/ghostty-org/ghostty/commit/befcdfd2c3a1cb24d9ec886e93c95b2b5daa7028) cli: include the port in the ssh-terminfo cache key ([#14472](https://github.com/ghostty-org/ghostty/issues/14472)) ([@jparise](https://github.com/jparise))
  ```text
  The ssh-terminfo cache keyed destinations as user@hostname from `ssh
  -G`, ignoring the port. Two machines behind one address on different
  ports (e.g. user@host:2221 and user@host:2218) shared a key, so once the
  first was cached the terminfo install was skipped for the second, which
  still got TERM=xterm-ghostty without the terminfo installed.
  
  The key now carries the port when it isn't 22: user@host:port, or
  user@[addr]:port for IPv6. Port 22 keeps the old user@host form, so
  existing caches stay valid.
  
  `+ssh-cache` accepts the new form: a bare `host` query matches that host
  on every port, a bare `host:port` query that port for any user, and
  `user@host:port` one exact entry.
  
  AI disclosure: the cause was found and the patch written with Claude
  Code (Claude Opus 5.5). Reviewed and tested by me.
  
  Discussed in #14465.
  ```
- [`406f2e5`](https://github.com/ghostty-org/ghostty/commit/406f2e54401978ad0bbf312b465554465b901f4e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`f96c971`](https://github.com/ghostty-org/ghostty/commit/f96c9711b9f72ecf75e0fd50f3434529b4dea5b6) Update VOUCHED list ([#14528](https://github.com/ghostty-org/ghostty/issues/14528)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12713#discussioncomment-18737824)
  from @jcollie.
  
  Vouch: @maddythewisp
  ```
- [`e6db5b6`](https://github.com/ghostty-org/ghostty/commit/e6db5b633a9ae820fea1620af52dbf87cc7e430c) terminal: fix crash after shrinking columns splits a wide char ([@fornwall](https://github.com/fornwall))
  ```text
  Narrowing without reflow cleared only the cells past the new width, so a
  wide char whose spacer tail was cut kept its head in the new last column.
  Every operation pairing a head with the cell after it then reached past
  the row end: insertBlanks and eraseLine(.left) panic in Screen.clearCells,
  and rowWillBeShifted writes cells[cols].
  
  Clear the orphaned head along with the cut columns.
  ```
- [`ac2ae69`](https://github.com/ghostty-org/ghostty/commit/ac2ae69e08690a6da4e92d61728da4513674bd4b) Update iTerm2 colorschemes ([#14527](https://github.com/ghostty-org/ghostty/issues/14527)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260928-151043-99d9701
  ```
- [`3425025`](https://github.com/ghostty-org/ghostty/commit/3425025e585a3403340d4dc6d65132f42e05e605) libghostty: document allocator alignment as log2 ([#14515](https://github.com/ghostty-org/ghostty/issues/14515)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The header says alignment is a power of two from 1 to 16:
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/include/ghostty/vt/allocator.h#L113-L114
  
  It's actually the log2, since we pass @intFromEnum of a
  std.mem.Alignment, which stores the exponent (@"16" = 4):
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/lib/allocator.zig#L99
  https://ziglang.org/documentation/0.16.0/std/#std.mem.Alignment
  
  So a C allocator written to the header aligns a 16-byte request to 4
  bytes.
  
  The 1–16 range is wrong too. Snapshot export asks the terminal's
  allocator for page-aligned memory:
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/terminal/snapshot/history.zig#L182
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/terminal/PageList.zig#L175-L178
  
  cc @pluiedev cuz i ruberducked the doc change with her.
  ```
- [`eee709f`](https://github.com/ghostty-org/ghostty/commit/eee709f5d3f1030cde981233ec75bfa940cd843f) input: encode ctrl+alt+shift+backspace in legacy mode ([#14508](https://github.com/ghostty-org/ghostty/issues/14508)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  In legacy key encoding, `Ctrl+Alt+Shift+Backspace` sent a bare DEL
  (`0x7f`), the same as plain Backspace.
  
  The backspace table in `function_keys.zig`, which [its header
  says](https://github.com/ghostty-org/ghostty/blob/33da6848d63b3bba2b4f31ab1531d618f2795192/src/input/function_keys.zig#L6-L7)
  is mostly based on foot's `keymap.h`, was missing [foot's Shift+Alt+Ctrl
  row](https://codeberg.org/dnkl/foot/src/commit/cb2771788998f6a6288e2de8273c55a8214551e0/keymap.h#L109).
  With this change it sends `ESC BS` (`\x1b\x08`), matching xterm.
  
  To reproduce, run:
  
  ```sh
  python3 -c 'import os,tty,termios;a=termios.tcgetattr(0);tty.setraw(0);b=os.read(0,16);termios.tcsetattr(0,termios.TCSADRAIN,a);print(repr(b))'
  ```
  
  Then press **Ctrl+Alt+Shift+Backspace** (Option for Alt on macOS).
  
  | | Output |
  |---|---|
  | Before | `b'\x7f'` |
  | After | `b'\x1b\x08'` |
  
  For comparison, Ctrl+Alt+Backspace prints `b'\x1b\x08'` both before and
  after.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ````
- [`2fb0c9c`](https://github.com/ghostty-org/ghostty/commit/2fb0c9cacb3fc75dbc8aedee9b7ed4321f091d33) terminal/tmux: don't count unstored bytes against max_bytes ([#14503](https://github.com/ghostty-org/ghostty/issues/14503)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A line that filled the control mode buffer exactly couldn't be
  terminated: the newline ending a notification or block, and the '%'
  starting the next notification, were rejected as exceeding the limit
  even though none of them are stored. The parser then broke and dropped
  all further control mode output.
  
  Fixes #11935
  
  AI disclosure: Claude Code assisted in the development of this PR.
  ```
- [`04d685c`](https://github.com/ghostty-org/ghostty/commit/04d685c6aa54b27a11fd547a9ac62cd97fdd5ee6) terminal: add suport for DECRQCRA and XTCHECKSUM ([#14483](https://github.com/ghostty-org/ghostty/issues/14483)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQCRA and XTCHECKSUM are used to inspect cells on the running
  terminal. They are mainly useful in conformance tests that verify that
  other control sequences are doing the right thing. Since these control
  sequences could be used to read the entire contents of the screen, they
  are disabled by default (see the `vt-checksum-report` config).
  
  Enabling these fix many of the failing `esctest2` tests.
  
  AI disclosure: Claude Code was used to develop this PR but I have
  thoroughly reviewed the code.
  ```
- [`aca9bf0`](https://github.com/ghostty-org/ghostty/commit/aca9bf031821c1b9dedfec24e93fb609468a274f) libghostty-vt: zero the decode_png output before the callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  For C embedders this was harmless but for embedders in garbage-collected
  languages like Go it isn't because it has a pointer field and in Go,
  storing a pointer into C memory requires that memory to be initialized first,
  because the collector also looks at the value being overwritten. If the
  leftover stack bytes happened to look like a Go heap address, the process
  would abort.
  
  And surprise surprise, around 1 in ~24,000 test runs on my Mac Studio at
  home was able to trigger this in my Go bindings.
  
  References:
  
  - cgo, "Passing pointers": C memory must be initialized before Go code
    stores a pointer into it.
    https://pkg.go.dev/cmd/cgo#hdr-Passing_pointers
  ```
- [`0e0ff28`](https://github.com/ghostty-org/ghostty/commit/0e0ff282f72c92d930d41f4703547d3bc9618ba2) libghostty-vt: zero the decode_png output before the callback ([#14530](https://github.com/ghostty-org/ghostty/issues/14530)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For C embedders this was harmless but for embedders in garbage-collected
  languages like Go it isn't because it has a pointer field and in Go,
  storing a pointer into C memory requires that memory to be initialized
  first, because the collector also looks at the value being overwritten.
  If the leftover stack bytes happened to look like a Go heap address, the
  process would abort.
  
  And surprise surprise, around 1 in ~24,000 test runs on my Mac Studio at
  home was able to trigger this in my Go bindings.
  
  References:
  
  - cgo, "Passing pointers": C memory must be initialized before Go code
  stores a pointer into it.
  https://pkg.go.dev/cmd/cgo#hdr-Passing_pointers
  ```
- [`5dc28bb`](https://github.com/ghostty-org/ghostty/commit/5dc28bb8eebaf57a6c793a406bfea8c632d4fa94) terminal: fix crash after shrinking columns splits a wide char ([#14509](https://github.com/ghostty-org/ghostty/issues/14509)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Narrowing the terminal without reflow (wraparound off, or the alternate
  screen) can cut a wide char in half, leaving its head in the last column
  with no spacer tail.
  
  Later edits on that row (e.g.
  [ICH](https://ghostty.org/docs/vt/csi/ich)) then clear the missing tail
  too, reaching one cell past the row end, which leads to a bounds
  assertion failure in safe builds or an out-of-bounds write otherwise.
  
  To reproduce, run the below script inside a safe build:
  
  ```sh
  #!/bin/sh
  printf '\e[?40h\e[?3h'       # allow DECCOLM, switch to 132 columns
  printf '\e[?47h\e[1;80H一'   # alternate screen: wide char in columns 80-81
  printf '\e[?47l\e[?3l'       # back to 80 columns (alternate screen shrinks without reflow)
  printf '\e[?47h\e[1;80H\e[@' # alternate screen: insert a blank at the last column
  printf '\e[2;1Hsurvived\n'
  ```
  
  - Before: Triggers assertion in `Screen.clearCells`.
  - After: Prints `survived`, column 80 is blank.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ````
- [`157c44f`](https://github.com/ghostty-org/ghostty/commit/157c44f643c9209e31bb92f4c2c4bcec9c6d23d5) input: UTF-8 encode the button in 1005 mouse reports ([@fornwall](https://github.com/fornwall))
  ```text
  In UTF-8 mouse mode (DECSET 1005) the button value was written as a
  single raw byte. xterm encodes it as UTF-8 like the coordinates, so
  values from 128 (buttons 8 and 9) take two bytes. The raw byte made
  the report invalid UTF-8.
  ```
- [`140feb8`](https://github.com/ghostty-org/ghostty/commit/140feb86ae4594472607859b75167889de0c13da) renderer: always release shaders when the render thread exits (Anonymous)
  ```text
  Since #14052, shaders are only freed by releaseGpuResources while the
  display is unrealized, and only the GTK apprt unrealizes. The macOS
  apprt never does, so each closed surface leaked its five render
  pipelines and shader library.
  
  threadExit now marks the display unrealized before releasing GPU
  resources. This frees the shaders and stops any later draw from
  rebuilding resources after the render thread is gone.
  ```
- [`b094a6b`](https://github.com/ghostty-org/ghostty/commit/b094a6ba31825aec1b2beaae54686b4a31f98a8a) input: UTF-8 encode the button in 1005 mouse reports ([#14532](https://github.com/ghostty-org/ghostty/issues/14532)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix UTF-8 mouse reporting (DECSET 1005) to UTF-8 encode the button
  value, as required by [xterm’s
  specification](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h3-Extended-coordinates).
  
  Previously, buttons 8 and 9 (back/forward) produced a raw byte of `0xA0`
  or `0xA1`, making the report invalid UTF-8. For example, pressing button
  8 at column 1, row 1 produced:
  
  - Before: `b'\x1b[M\xa0!!'`
  - After: `b'\x1b[M\xc2\xa0!!'`
  
  AI disclosure: Initially created with claude code using opus 5.5.
  Iterated on, reviewed and tested manually by me.
  ```
- [`35a81a9`](https://github.com/ghostty-org/ghostty/commit/35a81a980bb9fce09a1ea762a68b55f8eb3477ed) renderer: always release shaders  ([#14542](https://github.com/ghostty-org/ghostty/issues/14542)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  shaders are only fread by releaseGpuResources while the display is
  unrealized and only the gtk apprt unrealizes. The mac apprt never does
  automatically so each closed surface leaked its five render pipelines
  and shader library. Updated so threadExit now marks the display
  unrealized before releasing GPU resources.
  ```
- [`c3203ea`](https://github.com/ghostty-org/ghostty/commit/c3203ea4b169a18eb2ccfe92847e426d8afea858) Update VOUCHED list ([#14550](https://github.com/ghostty-org/ghostty/issues/14550)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14549#discussioncomment-18767762)
  from @jcollie.
  
  Vouch: @robmorgan
  ```
- [`13b5ab2`](https://github.com/ghostty-org/ghostty/commit/13b5ab2041fe866e9b448697cd8485b115c32ba2) terminal: stop line selection at prompt boundaries across blank cells ([@fornwall](https://github.com/fornwall))
  ```text
  Selecting a span of blank cells or whitespace between OSC 133 semantic
  boundaries could pull in neighboring prompt text and reverse the
  selection endpoints.
  
  The whitespace trims iterate with a `CellIterator` bounded by the end
  pin, but the iterator bounds only the row, so the trim ran past the end
  column into the next prompt.
  ```
- [`6220a36`](https://github.com/ghostty-org/ghostty/commit/6220a36172ec4558b308b317ac9a7b1e0960cb50) terminal: print codepoints above 0xFF unmapped in a charset, as xterm ([@robmorgan](https://github.com/robmorgan))
  ```text
  With a charset other than UTF-8 or ASCII designated (the DEC
  line-drawing set, say), printCell mapped every codepoint above 0xFF to
  a space. An emoji printed in that state became a blank, and since its
  width still came from the original codepoint, a two-column one, so the
  rest of the row shifted too.
  
  A designated set only applies to the range it is invoked into: G0 is
  invoked into GL (0x21-0x7E), so codepoints outside it pass through
  unchanged (DEC STD 070, following ISO 2022; xterm does the same). The
  charset tables already only remap codepoints in GL, so printCell now
  prints anything above 0xFF as is instead of replacing it with a space.
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
- [`2febd01`](https://github.com/ghostty-org/ghostty/commit/2febd0116dab28df8beb00e4a3453022fe8f3c16) Update VOUCHED list ([#14566](https://github.com/ghostty-org/ghostty/issues/14566)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14563#discussioncomment-18782495)
  from @jcollie.
  
  Vouch: @magnussp
  ```
- [`4611e04`](https://github.com/ghostty-org/ghostty/commit/4611e04ff63c50f71b3e951c4015cfae416cb40d) terminal: print codepoints above 0xFF unmapped in a charset, as xterm ([#14554](https://github.com/ghostty-org/ghostty/issues/14554)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With a charset other than UTF-8 or ASCII designated (e.g. the DEC
  line-drawing set), `printCell` mapped every codepoint above `0xFF` to a
  space. An emoji printed in that state became a blank, and since its
  width still came from the original codepoint (a two-column one), so the
  rest of the row shifted too.
  
  A designated set only applies to the range it is invoked into: G0 is
  invoked into GL (`0x21`–`0x7E`), so codepoints outside it should pass
  through unchanged (DEC STD 070, following ISO 2022 - I checked and xterm
  behaves the same way). Ghostty's charset tables already only remap
  codepoints in GL, so `printCell` now prints anything above `0xFF` as is
  instead of replacing it with a space.
  
  To reproduce, run this inside a current build:
  ```sh
  printf '\e(0`\U0001F600a\e(B\n'
  ```
  
  **Old**
  <img width="585" height="82" alt="image"
  src="https://github.com/user-attachments/assets/4df6c46f-eaf1-459a-b7c2-2e175bbca6ed"
  />
  
  **New**
  <img width="323" height="58" alt="image"
  src="https://github.com/user-attachments/assets/d618502b-e44f-4243-b4b4-8c76e079b88d"
  />
  
  AI disclosure: Created with help from Claude Code using Opus 5.5.
  Iterated on, manually tested, and reviewed by me.
  ````
- [`ca2356f`](https://github.com/ghostty-org/ghostty/commit/ca2356fa05bedefacfc30a71d93ee899aaedb998) terminal: stop line selection at prompt boundaries across blank cells ([#14553](https://github.com/ghostty-org/ghostty/issues/14553)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Selecting a span of blank cells or whitespace between [OSC 133 semantic
  boundaries](https://gitlab.freedesktop.org/Per_Bothner/specifications/-/blob/master/proposals/semantic-prompts.md)
  could pull in neighboring prompt text and reverse the selection
  endpoints. The whitespace trims iterate with a `CellIterator` bounded by
  the end pin, but the iterator bounds only the row, so the trim ran past
  the end column into the next prompt.
  
  To reproduce: Run this script and triple-click either blank cell between
  `x` and `m` on the first row. Before the fix, the selection reaches into
  the neighboring prompt text; after the fix, nothing is selected (like
  triple-clicking a blank row).
  
  ```sh
  #!/bin/sh
  # On exit:
  # \033]133;C\007  Switch back to command-output mode (OSC 133;C).
  # \033[?1049l     Leave the alternate screen and restore the original screen.
  trap 'printf "\033]133;C\007\033[?1049l"' 0
  
  # \033[?1049h     Enter the alternate screen, preserving the original screen.
  # \033]133;C\007  Mark subsequent text as command output (OSC 133;C).
  # \033[2J        Clear the visible screen, leaving unwritten output cells.
  # \033[H         Move the cursor to the top-left corner.
  printf '\033[?1049h\033]133;C\007\033[2J\033[H'
  
  # \033]133;A\007  Mark the start of a prompt (OSC 133;A).
  # x              Print a prompt cell in column 1.
  # \033[2C        Move right two columns, leaving two unwritten output cells.
  # m              Print another prompt cell in column 4.
  # \033]133;C\007  Switch back to command-output mode (OSC 133;C).
  printf '\033]133;A\007x\033[2Cm\033]133;C\007'
  
  # Wait for Enter while you test selection; the exit trap restores the screen.
  read -r _
  ```
  
  AI disclosure: Initially created with the help of gpt-6 astra in codex.
  Iterated on, reviewed and tested by me.
  ````
- [`bae2c3c`](https://github.com/ghostty-org/ghostty/commit/bae2c3cdbf73f2ac33a67e4b0b7811165f0f62d4) libghostty-vt: program status protocol (OSC 7501) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for OSC 7501, the program status protocol. A program
  uses it to tell the terminal what it is doing (idle, working, done,
  blocked on the user, or failed) and why.
  
  The terminal doesn't keep records itself, the same as OSC 9;4. The
  embedder keeps one record per id and applies the spec's lifetime rules.
  A full reset reports a clear of every record. The terminal only answers
  the support query (`OSC 7501 ; ?`) while the effect is set, so programs
  don't send reports that nothing reads. The Ghostty app ignores these
  reports for now.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
    https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`a4aacd9`](https://github.com/ghostty-org/ghostty/commit/a4aacd918ba9e79929ff608034c60a4341773ef0) libghostty-vt: program status protocol (OSC 7501) ([#14560](https://github.com/ghostty-org/ghostty/issues/14560)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for OSC 7501, the program status protocol. A program
  uses it to tell the terminal what it is doing (idle, working, done,
  blocked on the user, or failed) and why.
  
  OSC7501 is the first net-new terminal specification to be pioneered by
  the Ghostty project. In full transparency, this work was motivated by my
  work on Superlogical, but the specification was carefully written in a
  way that doesn't bias towards that use case. The specification is
  broadly useful across a wide variety of applications. I also distributed
  the specification with a diverse group of application and terminal
  developers to solicit feedback.
  
  The terminal doesn't keep records itself, the same as OSC 9;4. The
  embedder keeps one record per id and applies the spec's lifetime rules.
  A full reset reports a clear of every record. The terminal only answers
  the support query (`OSC 7501 ; ?`) while the effect is set, so programs
  don't send reports that nothing reads. The Ghostty app ignores these
  reports for now.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
  https://gist.github.com/mitchellh/7acae3abd8355c1c00287d67e96c913a
  ```
- [`c706451`](https://github.com/ghostty-org/ghostty/commit/c706451fe8bf1a55750c3262ed323df99d717a24) terminal: apply a single shift to exactly one printed character ([@robmorgan](https://github.com/robmorgan))
  ```text
  A single shift (SS2/SS3) applies to the next character received. Only
  printCell used it up, so a combining mark or VS16, which attaches to
  the previous cell without going through printCell, left the shift in
  place for the character after it.
  
  DEC STD 070 (3.8.3.2) says that if the character after a single shift
  is not a graphic character in its range, the shift is ignored and the
  character is processed as if the shift had not been received. ISO 2022
  (8.4) likewise applies it to the immediately following character
  only. print now takes the charset, and clears the single shift, once
  for each codepoint, so a combining mark or VS16 cancels the shift and
  prints unmapped. xterm does the same (WriteNow in charproc.c).
  
  printCell maps its character with that charset and writes it with the
  new writeCell, which writes a cell as it is. Spacers and blanks use
  writeCell, and so does the grapheme path that moves a character VS16
  widened to the next row. That path printed the stored, already mapped
  character through the charset again, so a '#' became a '£' if the
  British set was selected in between.
  ```
- [`34f3900`](https://github.com/ghostty-org/ghostty/commit/34f39002c6e3974b54e6a6d400bd83777c5ea558) Update VOUCHED list ([#14573](https://github.com/ghostty-org/ghostty/issues/14573)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14323#discussioncomment-18786373)
  from @jcollie.
  
  Vouch: @ekusiadadus
  ```
- [`b699ea7`](https://github.com/ghostty-org/ghostty/commit/b699ea79f4b881421b4b3055abc16a0957d76beb) terminal: apply a single shift to exactly one printed character ([#14576](https://github.com/ghostty-org/ghostty/issues/14576)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With a single shift (SS2/SS3) pending, a combining mark or VS16 did not
  use it up because only `printCell` cleared the shift and those
  characters attach to the previous cell without going through it. The
  shift then applied to the next character instead. So in `x` + SS2 + VS16
  + `#` with the British set in G2, the `#` became a `£`.
  
  ### Reproduce
  
  Run these in a current build:
  ```sh
  printf 'x\e*0\eN\u0301a\e*B\n'              # combining mark: prints x́▒, should be x́a
  printf 'x\e*A\eN\uFE0F#\e*B\n'              # VS16: prints x£, should be x#
  printf '\e[%dG#\e(A\uFE0F\e(B\n' $COLUMNS   # expect a wide # at the start of the next line
  ```
  
  **Old**
  <img width="656" height="297" alt="image"
  src="https://github.com/user-attachments/assets/7a20c734-71fd-422f-8394-106e6234d538"
  />
  
  **Fixed**
  <img width="434" height="295" alt="image"
  src="https://github.com/user-attachments/assets/1401e986-3fde-479c-aa5c-e7546861ed97"
  />
  
  DEC STD 070 (3.8.3.2) says that if the character after a single shift is
  not a graphic character in its range, the shift is ignored and the
  character is processed as if the shift had not been received. ISO 2022
  (8.4) likewise applies it to the immediately following character only.
  `print` now takes the charset, and clears the single shift, once for
  each codepoint, so a combining mark or VS16 cancels the shift and prints
  unmapped. xterm does the same (WriteNow in `charproc.c`).
  
  `printCell` maps its character with that charset and writes it with the
  new `writeCell`, which writes a cell as it is. Spacers and blanks use
  `writeCell`, and so does the grapheme path that moves a character VS16
  widened to the next row. That path printed the stored, already mapped
  character through the charset again, so a '#' became a '£' if the
  British set was selected in between (e.g: before VS16).
  
  ### Performance
  I ran `ghostty-bench +terminal-stream` with hyperfine against `main`
  (ReleaseFast, M1 Max, the same 100 MB inputs for both). ASCII, styled
  and DEC line-drawing input show no change, since they go through
  `printSlice` and never reach this code. Random UTF-8, which falls back
  to `print` for most codepoints, is about 1% slower, within this
  machine's run-to-run noise.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`23c7a3e`](https://github.com/ghostty-org/ghostty/commit/23c7a3e5a68aefee51b30a780e706771f80b5f97) formatter: write the cursor position relative to the margins in origin mode ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output from TerminalFormatter restores origin mode (DECOM) with the
  other modes and the scrolling region after the contents, then writes
  the cursor position with CUP. In origin mode CUP counts from the
  top-left of the scrolling region, but the position was written from the
  top-left of the screen, so replaying the output put the cursor that far
  down and to the right whenever a program had set margins and origin
  mode.
  
  When the output restores both origin mode and the scrolling region,
  the cursor position (and the cell reprinted to restore a pending wrap)
  is now written relative to the region's top-left. Without either, the
  replaying terminal counts from the screen's top-left, as before.
  ```
- [`7b60f9b`](https://github.com/ghostty-org/ghostty/commit/7b60f9bf5f057394038f81653eaa7cc5a55bb5df) i18n: improve Danish (da) translation ([@kgni](https://github.com/kgni))
- [`a60e9e2`](https://github.com/ghostty-org/ghostty/commit/a60e9e2a57f73e1eef2bd1cf2995a467f69e7fb0) Update VOUCHED list ([#14585](https://github.com/ghostty-org/ghostty/issues/14585)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14584#discussioncomment-18795569)
  from @jcollie.
  
  Vouch: @kgni
  ```
- [`8f0dd37`](https://github.com/ghostty-org/ghostty/commit/8f0dd3709050b1026f6324368805033197d8b4a5) i18n: improve Danish (da) translation ([#14586](https://github.com/ghostty-org/ghostty/issues/14586)) ([@trag1c](https://github.com/trag1c))
  ````text
  Hi!
  
  I'm a native Danish speaker and went through the Danish translation. I
  hope it's okay that I open this.
  
  My background: Got 0 errors in all of my spelling tests from 4th to 6th
  grade
  
  Happy to adjust or drop anything the da_DK maintainers disagree with.
  
  I followed the Danish GNOME translations for some of these - e.g.
  "Afslut" instead of "Luk ned"
  
  ## Summary
  
  Review pass of `po/da.po` with grammar fixes and small consistency
  changes. No new strings; still `252/252` translated.
  
  ```diff
  - Åben i Ghostty / Åben et nyt vindue. / …og åben den.
  + Åbn i Ghostty / Åbn et nyt vindue. / …og åbn den.        (imperative of "åbne", ~20 strings)
  - Kopiér det valgte tekst …
  + Kopiér den valgte tekst …                                 ("tekst" is common gender)
  - Slå sikker input til/fra
  + Slå sikkert input til/fra                                 ("input" is neuter / intetkøn)
  - Hvis ingen terminaltitel er angivet, vil dette have ingen effekt.
  + Hvis ingen terminaltitel er angivet, har dette ingen effekt.
  - Luk ned / Luk ned for Ghostty?
  + Afslut / Afslut Ghostty?                                  (matches GNOME)
  - Eksekver en kommando… / …vil blive eksekveret.
  + Kør en kommando… / …vil blive kørt.
  - Venligst gennemse fejlene nedenfor, og derefter enten genindlæs …
  + Gennemgå fejlene nedenfor, og genindlæs derefter …
  - Tjek efter opdateringer
  + Søg efter opdateringer
  - Dialog for at skifte titlen på den nuværende terminal.
  + Angiv en ny titel for den nuværende terminal.
  - Kopiér valg som HTML …
  + Kopiér markering som HTML …                               (matches "markering" elsewhere)
  ```
  
  Smaller consistency fixes:
  - `Dette medfører en nedsat ydeevne.` → `Ydeevnen vil være nedsat.`
  - `Slå vis altid øverst til/fra` → `Slå 'altid øverst' til/fra`
  - "Kopiér skærm/markering … til midlertidig fil" titles now use the same
  wording
  - Comma before "og" in all temp-file descriptions
  
  I used Claude Code to help review the initial translation; I went
  through and chose every change myself.
  ````
- [`55424c1`](https://github.com/ghostty-org/ghostty/commit/55424c1ccb34bff8f5534b5bc918ea859b3a9278) i18n: use "konfiguration" consistently in Danish (da) translation ([@kgni](https://github.com/kgni))
- [`e2ced6b`](https://github.com/ghostty-org/ghostty/commit/e2ced6b710427ea69dc6795bf00a787c81554452) i18n: update Danish (da) PO-Revision-Date ([@kgni](https://github.com/kgni))
- [`7551c5b`](https://github.com/ghostty-org/ghostty/commit/7551c5bad4211ebf3cf20647f5b735f2dc14b1f6) Update VOUCHED list ([#14599](https://github.com/ghostty-org/ghostty/issues/14599)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14598#issuecomment-6061636878)
  from @trag1c.
  
  Vouch: @Rayzerrek
  ```
- [`0f171f6`](https://github.com/ghostty-org/ghostty/commit/0f171f650a1cbbd6df4a2573b6b0c7de57cc6d90) Update VOUCHED list ([#14600](https://github.com/ghostty-org/ghostty/issues/14600)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14597#issuecomment-6061673855)
  from @pluiedev.
  
  Denounce: @riskirills66
  ```
- [`bad5854`](https://github.com/ghostty-org/ghostty/commit/bad5854f358332f3168b35c5052f41b45a2671b3) Update VOUCHED list ([#14603](https://github.com/ghostty-org/ghostty/issues/14603)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14595#issuecomment-6062284415)
  from @mitchellh.
  
  Vouch: @Huge
  ```
- [`7ec9e26`](https://github.com/ghostty-org/ghostty/commit/7ec9e26a29399b30ef78f06985fc75045b3cecb6) formatter: write the cursor position relative to the margins in origin mode ([#14588](https://github.com/ghostty-org/ghostty/issues/14588)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  When a program sets a scrolling region and origin mode (DECOM), the VT
  output from `TerminalFormatter` restores the cursor to the wrong place.
  The formatter restores origin mode and the scrolling region (along with
  the other modes) after the contents, then writes the cursor position
  with CUP. In origin mode, CUP counts from the top-left of the screen, so
  the replayed cursor lands too far down (and right with DECSLRM), by the
  size of the margins.
  
  ### Reproduce
  
  Format a terminal with a scrolling region on rows 5-20, with origin mode
  on and the cursor at row 7, column 7, then play the output back and
  print an `X` at the cursor. I made an agent write a small C program with
  `ghostty_formatter_terminal_new` (modes, scrolling region, and cursor
  extras on) against libghostty-vt built from `main` and from this branch:
  
  <img width="764" height="602" alt="formatter-side-by-side"
  src="https://github.com/user-attachments/assets/787943b4-3763-4bbc-8eb8-1924600063e1"
  />
  
  
  The only difference in the output is the cursor position:
  
  ```
  main:  …row 24\e[5;20r\e[7;7H\e[0m   → row 11 in origin mode
  fixed: …row 24\e[5;20r\e[3;7H\e[0m   → row 7
  ```
  
  **The Fix:** When the output restores both origin mode and the scrolling
  region, the cursor position is now rewritten relative to the region's
  top-left. Without either, the replaying terminal counts from the
  screen's top-left, as before. Setting origin mode moves the cursor home,
  so you must write the position relative to the margins after it, and no
  mode ordering avoids this.
  
  ### Performance
  
  The fix runs once per format, not per cell. I've used the benchmark I
  contributed in https://github.com/ghostty-org/ghostty/pull/14581 to run
  `ghostty-bench +terminal-formatter` with `TerminalFormatter` and every
  extra, ReleaseFast on my MacBook Pro M1 Max, median of 60 hyperfine
  runs:
  
  | **Input** | **main** | **this PR** |
  | --- | --- | --- |
  |  80×24 screen in origin mode, 100,000 formats | 1005.4 ms | 999.4 ms |
  | ghostty-gen +styled --seed=42, 640 KB, 20 formats | 47.4 ms | 47.3 ms
  |
  
  AI disclosure: Written with help from Claude Code using Opus 5.5. I
  reviewed, tested and ran the benchmarks myself.
  ````
- [`ce63fcb`](https://github.com/ghostty-org/ghostty/commit/ce63fcba60abb7e11e6435fae32855c20ef3c9cf) I18n/da konfiguration ([#14594](https://github.com/ghostty-org/ghostty/issues/14594)) ([@trag1c](https://github.com/trag1c))
  ````text
  ## Summary
  
  Small follow up to #14586  based on a suggestion from @Fjodor42.
  Two strings used "konfigurering" while the rest of the file uses
  "konfiguration".
  
  ```diff
   msgid "Open Configuration in OS Editor"
  -msgstr "Åbn konfigurering i styresystemets redigeringsprogram"
  +msgstr "Åbn konfiguration i styresystemets redigeringsprogram"
  
   msgid "Open Configuration in New Window"
  -msgstr "Åbn konfigurering i nyt vindue"
  +msgstr "Åbn konfiguration i nyt vindue"
  ```
  
  Also bumped `PO-Revision-Date`.
  ````
- [`54ba7b1`](https://github.com/ghostty-org/ghostty/commit/54ba7b1dd98dfaf14ee82ae7cbf435e867986da9) cli/list-themes: fix keypad page down binding ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  The move-down-by-20 binding listed kp_down instead of kp_page_down.
  Pressing keypad down matched both this binding and the move-down-by-1
  binding, so it moved 21 themes. The move-up-by-20 binding already uses
  kp_page_up.
  ```
- [`7f1219f`](https://github.com/ghostty-org/ghostty/commit/7f1219fd701449fa3e5de33b9ba9ce85f008ac33) cli/list-themes: add ctrl-d/u paging ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  Ctrl-D and Ctrl-U move down and up 20 themes, like PgDn and PgUp.
  This helps keyboards without page keys and matches the less/vi-style
  keys that already exist (g/G).
  ```
- [`c770410`](https://github.com/ghostty-org/ghostty/commit/c770410dbb57909ff4f6921a6497688a957f85db) cli/list-themes: fix keypad page down binding ([#14605](https://github.com/ghostty-org/ghostty/issues/14605)) ([@jcollie](https://github.com/jcollie))
  ````text
  discussion #14604
  
  ## small bug fix
  
  In the "move down 20" binding, `vaxis.Key.kp_down` should be
  `vaxis.Key.kp_page_down`. A `kp_down` press matches both `if` statements
  and moves down 21 rows. I cannot test this because I use macOS and have
  no keypad.
  
  ```zig
  // move down
  if (key.matchesAny(&.{ 'j', '+', vaxis.Key.down, vaxis.Key.kp_down, vaxis.Key.kp_add }, .{}))
      self.down(1);
  if (key.matchesAny(&.{ vaxis.Key.page_down, vaxis.Key.kp_down }, .{}))
      self.down(20);
  
  // move up (no issue, it uses kp_page_up)
  if (key.matchesAny(&.{ 'k', '-', vaxis.Key.up, vaxis.Key.kp_up, vaxis.Key.kp_subtract }, .{}))
      self.up(1);
  if (key.matchesAny(&.{ vaxis.Key.page_up, vaxis.Key.kp_page_up }, .{}))
      self.up(20);
  ```
  ````
- [`b804cb8`](https://github.com/ghostty-org/ghostty/commit/b804cb8fd7f48f471b741ffeaac240b61a31d694) benchmark: measure the terminal formatter with every extra ([@robmorgan](https://github.com/robmorgan))
  ```text
  The formatter benchmark only measured ScreenFormatter with no extras,
  the path clipboard copy, write_screen_file and search use. The
  libghostty-vt C API formats a whole terminal with
  ghostty_formatter_terminal_new, a TerminalFormatter whose extras
  (palette, modes, scrolling region, tabstops, cursor, style and so on)
  describe the terminal's state as well as its contents, and nothing
  measured it.
  
  --formatter=terminal formats with a TerminalFormatter and every extra,
  for every mode and region. With --mode=roundtrip both formats use it,
  so the round trip checks that the output reconstructs that state too,
  not only the contents. The default, --formatter=screen, is unchanged.
  ```
- [`f473f31`](https://github.com/ghostty-org/ghostty/commit/f473f310979da7002f3c2793f39cfbeef475bb88) terminal: support DECSTR ([@jcollie](https://github.com/jcollie))
  ```text
  Programs and test suites use DECSTR (CSI ! p) to undo the modes, margins,
  and pen they may have left behind without clearing the screen. It was
  ignored, so that state leaked into whatever ran next.
  ```
- [`5169c47`](https://github.com/ghostty-org/ghostty/commit/5169c473aa996a9eff29307daad6a01501c5c245) terminal: documentation for DECSTR ([@korikhin](https://github.com/korikhin))
- [`b115e45`](https://github.com/ghostty-org/ghostty/commit/b115e456749e2820a14d3942a63159ff8d46d925) terminal: support DECSTR ([#14538](https://github.com/ghostty-org/ghostty/issues/14538)) ([@jcollie](https://github.com/jcollie))
  ```text
  Programs and test suites use DECSTR (CSI ! p) to undo the modes,
  margins, and pen they may have left behind without clearing the screen.
  It was ignored, so that state leaked into whatever ran next.
  ```
- [`1de05f1`](https://github.com/ghostty-org/ghostty/commit/1de05f1a780b279dcbfc89d93b43b850bd50e517) core: use std.Io.Dir.max_path_bytes ([@paaloeye](https://github.com/paaloeye))
  ```text
  Replace all `std.fs.max_path_bytes` with `std.Io.Dir.max_path_bytes`.
  
  `std.fs.max_path_bytes` is deprected starting from 0.16.0.
  ```
- [`10f6eb4`](https://github.com/ghostty-org/ghostty/commit/10f6eb4603a3f154f8493593da5cfeb895680cbf) cli/list-themes: don't crash when no themes match the search ([@jcollie](https://github.com/jcollie))
  ```text
  With a search that matches nothing, the filtered list is empty, and
  three keys in normal mode assumed a selected theme existed:
  
  - Enter opened the save screen, which indexes the selected theme while
    drawing.
  - G and End set the selection to `len - 1`, which underflows.
  - c and C indexed the selected theme to copy its name or path.
  
  Enter now only opens the save screen when there is a theme to save,
  G and End saturate at zero, and c and C do nothing on an empty list.
  ```
- [`9d479dc`](https://github.com/ghostty-org/ghostty/commit/9d479dcb1664e8dc3c66c7302ce596dc56b36d6d) Update VOUCHED list ([#14614](https://github.com/ghostty-org/ghostty/issues/14614)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14582#discussioncomment-18831499)
  from @pluiedev.
  
  Denounce: @Martzcode
  ```
- [`246f702`](https://github.com/ghostty-org/ghostty/commit/246f702876b924a1cb7cade1e99274d1470302fc) cli/list-themes: add ctrl-d/u paging ([#14607](https://github.com/ghostty-org/ghostty/issues/14607)) ([@jcollie](https://github.com/jcollie))
  ```text
  discussion #14604
  
  ## Ctrl-D and Ctrl-U paging
  
  `Ctrl-D` and `Ctrl-U` move down and up 20 themes. `PgDn` and `PgUp`
  already do this. `g` and `G` already exist (#13376), so vim-like paging
  fits. It also helps users who have no `PgUp` or `PgDn` key.
  ```
- [`b10ba7e`](https://github.com/ghostty-org/ghostty/commit/b10ba7ea26502f8e637e5f698d8d001a6256d9c4) terminal: preserve grapheme data when widening wraps ([@fornwall](https://github.com/fornwall))
  ```text
  With grapheme clustering (mode 2027) enabled, a cluster can widen
  after it has been printed. Codepoints that join a cluster without
  changing its width, such as a zero-width joiner, are stored on the
  cluster's single narrow cell. A later joining codepoint can then make
  the cluster two columns wide (for example a heart, a zero-width joiner,
  then thumbs up).
  
  When that happens in the last column and auto-wrap is enabled, the
  cluster wraps to the next line and its stored codepoints have to move
  with it. Copy them before wrapping instead of looking them up on the
  row above afterwards. That row isn't the original one when the wrap
  scrolls a single-row screen or a margin region, or doesn't scroll at
  all below the scroll region. So the codepoints were dropped, taken
  from an unrelated cell, or the lookup panicked.
  ```
- [`6dae79d`](https://github.com/ghostty-org/ghostty/commit/6dae79db927110b29970a0fbe7979949c6a3ffd4) terminal: re-attach wrapped grapheme data in one allocation ([@fornwall](https://github.com/fornwall))
  ```text
  Re-attach the grapheme codepoints copied across a widening wrap with a
  single setGraphemes call instead of appending them one at a time.
  Appending probed the grapheme map and could reallocate the chunk once
  per codepoint, which cost about 10% on input where every wrap carries
  a maximal cluster.
  
  Screen.setGraphemes mirrors appendGrapheme: on a full grapheme map or
  allocator it grows the page's grapheme capacity, reloads the cell and
  retries. Add a test that wraps onto a compacted page with no grapheme
  capacity so that path is covered.
  ```
- [`9fa2e3a`](https://github.com/ghostty-org/ghostty/commit/9fa2e3aaffdc7ae30f7cc417d1ce706957ae58a0) libghostty-vt: add prompt-based viewport scrolling ([@elias8](https://github.com/elias8))
- [`1da3ac4`](https://github.com/ghostty-org/ghostty/commit/1da3ac43bef626ec1155c366c1960cb0f4f74d1f) Update VOUCHED list ([#14623](https://github.com/ghostty-org/ghostty/issues/14623)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14486#issuecomment-6097215618)
  from @trag1c.
  
  Denounce: @rebecca-bell-2001
  ```
- [`2485de9`](https://github.com/ghostty-org/ghostty/commit/2485de98f194200506ff1cd374a9aed652fcccc9) termio: nushell integration documentation clarification ([@paaloeye](https://github.com/paaloeye))
  ```text
  - explicit acknowledgement of the parse-time constant requirement for `source` command in Nushell
  - split from: https://github.com/ghostty-org/ghostty/pull/14616
  ```
- [`c986a09`](https://github.com/ghostty-org/ghostty/commit/c986a09dc4c04d641914995e4a8ee706d9ea4e4b) cli/list-themes: don't crash when no themes match the search ([#14612](https://github.com/ghostty-org/ghostty/issues/14612)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With a search that matches nothing, the filtered list is empty, and
  three keys in normal mode assumed a selected theme existed:
  
  - Enter opened the save screen, which indexes the selected theme while
  drawing.
  - G and End set the selection to `len - 1`, which underflows.
  - c and C indexed the selected theme to copy its name or path.
  
  Enter now only opens the save screen when there is a theme to save, G
  and End saturate at zero, and c and C do nothing on an empty list.
  
  AI disclosure: Claude Code assisted in the development of this PR.
  ```
- [`747dd53`](https://github.com/ghostty-org/ghostty/commit/747dd538d5a71bc84e980177db3b23c082ed5781) core: use std.Io.Dir.max_path_bytes ([#14611](https://github.com/ghostty-org/ghostty/issues/14611)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace all `std.fs.max_path_bytes` with `std.Io.Dir.max_path_bytes`.
  
  `std.fs.max_path_bytes` is deprected starting from 0.16.0.
  ```
- [`65f2b48`](https://github.com/ghostty-org/ghostty/commit/65f2b4838f1d5946aa19080bfb84732871c7b695) benchmark: measure the terminal formatter with every extra ([#14581](https://github.com/ghostty-org/ghostty/issues/14581)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The formatter benchmark only measures `ScreenFormatter` with no extras,
  the path clipboard copy, `write_screen_file` and search use. The
  libghostty-vt C API formats a whole terminal with
  `ghostty_formatter_terminal_new`, a lovely `TerminalFormatter` whose
  extras(palette, modes, scrolling region, cursor, etc.) describe the
  terminal's state as well as its contents. As far as I'm aware, nothing
  measured that path.
  
  This PR adds `--formatter=terminal` to the benchmarks, which formats
  with a `TerminalFormatter` and every extra. It works with every mode and
  region. With `--mode=roundtrip`, both formats use it, so the round trip
  also checks that the output reconstructs the terminal state, not just
  the contents. The default, `--formatter=screen`, is unchanged.
  
  ### Numbers
  
  Here is the `ghostty-bench +terminal-formatter`, ReleaseFast on my
  Macbook Pro M1 Max with a median of 60 hyperfine runs and the `noop`
  baseline subtracted:
  
  | Input | main `screen` | this PR `screen` | this PR `terminal` |
  | --- | --- | --- | --- |
  | `ghostty-gen +styled --seed=42`, 640 KB, 80×24 | 1,687 µs | 1,688 µs |
  1,718 µs |
  | Claude Code session, 120×40, alternate screen | 7.67 µs | 7.62 µs |
  16.27 µs |
  
  **Note:** The existing path is unchanged. The extras add a fixed ~8.6 µs
  per format, mostly the 256-entry palette and modes.
  
  AI disclosure: Written with help from Claude Code using Opus 5.5. I
  reviewed, tested and ran the benchmarks myself.
  ```
- [`b7207b2`](https://github.com/ghostty-org/ghostty/commit/b7207b2ef6aa3e05af992a6febb9ee83ad69bb8c) libghostty-vt: update program status protocol to revision 0.4 ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only change in behavior is the reply to the support query. It
  used to be a bare `?`. It now also lists the states and kinds the
  terminal accepts, computed at comptime.
  
  The rest is documentation to match revisions 0.3 and 0.4.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
    https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`9cd19b4`](https://github.com/ghostty-org/ghostty/commit/9cd19b40de63f5bd172d1fcf30b667c8186d8923) libghostty-vt: update program status protocol to revision 0.4 ([#14630](https://github.com/ghostty-org/ghostty/issues/14630)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only change in behavior is the reply to the support query. It used
  to be a bare `?`. It now also lists the states and kinds the terminal
  accepts, computed at comptime.
  
  The rest is documentation to match revisions 0.3 and 0.4.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
  https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`2551d93`](https://github.com/ghostty-org/ghostty/commit/2551d9323505043ee6f4fcd5fc6f116bbe06f1df) terminal: preserve grapheme data when widening wraps ([#14552](https://github.com/ghostty-org/ghostty/issues/14552)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With [grapheme
  clustering](https://mitchellh.com/writing/grapheme-clusters-in-terminals#grapheme-clustering-in-terminals)
  enabled, a cluster can widen after it has been printed. Codepoints that
  join a cluster without changing its width, such as a zero-width joiner,
  are stored on the cluster's single narrow cell. A later joining
  codepoint can then make the cluster two columns wide (for example a
  heart, a zero-width joiner, then thumbs up).
  
  When that happens in the last column and auto-wrap is enabled, the
  cluster wraps to the next line and its stored codepoints have to move
  with it. Copy them before wrapping instead of looking them up on the row
  above afterwards: that row isn't the original one when the wrap scrolls
  a single-row screen or a margin region, or doesn't scroll at all below
  the scroll region.
  
  To reproduce, open a window and run the below using a safe build:
  
  ```sh
  # \033[?2027h    Enable grapheme-cluster handling (mode 2027).
  # \033[2J        Clear the visible screen.
  # \033[1;2r      Set the scrolling region to rows 1–2 and home the cursor.
  # \033[999;999H  Move to the bottom-right corner (coordinates are clamped).
  # \u2764         Print a heart, initially one cell wide.
  # \u200d         Append a zero-width joiner to the heart.
  # \U0001f44d     Append thumbs up, widening the cluster and triggering wrapping.
  # \033[r         Restore full-screen scrolling and home the cursor.
  # \033[999;1H    Move to the first column of the bottom row (below grapheme).
  # \n             Print a newline.
  printf '\033[?2027h\033[2J\033[1;2r\033[999;999H\u2764\u200d\U0001f44d\033[r\033[999;1H\n'
  ```
  
  - Before: Panics in safe builds when the cluster widens at the
  bottom-right corner below a scroll region. In release builds it unwraps
  a missing grapheme lookup, which is undefined behavior (a ReleaseFast
  test run segfaults).
  - After: it wraps with its grapheme data intact.
  
  AI disclosure: Initially created with the help of gpt-6 astra in codex.
  Iterated on, reviewed and tested by me.
  ````
- [`4144f6d`](https://github.com/ghostty-org/ghostty/commit/4144f6dea4dbf9586c797e535a04f1cfd381d8a7) core: demote 'adjusting page capacity' log message to debug ([@jcollie](https://github.com/jcollie))
- [`6161591`](https://github.com/ghostty-org/ghostty/commit/61615915c8f423b1497ac2a1ae68885cad353892) core: demote 'adjusting page capacity' log message to debug ([#14631](https://github.com/ghostty-org/ghostty/issues/14631)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This can really spam the logs, and isn't really useful outside of a
  developer context anyway.
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
- [`e3ac620`](https://github.com/ghostty-org/ghostty/commit/e3ac62001ef2a6c9c4b4bb4231535c1c3c3e4ae3) feat(lib-vt): expose prompt navigation through the C API ([#14618](https://github.com/ghostty-org/ghostty/issues/14618)) ([@trag1c](https://github.com/trag1c))
  ```text
  Adds `GHOSTTY_SCROLL_VIEWPORT_DELTA_PROMPT` to the existing
  `ghostty_terminal_scroll_viewport` API. This allows libghostty consumers
  to navigate between shell prompts using the same native implementation
  as Ghostty's `jump_to_prompt` action.
  
  The signed `delta_prompt` count moves backward or forward from the
  viewport top, treating multiline prompt continuations as one group. This
  also fixes two boundary cases in the shared traversal: navigating
  backward through a trimmed prompt and navigating forward when the
  current prompt continues to the last retained row.
  
  AI disclosure: I used Codex to assist with the implementation.
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
- [`6104c78`](https://github.com/ghostty-org/ghostty/commit/6104c78f1a122d769e5dc92b6029197c9f612f40) terminal: support CSI 19 t (report screen size in characters) ([@jcollie](https://github.com/jcollie))
  ```text
  Respond to XTWINOPS CSI 19 t with CSI 9 ; rows ; cols t. Ghostty has no
  knowledge of the physical screen size, so, like VTE, report the size of
  the text area in characters (the same values as CSI 18 t).
  
  This is wired through both the libghostty-vt stream terminal and the
  termio stream handler, and exposed in the C API as
  GHOSTTY_SIZE_REPORT_CSI_19_T.
  ```
- [`6603157`](https://github.com/ghostty-org/ghostty/commit/66031576b7a8dcafa6d695c0bf23f15ae81aaf26) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`24da727`](https://github.com/ghostty-org/ghostty/commit/24da727f6857b5350b4a502bdcb30ab942b36e81) Update iTerm2 colorschemes ([#14634](https://github.com/ghostty-org/ghostty/issues/14634)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261005-151109-31756e7
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
- [`1e5cdb8`](https://github.com/ghostty-org/ghostty/commit/1e5cdb865807abc990181efb8ebfa9122955cce2) Update VOUCHED list ([#14647](https://github.com/ghostty-org/ghostty/issues/14647)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14640#discussioncomment-18868231)
  from @jcollie.
  
  Vouch: @gaborbernat
  ```
- [`1d8215c`](https://github.com/ghostty-org/ghostty/commit/1d8215c95057bade2c77ae4e0b1c22442d5a15cb) Update VOUCHED list ([#14650](https://github.com/ghostty-org/ghostty/issues/14650)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14649#discussioncomment-18869510)
  from @jcollie.
  
  Vouch: @ollieatkinson
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
- [`9f6a464`](https://github.com/ghostty-org/ghostty/commit/9f6a4640e6bca7a4d65f1b441f2666b151f4d402) Update VOUCHED list ([#14663](https://github.com/ghostty-org/ghostty/issues/14663)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14662#issuecomment-6127780468)
  from @jcollie.
  
  Vouch: @HeitorAugustoLN
  ```
- [`0900c8e`](https://github.com/ghostty-org/ghostty/commit/0900c8ee9aa631259d2d5d1d02fef8ac5f3edd36) apprt/gtk: fix command palette colors when `window-theme=ghostty` ([@HeitorAugustoLN](https://github.com/HeitorAugustoLN))
- [`05dcf88`](https://github.com/ghostty-org/ghostty/commit/05dcf887ef51ea27821f20979493306ec3a19149) apprt/gtk: fix command palette colors when `window-theme=ghostty` ([#14662](https://github.com/ghostty-org/ghostty/issues/14662)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14661
  From:
  https://github.com/GNOME/libadwaita/blob/6f337f9cf1249be9dc23a76835521224cc84cd06/src/stylesheet/widgets/_lists.scss#L4-L8
  ```

