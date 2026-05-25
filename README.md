> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 25, 2026 at 04:31 UTC.

## May 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26382148026), [2](https://github.com/ghostty-org/ghostty/actions/runs/26381111088)  
Summary: 2 runs • 4 commits • 2 authors

### Changes

- [`edf2da0`](https://github.com/ghostty-org/ghostty/commit/edf2da015705db22fffdcab62a0871c898fa064b) libghostty: expose per-cell selection state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Render-state rows already expose their selected range, but
  cell-oriented C API consumers had to fetch that row range separately
  and duplicate the containment check while rendering.
  
  Add a SELECTED row-cells data kind that carries the row selection into
  the row-cells wrapper and returns whether the current cell column is in
  that inclusive range. The field remains separate from cell colors and
  style so selection stays an explicit render overlay policy.
  
  For performance reasons, the span-based row getter is recommended still
  but this is a convenient thing to do for cell-oriented folks.
  ```
- [`b869a6e`](https://github.com/ghostty-org/ghostty/commit/b869a6e5ab0a50ce01e8eb5aa408a02b3cbe4f3a) libghostty: expose per-cell selection state ([#12798](https://github.com/ghostty-org/ghostty/issues/12798)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Render-state rows already expose their selected range, but cell-oriented
  C API consumers had to fetch that row range separately and duplicate the
  containment check while rendering.
  
  Add a SELECTED row-cells data kind that carries the row selection into
  the row-cells wrapper and returns whether the current cell column is in
  that inclusive range. The field remains separate from cell colors and
  style so selection stays an explicit render overlay policy.
  
  For performance reasons, the span-based row getter is recommended still
  but this is a convenient thing to do for cell-oriented folks.
  ```
- [`bb375a2`](https://github.com/ghostty-org/ghostty/commit/bb375a2f7565b9d8c8b60c6cbc0bd4e6c4532023) deal with large outputs from xdg-open/rundll32/open ([@jcollie](https://github.com/jcollie))
  ```text
  Depending on your system config, `xdg-open` may stay open for extended
  periods, and potentially log more than the 50kb of output that we were
  previously able to deal with. This changes `open()` so that output on
  `stdout` is just directly ignored. Any output from `stderr` is immedialy
  logged rather than collected for later logging.
  
  Note that this will generally occur if your system is not configured
  with the DBus portals that `xdg-open` uses to open URLs rather than
  launching programs like your web browser directly. This could be seen as
  user misconfiguration but we should deal with it robustly anyway.
  ```
- [`cf9e85e`](https://github.com/ghostty-org/ghostty/commit/cf9e85ecd73cc3f044cab228a75145f63e88ca1d) deal with large outputs from xdg-open/rundll32/open ([#12797](https://github.com/ghostty-org/ghostty/issues/12797)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Depending on your system config, `xdg-open` may stay open for extended
  periods, and potentially log more than the 50kb of output that we were
  previously able to deal with. This changes `open()` so that output on
  `stdout` is just directly ignored. Any output from `stderr` is immedialy
  logged rather than collected for later logging.
  
  Note that this will generally occur if your system is not configured
  with the DBus portals that `xdg-open` uses to open URLs rather than
  launching programs like your web browser directly. This could be seen as
  user misconfiguration but we should deal with it robustly anyway.
  ```

## May 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26373400178)  
Summary: 1 runs • 17 commits • 1 authors

### Changes

- [`ae03d3c`](https://github.com/ghostty-org/ghostty/commit/ae03d3cae4d4af244a43d91a0d8040739899e4a3) libghostty: expose get/set active selection state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add terminal set/get support for the active screen selection through the
  existing option and data APIs. Setting a selection copies the C snapshot
  into terminal-owned tracked state, while passing NULL clears the current
  selection.
  
  Getting the selection now returns an untracked GhosttySelection snapshot
  or GHOSTTY_NO_VALUE when there is no selection. The C header documents
  the different lifetimes for set and get so embedders know when input and
  returned grid references remain valid.
  ```
- [`24048ff`](https://github.com/ghostty-org/ghostty/commit/24048ffd471c5e88006bafc6ab3e5eb3c710a15d) libghostty: expose row-local render selections ([@mitchellh](https://github.com/mitchellh))
  ```text
  Render state already tracks the selected cell range for each viewport row,
  but C renderers could only get the full terminal selection. That required
  consumers to map global selection pins back into row-local spans themselves.
  
  Add row selection data to the render-state row API. Querying the new row
  data returns GHOSTTY_NO_VALUE for unselected rows and writes the inclusive
  start and end columns for selected rows. The render example now demonstrates
  setting a selection and reading the row-local range while iterating rows.
  ```
- [`545a5ae`](https://github.com/ghostty-org/ghostty/commit/545a5aef663ef551bd8b2b2b794f47d9a74d7586) libghostty: document selection snapshot lifetime ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clarify that GhosttySelection is a snapshot type whose endpoints are
  untracked GhosttyGridRef values. The previous documentation described the
  range shape but did not repeat the grid reference lifetime caveat, which
  made it easy to keep selections across terminal mutations incorrectly.
  ```
- [`15d8963`](https://github.com/ghostty-org/ghostty/commit/15d89636814ac0d8d0beb783da0dee6ba63f8f7c) libghostty: add selection adjustment api ([@mitchellh](https://github.com/mitchellh))
- [`4a77e81`](https://github.com/ghostty-org/ghostty/commit/4a77e8196720088cbdce701c88412d3ba16089b5) libghostty: add selection ordering APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose selection endpoint ordering through the libghostty-vt C API so
  embedders can safely normalize selections whose start and end refs may be
  reversed. The new APIs report the current order and return a fresh
  untracked selection with forward or reverse bounds.
  
  Selection.Order now uses lib.Enum, matching the existing adjustment enum
  pattern and keeping the C ABI enum generated from the same Zig source of
  truth. The new functions are wired through the C API re-export and lib-vt
  export paths, with coverage for mirrored rectangular selection ordering.
  ```
- [`671c12f`](https://github.com/ghostty-org/ghostty/commit/671c12fad9f85c8b384773c3ba936b07b4af45bf) libghostty: add selection contains API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose a C API for checking whether a GhosttyPoint is inside a
  GhosttySelection. The new terminal helper validates the selection snapshot
  against the active screen, resolves the point to a grid pin, and delegates
  to the internal Selection.contains implementation so C consumers get the
  same linear and rectangular selection semantics as Ghostty.
  
  Wire the symbol through the C API exports and public headers, and add a
  focused test covering linear containment and rectangular selection behavior.
  ```
- [`2512fad`](https://github.com/ghostty-org/ghostty/commit/2512fad9408bf0fee76dda2eae7a401e28d6b18f) libghostty: move selection functions to selection doxygen group ([@mitchellh](https://github.com/mitchellh))
- [`ae83939`](https://github.com/ghostty-org/ghostty/commit/ae839393d9b0a6d6776e816e8a9193c3d6875850) libghostty: add Selection equal and validate ([@mitchellh](https://github.com/mitchellh))
- [`7b49d1f`](https://github.com/ghostty-org/ghostty/commit/7b49d1f12928908de022c00ef5dbc099a66517fb) terminal: PageList.reset needs to reset page serial mins ([@mitchellh](https://github.com/mitchellh))
- [`847b8af`](https://github.com/ghostty-org/ghostty/commit/847b8afc872110f6cfd0c0f4690133904a06da16) libghostty: remove selection validation, way too expensive ([@mitchellh](https://github.com/mitchellh))
- [`cc48312`](https://github.com/ghostty-org/ghostty/commit/cc48312c08a0f0e08f77a8df74c15e9e367ce70e) libghostty: selection word/line/output/all helpers ([@mitchellh](https://github.com/mitchellh))
- [`e8f5353`](https://github.com/ghostty-org/ghostty/commit/e8f53539120e73e06c5bd82ab39dbf1499bf9311) example/c-vt-selection ([@mitchellh](https://github.com/mitchellh))
- [`eb777b8`](https://github.com/ghostty-org/ghostty/commit/eb777b8036d8c457ee181eab136858d1ca86aa88) libghostty: selectWordBetween in C ([@mitchellh](https://github.com/mitchellh))
- [`2ce5db2`](https://github.com/ghostty-org/ghostty/commit/2ce5db29ca162033e3cc570533184e13f3c01b53) libghostty: selection formatting ([@mitchellh](https://github.com/mitchellh))
- [`03df613`](https://github.com/ghostty-org/ghostty/commit/03df613e392b764d828941cb4f5864c5a75edb83) libghostty: detach tracked grid refs on free ([@mitchellh](https://github.com/mitchellh))
  ```text
  Tracked grid references previously held a raw terminal wrapper pointer and
  were required to be freed before the terminal. If callers kept one past
  terminal destruction, later tracked-ref calls could dereference freed
  terminal or page-list memory before detecting that the reference was no
  longer meaningful.
  
  Track live C tracked-grid-ref handles from the terminal wrapper and detach
  them before tearing down terminal storage. Detached refs now report no
  value through the tracked-ref APIs and can still be freed by the caller.
  Update the C API docs to describe this lifetime behavior and add a
  regression test for using a tracked ref after terminal free.
  
  This introduces some overhead but tracked pins shouldn't be numerous
  and this dramatically improves safety.
  ```
- [`5f08694`](https://github.com/ghostty-org/ghostty/commit/5f086947597dba0b5136d52c0b47db1d64fa5dfb) libghostty: selection APIs for C ([#12794](https://github.com/ghostty-org/ghostty/issues/12794)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds libghostty-vt selection APIs read/write, formatting, inspecting,
  and rendering selection state from C.
  
  | Introduced type/function | Purpose |
  | --- | --- |
  | `GhosttyRenderStateRowSelection` | Row-local inclusive selection range
  returned by render row queries. |
  | `GhosttyTerminalSelectWordOptions` | Options for deriving a word
  selection from a grid ref. |
  | `GhosttyTerminalSelectWordBetweenOptions` | Options for finding the
  nearest selectable word between two refs. |
  | `GhosttyTerminalSelectLineOptions` | Options for deriving line
  selections, including semantic prompt boundaries. |
  | `GhosttyTerminalSelectionFormatOptions` | Options for formatting the
  active or caller-provided selection. |
  | `GhosttySelectionOrder` | Describes endpoint ordering, including
  rectangular mirrored orders. |
  | `GhosttySelectionAdjust` | Operations for moving a selection endpoint.
  |
  | `ghostty_terminal_select_word` | Derive a word selection snapshot. |
  | `ghostty_terminal_select_word_between` | Derive the nearest word
  selection between two refs. |
  | `ghostty_terminal_select_line` | Derive a line selection snapshot. |
  | `ghostty_terminal_select_all` | Derive a selection covering all
  selectable content. |
  | `ghostty_terminal_select_output` | Derive a semantic command-output
  selection. |
  | `ghostty_terminal_selection_format_buf` | Format a selection into a
  caller-provided buffer. |
  | `ghostty_terminal_selection_format_alloc` | Format a selection into an
  allocated buffer. |
  | `ghostty_terminal_selection_adjust` | Mutate a selection snapshot
  endpoint. |
  | `ghostty_terminal_selection_order` | Query selection endpoint order. |
  | `ghostty_terminal_selection_ordered` | Return a selection with
  normalized endpoint order. |
  | `ghostty_terminal_selection_contains` | Test whether a point is inside
  a selection. |
  | `ghostty_terminal_selection_equal` | Compare two selection snapshots
  using terminal semantics. |
  ```
- [`c5946f4`](https://github.com/ghostty-org/ghostty/commit/c5946f4fefd9382ba00d21c1bed0b6ff33a1b687) libghostty: detach tracked grid refs on free ([#12795](https://github.com/ghostty-org/ghostty/issues/12795)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Tracked grid references previously held a raw terminal wrapper pointer
  and were required to be freed before the terminal. If callers kept one
  past terminal destruction, later tracked-ref calls could dereference
  freed terminal or page-list memory before detecting that the reference
  was no longer meaningful.
  
  Track live C tracked-grid-ref handles from the terminal wrapper and
  detach them before tearing down terminal storage. Detached refs now
  report no value through the tracked-ref APIs and can still be freed by
  the caller. Update the C API docs to describe this lifetime behavior and
  add a regression test for using a tracked ref after terminal free.
  
  This introduces some overhead but tracked pins shouldn't be numerous and
  this dramatically improves safety.
  
  No API changes due to this (just more safety).
  ```

## May 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26344833525), [2](https://github.com/ghostty-org/ghostty/actions/runs/26344470484), [3](https://github.com/ghostty-org/ghostty/actions/runs/26327527612)  
Summary: 3 runs • 9 commits • 4 authors

### Changes

- [`7a346dd`](https://github.com/ghostty-org/ghostty/commit/7a346dd8d40e21b14c96114c45f75eb0d347c236) macOS: fix search bar Enter key blocking IME composition ([@minorcell](https://github.com/minorcell))
  ```text
  Use onSubmit for the plain Enter → next-match behavior, which respects
  IME composition state. Keep onKeyPress only for Shift+Enter (previous
  match), returning .ignored for plain Enter so the IME can process it.
  ```
- [`da541be`](https://github.com/ghostty-org/ghostty/commit/da541bea6333458c5f4a987e734269e019a2103d) fix stray brace from conflict resolution ([@minorcell](https://github.com/minorcell))
- [`d5d8cef`](https://github.com/ghostty-org/ghostty/commit/d5d8cef4d3834cc8999eb9344066b0960b033f2d) macOS: fix search bar Enter key blocking IME composition ([#12781](https://github.com/ghostty-org/ghostty/issues/12781)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes https://github.com/ghostty-org/ghostty/discussions/12774
  
  `.onKeyPress(.return)` unconditionally returns `.handled`, so when IME
  is composing the return key never reaches the IME to confirm the
  candidate. The search bar gets stuck.
  
  The fix: use `.onSubmit` for the next-match navigation — it only fires
  when there is no composing text. In `.onKeyPress` only intercept
  shift+return (previous match), return `.ignored` otherwise.
  
  Tested on macOS 26.5, Ghostty 1.3.1, built from source. Chinese Pinyin
  input in the search bar works correctly after the fix.
  ```
- [`1b3c5b5`](https://github.com/ghostty-org/ghostty/commit/1b3c5b57ff50c4241c612337bc202c12823cc5d8) Update VOUCHED list ([@github-actions[bot]](https://github.com/apps/github-actions))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/12775#discussioncomment-DC_kwDOHFhdAs4BA9x5
  ```
- [`2355550`](https://github.com/ghostty-org/ghostty/commit/2355550a9410f0f10bc1e88e677a9f9ed091bb71) libghostty: add tracked grid ref API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C API for tracked pins, known as a tracked grid ref in C.
  
  The new API can create tracked refs from terminal points, snapshot them
  back to regular grid refs for cell access, convert them to coordinates,
  move them to a new point, report when their semantic location was lost,
  and free the tracked pin bookkeeping. This is backed by PageList tracked
  pins and exposed through the libghostty-vt export layer and headers.
  ```
- [`60f767d`](https://github.com/ghostty-org/ghostty/commit/60f767dd84cac94d5a6f4e827847361c42d1c078) core: guard surface left-click pins with screen generations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Left-click mouse state stored a tracked pin with only the screen key that
  owned it. If the alternate screen was removed and later recreated, the key
  could match again even though the stored pin belonged to destroyed PageList
  storage.
  
  Store the screen generation alongside the left-click pin and resolve the
  pin through helpers that require both the key and generation to match. This
  keeps selection scrolling, link hover checks, pressure selection, and drag
  selection from dereferencing stale tracked pins after screen teardown.
  ```
- [`af94eac`](https://github.com/ghostty-org/ghostty/commit/af94eac1e1f26bee94b84f7d0076776dd3514d05) libghostty: add tracked grid ref API ([#12785](https://github.com/ghostty-org/ghostty/issues/12785)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C API for tracked pins, known as a tracked grid ref in C.
  
  The new API can create tracked refs from terminal points, snapshot them
  back to regular grid refs for cell access, convert them to coordinates,
  move them to a new point, report when their semantic location was lost,
  and free the tracked pin bookkeeping. This is backed by PageList tracked
  pins and exposed through the libghostty-vt export layer and headers.
  ```
- [`7c3d950`](https://github.com/ghostty-org/ghostty/commit/7c3d9502dc6374d2563c30629f354fcd5251f141) Update VOUCHED list ([#12779](https://github.com/ghostty-org/ghostty/issues/12779)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12775#discussioncomment-17030265)
  from @bo2themax.
  
  Vouch: @minorcell
  ```
- [`a968e12`](https://github.com/ghostty-org/ghostty/commit/a968e120dd084bd886239d1cac938f0177f019d9) Update VOUCHED list ([#12780](https://github.com/ghostty-org/ghostty/issues/12780)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12775#discussioncomment-17030265)
  from @bo2themax.
  
  Vouch: @minorcell
  ```

## May 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26299049671), [2](https://github.com/ghostty-org/ghostty/actions/runs/26262927116)  
Summary: 2 runs • 33 commits • 9 authors

### Changes

- [`3c2c596`](https://github.com/ghostty-org/ghostty/commit/3c2c596dc77679385e18039052e2b7556049e07f) fix global keybinds from not repsonding anymore ([@adrum](https://github.com/adrum))
- [`3828660`](https://github.com/ghostty-org/ghostty/commit/3828660382483a9eae10c0a4e4c3d0ae826d3aed) Merge branch 'main' into fix/keybind ([@adrum](https://github.com/adrum))
- [`484d6ec`](https://github.com/ghostty-org/ghostty/commit/484d6ec66b0c27808341c05eb71416a39517ad03) cli: add an ssh-wrapping +ssh action ([@jparise](https://github.com/jparise))
  ```text
  Add a drop-in `ssh` wrapper that sets up the remote environment for
  Ghostty. Anything not consumed as one of our own flags is forwarded to
  the real, wrapped `ssh` binary. It can be used directly (`ghostty +ssh
  user@host`), aliased (`alias ssh='ghostty +ssh --'`), or invoked through
  Ghostty's shell integration.
  
  Before exec'ing ssh, `+ssh`:
  
  - Forwards Ghostty environment to the remote (`--forward-env`): sets
    TERM=xterm-256color and requests SendEnv forwarding of COLORTERM,
    TERM_PROGRAM, and TERM_PROGRAM_VERSION.
  - Installs Ghostty's terminfo on the remote (`--terminfo`), informed by
    our existing `ssh-cache` system and using our internal xterm-ghostty
    terminfo representation.
  
  A third flag, `--cache`, controls cache use; `--cache=false` bypasses
  both read and write, which is useful for scripting and for debugging
  install failures without polluting the cache.
  
  For shell integration, this replaces the per-shell logic (which made up
  roughly a third of our shell integration scripts) with a simple wrapper
  function that translates GHOSTTY_SHELL_FEATURES into a `ghostty +ssh`
  command line. This commit only migrates the bash integration; the other
  shells will follow separately.
  ```
- [`2d11205`](https://github.com/ghostty-org/ghostty/commit/2d112059a7e87104a483866ff472638e3ebd81b1) zsh: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line. The shell
  wrapper no longer carries terminfo install, ControlMaster wiring, or
  cache bookkeeping; it just maps the feature flags to flags on `+ssh`
  and forwards everything else.
  ```
- [`283dca1`](https://github.com/ghostty-org/ghostty/commit/283dca130e02945aed1d3f2eae43676d37782717) fish: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line.
  ```
- [`e537810`](https://github.com/ghostty-org/ghostty/commit/e5378107eb8ffff72ba98eab45092b569f56bcf0) elvish: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line.
  ```
- [`ac103b8`](https://github.com/ghostty-org/ghostty/commit/ac103b8f75f5206af3cc98deecc2b7d0f9705683) nushell: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line. When no
  ssh-* feature is enabled, the wrapper falls through to the real `ssh`
  binary unchanged so nushell users without ssh integration get plain
  ssh behavior.
  ```
- [`3f11e69`](https://github.com/ghostty-org/ghostty/commit/3f11e695d0fd8f3cabc2c46c7a091c0509884b41) fix: apply variation selectors to preceding codepoint ([@noib3](https://github.com/noib3))
  ```text
  This fixes a bug where the variation selectors (VS15 & VS16) were
  checked against the first codepoint in a cell instead of the previous
  codepoint in the cell's grapheme cluster, causing them to be dropped if
  the first codepoint was not a valid base.
  ```
- [`c44afa6`](https://github.com/ghostty-org/ghostty/commit/c44afa62506dd94b9dcc680da412ddb650931b3b) fix: preserve active cursor position during reflow ([@noib3](https://github.com/noib3))
  ```text
  This PR fixes an issue where reflowing could leave the active cursor
  attached to a clipped trailing blank cell instead of following the
  current write position.
  ```
- [`366c348`](https://github.com/ghostty-org/ghostty/commit/366c34831a39651b196f216f1e9fd651568b60b8) macOS: fix first responder after dragging a non-focused surface ([@bo2themax](https://github.com/bo2themax))
  ```text
  This fixes a bug: after dragging a non-focused surface from window A to window B **quickly without making B the key window**, the focused surface in window A is not receiving `keyDown` events.
  ```
- [`2c6dd59`](https://github.com/ghostty-org/ghostty/commit/2c6dd5940688643604f82cd50fd426a463e78d56) macOS: fix render_thread "stuck" after dragging surface to another tab within the same window ([@bo2themax](https://github.com/bo2themax))
  ```text
  The reason the thread is stuck is because the surface's occlusion state is set to invisible after target tab's activate while dragging, since the dragged surface is still in previous tree before dropping, and after dropping the occlusion state of this surface is not updated to visible, which causing the surface is accepting input but not rendering.
  ```
- [`0226bcf`](https://github.com/ghostty-org/ghostty/commit/0226bcf034a0ba040ae4178336144f9df80e4c6e) macOS: update window appearance for About and ConfigurationErrors ([@bo2themax](https://github.com/bo2themax))
- [`59eece9`](https://github.com/ghostty-org/ghostty/commit/59eece9a8edebf29f59d7d1b627cbc97c1363924) feat: use find pasteboard to store search needle ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`8fa42c6`](https://github.com/ghostty-org/ghostty/commit/8fa42c6ec0b2be97148ec7e90c00e3cc58d5c589) feat: add search state unit tests ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`69cab3d`](https://github.com/ghostty-org/ghostty/commit/69cab3d8085d0731574f4498864ced901e55c8b0) feat: select needle when reading from pasteboard ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`ed52160`](https://github.com/ghostty-org/ghostty/commit/ed521606122cde73f0072abc6a7caa5da7dc4829) feat: support BackportSelectionTextField on iOS 18 ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`bf716a0`](https://github.com/ghostty-org/ghostty/commit/bf716a0c3940ef9a77a4a5d38581e83c0ad44411) feat: add extension to normalize OSPasteboard string interface ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`7f5c233`](https://github.com/ghostty-org/ghostty/commit/7f5c233492c40e26d6e58e25b4ad07617e728ea4) macOS: add `windowCanBeClosedWithoutConfirmation` without any side effects ([@bo2themax](https://github.com/bo2themax))
- [`8f9b86a`](https://github.com/ghostty-org/ghostty/commit/8f9b86afa8d48afe94e2b895c8442f670c4a0b9b) macOS: add confirmCloseAsync to return the actual response ([@bo2themax](https://github.com/bo2themax))
- [`00a9897`](https://github.com/ghostty-org/ghostty/commit/00a989774e23d4c6035f5565a167be63e22c788d) macOS: add review windows when quitting ([@bo2themax](https://github.com/bo2themax))
  ```text
  Inspired by Terminal.app
  ```
- [`88d30bb`](https://github.com/ghostty-org/ghostty/commit/88d30bb30a02459a97e49fbb0817748422d6f65a) gtk: wire occlusionCallback to GLArea map/unmap ([@mjbommar](https://github.com/mjbommar))
  ```text
  Calls core_surface.occlusionCallback(visible) from the existing
  glareaMap/glareaUnmap handlers (added in #12698) so the renderer
  thread learns when a surface is off-screen.
  ```
- [`14d9e60`](https://github.com/ghostty-org/ghostty/commit/14d9e600acf274f9b04da0dd2695d092aa93c3b6) renderer: skip updateFrame when surface is not visible ([@mjbommar](https://github.com/mjbommar))
  ```text
  renderCallback early-returns while !flags.visible to avoid the
  cell rebuild for hidden surfaces (tab switch, minimize, etc.).
  The .visible → true mailbox handler now runs updateFrame before
  drawFrame so the first frame after re-show isn't stale.
  ```
- [`ec15d0e`](https://github.com/ghostty-org/ghostty/commit/ec15d0e7db3d8079f0e109d0abc9323b750646ba) gtk: wire up occlusionCallback for non-focused tabs ([#12760](https://github.com/ghostty-org/ghostty/issues/12760)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  As discussed in #12745, there has been an outstanding plan to make
  rendering behavior for non-focused surfaces consistent across platforms.
  This PR does that for Linux/GTK using the same patterns as OSX.
  
  The change in `src/apprt/gtk/class/surface.zig` piggybacks on the
  existing `glareaMap` / `glareaUnmap` callbacks (added by `e59e27f8b`) by
  also calling a new `updateOcclusion(bool)` helper. If you don't like the
  helper, or want the helper lifted up further and used on other paths,
  let me know and I can revise.
  
  The changes in `src/renderer/Thread.zig` bail on `renderCallback` when
  not visible and then block on `drainMailbox` to complete the "catch up"
  before trying to draw again.
  
  I want to note that this is more granular than the original #1512, which
  was just focused on the top level window state. I can look at that as
  well if you want, but given the complexity around how
  `XDG_TOPLEVEL_STATE_SUSPENDED` event is fired, I would want to make sure
  we discussed things like transparency and single-instance properly first
  (e.g., do we render when behind another transparent window).
  
  ## Testing
  
  Here's a summary of what I tested:
  
  Tested on Linux/GTK (Ubuntu 26.04, GTK 4.22.2, libadwaita 1.9.0,
  Wayland), built `ReleaseFast`. The patched binary has been daily-driven
  for ~24 hours as my primary terminal.
  
  | Test | Workload | Result |
  |---|---|---|
  | Daily drive | byobu × multiple SSH sessions, Claude Code and Codex
  producing sustained streaming output, `top` / `btop` redrawing on 1 s
  intervals, frequent tab switching | No observed issues over ~24 hours of
  mixed use |
  | Bell on hidden tab | `sleep 5 && printf '\a'` in background tab | Bell
  + needs-attention indicator both fire; confirms IO-thread → GTK-signal
  path is untouched |
  | Search highlight survives hide/show | Open search w/ matches
  highlighted in tab B → switch to tab A for ~10 s → switch back |
  Highlights restored instantly with no stale state; confirms
  deferred-replay path (`updateFrame` on `.visible → true`) works
  correctly |
  | Selection persistence | Select text in tab B → switch tabs → switch
  back | Selection preserved exactly |
  | Lifecycle (close-all) | Opened 8 surfaces, closed them one at a time,
  then process exit + systemd restart | Zero `glib-CRITICAL`, zero `error
  in occlusion callback ...` warnings, clean teardown per `journalctl
  --user -u app-com.mitchellh.ghostty` |
  | Per-thread CPU during workload | `pidstat -t -p <pid>` 30 s with 1
  byobu surface focused, 1 background | Hidden surface's renderer thread
  sits at 0.00 % every sample; focused surface's renderer shows ~1 % blips
  on byobu status ticks |
  
  
  
  ## AI usage
  
  Claude Code (Opus 4.7) helped review my patch and monitor / summarize
  the jorunald log and pidstat entries.
  ```
- [`52f23fb`](https://github.com/ghostty-org/ghostty/commit/52f23fb4190d7f1830635c4171e33f3f394d3919) macOS: review windows when quitting ([#12742](https://github.com/ghostty-org/ghostty/issues/12742)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Inspired by `Terminal.app` which I think is a nice feature.
  
  First two commits contains some changes in `BaseTerminalController` so
  that I can use swift concurrency to review those windows in chain more
  easily.
  
  
  
  https://github.com/user-attachments/assets/41d92432-4ae0-499e-961a-fc247602f3d7
  
  
  Works with tabs as well, i forgot to record that.
  ```
- [`afe4819`](https://github.com/ghostty-org/ghostty/commit/afe4819920036d2d85edc75ccf757404f45632f0) macOS: Re-enable global keybinds after event tap disable events ([#12714](https://github.com/ghostty-org/ghostty/issues/12714)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  While testing https://github.com/ghostty-org/ghostty/pull/9857, I
  encountered the behavior mentioned below. It's pretty frustrating to
  encounter, so I've been actually compiling this fix into my test builds
  for last month or so, and the issue has not come back. I exclusively use
  the QuickTerminal, so my workflow depends on global keybinds working
  reliably.
  
  Issue: https://github.com/ghostty-org/ghostty/issues/12294
  
  The solution includes listening to two events that are fired when a tap
  is disabled:
  - tapDisabledByTimeout
  - tapDisabledByUserInput
  
  When these are fired, we re-enable the tap.
  
  Apple's Docs:
  https://developer.apple.com/documentation/coregraphics/cgeventtype?language=swift
  
  Related Discussions:
  - https://github.com/ghostty-org/ghostty/discussions/11819
  - https://github.com/ghostty-org/ghostty/discussions/12091
  ```
- [`7e24f0e`](https://github.com/ghostty-org/ghostty/commit/7e24f0e0bc771d48c8a3db49bc18425318c0794e) macOS: use find pasteboard for search needle ([#12712](https://github.com/ghostty-org/ghostty/issues/12712)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the issue described in #12516.
  
  ### What
  - Inject an `OSPasteboard` into `SearchState`
  - Add `OSPasteboard` extension to normalize working with strings between
  UIPasteboard/NSPasteboard
  - Add `BackportSelectionTextField` which supports text selection for
  MacOS 15/iOS 18 and up.
  - Read from the pasteboard when the overlay opens and when the app
  becomes active
  - Write to the pasteboard when the search needle changes
  - Annotate `SearchState` as MainActor. `NSPasteboard` isn't thread safe,
  and since `SearchState` is already accessed from the main thread,
  MainActor enforces our writes be thread safe
  - Add SearchState unit tests
  
  ### Why
  Consistent with other macOS apps, the Find bar's search needle should
  persist when re-opened and should sync to the Find bar in other apps.
  For example, see Xcode, Notes, Terminal, and Safari.
  
  
  https://github.com/user-attachments/assets/b6a55a4a-a52c-45bc-ac38-c9df452c11cb
  ```
- [`b78174a`](https://github.com/ghostty-org/ghostty/commit/b78174a68f6a97c487fe5ee4e0c155433f4a03d9) macOS: update window appearance for About and ConfigurationErrors ([#12601](https://github.com/ghostty-org/ghostty/issues/12601)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="1224" height="696" alt="Xnip2026-05-06_19-13-31"
  src="https://github.com/user-attachments/assets/ab090dc0-7c06-4a01-8e7c-5d48ca6ccca3"
  />
  ```
- [`24d664f`](https://github.com/ghostty-org/ghostty/commit/24d664f0ba1074c4c1047da7a239bd1cf6bdf7af) fix: apply variation selectors to preceding codepoint ([#12596](https://github.com/ghostty-org/ghostty/issues/12596)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a bug where the variation selectors (VS15 & VS16) were
  checked against the first codepoint in a cell instead of the previous
  codepoint in the cell's grapheme cluster, causing them to be dropped if
  that first codepoint was not a valid base.
  ```
- [`a03b52e`](https://github.com/ghostty-org/ghostty/commit/a03b52e18b26048dbd71c08764cb011044edfd3a) fix: preserve active cursor position during reflow ([#12598](https://github.com/ghostty-org/ghostty/issues/12598)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR fixes an issue where reflowing could leave the active cursor
  attached to a clipped trailing blank cell instead of following the
  current write position.
  ```
- [`f5aa271`](https://github.com/ghostty-org/ghostty/commit/f5aa271d07f97f68886153f2d741f50ec060ba9b) cli: add an ssh-wrapping +ssh action ([#12582](https://github.com/ghostty-org/ghostty/issues/12582)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a drop-in `ssh` wrapper that sets up the remote environment for
  Ghostty. Anything not consumed as one of our own flags is forwarded to
  the real, wrapped `ssh` binary. It can be used directly (`ghostty +ssh
  user@host`), aliased (`alias ssh='ghostty +ssh --'`), or invoked through
  Ghostty's shell integration.
  
  Before exec'ing ssh, `+ssh`:
  
  - Forwards Ghostty environment to the remote (`--forward-env`): sets
  TERM=xterm-256color and requests SendEnv forwarding of COLORTERM,
  TERM_PROGRAM, and TERM_PROGRAM_VERSION.
  - Installs Ghostty's terminfo on the remote (`--terminfo`), informed by
  our existing `ssh-cache` system and using our internal xterm-ghostty
  terminfo representation.
  
  A third flag, `--cache`, controls cache use; `--cache=false` bypasses
  both read and write, which is useful for scripting and for debugging
  install failures without polluting the cache.
  
  For shell integration, this replaces the per-shell logic (which made up
  roughly a third of our shell integration scripts) with a simple wrapper
  function that translates GHOSTTY_SHELL_FEATURES into a `ghostty +ssh`
  command line.
  ```
- [`3e3705b`](https://github.com/ghostty-org/ghostty/commit/3e3705b93233480f18274620f5e57c1c7021bf85) macOS: fix surface focus/render state after dragging in to to another window/tab ([#12338](https://github.com/ghostty-org/ghostty/issues/12338)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes 2 bugs
  
  1. After dragging a non-focused surface from window A to window B
  **quickly without making B the key window**, the focused surface in
  window A is not receiving `keyDown` events.
  
  
  https://github.com/user-attachments/assets/a8861c0a-9300-470d-bf7e-0f32a9ab2cd1
  
  2. #12343 After dragging a surface from tab A to tab B within the same
  window, the dragged surface is not rendering input correctly.
  > The reason the thread is stuck is because the surface's occlusion
  state is set to invisible after target tab's activate while dragging,
  since the dragged surface is still in previous tree before dropping, and
  after dropping the occlusion state of this surface is not updated to
  visible, which causing the surface is accepting input but not rendering.
  
  
  
  https://github.com/user-attachments/assets/d67f5dba-8609-4f67-a956-921982faf796
  ```
- [`cb79efa`](https://github.com/ghostty-org/ghostty/commit/cb79efa779ce05535797ff191bd0b7ce06b2ea77) build(deps): bump docker/build-push-action from 7.1.0 to 7.2.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 7.1.0 to 7.2.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/bcafcacb16a39f128d818304e6c9c0c18556b85f...f9f3042f7e2789586610d6e8b85c8f03e5195baf)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.2.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`10c6121`](https://github.com/ghostty-org/ghostty/commit/10c6121458c8a03e7b7804c00291292d7a811ecf) build(deps): bump docker/build-push-action from 7.1.0 to 7.2.0 ([#12765](https://github.com/ghostty-org/ghostty/issues/12765)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 7.1.0 to 7.2.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.2.0</h2>
  <ul>
  <li>Bump <code>@​actions/core</code> from 3.0.0 to 3.0.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1525">docker/build-push-action#1525</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.87.0 to 0.90.0 in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1517">docker/build-push-action#1517</a></li>
  <li>Bump brace-expansion from 2.0.2 to 5.0.6 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1534">docker/build-push-action#1534</a></li>
  <li>Bump fast-xml-builder from 1.1.4 to 1.2.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1529">docker/build-push-action#1529</a></li>
  <li>Bump fast-xml-parser from 5.5.7 to 5.8.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1521">docker/build-push-action#1521</a></li>
  <li>Bump postcss from 8.5.6 to 8.5.10 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1526">docker/build-push-action#1526</a></li>
  <li>Bump tar from 6.2.1 to 7.5.15 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1533">docker/build-push-action#1533</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v7.1.0...v7.2.0">https://github.com/docker/build-push-action/compare/v7.1.0...v7.2.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/f9f3042f7e2789586610d6e8b85c8f03e5195baf"><code>f9f3042</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1517">#1517</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/812d5fd9212a4c5d419e5be02fd8e9bb435c5d76"><code>812d5fd</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/b6f66930769f2917a3275dc4d81f15583ac7e105"><code>b6f6693</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.87.0 to
  0.90.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/c1c626eced73a500ec65c4256c620b3b9e8278c0"><code>c1c626e</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1525">#1525</a>
  from docker/dependabot/npm_and_yarn/actions/core-3.0.1</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/51bb284cd4d05650aa6f5e4e22cb96d2cbfe62b7"><code>51bb284</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/5f7884def8f133e8ef40c53d003d1471c05621c6"><code>5f7884d</code></a>
  chore(deps): Bump <code>@​actions/core</code> from 3.0.0 to 3.0.1</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/e01deff7d956c756a20f3e19ff7ddc0e4a50fc1d"><code>e01deff</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1521">#1521</a>
  from docker/dependabot/npm_and_yarn/fast-xml-parser-...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/3804d497934b39bd591ee9d1c6c9e593b4488a67"><code>3804d49</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/71e8947aac5dad23ce83a43e9c98f750e02de2f3"><code>71e8947</code></a>
  chore(deps): Bump fast-xml-parser from 5.5.7 to 5.8.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/4925ad24cdbc42ff492d76cf9fe7a30b79976b60"><code>4925ad2</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1526">#1526</a>
  from docker/dependabot/npm_and_yarn/postcss-8.5.10</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/bcafcacb16a39f128d818304e6c9c0c18556b85f...f9f3042f7e2789586610d6e8b85c8f03e5195baf">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=7.1.0&new-version=7.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## May 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26177391439), [2](https://github.com/ghostty-org/ghostty/actions/runs/26172134530), [3](https://github.com/ghostty-org/ghostty/actions/runs/26165647879), [4](https://github.com/ghostty-org/ghostty/actions/runs/26139523610)  
Summary: 4 runs • 7 commits • 6 authors

### Changes

- [`4f94afd`](https://github.com/ghostty-org/ghostty/commit/4f94afdb4b25b52583eef6c03217b8bb561c9ad6) vouch: enable auto-locking closed issues ([@trag1c](https://github.com/trag1c))
- [`46d54ed`](https://github.com/ghostty-org/ghostty/commit/46d54ed673a004df09078bee56e809421a82370e) vouch: enable auto-locking closed issues ([#12752](https://github.com/ghostty-org/ghostty/issues/12752)) ([@mitchellh](https://github.com/mitchellh))
- [`41878d6`](https://github.com/ghostty-org/ghostty/commit/41878d6f7977d4758ea15b6599ee7d025be40ecc) snap: export TERMINFO_DIRS so child shells find xterm-ghostty ([@aaron-ang](https://github.com/aaron-ang))
  ```text
  Without this, shells spawned by ghostty cannot find the xterm-ghostty
  terminfo entry because ncurses only searches standard system paths.
  The snap's terminfo lives inside the snap sandbox and is inaccessible
  unless TERMINFO_DIRS is set explicitly.
  ```
- [`2559654`](https://github.com/ghostty-org/ghostty/commit/25596541ec42f08d2a98ac54337b81a6244a5328) snap: export TERMINFO_DIRS so child shells find xterm-ghostty ([#12662](https://github.com/ghostty-org/ghostty/issues/12662)) ([@kenvandine](https://github.com/kenvandine))
  ````text
  ## Summary
  
  When Ghostty is installed via snap on Ubuntu, programs running inside
  Ghostty (e.g. `clear`) fail with:
  
  ```
  terminals database is inaccessible
  ```
  
  The snap ships terminfo at `${SNAP}/share/terminfo` but the launcher
  never exports `TERMINFO_DIRS`, so ncurses in child shells falls back to
  the host's system database. On Ubuntu 24.04 (ncurses 6.4) the system
  database predates the `xterm-ghostty` entry, so the lookup fails.
  
  This is the same fix as the auto-closed #12303 and resolves #12304.
  
  ## Fix
  
  Export `TERMINFO_DIRS` in `snap/local/launcher` so all child processes
  can resolve the bundled entry without manual setup.
  
  ## Local build (how this PR was verified)
  
  Remix the installed store snap by swapping `app/launcher` with the
  patched one:
  
  ```sh
  sudo unsquashfs -d /tmp/g \
    /var/lib/snapd/snaps/ghostty_$(readlink /snap/ghostty/current).snap
  sudo cp snap/local/launcher /tmp/g/app/launcher
  sudo mksquashfs /tmp/g /tmp/ghostty-test.snap -comp xz -noappend
  sudo snap install --dangerous --classic /tmp/ghostty-test.snap
  ```
  
  Then launch `/snap/bin/ghostty` and run `clear`.
  
  ## Test plan
  
  Verified locally on Ubuntu 24.04 / arm64.
  
  - [x] In default `zsh` / `bash` inside Ghostty, `clear` succeeds.
  - [x] `infocmp xterm-ghostty` resolves to
  `/snap/ghostty/current/share/terminfo/x/xterm-ghostty`.
  - [x] No manual copying of terminfo entries into `~/.terminfo/`
  required.
  
  ## AI Disclosure
  
  Claude Code was used to investigate the root cause and to draft this
  single-line launcher change. The fix is identical to the proposal in the
  linked discussion (#12304). I manually verified by remixing the
  installed snap with the patched launcher and confirming `clear` and
  `infocmp xterm-ghostty` work without manually copying terminfo entries
  into `~/.terminfo/` (original workaround shared in the discussion).
  ````
- [`7c2b29a`](https://github.com/ghostty-org/ghostty/commit/7c2b29a9f3047b2f73d632546c51cfbe52fd6a7b) build(highway): require `apple_sdk` for darwin builds ([@elias8](https://github.com/elias8))
- [`8644415`](https://github.com/ghostty-org/ghostty/commit/86444156b403e7dd79ea7f0b2854be76927875b1) build(highway): require `apple_sdk` for darwin builds ([#12725](https://github.com/ghostty-org/ghostty/issues/12725)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Noticed this was removed in another PR, but `apple_sdk` is required to
  build libghsotty for the iOS simulator, specifically for the x86 version
  (see the error log
  [here](https://github.com/elias8/libghostty/actions/runs/26075576793/job/76666498246)).
  Figured it'd be better to include the SDK in all darwin builds for
  consistency.
  ```
- [`19e20f7`](https://github.com/ghostty-org/ghostty/commit/19e20f7664dc7a755d2d7a16ab545b2503f26caf) Update VOUCHED list ([#12746](https://github.com/ghostty-org/ghostty/issues/12746)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12745#discussioncomment-16984203)
  from @jcollie.
  
  Vouch: @mjbommar
  ```

## May 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26123808733), [2](https://github.com/ghostty-org/ghostty/actions/runs/26110763000)  
Summary: 2 runs • 6 commits • 3 authors

### Changes

- [`9bcb30a`](https://github.com/ghostty-org/ghostty/commit/9bcb30aa119b20833d74d4e32104dafe20bd8203) Update VOUCHED list ([#12744](https://github.com/ghostty-org/ghostty/issues/12744)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12743#discussioncomment-16981434)
  from @bo2themax.
  
  Vouch: @b0uks
  ```
- [`aed6461`](https://github.com/ghostty-org/ghostty/commit/aed646139d2a8571c4d4048158e6a6f0c8b353e0) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`fdf84ef`](https://github.com/ghostty-org/ghostty/commit/fdf84ef7ce611b4374d5cef3e213f155fae26914) macOS: check the resource the URL refers to. ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes #12727. [`NSURL.hasDirectoryPath` doesn't do this](https://developer.apple.com/documentation/foundation/nsurl/hasdirectorypath).
  
  We don't need to check this in NewTerminalIntent since AppIntent already appends `/` to the directory.
  ```
- [`3ac7562`](https://github.com/ghostty-org/ghostty/commit/3ac75627910232ac761e8e932a2850123243d5a3) macOS: set error when there is no directory to open with ([@bo2themax](https://github.com/bo2themax))
- [`5f2f08e`](https://github.com/ghostty-org/ghostty/commit/5f2f08ebda33bf7e1f9f0b80c2c5845b39357f76) macOS: check the resource the URL refers to ([#12731](https://github.com/ghostty-org/ghostty/issues/12731)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Fixes https://github.com/ghostty-org/ghostty/issues/12727.
  [`NSURL.hasDirectoryPath` doesn't do
  this](https://developer.apple.com/documentation/foundation/nsurl/hasdirectorypath).
  
  <img width="977" height="177" alt="image"
  src="https://github.com/user-attachments/assets/94f77277-8ef0-4573-8ae1-0e54f810463f"
  />
  
  > We don't need to check this in NewTerminalIntent since AppIntent
  already appends `/` to the directory.
  
  - Set error when there is no directory to open with
  ```
- [`8150b5b`](https://github.com/ghostty-org/ghostty/commit/8150b5b772343887c76d1a50e79cd844d9d4d5c0) Update iTerm2 colorschemes ([#12711](https://github.com/ghostty-org/ghostty/issues/12711)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260511-160054-2671288
  ```

