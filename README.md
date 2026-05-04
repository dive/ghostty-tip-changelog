> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 4, 2026 at 00:34 UTC.

## May 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25267280551)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`1547dd6`](https://github.com/ghostty-org/ghostty/commit/1547dd667ab6d1f4ebcdc7282adc54c95752ee67) Update VOUCHED list ([#12564](https://github.com/ghostty-org/ghostty/issues/12564)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12563#discussioncomment-16793038)
  from @jcollie.
  
  Vouch: @agoodkind
  ```

## May 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25255420939), [2](https://github.com/ghostty-org/ghostty/actions/runs/25240925859)  
Summary: 2 runs • 8 commits • 4 authors

### Changes

- [`d60a16c`](https://github.com/ghostty-org/ghostty/commit/d60a16c1465415cedf7154d1fd4ad44ca66c3ebe) macos: avoid replaying keys that commit preedit ([@knu](https://github.com/knu))
  ```text
  Refs #10460
  Related: #12518
  
  When an input method commits all or part of marked text during keyDown,
  AppKit returns the committed text through insertText. Treat that as
  text committed by the input method instead of replaying the original key
  event to the terminal.
  
  Previously this path only handled arrow-key commits specially. A
  control-key shortcut that commits preedit text could still be encoded as
  the original control input after composition, such as ctrl+j becoming LF.
  
  Send committed preedit text as a text-only event for any key that causes
  the commit. Only replay arrow navigation keys that the existing Korean
  IME handling expects, and keep plain left-arrow suppressed because AppKit
  already leaves the caret in place.
  
  AI usage: OpenAI Codex helped investigate, implement, test, and refine
  this change. I reviewed and tested the resulting code.
  ```
- [`a971bf1`](https://github.com/ghostty-org/ghostty/commit/a971bf16a0152c31f20001864a196f24e117a731) libghostty-vt: support building nix derivation on darwin ([@sandydoo](https://github.com/sandydoo))
- [`9df670c`](https://github.com/ghostty-org/ghostty/commit/9df670cb557e4dde7870fe551a472ddf2feb2bcc) build: skip unnecessary steps for libghostty-vt ([@sandydoo](https://github.com/sandydoo))
- [`d17e551`](https://github.com/ghostty-org/ghostty/commit/d17e5517c7d1b38d78811801285a38ced8c6fe5a) libghostty-vt: fix dependency path resolution errors ([@sandydoo](https://github.com/sandydoo))
  ```text
  Zigs build infra computes relatives paths to build-time executables that use `setCwd.`
  The logic is purely lexical and doesn't take into account symlinks, unlike `chdir` that follows symlinks.
  
  If the `cwd` resolves to a different depth, then the relative path becomes incorrect.
  ```
- [`7123bdd`](https://github.com/ghostty-org/ghostty/commit/7123bddc184e4c96caa7705b319609f07534359d) libghostty-vt: fix linker tests for darwin ([@sandydoo](https://github.com/sandydoo))
- [`058d054`](https://github.com/ghostty-org/ghostty/commit/058d054fa24478a19a6b71fb2e1977f084d0ff12) libghostty-vt: support building on macOS with Nix ([#12548](https://github.com/ghostty-org/ghostty/issues/12548)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds support for building libghostty-vt on macOS with Nix.
  
  Tested on aarch64-darwin. Tests pass as well.
  
  _Claude used to speed up debugging process. All comments, commit
  messages, and final code authored by me._
  ```
