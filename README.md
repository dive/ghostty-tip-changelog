> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 31, 2026 at 02:21 UTC.

## July 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30572539376), [2](https://github.com/ghostty-org/ghostty/actions/runs/30565278840), [3](https://github.com/ghostty-org/ghostty/actions/runs/30528378351), [4](https://github.com/ghostty-org/ghostty/actions/runs/30510818052)  
Summary: 4 runs • 10 commits • 2 authors

### Changes

- [`b61fd5f`](https://github.com/ghostty-org/ghostty/commit/b61fd5fbb6830b2546cfcaab0e17e6df010e4075) terminal: add iterator to ref counted set ([@mitchellh](https://github.com/mitchellh))
- [`fc1bd06`](https://github.com/ghostty-org/ghostty/commit/fc1bd06a1a090d0ebe59a6b04b021440fbae5b57) terminal: PageList builder to build from raw pages ([@mitchellh](https://github.com/mitchellh))
- [`35db320`](https://github.com/ghostty-org/ghostty/commit/35db32078bc97a54334895bd32a83fce8fc0ef4c) terminal: PageList allocatePage ([@mitchellh](https://github.com/mitchellh))
- [`e77c261`](https://github.com/ghostty-org/ghostty/commit/e77c2612e51af6489cb60043af31aef2da3a5fa5) lib: Zig enums have stable values ([@mitchellh](https://github.com/mitchellh))
- [`457c5a0`](https://github.com/ghostty-org/ghostty/commit/457c5a0a64632282f7f8c2833013b38dc2c312ed) terminal: PageList align Builder/PageAllocation APIs better ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename Builder.addPage and PageAllocation.cancel to their consistent allocatePage and deinit forms. Track successful ownership transfers so both builder APIs can use unconditional deferred cleanup without releasing pages transferred to a PageList.
  ```
- [`4d605bf`](https://github.com/ghostty-org/ghostty/commit/4d605bf0d819df901a0332bbb320dc849fdd82e4) Misc improvements for future binary snapshot API ([#13525](https://github.com/ghostty-org/ghostty/issues/13525)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extracted out the raw `src/terminal` changes needed for the future
  snapshot work, 4 separate changes. These are uncontroversial and
  relatively simple, summarized below. Tests AI assisted but the rest
  including commit messages, this PR message, etc. all organic.
  
  * **Add iterator to ref counted set.** Iterate over live entries and
  their IDs. Const, doesn't mutate the set.
  * **lib.Enum produces stable enums for Zig.** Basically the same as C
  except it uses the smallest fitting integer including the holes.
  * **PageList: a couple helpers for manually creating pages.** There is
  `PageList.Builder` for creating a new pagelist and
  `PageList.allocatePage` for modifying an existing one. This allows
  PageList construction from raw pages.
  ```
- [`d5c7e54`](https://github.com/ghostty-org/ghostty/commit/d5c7e54ae465895fe849de3f35a1440a434db983) terminal: fix string capacity check in hyperlink reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13522
  
  Fixes unreachable when reflow dupes a hyperlink into a destination page
  whose string allocator is nearly full.
  
  The capacity precondition in ReflowCursor.writeCell performed a single
  test allocation of `uri.len + id.len` bytes before duping a hyperlink
  into the destination page. But PageEntry.dupe allocates the URI and
  the explicit ID as two separate allocations, and the string allocator
  rounds every allocation up to its 32-byte chunk size independently, so
  the two separate allocations can require one more chunk than the
  single combined test allocation.
  
  Write a new helper to make sure we get the right amount of space
  using the same allocation pattern of dupe.
  ```
- [`506de85`](https://github.com/ghostty-org/ghostty/commit/506de8517a6579926d35a7b9ae388f32afb8fe42) terminal: fix string capacity check in hyperlink reflow ([#13524](https://github.com/ghostty-org/ghostty/issues/13524)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13522
  
  Fixes unreachable when reflow dupes a hyperlink into a destination page
  whose string allocator is nearly full.
  
  The capacity precondition in ReflowCursor.writeCell performed a single
  test allocation of `uri.len + id.len` bytes before duping a hyperlink
  into the destination page. But PageEntry.dupe allocates the URI and the
  explicit ID as two separate allocations, and the string allocator rounds
  every allocation up to its 32-byte chunk size independently, so the two
  separate allocations can require one more chunk than the single combined
  test allocation.
  
  Write a new helper to make sure we get the right amount of space using
  the same allocation pattern of dupe.
  
  **AI note:** Verified upstream via Fable. I told it to ignore any
  conclusions and do its own validation and fix suggestion. It did
  validate it with a failing test which I studied. It implement a fix, I
  rewrote it to be more idiomatic.
  ```
- [`70c498a`](https://github.com/ghostty-org/ghostty/commit/70c498ac3273661aebf6cce9904c0d42b2e5d299) Update VOUCHED list ([#13521](https://github.com/ghostty-org/ghostty/issues/13521)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13520#discussioncomment-17837792)
  from @pluiedev.
  
  Vouch: @carlvillads
  ```
- [`96e39f8`](https://github.com/ghostty-org/ghostty/commit/96e39f82355d6bbc09f777c775bf01e667f3803e) Update VOUCHED list ([#13518](https://github.com/ghostty-org/ghostty/issues/13518)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13516#discussioncomment-17834904)
  from @jcollie.
  
  Vouch: @fallintoplace
  ```

## July 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30467033163), [2](https://github.com/ghostty-org/ghostty/actions/runs/30460185353), [3](https://github.com/ghostty-org/ghostty/actions/runs/30419843281)  
Summary: 3 runs • 9 commits • 6 authors

### Changes

- [`9fc2a30`](https://github.com/ghostty-org/ghostty/commit/9fc2a3085201f8b51095ff509ef8ebf2b7ed2c55) url: exclude trailing spaces from path matches ([@ruseel](https://github.com/ruseel))
  ```text
  #13491
  #9921
  
  Path matching previously included end-of-line spaces. Pi redraws can
  leave blank cells after a path, causing cmd-click to open a pathname
  that includes those cells. Do not include trailing whitespace in path
  matches.
  
  AI disclosure: Pi using GPT-5.6 Terra High was used to investigate
  and write this change. I reviewed it personally.
  ```
- [`c3b5cab`](https://github.com/ghostty-org/ghostty/commit/c3b5cab94165ea253b8e33683d5fd76fdddb025a) wayland/Hotkeys: polish & simplify ([@pluiedev](https://github.com/pluiedev))
  ```text
  I've come up with a way to avoid manually allocating each entry which
  honestly makes the code flow much more smoothly. Basically you collect
  all the applicable keybinds first, then try to bind them with their
  stable memory addresses.
  ```
- [`adfef29`](https://github.com/ghostty-org/ghostty/commit/adfef29776abcafad57fa17c973a8651ab95b3b9) wayland/Hotkeys: polish & simplify ([#13512](https://github.com/ghostty-org/ghostty/issues/13512)) ([@jcollie](https://github.com/jcollie))
  ```text
  I've come up with a way to avoid manually allocating each entry which
  honestly makes the code flow much more smoothly. Basically you collect
  all the applicable keybinds first, then try to bind them with their
  stable memory addresses.
  ```
- [`6ad1fe7`](https://github.com/ghostty-org/ghostty/commit/6ad1fe7d8cbda36c77b337a96c9bea8a77883699) url: exclude trailing spaces from path matches ([#13505](https://github.com/ghostty-org/ghostty/issues/13505)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This change improves the user experience for Pi TUI users on macOS.
  
  As a user of Ghostty 1.3.1, Pi 0.80.7, and macOS 26.5, I noticed that
  Command-click was not working.
  
  With Pi's help (GPT-5.6 Terra High), I narrowed the cause down to Pi's
  redraw
  behavior and `src/config/url.zig`'s regular expression. More details are
  in
  [Vouch Request
  #13491](https://github.com/ghostty-org/ghostty/discussions/13491).
  
  The `trailing_spaces_at_eol` behavior in `src/config/url.zig` was
  introduced in
  [PR #9921](https://github.com/ghostty-org/ghostty/pull/9921) while
  improving
  Command-click handling for relative and local paths. The concern about
  matching
  trailing whitespace was also noted in [a review
  comment](https://github.com/ghostty-org/ghostty/pull/9921#issuecomment-3661107609).
  
  However, supporting file paths with trailing spaces does not seem like a
  good
  trade-off because it blocks Command-click for file paths displayed by Pi
  TUI.
  
  This PR removes that behavior.
  
  I tested this on my Mac with a patched Ghostty build, and Command-click
  worked
  correctly for file paths in Pi TUI.
  
  AI disclosure: I used Pi with GPT-5.6 Terra High to investigate and
  implement this change.
  I reviewed the code and tested the result myself.
  ```
- [`a34bf0d`](https://github.com/ghostty-org/ghostty/commit/a34bf0dce717fe29c209b77e58f0d6e372bb3747) Update VOUCHED list ([#13511](https://github.com/ghostty-org/ghostty/issues/13511)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13508#discussioncomment-17828581)
  from @jcollie.
  
  Vouch: @simonbcn
  ```
- [`4b58623`](https://github.com/ghostty-org/ghostty/commit/4b586231af5aa8c1f4221704ef452782715022ef) docs: clarify macOS dependencies ([@vegerot](https://github.com/vegerot))
  ```text
  reword: The doc said "macOS doesn't need any dependencies" and then immediately listed things you needed to install for macOS 😁.  This is just rewording the doc to be more consistent.
  ```
- [`1cc5e7b`](https://github.com/ghostty-org/ghostty/commit/1cc5e7bec1eb81c05bb79cc3af22c98cabdbe7cd) update zig-gobject to 0.3.2 ([@jcollie](https://github.com/jcollie))
  ```text
  Includes better ZIg 0.16 compat and updates for Gnome 50.
  ```
- [`6bbbf59`](https://github.com/ghostty-org/ghostty/commit/6bbbf59e9fb08b769539899f27034c50b4ac8de2) update zig-gobject to 0.3.2 ([#13502](https://github.com/ghostty-org/ghostty/issues/13502)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Includes better ZIg 0.16 compat and updates for Gnome 50.
  ```
- [`ae87274`](https://github.com/ghostty-org/ghostty/commit/ae8727401d8c549671c36cdc326a94f47c94b635) docs: clarify macOS dependencies ([#13498](https://github.com/ghostty-org/ghostty/issues/13498)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  reword: The doc said "macOS doesn't need any dependencies" and then
  immediately listed things you needed to install for macOS 😁. This is
  just rewording the doc to be more consistent.
  ```

## July 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30394987951), [2](https://github.com/ghostty-org/ghostty/actions/runs/30393463354), [3](https://github.com/ghostty-org/ghostty/actions/runs/30380212926), [4](https://github.com/ghostty-org/ghostty/actions/runs/30372308941), [5](https://github.com/ghostty-org/ghostty/actions/runs/30370584052), [6](https://github.com/ghostty-org/ghostty/actions/runs/30325837845)  
Summary: 6 runs • 14 commits • 7 authors

### Changes

- [`232d40c`](https://github.com/ghostty-org/ghostty/commit/232d40c062e2fb6fedc24276843afae7a315a664) Update VOUCHED list ([#13499](https://github.com/ghostty-org/ghostty/issues/13499)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13498#issuecomment-5109104876)
  from @mitchellh.
  
  Vouch: @vegerot
  ```
- [`7bea975`](https://github.com/ghostty-org/ghostty/commit/7bea975bd34f8da977674246b36ae80c6df57d09) Update VOUCHED list ([#13497](https://github.com/ghostty-org/ghostty/issues/13497)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13458#discussioncomment-17817388)
  from @jcollie.
  
  Vouch: @RoniJacobson
  ```
- [`2f3814c`](https://github.com/ghostty-org/ghostty/commit/2f3814ca5e6cfcbd504ff86b8120f7e6b7266f56) gtk: honor suspended window state ([@rockorager](https://github.com/rockorager))
  ```text
  GTK exposes the Wayland xdg_toplevel suspended state when the
  compositor knows a window is not visible. Ghostty previously only used
  widget map state, so it could continue rendering a mapped surface on an
  inactive workspace or behind other windows.
  
  Combine the mapped and suspended states for surface occlusion and update
  all displayed surfaces whenever the toplevel suspension state changes.
  
  Amp-Thread-ID: https://ampcode.com/threads/T-019fa965-aa5f-7099-85b4-a9679d2c8bd3
  ```
- [`6c8c079`](https://github.com/ghostty-org/ghostty/commit/6c8c07981d7b4d7c6509323ffb1fe19f45e8af1c) terminal: add visibility reports ([@rockorager](https://github.com/rockorager))
  ```text
  Applications cannot infer whether an unfocused terminal remains visible, so
  focus reports are insufficient for avoiding expensive rendering while a
  view is hidden.
  
  Implement private mode 2033 and the visibility query/report sequences.
  Track conservative per-surface visibility, report every effective change
  while enabled, and always answer explicit queries and mode enables. Keep
  view visibility across terminal resets because it is owned by the host,
  not terminal state.
  
  Amp-Thread-ID: https://ampcode.com/threads/T-019fa965-aa5f-7099-85b4-a9679d2c8bd3
  ```
- [`03eaa01`](https://github.com/ghostty-org/ghostty/commit/03eaa01d484b8c6a098bc94c948e474f33879677) terminal: add visibility reports with GTK suspension tracking ([#13494](https://github.com/ghostty-org/ghostty/issues/13494)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  Applications cannot reliably determine whether an unfocused terminal is
  still
  visible, so focus reports alone are insufficient for avoiding
  unnecessary
  rendering.
  
  This adds terminal visibility reporting by:
  
  - implementing private mode 2033
  - supporting `CSI ? 998 n` visibility queries and `CSI ? 999 ; Ps n`
  responses
  - reporting effective visibility changes while mode 2033 is enabled
  - preserving host-owned visibility state across terminal resets
  - treating unknown visibility conservatively as potentially visible
  
  On GTK 4.12 and newer, surface visibility now combines widget mapping
  with the
  toplevel `suspended` state. This allows Ghostty to recognize windows
  hidden on
  another workspace or otherwise known by the compositor to be
  non-visible.
  Older GTK versions retain the existing conservative behavior.
  
  ## Testing
  
  Added coverage for:
  
  - mode 2033 support and enable/disable behavior
  - explicit visibility queries
  - immediate reports when enabling the mode
  - visible and non-visible responses
  - visibility persistence across terminal resets
  - suppression of visibility queries in read-only mode
  
  ## AI disclosure
  
  Amp assisted with the implementation, tests, commit messages, and this
  pull
  request description. I reviewed the resulting changes and understand how
  they
  interact with the terminal, termio, surface, and GTK visibility paths.
  
  Implements: #13451
  Reference: https://rockorager.dev/misc/visibility-reports/
  ```
- [`07f6c6b`](https://github.com/ghostty-org/ghostty/commit/07f6c6bb07afe0f1d44e5b05fc50b543b6ee878c) mirror deps ([@mitchellh](https://github.com/mitchellh))
- [`4133c6e`](https://github.com/ghostty-org/ghostty/commit/4133c6e48c4b99d19f5885478a19db4868994d07) mirror deps ([#13496](https://github.com/ghostty-org/ghostty/issues/13496)) ([@mitchellh](https://github.com/mitchellh))
- [`95befb3`](https://github.com/ghostty-org/ghostty/commit/95befb33775a4d292732b5d2605d3e95dec05c81) Update VOUCHED list ([#13495](https://github.com/ghostty-org/ghostty/issues/13495)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13491#discussioncomment-17814823)
  from @tristan957.
  
  Vouch: @ruseel
  ```
- [`d716955`](https://github.com/ghostty-org/ghostty/commit/d71695550d4f4aba8b28ce700eeb4b95365ca0e9) config: update info about global keybinds on Linux ([@pluiedev](https://github.com/pluiedev))
- [`d320cd7`](https://github.com/ghostty-org/ghostty/commit/d320cd7df28e4abf6483e021402c65f2ca3f53a2) cli: fix list-themes preview lifecycle ([@jparise](https://github.com/jparise))
  ```text
  Start the vaxis event loop so the theme preview can receive terminal
  input, and retain its environment map for as long as vaxis may access
  it.
  ```
- [`74f45b3`](https://github.com/ghostty-org/ghostty/commit/74f45b321982546e182885a06051c2aab62ce01d) config: update info about global keybinds on Linux ([#13492](https://github.com/ghostty-org/ghostty/issues/13492)) ([@mitchellh](https://github.com/mitchellh))
- [`6e21f41`](https://github.com/ghostty-org/ghostty/commit/6e21f41c0cc6bd09b19e0cc6b8267c7c29ac6159) cli: fix list-themes preview lifecycle ([#13466](https://github.com/ghostty-org/ghostty/issues/13466)) ([@jcollie](https://github.com/jcollie))
  ```text
  Start the vaxis event loop so the theme preview can receive terminal
  input, and retain its environment map for as long as vaxis may access
  it.
  ```
- [`4a22eed`](https://github.com/ghostty-org/ghostty/commit/4a22eed6d9e054fc162a1fb8d4b2899f144da174) renderer/metal: fix 2x sizeof over-allocation in Buffer.sync ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Buffer.sync and Buffer.syncFromArrayLists computed the new buffer size
  in bytes (req_bytes * 2) and then multiplied by @sizeOf(T) again when
  passing it to newBufferWithLength:, allocating data.len * sizeOf(T)^2 * 2
  bytes. For the 32-byte CellText buffers this is a 64x over-allocation
  and for the 4-byte CellBg buffers 8x, per swap-chain frame (e.g. ~9.4MB
  instead of ~300KB per frame for a full 120x40 screen of text).
  
  Match the OpenGL buffer implementation: track the new length in units
  of T and multiply by @sizeOf(T) exactly once.
  ```
- [`a60cd15`](https://github.com/ghostty-org/ghostty/commit/a60cd15bb5a197d8e2596e86442031cbece06bcc) renderer/metal: fix 2x sizeof over-allocation in Buffer.sync ([#13490](https://github.com/ghostty-org/ghostty/issues/13490)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Seems to me the grow path in `Buffer.sync` (and `syncFromArrayLists`)
  multiplies by `@sizeOf(T)` twice: `req_bytes` is already a byte count,
  it gets doubled into size, and then the `newBufferWithLength:` call does
  `size * @sizeOf(T)` on top of that. So every reallocation ends up being
  `data.len` × `@sizeOf(T)`^2 × 2 bytes instead of the intended `data.len`
  × `@sizeOf(T)` × 2.
  
  The OpenGL version of this same helper does it what seems to be the
  intended way, so this looks like a mixup rather than a deliberate safety
  margin.
  
  This makes the Metal implementation match the OpenGL one: track the new
  length in units of T (which also fixes self.len going stale after a
  grow. It's documented as the allocated element count but was never
  updated here)
  ```

## July 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30304357049), [2](https://github.com/ghostty-org/ghostty/actions/runs/30295137203), [3](https://github.com/ghostty-org/ghostty/actions/runs/30286163644), [4](https://github.com/ghostty-org/ghostty/actions/runs/30281549818), [5](https://github.com/ghostty-org/ghostty/actions/runs/30270547633)  
Summary: 5 runs • 22 commits • 6 authors

### Changes

- [`c3655ba`](https://github.com/ghostty-org/ghostty/commit/c3655ba258d930b1eceae05a91a226a8f3720cb9) terminal: expose desktop notification effect ([@pearkes](https://github.com/pearkes))
- [`47d602c`](https://github.com/ghostty-org/ghostty/commit/47d602c422d180eb08627dd29f3386719fac7dcb) terminal: expose progress report effect ([@pearkes](https://github.com/pearkes))
- [`628adaf`](https://github.com/ghostty-org/ghostty/commit/628adaf30f54b7310a163fed164d72ea4391ed3c) terminal: share progress state enum ([@pearkes](https://github.com/pearkes))
- [`2729996`](https://github.com/ghostty-org/ghostty/commit/2729996eab608d19847f4d0c37508442bb3a2096) terminal: update event tests for constructor API ([@pearkes](https://github.com/pearkes))
- [`d0e72a3`](https://github.com/ghostty-org/ghostty/commit/d0e72a3ab654326bc1e5de07199cee229066ee19) font/sprite: update to z2d 0.12.1, use native path insetting ([@vancluever](https://github.com/vancluever))
  ```text
  This change updates z2d to 0.12.1 and changes the sprite font path
  insetting functionality to use the new path offset abilities released in
  the update.
  
  In addition, there has been a slight change to the drawing of E0B5 and
  its respective reflection; we now add a 1-pixel horizontal line segment
  to each end to force them to be perpendicular. This is because
  offsetting pre-expands the curves and ultimately causes the end segments
  of the curve itself to have slight non-horizontal angles, which produce
  small artifacts at the ends without the forced horizontal ends.
  ```
- [`eb9faed`](https://github.com/ghostty-org/ghostty/commit/eb9faed28beac3a0736dc4b6d3327ece78266c03) font/sprite: update to z2d 0.12.1, use native path insetting ([#13489](https://github.com/ghostty-org/ghostty/issues/13489)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This change updates z2d to 0.12.1 and changes the sprite font path
  insetting functionality to use the new path offset abilities released in
  the update.
  
  In addition, there has been a slight change to the drawing of E0B5 and
  its respective reflection; we now add a 1-pixel horizontal line segment
  to each end to force them to be perpendicular. This is because
  offsetting pre-expands the curves and ultimately causes the end segments
  of the curve itself to have slight non-horizontal angles, which produce
  small artifacts at the ends without the forced horizontal ends.
  ```
- [`2dd79f3`](https://github.com/ghostty-org/ghostty/commit/2dd79f3bc6af649e68422b08e21ad0300fd8b391) Expose additional events: desktop and progress ([#13483](https://github.com/ghostty-org/ghostty/issues/13483)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This exposes libghostty-vt callbacks for additional terminal events.
  
  * Desktop notifications from OSC 9/777
  * Progress reports from OSC 9;4, including state and optional percentage
  * Uses the `lib.Enum` progress state
  * Exposes both through the existing terminal option/effect API
  
  AI disclosure: Sol-5.6 was used extensively to write the code, I
  reviewed it personally.
  ```
- [`10e6ace`](https://github.com/ghostty-org/ghostty/commit/10e6ace6b66bddcee1a746c8d5fffb414209cf2a) GhosttyI18n: fix build on freebsd with zig 0.16 ([@svmhdvn](https://github.com/svmhdvn))
- [`c14cb51`](https://github.com/ghostty-org/ghostty/commit/c14cb5196adf4350e6b86f81c871502281016701) GhosttyI18n: fix build on freebsd with zig 0.16 ([#13485](https://github.com/ghostty-org/ghostty/issues/13485)) ([@jcollie](https://github.com/jcollie))
- [`28f02ac`](https://github.com/ghostty-org/ghostty/commit/28f02ac3ce1656f41134f53dc8bf8e3882e14507) Update VOUCHED list ([#13487](https://github.com/ghostty-org/ghostty/issues/13487)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13485#issuecomment-5094118020)
  from @jcollie.
  
  Vouch: @svmhdvn
  ```
- [`f4c68d6`](https://github.com/ghostty-org/ghostty/commit/f4c68d65e5008b950c9a2aac9fa928b244dc3b99) terminal: support runtime scrollback limits ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrollback limits were fixed when a terminal screen was initialized.
  Move byte and line state and enforcement into a shared Limits type so
  PageList can update both constraints after initialization and resize.
  
  Add runtime setters to PageList and Terminal. Lowering a limit prunes
  eligible history immediately, while zero bytes switches the primary
  screen to no-scrollback behavior and clears retained history. Keep
  alternate screens unchanged.
  ```
- [`03d5fa2`](https://github.com/ghostty-org/ghostty/commit/03d5fa268902d609b2872178a1d5a4d9ff351ee7) lib-vt: move scrollback limits to terminal_set ([@mitchellh](https://github.com/mitchellh))
  ```text
  Terminal construction previously accepted GhosttyTerminalOptions with
  dimensions and one scrollback byte limit. Remove the options struct from
  the ABI and make ghostty_terminal_new accept columns and rows directly.
  
  Add byte and line limit options to ghostty_terminal_set and forward them
  to the runtime Terminal setters. NULL removes a limit, while zero bytes
  disables scrollback. Update type metadata, tests, and all API examples.
  ```
- [`a27e04e`](https://github.com/ghostty-org/ghostty/commit/a27e04e8f938be5a6b4c1831d78fea57fae5813f) lib-vt: readers for configured scrollback limits ([@mitchellh](https://github.com/mitchellh))
  ```text
  C API callers could configure runtime scrollback limits but could not
  read them back. Add terminal data keys for the primary screen byte and
  line configurations.
  
  Return GHOSTTY_NO_VALUE for unlimited limits and keep reads stable while
  an alternate screen is active. Document the configured-value semantics
  and add focused coverage for defaults, updates, and unlimited values.
  ```
- [`5fd2973`](https://github.com/ghostty-org/ghostty/commit/5fd2973b9a53ca639e82f1db178587f553dc6e0a) lib-vt: better docs for C options ([@mitchellh](https://github.com/mitchellh))
- [`5a35415`](https://github.com/ghostty-org/ghostty/commit/5a35415a5d59a117e654735ca5a01f876dec5841) libghostty: scrollback limits can be changed at runtime ([#13481](https://github.com/ghostty-org/ghostty/issues/13481)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This is an ABI breaking change for C libs.**
  
  Fixes https://github.com/ghostty-org/ghostty/issues/13268
  
  You can now change scrollback limits (bytes and lines) at runtime.
  
  This breaks the ABI but makes for a much more long-term pattern:
  `ghostty_terminal_new` now only takes viewport size, and you set
  scrollback configurations with the generic `ghostty_terminal_set`. The
  `GhosttyTerminalOptions` struct is fully removed. I think this will
  serve us much better over the long term.
  ```
- [`5b2d3b7`](https://github.com/ghostty-org/ghostty/commit/5b2d3b7df184b8395519baa235ee9539e2fb1a9b) terminal: limit scrollback by physical lines ([@mitchellh](https://github.com/mitchellh))
- [`86f81fb`](https://github.com/ghostty-org/ghostty/commit/86f81fb5b1e45a14281a23e556f916096093e3a3) terminal: expose scrollback line limit ([@mitchellh](https://github.com/mitchellh))
- [`10bc434`](https://github.com/ghostty-org/ghostty/commit/10bc43420cef8b5c8f1a4ac28b5a917d5c12b9cb) terminal: make scrollback byte limit optional ([@mitchellh](https://github.com/mitchellh))
- [`65c4821`](https://github.com/ghostty-org/ghostty/commit/65c48213b6ebbc7c8382d86ccf429101969040c4) config: expose scrollback line limit ([@mitchellh](https://github.com/mitchellh))
- [`1092204`](https://github.com/ghostty-org/ghostty/commit/1092204df19bf56eb5b983dcc44394a1855f111e) config: support unlimited scrollback limits ([@mitchellh](https://github.com/mitchellh))
- [`659a60a`](https://github.com/ghostty-org/ghostty/commit/659a60ae53e96e6303e50180fa68587b7cacc911) terminal/search: fix tests ([@mitchellh](https://github.com/mitchellh))
- [`739603b`](https://github.com/ghostty-org/ghostty/commit/739603b8a2b643b167031a99718127cc0ca311a5) Introduce `scrollback-limit-lines` to limit scrollback by lines instead of bytes ([#13473](https://github.com/ghostty-org/ghostty/issues/13473)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new config `scrollback-limit-lines` to limit scrollback by
  lines instead of bytes. This also renames `scrollback-limit` to
  `scrollback-limit-bytes` to make it clear what it does but we have a
  compatibility entry so old configurations will continue to work, so its
  not breaking.
  
  **This is NOT exclusive to `scrollback-limit-bytes`**. When both are
  set, then the _first limit reached_ is used. Since lines is affected by
  viewport size and bytes are affected by entries (more styles, more
  graphemes, etc.), they serve somewhat different purposes and it might be
  useful to set both.
  
  The default remains 50MB of bytes, unlimited lines.
  
  This is not exposed to libghostty yet. I have that coming as a follow up
  change.
  ```

## July 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30223933750), [2](https://github.com/ghostty-org/ghostty/actions/runs/30222980936), [3](https://github.com/ghostty-org/ghostty/actions/runs/30222642647), [4](https://github.com/ghostty-org/ghostty/actions/runs/30219700544), [5](https://github.com/ghostty-org/ghostty/actions/runs/30187225687)  
Summary: 5 runs • 27 commits • 8 authors

### Changes

- [`e31f729`](https://github.com/ghostty-org/ghostty/commit/e31f729b38d5008be7860b1493d3bee28e571431) deps: update translate-c backport ([@vancluever](https://github.com/vancluever))
  ```text
  This updates the translate-c backport to use the Zig lib dir from the
  build graph rather than an external "zig env" invocation.
  ```
- [`1fe1b2d`](https://github.com/ghostty-org/ghostty/commit/1fe1b2d23c93a252babf7606e74215acdabf5013) build: fix static libghostty-vt linking on Windows ([@noib3](https://github.com/noib3))
  ```text
  This PR fixes static linking for libghostty-vt on Windows by propagating
  a couple of missing dependencies (discovered while running Neovim's Zig
  build, see
  https://github.com/neovim/neovim/actions/runs/30130848061/job/89604799965?pr=39773).
  ```
- [`84254a9`](https://github.com/ghostty-org/ghostty/commit/84254a9d8cb7d8bd28852933484be3f499cfbeee) build: avoid MSVC C++ runtime in no-libcxx builds ([@noib3](https://github.com/noib3))
  ```text
  AI-assisted: Codex
  ```
- [`3b46000`](https://github.com/ghostty-org/ghostty/commit/3b4600014c0e897acd2db469af6e101f1f8645eb) clarify comments ([@mitchellh](https://github.com/mitchellh))
- [`82e53e3`](https://github.com/ghostty-org/ghostty/commit/82e53e3f6e219e0cf0499fe29c82d925ea26cd5e) deps: update translate-c backport ([#13454](https://github.com/ghostty-org/ghostty/issues/13454)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Was brought up as possibly being a build issue here:
  https://codeberg.org/vancluever/translate-c/pulls/1
  
  I do think that this is the better approach and seems to be the close
  equivalent of the `.zig_ilb` option that's coming with `LazyPath` in
  0.17.0 (which is how translate-c behaves there).
  
  I was looking for something like this initially and I _think_ I might
  have passed over it to start with because it was a bit hard to determine
  the circumstances that `b.graph.zig_lib_directory` would be null, but
  upon further examination, I think such cases would be rare if they
  happened at all. Rather than default to the cwd in this event though I
  just get it to error out - that way we'll know if it ever is the case!
  ```
- [`24f7fb9`](https://github.com/ghostty-org/ghostty/commit/24f7fb983506469843c824f65e0c0f7cdf33661c) build: fix static libghostty-vt linking on Windows ([#13452](https://github.com/ghostty-org/ghostty/issues/13452)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR fixes static linking for libghostty-vt on Windows by propagating
  a couple of missing dependencies (discovered while running Neovim's Zig
  build, see [this CI
  run](https://github.com/neovim/neovim/actions/runs/30130848061/job/89604799965?pr=39773)).
  ```
- [`39ae85f`](https://github.com/ghostty-org/ghostty/commit/39ae85f040dd922990e58b8a830414b471ddaf97) lib-vt: handle DECRQSS ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move DECRQSS response encoding into the terminal DCS handler so both
  the full termio path and libghostty-vt terminal stream emit the same
  replies. The C API stream now maintains and releases DCS parser state
  and forwards responses through write_pty.
  ```
- [`40ab02e`](https://github.com/ghostty-org/ghostty/commit/40ab02e3389fe9ff59c3ea682a48359c68ecaf4a) lib-vt: handle DECRQSS ([#13471](https://github.com/ghostty-org/ghostty/issues/13471)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move DECRQSS response encoding into the terminal DCS handler so both the
  full termio path and libghostty-vt terminal stream emit the same
  replies. The C API stream now maintains and releases DCS parser state
  and forwards responses through write_pty.
  ```
- [`4c1d696`](https://github.com/ghostty-org/ghostty/commit/4c1d69696b636fe9915d3d766dc597d36cef0e5e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`5caf20e`](https://github.com/ghostty-org/ghostty/commit/5caf20e3e580dbda86fb3bba73211194843af757) terminal: avoid reallocating tabstop storage ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Resizing tabstops to an already-supported width previously allocated and
  copied an equally sized dynamic buffer because the capacity check
  excluded equality. Treat an exactly sized buffer as sufficient, avoiding
  the temporary allocation and copy.
  Add a fixed-buffer regression test so an unnecessary second allocation
  fails the test.
  ```
- [`35790a7`](https://github.com/ghostty-org/ghostty/commit/35790a7e567124779329a546498f42788b41e0c9) Revert "macOS: fix undo new tab will cause a crash ([#9512](https://github.com/ghostty-org/ghostty/issues/9512))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit fbabafe8e305716d8a5152d6b48014c6814289f2, reversing
  changes made to 7f0468f910fba3e73303bccf1e3d92a36ece3acd.
  ```
- [`a6edca2`](https://github.com/ghostty-org/ghostty/commit/a6edca2d7cef427e78145f7beee6a06af058d5fe) macOS: free surface synchronously in deinit on main thread ([@bo2themax](https://github.com/bo2themax))
- [`20c3eae`](https://github.com/ghostty-org/ghostty/commit/20c3eae04dee606349eb21e2dd0293b203d47179) memset should match the C ABI ([@noib3](https://github.com/noib3))
  ```text
  The custom memset accepted its fill value as u8 even though C callers
  pass int. Accept c_int and explicitly truncate it to the low byte, which
  is what other implementations of this do.
  ```
- [`cb2fef3`](https://github.com/ghostty-org/ghostty/commit/cb2fef39027b6cdfa2b1e4400a0efa90763fea3f) terminal: preserve underline style in DECRQSS ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQSS previously serialized every active underline as SGR 4,
  which caused double, curly, dotted, and dashed styles to round-trip
  as single underlines.
  
  Emit the 4:n form for extended underline styles while retaining the
  legacy 4 form for single underlines, and cover every supported style.
  ```
- [`1eecfe0`](https://github.com/ghostty-org/ghostty/commit/1eecfe089f7e0cb06a328c91e327b5b1188c415a) macOS: free surface synchronously in deinit on main thread ([#13364](https://github.com/ghostty-org/ghostty/issues/13364)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Since the renderer thread now emits scrollbar events on almost every
  frame, there's always a `.scrollbar` message for the dying surface in
  the app mailbox.
  
  The OS runtime seems to schedule `appTick` and `ghostty_surface_free`
  differently across macOS pre-26, 26 and 27.
  
  On macOS 26.x, `ghostty_app_free` happens after
  `App.scrollbar(_:target:v:)`, leaving `surface.userdata` pointing at a
  freed `SurfaceView`.
  
  When `deinit` runs on the main thread, free the surface synchronously
  instead of detaching to a task. This fixes both crashes mentioned in
  https://github.com/ghostty-org/ghostty/pull/9512 and
  https://github.com/ghostty-org/ghostty/issues/13359.
  
  ### AI Disclosure
  
  I used Claude to analyze the backtrace, but the code is written and
  tested by myself.
  ```
- [`8374aa7`](https://github.com/ghostty-org/ghostty/commit/8374aa7850ee5a2630bfda87c279f5fe101df972) Update iTerm2 colorschemes ([#13461](https://github.com/ghostty-org/ghostty/issues/13461)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260720-153658-97e244c
  ```
- [`be3d4a5`](https://github.com/ghostty-org/ghostty/commit/be3d4a53358c7b28f610dd28036b7c7671a4c8ea) terminal: avoid reallocating tabstop storage ([#13465](https://github.com/ghostty-org/ghostty/issues/13465)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Avoid redundant tabstop allocation when the current buffer already
  satisfies the requested size
  ```
- [`6f10ddf`](https://github.com/ghostty-org/ghostty/commit/6f10ddfe83d59d8633421a8bfa13cffbdd0fd121) terminal: preserve underline style in DECRQSS ([#13470](https://github.com/ghostty-org/ghostty/issues/13470)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQSS previously serialized every active underline as SGR 4, which
  caused double, curly, dotted, and dashed styles to round-trip as single
  underlines.
  
  Emit the 4:n form for extended underline styles while retaining the
  legacy 4 form for single underlines, and cover every supported style.
  ```
- [`edcb6fb`](https://github.com/ghostty-org/ghostty/commit/edcb6fb509682d6cfc95b338891e259e22e4e637) memset should match the C ABI ([#13469](https://github.com/ghostty-org/ghostty/issues/13469)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The custom memset accepted its fill value as u8 even though C callers
  pass int. Accept c_int and explicitly truncate it to the low byte, which
  is what other implementations of this do.
  ```
- [`1ce5d42`](https://github.com/ghostty-org/ghostty/commit/1ce5d4229e1dccad2fe83278847048471532e99d) Revert "macOS: fix undo new tab will cause a crash ([#9512](https://github.com/ghostty-org/ghostty/issues/9512))" ([#13467](https://github.com/ghostty-org/ghostty/issues/13467)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We don't need this anymore after #13364
  ```
- [`88bd4fd`](https://github.com/ghostty-org/ghostty/commit/88bd4fdcea7a6416c17c3ace9be6b5aac60d55a7) feat: implement vicinae-hotkey-v1 ([@aurelleb](https://github.com/aurelleb))
- [`9c6f287`](https://github.com/ghostty-org/ghostty/commit/9c6f287aab4358d49a9c6b9ebb734bea1a04bc63) chore: regenerate translations ([@aurelleb](https://github.com/aurelleb))
- [`3024c5d`](https://github.com/ghostty-org/ghostty/commit/3024c5d19e0d5fbe399fbe2192e3dfd3b9793c46) refactor: address nits ([@aurelleb](https://github.com/aurelleb))
- [`0075c75`](https://github.com/ghostty-org/ghostty/commit/0075c75b6127cffe09126b84d3c23ae5101d0447) refactor: remove unneeded appendAssumeCapacity ([@aurelleb](https://github.com/aurelleb))
- [`7ee3ac9`](https://github.com/ghostty-org/ghostty/commit/7ee3ac9ec856d279310faf23947e600769cb3764) refactor: use arena allocator ([@aurelleb](https://github.com/aurelleb))
- [`32e76d8`](https://github.com/ghostty-org/ghostty/commit/32e76d8ed0a2e52e4af70b1e05bda8e1cdb1a4c1) feat: implement global shortcuts through vicinae-hotkey-v1 ([#13464](https://github.com/ghostty-org/ghostty/issues/13464)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR provides an implementation for the
  [vicinae-hotkey-v1](https://github.com/vicinaehq/vicinae-wayland-protocols/tree/main/staging/vicinae-hotkey)
  protocol, as discussed
  [here](https://github.com/ghostty-org/ghostty/discussions/13453).
  
  This is a wayland protocol that allows the client to dynamically
  negotiate global shortcuts with the compositor. Unlike the portal, the
  clients are free to bind, rebind, and unbind global shortcuts they
  reserve.
  
  Here are a few advantages of using this over the global shortcut portal
  for ghostty specifically:
  
  - `vicinae-hotkey-v1` lets the client know the state of its bindings at
  all time, if a global bind is not granted by the compositor the cllient
  is notified with a descriptive error message which is designed to help
  the user understand what the problem might be. In my implementation, I
  decided I would show a desktop notification to the user in case a global
  shortcut reservation fails.
  
  - Global binds set in the config cannot drift from what is actually
  registered, cannot be unilaterally changed by the user in compositor
  settings, and do not pollute the global shortcut namespace permanently.
  Reservations are only active while ghostty is running.
  
  - The protocol provides the client with an input serial that can be used
  to generate an `xdg_activation` token, allowing ghostty to steal focus
  when one of its global shortcut is used. Currently ghostty doesn't have
  an input serial to pass to `xdg_activation`. I didn't wire it for now,
  in order keep things simple. But I guess it will be a nice to have.
  
  ---
  
  AI disclosure: most of the code was written by Fable 5 (Claude Code), as
  zig is not my primary language.
  
  From an implementation perspective: I made it so that
  `vicinae-hotkey-v1` is used to manage global shortcuts over the portal
  when the global is advertised by the compositor. If it's not available,
  we fallback on the portal like before.
  
  At this time the protocol is implemented by Hyprland (since
  [v0.56.0](https://github.com/hyprwm/Hyprland/pull/15010)) and there is
  an open PR for [niri](https://github.com/niri-wm/niri/pull/4145). There
  is also an official [wayland-protocols
  proposal](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/merge_requests/525).
  
  As for the clients, for now the only implementer (that I know of) is
  [vicinae](https://github.com/vicinaehq/vicinae).
  
  The idea would be to merge this `vicinae-hotkey-v1` implementation and
  then have it be superseded by the upstream version later, assuming it is
  turned into an official extension protocol following the
  wayland-protocols process.
  
  PS: sorry for the diff noise about all the .po changes, I'm not sure
  whether this is intended or not, but I did regenerate the translations
  as asked
  ```
- [`2de5e7d`](https://github.com/ghostty-org/ghostty/commit/2de5e7d38e1354759211722a8687c0815d2cf02c) Update VOUCHED list ([#13463](https://github.com/ghostty-org/ghostty/issues/13463)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13462#discussioncomment-17783961)
  from @pluiedev.
  
  Vouch: @aurelleb
  ```

## July 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30165528111)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`fa3802a`](https://github.com/ghostty-org/ghostty/commit/fa3802a70eb7522567c6303a171b9d36bd5dec03) macOS: change split drag's point style to match HIG ([@bo2themax](https://github.com/bo2themax))
- [`66fed65`](https://github.com/ghostty-org/ghostty/commit/66fed652a148cda9d8ea90b1b34ae9768871dbd9) macOS: change split drag's point style to match HIG ([#13433](https://github.com/ghostty-org/ghostty/issues/13433)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="637" height="373" alt="image"
  src="https://github.com/user-attachments/assets/bdcd25f1-7755-47d0-8582-26ea8a00a0ca"
  />
  
  Previously there's mismatch with
  [`CursorStyle.cursor`](https://github.com/ghostty-org/ghostty/blob/15484b607eb5a518dedf1548247c923b8abaae7c/macos/Sources/Helpers/Cursor.swift#L74-L109)
  
  >
  https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Pointers
  ```

