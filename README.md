> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 28, 2026 at 08:25 UTC.

## July 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30325837845)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

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

## July 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30067558033)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`4c72524`](https://github.com/ghostty-org/ghostty/commit/4c725242b7dbe8c77c6e227ef1f9540c5ef17921) Update VOUCHED list ([#13437](https://github.com/ghostty-org/ghostty/issues/13437)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13436#discussioncomment-17759608)
  from @jcollie.
  
  Vouch: @SanJJ1
  ```

## July 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30046267613), [2](https://github.com/ghostty-org/ghostty/actions/runs/30016145400), [3](https://github.com/ghostty-org/ghostty/actions/runs/30010810985)  
Summary: 3 runs • 8 commits • 4 authors

### Changes

- [`f8e13f3`](https://github.com/ghostty-org/ghostty/commit/f8e13f31e6a25f55bfb9725f9b55f74cea1af50f) Fix desktop detection tests when running from Gnome ([@jcollie](https://github.com/jcollie))
  ```text
  Environment variables from the "real" environment leaked into the test
  after the Zig 0.16 update which would cause them to fail if you ran them
  on a Gnome system.
  ```
- [`e6e26e1`](https://github.com/ghostty-org/ghostty/commit/e6e26e165ab143f087761cee9f8a479801a27ba7) Fix desktop detection tests when running from Gnome ([#13434](https://github.com/ghostty-org/ghostty/issues/13434)) ([@jcollie](https://github.com/jcollie))
  ```text
  Environment variables from the "real" environment leaked into the test
  after the Zig 0.16 update which would cause them to fail if you ran them
  on a Gnome system.
  ```
- [`d65cb51`](https://github.com/ghostty-org/ghostty/commit/d65cb5128abfbee4dcb8a4ace3bcb35c1a7f0790) build: link libghostty-vt on Apple hosts with native linker ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replaces: https://github.com/ghostty-org/ghostty/pull/13427
  
  Zig's Mach-O linker does not emit LC_ENCRYPTION_INFO_64 for physical
  iOS dylibs. This allows libghostty-vt to build successfully but causes
  frameworks containing it to fail App Store validation.
  
  I think it'd be cleaner to always just build Apple targets on Apple hosts
  with the native linker. We don't need to rely on Zig being correct and
  this helps ensure compatibility for details like this.
  ```
