> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 3, 2026 at 04:31 UTC.

## June 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26822901695)  
Summary: 1 runs • 3 commits • 2 authors

### Changes

- [`ab82b8a`](https://github.com/ghostty-org/ghostty/commit/ab82b8ab720ce46183a58a55554e4a4a7423e3f5) core: fix use-after-free in Surface.setSelection ([@jparise](https://github.com/jparise))
  ```text
  setSelection captured the previous selection, then called Screen.select
  (which deinits the previous selection's tracked pins), then compared the
  new selection against the now-freed previous pin via `sel.eql(prev)`.
  That read freed pin memory (use-after-free).
  
  The comparison was a copy-on-select optimization ("only re-copy if the
  selection changed"). Remove it rather than repair it because:
  
  - It never fired correctly. It compared against freed memory, so the
    shipped behavior was already "always copy".
  
  - It can't be repaired by copying `prev`'s pin before Screen.select.
    That fixes the use-after-free but not the logic: the call sites (e.g.
    mouse drag release) pass a selection equal to the one already set, so
    a working `eql` skip would suppress the very copy those sites exist to
    perform. A correct optimization would have to compare against the
    last-copied selection (before the mouse event mutated the live one),
    which would require extra state.
  
  - It isn't worth tracking that additional state. The copy runs once per
    selection gesture (mouse up, double-click), which isn't in a hot path,
    so skipping a redundant re-copy only saves a single clipboard write.
  
  Removing the skip eliminates the use-after-free and keeps the behavior
  consistent with what we've already been doing.
  ```
- [`76b9bdb`](https://github.com/ghostty-org/ghostty/commit/76b9bdb1999398fa1b64d000f9a77088af232b62) terminal: test Screen.select frees existing pins ([@jparise](https://github.com/jparise))
- [`6246c28`](https://github.com/ghostty-org/ghostty/commit/6246c288ae1087c8d67f75432a59da004b30bf25) core: fix use-after-free in Surface.setSelection ([#12894](https://github.com/ghostty-org/ghostty/issues/12894)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `setSelection` captured the previous selection, then called
  `Screen.select` (which deinits the previous selection's tracked pins),
  then compared the new selection against the now-freed previous pin via
  `sel.eql(prev)`. That read freed pin memory (use-after-free).
  
  The comparison was a copy-on-select optimization ("only re-copy if the
  selection changed"). Remove it rather than repair it because:
  
  - It never fired correctly. It compared against freed memory, so the
  shipped behavior was already "always copy".
  
  - It can't be repaired by copying `prev`'s pin before `Screen.select`.
  That fixes the use-after-free but not the logic: the call sites (e.g.
  mouse drag release) pass a selection equal to the one already set, so a
  working `eql` skip would suppress the very copy those sites exist to
  perform. A correct optimization would have to compare against the
  last-copied selection (before the mouse event mutated the live one),
  which would require extra state.
  
  - It isn't worth tracking that additional state. The copy runs once per
  selection gesture (mouse up, double-click), which isn't in a hot path,
  so skipping a redundant re-copy only saves a single clipboard write.
  
  Removing the skip eliminates the use-after-free and keeps the behavior
  consistent with what we've already been doing.
  
  ---
  
  _AI Disclosure_: Claude Opus 4.8 found this in a review while I was
  working on adjacent code.
  ```

## June 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26773386588), [2](https://github.com/ghostty-org/ghostty/actions/runs/26770642732)  
Summary: 2 runs • 13 commits • 7 authors

### Changes

- [`d3775d1`](https://github.com/ghostty-org/ghostty/commit/d3775d1ed0a2e41ee8f2ecdb325f6c016b2b3e93) terminal: glyph protocol parser and response encoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds the core parse/encode for the still in-development and experimental
  terminal glyph protocol: https://github.com/raphamorim/rio/pull/1542
  Up to version 1.9.
  
  The only cross-cutting change necessary was changing the APC
  identification logic which previously only looked at a single byte to
  support multi-byte identifiers since the glyph protocol uses `25a1`.
  ```
- [`5758e14`](https://github.com/ghostty-org/ghostty/commit/5758e149319d244cbf2d21d1ae8d1376adaf1f91) terminal: glyph protocol parser and response encoder ([#12352](https://github.com/ghostty-org/ghostty/issues/12352)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Important: this DOES NOT hook up the glyph protocol to Ghostty or
  libghostty. Its just the parser.**
  
  This adds the core parse/encode for the still in-development and
  experimental terminal glyph protocol:
  https://github.com/raphamorim/rio/pull/1542
  
  The only cross-cutting change necessary was changing the APC
  identification logic which previously only looked at a single byte to
  support multi-byte identifiers since the glyph protocol uses `25a1`.
  
  For DoS protection, the default limits any glyph-related APC command
  size to 1 megabyte.
  
  > [!WARNING]
  >
  > Since this protocol is still in development and discussion, there is
  no promise the implementation will stay within Ghostty or that any of
  the APIs exposed by this will remain stable. We're just getting ahead of
  it.
  ```
- [`024880b`](https://github.com/ghostty-org/ghostty/commit/024880b9ca40ecf8a399deff14e422dd32746f68) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`33adb58`](https://github.com/ghostty-org/ghostty/commit/33adb58bee9eeca906e29ee957140275d4903257) macos: remove unneeded initializers ([@jparise](https://github.com/jparise))
  ```text
  These will be automatically synthesized (they only do memberwise
  initialization) and do not need to be manually defined.
  ```
- [`e32d7ab`](https://github.com/ghostty-org/ghostty/commit/e32d7abe6eeae9c3aa557fef2bcfe97a212688c5) macos: fix swiftlint opening_brace issue ([@jparise](https://github.com/jparise))
- [`3e83a54`](https://github.com/ghostty-org/ghostty/commit/3e83a54d08ef4f4820b8a401910c838f4f0636e0) macos: remove unneeded initializers ([#12875](https://github.com/ghostty-org/ghostty/issues/12875)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  These will be automatically synthesized (they only do memberwise
  initialization) and do not need to be manually defined.
  ```
- [`eb5c1c7`](https://github.com/ghostty-org/ghostty/commit/eb5c1c7220121c8616160e10cb1aa664166a06f3) fix(macos): mark Swift os.Logger interpolations as public ([@claude](https://github.com/claude))
- [`a181c38`](https://github.com/ghostty-org/ghostty/commit/a181c386ca938f730c6e802b7931b37ec65f3047) config: fix missing space in docs ([@masterflitzer](https://github.com/masterflitzer))
  ```text
  fixes #12873
  
  comment/docs only change:
  switched space and tab in default value of `selection-word-chars`
  so there is no space at the value boundary
  needed because markdown trims spaces at the beginning & end
  of a code snippet
  ```
- [`c4c9e94`](https://github.com/ghostty-org/ghostty/commit/c4c9e945aefbd0afbfc21a05f76d06e36e10a625) Update VOUCHED list ([#12880](https://github.com/ghostty-org/ghostty/issues/12880)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12879#issuecomment-4587359428)
  from @00-kat.
  
  Vouch: @masterflitzer
  ```
- [`16f2fdc`](https://github.com/ghostty-org/ghostty/commit/16f2fdc90c2ca59ed870c7b3355a337b1fd650b2) config: fix missing space in docs ([#12879](https://github.com/ghostty-org/ghostty/issues/12879)) ([@jcollie](https://github.com/jcollie))
  ```text
  fixes #12873
  
  comment/docs only change:
  switched space and tab in default value of `selection-word-chars` so
  there is no space at the value boundary
  needed because markdown trims spaces at the beginning & end of a code
  snippet
  ```
- [`0f7cd84`](https://github.com/ghostty-org/ghostty/commit/0f7cd84b880b203c98683e520e84b9db0c5938d8) Update VOUCHED list ([#12889](https://github.com/ghostty-org/ghostty/issues/12889)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12840#discussioncomment-17132417)
  from @bo2themax.
  
  Vouch: @52dyd
  ```
- [`b81670f`](https://github.com/ghostty-org/ghostty/commit/b81670f3f439eff8df615257ff70d9ef39e60065) macOS: mark Swift os.Logger interpolations as public ([#12877](https://github.com/ghostty-org/ghostty/issues/12877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### AI Disclosure
  
  Claude implemented it. I'm fully aware of and confident about the
  change; it's just chore work actually.
  ```
- [`43e0340`](https://github.com/ghostty-org/ghostty/commit/43e03401758e8e1e0d23afb3a8e2a00b43e8e8ee) Update iTerm2 colorschemes ([#12867](https://github.com/ghostty-org/ghostty/issues/12867)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260525-155808-7335c0a
  ```

## May 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26674005784)  
Summary: 1 runs • 6 commits • 3 authors

### Changes

- [`37997f8`](https://github.com/ghostty-org/ghostty/commit/37997f8dbe1221f19343e6b9fa907ce2b944f1a2) Use a timeout callback to wait for changes in window active state to settle. Depending on the backend a window might temporarily become inactive. ([@dkinzler](https://github.com/dkinzler))
  ```text
  Fixes an issue where quick-terminal would disappear when opening the surface context menu.
  ```
- [`1753d57`](https://github.com/ghostty-org/ghostty/commit/1753d57bfdf0ac694ac624e7d63ec9fecd220bc6) remove timeout source when window is disposed ([@dkinzler](https://github.com/dkinzler))
- [`ff963f3`](https://github.com/ghostty-org/ghostty/commit/ff963f3119bffbd9366a5b7d98fbcaba06fc9f05) Renamed timeout source and callback function. Added comment explaining timeout delay. ([@dkinzler](https://github.com/dkinzler))
- [`c09ade2`](https://github.com/ghostty-org/ghostty/commit/c09ade225acb0abfea2f845197b227086a76922f) agents: symlink CLAUDE.md to AGENTS.md ([@Uzaaft](https://github.com/Uzaaft))
- [`c4eba3d`](https://github.com/ghostty-org/ghostty/commit/c4eba3da38c629dbd4b8f770da3e0c605f2a7f53) agents: symlink CLAUDE.md to AGENTS.md ([#12861](https://github.com/ghostty-org/ghostty/issues/12861)) ([@jcollie](https://github.com/jcollie))
  ```text
  Claude code [doesn't support AGENTS.md
  files](https://github.com/anthropics/claude-code/issues/6235) so I've
  seen lots of repos symlinking
  ```
- [`2c62d18`](https://github.com/ghostty-org/ghostty/commit/2c62d182cec246764ff725096a70b9ef44996f7f) gtk: fix context menu hiding quick-terminal ([#12843](https://github.com/ghostty-org/ghostty/issues/12843)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #12783 where opening the context menu (with right click) inside
  the quick-terminal will hide the quick-terminal if autohide is enabled.
  
  The cause of this issue is the quick-terminal window becoming inactive
  and immediately active again when you open the context-menu. When the
  window becomes inactive, the autohide feature hides the quick-terminal.
  The temporary focus loss in GTK is triggered by GDK focus change events,
  which probably originate from the windowing backend treating the context
  menu as its own window. Whereas in GTK the context menu is not a
  separate window but instead part of the widget tree of the window it was
  opened from, so even when the context menu has focus that window is
  still the active one in GTK.
  
  As a fix `Window.propIsActive`, which implements the autohide logic,
  will now do its work from a timeout callback, since there is probably no
  reliable way to distinguish a temporary focus loss from a real one from
  inside GTK and I'm not sure we can make any assumptions about the timing
  of things happening in the windowing backend. A 100ms delay should be
  long enough for the focus state to settle while still hiding the
  quick-terminal quickly.
  
  I reproduced the bug and verified the fix on Wayland with both Hyprland
  and KDE. Temporary focus loss happens on X11+KDE as well, although it
  doesn't matter there because there is no quick-terminal.
  
  ### AI Disclosure
  
  No AI was used, code and comments were written by myself.
  ```

## May 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26641829987)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`b771a3d`](https://github.com/ghostty-org/ghostty/commit/b771a3d4f1a2087ec5938e4a653c6926775caf5b) libghostty-vt: preserve shell prompts on resize by default ([@noib3](https://github.com/noib3))
  ```text
  This PR makes libghostty-vt preserve shell prompts across resize unless
  the shell explicitly opts into prompt clearing/redraw with `redraw=1`.
  ```
- [`9017595`](https://github.com/ghostty-org/ghostty/commit/90175950d5004382abd3b0b9528e7be81b0b52ec) libghostty-vt: preserve shell prompts on resize by default ([#12653](https://github.com/ghostty-org/ghostty/issues/12653)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR makes libghostty-vt preserve shell prompts across resize unless
  the shell explicitly opts into prompt clearing/redraw with `redraw=1`.
  ```

## May 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26600341544), [2](https://github.com/ghostty-org/ghostty/actions/runs/26554769180)  
Summary: 2 runs • 5 commits • 1 authors

### Changes

- [`3cf01e8`](https://github.com/ghostty-org/ghostty/commit/3cf01e84453c73e196cd3900d1b30757f4358e84) libghostty: add utf-8 grapheme cell getter to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render-state row-cells getter that encodes the current cell's
  full grapheme cluster directly as UTF-8 into a caller-provided
  GhosttyBuffer. The getter writes the base codepoint first, followed by
  any extra grapheme codepoints, and follows the existing buffer-writer
  convention where len is bytes written on success or required capacity
  on GHOSTTY_OUT_OF_SPACE.
  
  Previously C consumers could query grapheme codepoints, but bindings
  that needed UTF-8 text had to reconstruct and encode the cluster
  themselves. That duplicated terminal internals in downstream bindings
  and made users pay for awkward cross-language struct handling. By
  owning the UTF-8/grapheme behavior in libghostty, bindings can use one
  stable C API and optionally wrap it with small binding-local helpers.
  ```
- [`519a612`](https://github.com/ghostty-org/ghostty/commit/519a612bebf25887973bab4ae22bba85f48a5e6b) libghostty: fix wasm build for selection gesture ([@mitchellh](https://github.com/mitchellh))
- [`cb36966`](https://github.com/ghostty-org/ghostty/commit/cb36966a752982014827a9cabcf630ec3788b3d9) libghostty: add utf-8 grapheme cell getter to C API ([#12847](https://github.com/ghostty-org/ghostty/issues/12847)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render-state row-cells getter that encodes the current cell's full
  grapheme cluster directly as UTF-8 into a caller-provided GhosttyBuffer.
  The getter writes the base codepoint first, followed by any extra
  grapheme codepoints, and follows the existing buffer-writer convention
  where len is bytes written on success or required capacity on
  GHOSTTY_OUT_OF_SPACE.
  
  Previously C consumers could query grapheme codepoints, but bindings
  that needed UTF-8 text had to reconstruct and encode the cluster
  themselves. That duplicated terminal internals in downstream bindings
  and made users pay for awkward cross-language struct handling. By owning
  the UTF-8/grapheme behavior in libghostty, bindings can use one stable C
  API and optionally wrap it with small binding-local helpers.
  ```
- [`8beea5f`](https://github.com/ghostty-org/ghostty/commit/8beea5f92dcfb229b9434eed6ea5548e32ed5df8) libghostty: expose row cell styling bit ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render row-cells data key for querying whether the current cell has
  explicit styling. This lets consumers avoid fetching a raw cell or full style
  snapshot when all they need is the cell's HasStyling bit.
  
  The new key is appended to the existing enum for ABI safety and is served by
  the existing row-cells getter path. Existing data keys and function exports are
  unchanged.
  ```
- [`54ac5fd`](https://github.com/ghostty-org/ghostty/commit/54ac5fd21e5eeef5e910f7f646934dc58fd373f8) libghostty: expose row cell styling bit ([#12837](https://github.com/ghostty-org/ghostty/issues/12837)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render row-cells data key for querying whether the current cell
  has explicit styling. This lets consumers avoid fetching a raw cell or
  full style snapshot when all they need is the cell's HasStyling bit.
  
  The new key is appended to the existing enum for ABI safety and is
  served by the existing row-cells getter path. Existing data keys and
  function exports are unchanged.
  
  This was identified as an allocation hot-spot in Go renderers.
  ```

