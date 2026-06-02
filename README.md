> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 2, 2026 at 16:31 UTC.

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

## May 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26543370661), [2](https://github.com/ghostty-org/ghostty/actions/runs/26530789804), [3](https://github.com/ghostty-org/ghostty/actions/runs/26519976482)  
Summary: 3 runs • 32 commits • 5 authors

### Changes

- [`f730ee0`](https://github.com/ghostty-org/ghostty/commit/f730ee0557917258024e18a45489918de2ce9fa7) libghostty: expose viewport active state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose whether the terminal viewport is currently pinned to the active
  area through the libghostty-vt terminal data API. Previously embedders
  could only infer this from scrollbar geometry, which was indirect and
  could require the more expensive scrollbar calculation.
  
  The new GHOSTTY_TERMINAL_DATA_VIEWPORT_ACTIVE value returns the exact
  PageList viewport state as a bool. The scroll viewport test now verifies
  the value while moving between the active area and scrollback.
  ```
- [`1526485`](https://github.com/ghostty-org/ghostty/commit/15264856f61b112c8beb14fbe3f403f6266c8bdf) libghostty: expose viewport active state ([#12836](https://github.com/ghostty-org/ghostty/issues/12836)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose whether the terminal viewport is currently pinned to the active
  area through the libghostty-vt terminal data API. Previously embedders
  could only infer this from scrollbar geometry, which was indirect and
  could require the more expensive scrollbar calculation.
  
  The new GHOSTTY_TERMINAL_DATA_VIEWPORT_ACTIVE value returns the exact
  PageList viewport state as a bool. The scroll viewport test now verifies
  the value while moving between the active area and scrollback.
  ```
- [`2f61ba0`](https://github.com/ghostty-org/ghostty/commit/2f61ba036ed4d0013f34414728938bf7825219c8) libghostty: starting the SelectionGesture API, just init/get ([@mitchellh](https://github.com/mitchellh))
- [`bbfa984`](https://github.com/ghostty-org/ghostty/commit/bbfa984aec99c8d3e2e7dde1a10c7520f4f873cb) libghostty: GhosttySelectionGestureEvent ([@mitchellh](https://github.com/mitchellh))
- [`5ac8e65`](https://github.com/ghostty-org/ghostty/commit/5ac8e6569a8d1d73f1bff9b4fc82ea703b9ca97e) libghostty: add ghostty_selection_gesture_event ([@mitchellh](https://github.com/mitchellh))
- [`3fd2c66`](https://github.com/ghostty-org/ghostty/commit/3fd2c66a048ad12901ea30ef30da1a4dfc7395a4) libghostty: selection gesture release event ([@mitchellh](https://github.com/mitchellh))
- [`90fd1ec`](https://github.com/ghostty-org/ghostty/commit/90fd1ec2e78d1c0b3f640c9eb1e73a6e7dd7232b) libghostty: selection gesture drag events ([@mitchellh](https://github.com/mitchellh))
- [`603684b`](https://github.com/ghostty-org/ghostty/commit/603684ba11092b9430c336b3378ba22ef9615cc0) libghostty: selection gesture autotick ([@mitchellh](https://github.com/mitchellh))
- [`f0fcb10`](https://github.com/ghostty-org/ghostty/commit/f0fcb104069647051b2e612c23c90e2414a0db58) libghostty: selection gesture deep press ([@mitchellh](https://github.com/mitchellh))
- [`3e0477a`](https://github.com/ghostty-org/ghostty/commit/3e0477a14a1a6a0a8f4a5256b95528aa8145351a) example/c-vt-selection-gesture ([@mitchellh](https://github.com/mitchellh))
- [`4e2d7c3`](https://github.com/ghostty-org/ghostty/commit/4e2d7c314b2e3645924c50eba309a431d28c4bb2) libghostty: optimize bits for selection gesture validation fields ([@mitchellh](https://github.com/mitchellh))
- [`6d089a5`](https://github.com/ghostty-org/ghostty/commit/6d089a544db53f3457374c2c406bccee80722cdf) libghostty: C API for SelectionGesture ([#12833](https://github.com/ghostty-org/ghostty/issues/12833)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  C API side of https://github.com/ghostty-org/ghostty/pull/12830
  ```
- [`ac69942`](https://github.com/ghostty-org/ghostty/commit/ac69942cdcc2d7c26bc5fe7ed1d5d505c3461e0c) cli: rework +ssh-cache internals and user interface ([@jparise](https://github.com/jparise))
  ```text
  This change primarily focused on a revised +ssh-cache user interface,
  but it also reworks a bunch of the internals.
  
  The primary CLI improvement is support for positional arguments and a
  consistent list output format that includes both the ISO-formatted
  timestamp and relative age.
  
      ghostty +ssh-cache                           # List all cached destinations
      ghostty +ssh-cache user@example.com          # Show that destination
      ghostty +ssh-cache example.com               # Show all users on that host
      ghostty +ssh-cache --add=user@example.com    # Manually add a destination
      ghostty +ssh-cache --remove=user@example.com # Remove a destination
      ghostty +ssh-cache --prune=30d               # Remove entries older than 30 days
      ghostty +ssh-cache --clear                   # Clear entire cache
  
  Notable, we now support a --prune operation that replaces the previous
  --expire-days flag that was never actually hooked up to anything (!!).
  --prune also supports a wider range of Duration-based values.
  
  We're also much more consistent with error codes: 0=success, 1=failure,
  2=usage.
  
  While working on those changes, I also reworked the cache internals,
  particularly the code around timestamp handling and errors. For example,
  I dropped the explicit error sets because they were growing unwieldy,
  and in practice we only matched on a subset of those errors.
  
  Lastly, overall test coverage should be much improved, especially around
  the time- and allocation-related operations.
  ```
- [`d86ff37`](https://github.com/ghostty-org/ghostty/commit/d86ff37a58f77d87f1774a433bdcfabf9f99e246) terminal: SelectionGesture, but only with mouse press ([@mitchellh](https://github.com/mitchellh))
- [`14df684`](https://github.com/ghostty-org/ghostty/commit/14df684a70fed6085ec70b711f045f0261dbe4c2) core: adapt Surface to use SelectionGesture with press only ([@mitchellh](https://github.com/mitchellh))
- [`57d2020`](https://github.com/ghostty-org/ghostty/commit/57d202066d138e9078f89c9b27302a5aee6b9422) macOS: clear stale OSC 11 background cache on config change ([@b0uks](https://github.com/b0uks))
  ```text
  SurfaceView caches the background color set by OSC 11 in
  backgroundColor. TerminalWindow.preferredBackgroundColor consults
  that cache before falling back to derivedConfig.backgroundColor,
  so once OSC 11 has fired the cached value masks any later config
  change. After a light/dark theme auto-switch this leaves the
  window chrome on the previous theme's color until the application
  next emits OSC 11.
  
  In ghosttyConfigDidChange, after updating derivedConfig, drop the
  cache when it no longer matches the new config-derived background.
  A subsequent ghosttyColorDidChange repopulates it as before, so
  within-config OSC 11 behavior is unchanged.
  ```
- [`33f1558`](https://github.com/ghostty-org/ghostty/commit/33f1558801d5282e9b2fb7b35194fed69d98f167) core: mouse left release renderer lock made more coarse ([@mitchellh](https://github.com/mitchellh))
  ```text
  This will make our selection gesture extraction a bit easier.
  ```
- [`c00cdd8`](https://github.com/ghostty-org/ghostty/commit/c00cdd886b933cd7db175ddcf031c2e703ea1409) SelectionGesture: drag events ([@mitchellh](https://github.com/mitchellh))
- [`229f4c1`](https://github.com/ghostty-org/ghostty/commit/229f4c1f4fdd2a24ff1e2634d6450de158fd987c) terminal: SelectionGesture handles word/line drag ([@mitchellh](https://github.com/mitchellh))
- [`141c7d4`](https://github.com/ghostty-org/ghostty/commit/141c7d44d2d10621d6b8f014c6a1ec3e416f14ea) SelectionGesture: release event ([@mitchellh](https://github.com/mitchellh))
- [`df98b6d`](https://github.com/ghostty-org/ghostty/commit/df98b6d9833dbc80babee58b8a02d102d14bfd83) terminal: SelectionGesture autoscrollTick ([@mitchellh](https://github.com/mitchellh))
- [`f5f9d32`](https://github.com/ghostty-org/ghostty/commit/f5f9d32d0a42b55bb80599a000e63c33a25d549e) terminal: SelectionGesture deep press ([@mitchellh](https://github.com/mitchellh))
- [`5368adc`](https://github.com/ghostty-org/ghostty/commit/5368adcd29754939e6c283198ef6b1c122293815) macos: avoid duplicate appearance sync on tab focus ([@Tunglies](https://github.com/Tunglies))
  ```text
  Close #12825
  
  Skip the initial emissions from the focused surface appearance publishers after a tab focus change. The focused surface is already synced immediately, so the initial Combine values only repeat the same titlebar and background updates. Subsequent derived config and OSC background changes still resync the window appearance.
  ```
- [`ce4128a`](https://github.com/ghostty-org/ghostty/commit/ce4128afc494d192edcc0f3a28e2d63fbb059eda) Update VOUCHED list ([#12829](https://github.com/ghostty-org/ghostty/issues/12829)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12827#discussioncomment-17075382)
  from @trag1c.
  
  Denounce: @Cznorth
  ```
- [`9b00bb4`](https://github.com/ghostty-org/ghostty/commit/9b00bb436a99ece1b78bea90b403f38636cbff15) terminal: better SelectionGesture docs ([@mitchellh](https://github.com/mitchellh))
- [`82a73f2`](https://github.com/ghostty-org/ghostty/commit/82a73f2bf185ee2836378e3aeea8fc528e757921) terminal: SelectionGesture press returns standard behaviors ([@mitchellh](https://github.com/mitchellh))
- [`7d4d1e5`](https://github.com/ghostty-org/ghostty/commit/7d4d1e5819b635004b17e28bc302a036e4461c04) terminal: add configurable behaviors based on click count ([@mitchellh](https://github.com/mitchellh))
- [`68959c5`](https://github.com/ghostty-org/ghostty/commit/68959c5c6388fad9f7c169ad8229a6bfd17d8ff0) terminal: fix selection gesture edge cases ([@mitchellh](https://github.com/mitchellh))
  ```text
  Selection gestures now treat releases with invalidated anchors as dragged,
  so a press that crosses screen boundaries cannot also activate links or
  prompt clicks on release. Cell drags that create a same-cell selection also
  mark the gesture as dragged, which keeps click-only actions from firing
  after a threshold-crossing drag.
  
  Autoscroll now resolves the drag pin after moving the viewport instead of
  reusing the pin from before the scroll. This keeps the selection aligned
  with the row currently under the pointer. The inspector also validates the
  tracked click pin before displaying it so stale pins from inactive screens
  are ignored.
  ```
- [`c343c5a`](https://github.com/ghostty-org/ghostty/commit/c343c5a67a041833eb9c716319f2df3ca8388144) Extract click/drag selection handling into SelectionGesture ([#12830](https://github.com/ghostty-org/ghostty/issues/12830)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Refactor terminal text selection into a reusable `SelectionGesture`
  state machine. Most importantly, this means our click+drag logic around
  selection is now fully unit tested! And we found bugs! And fixed them!
  
  The large line increase in this diff is mainly comments + tests.
  
  I've wanted to do this forever so we can unit test this, but I was
  kicked in the butt to do it recently because reimplementing selection
  logic in libghostty consumers turns out to be complex and error prone
  and we have a perfectly battle tested logic machine here so why not
  extract it?
  
  Behavioral changes from main surfaced via unit testing:
  
  - Dragging now drags by output across semantic output blocks when the
  initial press was an output selection. This matches the behavior of
  dragging continuing whatever the initial selection logic was.
  - Selection autoscroll now stops when the click anchor is invalidated by
  a screen change (e.g. primary to alt)
  - Deep press (macOS force touch) now selects the word at the original
  press location and consumes the active drag gesture, preventing later
  movement from dragging or autoscrolling that selection. This matches
  built-in macOS apps.
  - Mouse release records whether the gesture moved away from the pressed
  cell, so link and prompt clicks are skipped after a drag while normal
  clicks still activate them.
  
  Example usage:
  
  ```zig
  var gesture: terminal.SelectionGesture = .init;
  defer gesture.deinit(t);
  
  const press_selection = try gesture.press(t, .{
      .time = try std.time.Instant.now(),
      .pin = press_pin,
      .xpos = mouse_x,
      .ypos = mouse_y,
      .max_distance = cell_width,
      .repeat_interval = mouse_interval,
      .word_boundary_codepoints = selection_word_chars,
      .behaviors = &.{ .cell, .word, .output },
  });
  try t.screens.active.select(press_selection);
  
  if (gesture.drag(t, drag_event)) |drag_selection| {
      try t.screens.active.select(drag_selection);
  }
  
  gesture.release(t, .{ .pin = release_pin });
  ```
  ````
- [`8518986`](https://github.com/ghostty-org/ghostty/commit/8518986b1e84998e8141eacce462afd213b38073) macOS: clear stale OSC 11 background cache on config change ([#12822](https://github.com/ghostty-org/ghostty/issues/12822)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  `SurfaceView` caches the background color set by OSC 11 in
  `backgroundColor`. `TerminalWindow.preferredBackgroundColor` consults
  that cache before falling back to `derivedConfig.backgroundColor`, so
  once OSC 11 has fired the cached value masks any later config change.
  
  After a light/dark theme auto-switch (e.g. `theme =
  light:my-light,dark:my-dark`) this leaves the window chrome on the
  previous theme's color until the application next emits OSC 11.
  
  In `ghosttyConfigDidChange`, after updating `derivedConfig`, drop the
  cache when it no longer matches the new config-derived background. A
  subsequent `ghosttyColorDidChange` repopulates it as before, so
  within-config OSC 11 behavior is unchanged.
  
  ## Reproduction
  
  1. Configure `theme = light:SomeLight,dark:SomeDark` where the two
  themes have visibly different background colors.
  2. Open a terminal session where any application (e.g. a shell startup
  script) has sent OSC 11 to set a custom background color.
  3. Switch macOS appearance (System Settings → Appearance).
  4. **Before**: window chrome stays the previous theme's color until the
  terminal next emits OSC 11.
  5. **After**: window chrome immediately updates to the new theme's
  background color.
  
  ## Changes
  
  - `SurfaceView_AppKit.swift` — one guard: if the cached
  `backgroundColor` disagrees with the new
  `derivedConfig.backgroundColor`, set it to `nil`.
  ```
- [`756fda7`](https://github.com/ghostty-org/ghostty/commit/756fda776b1f8516bcf925ad9901cb0139b64271) cli: rework +ssh-cache internals and user interface ([#12814](https://github.com/ghostty-org/ghostty/issues/12814)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This change primarily focused on a revised +ssh-cache user interface,
  but it also reworks a bunch of the internals.
  
  The primary CLI improvement is support for positional arguments and a
  consistent list output format that includes both the ISO-formatted
  timestamp and relative age.
  
  ghostty +ssh-cache # List all cached destinations
      ghostty +ssh-cache user@example.com          # Show that destination
  ghostty +ssh-cache example.com # Show all users on that host
  ghostty +ssh-cache --add=user@example.com # Manually add a destination
      ghostty +ssh-cache --remove=user@example.com # Remove a destination
  ghostty +ssh-cache --prune=30d # Remove entries older than 30 days
      ghostty +ssh-cache --clear                   # Clear entire cache
  
  Notable, we now support a --prune operation that replaces the previous
  --expire-days flag that was never actually hooked up to anything (!!).
  --prune also supports a wider range of Duration-based values.
  
  We're also much more consistent with error codes: 0=success, 1=failure,
  2=usage.
  
  While working on those changes, I also reworked the cache internals,
  particularly the code around timestamp handling and errors. For example,
  I dropped the explicit error sets because they were growing unwieldy,
  and in practice we only matched on a subset of those errors.
  
  Lastly, overall test coverage should be much improved, especially around
  the time- and allocation-related operations.
  
  ---
  
  *AI Disclosure:* I made a lot of iterative, AI-assisted (Claude Opus
  4.7) correctness passes over this work. It was particularly helpful in
  tracing through the various failure modes, and it wrote those unit tests
  in the process.
  ```
- [`3103ae8`](https://github.com/ghostty-org/ghostty/commit/3103ae883880fe6cccdc17ea923e3ccd3587a83e) macos: avoid duplicate appearance sync on tab focus ([#12828](https://github.com/ghostty-org/ghostty/issues/12828)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Close #12825
  
  Skip the initial emissions from the focused surface appearance
  publishers after a tab focus change. The focused surface is already
  synced immediately, so the initial Combine values only repeat the same
  titlebar and background updates. Subsequent derived config and OSC
  background changes still resync the window appearance.
  
  
  
  https://github.com/user-attachments/assets/f229fb95-4b4c-4040-85ac-0acfcc54ca82
  
  
  
  Assigned to Codex GPT 5.5(medium)
  PS: Sry for I don't write zig and let AI write this.
  ```