- [`15484b6`](https://github.com/ghostty-org/ghostty/commit/15484b607eb5a518dedf1548247c923b8abaae7c) build: link libghostty-vt on Apple hosts with native linker ([#13430](https://github.com/ghostty-org/ghostty/issues/13430)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replaces: https://github.com/ghostty-org/ghostty/pull/13427
  
  Zig's Mach-O linker does not emit LC_ENCRYPTION_INFO_64 for physical iOS
  dylibs. This allows libghostty-vt to build successfully but causes
  frameworks containing it to fail App Store validation.
  
  I think it'd be cleaner to always just build Apple targets on Apple
  hosts with the native linker. We don't need to rely on Zig being correct
  and this helps ensure compatibility for details like this.
  ```
- [`960c2cc`](https://github.com/ghostty-org/ghostty/commit/960c2cca5d57ca6e293efd2d7b7a0f590412cfa8) fix: fix kitty temp directory copy length mismatch ([@elias8](https://github.com/elias8))
- [`e663d54`](https://github.com/ghostty-org/ghostty/commit/e663d54051d3af9103d1d889d3d7eac7d7176931) os/hostname: switch to std.Io.net.HostName.validate ([@jparise](https://github.com/jparise))
  ```text
  Zig 0.16's hostname validation routine is RFC 1123-compliant, so we can
  use it directly rather than rolling our own.
  
  Ref: https://codeberg.org/ziglang/zig/commit/efe649b13e582be855376944bac1346426e238d6
  Ref: https://github.com/ziglang/zig/pull/25710
  ```
- [`4154185`](https://github.com/ghostty-org/ghostty/commit/4154185e23707870a118767afa1dc074828a3b2f) os/hostname: switch to std.Io.net.HostName.validate ([#13428](https://github.com/ghostty-org/ghostty/issues/13428)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig 0.16's hostname validation routine is RFC 1123-compliant, so we can
  use it directly rather than rolling our own.
  
  Ref:
  https://codeberg.org/ziglang/zig/commit/efe649b13e582be855376944bac1346426e238d6
  Ref: https://github.com/ziglang/zig/pull/25710
  ```
- [`30de782`](https://github.com/ghostty-org/ghostty/commit/30de782e8edb5658e6539f5ccebcdcfa6582f102) fix(terminal): fix kitty temp directory copy length mismatch ([#13424](https://github.com/ghostty-org/ghostty/issues/13424)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  EDIT:
  [exposed](https://github.com/elias8/libghostty/actions/runs/29996356691/job/89171182671?pr=113#step:12:447)
  while syncing libghostty dart bindings to latest main.
  ```

## July 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29956921809), [2](https://github.com/ghostty-org/ghostty/actions/runs/29949317476), [3](https://github.com/ghostty-org/ghostty/actions/runs/29936126378)  
Summary: 3 runs • 14 commits • 2 authors

### Changes

- [`1c861e3`](https://github.com/ghostty-org/ghostty/commit/1c861e3c476f2489008c12fc0b75af72c1b8484d) pkg/apple-sdk: support Xcode 27 SDK headers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Xcode 27's math.h uses the __need_infinity_nan protocol provided by
  matching Clang resource headers. Zig 0.16's bundled float.h predates
  that protocol, causing the bundled libc++ compilation to fail.
  
  Overlay the SDK math.h through the Apple SDK libc include path and
  provide the missing infinity and NaN definitions. The compatibility
  header can be removed once Zig's bundled Clang headers support the
  protocol.
  ```
- [`d97a574`](https://github.com/ghostty-org/ghostty/commit/d97a5742423551e8847f2c81f6c10feeb6f5a66e) ci: test with Xcode 27 ([@mitchellh](https://github.com/mitchellh))
- [`ab0b9da`](https://github.com/ghostty-org/ghostty/commit/ab0b9da9e88fcb4b0533a1854e84628f663930af) pkg/apple-sdk: support Xcode 27 SDK headers ([#13419](https://github.com/ghostty-org/ghostty/issues/13419)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Xcode 27's math.h uses the __need_infinity_nan protocol provided by
  matching Clang resource headers. Zig 0.16's bundled float.h predates
  that protocol, causing the bundled libc++ compilation to fail.
  
  Overlay the SDK math.h through the Apple SDK libc include path and
  provide the missing infinity and NaN definitions. The compatibility
  header can be removed once Zig's bundled Clang headers support the
  protocol.
  ```
- [`dac134d`](https://github.com/ghostty-org/ghostty/commit/dac134d254bab15209e494413973e4f902b654c6) pkg/apple-sdk: enable libc++ availability annotations ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13417
  
  The bundled upstream libc++ headers in Zig 0.16 skip the Apple-configured
  availability setting. This causes the headers to assume every LLVM 21
  ABI symbol is present in the target system libc++, producing binaries
  that fail at launch on macOS versions without `std::__hash_memory`.
  
  Enable the Apple vendor availability table for compile steps configured
  by the Apple SDK helper. libc++ now selects its inline compatibility
  implementation when the target system dylib does not provide the symbol.
  
  References in the mega comment
  ```
- [`49a76f2`](https://github.com/ghostty-org/ghostty/commit/49a76f244d6db48115ec48b4d9b5d40593386099) pkg/apple-sdk: enable libc++ availability annotations ([#13418](https://github.com/ghostty-org/ghostty/issues/13418)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13417
  
  The bundled upstream libc++ headers in Zig 0.16 skip the
  Apple-configured availability setting. This causes the headers to assume
  every LLVM 21 ABI symbol is present in the target system libc++,
  producing binaries that fail at launch on macOS versions without
  `std::__hash_memory`.
  
  Enable the Apple vendor availability table for compile steps configured
  by the Apple SDK helper. libc++ now selects its inline compatibility
  implementation when the target system dylib does not provide the symbol.
  
  References in the mega comment
  ```
- [`e8525c0`](https://github.com/ghostty-org/ghostty/commit/e8525c0fd907a6bfa91286984c767894b2b8fa65) Update to Zig 0.16.0 ([@vancluever](https://github.com/vancluever))
  ```text
  This commit represents the majority of the work necessary to upgrade
  Ghostty to use Zig 0.16.0.
  
  Key parts:
  
  * In addition to its previous responsibilities, the global state now
    houses state for global I/O implementations and the process
    environment. It is now also utilized in the main application along
    with the C library. Where necessary, global state is isolated from key
    parts of the implementation (e.g., in libghostty subsystems), and it's
    expected that this list will grow.
  
  * We currently manage our own C translation layer where necessary. In
    these cases, cImport has been removed in favor of the new external
    translate-c package. Due to fixes that have needed be made to properly
    translate the dependencies that were swapped out, as mentioned, we
    have had to backport fixes from the current translate-c package (and
    the upstream Arocc dependency). We will host this ourselves until Zig
    0.17.0 is released with these fixes.
  
  * Where necessary (only a small number of cases), some stdlib code from
    0.15.2 (and even from 0.17.0) has been taken, adopted, and vendored in
    lib/compat.
  ```
- [`f2a7652`](https://github.com/ghostty-org/ghostty/commit/f2a7652abab5d03f846f3150f9cc1b2dc23bb3dd) mitchell's touchups ([@mitchellh](https://github.com/mitchellh))
  ```text
  - benchmark: avoid buffers to avoid a memcpy
  - build: keep frame pointers on macOS. There was some debug changes from
    Zig 0.15 and this helps. Also, Apple actually requires/expects x29 to
    always be a frame pointer.
  - build/macos: force libSystem symbols instead of compiler-rt
  - global: add InitOpts.tool so that ghostty-gen/bench can parse their
    own actions in `+action`
  - quirks: provide our own vectorized memset. see the comment for more
    details why.
  - synthetic: fix UB by accessing global.io before it was initialized
  - terminal/hash_map: force inline for unique repr types. Zig 0.15
    inlined and 0.16 doesn't, measured a huge slowdown in hyperlink
    benchmarks.
  - terminal: add explicit `@Vector` usage for storing a run of identical cells
    as well as for scanning printable cells. This auto-vectorized in Zig
    0.15 but not in Zig 0.16. This produces the same assembly.
  - unicode: properties and LUT need power-of-two backing integer to avoid
    bad LLVM codegen
  ```
- [`da04b65`](https://github.com/ghostty-org/ghostty/commit/da04b65d4c3e590aa37a431ec6e25efc6900224d) terminal: init_single_threaded for C API ([@vancluever](https://github.com/vancluever))
  ```text
  The C API is assumed to be single-threaded per VT instance.
  Additionally, using fully-threaded I/O instances registers signal
  handlers, and would do a pair of registrations once per instance, which
  could easily get out of hand (and is not really what we intend anyway).
  
  init_single_threaded does not register signal handlers, so it does not
  have this issue, and matches the execution model of the C VT API
  (single-threaded/not thread-safe within a single VT instance).
  
  This also fixes an initialization issue with the threaded I/O instance
  in general (needs allocation as the memory location would have gone out
  of scope before).
  ```
- [`048619a`](https://github.com/ghostty-org/ghostty/commit/048619a6bf548684ec6af3a3b0d3cc45dd9f189e) global: take minimal instead of juicy main ([@vancluever](https://github.com/vancluever))
  ```text
  The early-stage main Zig wrapper recognizes if main only needs the
  minimal state (args and lower-level environment) and skips a bunch of
  unneeded initialization (allocator, arena, threaded I/O, and the
  higher-level environment map). Particularly, the fact that it does not
  set up an I/O instance means that we won't have any unneeded signal
  handlers set up for the unused threaded I/O implementation, which is
  similar in spirit to the fixes we applied for the C VT implementation,
  with the notable difference that we do actually set a threaded I/O up in
  global state - hence, again, we don't want the duplicate unused one.
  ```
- [`4956668`](https://github.com/ghostty-org/ghostty/commit/4956668702f3e029b615a5600531eadc40170f9b) vt: get rid of log spam on tests ([@vancluever](https://github.com/vancluever))
  ```text
  Zig 0.16.0 made the criteria for reporting "failed command" stricter (or
  looser, depending on your perspective I guess...) - now, tests that
  print anything to stderr cause the message to appear.
  
  Note that in this instance tests still pass and you get a return code of
  0, but nonetheless, it can be confusing.
  
  Additionally, having spammy passing tests in general is not necessarily
  a great experience, so this should help with that.
  
  Note that this change was already done to the main tests. We can add a
  build argument to control this if need be.
  ```
- [`7121ab6`](https://github.com/ghostty-org/ghostty/commit/7121ab6c3f0e868d3383c59a2e4d5a564f96aa9f) global: state should default to null ([@vancluever](https://github.com/vancluever))
- [`a77c706`](https://github.com/ghostty-org/ghostty/commit/a77c706a180528f8197771abd51436d98ccd854a) fix process and global error handling ([@mitchellh](https://github.com/mitchellh))
  ```text
  Restore the error handling that the removed std.posix fork and waitpid
  wrappers previously provided. Raw fork failures now propagate, waitpid
  retries interruptions before reading status, and edit-config constructs the
  sentinel-terminated argv required by execve.
  
  Let global initialization own cleanup through its existing errdefer so
  temporary paths are freed once. Report initialization failures with the
  static synchronous I/O provider because global I/O has already been torn
  down by that point.
  ```
- [`b988efc`](https://github.com/ghostty-org/ghostty/commit/b988efcfe584e88a3d0330e2c17c386ffa419d72) fix some 0.16 translation regressions ([@mitchellh](https://github.com/mitchellh))
- [`7aa9591`](https://github.com/ghostty-org/ghostty/commit/7aa9591746ffa4d2eee458960c76554352832595) Update to Zig 0.16.0 ([#12726](https://github.com/ghostty-org/ghostty/issues/12726)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #12228
  Supersedes #12388
  
  **UPDATED** - Also check comments for additional details!
  
  This commit represents the majority of the work necessary to upgrade
  Ghostty to use Zig 0.16.0.
  
  At this point, all tests pass under Linux, but more work may be
  necessary to get them to build and function on other platforms.
  
  There are some parts of this update that deserve commentary, so that
  follows below:
  
  ## Expanded use of global state (IO/environment related)
  
  Global state, once generally only used by the C library, has now been
  expanded to be used across the project at large. The static local
  variable that holds the state has been moved private in its source
  container with all attributes that need to be accessed globally gated
  behind accessors, most of which guard on testing and send test copies
  instead. Use of the global state in non-testing scenarios asserts that
  the state has been initialized through `init` naturally through the
  optional assertion process.
  
  The rationale for this change is to have a location to store a
  general-purpose I/O implementation and environment variables, both of
  which are now provided through [Juicy
  Main](https://ziglang.org/download/0.16.0/release-notes.html#Juicy-Main)
  and hence can no longer be accessed or mutated through stdlib without
  use of lower-level system calls and hacks (some of which are employed,
  but sparingly).
  
  As the code matures, dependence on global state should naturally slim
  down.
  
  We do not allow global state to be used in libghostty-vt. There are
  comptime guards that prevent this should compilation of libghostty-vt
  end up pulling `global.zig`. This means that as per the last paragraph,
  work has already begun to de-couple the codebase from global state where
  necessary. Additionally, in some places where environment needs to be
  updated and where it can be done in an isolated fashion, environment
  maps are used - system-level injection of environment through the use of
  `setenv` or `unsetenv` now only happens during early initialization (and
  hopefully we can remove these in the future too, especially since they
  require re-synchronization of the higher-level environment primitives
  after this is done).
  
  ## The `lib/compat` Tree
  
  Some stdlib features that have been removed but still either seem they
  would be valuable to us or outright complex to move away from
  (particularly `SegmentedList`) have been extracted from 0.15.2, updated
  as needed, and placed in `src/lib/compat`. The intention again is to
  allow for piecemeal migration to more modern implementations or possibly
  straight local versions.
  
  This paradigm has also allowed us to add `std.Io.Condition.waitTimeout`,
  which incidentally was missed in the 0.16.0 shuffle and has been
  re-added for 0.17.0. We can remove this in favor of the upstream when we
  eventually migrate to that, obviously.
  
  Note that there was a lot more of this extracted code when this work was
  started, but a lot of said code has been removed (namely environment or
  process/fd-related functionality).
  
  ## translate-c Issues (functional on Linux, Darwin WIP)
  
  There have been a number of C translation issues that we have been
  working through through submitted patches and the great help from folks
  on the Arocc and Zig side. This is ongoing, with the remaining work to
  getting things fixed mainly focused on the MacOS side. Stay tuned for
  further developments.
  
  As mentioned at the top, follow comments for more details!
  ```