- [`f0bb6ed`](https://github.com/ghostty-org/ghostty/commit/f0bb6ed9eee5271cbbcee7b87d252830b90fb719) macos: avoid replaying keys that commit preedit ([#12547](https://github.com/ghostty-org/ghostty/issues/12547)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #10460
  Related: #12518
  
  When an input method commits all or part of marked text during keyDown,
  AppKit returns the committed text through insertText. Treat that as text
  committed by the input method instead of replaying the original key
  event to the terminal.
  
  Previously this path only handled arrow-key commits specially. A
  control-key shortcut that commits preedit text could still be encoded as
  the original control input after composition, such as ctrl+j becoming
  LF.
  
  Send committed preedit text as a text-only event for any key that causes
  the commit. Only replay arrow navigation keys that the existing Korean
  IME handling expects, and keep plain left-arrow suppressed because
  AppKit already leaves the caret in place.
  
  Before:
  <img width="375" height="375" alt="before"
  src="https://github.com/user-attachments/assets/1073b93f-625a-4881-8f95-67adefe9d3da"
  />
  
  After:
  <img width="375" height="375" alt="after"
  src="https://github.com/user-attachments/assets/3e4be2a5-4df9-4cdd-bc95-e178ca44c7e7"
  />
  
  AI usage: OpenAI Codex helped investigate, implement, test, and refine
  this change. I reviewed and tested the resulting code.
  ```
- [`f27aa86`](https://github.com/ghostty-org/ghostty/commit/f27aa865af5a8f33178d68ef9d9f30b05ba74036) Update VOUCHED list ([#12552](https://github.com/ghostty-org/ghostty/issues/12552)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12542#discussioncomment-16785276)
  from @00-kat.
  
  Denounce: @MorgenGeluk
  ```

## May 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25212984448)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`35c0e25`](https://github.com/ghostty-org/ghostty/commit/35c0e2572fe6f3ca142d2af92f3a22c411e1e16b) Update VOUCHED list ([#12545](https://github.com/ghostty-org/ghostty/issues/12545)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12544#issuecomment-4359105411)
  from @trag1c.
  
  Vouch: @erral
  ```

## April 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25169622892), [2](https://github.com/ghostty-org/ghostty/actions/runs/25150964925)  
Summary: 2 runs • 11 commits • 5 authors

### Changes

- [`a43cc02`](https://github.com/ghostty-org/ghostty/commit/a43cc02ebd709ca2b11d0b31b5bd0e7bf26fb6b3) macos: suppress control-char input while composing ([@knu](https://github.com/knu))
  ```text
  When AppKit delivers a single C0 control character during
  marked-text composition, Ghostty should treat it as input consumed by
  the composing state instead of forwarding it to the terminal.
  
  This prevents control-key IME actions, such as Japanese input
  shortcuts like ctrl+h/j/m/n, from leaking into the terminal while
  composition is still active. Printable text and non-composing control
  input continue through the normal key path.
  
  AI usage: OpenAI Codex helped investigate, implement, test, and refine
  this change. I reviewed and tested the resulting code.
  ```
- [`dbffe99`](https://github.com/ghostty-org/ghostty/commit/dbffe994db3685fbd8794e2dc986b7f895aa86d2) chore: remove Ghostty.xctestplan in project tree. ([@bo2themax](https://github.com/bo2themax))
  ```text
  `lastKnownFileType = file` will change to `text` if you checking out branches with Xcode opened. But this was generated by Xcode in the first place.
  
  Anyway we don't need it to be in the project tree to run the tests, and you can still open the test plan in scheme editor.
  ```
- [`6fdca6b`](https://github.com/ghostty-org/ghostty/commit/6fdca6bb534018581c611a54f5b85fc0d719c44a) macOS: enable copy only when there’s actual selected text ([@bo2themax](https://github.com/bo2themax))
- [`61595b5`](https://github.com/ghostty-org/ghostty/commit/61595b5ec90599cf03c25a1f236d25974f6b7f80) macOS: fix focus state when toggling command palette from inline title editor ([@bo2themax](https://github.com/bo2themax))
- [`f8f3b6f`](https://github.com/ghostty-org/ghostty/commit/f8f3b6f6945e5456fc02be286412778cd8e66742) Fall back to Zig-bundled Darwin headers when an SDK can't be found ([@Samasaur1](https://github.com/Samasaur1))
  ```text
  Currently, cross to Darwin uses the Darwin headers bundled with Zig.
  However, if you're running a build _on_ Darwin, an error is thrown if
  the SDK can't be found, even though the bundled headers are still
  available.
  
  Now, we continue to search for and prefer the installed SDK, but if it
  can't be found, we fall back to the bundled headers rather than failing
  the build.
  ```
- [`83ae471`](https://github.com/ghostty-org/ghostty/commit/83ae47191a6adc89c82fd039bf2133a806a957ea) Fall back to Zig-bundled Darwin headers when an SDK can't be found ([#12534](https://github.com/ghostty-org/ghostty/issues/12534)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Currently, cross to Darwin uses the Darwin headers bundled with Zig.
  However, if you're running a build _on_ Darwin, an error is thrown if
  the SDK can't be found, even though the bundled headers are still
  available.
  
  Now, we continue to search for and prefer the installed SDK, but if it
  can't be found, we fall back to the bundled headers rather than failing
  the build.
  ```
- [`25cd206`](https://github.com/ghostty-org/ghostty/commit/25cd206e25e4c47e6b0d1578325b5ae976a6c954) chore(macOS): remove Ghostty.xctestplan in project tree. ([#12520](https://github.com/ghostty-org/ghostty/issues/12520)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `lastKnownFileType = file` will change to `text` if you checking out
  branches with Xcode opened. But this was generated by Xcode in the first
  place.
  
  Anyway we don't need it to be in the project tree to run the tests, and
  you can still open the test plan in scheme editor.
  ```
- [`1623daf`](https://github.com/ghostty-org/ghostty/commit/1623daf21c89639438d6d55359926b102a49d1ab) macOS: enable copy only when there’s actual selected text ([#12521](https://github.com/ghostty-org/ghostty/issues/12521)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This matches the `peformable` definition and the default behaviors of
  text editing on macOS.
  ```
- [`95b56eb`](https://github.com/ghostty-org/ghostty/commit/95b56eb52510d841814fcf563956c01209bdd414) macOS: fix focus state when toggling command palette from inline title editor ([#12524](https://github.com/ghostty-org/ghostty/issues/12524)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A bug found while recording that menu fix.
  > ~~Will link to an open issue if there is one.~~
  
  When toggling the command palette from the inline title editor, the
  first responder state of the surface is changed quickly from true to
  false.
  
  `makeFirstResponder:` is called by the title editor when finishing, but
  it happens **after** the command palette is shown, so the `focused` is
  set to `true` while the command palette is shown. (Could be an AppKit
  issue as well, since the resign is not called after but the command
  palette is receiving `keyDown`.)
  
  Since `performKeyEquivalent(with:)` is called on all of the subviews
  until one of the return `true` so the paste action is consumed by the
  surface instead of the first responder (command palette).
  ```
- [`4dcb09a`](https://github.com/ghostty-org/ghostty/commit/4dcb09ada0c0909717d92547623b26eafa50ca8a) macos: suppress control-char input while composing ([#12518](https://github.com/ghostty-org/ghostty/issues/12518)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  macos: suppress control-char input while composing
  
  When AppKit delivers a single C0 control character during marked-text
  composition, Ghostty should treat it as input consumed by the composing
  state instead of forwarding it to the terminal.
  
  This prevents control-key IME actions, such as Japanese input shortcuts
  like ctrl+h/j/m/n, from leaking into the terminal while composition is
  still active. Printable text and non-composing control input continue
  through the normal key path.
  
  Refs #10460
  Related: #2628, #4539
  Vouched in #12169
  
  Testing:
  - xcodebuild test -scheme Ghostty -destination platform=macOS
  -only-testing:GhosttyTests/SurfaceViewAppKitTests
  - Manually tested Japanese IME control-key shortcuts on macOS
  
  AI usage:
  - OpenAI Codex helped investigate, implement, test, and refine this
  change. I reviewed and tested the resulting code.
  ```
- [`f5664cd`](https://github.com/ghostty-org/ghostty/commit/f5664cd7b0c0c23f35782c9ec5bdb485e0b9510f) Update VOUCHED list ([#12533](https://github.com/ghostty-org/ghostty/issues/12533)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12530#discussioncomment-16765566)
  from @jcollie.
  
  Vouch: @Samasaur1
  ```

