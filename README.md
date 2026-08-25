> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 25, 2026 at 12:37 UTC.

## August 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32811372816)  
Summary: 1 runs • 4 commits • 1 authors

### Changes

- [`70f0065`](https://github.com/ghostty-org/ghostty/commit/70f0065759428c0594c7c5befcb20104ff7ab615) terminal: reject oversized Kitty clipboard writes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update OSC 5522 writes to reject every transaction that exceeds the
  configured decoded-data limit. The previous behavior truncated text
  while rejecting only non-text data.
  
  Programs now receive EFBIG as soon as a write crosses the limit. The
  clipboard remains untouched, and remaining write packets are ignored
  until a new transaction begins. Raise the default to the protocol
  minimum of 64 MiB.
  
  This applies the latest spec change:
  https://github.com/kovidgoyal/kitty/commit/32ea1041921607836e37815e0ab3692264a6cc81
  ```
- [`e8d8945`](https://github.com/ghostty-org/ghostty/commit/e8d8945b536189366e227b157aa0b8202b94890a) terminal: update Kitty clipboard text input validation to spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate decoded OSC 5522 metadata, read MIME lists, and alias
  lists as UTF-8. Treat an alias without a target MIME type as an
  invalid write packet.
  
  Malformed write packets now return EINVAL and terminate the in-flight
  transaction instead of leaving it active. Malformed reads are dropped
  without disturbing an active write.
  
  Latest changes upstream to spec:
  https://github.com/kovidgoyal/kitty/commit/458421af4656a8f90beca7d95e4c1ff7093cf269
  ```
- [`4888c0a`](https://github.com/ghostty-org/ghostty/commit/4888c0a02c2e36b5146900195e344a8ac307660f) terminal: reject oversized Kitty clipboard writes ([#14004](https://github.com/ghostty-org/ghostty/issues/14004)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update OSC 5522 writes to reject every transaction that exceeds the
  configured decoded-data limit. The previous behavior truncated text
  while rejecting only non-text data.
  
  Programs now receive EFBIG as soon as a write crosses the limit. The
  clipboard remains untouched, and remaining write packets are ignored
  until a new transaction begins. Raise the default to the protocol
  minimum of 64 MiB.
  
  This applies the latest spec change:
  
  https://github.com/kovidgoyal/kitty/commit/32ea1041921607836e37815e0ab3692264a6cc81
  ```
- [`8867c37`](https://github.com/ghostty-org/ghostty/commit/8867c37c55b578b9eb4cfaba41cb9023e557176d) terminal: update Kitty clipboard text input validation to spec ([#14005](https://github.com/ghostty-org/ghostty/issues/14005)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate decoded OSC 5522 metadata, read MIME lists, and alias lists as
  UTF-8. Treat an alias without a target MIME type as an invalid write
  packet.
  
  Malformed write packets now return EINVAL and terminate the in-flight
  transaction instead of leaving it active. Malformed reads are dropped
  without disturbing an active write.
  
  Latest changes upstream to spec:
  
  https://github.com/kovidgoyal/kitty/commit/458421af4656a8f90beca7d95e4c1ff7093cf269
  ```

## August 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32777108950), [2](https://github.com/ghostty-org/ghostty/actions/runs/32770438411), [3](https://github.com/ghostty-org/ghostty/actions/runs/32756605657), [4](https://github.com/ghostty-org/ghostty/actions/runs/32750192789), [5](https://github.com/ghostty-org/ghostty/actions/runs/32747596501), [6](https://github.com/ghostty-org/ghostty/actions/runs/32739314488), [7](https://github.com/ghostty-org/ghostty/actions/runs/32707654358), [8](https://github.com/ghostty-org/ghostty/actions/runs/32690367805), [9](https://github.com/ghostty-org/ghostty/actions/runs/32676729390)  
Summary: 9 runs • 44 commits • 5 authors

### Changes

- [`5501518`](https://github.com/ghostty-org/ghostty/commit/550151882a93b9272d381df29ab10b2041981359) macos: restore paste semantics for dropped text ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #13979
  
  Dropped paths and text once again honor bracketed paste mode.
  IME, dictation, emoji picker, and character viewer commits remain typed input.
  
  sendText calls ghostty_surface_text, which applies the clipboard paste
  pipeline and bracketed paste framing when enabled. Separating the
  paths at the drag-and-drop caller preserves the input-method behavior
  introduced by #13817.
  ```
- [`1334cc2`](https://github.com/ghostty-org/ghostty/commit/1334cc213e6db4be3f2fc695a06c13d49362a570) macos: answer ENOSYS for Kitty clipboard writes to primary ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) write transaction targeting
  `loc=primary` replied `type=write:status=DONE` in the macOS app even
  though macOS has no primary selection and the data was silently
  discarded.
  
  The spec requires ENOSYS when the requested location is not
  available on the system, which the read path already answers correctly:
  https://sw.kovidgoyal.net/kitty/clipboard/
  ```
- [`928c7f0`](https://github.com/ghostty-org/ghostty/commit/928c7f0e796a96bdee53de0ba4e3469c3e7d84a9) terminal: exempt Kitty clipboard listing reads from permission prompts ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) read that only requests the
  targets type ('.') is now served without a permission prompt and never
  consults (or consumes) session password grants.
  
  The spec requires this so that a client listing the available data types
  before reading one doesn't present the user with a double permission prompt.
  ```
- [`4f4da76`](https://github.com/ghostty-org/ghostty/commit/4f4da7657ba9c551f6110d38b73e72d3c504fd54) macos: answer ENOSYS for Kitty clipboard writes to primary ([#14000](https://github.com/ghostty-org/ghostty/issues/14000)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) write transaction targeting
  `loc=primary` replied `type=write:status=DONE` in the macOS app even
  though macOS has no primary selection and the data was silently
  discarded.
  
  The spec requires ENOSYS when the requested location is not available on
  the system, which the read path already answers correctly:
  https://sw.kovidgoyal.net/kitty/clipboard/
  ```
- [`13b9857`](https://github.com/ghostty-org/ghostty/commit/13b9857a25e7befc9ae95ecaf8f3563a13757350) macos: restore paste semantics for dropped text ([#13999](https://github.com/ghostty-org/ghostty/issues/13999)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #13979
  
  Dropped paths and text once again honor bracketed paste mode. IME,
  dictation, emoji picker, and character viewer commits remain typed
  input.
  
  sendText calls ghostty_surface_text, which applies the clipboard paste
  pipeline and bracketed paste framing when enabled. Separating the paths
  at the drag-and-drop caller preserves the input-method behavior
  introduced by #13817.
  ```
- [`5350d4a`](https://github.com/ghostty-org/ghostty/commit/5350d4a5f5971da9ef4ea32566bd5d7b011dc29c) terminal: make Kitty clipboard write limit configurable ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new `clipboard-write-limit-bytes` option (similar to
  `scrollback-limit-bytes`) to limit the maximum OSC 5522 write size.
  Defaults to 32 MB.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_CLIPBOARD_WRITE_MAX_BYTES`
  option for libghostty-vt embedders to control the same.
  
  Kitty has a limit too and it works by truncating all data. I decided on
  purpose to diverge from this because I don't think truncated binary data
  is useful. Instead, we reject it so the application knows the write
  didn't work.
  
  We truncate text data, and we try to do it at the nearest complete UTF-8
  sequence (if possible).
  ```
- [`75606a6`](https://github.com/ghostty-org/ghostty/commit/75606a6900124a1c9774d97968f69a5f7bb9c080) terminal: exempt Kitty clipboard listing reads from permission prompts ([#14001](https://github.com/ghostty-org/ghostty/issues/14001)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) read that only requests the
  targets type ('.') is now served without a permission prompt and never
  consults (or consumes) session password grants.
  
  The spec requires this so that a client listing the available data types
  before reading one doesn't present the user with a double permission
  prompt.
  ```
- [`600a86d`](https://github.com/ghostty-org/ghostty/commit/600a86dcfd70ac6a16db199367ee6aad337b99cc) terminal: make Kitty clipboard write limit configurable ([#14002](https://github.com/ghostty-org/ghostty/issues/14002)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new `clipboard-write-limit-bytes` option (similar to
  `scrollback-limit-bytes`) to limit the maximum OSC 5522 write size.
  Defaults to 32 MB.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_CLIPBOARD_WRITE_MAX_BYTES`
  option for libghostty-vt embedders to control the same.
  
  Kitty has a limit too and it works by truncating all data. I decided on
  purpose to diverge from this because I don't think truncated binary data
  is useful. Instead, we reject it so the application knows the write
  didn't work.
  
  We truncate text data, and we try to do it at the nearest complete UTF-8
  sequence (if possible).
  
  For the future: Kitty spools any write data more than some size (can't
  remember) to a temp file on disk. We might want to consider doing
  something similar since we're all in-memory at the moment. This PR
  doesn't change that.
  ```
- [`9313d58`](https://github.com/ghostty-org/ghostty/commit/9313d580c6b0aff578160c79fc99fff341cf4aa3) terminal: fix stale cursor style/hyperlink state after scroll clear ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clearing the screen into scrollback and then printing could crash debug
  builds with a page integrity violation, or silently corrupt style/hyperlink
  reference counts in release builds. Found in #13991 via fuzzing.
  
  The cursor's style and hyperlink IDs are only valid on the page the
  cursor is on. When the scroll clear moved the start of the fresh
  screen onto a new page, the reset path in cursorReload updated the
  cursor's position directly instead of going through cursorChangePin,
  so the cursor kept IDs from its old page. On the new page those IDs
  pointed at entries that were dead or belonged to something else, and
  the next print used them.
  
  Fix this by making the reset path go through `cursorChangePin` like
  every other cross-page cursor move, which releases the style and
  hyperlink from the old page and recreates them on the new one.
  ```
- [`7c49e72`](https://github.com/ghostty-org/ghostty/commit/7c49e723a3f2448d3224624b054d74983c4143ca) terminal: fix stale cursor style/hyperlink state after scroll clear ([#13997](https://github.com/ghostty-org/ghostty/issues/13997)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clearing the screen into scrollback and then printing could crash debug
  builds with a page integrity violation, or silently corrupt
  style/hyperlink reference counts in release builds. Found in #13991 via
  fuzzing.
  
  The cursor's style and hyperlink IDs are only valid on the page the
  cursor is on. When the scroll clear moved the start of the fresh screen
  onto a new page, the reset path in cursorReload updated the cursor's
  position directly instead of going through cursorChangePin, so the
  cursor kept IDs from its old page. On the new page those IDs pointed at
  entries that were dead or belonged to something else, and the next print
  used them.
  
  Fix this by making the reset path go through `cursorChangePin` like
  every other cross-page cursor move, which releases the style and
  hyperlink from the old page and recreates them on the new one.
  ```
- [`25c61e8`](https://github.com/ghostty-org/ghostty/commit/25c61e852ff8de428a207a89a824bbba94a27da4) macos: implement Kitty clipboard protocol writes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Programs can now write the system clipboard through the Kitty
  clipboard protocol in the macOS app. This also does all the hard work
  plumbing through core termio/apprt so GTK should be an easy follow.
  
  This functionality lets clients copy arbitrary representations (images,
  HTML, etc.) into the clipboard. Writes honor `clipboard-write`: allow
  applies silently, deny answers EPERM up front before any data is used,
  and ask shows the standard confirmation prompt.
  ```
- [`89d17b3`](https://github.com/ghostty-org/ghostty/commit/89d17b378ed9c9d68a82ab2359cfa8030f8ff4f9) macos: implement Kitty clipboard protocol writes ([#13998](https://github.com/ghostty-org/ghostty/issues/13998)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Programs can now write the system clipboard through the Kitty clipboard
  protocol in the macOS app. This also does all the hard work plumbing
  through core termio/apprt so GTK should be an easy follow.
  
  This functionality lets clients copy arbitrary representations (images,
  HTML, etc.) into the clipboard. Writes honor `clipboard-write`: allow
  applies silently, deny answers EPERM up front before any data is used,
  and ask shows the standard confirmation prompt.
  
  After this, I believe the core and macOS have 100% Kitty clipboard
  implementation but I'll double check after this.
  
  ## Demo
  
  
  
  https://github.com/user-attachments/assets/71234fa0-f539-48eb-a633-8dea3addddd5
  ```
- [`169213c`](https://github.com/ghostty-org/ghostty/commit/169213cd292417ae25cb8df78d0a77243c134c81) renderer/image: Fuse copy to owned data and pixel format conversion in prepImage ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
- [`b17abd9`](https://github.com/ghostty-org/ghostty/commit/b17abd96df2ef19a9df8e346d54a56db56f76221) refactor(image): Restrict prepForUpload to Image.Pending ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
- [`c2c0db6`](https://github.com/ghostty-org/ghostty/commit/c2c0db68aa3b33f996a0426f00cd5972dc691ef3) macOS: enable mode 5522 paste events ([@mitchellh](https://github.com/mitchellh))
  ```text
  Advertise Kitty clipboard protocol mode 5522 on macOS and route
  clipboard paste requests through the protocol when it is enabled.
  ```
- [`1dcf4eb`](https://github.com/ghostty-org/ghostty/commit/1dcf4eb2dff0e61cac22d2a6c0700fe2dade9011) renderer/image: Fuse copying data and converting pixel format ([#13987](https://github.com/ghostty-org/ghostty/issues/13987)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Profiling `mpv --vo=kitty --vo-kitty-use-shm <video>` shows up a copy
  and then swizzle in `prepImage`
  This comes from the renderer copying the raw image data for ownership,
  then doing an rgb to rgba conversion to replace the copied data.
  This change optimize this case by letting the format conversion read
  from the data source instead of a copy of it.
  
  <img width="3825" height="1579" alt="image"
  src="https://github.com/user-attachments/assets/25851c04-b582-4bad-8f8d-930448d89fa2"
  />
  <img width="3825" height="1579" alt="image"
  src="https://github.com/user-attachments/assets/fbb1ca73-a86f-421b-992d-a764ce08c83e"
  />
  > Above-Before: prepImage profiles a memcpy + swizzle
  > Below-After: prepImage profiles just a swizzle
  
  
  The existing data path for kitty images is:
  ```
  
  Read tty for Kitty image transmission (srgb, srgba, or PNG bytes)
  -> copy into Kitty graphics ImageStorage (cpu-owned)
  
  Renderer updateFrame creates Image.Pending in renderer-owned CPU storage
  -> sync Kitty ImageStorage with renderer-owned ImageMap
  -> copy bytes into renderer.ImageMap (renderer-owned)
  -> convert ImageMap bytes to preferred GPU upload format
  
  Renderer drawFrame uploads image data to the GPU
  -> iterate through renderer.ImageMap
    -> for Pending image uploads
      -> convert the pixel format (no-op if already done), create the GPU-side texture and upload the data
  ```
  
  # Note
  Kitty graphics only supports RGB and RGBA data
  The image file decode path uses a wuffs png and jpeg decode function
  configured to return RGBA 8-bit, so I think in practice we only ever
  upload RGB8 or RGBA8. And the gray-alpha and gray pixel formats aren't
  ever used.
  
  
  # AI Disclosure
  I didn't use any LLM assistance for this.
  ````
- [`c8554f2`](https://github.com/ghostty-org/ghostty/commit/c8554f28e0efe2f5595f32020371c34b25ec628f) macOS: enable mode 5522 paste events ([#13995](https://github.com/ghostty-org/ghostty/issues/13995)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Advertise Kitty clipboard protocol mode 5522 on macOS and route
  clipboard paste requests through the protocol when it is enabled.
  ```
- [`0ce9054`](https://github.com/ghostty-org/ghostty/commit/0ce9054bf9ff5c4107bbe8a460076012861f9a3a) macos: implement Kitty clipboard protocol reads (OSC 5522) ([@mitchellh](https://github.com/mitchellh))
- [`8c7a34d`](https://github.com/ghostty-org/ghostty/commit/8c7a34d4c9c6a1afcb7a96dcc9aa4665e05d883e) macos: Kitty clipboard reads serve all clipboard content types ([@mitchellh](https://github.com/mitchellh))
- [`af9470b`](https://github.com/ghostty-org/ghostty/commit/af9470b19b40b2829653130b6b491c9ecbe6bbee) macos: Kitty clipboard reads support pw/name session grants ([@mitchellh](https://github.com/mitchellh))
- [`c1f0ef7`](https://github.com/ghostty-org/ghostty/commit/c1f0ef73a9f3a80673d8be3e9ced5e50afaf65ac) macos: serve copied files as text/uri-list in Kitty clipboard reads ([@mitchellh](https://github.com/mitchellh))
- [`df14efa`](https://github.com/ghostty-org/ghostty/commit/df14efaf332ab66c2838bed6c3d15ff41f2fd31e) macos: preview images in the clipboard read confirmation dialog ([@mitchellh](https://github.com/mitchellh))
- [`1bc1887`](https://github.com/ghostty-org/ghostty/commit/1bc188739d62f05df33a7bbc9c8db93a1b9f5a13) typos ([@mitchellh](https://github.com/mitchellh))
- [`75d6577`](https://github.com/ghostty-org/ghostty/commit/75d657788a63d1593e5fff22c766bd7e162f255c) macOS: Kitty clipboard read support ([#13993](https://github.com/ghostty-org/ghostty/issues/13993)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds Kitty clipboard protocol _read_ support to macOS. In the
  process, this also does most of the core termio, apprt, and Surface work
  so GTK is likely very easy to do, I just didn't have the machine on hand
  to test at the given moment. I will create an issue to follow up with
  that.
  
  This fully supports:
  
  - Non-text data, like images! For this, we show an image preview.
  - Per-program "remember"
  - Showing the program name if given instead of generic "An application"
  
  <img width="1848" height="996" alt="CleanShot 2026-08-24 at 08 37 45@2x"
  src="https://github.com/user-attachments/assets/549d9031-2e98-46bf-90d4-94171b255c42"
  />
  ```
- [`88dc6f9`](https://github.com/ghostty-org/ghostty/commit/88dc6f9723e7a0371cffba0b32ecb945ad126770) docs: reformatting for help book support ([@bo2themax](https://github.com/bo2themax))
- [`53d1b28`](https://github.com/ghostty-org/ghostty/commit/53d1b28ad32dcf2e10e01177ef97863c1ba69f0d) docs: reformatting for help book support ([#13994](https://github.com/ghostty-org/ghostty/issues/13994)) ([@mitchellh](https://github.com/mitchellh))
- [`94b6dae`](https://github.com/ghostty-org/ghostty/commit/94b6dae423a29d965dbf613307634fcb2ec6b112) libghostty: gate mode 5522 reports on clipboard read callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  Report Kitty paste event mode 5522 as unrecognized when the stream
  handler has no clipboard_read effect.
  
  Previously libghostty-vt advertised Kitty paste events
  unconditionally but Kitty clipboard reads can't work without a clipboard
  read effect set.
  ```
- [`a53771a`](https://github.com/ghostty-org/ghostty/commit/a53771af0165c34a7bd753ddbcbc5dd7126ee87f) libghostty: gate mode 5522 reports on clipboard read callback ([#13990](https://github.com/ghostty-org/ghostty/issues/13990)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Report Kitty paste event mode 5522 as unrecognized when the stream
  handler has no clipboard_read effect.
  
  Previously libghostty-vt advertised Kitty paste events unconditionally
  but Kitty clipboard reads can't work without a clipboard read effect
  set.
  ```
- [`7ae9b11`](https://github.com/ghostty-org/ghostty/commit/7ae9b11138e6c63888cc02ceefb92c6c1b3d4e9e) libghostty: Kitty clipboard write permission prompts and grants ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `clipboard_write` effect now is similar to read: it must response
  to a "reply" callback synchronously. This lets the embedder ask for write
  permission, too.
  
  We also now pass through program name and grant information from Kitty
  clipboard protocol so that embedders can use that if they want.
  
  This is a breaking ABI change.
  ```
- [`9f2aa93`](https://github.com/ghostty-org/ghostty/commit/9f2aa93e825735220c44159a2f4856af3ea6e79c) libghostty: Kitty clipboard write permission prompts and grants ([#13992](https://github.com/ghostty-org/ghostty/issues/13992)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `clipboard_write` effect now is similar to read: it must response to
  a "reply" callback synchronously. This lets the embedder ask for write
  permission, too.
  
  We also now pass through program name and grant information from Kitty
  clipboard protocol so that embedders can use that if they want.
  
  This is a breaking ABI change.
  ```
- [`6cf7e0c`](https://github.com/ghostty-org/ghostty/commit/6cf7e0cc544e7aa505713f40b58502bfc0ee8beb) macOS: fix swiftlint warnings ([@bo2themax](https://github.com/bo2themax))
  ```text
  swiftlint 0.63.3 introduced a new rule called [`legacy_swiftui_aspect_ratio`](https://github.com/realm/SwiftLint/blob/76363aa4d733934ece226f5bce8e27c43b986a63/CHANGELOG.md?plain=1#L314)
  ```
- [`1d24eec`](https://github.com/ghostty-org/ghostty/commit/1d24eecb207e8d9188d84b607b1de0e38eb999f6) macOS: fix responsiveness for repeated new tab action ([@bo2themax](https://github.com/bo2themax))
- [`2303bcf`](https://github.com/ghostty-org/ghostty/commit/2303bcf08df639a27ff949fb172a2b1e3feea0cd) ci: update actions/upload-artifact pinned tag comment ([@jparise](https://github.com/jparise))
- [`874735a`](https://github.com/ghostty-org/ghostty/commit/874735a9af41ec6aea0017b56836a3d3746f44b7) ci: update actions/upload-artifact pinned tag comment ([#13989](https://github.com/ghostty-org/ghostty/issues/13989)) ([@mitchellh](https://github.com/mitchellh))
- [`f9206be`](https://github.com/ghostty-org/ghostty/commit/f9206be827271b6765c966f85f6a68a1e44176b6) macOS: fix swiftlint warnings ([#13986](https://github.com/ghostty-org/ghostty/issues/13986)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  swiftlint 0.63.3 introduced a new rule called
  [`legacy_swiftui_aspect_ratio`](https://github.com/realm/SwiftLint/blob/76363aa4d733934ece226f5bce8e27c43b986a63/CHANGELOG.md?plain=1#L314)
  
  <img width="509" height="451" alt="image"
  src="https://github.com/user-attachments/assets/1ff6f593-ce8a-493e-a241-e9ae418746ee"
  />
  ```
- [`7a9bca6`](https://github.com/ghostty-org/ghostty/commit/7a9bca6a6e675ab71d6a2228237fd27b8f9f6345) macOS: fix responsiveness for repeated new tab action ([#13985](https://github.com/ghostty-org/ghostty/issues/13985)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13725
  ```
- [`569ff33`](https://github.com/ghostty-org/ghostty/commit/569ff3307c793a10380e1de4770ba21bc4ff58c5) macos: translate physical menu shortcuts ([@jparise](https://github.com/jparise))
  ```text
  Translate printable physical keybindings through the current macOS
  keyboard layout before assigning menu key equivalents. Previously these
  bindings could not be represented because SwiftUI shortcuts are
  character-based, so actions such as super+backquote had no native menu
  shortcut.
  
  Keep native keycodes as dispatch identity so translated display characters
  do not change physical semantics or precedence over Unicode bindings.
  Refresh shortcuts when the input source changes, and prevent AppKit from
  transforming equivalents that are already localized.
  ```
- [`761696c`](https://github.com/ghostty-org/ghostty/commit/761696c349c61b38e3b474a48a76f2dfc6f1af28) macos: simplify menu shortcut identity ([@jparise](https://github.com/jparise))
  ```text
  Separate menu shortcut presentation from lookup identity. Store either a
  normalized key equivalent or a physical keycode in a private hashable enum,
  allowing Swift to synthesize equality and hashing instead of maintaining
  parallel optional-key logic.
  
  Assign display characters directly from KeyboardShortcut and remove unused
  NSMenuItem and SwiftUI conversion helpers.
  ```
- [`9886f48`](https://github.com/ghostty-org/ghostty/commit/9886f4817cbc83319d69391f505fd6b611d0a621) macos: enforce keyboard layout actor isolation ([@jparise](https://github.com/jparise))
  ```text
  Text Input Sources APIs are not thread-safe, but shortcut translation could
  be called outside a declared main-actor context.
  
  Mark keyboard layout and shortcut conversion as main-actor isolated, update
  their tests, and dispatch key-sequence UI notifications to the main queue
  before translating their shortcuts.
  ```
- [`f5ad3a0`](https://github.com/ghostty-org/ghostty/commit/f5ad3a0a4a1e56b71e7710660f247899a6f19c5d) macos: use AppKit for shortcut translation ([@jparise](https://github.com/jparise))
  ```text
  Translate synthetic physical-key events with characters(byApplyingModifiers:).
  This preserves current-layout and Command-table behavior while avoiding a
  duplicate direct UCKeyTranslate implementation in Swift.
  ```
- [`6a508fd`](https://github.com/ghostty-org/ghostty/commit/6a508fd5e34c7e222c052a6d00bb3891ff3feace) macos: translate physical menu shortcuts ([#13888](https://github.com/ghostty-org/ghostty/issues/13888)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Translate printable physical keybindings through the current macOS
  keyboard layout before assigning menu key equivalents. Previously these
  bindings could not be represented because SwiftUI shortcuts are
  character-based, so actions such as `super+backquote` had no native menu
  shortcut.
  
  Keep native keycodes as dispatch identity so translated display
  characters do not change physical semantics or precedence over Unicode
  bindings. Refresh shortcuts when the input source changes, and prevent
  AppKit from transforming equivalents that are already localized.
  
  **AI Usage:** The approach was suggested by GPT 5.6 Sol, but I wrote
  most of the code and understand it all.
  ```
- [`da27e6c`](https://github.com/ghostty-org/ghostty/commit/da27e6c9082705f62a9ebbeae1753e17d2a88088) libghostty: paste reads clipboard contents on demand, streams to pty ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up to #13978
  
  `ghostty_terminal_paste` no longer takes the clipboard's data up front.
  The request now carries only the list of available MIME types plus a
  a callback that writes one representation's bytes into a `GhosttyWriter`.
  
  Previously an embedder had to load every representation for every MIME
  type into memory before pasting. For a clipboard holding a large image
  or video next to some text that could be hundreds of megabytes that
  were never used.
  
  I also took care to make sure that the data is only read once, to avoid
  any time-of-check/time-of-use (TOCTOU) issues.
  
  There is only one case where data might be fully buffered in memory now:
  unsafe text data that needs to be checked. This is true for how Ghostty
  GUI works today too.
  ```
- [`e77b230`](https://github.com/ghostty-org/ghostty/commit/e77b2309fca3a27db1123a4f904b7fb432ee7162) libghostty: paste reads clipboard contents on demand, streams to pty ([#13983](https://github.com/ghostty-org/ghostty/issues/13983)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up to #13978
  
  `ghostty_terminal_paste` no longer takes the clipboard's data up front.
  The request now carries only the list of available MIME types plus a a
  callback that writes one representation's bytes into a `GhosttyWriter`.
  
  Previously an embedder had to load every representation for every MIME
  type into memory before pasting. For a clipboard holding a large image
  or video next to some text that could be hundreds of megabytes that were
  never used.
  
  I also took care to make sure that the data is only read once, to avoid
  any time-of-check/time-of-use (TOCTOU) issues.
  
  There is only one case where data might be fully buffered in memory now:
  unsafe text data that needs to be checked. This is true for how Ghostty
  GUI works today too.
  ```
- [`a36dc24`](https://github.com/ghostty-org/ghostty/commit/a36dc245b0a8111b86b8cecdd0abf1c8d8c4dff9) Sync CODEOWNERS vouch list ([#13981](https://github.com/ghostty-org/ghostty/issues/13981)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @ollioddi
  - @rkoten
  - @tuananh
  - @vasilmytsyk
  ```

## August 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32652255901), [2](https://github.com/ghostty-org/ghostty/actions/runs/32646964497), [3](https://github.com/ghostty-org/ghostty/actions/runs/32619936178), [4](https://github.com/ghostty-org/ghostty/actions/runs/32614384859)  
Summary: 4 runs • 9 commits • 4 authors

### Changes

- [`bfc200c`](https://github.com/ghostty-org/ghostty/commit/bfc200c854d33954caf307ae459b659dd38f77c1) i18n: update bg_BG translations ([@reo101](https://github.com/reo101))
- [`9f0e171`](https://github.com/ghostty-org/ghostty/commit/9f0e1719dc918368367d368bfe300f59bb68b5a4) i18n: update bg_BG translations ([#13802](https://github.com/ghostty-org/ghostty/issues/13802)) ([@trag1c](https://github.com/trag1c))
- [`a5bb22e`](https://github.com/ghostty-org/ghostty/commit/a5bb22e235e6297b05f07b08ef1fecff7f2a8c5d) terminal: add shared paste core with Kitty clipboard paste events ([@mitchellh](https://github.com/mitchellh))
- [`8760323`](https://github.com/ghostty-org/ghostty/commit/87603231658a0e0c6a8b4be0be684b7f08778255) terminal: add stream handler paste operation and enable mode 5522 in libghostty ([@mitchellh](https://github.com/mitchellh))
- [`dda8e6f`](https://github.com/ghostty-org/ghostty/commit/dda8e6f3146fc3cd2bcff0049cfc8867b3e7b58a) sys: add secure random override option with a platform default ([@mitchellh](https://github.com/mitchellh))
- [`60a1ae2`](https://github.com/ghostty-org/ghostty/commit/60a1ae2df755629dc7aa7d7aac38569ca46d43a5) libghostty: add ghostty_terminal_paste C API with paste events example ([@mitchellh](https://github.com/mitchellh))
- [`e424060`](https://github.com/ghostty-org/ghostty/commit/e4240606752e5e4eb480b69104d75db0054f71c8) libghostty: centralize pasting to `ghostty_terminal_paste`, enable mode 5522 ([#13978](https://github.com/ghostty-org/ghostty/issues/13978)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Note: this has no changes for Ghostty GUI yet.** This only impacts
  libghostty-vt.
  
  This introduces a new `ghostty_terminal_paste` C API along with a
  central `terminal.paste.paste` function that handles (1) mode 5522
  (Kitty clipboard) (2) bracketed paste (3) normal paste all in one place,
  combined with unsafe value detection and proper xterm-style newline
  handling.
  
  Terminal pasting is now stateful because for the Kitty clipboard
  protocol in particular, it must mint "grants" that stay with the
  terminal. Previously, paste encoding was stateless.
  
  To start, this is only exposed/used by libghostty to enable Kitty
  clipboard handling.
  
  Other changes:
  
  - **IO: randomSecure.** This also adds the `io.randomSecure`
  implementation to `TinyIo` and a global sys override for it because
  Kitty clipboard requires the ability to create one-time passwords and
  the implementation (following Kitty) requires a crypto random source.
  The sys model is for libghostty embedders.
  
  - **New C result value: rejected.** This introduces a new C result enum
  value "rejected" for values that are valid but rejected for some reason.
  Its very possible that prior "invalid value" users will have to update
  to this, and I recognize that its close to both but it fills an
  important semantic difference.
  
  Also note this still _eagerly_ requires all clipboard contents. I want
  to move to a callback based model but it made the PR much more
  complicated. I plan on playing with that before converting apprt's to
  this.
  ```
- [`5834a0e`](https://github.com/ghostty-org/ghostty/commit/5834a0e3df621802e9578e4562d88b0c2ad4ada8) Update VOUCHED list ([#13977](https://github.com/ghostty-org/ghostty/issues/13977)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13976#discussioncomment-18121426)
  from @pluiedev.
  
  Denounce: @tangivis
  ```
- [`da00936`](https://github.com/ghostty-org/ghostty/commit/da0093671a12cdbdbe62b70099113cca454cd997) Update VOUCHED list ([#13975](https://github.com/ghostty-org/ghostty/issues/13975)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13899#discussioncomment-18120807)
  from @jcollie.
  
  Vouch: @j-c-m
  ```

## August 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32588364477), [2](https://github.com/ghostty-org/ghostty/actions/runs/32584512359), [3](https://github.com/ghostty-org/ghostty/actions/runs/32564900757), [4](https://github.com/ghostty-org/ghostty/actions/runs/32563532476), [5](https://github.com/ghostty-org/ghostty/actions/runs/32561819941), [6](https://github.com/ghostty-org/ghostty/actions/runs/32552331897)  
Summary: 6 runs • 15 commits • 4 authors

### Changes

- [`7c845e8`](https://github.com/ghostty-org/ghostty/commit/7c845e8af5b2e0dc508f3f64c08383985bb536ed) terminal/kitty: drag and drop command decoding ([@mitchellh](https://github.com/mitchellh))
- [`38746b8`](https://github.com/ghostty-org/ghostty/commit/38746b8c14321004edaed584c2bf3d61b1cfd676) terminal/kitty: drag and drop response encoding ([@mitchellh](https://github.com/mitchellh))
- [`50f69b8`](https://github.com/ghostty-org/ghostty/commit/50f69b883cc75061441deadcbcbee9ecf6fc81b7) terminal/kitty: drag and drop drop state machine ([@mitchellh](https://github.com/mitchellh))
- [`af8d28a`](https://github.com/ghostty-org/ghostty/commit/af8d28a940beb3dd41d16a885c1f92c729aede37) terminal/kitty: drag and drop stream handler ([@mitchellh](https://github.com/mitchellh))
- [`db2f8be`](https://github.com/ghostty-org/ghostty/commit/db2f8be59011b09e4943cade3299e83686dc68d0) terminal/kitty: dnd docs ([@mitchellh](https://github.com/mitchellh))
- [`da5ddcb`](https://github.com/ghostty-org/ghostty/commit/da5ddcb0857c0e4ddb32f7a089911e9038d040f3) terminal: Kitty drag and drop protocol drop-only core logic and state machine ([#13973](https://github.com/ghostty-org/ghostty/issues/13973)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds out the core logic and state machine for the Kitty drag and
  drop protocol for _drops only_. This hooks it into libghostty-vt's Zig
  API but it isn't available to the C API and it isn't hooked up to any
  Ghostty GUI. It isn't really recommended that Zig consumers integrate
  this yet because I'm sure the API will continue to change dramatically
  as I address the missing features: drag source, remote drops, etc.
  
  The major thing this does it the core `src/terminal/kitty/dnd.zig` stuff
  with e2e tests extracted from Kitty's own `kitty_tets/dnd.py`. So this
  verifies that what we have so far is working properly.
  ```
- [`6959fd4`](https://github.com/ghostty-org/ghostty/commit/6959fd46c6ea7e6a2e5c2f9c680158db2f6f82f5) libghostty: implement Kitty clipboard protocol write only ([@mitchellh](https://github.com/mitchellh))
  ```text
  This implements only the clipboard _write_ side of the Kitty clipboard
  protocol for libghostty-vt. libghostty users don't need to do anything,
  this all automatically works since it just piggy-backs on the previous
  clipboard write effect.
  
  Clipboard reading is far more complicated because we don't have anything
  designed yet for libghostty-vt that does async requests (e.g. to ask the
  user for permission). I need to think about that more.
  ```
- [`4f49dc2`](https://github.com/ghostty-org/ghostty/commit/4f49dc2b8bfcd8b1a33de8a95d3b1a1a7135496f) libghostty: implement Kitty clipboard protocol reads via clipboard_read effect ([@mitchellh](https://github.com/mitchellh))
- [`3b9c4e0`](https://github.com/ghostty-org/ghostty/commit/3b9c4e0ddbe953540243af89cf11fad26f297088) libghostty: implement Kitty clipboard protocol read/write ([#13963](https://github.com/ghostty-org/ghostty/issues/13963)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This implements the full Kitty clipboard protocol for libghostty-vt.
  libghostty users need to only have the clipboard read/write effect for
  this to work. This doesn't yet do mode 5522.
  ```
- [`ef01d5f`](https://github.com/ghostty-org/ghostty/commit/ef01d5fda746398f8ad269f6589e53ba47362657) gtk: avoid physical fallback for XKB modifiers ([@tothedarktowercame](https://github.com/tothedarktowercame))
- [`5851d98`](https://github.com/ghostty-org/ghostty/commit/5851d98615187d85052e41042bcf66e0ccec11d4) gtk: avoid physical fallback for XKB modifiers ([#13967](https://github.com/ghostty-org/ghostty/issues/13967)) ([@jcollie](https://github.com/jcollie))
  ````text
  Hi, I noticed that this XKB config line was causing problems for
  Ghosttty:
  
  ```
      key <DELE> {   [ ISO_Level3_Shift ] };
  ```
  
  That's a valid reconfiguration of the "delete key" as a modifier, and
  the same worked find in other terminal emulators (like Alacritty). With
  Ghosttty, I was getting actual `<delete>` behaviour whenever I pressed
  the modifier key (although the modifier engaged after that).
  
  This patch fixes it. In line with your AI disclose policy: I made the
  patch with Codex Sol. The logical fix is very succinct, and the bulk of
  the patch works around an underlying issue to do with GDK not
  recognising some modifiers as modifiers. I've tested the implementation
  and the patch definitely resolves it!
  ````
- [`d03cd1f`](https://github.com/ghostty-org/ghostty/commit/d03cd1f5340ff2841bbe88a3fb9c70bdd2e69e76) Update VOUCHED list ([#13970](https://github.com/ghostty-org/ghostty/issues/13970)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13966#discussioncomment-18114178)
  from @jcollie.
  
  Vouch: @by-nelson
  ```
- [`2021d2a`](https://github.com/ghostty-org/ghostty/commit/2021d2addb8c193675531ade4cb838b27089e883) Update VOUCHED list ([#13969](https://github.com/ghostty-org/ghostty/issues/13969)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13968#discussioncomment-18113956)
  from @pluiedev.
  
  Vouch: @tothedarktowercame
  ```
- [`e03475c`](https://github.com/ghostty-org/ghostty/commit/e03475c0cc52b9a6b01930380c61cd354e60a36a) libghostty: clipboard_read effect, enables OSC52 reads ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a `clipboard_read` effect to the stream terminal handler and a
  matching `GHOSTTY_TERMINAL_OPT_CLIPBOARD_READ` callback to the
  libghostty-vt C API so that embedders can answer OSC 52 read requests
  (the `?` payload).
  
  This is a _blocking_ effect: if the embedder needs to ask the user for
  permission, the entire VT processing pipeline is _blocked_ during the
  callback. This is a purposeful simplification choice compared to how
  Ghostty GUI works with async requests. I think its reasonable, it
  eliminates a TON of complexity.
  
  If the effect isn't set, then any clipboard reads are denied.
  
  This can be expanded easily to support Kitty clipboard protocol later.
  ```
- [`36676c5`](https://github.com/ghostty-org/ghostty/commit/36676c5728b626738ed73d288145c50a5494971e) libghostty: clipboard_read effect, enables OSC52 reads ([#13965](https://github.com/ghostty-org/ghostty/issues/13965)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a `clipboard_read` effect to the stream terminal handler and a
  matching `GHOSTTY_TERMINAL_OPT_CLIPBOARD_READ` callback to the
  libghostty-vt C API so that embedders can answer OSC 52 read requests
  (the `?` payload).
  
  This is a _blocking_ effect: if the embedder needs to ask the user for
  permission, the entire VT processing pipeline is _blocked_ during the
  callback. This is a purposeful simplification choice compared to how
  Ghostty GUI works with async requests. I think its reasonable, it
  eliminates a TON of complexity.
  
  If the effect isn't set, then any clipboard reads are denied.
  
  This can be expanded easily to support Kitty clipboard protocol later.
  ```

## August 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32529091580), [2](https://github.com/ghostty-org/ghostty/actions/runs/32523564540), [3](https://github.com/ghostty-org/ghostty/actions/runs/32518446429), [4](https://github.com/ghostty-org/ghostty/actions/runs/32510792341), [5](https://github.com/ghostty-org/ghostty/actions/runs/32504827151), [6](https://github.com/ghostty-org/ghostty/actions/runs/32499136892), [7](https://github.com/ghostty-org/ghostty/actions/runs/32489342394), [8](https://github.com/ghostty-org/ghostty/actions/runs/32486497354), [9](https://github.com/ghostty-org/ghostty/actions/runs/32478620777), [10](https://github.com/ghostty-org/ghostty/actions/runs/32448926918)  
Summary: 10 runs • 50 commits • 7 authors

### Changes

- [`c67a1db`](https://github.com/ghostty-org/ghostty/commit/c67a1db991842f0c0962291581c947011eaa0334) osc: parse the Kitty desktop notification protocol (OSC 99) ([@jcollie](https://github.com/jcollie))
  ```text
  This includes only parsing of the OSC. You cannot use OSC 99 to send
  notifications. Uses lazy parsing of the metadata modelled on the new OSC
  133 behavior.
  ```
- [`93bf7d8`](https://github.com/ghostty-org/ghostty/commit/93bf7d8104a033a643e78a747ca06500f51539e7) osc: address review comments on OSC 99 (Kitty desktop notifications) ([@jcollie](https://github.com/jcollie))
  ```text
  * Add comments to Option keys to clarify their usage without having
    to refer to the spec online.
  * Use `indexOfNone` to simplify code.
  ```
- [`202e639`](https://github.com/ghostty-org/ghostty/commit/202e639d97bada1220d542821b2063e41f46d29f) osc: clean up comments in OSC 99 ([@jcollie](https://github.com/jcollie))
- [`301b69d`](https://github.com/ghostty-org/ghostty/commit/301b69df43484b8709da6c073454fab388850af7) osc: save terminator from OSC 99 in case we need to send a response ([@jcollie](https://github.com/jcollie))
- [`9a8e7ae`](https://github.com/ghostty-org/ghostty/commit/9a8e7ae1869dd75a312b2cc009a1294c52361e34) core: add alias for Kitty desktop notification OSC struct ([@jcollie](https://github.com/jcollie))
- [`aa4ec35`](https://github.com/ghostty-org/ghostty/commit/aa4ec3508ecb789c69585dd073ca474e2297f6be) osc 99: address review feedback ([@jcollie](https://github.com/jcollie))
  ```text
  * Fix typos.
  * Eliminate metadata parsing code duplication.
  * Improve documentation.
  * Ensure assert is comptime only.
  * Derive valid metadata characters from valid identifier characters.
  ```
- [`07f33ad`](https://github.com/ghostty-org/ghostty/commit/07f33ad91453ebf9bbfdc24a26d935bcb949d08a) osc 99 & 5522: share metadata parsing code ([@jcollie](https://github.com/jcollie))
  ```text
  Reduce redundant code by sharing the metadata parsing code
  between the OSC 99 & OSC 5522 parsers.
  ```
- [`073bffc`](https://github.com/ghostty-org/ghostty/commit/073bffcff4aeb1f748edda397b4f2d367296c9f2) osc 99: eliminate unnecessary inline switch branches ([@jcollie](https://github.com/jcollie))
- [`ca9e5b1`](https://github.com/ghostty-org/ghostty/commit/ca9e5b1301354018f92152c1282a922baacfa0e1) terminal/osc: kitty notification parsing feedback ([@mitchellh](https://github.com/mitchellh))
- [`5984d6f`](https://github.com/ghostty-org/ghostty/commit/5984d6f7326845312bf5c00f4d4ae181cd733c41) terminal: add isTextMime helper for plain text MIME type names ([@mitchellh](https://github.com/mitchellh))
- [`25b1170`](https://github.com/ghostty-org/ghostty/commit/25b1170d422f06146661eb1531c1b574d20f1771) terminal: add kitty clipboard protocol (OSC 5522) command parsing ([@mitchellh](https://github.com/mitchellh))
- [`e28acd9`](https://github.com/ghostty-org/ghostty/commit/e28acd928c4c02e8a7d8999e55b4d118098ec423) terminal: add kitty clipboard protocol (OSC 5522) response encoding ([@mitchellh](https://github.com/mitchellh))
- [`33cda4d`](https://github.com/ghostty-org/ghostty/commit/33cda4dc5dbfd0478f6891fb4b53844a4fbee17c) terminal: reload cell pointers when print grows a page ([@ArneshBanerjee](https://github.com/ArneshBanerjee))
  ```text
  Terminal.print's grapheme path holds a raw pointer to the previous cell
  while it writes other cells. Writing the wide spacer tail can grow the
  page to fit the cursor hyperlink, and growing replaces the page, so the
  pointer is left dangling and the following appendGrapheme writes into
  freed memory.
  
  Record the cursor page identity (node pointer plus serial, since pooled
  nodes can reuse an address) before the spacer write and reload the cell
  only when the page actually changed, so the common path costs nothing.
  
  The same function had three more pointers held across an operation that
  can replace a page: the grapheme move after a wrap, the grapheme append
  loop, and printCell's assert on a failed hyperlink write. Those now read
  through the cursor or a freshly resolved pin.
  
  Fixes #11261
  ```
- [`7a940ec`](https://github.com/ghostty-org/ghostty/commit/7a940ec02830fcd39f94ea9a28974c2a82d96486) terminal: add kitty clipboard protocol (OSC 5522) write transactions ([@mitchellh](https://github.com/mitchellh))
- [`6f007e7`](https://github.com/ghostty-org/ghostty/commit/6f007e7678a4d893a5c73df2f0305b1e00609b5a) terminal: add kitty clipboard protocol (OSC 5522) session password grants ([@mitchellh](https://github.com/mitchellh))
- [`f2d4b32`](https://github.com/ghostty-org/ghostty/commit/f2d4b32be3eb8c17f1ca943dda82a6506e7260b3) terminal: expose kitty clipboard protocol (OSC 5522) for stream dispatch ([@mitchellh](https://github.com/mitchellh))
- [`07c6fc2`](https://github.com/ghostty-org/ghostty/commit/07c6fc21ba79f2d3d320f3300029269ebf84030b) terminal: add kitty clipboard paste events mode (5522), disabled for now ([@mitchellh](https://github.com/mitchellh))
- [`bcf44b4`](https://github.com/ghostty-org/ghostty/commit/bcf44b40e69ffc4f32216016bb8e6ee68560cae2) terminal: dispatch OSC 5522 as a kitty_clipboard stream action, unhandled ([@mitchellh](https://github.com/mitchellh))
- [`128ec7c`](https://github.com/ghostty-org/ghostty/commit/128ec7cd047ab0d9ceb4f0b5c2c449984702266d) terminal: rename paste_events mode to kitty_paste_events ([@mitchellh](https://github.com/mitchellh))
- [`a8c3ab1`](https://github.com/ghostty-org/ghostty/commit/a8c3ab1915c9dc9cecf4ae93b5337d65f1bfffbf) simd: fix scalar base64 empty input handling causing a crash ([@mitchellh](https://github.com/mitchellh))
- [`c8634f3`](https://github.com/ghostty-org/ghostty/commit/c8634f3fce12f8189ed058e018195eb693f8562b) terminal: reload cell pointers when print grows a page ([#13960](https://github.com/ghostty-org/ghostty/issues/13960)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11261.
  
  `Terminal.print`'s grapheme path caches a `*Cell` for the previous cell
  and keeps using it after writing other cells. Writing the wide spacer
  tail calls `printCell`, which can grow the page to make room for the
  cursor hyperlink. Growing clones the page and frees the old one, so the
  cached pointer dangles and the following `appendGrapheme` writes into
  freed memory. The second test case in the issue reproduces it.
  
  Rather than recomputing `prev` on every use, which is too expensive for
  this path, the fix records the cursor page identity before the spacer
  write and reloads the cell only if the page actually changed. Node
  pointer plus serial is used because nodes are pooled and a replacement
  can land on the same address. Nothing changes when the page does not
  grow.
  
  Three other pointers in the same function were held across an operation
  that can replace a page, so they are now read through the cursor or a
  freshly resolved pin: the grapheme move after a wrap, the grapheme
  append loop, and `printCell`'s assert on a failed hyperlink write.
  
  Tests:
  
  - `Terminal: VS16 widening when the spacer tail grows the page` fills
  the page hyperlink map so the spacer tail is what forces growth. It
  crashes without the fix.
  - `Terminal: grapheme transfer when widening wraps to the next line`
  covers the wrap path where the previous cell already holds grapheme
  data, which had no test before.
  
  `zig build test` passes.
  ```
- [`819b241`](https://github.com/ghostty-org/ghostty/commit/819b241dec1a3a6a4c1c87f0b01152c99197c02a) terminal: Kitty Clipboard core logic (no apprt hookups yet) ([#13962](https://github.com/ghostty-org/ghostty/issues/13962)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds all the core logic and tests for the full Kitty Clipboard
  protocol in the `src/terminal` package.
  
  This is purposefully shaped similarly to the way we organize Kitty
  graphics. There is an umbrella `clipboard.zig` and then a bunch of leaf
  zig files that cover: request parsing, response encoding, state
  management, etc. I think that worked really well for Kitty graphics so
  we're doing it here too.
  
  The core logic covers every part of the protocol: read and write.
  
  The only thing hooked up to the end user is a DECRQM for mode 5522 will
  return unset. And it can't be set currently (since it never works yet).
  Outside of that, nothing in this diff is actually used in the real
  binary.
  
  **AI usage:** Validation against the spec and Kitty impl, test writing
  and coverage validation, of course some code writing but within the
  broad organizational shape I defined. I went through and either rewrote
  or wrote all the comments myself plus this PR message.
  ```
- [`74a133e`](https://github.com/ghostty-org/ghostty/commit/74a133ea17f197482aea5880be5a7c575458104a) Update VOUCHED list ([#13961](https://github.com/ghostty-org/ghostty/issues/13961)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13960#issuecomment-5374295208)
  from @jcollie.
  
  Vouch: @ArneshBanerjee
  ```
- [`4b915e3`](https://github.com/ghostty-org/ghostty/commit/4b915e3bc460ec8c6765e3f4637dbfb74f7083fa) terminal/kitty: complete animation command parsing ([@mitchellh](https://github.com/mitchellh))
- [`d8b920e`](https://github.com/ghostty-org/ghostty/commit/d8b920e504670a7603c912e9219668e2b358b909) terminal/kitty: animation frame storage, composition, and playback ([@mitchellh](https://github.com/mitchellh))
- [`d2ffeb5`](https://github.com/ghostty-org/ghostty/commit/d2ffeb5ba5009427babfec730f55e3084b56eda3) terminal/kitty: execute animation commands ([@mitchellh](https://github.com/mitchellh))
- [`73903f7`](https://github.com/ghostty-org/ghostty/commit/73903f76aa39f1c8ae67e42b61d9712b7b78be2e) terminal/c: image data returns the current animation frame ([@mitchellh](https://github.com/mitchellh))
- [`aee7bf3`](https://github.com/ghostty-org/ghostty/commit/aee7bf347564f1db02f4788186464d4c51ea9770) renderer: drive kitty graphics animation ([@mitchellh](https://github.com/mitchellh))
- [`f3e98fb`](https://github.com/ghostty-org/ghostty/commit/f3e98fb72b6bf12f0c7029993fd37ee1137edcec) terminal/kitty: X handling properly since 0.45 fix ([@mitchellh](https://github.com/mitchellh))
- [`322d7ae`](https://github.com/ghostty-org/ghostty/commit/322d7ae789b06e4b3987b8cdd33c864b5bdb0412) terminal/kitty: switch to wuffs for pixel work ([@mitchellh](https://github.com/mitchellh))
- [`dff13b4`](https://github.com/ghostty-org/ghostty/commit/dff13b41c9932ee871f4d1e700c0e1ab8e27edff) pkg/{afl++,wuffs}: fix builds for CI ([@mitchellh](https://github.com/mitchellh))
- [`4be9d78`](https://github.com/ghostty-org/ghostty/commit/4be9d782e3cc7c96f2f020b7d04aed5ec83b9d8a) terminal: avoid Kitty image reset test if no kitty images ([@mitchellh](https://github.com/mitchellh))
- [`a88ad03`](https://github.com/ghostty-org/ghostty/commit/a88ad03e692c2831f7375f4ac00d54653d2b21af) kitty graphics: animation support ([#13943](https://github.com/ghostty-org/ghostty/issues/13943)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #5255
  
  This adds support for the Kitty graphics animation frames
  (https://sw.kovidgoyal.net/kitty/graphics-protocol/#animation),
  completely (transmission, control, composition, rendering, etc.).
  
  This does it in a somewhat naive way: we pre-compose all frames and
  store the full RGBA in-memory. Animation is already rare enough, and I
  wanted to focus on things working first, so I didn't optimize this very
  well. I also wanted this PR to be relatively understandable up front. We
  can add complexity later.
  
  But, this adds very little overhead to a non-animation using Kitty
  graphics user. The animation state is heap-allocated only when its
  needed. So, it just costs a pointer sized field on every image. Plus a
  little bit of overhead in the loading state (which itself is heap
  allocated during image load only).
  
  On the renderer side, this **unifies Kitty graphics animations and
  custom shader animations into a single animation abstraction.** This
  simplified our renderer thread and made the generic renderer more
  complicated (slightly, its not much!).
  
  **AI usage:** Test writing, validation against the spec/reference
  implementation. I drove the main architecture and shaped out the
  functions and params, animation storage, etc. I had AI fill in some of
  the blanks that I spaced out. Commit messages, comments, and this PR
  message are written by me.
  
  ## Demo
  
  
  
  https://github.com/user-attachments/assets/91be3d66-a5ff-4cab-b3e9-e672f39861c9
  ```
- [`08c80d2`](https://github.com/ghostty-org/ghostty/commit/08c80d253aefef517a010f16cc026aa4cccaa957) po/zh_TW: add missing translations ([@a-lang](https://github.com/a-lang))
- [`08df9f6`](https://github.com/ghostty-org/ghostty/commit/08df9f6e29a93e16d64c3c70cf7200dab4526a15) po/zh_TW: remove trailing blank line at EOF ([@a-lang](https://github.com/a-lang))
- [`79e78e6`](https://github.com/ghostty-org/ghostty/commit/79e78e6c0325b37539b1b9383f6e361462655395) Merge branch 'ghostty-org:main' into l10n-tw ([@a-lang](https://github.com/a-lang))
- [`b5716a8`](https://github.com/ghostty-org/ghostty/commit/b5716a87103961bad7d2a51f2b0daa0266de8fa2) po/zh_TW: refine two translations per review feedback ([@a-lang](https://github.com/a-lang))
- [`f0eaaea`](https://github.com/ghostty-org/ghostty/commit/f0eaaea6fe14dd52225806fb13c5812dee24bbc4) po/zh_TW: refine translations for reset, copy, and placeholder strings ([@a-lang](https://github.com/a-lang))
- [`fa7fe3b`](https://github.com/ghostty-org/ghostty/commit/fa7fe3b3afd04f11281358ee3704f40b628f6e35) po/zh_TW: add missing translations ([#13690](https://github.com/ghostty-org/ghostty/issues/13690)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translate the remaining 181 untranslated strings in po/zh_TW.po,
  bringing it to 100% coverage (252/252), including the strings added by
  the recent template update.
  
  All 72 existing translations are preserved unchanged.
  ```
- [`ffad4c6`](https://github.com/ghostty-org/ghostty/commit/ffad4c6ec480647769f1b9b4be6263c4e0d0796c) update mirror, support git+https dependencies ([@mitchellh](https://github.com/mitchellh))
- [`d617133`](https://github.com/ghostty-org/ghostty/commit/d6171332cd301eabdb04219a2220fce7f9be4057) update mirror, support git+https dependencies ([#13957](https://github.com/ghostty-org/ghostty/issues/13957)) ([@mitchellh](https://github.com/mitchellh))
- [`bcbc93a`](https://github.com/ghostty-org/ghostty/commit/bcbc93a6b9ccb5eb96e7de4739af369243f78629) terminal/kitty: preserve image limits across full reset ([@mitchellh](https://github.com/mitchellh))
  ```text
  RIS previously cleared configured storage limits and allowed mediums.
  We now retain this properly.
  ```
- [`442046f`](https://github.com/ghostty-org/ghostty/commit/442046f8eecfb879d30a18ae1563a43fc0260a8d) terminal/kitty: preserve image limits across full reset ([#13951](https://github.com/ghostty-org/ghostty/issues/13951)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  RIS previously cleared configured storage limits and allowed mediums. We
  now retain this properly.
  ```
- [`10d7326`](https://github.com/ghostty-org/ghostty/commit/10d73268897fc17412855f022fffc846ad98fe1b) macOS: clean up GlassViewModel ([@bo2themax](https://github.com/bo2themax))
- [`99d7b5f`](https://github.com/ghostty-org/ghostty/commit/99d7b5fd508eededf2de08ca641f2d83027631f8) macOS: clean up GlassViewModel ([#13944](https://github.com/ghostty-org/ghostty/issues/13944)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Forgot to delete the autocomplete template in the previous pr...
  ```
- [`619555d`](https://github.com/ghostty-org/ghostty/commit/619555d1ccd8ac583b3aa53ac2d335c28663aeb4) pkg/wuffs: build without libc ([@mitchellh](https://github.com/mitchellh))
  ```text
  This modifies our wuffs dependency so that it no longer requires libc.
  
  This unblocks using wuffs from libghostty-vt on freestanding targets,
  which we'll eventually want for some Kitty graphics stuff.
  ```
- [`ac9a2c4`](https://github.com/ghostty-org/ghostty/commit/ac9a2c4cd5772cd0d33aa7d3433a574e2e3a3c41) pkg/wuffs: build without libc ([#13942](https://github.com/ghostty-org/ghostty/issues/13942)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This modifies our wuffs dependency so that it no longer requires libc.
  
  This unblocks using wuffs from libghostty-vt on freestanding targets,
  which we'll eventually want for some Kitty graphics stuff.
  ```
- [`311d383`](https://github.com/ghostty-org/ghostty/commit/311d38376634f90869b97877254c3e8c4d8ab918) Update VOUCHED list ([#13948](https://github.com/ghostty-org/ghostty/issues/13948)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13947#discussioncomment-18105162)
  from @trag1c.
  
  Denounce: @DIDOUOUGHA
  ```
- [`86db307`](https://github.com/ghostty-org/ghostty/commit/86db30785c9310ba5e7f3c7634ea70d0c61df37c) pkg/wuffs: fix gray+alpha to RGBA swizzle failing for all inputs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The gaToRgba swizzle requested a YA_PREMUL source pixel format from
  the wuffs pixel swizzler, but wuffs does not support YA_PREMUL as a
  swizzle source. As a result, gaToRgba returned error.WuffsError for every input.
  
  The path can't happen in Ghostty GUI today since our PNG decoding always
  produces RGBA, but it is possible via libghostty that submit grey+alpha
  directly.
  ```
- [`42a161a`](https://github.com/ghostty-org/ghostty/commit/42a161aadad94d593b87db12d59c93f8915d3921) pkg/wuffs: fix gray+alpha to RGBA swizzle failing for all inputs ([#13941](https://github.com/ghostty-org/ghostty/issues/13941)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The gaToRgba swizzle requested a YA_PREMUL source pixel format from the
  wuffs pixel swizzler, but wuffs does not support YA_PREMUL as a swizzle
  source. As a result, gaToRgba returned error.WuffsError for every input.
  
  The path can't happen in Ghostty GUI today since our PNG decoding always
  produces RGBA, but it is possible via libghostty that submit grey+alpha
  directly.
  ```

## August 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32428404813), [2](https://github.com/ghostty-org/ghostty/actions/runs/32421386810), [3](https://github.com/ghostty-org/ghostty/actions/runs/32413190698), [4](https://github.com/ghostty-org/ghostty/actions/runs/32399782294), [5](https://github.com/ghostty-org/ghostty/actions/runs/32393437956), [6](https://github.com/ghostty-org/ghostty/actions/runs/32387594013), [7](https://github.com/ghostty-org/ghostty/actions/runs/32380496303), [8](https://github.com/ghostty-org/ghostty/actions/runs/32327389360), [9](https://github.com/ghostty-org/ghostty/actions/runs/32324155930), [10](https://github.com/ghostty-org/ghostty/actions/runs/32318148403)  
Summary: 10 runs • 34 commits • 5 authors

### Changes

- [`d30a9c4`](https://github.com/ghostty-org/ghostty/commit/d30a9c424d3e4afd8eada988e154c77937a3c59c) terminal: clear cursor pin garbage flag on screen reset ([@mitchellh](https://github.com/mitchellh))
- [`a32a100`](https://github.com/ghostty-org/ghostty/commit/a32a100d4bcef7fe5ee639ea4075545c1eb2eeba) terminal/kitty: centralize placeholder placement lookup ([@mitchellh](https://github.com/mitchellh))
- [`cd5f9ee`](https://github.com/ghostty-org/ghostty/commit/cd5f9eef0a1ac100b022acdfb565d64579c03225) terminal/kitty: add relative placement storage ([@mitchellh](https://github.com/mitchellh))
- [`f5b3efe`](https://github.com/ghostty-org/ghostty/commit/f5b3efe45299437aa8416be9e2a4ebcde47690e3) terminal/c: resolve relative placement viewport positions ([@mitchellh](https://github.com/mitchellh))
- [`33ca9e5`](https://github.com/ghostty-org/ghostty/commit/33ca9e5ddc6db3be63717306735ffcf8e725401a) terminal/kitty: create relative placements from put commands ([@mitchellh](https://github.com/mitchellh))
- [`9490f71`](https://github.com/ghostty-org/ghostty/commit/9490f71342151bea3523d388430328210dde6f96) renderer: position relative kitty image placements ([@mitchellh](https://github.com/mitchellh))
- [`08450e2`](https://github.com/ghostty-org/ghostty/commit/08450e21e5a3ad94b62d1e67f9eda554dfa1c971) kitty graphics: support relative placements ([#13939](https://github.com/ghostty-org/ghostty/issues/13939)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds full support for relative placements:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#relative-placements
  (`R=` and `Q=`). The high-level description is that this allows images
  to be placed relative to other images. For more details, the spec
  explains it better than I can, or the demo video below.
  
  The implementation here was pretty straightforward. It mainly revolved
  around adding parent resolution logic to puts (and validation), and
  proper unparented placement reaping in the right points, and then the
  various tests around that. The renderer logic itself was also
  straigthforward, I had to add some offset resolution to the core
  graphics storage but we can reuse that. The main complexity -- as always
  -- (MY OWN EMDASHES) is Unicode placeholders. But... also not too hard.
  
  After this, the only feature we don't support from the protocol is
  animation.
  
  **AI usage:** Test writing, validation against spec/reference, judging,
  and some "fill in the function/block". I setup the overall shape of the
  implementation.
  
  ## Demo
  
  Ghostty on the left, Kitty on the right
  
  
  
  https://github.com/user-attachments/assets/dc2ec3ac-480a-4587-94e4-06a842f9b3f4
  ```
- [`1ffdd74`](https://github.com/ghostty-org/ghostty/commit/1ffdd7415a9fd852091d97f1de68fd8bf5a16cfd) os: remove flaky TempDir handle checks ([@mitchellh](https://github.com/mitchellh))
  ```text
  The TempDir tests saved directory descriptors before close and expected
  `fcntl(F_GETFD)` to return `EBADF` afterward. A descriptor number
  becomes available for reuse as soon as it is closed.
  
  Unrelated I/O could reuse either number before the assertion, causing
  the Valgrind job to report a leak even though TempDir closed both
  handles correctly [1].
  
  Remove the raw descriptor assertions and keep coverage of observable
  delete and retain behavior. Explain at both close sites why descriptor
  numbers cannot identify the original handles after close.
  
  [1]: https://github.com/ghostty-org/ghostty/actions/runs/32410237002/job/96561246487
  ```
- [`c5f4f00`](https://github.com/ghostty-org/ghostty/commit/c5f4f00ed3e7c43528461968b8d1611f15f2bb39) fix up recent Valgrind errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  - ci: valgrind runs now fail when Memcheck finds an unsuppressed error.
  - fix real memory issues in unit tests
  - add a suppression for Zig's flate compression which documents as
    purposely using undefined memory
  ```
- [`04d6954`](https://github.com/ghostty-org/ghostty/commit/04d6954ebf7cffef4c551d77761b4f4820a7e070) os: remove flaky TempDir handle checks ([#13937](https://github.com/ghostty-org/ghostty/issues/13937)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The TempDir tests saved directory descriptors before close and expected
  `fcntl(F_GETFD)` to return `EBADF` afterward. A descriptor number
  becomes available for reuse as soon as it is closed.
  
  Unrelated I/O could reuse either number before the assertion, causing
  the Valgrind job to report a leak even though TempDir closed both
  handles correctly [1].
  
  Remove the raw descriptor assertions and keep coverage of observable
  delete and retain behavior. Explain at both close sites why descriptor
  numbers cannot identify the original handles after close.
  
  [1]:
  https://github.com/ghostty-org/ghostty/actions/runs/32410237002/job/96561246487
  ```
- [`16b39f4`](https://github.com/ghostty-org/ghostty/commit/16b39f45a8d0ad9d2d19ea1fe9cf94c44c0e740b) fix up recent Valgrind errors ([#13938](https://github.com/ghostty-org/ghostty/issues/13938)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  No issues in actual shipped code found.
  
  - ci: valgrind runs now fail when Memcheck finds an unsuppressed error.
  - fix real memory issues in unit tests
  - add a suppression for Zig's flate compression which documents as
  purposely using undefined memory
  ```
- [`90bce0d`](https://github.com/ghostty-org/ghostty/commit/90bce0d2dd3bd8eaf5487ff0e7475f0a03d05e94) terminal/kitty: scroll and clip image placements within margins ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #4323
  
  The Kitty graphics protocol requires that when margins are defined
  and index commands are used, only images entirely within the scroll
  region are scrolled, and that they are clipped when scrolling would
  cause them to extend outside the region [1].
  
  This implements that part of the spec.
  
  Benchmarked pure `\n` terminal streams to ensure that the no-image case
  is not regressed. Our branch hints plus checks on placements keep that
  true. When images are present, things get a lot slower but thats
  acceptable for now.
  
  [1]: https://sw.kovidgoyal.net/kitty/graphics-protocol/#interaction-with-other-terminal-actions
  ```
- [`1ffa77c`](https://github.com/ghostty-org/ghostty/commit/1ffa77c90bc47e8200e2c2c88b34ef6745ffd834) terminal/kitty: scroll and clip image placements within margins ([#13935](https://github.com/ghostty-org/ghostty/issues/13935)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #4323
  
  The Kitty graphics protocol requires that when margins are defined and
  index commands are used, only images entirely within the scroll region
  are scrolled, and that they are clipped when scrolling would cause them
  to extend outside the region [1].
  
  This implements that part of the spec.
  
  Benchmarked pure `\n` terminal streams to ensure that the no-image case
  is not regressed. Our branch hints plus checks on placements keep that
  true. When images are present, things get a lot slower but thats
  acceptable for now.
  
  ## Demo
  
  
  
  https://github.com/user-attachments/assets/22e23c8b-ffd4-48fb-9e86-31e810d36ea0
  
  
  
  [1]:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#interaction-with-other-terminal-actions
  ```
- [`6b23c58`](https://github.com/ghostty-org/ghostty/commit/6b23c584cab57c8ac9714775dd0975eb7db32dd4) terminal/kitty: prevent auto-assigned image ID collisions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #2197
  
  Image transmissions without an explicit ID (i=) were assigned IDs from
  a wrapping counter starting with no collision check. The protocol allows
  clients to choose IDs anywhere in the u32 range, so an auto-assigned ID could
  collide.
  
  Number-based transmissions (I= without i=) now receive the smallest ID
  not currently in use. This probes the image map in an `O(N)` fashion but
  performance issues here require a pathological client and this implementation
  matches Kitty's performance as well.
  ```
- [`e660500`](https://github.com/ghostty-org/ghostty/commit/e6605009bb956eb7a24d5fd3fd5a40b99d1c1892) terminal/kitty: prevent auto-assigned image ID collisions ([#13934](https://github.com/ghostty-org/ghostty/issues/13934)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #2197
  
  Image transmissions without an explicit ID (i=) were assigned IDs from a
  wrapping counter starting with no collision check. The protocol allows
  clients to choose IDs anywhere in the u32 range, so an auto-assigned ID
  could collide.
  
  Number-based transmissions (I= without i=) now receive the smallest ID
  not currently in use. This probes the image map in an `O(N)` fashion but
  performance issues here require a pathological client and this
  implementation matches Kitty's performance as well.
  ```
- [`f7d29b1`](https://github.com/ghostty-org/ghostty/commit/f7d29b19e801f184f7526359c034644ace8e9615) terminal/kitty: accept empty graphics delete ranges ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `d=r`/`d=R` delete parser required a `y` key and enforced `x <= y`,
  rejecting the entire command with `error.InvalidFormat` otherwise. Both
  bounds now default to zero and neither is validated.
  
  This matches upstream reference implementation.
  ```
- [`48c7006`](https://github.com/ghostty-org/ghostty/commit/48c7006b9a0a4eff2f561acb8614796e839f41f4) terminal/kitty: accept empty graphics delete ranges ([#13932](https://github.com/ghostty-org/ghostty/issues/13932)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `d=r`/`d=R` delete parser required a `y` key and enforced `x <= y`,
  rejecting the entire command with `error.InvalidFormat` otherwise. Both
  bounds now default to zero and neither is validated.
  
  This matches upstream reference implementation.
  ```
- [`2427232`](https://github.com/ghostty-org/ghostty/commit/242723223f3e261dab9bfdb3e5e43fa247069cd7) terminal/kitty: fix various validation behaviors to match Kitty ([@mitchellh](https://github.com/mitchellh))
  ```text
  There are various validation behaviors we did that matched the spec but
  didn't match Kitty, because Kitty is written in C (these parts) and does
  a lot of C-ish things (like bool is any non-zero value, despite the spec
  saying 1/0).
  
  This also fixes a more major issue where invalid formats should be
  deferred until transmission finishes so we send a proper response. Right
  now we send no response which can cause a client to hang!
  ```
- [`b6cbaf5`](https://github.com/ghostty-org/ghostty/commit/b6cbaf54efe5dc5c0872e7b0c4e28e7cad771eb5) terminal/kitty: fix various validation behaviors to match Kitty ([#13933](https://github.com/ghostty-org/ghostty/issues/13933)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  There are various validation behaviors we did that matched the spec but
  didn't match Kitty, because Kitty is written in C (these parts) and does
  a lot of C-ish things (like bool is any non-zero value, despite the spec
  saying 1/0).
  
  This also fixes a more major issue where invalid formats should be
  deferred until transmission finishes so we send a proper response. Right
  now we send no response which can cause a client to hang!
  ```
- [`eeab85b`](https://github.com/ghostty-org/ghostty/commit/eeab85b9679920e4f23459171db8405157a589d7) terminal: clear progress bar on full reset ([@fornwall](https://github.com/fornwall))
  ```text
  Emit a progress_report remove effect from the full_reset arm, matching
  kitty and WezTerm which both clear progress on reset.
  
  Previously, only the termio StreamHandler removed the progress bar on
  RIS (ghostty#10178); the terminal stream handler used by libghostty-vt
  did not, so an embedder's progress bar would outlive the reset.
  ```
- [`b56c6d8`](https://github.com/ghostty-org/ghostty/commit/b56c6d88f81bd68d36a9dcb84fa43c1455df53b0) terminal: only clear the progress bar on full reset if there is one ([@fornwall](https://github.com/fornwall))
- [`b7ee3ab`](https://github.com/ghostty-org/ghostty/commit/b7ee3ab6b321470e0638d02aabb5043efdbe797b) Revert "terminal: only clear the progress bar on full reset if there is one" ([@fornwall](https://github.com/fornwall))
  ```text
  This reverts commit b56c6d88f81bd68d36a9dcb84fa43c1455df53b0.
  ```
- [`af15014`](https://github.com/ghostty-org/ghostty/commit/af150144e24c77beee400b353eeb5d8fc202137f) terminal: clear progress bar on full reset ([#13901](https://github.com/ghostty-org/ghostty/issues/13901)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Emit a `progress_report` remove effect from the `full_reset` arm,
  matching kitty and WezTerm which both clear progress on reset.
  
  Previously, only the termio `StreamHandler` removed the progress bar on
  RIS (#10178) - but the terminal stream handler used by `libghostty-vt`
  did not, so an embedder's progress bar would outlive the reset.
  ```
- [`fd17869`](https://github.com/ghostty-org/ghostty/commit/fd17869d15764a5a1f0f94e3b986e0a15eef0c43) macOS: rework for [#10943](https://github.com/ghostty-org/ghostty/issues/10943) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Keep the background color as it is and apply glass effect on top of it
  ```
- [`6f02d9a`](https://github.com/ghostty-org/ghostty/commit/6f02d9aad6d0fd4263b20e9a895ab4754b2ecc59) font: render glyf directly into output bitmap ([@jparise](https://github.com/jparise))
  ```text
  Glyf rasterization previously let z2d allocate its alpha surface, then
  duplicated the completed pixels into caller-owned storage. Back the z2d
  surface with the final bitmap instead, eliminating one allocation and a
  full bitmap copy for each non-empty glyph.
  ```
- [`9566a1a`](https://github.com/ghostty-org/ghostty/commit/9566a1a87eb04c85f7d9db5b62a138aa7e1a1879) termio: release initial input resources ([@jparise](https://github.com/jparise))
  ```text
  Initial input files remained open and their fully read buffers remained
  allocated after queueWrite copied their contents. Close these files on
  both startup success and failure, free their contents after queueing, and
  borrow raw values already owned by the arena.
  ```
- [`0de91ee`](https://github.com/ghostty-org/ghostty/commit/0de91eee32aa6bc8ac75c4bd868a297daa13a28a) font: render glyf directly into output bitmap ([#13929](https://github.com/ghostty-org/ghostty/issues/13929)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Glyf rasterization previously let z2d allocate its alpha surface, then
  duplicated the completed pixels into caller-owned storage. Back the z2d
  surface with the final bitmap instead, eliminating one allocation and a
  full bitmap copy for each non-empty glyph.
  ```
- [`aea0301`](https://github.com/ghostty-org/ghostty/commit/aea03011d08e2cba529cc8f21d1d5aeba2b447c5) termio: release initial input resources ([#13931](https://github.com/ghostty-org/ghostty/issues/13931)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Initial input files remained open and their fully read buffers remained
  allocated after queueWrite copied their contents. Close these files on
  both startup success and failure, free their contents after queueing,
  and borrow raw values already owned by the arena.
  
  **AI Usage:** This was spotted by GPT 5.6 Sol. I reworked the code a bit
  and understand it all.
  ```
- [`956a687`](https://github.com/ghostty-org/ghostty/commit/956a687d6393c57cf23176e00a86b74f4064441a) macOS: refine liquid glass styles ([#13928](https://github.com/ghostty-org/ghostty/issues/13928)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework for https://github.com/ghostty-org/ghostty/pull/10943;
  
  Keep the background color as it is and apply glass effect on top of it.
  Remove the color modification and keep our implementation relatively
  simple and more straightforward.
  
  This fixes https://github.com/ghostty-org/ghostty/issues/13914 and also
  ofc the linked issue in previous pr.
  
  ### Regular
  
  
  https://github.com/user-attachments/assets/b44e0af1-0a03-4773-8bfa-03ba48804235
  
  
  https://github.com/user-attachments/assets/83ab0ef5-6791-412d-b260-e7c55e7f890c
  
  ### Clear
  
  
  https://github.com/user-attachments/assets/8970b97c-7866-45dd-a122-dc9c8bdc7ec0
  
  
  https://github.com/user-attachments/assets/4105dc8f-f531-4a77-b193-b914c46d3075
  ```
- [`f1948d5`](https://github.com/ghostty-org/ghostty/commit/f1948d50544c36857047c12e46f10a3a1d41160d) terminal: transfer selection text into string maps ([@jparise](https://github.com/jparise))
  ```text
  Selection strings previously duplicated formatted text when callers
  requested a StringMap, even though the regex-link caller immediately
  freed the returned copy.
  
  Add a dedicated selectionStringMap path that transfers the formatter
  output and pin map directly into the returned map. This removes the
  extra allocation and copy while making ownership explicit.
  ```
- [`9ae02a3`](https://github.com/ghostty-org/ghostty/commit/9ae02a326f62bd88f7f5508cf1807c67e7775cb5) terminal: transfer selection text into string maps ([#13923](https://github.com/ghostty-org/ghostty/issues/13923)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Selection strings previously duplicated formatted text when callers
  requested a `StringMap`, even though the regex-link caller immediately
  freed the returned copy.
  
  Add a dedicated `selectionStringMap` path that transfers the formatter
  output and pin map directly into the returned map. This removes the
  extra allocation and copy while making ownership explicit.
  
  **AI Usage:** GTP 5.6 Sol identified and implemented this opportunity. I
  reviewed and understand it all.
  ```
- [`fc5ac17`](https://github.com/ghostty-org/ghostty/commit/fc5ac17a6886c69de93d645d2a7d8e16cb6ebbeb) i18n: complete Dutch (nl) translation for v1.4 ([#13853](https://github.com/ghostty-org/ghostty/issues/13853)) ([@kjvdven](https://github.com/kjvdven))
  ```text
  Fills the 181 untranslated strings in `po/nl.po`, bringing it to
  252/252. Most of them are the command palette actions from
  `src/input/command.zig`; the rest are the new context menu items, global
  keybind notifications, and config editing strings.
  
  **Style.** Ten of the new command palette strings had already been
  translated by previous translators, and those settle the verb form, so
  the rest follows them: imperative for verb+object action titles (`Split
  Left` → `Splits naar links`, `Close Tab` → `Sluit tabblad`), noun
  phrases left as noun phrases (`New Window` → `Nieuw venster`), no title
  case, informal "je". Descriptions are full imperative sentences. Dialog
  headings keep the noun-first infinitive form of the existing `Change
  Terminal Title` → `Titel van de terminal wijzigen`.
  
  A few translation notes:
  
  - `ANSI Sequences` → `ANSI-reeksen` in titles, `ANSI escape sequences` →
  `ANSI-escapereeksen` in descriptions, mirroring the distinction the
  source makes.
  - `Toggle X` titles use the idiomatic `X aan/uit`; their descriptions
  stay imperative (`Schakel … in of uit.`).
  - `surface` is rendered as `terminal` - the Dutch UI has no equivalent
  concept.
  - `scrollback` → `scrollbuffer`.
  
  **No existing translation was modified.** The diff only touches empty
  `msgstr` lines plus `PO-Revision-Date` and `Last-Translator`.
  
  Checked with `msgfmt -c --statistics` (252 translated, no warnings, no
  fuzzy) and `msgcat` (formatting is idempotent, so no rewrap noise for
  the next translator). No `X-Generator` field added.
  
  ---------
  ```
- [`a436a9e`](https://github.com/ghostty-org/ghostty/commit/a436a9edccee8688ec916f4e7ba223532a5183c4) macos: avoid temporary path component allocation ([@jparise](https://github.com/jparise))
  ```text
  The common directory helper previously allocated a temporary slice to
  prepend the base directory before joining path components. Pass the
  three known components directly to std.fs.path.join, leaving only the
  allocation for the returned path.
  ```
- [`9154efc`](https://github.com/ghostty-org/ghostty/commit/9154efcbd3c03bab3f1407c2ece38694fdbcb7ba) macos: avoid temporary path component allocation ([#13921](https://github.com/ghostty-org/ghostty/issues/13921)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The common directory helper previously allocated a temporary slice to
  prepend the base directory before joining path components. Pass the
  three known components directly to std.fs.path.join, leaving only the
  allocation for the returned path.
  ```

## August 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32310030415), [2](https://github.com/ghostty-org/ghostty/actions/runs/32305536881), [3](https://github.com/ghostty-org/ghostty/actions/runs/32298968455), [4](https://github.com/ghostty-org/ghostty/actions/runs/32273834618), [5](https://github.com/ghostty-org/ghostty/actions/runs/32205120526)  
Summary: 5 runs • 293 commits • 35 authors

### Changes

- [`a9f7f6d`](https://github.com/ghostty-org/ghostty/commit/a9f7f6d212a0af39a9597a3ea815140358d1975e) surface: parse text bindings with stack fallback ([@jparise](https://github.com/jparise))
  ```text
  Text binding actions previously allocated a temporary buffer for every
  escaped string. Use a 256-byte stack fallback allocator so typical
  bindings avoid the transient heap allocation while larger values
  continue to use the existing heap-backed behavior.
  ```
- [`8e8d76b`](https://github.com/ghostty-org/ghostty/commit/8e8d76b634f1b791fd693715fc56d728b4967dab) shell-integration: avoid owning temporary commands ([@jparise](https://github.com/jparise))
  ```text
  Some shell setup functions previously converted their stack-backed
  command builders to owned sentinel slices before duplicating them into
  the result arena. Duplicate the builders' written bytes directly
  instead, avoiding unnecessary ownership transfer and sentinel handling.
  ```
- [`49e503f`](https://github.com/ghostty-org/ghostty/commit/49e503fd40401baf3c13903b5941f67dfdcd07db) surface: parse text bindings with stack fallback ([#13918](https://github.com/ghostty-org/ghostty/issues/13918)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Text binding actions previously allocated a temporary buffer for every
  escaped string. Use a 256-byte stack fallback allocator so typical
  bindings avoid the transient heap allocation while larger values
  continue to use the existing heap-backed behavior.
  ```
- [`50d3ac8`](https://github.com/ghostty-org/ghostty/commit/50d3ac8ed6ad1cbca498f7a4388ab14054a5c3e1) shell-integration: avoid owning temporary commands ([#13919](https://github.com/ghostty-org/ghostty/issues/13919)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Some shell setup functions previously converted their stack-backed
  command builders to owned sentinel slices before duplicating them into
  the result arena. Duplicate the builders' written bytes directly
  instead, avoiding unnecessary ownership transfer and sentinel handling.
  ```
- [`f699069`](https://github.com/ghostty-org/ghostty/commit/f6990690f07fdb0a71e46cd809531ca0f5b86f40) Revert "macOS: hide settings menu icon on macOS 27 ([#13664](https://github.com/ghostty-org/ghostty/issues/13664))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 99c483f477dcf3d6523a976772dcac71ab9466d3, reversing
  changes made to 33bdeed1cbc69196c10466d0c9d881c0a7a7ac9c.
  ```
- [`043abc7`](https://github.com/ghostty-org/ghostty/commit/043abc7b6045fa11c08660337a7a2b7a9533205e) macOS: group settings menu in a separate group ([@bo2themax](https://github.com/bo2themax))
- [`5a8921e`](https://github.com/ghostty-org/ghostty/commit/5a8921ecb5bcb0411825722b2b7010db8eb3f56a) surface: keep clipboard content list on stack ([@jparise](https://github.com/jparise))
  ```text
  Use a two element stack-based buffer for the one or two ClipboardContent
  entries rather than the (arena-based) heap allocator.
  ```
- [`4d646ba`](https://github.com/ghostty-org/ghostty/commit/4d646bae0c6dd28c1e49db1b3e04464417f94b41) macOS: group settings menu in a separate group ([#13906](https://github.com/ghostty-org/ghostty/issues/13906)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Reverted https://github.com/ghostty-org/ghostty/pull/13664 with a
  second thought.**
  
  This keeps the consistency with other first-party apps like Terminal,
  Finder, and Music. It seems that most of the first-party apps show the
  standard icons on macOS 27 for "Settings...", "Find", "AutoFill" and
  etc., but in a separate group.
  
  <img width="1060" height="375" alt="image"
  src="https://github.com/user-attachments/assets/d3017865-a443-4c14-ace9-1c6b5acb3f56"
  />
  
  
  I believe this still follows
  [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Icons).
  ```
- [`a4edca2`](https://github.com/ghostty-org/ghostty/commit/a4edca2a90d6cf89900bb058e71cb6860cec78c5) surface: keep clipboard content list on stack ([#13916](https://github.com/ghostty-org/ghostty/issues/13916)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use a two element stack-based buffer for the one or two ClipboardContent
  entries rather than the (arena-based) heap allocator.
  ```
- [`ece96a1`](https://github.com/ghostty-org/ghostty/commit/ece96a14cf4ff3497505067ec4821a201d2f2b70) i18n: update pt_BR translations ([@guilhermetk](https://github.com/guilhermetk))
- [`8a0a9fa`](https://github.com/ghostty-org/ghostty/commit/8a0a9faf8577c72fa8a287fb72694018a9c80f23) i18n: use "Redefinir" for reset actions in pt_BR ([@guilhermetk](https://github.com/guilhermetk))
  ```text
  The "Reset" menu item and the "Reset Terminal" command palette entry
  were translated as "Reiniciar", which reads as restarting the terminal
  session or process. These actions perform a VT reset that clears
  terminal state without restarting the shell, so "Redefinir" conveys
  the correct meaning and matches the standard pt_BR terminology used
  by other terminal emulators.
  ```
- [`6ab3ef9`](https://github.com/ghostty-org/ghostty/commit/6ab3ef94714f95d8a8f486d645f9056974dcf859) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`123dc0c`](https://github.com/ghostty-org/ghostty/commit/123dc0ccb1e3c7209c94faa9286748bb29a22d52) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`1c34e0d`](https://github.com/ghostty-org/ghostty/commit/1c34e0df8504313223e468020d2415b7e2e5aec7) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`6c29a0a`](https://github.com/ghostty-org/ghostty/commit/6c29a0a28292a75d9c259538193fef994ec6b934) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`d6871cd`](https://github.com/ghostty-org/ghostty/commit/d6871cd924569e5149e18fc6545957e087cd4f7c) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`6fe197d`](https://github.com/ghostty-org/ghostty/commit/6fe197d86ade436f7bbab5d57fdf9893e7eb5e31) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`1225632`](https://github.com/ghostty-org/ghostty/commit/1225632d1c9dc90eb04efd62bd5ec0958a151e27) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`31a10a7`](https://github.com/ghostty-org/ghostty/commit/31a10a7b5172c9233243ca81608cde53a21e705b) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`1b8da6b`](https://github.com/ghostty-org/ghostty/commit/1b8da6b40fd1c67d5d60a02c62b00d86b18ab072) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`58c4796`](https://github.com/ghostty-org/ghostty/commit/58c4796c1c9876995dbc02d91be084df6c2cdea5) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`0149ef5`](https://github.com/ghostty-org/ghostty/commit/0149ef5f72f5aaafd0382fad09f1618c509ffa20) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`17a6627`](https://github.com/ghostty-org/ghostty/commit/17a66279be132cb35b790f6610514ed1a31d6163) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`be892fc`](https://github.com/ghostty-org/ghostty/commit/be892fc6c1aab84b31223ce8a23385e739c59520) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`cdefb68`](https://github.com/ghostty-org/ghostty/commit/cdefb6809a7184f0910861ac57a4ee218e433e03) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`ed13a09`](https://github.com/ghostty-org/ghostty/commit/ed13a09a59dde5ff2695c4a84aad49050c839711) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`e493926`](https://github.com/ghostty-org/ghostty/commit/e49392671390ec9e87f75668608e355122605e27) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`e820ef4`](https://github.com/ghostty-org/ghostty/commit/e820ef48b2b10b7ed44199e24396f1d3b7e456d2) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`03cb485`](https://github.com/ghostty-org/ghostty/commit/03cb485f60d93243bacfdfe51c512c03f1bb9c32) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`3bdbad7`](https://github.com/ghostty-org/ghostty/commit/3bdbad7d8869afb6b95e7997a1a4703e8a71acb3) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`132f154`](https://github.com/ghostty-org/ghostty/commit/132f154e5f419bd719ef77a3c9cf050e7d2f2741) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`bde2047`](https://github.com/ghostty-org/ghostty/commit/bde2047a636dd602a15b034fdefb7b9b61f5b2c2) Apply suggestions from code review ([@guilhermetk](https://github.com/guilhermetk))
- [`d2f08cb`](https://github.com/ghostty-org/ghostty/commit/d2f08cb0b12bf81ac4029a5181bf3dea2ea0f0bd) Apply suggestions from code review ([@guilhermetk](https://github.com/guilhermetk))
- [`ae7080e`](https://github.com/ghostty-org/ghostty/commit/ae7080e6cc00fa7a1107ef57974945b8b18a23e4) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`6562166`](https://github.com/ghostty-org/ghostty/commit/65621664eda30796a5d2fbc04b09e9b01825ef39) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`9581f7d`](https://github.com/ghostty-org/ghostty/commit/9581f7dd456f684d6f41c3b4e58f4621262ff725) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`4302020`](https://github.com/ghostty-org/ghostty/commit/4302020990ad25cfc8294b5fb33b2ca0a4b5310d) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`5a55a34`](https://github.com/ghostty-org/ghostty/commit/5a55a345aa5247d4e67be431f9a920f5fa67399e) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`e8a7097`](https://github.com/ghostty-org/ghostty/commit/e8a7097f65bda1e6bb7a78cee1a67d8f8c9d376f) i18: use "aplicativo" instead of "aplicação" for "application" ([@guilhermetk](https://github.com/guilhermetk))
- [`959c0da`](https://github.com/ghostty-org/ghostty/commit/959c0daeaa1abbe9fd03a0da0601e4cd6e360799) i18n: update revision date ([@guilhermetk](https://github.com/guilhermetk))
- [`3e7230b`](https://github.com/ghostty-org/ghostty/commit/3e7230bf5d0e12d018b850ed3856daa848bfebb7) i18n: update pt_BR translations ([#13819](https://github.com/ghostty-org/ghostty/issues/13819)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update all missing Portuguese/BR translations for 1.4.
  
  Part of https://github.com/ghostty-org/ghostty/issues/13766
  ```
- [`f4f9991`](https://github.com/ghostty-org/ghostty/commit/f4f9991d2c188b7c1f364ed9e44b92dd3356bb2a) chore(vt): expose snapshot api ([@neurosnap](https://github.com/neurosnap))
- [`d9ffbbf`](https://github.com/ghostty-org/ghostty/commit/d9ffbbf17c11f570897a49d4c722130e8698d93b) chore(vt): expose snapshot api ([#13912](https://github.com/ghostty-org/ghostty/issues/13912)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Link:
  https://discord.com/channels/1005603569187160125/1420009803173859449/1539649787748417667
  ```
- [`2dc0883`](https://github.com/ghostty-org/ghostty/commit/2dc08839b1a1a331d9ba71ca097c5f8db2965182) build: fix Linux Android SDK fallback path ([#13705](https://github.com/ghostty-org/ghostty/issues/13705)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use the standard `~/Android/Sdk` capitalization for the Linux SDK
  fallback.
  
  This lets NDK discovery work when neither `ANDROID_NDK_HOME` nor an
  `SDK` environment variable is set.
  ```
- [`9d8fbd1`](https://github.com/ghostty-org/ghostty/commit/9d8fbd15b3b4e385b82c1a9e31cdbb99a74dabd6) gtk: add +new-tab action ([#11762](https://github.com/ghostty-org/ghostty/issues/11762)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR adds a `+new-tab` CLI action, useful for automation on GTK. This
  mainly re-uses machinery added for the `+new-window`, but adds in a
  unique surface ID for identifying surfaces for IPC purposes (and
  eliminates use of raw pointers for callbacks from notifications).
  ```
- [`0aa71d0`](https://github.com/ghostty-org/ghostty/commit/0aa71d02ed068a3a036721ab9e480cbdf82ac329) terminal: reduce Parser.Action log formatting code size ([@mitchellh](https://github.com/mitchellh))
  ```text
  Shrinks libghostty-vt dylib by ~2%.
  ```
- [`f368543`](https://github.com/ghostty-org/ghostty/commit/f36854345e50fe382f37a6ef5859f9013787a23b) libghostty: skip stack traces in release panic handlers ([@mitchellh](https://github.com/mitchellh))
  ```text
  The default Zig panic handler unwinds the stack and symbolicates it,
  which drags in ~160KB worth of helper machinery. For an embedded library
  this isn't great because the embedder's environment should be providing
  this as long as libghostty is compiled with symbols or has a way to
  symbolize.
  
  Change ReleaseFast/ReleaseSmall libghostty-vt builds to use a custom
  panic handler. Debug/ReleaseSafe keep the full Zig handlers.
  
  This shrinks libghostty-vt on macOS by ~160KB (~9%).
  ```
- [`579db41`](https://github.com/ghostty-org/ghostty/commit/579db418934a5990296b7fd65d1b6b586b46dfc6) libghostty: log to stderr with raw writes, not lockStderr ([@mitchellh](https://github.com/mitchellh))
  ```text
  see the prior commit, but most importantly this makes it so we can
  replace our IO impl from Threaded.
  ```
- [`82df79e`](https://github.com/ghostty-org/ghostty/commit/82df79ec8d2c61f3beb3ecfc543ed32cb4aba450) libghostty: replace Io.Threaded with custom Io impl (TinyIo) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new Io implementation `TinyIo` that only supports the operations
  we need and doesn't support concurrency. This shrinks the binary size
  of libghostty by anywhere from ~100KB (macOS) to ~200KB (Linux) and
  runtime memory requirements by over 256KB (the thread-local storage
  `std.Io.Threaded` creates plus the 18KB threaded structure is gone).
  
  `TinyIo` is POSIX-only: Windows keeps std.Io.Threaded, and on
  freestanding targets (wasm) TinyIo degrades to std.Io.failing
  behavior just like before.
  
  It is also exported from the Zig module as `ghostty.TinyIo` so
  Zig embedders can opt into the same size win when constructing
  terminals.
  ```
- [`d524a0f`](https://github.com/ghostty-org/ghostty/commit/d524a0fe645cfd4d9ae27bd8451b934dcf2ebaef) libghostty: guard release builds against std debug Io ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release libghostty-vt builds carefully avoid referencing
  std.Options.debug_io because its default implementation is
  std.Io.Threaded, and referencing that vtable keeps every operation
  Threaded supports linked into the binary: roughly 110KB of unreachable
  code. Nothing references it today, but any std.debug.print,
  std.debug.lockStderr, or std.log default-handler call added to
  release-reachable code would silently reintroduce all of it.
  
  Declare std_options_debug_io in the root module so std uses our value
  instead of constructing the Threaded default. Development builds
  (Debug, ReleaseSafe, tests) forward the std default so std.debug.print
  and friends work normally. ReleaseFast and ReleaseSmall builds declare
  it as a @compileError: since std only analyzes the declaration lazily,
  at the moment something references a debug Io code path, the error
  fires exactly at the offending reference, turning a silent size
  regression into a build failure with a message explaining the
  alternatives.
  
  Release binaries are byte-identical when the guard is not tripped.
  ```
- [`a15ddda`](https://github.com/ghostty-org/ghostty/commit/a15dddae2a497e6540feca5c6adc7e86edd59adb) TinyIo: fix failing tests in CI ([@mitchellh](https://github.com/mitchellh))
- [`49e4df7`](https://github.com/ghostty-org/ghostty/commit/49e4df78333ccdeb262e59d0f3c4de9d4b0bc7fd) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([@bo2themax](https://github.com/bo2themax))
- [`fea378e`](https://github.com/ghostty-org/ghostty/commit/fea378e565c8ddb7f49808c4f2e36a4a932e35ff) libghostty: reduce binary size ~16% (macOS), ~22% (Linux) ([#13715](https://github.com/ghostty-org/ghostty/issues/13715)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This shrinks the binary size of libghostty-vt by **16% on aarch64 macOS
  and 22% on x86_64 Linux**. It also shrinks the in-memory footprint by
  ~256KB per thread + ~20KB per app. All benchmarks remain the same, no
  speedups or slowdowns.
  
  Each commit message explains an individual tactic used, but to
  summarize:
  
  1. **No stack traces in release panic handlers (~160KB).** This requires
  the Zig stack unwind and symbolication logic. I don't think this makes
  sense in an embedded library because the embedder should handle this.
  
  2. **An alternate `std.Io` implementation called `TinyIo` (~100KB to
  200KB).** See later... since this is the big one.
  
  3. **Disable recursive Parser.Action logging (~35KB).** We now only log
  the top-level fields of a Parser.Action, which lowers the amount of
  `std.fmt` codegen significantly.
  
  All sizes above are aarch64 macOS and x86_64 Linux ReleaseFast
  libghostty builds.
  
  ## TinyIo
  
  I think the main complexity introduction here is our alternate `std.Io`
  implementation `TinyIo`. This is an IO implementation that implements IO
  operations we need through direct syscalls and does not support
  concurrency or any other options like network, progress, etc.
  
  Why? Because of the way `std.Io` works through vtable dispatch, the
  linker and dead code removal can't prune ANY of the function pointers.
  So our binary has full implementations of all the networking,
  concurrency, etc. related code even though we don't use it.
  
  This has a runtime effect too: even though we put `std.Io.Threaded` in
  single-threaded mode, it still allocates ~256KB of TLS _per thread_, and
  its raw struct state is ~18KB (versus 80 _bytes_ for `TinyIo`).
  
  For future maintenance: I exhaustively implemented the vtable rather
  than use the failing vtable from Zig stdlib so any Zig changes to add
  new fields to this error so we can determine if we want to support it or
  not.
  ```
- [`c285d3c`](https://github.com/ghostty-org/ghostty/commit/c285d3c2442f314b9b9221bc95d02108c61d8d0f) build(deps): bump dorny/paths-filter from 4.0.2 to 4.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 4.0.2 to 4.0.3.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/7b450fff21473bca461d4b92ce414b9d0420d706...ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`bb876a0`](https://github.com/ghostty-org/ghostty/commit/bb876a0d286b661089b7f40dd3a6488d629beffe) build(deps): bump dorny/paths-filter from 4.0.2 to 4.0.3 ([#13718](https://github.com/ghostty-org/ghostty/issues/13718)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  4.0.2 to 4.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/releases">dorny/paths-filter's
  releases</a>.</em></p>
  <blockquote>
  <h2>v4.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update Outputs in readme to account for the 'every'
  predicate-quantifier by <a
  href="https://github.com/hintron"><code>@​hintron</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">dorny/paths-filter#247</a></li>
  <li>fix: scope base-ignored warning to API path by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/319">dorny/paths-filter#319</a></li>
  <li>docs: add contents permission to PR example by <a
  href="https://github.com/134130"><code>@​134130</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">dorny/paths-filter#248</a></li>
  <li>feat: add 'some-with-excludes' predicate quantifier by <a
  href="https://github.com/arxeiss"><code>@​arxeiss</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">dorny/paths-filter#322</a></li>
  <li>Document safe handling of file list outputs in workflows by <a
  href="https://github.com/dorny"><code>@​dorny</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/326">dorny/paths-filter#326</a></li>
  </ul>
  <h2>Security</h2>
  <ul>
  <li>Escape multi-line filenames in list-files shell and csv output] by
  <a href="https://github.com/ken-matsui"><code>@​ken-matsui</code></a>
  and <a href="https://github.com/tjswlsgg"><code>@​tjswlsgg</code></a> in
  <a
  href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">https://github.com/advisories/GHSA-7hc6-8hq5-9q2m</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/hintron"><code>@​hintron</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">dorny/paths-filter#247</a></li>
  <li><a href="https://github.com/134130"><code>@​134130</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">dorny/paths-filter#248</a></li>
  <li><a href="https://github.com/arxeiss"><code>@​arxeiss</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">dorny/paths-filter#322</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v4...v4.0.3">https://github.com/dorny/paths-filter/compare/v4...v4.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md">dorny/paths-filter's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v4.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/326">Document
  safe handling of file list outputs in workflows</a></li>
  <li><a href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">Escape
  multi-line filenames in list-files shell and csv output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">Add
  'some-with-excludes' predicate quantifier</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">Add
  contents permission to PR example</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/319">Scope
  base-ignored warning to API path</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">Update
  outputs in readme to account for the 'every'
  predicate-quantifier</a></li>
  </ul>
  <h2>v4.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/317">Work
  around git dubious ownership errors in container jobs</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/303">Use
  rev-parse instead of branch --show-current for older git compat</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/282">Fix
  warning message</a></li>
  </ul>
  <h2>v4.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/255">Support
  merge queue</a></li>
  </ul>
  <h2>v4.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">Update
  action runtime to node24</a></li>
  </ul>
  <h2>v3.0.4</h2>
  <ul>
  <li><a href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">Escape
  multi-line filenames in list-files shell and csv output</a></li>
  </ul>
  <h2>v3.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">Add
  missing predicate-quantifier</a></li>
  </ul>
  <h2>v3.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/224">Add
  config parameter for predicate quantifier</a></li>
  </ul>
  <h2>v3.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/133">Compare
  base and ref when token is empty</a></li>
  </ul>
  <h2>v3.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/210">Update to
  Node.js 20</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/215">Update
  all dependencies</a></li>
  </ul>
  <h2>v2.11.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/167">Update
  @​actions/core to v1.10.0 - Fixes warning about deprecated
  set-output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/168">Document
  need for pull-requests: read permission</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/164">Updating
  to actions/checkout@v3</a></li>
  </ul>
  <h2>v2.11.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/157">Set
  list-files input parameter as not required</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/161">Update
  Node.js</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/162">Fix
  incorrect handling of Unicode characters in exec()</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/163">Use
  Octokit pagination</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/160">Updates
  real world links</a></li>
  </ul>
  <h2>v2.10.2</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d"><code>ceb8a2b</code></a>
  Update CHANGELOG.md for v4.0.3 and v3.0.4 (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/327">#327</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ef09b88f3eacdbec6ce135a7c9a193a6849545c1"><code>ef09b88</code></a>
  Document safe handling of file list outputs in workflows (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/326">#326</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/44adc5b06dc135dba334efce9bf3cf0624512d2d"><code>44adc5b</code></a>
  Merge commit from fork</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/4711b7a31b4aa89103d8c6ffab2e3b8e7b6381c7"><code>4711b7a</code></a>
  feat: add 'some-with-excludes' predicate quantifier (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/322">#322</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/93c889f9e58fca66f35a0c83d8673ac7e88bb70a"><code>93c889f</code></a>
  fix: escape multi-line filenames in list-files shell and csv output</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/b41dfa943b1939b9b646f67753bfe35cf6e4de03"><code>b41dfa9</code></a>
  docs: add contents permission to PR example (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/248">#248</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/9af6e5a9d010d1ae8ec570390b3d793e2b70a402"><code>9af6e5a</code></a>
  fix: scope base-ignored warning to API path (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/319">#319</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/cae9006b65a1a53044b518c68e13e835c54948a7"><code>cae9006</code></a>
  docs: update outputs in readme to account for the 'every'
  predicate-quantifie...</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/7b450fff21473bca461d4b92ce414b9d0420d706...ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=4.0.2&new-version=4.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`a82637b`](https://github.com/ghostty-org/ghostty/commit/a82637b53aa434fa5c8bc8360c58561d7d48a8e1) crash: resolve sentry directories on the init thread ([@mitchellh](https://github.com/mitchellh))
  ```text
  Sentry initialization already ran on a separate thread, but the cache
  and state directory resolution happened on the main thread before
  spawning it. On macOS the cache dir resolution calls NSFileManager
  URLForDirectory:inDomain:appropriateForURL:create:error: which takes
  multiple milliseconds and was the single largest cost in global.init.
  
  All directory resolution now happens on the init thread.
  
    before: 2967us-4018us
    after:    30us-70us (env map snapshot + thread spawn)
  
  global.init total drops from ~3.4-5.0ms to ~0.4-1.0ms.
  ```
- [`3225e9e`](https://github.com/ghostty-org/ghostty/commit/3225e9ebb195b1cc237c7b8d9de3d51c6863cb5e) macos: cache unified logging loggers per scope ([@mitchellh](https://github.com/mitchellh))
  ```text
  The logFn for macOS unified logging created and released an os_log_t
  logger on every single log call. Loggers are now cached per log scope for
  the process lifetime via an atomic pointer (a creation race wastes at most
  one create).
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, the version-info logging block in global.init:
  
    before: 1070us-2629us
    after:   858us-1319us
  ```
- [`afc79b8`](https://github.com/ghostty-org/ghostty/commit/afc79b8ccf4098ba15659578d0fc666c74fb61bd) font: look up Apple Color Emoji by exact name on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Apple Color Emoji fallback font was discovered with the generic
  discovery path, which builds a CTFontCollection and runs system-wide
  font matching. Since we know the exact font we want, we can look it
  up directly with CTFontCreateWithName instead.
  ```
- [`c454a3b`](https://github.com/ghostty-org/ghostty/commit/c454a3bf47cd72945b7f4db3b53f8af332e167c9) font: support warmup threads ([@mitchellh](https://github.com/mitchellh))
  ```text
  The first CoreText font query in a process initializes the system
  font database, which takes multiple milliseconds (~7ms measured in an
  isolated process; 2-4ms observed inside Ghostty startup). This cost
  was previously paid during the first surface's font grid
  initialization, on the critical path to the first window.
  
  App.create can now spawn a background thread that performs the warmup.
  ```
- [`131b293`](https://github.com/ghostty-org/ghostty/commit/131b293dbbf426acf57618bc43bef0a4fe260d12) renderer/metal: warm up the Metal device machinery at app creation ([@mitchellh](https://github.com/mitchellh))
  ```text
  The first Metal device query in a process (MTLCopyAllDevices) takes
  multiple milliseconds; once the framework is warm, subsequent queries
  are effectively free (measured ~15ms cold, ~1us warm in isolation).
  This cost was paid during the first surface's renderer
  initialization, on the critical path to the first window.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, first surface renderer initialization:
  
    GraphicsAPI.init before: 4227us (device query ~3.5ms)
    GraphicsAPI.init after:  ~900us (device query 20-25us)
  ```
- [`de1336f`](https://github.com/ghostty-org/ghostty/commit/de1336faddbdffc8fb4f58af3597d3f031e2b2d9) renderer/metal: warm up command queue and shader pipelines ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extend the Metal portion of the startup warmup thread to also create
  (and discard) a command queue and build (and discard) the shader
  pipelines for both pixel formats we may use (which one is used
  depends on the blending config). The first command queue for a device
  and the first render pipeline state creations pay one-time driver
  setup and shader compilation costs; once warm, the real creations
  during surface initialization hit driver and OS caches.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, first surface renderer initialization:
  
    queue creation:  717us -> 93us
    pipeline builds: 1023us -> 347us
    renderer init total: 2777us -> 1466us
  ```
- [`db6d20d`](https://github.com/ghostty-org/ghostty/commit/db6d20dce1df0614b4903a4c5c5489a384ab8eeb) apprt/embedded: initialize the TIS keymap lazily ([@mitchellh](https://github.com/mitchellh))
  ```text
  The embedded apprt App init created the keyboard layout keymap
  eagerly, which requires talking to the text input system (TIS). The
  first TIS call in a process is slow: 6.6ms measured inside
  ghostty_app_new during app launch (up to ~30ms in a cold process).
  
  The keymap is only used for keyboard layout queries (option-as-alt
  detection, layout change reload), which happen once keyboard events
  are flowing. By then AppKit has already warmed TIS and the call is
  effectively free (~0.2us measured warm). So initialize the keymap
  lazily on first use. If the layout changes before the keymap was ever
  created, reload is a no-op since lazy init picks up the current
  layout.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch:
  
    embedded app init before: ~6.7ms (keymap 6614us)
    embedded app init after:  ~60us (config clone only)
  ```
- [`4b1e02c`](https://github.com/ghostty-org/ghostty/commit/4b1e02c7c3cf6d6a3548a67d88d08d4962ff67ed) macos: do not load the config errors window when there are no errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Measured on macOS (Apple Silicon) during app launch, via a startup
  timeline instrumented across the Swift app and libghostty:
  
    config apply, errors step:      35.5ms -> 0.1ms
    main() -> first frame rendered: ~126ms -> ~93ms
    main() -> window visible:       ~193ms -> ~173ms
  ```
- [`da74563`](https://github.com/ghostty-org/ghostty/commit/da745630bed8689365be0ec9a0cfe283a2ed965d) macos: only check for auto-tabbing when tabbing preference is always ([@mitchellh](https://github.com/mitchellh))
  ```text
  windowDidLoad undoes macOS automatic window tabbing by inspecting
  window.tabGroup. Accessing tabGroup on a fresh window materializes
  AppKit's tab group machinery, which takes ~15-20ms and is on the
  critical path of every window creation, including the first window at
  app launch.
  
  AppKit only auto-tabs a fresh window when the system tabbing
  preference is "always": the tab bar "+" button goes through
  newWindowForTab which we intercept and route through our own tab
  logic, so it never auto-tabs. Guard the check on
  NSWindow.userTabbingPreference == .always so everyone else skips the
  tab group materialization entirely.
  
  Measured on macOS (Apple Silicon) during app launch via the startup
  timeline instrumentation:
  
    windowDidLoad tab group check: 17.8ms -> ~0ms
    main() -> window visible: median ~173ms -> ~165ms (n=7)
  ```
- [`931a538`](https://github.com/ghostty-org/ghostty/commit/931a538a3992c0f33c6647360bd15ff54f0f7a87) comments ([@mitchellh](https://github.com/mitchellh))
- [`ad08f3b`](https://github.com/ghostty-org/ghostty/commit/ad08f3b0378b119c584aa54980fc5f7fb18b45bb) macos: reduce app launch time ~15%, time to first frame ~27% ([#13722](https://github.com/ghostty-org/ghostty/issues/13722)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Startup optimizations for macOS! Highlights:
  
   * Process exec to visible window: **15% reduction, ~193ms to ~165ms.**
   * Time to first rendered frame: **27% reduction, ~126ms to ~92ms.**
  * Zig startup time goes from **20ms to ~5ms**, the remainder is
  AppKit/Swift stuff.
  
  > [!NOTE]
  >
  > "Time to first rendered frame?" I measured the time between global
  init start to the first Metal callback saying that a frame was
  completed/drawn. This is faster than when it is _presented_ because we
  can create an IOSurfaceLayer and draw to it before AppKit finishes its
  startup and shows the window. But, the good news is this means that when
  the window is shown, the frame is already drawn!
  
  See individual commits for speeds, but a summary below:
  
  1. **Resolve Sentry directories on the init thread, not startup thread
  (~3-4ms).** Sentry init already ran on a thread, but directory
  resolution happened on the main thread first, and on macOS that calls
  `NSFileManager URLForDirectory:` which is slow as shit.
  
  2. **Initialize the TIS keymap lazily (~7ms).** The keymap is only
  needed once keyboard events flow. If AppKit isn't warmed up, this is
  SLOW. Defer setup until its needed.
  
  3. **Warm up the font registry and Metal on background threads (~7ms+
  off the first surface).** The first CoreText query initializes the
  system font database (~7ms) and the first Metal device/queue/pipeline
  use pays framework init and shader compilation costs. `App.create` now
  spawns a detached warmup thread per subsystem so this overlaps config
  load, AppKit launch, and window creation. First font grid init went from
  ~4.5ms to ~1.1ms, renderer init from ~6.8ms to ~1.5ms.
  
  4. **Look up Apple Color Emoji by exact name.** We know exactly which
  font we want, so skip the system-wide `CTFontCollection` matching
  (~312us to ~13us).
  
  5. **Cache unified logging loggers per scope.** We created and released
  an `os_log_t` on every log call. I actually had a comment saying this is
  slow but probably won't matter. Well, we log a lot on startup, and this
  actually mattered.
  
  ## Warmup Threads
  
  As a note, some of the biggest speedups are by using "warmup" threads.
  These are one-time launched threads on system start that basically just
  "touch" the relevant frameworks (CoreText/Metal). The initial touching
  of these frameworks has a ton of cost associated with them (and they're
  thread-safe), so we can shave off a bunch of time by just touching them
  in the background.
  
  This sets up a race between our own startup needing it and these warmup
  threads, but in every case I measured, the warmup threads win.
  
  ## Linux
  
  All the optimizations here focused really on slow macOS APIs. I plan on
  measuring on Linux, but nothing here should slow it down.
  
  **AI usage:** Fable was used for this one to find the issues, help
  perform the measurements, and draft commit messages by splitting up my
  work. I wrote the code, then edited the commit messages. This PR message
  is fully hand-written.
  ```
- [`b8222f4`](https://github.com/ghostty-org/ghostty/commit/b8222f4a8403765050cca52c537ddd7638725457) terminal/kitty: clear placements on image retransmit ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13719
  
  The Kitty graphics protocol requires retransmitting data for a
  specific image ID to delete the previous image and all of its
  placements.
  
  Ghostty instead preserved the placement count and map when replacing image
  data. Repeated `a=T` commands therefore added one anonymous placement per
  frame and retained its tracked pin.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/#display-images-on-screen
  ```
- [`156bc8c`](https://github.com/ghostty-org/ghostty/commit/156bc8c814292349981f3adbfb1120c3d4f02020) terminal/kitty: clear placements on image retransmit ([#13723](https://github.com/ghostty-org/ghostty/issues/13723)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13719
  
  The Kitty graphics protocol requires retransmitting data for a specific
  image ID to delete the previous image and all of its placements.
  
  Ghostty instead preserved the placement count and map when replacing
  image data. Repeated `a=T` commands therefore added one anonymous
  placement per frame and retained its tracked pin.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#display-images-on-screen
  ```
- [`d6248a3`](https://github.com/ghostty-org/ghostty/commit/d6248a32dd724e1cd9c7f9b68c9360f3ad630d47) ghostty.h: mark as internal ([@pluiedev](https://github.com/pluiedev))
  ```text
  Its moniker has been `libghostty-internal` for *quite* a while now among
  maintainers but that has never really been clarified for the public aside
  from a couple comments on discussions. Judging by how many people still
  try to vibe their way into making this work for their purposes, I think
  we should clear this up once and for all.
  ```
- [`7e463bc`](https://github.com/ghostty-org/ghostty/commit/7e463bc65d430e8a8f0aa786abf83601cf2b9598) ghostty.h: mark as internal ([#13724](https://github.com/ghostty-org/ghostty/issues/13724)) ([@bo2themax](https://github.com/bo2themax))
- [`4b9d589`](https://github.com/ghostty-org/ghostty/commit/4b9d589bcb234b3fdd2160a3abf02cf9b647f328) macOS: disable text selection on macOS 15 ([@bo2themax](https://github.com/bo2themax))
- [`0c8ec22`](https://github.com/ghostty-org/ghostty/commit/0c8ec225b5a998792ddcbf626687cd3a28ec4523) macOS: remove unused menu validations ([@bo2themax](https://github.com/bo2themax))
- [`fd47b15`](https://github.com/ghostty-org/ghostty/commit/fd47b15cd4dad1152e17d13b8f79a0f1183c61f2) gtk: free hotkeys memory on app teardown ([@dkinzler](https://github.com/dkinzler))
  ```text
  Free array list memory in Hotkeys.deinit to avoid DebugAllocator
  throwing an error about leaked memory.
  ```
- [`1dbc8ca`](https://github.com/ghostty-org/ghostty/commit/1dbc8ca30c8ce929019c8a4d971113fc79cd4d58) apprt/gtk: add WeakRef.deinit and use it at teardown sites ([@hakonhagland](https://github.com/hakonhagland))
  ```text
  A GWeakRef must be released before the memory holding it is freed: the
  target keeps a pointer to the GWeakRef so it can clear it at finalize,
  and if that memory is gone by then the target walks into whatever now
  occupies it. inspector_window.zig already carries this warning, and
  every call site follows it — but the rule lives in a comment in one
  file, while the type itself offers only set and get, so releasing one
  looks like an ordinary assignment.
  
  Give it a name. deinit forwards to g_weak_ref_clear, which is the call
  GLib documents for a GWeakRef that is going away, and the dispose-time
  clears now use it. set(null) still works and is unchanged; the clear in
  handleReloadConfig stays a set(null) because the object is still alive
  there and the reference is reused.
  
  Zig has no destructors so this enforces nothing. It puts the
  requirement on the type someone is already looking at.
  ```
- [`0a183c9`](https://github.com/ghostty-org/ghostty/commit/0a183c923bfc6150e710121f481e3d03464f1b60) core/gtk: allow editing Ghostty config in a Ghostty window ([@jcollie](https://github.com/jcollie))
  ```text
  This PR extends the `open_config` keybind action to allow editing the
  Ghostty config in a new Ghostty window using the editor configured in
  `$EDITOR` or `$VISUAL`.
  ```
- [`e53b18a`](https://github.com/ghostty-org/ghostty/commit/e53b18a64726ad0ef0860d1dd77065defca8223f) gtk: free hotkeys memory on app teardown ([#13727](https://github.com/ghostty-org/ghostty/issues/13727)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  In debug builds the DebugAllocator throws an error about leaked memory
  when you close Ghostty, if you have global keybinds in your config with
  a Wayland compositor that supports the vicinae-hotkey protocol. The
  cause is the `Hotkeys.entries` array list never actually being freed.
  Not really a problem because the list should be kept around until app
  teardown anyway, but not getting an error every time would be nice (even
  if you need a somewhat specific setup for this to even happen right
  now).
  
  To fix this free the array list memory in Hotkeys.deinit with
  `ArrayList.clearAndFree`. As the existing comment on `deinit` already
  mentions, we can't use `ArrayList.deinit` because it leaves the list in
  an invalid state and `Hotkeys.clear` might still get called and use it.
  ```
- [`0914c5c`](https://github.com/ghostty-org/ghostty/commit/0914c5c2f1b96cefb2277a2cb871db181fd559da) core/gtk: allow editing Ghostty config in a Ghostty window ([#11905](https://github.com/ghostty-org/ghostty/issues/11905)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR extends the `open_config` keybind action to allow editing the
  Ghostty config in a new Ghostty window using the editor configured in
  `$EDITOR` or `$VISUAL`.
  ```
- [`8b7c57c`](https://github.com/ghostty-org/ghostty/commit/8b7c57c756115e519516698206b54ed80b49d1e7) gtk: add window title renaming ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #10469 for GTK.
  ```
- [`951a03b`](https://github.com/ghostty-org/ghostty/commit/951a03b58bf60e73d2d361ac8848cb9423c8be26) apprt/gtk: add WeakRef.deinit and use it at teardown sites ([#13732](https://github.com/ghostty-org/ghostty/issues/13732)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #13713.
  
  `WeakRef(T)` offers `set` and `get`, so releasing one is spelled
  `set(null)` — indistinguishable from an ordinary assignment. The
  requirement that it *must* happen before the owning memory is freed
  lives in a comment in `class/inspector_window.zig`, which is not where
  somebody using the type is looking.
  
  This adds `deinit`, forwarding to `g_weak_ref_clear` — the call GLib
  documents for a `GWeakRef` that is going away — and switches the
  dispose-time clears to it.
  
  ### What changed
  
  - `weak_ref.zig`: new `deinit`, with the reasoning in its doc comment.
  - `window.zig`, `split_tree.zig`, `application.zig`,
  `command_palette.zig`: the four dispose-time clears now call `deinit`.
  
  `set(null)` is unchanged and still valid. The clear in
  `Application.handleReloadConfig` deliberately stays a `set(null)`: the
  object is alive there and the reference is reused, so it is a logical
  clear rather than teardown — which is the distinction the new name is
  meant to make visible.
  
  ### Why it is worth a method
  
  Zig has no destructors, so this enforces nothing; it is documentation
  that happens to be executable. The concrete case is in #13713: I added a
  `WeakRef(Window)` in a downstream branch, did not clear it, and closing
  a window that had shown that dialog deadlocked the GTK main loop inside
  `weak_ref_data_clear_list` locking freed memory. Every upstream call
  site already gets this right — the point is only to put the rule where
  the next person will see it.
  
  ### Testing
  
  `zig build test` passes. `zig fmt --check` clean. Built and used on
  Linux/GTK; the change is behaviourally identical to what was there,
  since `g_weak_ref_clear` and `g_weak_ref_set(NULL)` both unregister.
  
  ---
  
  **AI disclosure per `AI_POLICY.md`:** I investigated the underlying
  incident with Claude Code and it drafted this change; I reviewed it.
  ```
- [`f0e3be3`](https://github.com/ghostty-org/ghostty/commit/f0e3be3eefe104eeb119562499df45f4762995f9) macOS: support decoding the surrogate pair with UnicodeHexInput ([@bo2themax](https://github.com/bo2themax))
- [`b68eb67`](https://github.com/ghostty-org/ghostty/commit/b68eb67e956b051372910cfe6b453e43121b76e3) config/edit: better handling of existing paths ([@vancluever](https://github.com/vancluever))
  ```text
  This adds some better handling of existing paths when editing
  configuration files:
  
  * If we've found an existing file we just skip any attempts to create
    files/dirs, and just return the path.
  
  * If the path (including file) does not exist, we check to see if the
    directory exists first (possibly following symlinks). Directory
    creation happens normally after this (note that any intermediary
    symlinks in this process will still cause the process to fail, this is
    to prevent infinite loops, as per the comments in
    std.Io.Threaded.dirCreateDirPath).
  ```
- [`d929e6a`](https://github.com/ghostty-org/ghostty/commit/d929e6a34a091dcfd69d45011b96cc70b5575dac) config/edit: better handling of existing paths ([#13736](https://github.com/ghostty-org/ghostty/issues/13736)) ([@jcollie](https://github.com/jcollie))
  ```text
  This adds some better handling of existing paths when editing
  configuration files:
  
  * If we've found an existing file we just skip any attempts to create
  files/dirs, and just return the path.
  
  * If the path (including file) does not exist, we check to see if the
  directory exists first (possibly following symlinks). Directory creation
  happens normally after this (note that any intermediary symlinks in this
  process will still cause the process to fail, this is to prevent
  infinite loops, as per the comments in
  std.Io.Threaded.dirCreateDirPath).
  ```
- [`09557e9`](https://github.com/ghostty-org/ghostty/commit/09557e91dc33907fb151b2791414d2c6153fd2e0) Update VOUCHED list ([#13739](https://github.com/ghostty-org/ghostty/issues/13739)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13738#discussioncomment-17968662)
  from @jcollie.
  
  Vouch: @PRIHLOP
  ```
- [`44f06d4`](https://github.com/ghostty-org/ghostty/commit/44f06d4e4fd098aa4b5627e0c2b2d6e704834117) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([#13717](https://github.com/ghostty-org/ghostty/issues/13717)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `needleSelection` was introduced in #12712 to select all texts when
  syncing pasteboard, the crash happens most on macOS 15 in
  `readPasteboardNeedle`. It seems that `objectWillChange` fires
  differently there, and it's hard to reproduce on macOS 26/27. I think
  guaranteeing from ourside is enough, I believe SwiftUI already as its
  own when updating the binding.
  
  **Confirmed with a simple example on macOS 15, it seems a SwiftUI
  issue🫪. So I changed the minimal macOS version for text selection to
  macOS 26. I don't see an elegant way to fix it.**
  
  <img width="1352" height="849" alt="image"
  src="https://github.com/user-attachments/assets/1dfef3f5-ceaa-41dd-bb91-c23dbc5e4ad3"
  />
  
  
  ```swift
  struct ContentView: View {
      @State private var text = ""
      @State private var selection: TextSelection?
      var body: some View {
          TextField("Search", text: $text, selection: $selection)
      }
  }
  ```
  ````
- [`94d775f`](https://github.com/ghostty-org/ghostty/commit/94d775fefc21f74d9cc85a46b34c4e1d85318fd0) Update VOUCHED list ([#13743](https://github.com/ghostty-org/ghostty/issues/13743)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13742#discussioncomment-17970277)
  from @jcollie.
  
  Vouch: @dave92082
  ```
- [`d695fff`](https://github.com/ghostty-org/ghostty/commit/d695ffff3b268490a73fd241ea94ac8c26e99599) macos: defer OSC52 clipboard read confirmations until focused ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10077
  
  Clipboard read confirmations would immediately show a sheet which
  grabbed focus. This could be used for a bunch of dumb reasons, including
  DoS attacks. But, it also caused focus/sheet loops for programs that did
  OSC52 on focus changes (which was seen via some Neovim configs!).
  
  Now, if a surface is unfocused, we bell the surface and show the confirmation
  request on next focus. If the surface is not focused or another request
  comes in, we cancel the prior one.
  
  This also fixes some memory management issues around clipboard requests
  that were likely small leaks (didn't verify the old bug, but verified
  the new code, and eyeballed the old).
  ```
- [`046b8fc`](https://github.com/ghostty-org/ghostty/commit/046b8fcc2a9afccd238577778752a5f86ef9968a) macos: defer OSC52 clipboard read confirmations until focused ([#13744](https://github.com/ghostty-org/ghostty/issues/13744)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10077
  
  Clipboard read confirmations would immediately show a sheet which
  grabbed focus. This could be used for a bunch of dumb reasons, including
  DoS attacks. But, it also caused focus/sheet loops for programs that did
  OSC52 on focus changes (which was seen via some Neovim configs!).
  
  Now, if a surface is unfocused, we bell the surface and show the
  confirmation request on next focus. If the surface is not focused or
  another request comes in, we cancel the prior one.
  
  This also fixes some memory management issues around clipboard requests
  that were likely small leaks (didn't verify the old bug, but verified
  the new code, and eyeballed the old).
  
  To implement this, I decided to reorient the whole clipboard
  confirmation thing around state on SurfaceView (which simplifies memory
  management) and using Combine on BaseTerminalController to get notified.
  ```
- [`426386b`](https://github.com/ghostty-org/ghostty/commit/426386b8579d5e558aa5d4cfdfb003ad06bc4fc5) Update VOUCHED list ([#13747](https://github.com/ghostty-org/ghostty/issues/13747)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13746#discussioncomment-17977627)
  from @jcollie.
  
  Vouch: @alex19EP
  ```
- [`90154e2`](https://github.com/ghostty-org/ghostty/commit/90154e28957ae2257993a30284cce9337c3060e6) macos: ignore -e arguments as open files ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13319
  
  AppKit treats existing positional arguments as documents, causing paths
  passed to a child command after -e to open an extra terminal surface.
  
  We now process args ourselves during openFile callbacks to ignore
  file paths after `-e`. There isn't a way to avoid this I can find
  because AppKit processes argc/argv from the main entrypoint and that
  can't be overridden.
  ```
- [`a858bd4`](https://github.com/ghostty-org/ghostty/commit/a858bd4d35f4cbab142b0fd68d7179cc99de4f4a) macos: ignore -e arguments as open files ([#13748](https://github.com/ghostty-org/ghostty/issues/13748)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13319
  
  AppKit treats existing positional arguments as documents, causing paths
  passed to a child command after -e to open an extra terminal surface.
  
  We now process args ourselves during openFile callbacks to ignore file
  paths after `-e`. There isn't a way to avoid this I can find because
  AppKit processes argc/argv from the main entrypoint and that can't be
  overridden.
  ```
- [`8c9fd7a`](https://github.com/ghostty-org/ghostty/commit/8c9fd7aa79c4d6cc768293fa6e3726162d00c618) macos: normalize command paths as file URLs ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13319
  #13748
  
  Normalize command-line file arguments as file URLs internally while
  keeping the AppKit and FileManager string boundaries unchanged.
  
  This handles relative paths, URL-sensitive characters, and trailing
  directory separators consistently when matching duplicate open-file
  events.
  ```
- [`f719af0`](https://github.com/ghostty-org/ghostty/commit/f719af00c2f44ca7473219abb29dfd5fbb0fcc85) terminal/kitty: use fixed table for control keys ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Graphics commands prev. stored parsed control fields in a hash map
  backed that used an arena.
  This added hashing and allocation to every command even though protocol
  keys are single ASCII letters.
  
  Store letter keys in a fixed array with a presence bitmap and remove the
  now-unnecessary arena. Unknown non-letter keys remain ignored and are
  covered by a regression test.
  ```
- [`5ce1fe1`](https://github.com/ghostty-org/ghostty/commit/5ce1fe1ff9d5a1069604e1cae599c2f283ec12aa) terminal/kitty: document the experiment variants that were considered ([@Uzaaft](https://github.com/Uzaaft))
- [`04d1939`](https://github.com/ghostty-org/ghostty/commit/04d1939d5f3d0120ed9a4754146883f848e65d43) issue-triage: add a documentation search checkbox ([@trag1c](https://github.com/trag1c))
- [`92cdfc7`](https://github.com/ghostty-org/ghostty/commit/92cdfc748ec42045bc23bff6c8d887de2872ccb3) issue-triage: add a documentation search checkbox ([#13752](https://github.com/ghostty-org/ghostty/issues/13752)) ([@mitchellh](https://github.com/mitchellh))
- [`8e4715b`](https://github.com/ghostty-org/ghostty/commit/8e4715b6ea65c7f5b3e476c81d111a35053d8d4a) terminal/kitty: use fixed table for control keys ([#13729](https://github.com/ghostty-org/ghostty/issues/13729)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Swap out the hash map backed by an arena with a fixed array.
  Measurements from poop:
  CPU Cycles: 173M → 171M (−1.2%)
  Instructions: 519M → 517M (−0.5%)
  Peak RSS: 11.9 → 11.8 MB
  Cache misses: 356K → 312K (−12.4%)
  ```
- [`d1937d6`](https://github.com/ghostty-org/ghostty/commit/d1937d63e45547515484e9820f9148988783ecfe) macOS: remove unused menu validations ([#13726](https://github.com/ghostty-org/ghostty/issues/13726)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  UpdateController isn't the target of any menu item, we don't need add
  menu validation here.
  ```
- [`b0b9fbc`](https://github.com/ghostty-org/ghostty/commit/b0b9fbc8d5b0faecdd79da2303811b42bd0afc67) macOS: support decoding the surrogate pair with UnicodeHexInput ([#13737](https://github.com/ghostty-org/ghostty/issues/13737)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Not yet a perfect fix for
  https://github.com/ghostty-org/ghostty/discussions/13730
  ```
- [`fad7f85`](https://github.com/ghostty-org/ghostty/commit/fad7f854e8f976968bf4d61d408de9699cf87666) Update VOUCHED list ([#13754](https://github.com/ghostty-org/ghostty/issues/13754)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13753#discussioncomment-17980814)
  from @mitchellh.
  
  Vouch: @shorsher
  ```
- [`9f9b8d1`](https://github.com/ghostty-org/ghostty/commit/9f9b8d1d0525e63106cfc0ea19775056b205ffb5) Update VOUCHED list ([#13756](https://github.com/ghostty-org/ghostty/issues/13756)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13755#discussioncomment-17982722)
  from @jcollie.
  
  Vouch: @figelwump
  ```
- [`3901168`](https://github.com/ghostty-org/ghostty/commit/3901168b161783cd10b8211c08635bcf756a0751) macOS: remove iOS target ([@bo2themax](https://github.com/bo2themax))
- [`400be4c`](https://github.com/ghostty-org/ghostty/commit/400be4cc1d6c1fbec2222c02aedcef7ada4d796f) macOS: adjust file tree ([@bo2themax](https://github.com/bo2themax))
- [`daab08e`](https://github.com/ghostty-org/ghostty/commit/daab08ec0158934e646d37613f805584277a586f) macOS: drop the cross-platform check and abstraction ([@bo2themax](https://github.com/bo2themax))
- [`b112f39`](https://github.com/ghostty-org/ghostty/commit/b112f3954ce703ceb90afe5bb391b9d33321db2b) build: stop building Ghostty for iOS ([@bo2themax](https://github.com/bo2themax))
- [`4f39c50`](https://github.com/ghostty-org/ghostty/commit/4f39c506ef666887eb0ea68ee125fe1036ace31b) macOS: remove iOS target and clean up cross platform checks ([#13759](https://github.com/ghostty-org/ghostty/issues/13759)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  As discussed in Discord: Ghostty internal support for iOS is not
  important and we verify iOS compatibility for `libghostty-vt` through
  compilation.
  
  Diff is **BIG**, but it contains mostly cleanup and didn't touch macOS's
  implementation (except for some renaming).
  
  ### AI Disclosure
  
  Claude did batch removal for me, I manually reviewed them and ran
  locally for macOS.
  ```
- [`7a17189`](https://github.com/ghostty-org/ghostty/commit/7a171895ddf7088b6f24b137c394e080d967d25e) build: stop building Ghostty.xcframework for iOS ([@bo2themax](https://github.com/bo2themax))
- [`396166e`](https://github.com/ghostty-org/ghostty/commit/396166ecbeca91cb9623e993e6049053cead68bc) build: stop building Ghostty.xcframework for iOS ([#13760](https://github.com/ghostty-org/ghostty/issues/13760)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Depends on https://github.com/ghostty-org/ghostty/pull/13759.
  
  **Removing iOS for `Ghostty.xcframework` will affect other
  [awesome-libghostty](https://github.com/Uzaaft/awesome-libghostty)
  projects**, so I separated it.
  
  
  ### AI Disclosure
  
  Claude ran the check and did the changes, I reviewed it.
  ```
- [`a69a591`](https://github.com/ghostty-org/ghostty/commit/a69a591af11370453d707aa9c0b2ec6ff17ce3c3) libghostty: functions to detect and write until stream ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds new functions to both C and Zig to write VT data until the
  VT parser reaches a "ground" state. The ground state is when the
  parser/stream is stateless: between all partial UTF-8, OSC, CSI, etc.
  
  This lets embedders safely interleave custom VT sequences from multiple
  sources. A practical example is a standard terminal reading from a pty
  that is then doing custom APC or something mid-stream for their emulator
  client.
  ```
- [`da8b171`](https://github.com/ghostty-org/ghostty/commit/da8b171265e0f9db09287e62e70e10afa0d44e9c) macOS: fix Sendable warning for UnsafeMutablePointer ([@bo2themax](https://github.com/bo2themax))
  ```text
  Swift explicitly [marked UnsafeMutablePointer as non sendable](https://github.com/swiftlang/swift/commit/0568dbf903bbd7c1278c029d7e4eaaad6a460002). Moving from `@unchecked @retroactive` to `nonisolated(unsafe)` is safe for us as per the previous comments
  ```
- [`97ae257`](https://github.com/ghostty-org/ghostty/commit/97ae257497ae687bca7f9c711e46c6937386480e) macOS: fix warnings in showUserNotification ([@bo2themax](https://github.com/bo2themax))
- [`51ed437`](https://github.com/ghostty-org/ghostty/commit/51ed437cd1a202e625feb7fd0577354d81bcc54b) libghostty: functions to detect and write until stream ground state ([#13761](https://github.com/ghostty-org/ghostty/issues/13761)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds new functions to both C and Zig to write VT data until the VT
  parser reaches a "ground" state. The ground state is when the
  parser/stream is stateless: between all partial UTF-8, OSC, CSI, etc.
  
  This lets embedders safely interleave custom VT sequences from multiple
  sources. A practical example is a standard terminal reading from a pty
  that is then doing custom APC or something mid-stream for their emulator
  client.
  
  The new function is anywhere from 1% to 5% slower than normal VT write,
  but that should be acceptable due to its special case. Normal VT writes
  are unchanged.
  ```
- [`c78226b`](https://github.com/ghostty-org/ghostty/commit/c78226bfaea1e03107d91c4e27c836f9d8143a7b) macOS:  fix Main actor-isolated static property 'find' warnings ([@bo2themax](https://github.com/bo2themax))
- [`cb7eaa0`](https://github.com/ghostty-org/ghostty/commit/cb7eaa059dbc4be7318a6071efc14b4891c628e6) macOS: silent weak ownership difference warnings ([@bo2themax](https://github.com/bo2themax))
  ```text
  UpdateViewModel doesn't own the Task, we don't actually need it here.
  ```
- [`7e3ddc2`](https://github.com/ghostty-org/ghostty/commit/7e3ddc2c891b1076caa235de9681a9b598bc3546) macOS: fix swift warnings ([#13762](https://github.com/ghostty-org/ghostty/issues/13762)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework for #12764
  ```
- [`1eaf457`](https://github.com/ghostty-org/ghostty/commit/1eaf457b184c0fd34f5ff3fb2d0241d04d7515c4) gtk: add window title renaming ([#10999](https://github.com/ghostty-org/ghostty/issues/10999)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes #10469 for GTK.
  ```
- [`e523cf8`](https://github.com/ghostty-org/ghostty/commit/e523cf81040626cf240723443d9106813709e49c) terminal: move cursor home after formatting tabstops ([@mitchellh](https://github.com/mitchellh))
  ```text
  Home the cursor after serializing custom tab stops, since formatting VT
  expects it to be there for new lines.
  ```
- [`99b877a`](https://github.com/ghostty-org/ghostty/commit/99b877ad22a7c9e146d6e4c3ba118e66ea694fb7) terminal: move cursor home after formatting tabstops ([#13763](https://github.com/ghostty-org/ghostty/issues/13763)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Home the cursor after serializing custom tab stops, since formatting VT
  expects it to be there for new lines.
  ```
- [`4a516fa`](https://github.com/ghostty-org/ghostty/commit/4a516fa393932fe263bbca8d30740d17e40484f1) github: remove the issue templates ([@trag1c](https://github.com/trag1c))
- [`d2eeb73`](https://github.com/ghostty-org/ghostty/commit/d2eeb734b0dbf80954d1b630986746a5e9e194fd) github: remove the issue templates ([#13765](https://github.com/ghostty-org/ghostty/issues/13765)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  They're not needed anymore since the "New issue" button is now
  inaccessible to non-maintainers anyway.
  ```
- [`bdb5660`](https://github.com/ghostty-org/ghostty/commit/bdb566068ead29409eb5d410249f02f51d274d3d) Expose semantic prompt state through C APIs ([@figelwump](https://github.com/figelwump))
- [`b104a3f`](https://github.com/ghostty-org/ghostty/commit/b104a3f0b3f7e021df5a773f68d5ff6130a8ce64) i18n - Latvian translation of command palette, typo fixes and more natural translations ([@EriksRemess](https://github.com/EriksRemess))
- [`b3514d5`](https://github.com/ghostty-org/ghostty/commit/b3514d56210e8a57a480fb4d0c82121e86df28e4) i18n: Latvian translation. Additional strings. ([@EriksRemess](https://github.com/EriksRemess))
- [`491806f`](https://github.com/ghostty-org/ghostty/commit/491806fbeb35b9153838085d6cf615cb977546e6) i18n(lv): last two missing translations ([@EriksRemess](https://github.com/EriksRemess))
- [`c80c373`](https://github.com/ghostty-org/ghostty/commit/c80c3736275412a0cf75588fb6b7e73fd9395fcd) Remove internal surface prompt query ([@figelwump](https://github.com/figelwump))
- [`b2fa293`](https://github.com/ghostty-org/ghostty/commit/b2fa2931b6599f7e32a7c547b3f5520ac3333881) Expose semantic prompt state through libghostty-vt ([#13767](https://github.com/ghostty-org/ghostty/issues/13767)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - Add `GHOSTTY_TERMINAL_DATA_CURSOR_AT_PROMPT` to expose semantic prompt
  state through `libghostty-vt`.
  - Reuse `Terminal.cursorIsAtPrompt()` rather than introducing separate
  prompt tracking.
  
  ## Motivation
  
  Ghostty already tracks whether the cursor is at a semantic prompt
  through `Terminal.cursorIsAtPrompt()`. Exposing this query through
  `libghostty-vt` lets downstream terminal consumers use Ghostty's
  existing semantic prompt state without introducing separate tracking.
  
  The query returns false when semantic prompt information is unavailable
  or the alternate screen is active.
  
  Discussed in https://github.com/ghostty-org/ghostty/discussions/13755.
  
  ## Testing
  
  - `zig build test-lib-vt`
  - `zig build test-lib-vt -Dtest-filter="get cursor_at_prompt"`
  - `zig build -Demit-lib-vt`
  
  ## AI disclosure
  
  Codex assisted with adding the `libghostty-vt` query and test,
  addressing review feedback, running validation, and drafting this
  description. I reviewed and edited the final code and description,
  reviewed the validation results, and understand how the change interacts
  with Ghostty's semantic prompt state.
  ```
- [`e2662d7`](https://github.com/ghostty-org/ghostty/commit/e2662d7b63d4aee02f31164c96c180ebed8ddf0b) i18n: translate v1.4 command palette and remaining strings (be) ([@iweuhi2kjrnkw](https://github.com/iweuhi2kjrnkw))
- [`3650bef`](https://github.com/ghostty-org/ghostty/commit/3650bef4ec28512c1402be8ed838b2929f3aa794) Fix +new-window -e <command> inheriting forced shell integration from the running GTK application. ([@PRIHLOP](https://github.com/PRIHLOP))
  ```text
  Arguments after -e are now marked as an explicit command that requires shell detection. That marker is propagated with the existing command override to the new surface for both the current +new-window and +new-tab GTK paths. When the override is applied, forced shell integration becomes detect; an explicit none remains disabled.
  
  This is scoped to the GTK -e path. It does not change the generic forced shell-integration behavior, so configured integration continues to support shell executables with non-standard names.
  
  Fixes #12378.
  ```
- [`c54ec80`](https://github.com/ghostty-org/ghostty/commit/c54ec80c55a045312f7c97d66b32c8043526f03c) gtk: Fix +new-window -e <command> inheriting forced shell integration from the running GTK application. Fixes [#12378](https://github.com/ghostty-org/ghostty/issues/12378). ([#13741](https://github.com/ghostty-org/ghostty/issues/13741)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  Fix `+new-window -e <command>` inheriting forced shell integration from
  the running GTK application.
  
  Arguments after `-e` are now marked as an explicit command that requires
  shell detection. That marker is propagated with the existing command
  override to the new surface for both the current `+new-window` and
  `+new-tab` GTK paths. When the override is applied, forced shell
  integration becomes `detect`; an explicit `none` remains disabled.
  
  This is scoped to the GTK `-e` path. It does not change the generic
  forced shell-integration behavior, so configured integration continues
  to support shell executables with non-standard names.
  
  Fixes #12378.
  
  ## Root cause
  
  The GTK IPC path replaced `config.command` for the new surface but
  retained the running application's `shell-integration` value. `termio`
  therefore treated an arbitrary explicit command such as Vim as the
  forced shell and appended shell-specific arguments.
  
  ## AI usage
  
  I used Hermes Agent (with ChatGPT 5.6) to help inspect the codebase,
  trace the GTK command path, and draft parts of the implementation and
  test. I manually reviewed and edited the changes, validated the behavior
  and test results, and understand the affected code paths.
  ```
- [`d2c70a8`](https://github.com/ghostty-org/ghostty/commit/d2c70a8c7b9b6893c13640c02d7b6f9a1624f3f0) Update VOUCHED list ([#13775](https://github.com/ghostty-org/ghostty/issues/13775)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13773#discussioncomment-17996184)
  from @jcollie.
  
  Vouch: @steven-tk
  ```
- [`004f79e`](https://github.com/ghostty-org/ghostty/commit/004f79e2737a6b4c10bcff856680802061b00aa1) Merge branch 'ghostty-org:main' into localization-da ([@carlvillads](https://github.com/carlvillads))
- [`1d9fcdc`](https://github.com/ghostty-org/ghostty/commit/1d9fcdc151aedc72db1678e6e1df3425ed94939b) i18n: complete Kazakh (kk) translation for v1.4 ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
  ```text
  Translates the 180 remaining strings, mainly command palette entries
  introduced for v1.4 localization.
  ```
- [`98b828a`](https://github.com/ghostty-org/ghostty/commit/98b828a0232e411eb1e39b83de22fa3869faa51a) config: flush autogenerated config template ([@steven-tk](https://github.com/steven-tk))
  ```text
  #13774
  
  Flush the buffered writer after writing the template so newly created
  configuration files contain the expected guidance instead of being empty.
  ```
- [`4713668`](https://github.com/ghostty-org/ghostty/commit/47136687d725d611a5b9d7fd59a13b1c4e360617) add command palette translations ([@carlvillads](https://github.com/carlvillads))
- [`dab1b10`](https://github.com/ghostty-org/ghostty/commit/dab1b105b932fecf155d2b6a66c79d8311f826ea) config: flush autogenerated config template ([#13780](https://github.com/ghostty-org/ghostty/issues/13780)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #13774
  
  Simple one-line fix: added the missing flush to the function.
  
  - `zig build` passed
  - `zig build test` passed
  - Confirmed template appears after fix in `~/Library/Application
  Support/com.mitchellh.ghostty/config.ghostty`
  
  ---
  **AI Disclosure**
  
  As mentioned before - I used OpenAI Codex (Sol 5.6 high):
  a) to see if the template still exists & a function exists that tries to
  use the template
  b) find the moment in history this behavior changed.
  Additionally:
  c) reviewing my work and draft a commit message matching your preferred
  style
  
  I implemented the change, ran the build/test, manually verified the
  behavior, and understand the fix.
  ```
- [`613050d`](https://github.com/ghostty-org/ghostty/commit/613050ddffbe9e15e538a355e2c6934407113793) i18n - Latvian translation of command palette, typo fixes and more natural translations ([#11663](https://github.com/ghostty-org/ghostty/issues/11663)) ([@00-kat](https://github.com/00-kat))
- [`dd22396`](https://github.com/ghostty-org/ghostty/commit/dd22396bd798d90445e1b365a79da061f96e5dc9) i18n: update es_BO translations for 1.4 ([@MiguelElGallo](https://github.com/MiguelElGallo))
- [`aa25679`](https://github.com/ghostty-org/ghostty/commit/aa25679da8c87b47e9b45410435bded87e283031) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`d7f782d`](https://github.com/ghostty-org/ghostty/commit/d7f782dbcc4471eb697cce0ce888c83787ca38f0) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`7c1d0d4`](https://github.com/ghostty-org/ghostty/commit/7c1d0d414c4bfd976c6ae422f170a4b6249716d5) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
  ```text
  Removed translation for opening config file with default editor.
  ```
- [`7c4c7ad`](https://github.com/ghostty-org/ghostty/commit/7c4c7adadc8b080ab168ed0af48319185dcbd2ba) pkg/wuffs: use C-only mirror of wuffs ([@jcollie](https://github.com/jcollie))
  ```text
  This prevents us from pulling in test images that trigger some anti-virus
  scanners. It's also smaller since it only has the necessary bits that we need.
  
  This also updates to the latest release: 0.4.0-alpha.10.
  ```
- [`9f8550b`](https://github.com/ghostty-org/ghostty/commit/9f8550b7f4e671a4305cb63541bbce9652bce38a) Add danish translations ([#13538](https://github.com/ghostty-org/ghostty/issues/13538)) ([@00-kat](https://github.com/00-kat))
- [`4770375`](https://github.com/ghostty-org/ghostty/commit/47703753ad8f313601689d3eb6087469f5665d16) Update VOUCHED list ([#13793](https://github.com/ghostty-org/ghostty/issues/13793)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13791#discussioncomment-18005730)
  from @jcollie.
  
  Vouch: @dolzenko
  ```
- [`bb019ca`](https://github.com/ghostty-org/ghostty/commit/bb019cac272a953c6338b2ab709d6ae26725c3a5) Update VOUCHED list ([#13794](https://github.com/ghostty-org/ghostty/issues/13794)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13792#discussioncomment-18005749)
  from @jcollie.
  
  Vouch: @dmunozv04
  ```
- [`27d1642`](https://github.com/ghostty-org/ghostty/commit/27d1642879adb0da7a363cbfca67c11a102cbc48) Update Turkish translations ([@bitigchi](https://github.com/bitigchi))
- [`908961f`](https://github.com/ghostty-org/ghostty/commit/908961f8a95573096ab231654cccc97170da8086) terminal: size dynamic tabstops by bits ([#13600](https://github.com/ghostty-org/ghostty/issues/13600)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Dynamic tabstop storage treated the number of columns above the inline
  capacity as a byte count even though each byte stores eight stops. This
  was wasteful, although in practice this is in the order of just bytes.
  
  Round the extra column count up to whole storage units and grow the
  existing slice with realloc, preserve existing stops.
  ```
- [`43fe699`](https://github.com/ghostty-org/ghostty/commit/43fe699071c7dceb161dc3b0c04fce46ade36174) Update VOUCHED list ([#13797](https://github.com/ghostty-org/ghostty/issues/13797)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13796#discussioncomment-18006390)
  from @jcollie.
  
  Vouch: @sghng
  ```
- [`8fd2013`](https://github.com/ghostty-org/ghostty/commit/8fd2013a09c9105507a98360318ec7f5e802d50b) i18n: add missing Polish translations + minor fixes ([@trag1c](https://github.com/trag1c))
- [`987ee52`](https://github.com/ghostty-org/ghostty/commit/987ee52751a7d87a7bee996cd2e249a01be2571b) Update and (hopefully) complete Hungarian translations in hu.po ([@balazs-szucs](https://github.com/balazs-szucs))
- [`bedb6f2`](https://github.com/ghostty-org/ghostty/commit/bedb6f2ff9d2c65456a7b1e98a5a04a702b77f27) i18n: update es_BO translations for 1.4 ([#13782](https://github.com/ghostty-org/ghostty/issues/13782)) ([@trag1c](https://github.com/trag1c))
  ```text
  issue #13766
  ```
- [`51992ab`](https://github.com/ghostty-org/ghostty/commit/51992ab01ad7e6dfeced16615080b68f620bb122) libghostty: make device and point headers self-contained ([@mitchellh](https://github.com/mitchellh))
- [`e4ec4f0`](https://github.com/ghostty-org/ghostty/commit/e4ec4f0f95f44b131c256127d26c67258104be5a) libghostty: fix enum underlying type detection ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use fixed int enum types for C++11, C23, Clang's fixed-enum extension,
  and GCC 13 or newer. Previously only finalized C23 mode selected an explicit
  underlying type, leaving C++ and common older C modes with
  implementation-defined enum types.
  ```
- [`309440e`](https://github.com/ghostty-org/ghostty/commit/309440e07f3ff097fb4b11ab8cc92b01e29625e8) libghostty: include all public structs in type JSON ([@mitchellh](https://github.com/mitchellh))
- [`d930c74`](https://github.com/ghostty-org/ghostty/commit/d930c74c4d8211d551d0cb99054f13338113f4f9) libghostty: make sized initialization valid C++ ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use an immediately invoked lambda for GHOSTTY_INIT_SIZED in C++ so the
  macro value-initializes every field before setting the ABI size. The
  previous C compound literal and designated initializer required compiler
  extensions in C++17 and C++20.
  
  Keep the existing standard compound literal for C callers.
  ```
- [`250a36f`](https://github.com/ghostty-org/ghostty/commit/250a36fe6f55de3d2a910deb420f35b0cf6dc350) i18n: Update es_ES translations ([@alosarjos](https://github.com/alosarjos))
  ```text
  Update the translations for the next 1.4 release
  ```
- [`119f4fd`](https://github.com/ghostty-org/ghostty/commit/119f4fd6063cb695d1179c5ab1b362c4d71f23d0) libghostty: minor C/C++ compatibility fixes ([#13801](https://github.com/ghostty-org/ghostty/issues/13801)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Minor things as I was just auditing the state of our headers:
  
  * Make sure all subheaders like `point.h` can be included standalone
  * Support Clang/GCC extensions for typed enums if we can detect it
  * Add missing structs to the `ghostty_type_json` function
  * Fix `GHOSTTY_INIT_SIZED` for C++ mode
  ```
- [`226a916`](https://github.com/ghostty-org/ghostty/commit/226a91658da6400140a7da3f38b825ba0395bd5d) Update Turkish translations ([#13770](https://github.com/ghostty-org/ghostty/issues/13770)) ([@00-kat](https://github.com/00-kat))
- [`0ee8a72`](https://github.com/ghostty-org/ghostty/commit/0ee8a72970734717394c1e9e988e365b650ea415) i18n: add missing Polish translations + minor fixes ([#13798](https://github.com/ghostty-org/ghostty/issues/13798)) ([@00-kat](https://github.com/00-kat))
- [`710b872`](https://github.com/ghostty-org/ghostty/commit/710b8723905533d623c5e64ba0c5e6662fe79713) Update VOUCHED list ([#13805](https://github.com/ghostty-org/ghostty/issues/13805)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13804#discussioncomment-18010199)
  from @jcollie.
  
  Vouch: @pssalman
  ```
- [`365e0bd`](https://github.com/ghostty-org/ghostty/commit/365e0bd0083f3d51a7b7242ad8c5a025c7848c75) i18n: Updating `es_AR` for 1.4 ([#13784](https://github.com/ghostty-org/ghostty/issues/13784)) ([@alanmoyano](https://github.com/alanmoyano))
  ```text
  This PR also updates old translations to keep better consistency.
  
  AI Disclaimer: I translated manually all strings and then used an agent
  to review consistency and legibility and applied many suggestions.
  ```
- [`89a26a3`](https://github.com/ghostty-org/ghostty/commit/89a26a39eb01a7cf34a64f9329da8304bebd4d8e) Update VOUCHED list ([#13808](https://github.com/ghostty-org/ghostty/issues/13808)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12664#discussioncomment-18012616)
  from @pluiedev.
  
  Vouch: @Zlitus
  ```
- [`93e7e7e`](https://github.com/ghostty-org/ghostty/commit/93e7e7e9933a339032a0499043e0f0c6d7218a7a) po/zh_CN: add missing translations ([@pluiedev](https://github.com/pluiedev))
  ```text
  Frankly the number of command palette entries is a bit ridiculous,
  but such is life
  ```
- [`6cadad0`](https://github.com/ghostty-org/ghostty/commit/6cadad06f468745651a6bb53e64d31cc8fae9e24) termio: preserve UTF-8 in desktop notification truncation ([@dolzenko](https://github.com/dolzenko))
- [`034f584`](https://github.com/ghostty-org/ghostty/commit/034f5843f21b7a3c9924d5e42ee34ee784699763) fix: apply kk translation review feedback ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
- [`f2022fe`](https://github.com/ghostty-org/ghostty/commit/f2022fe88d57f1b93913de1087ec4f3e459ef3b7) macOS: avoid holding SurfaceView when sending notifications ([@bo2themax](https://github.com/bo2themax))
- [`485864c`](https://github.com/ghostty-org/ghostty/commit/485864cd609ebc7c0350aacbf0ef8c8a0a767c86) po/zh_CN: add missing translations ([#13608](https://github.com/ghostty-org/ghostty/issues/13608)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Frankly the number of command palette entries is a bit ridiculous, but
  such is life
  ```
- [`fa392ba`](https://github.com/ghostty-org/ghostty/commit/fa392baf28c7343ea8f7b005fe2a3299116ee79b) i18n: add missing Hungarian translations ([#13799](https://github.com/ghostty-org/ghostty/issues/13799)) ([@00-kat](https://github.com/00-kat))
  ```text
  Part of: #13766
  ```
- [`ae6d97e`](https://github.com/ghostty-org/ghostty/commit/ae6d97ea71b8ad4bb0d3837cc807d6ae097d4145) termio: avoid rescanning UTF-8 prefixes ([@dolzenko](https://github.com/dolzenko))
- [`375ce78`](https://github.com/ghostty-org/ghostty/commit/375ce787466f7bd666f5d8b2e32182ade296dcf3) i18n: Update Norwegian translations ([@Uzaaft](https://github.com/Uzaaft))
- [`6584450`](https://github.com/ghostty-org/ghostty/commit/6584450279ae3ccd20c889c091a73b3a52d5ce09) i18n: Update Norwegian translations ([#13781](https://github.com/ghostty-org/ghostty/issues/13781)) ([@trag1c](https://github.com/trag1c))
- [`1ff3deb`](https://github.com/ghostty-org/ghostty/commit/1ff3deb1bbbf960e69edf49eb7b34fa227080b8d) i18n: Update es_ES translations ([#13800](https://github.com/ghostty-org/ghostty/issues/13800)) ([@00-kat](https://github.com/00-kat))
  ```text
  Update the translations for the next 1.4 release
  ```
- [`562f21a`](https://github.com/ghostty-org/ghostty/commit/562f21a6e72ce1710ca859b25b1562f7f7b0f76a) macOS: avoid holding SurfaceView when sending notifications ([#13810](https://github.com/ghostty-org/ghostty/issues/13810)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We shouldn't hold a closing surface view when sending notifications and
  waiting to dismiss that notification. This happens rarely, but it's the
  right thing to do.
  
  ### AI Disclosure
  Found by Claude when judging other branches, I applied the changes
  myself.
  
  > Forgot that after force pushing, you can't reopen #13787 🫪, linking it
  here for the review history.
  ```
- [`f81dcad`](https://github.com/ghostty-org/ghostty/commit/f81dcadc82ea2afdcf2dc92929037701122f05b5) Update VOUCHED list ([#13814](https://github.com/ghostty-org/ghostty/issues/13814)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13812#discussioncomment-18018163)
  from @mitchellh.
  
  Vouch: @elitex45
  ```
- [`cde7f93`](https://github.com/ghostty-org/ghostty/commit/cde7f93435eb40dfbc306e338c43418e8322220e) renderer: simplify cell row storage ([@jparise](https://github.com/jparise))
  ```text
  Cell contents used our ArrayListCollection container to manage per-row
  foreground lists. This was the only place ArrayListCollection was used.
  
  We now own the row list slice directly, initialize cursor capacity to
  exactly one cell, and reallocate the contiguous background buffer in
  place when possible. Foreground rows still use exact sizes so resizes
  (which are infrequent) do not retain the high-water mark.
  ```
- [`1eceea9`](https://github.com/ghostty-org/ghostty/commit/1eceea92dac457f95858706f946be7d6b21e5885) i18n: Update ko_KR translations ([@dobbylee](https://github.com/dobbylee))
- [`ecbeb60`](https://github.com/ghostty-org/ghostty/commit/ecbeb60ca5327186301900ccef208143ff46ef22) macos: send all insertText commits as key events ([@sghng](https://github.com/sghng))
  ```text
  Previously, insertText commits without marked text were delivered via
  sendText, which applies paste semantics and wraps the text in bracketed
  paste when the program enables it. macOS dictation and other input
  methods often commit without marked text, so programs treated dictated
  text as a paste and applied paste-specific handling.
  
  insertText is only invoked by input methods (IME, dictation, emoji
  picker, character viewer); real paste operations use a separate path.
  Send every non-empty commit through the key event path so programs
  interpret input method text as typed input. Typing is unaffected (the
  accumulator path returns earlier) and Cmd+V pastes are unaffected.
  
  The helper is renamed from committedPreeditTextAction to
  committedTextAction since it no longer only handles preedit commits.
  ```
- [`4a174e1`](https://github.com/ghostty-org/ghostty/commit/4a174e1c89a93853d18e47fd7553801633ba8746) renderer: simplify cell row storage ([#13599](https://github.com/ghostty-org/ghostty/issues/13599)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cell contents used our ArrayListCollection container to manage per-row
  foreground lists. This was the only place ArrayListCollection was used.
  
  We now own the row list slice directly, initialize cursor capacity to
  exactly one cell, and reallocate the contiguous background buffer in
  place when possible. Foreground rows still use exact sizes so resizes
  (which are infrequent) do not retain the high-water mark.
  ```
- [`e305665`](https://github.com/ghostty-org/ghostty/commit/e3056658d05bdd54db9fd37a02c196bfe81cfe39) libghostty: faster render state updates and C API reads ([@mitchellh](https://github.com/mitchellh))
  ```text
  This improves the performance of render state plus C API reads. I
  specifically benchmarked the C API call and found a lot of overhead in
  the C API layer which this cleans up. The impact of these changes will be
  less visible to Zig consumers but moderately improve there.
  
  All benchmark numbers below are via the C API.
  
  Highlights:
  
  - full rebuilds are **1.71x faster (11.4µs to 6.6µs per 120x80 frame)**
  - single-dirty-row updates (e.g. the TUI/prompt steady state) are *1.44x
    faster**
  - full-frame reads through the C API are **1.2x to 1.8x faster**
  
  ## Changes
  
  * endUpdate skips unchanged style runs.
  * `GRAPHEMES_UTF8` getter gets a fast path for single ASCII codepoints (the
    overwhelming majority of cells).
  * The bg/fg color getters no longer copy the full 28-byte style. Instead,
     they switch directly on the one color field they need.
  * The `get_multi` variants validate the handle and position once per batch
    instead of per key.
  * Iterator positions are sentinel values instead of Zig optionals. The
    optional tagging overhead was showing up in benchmarks.
  * `colors_get` reads through a pointer instead of copying the ~1KB colors
    struct to the stack per call.
  * The palette conversion is vectorized. The 4-byte padded RGB to 3-byte
    was not being auto-vectorized. Explicitly vectorize it. Something like
    a 4x speedup on NEON.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | update (forced full rebuild) | 11.4 µs/frame | 6.6 µs/frame | 1.71x |
  | update (single dirty row) | 143 ns | 99 ns | 1.44x |
  | read cell style/bg/fg/selected | 10.3 ns/cell | 8.8 ns/cell | 1.17x |
  | read cell via get_multi | 9.6 ns/cell | 6.9 ns/cell | 1.40x |
  | read cell UTF-8 text | 4.9 ns/cell | 2.7 ns/cell | 1.78x |
  | colors_get + palette | 213 ns/call | 45 ns/call | 4.58x |
  
  Clean updates (no terminal changes) and the raw cell read paths
  are unchanged.
  
  **AI usage:** Driven by Fable primarily, reviewed everything and rewrote
  all human-language (comments) since Fable in particular does really bad
  at that. This commit message too.
  ```
- [`53be7d0`](https://github.com/ghostty-org/ghostty/commit/53be7d0353640351e2d6a06725779f21a3ebe481) libghostty: faster render state updates and C API reads ([#13818](https://github.com/ghostty-org/ghostty/issues/13818)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This improves the performance of render state plus C API reads. I
  specifically benchmarked the C API call and found a lot of overhead in
  the C API layer which this cleans up. The impact of these changes will
  be less visible to Zig consumers but moderately improve there.
  
  All benchmark numbers below are via the C API.
  
  Highlights:
  
  - full rebuilds are **1.71x faster (11.4µs to 6.6µs per 120x80 frame)**
  - single-dirty-row updates (e.g. the TUI/prompt steady state) are
  **1.44x faster**
  - full-frame reads through the C API are **1.2x to 1.8x faster**
  
  ## Changes
  
  * endUpdate skips unchanged style runs.
  * `GRAPHEMES_UTF8` getter gets a fast path for single ASCII codepoints
  (the overwhelming majority of cells).
  * The bg/fg color getters no longer copy the full 28-byte style.
  Instead, they switch directly on the one color field they need.
  * The `get_multi` variants validate the handle and position once per
  batch instead of per key.
  * Iterator positions are sentinel values instead of Zig optionals. The
  optional tagging overhead was showing up in benchmarks.
  * `colors_get` reads through a pointer instead of copying the ~1KB
  colors struct to the stack per call.
  * The palette conversion is vectorized. The 4-byte padded RGB to 3-byte
  was not being auto-vectorized. Explicitly vectorize it. Something like a
  4x speedup on NEON.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | update (forced full rebuild) | 11.4 µs/frame | 6.6 µs/frame | 1.71x |
  | update (single dirty row) | 143 ns | 99 ns | 1.44x |
  | read cell style/bg/fg/selected | 10.3 ns/cell | 8.8 ns/cell | 1.17x |
  | read cell via get_multi | 9.6 ns/cell | 6.9 ns/cell | 1.40x |
  |read cell UTF-8 text | 4.9 ns/cell | 2.7 ns/cell | 1.78x |
  | colors_get + palette | 213 ns/call | 45 ns/call | 4.58x |
  
  Clean updates (no terminal changes) and the raw cell read paths are
  unchanged.
  
  **AI usage:** Driven by Fable primarily, reviewed everything and rewrote
  all human-language (comments) since Fable in particular does really bad
  at that. This commit message too.
  ```
- [`87f69a1`](https://github.com/ghostty-org/ghostty/commit/87f69a12ee28445cd95e39060fd626ccfc27b5e0) libghostty: much faster vt_write on wasm targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes `ghostty_terminal_vt_write` on wasm32-freestanding anywhere
  from 1.4x to 13x faster depending on the input, measured in V8 via Node
  for Chrome as well as `jsc` for Safari.
  
  ## Changes
  
  * stream: the batched parse path (bulk UTF-8 decode, print_slice runs)
    is used even when `build_options.simd` is false. The per-byte loop
    is now debug-only.
  * simd/vt: the scalar `utf8DecodeUntilControlSeq` gets a vectorized
    ASCII bulk path that is compatible with wasm simd128.
  * style: on wasm, `Style.eql` compares canonical `PackedStyle` forms
    which is faster by like 11%. On native its slower so we only do this
    for wasm.
  * build: wasm targets now default to the `simd128` CPU feature since
    every browser engine has supported it for years. Opt out with
    `-Dcpu=generic`.
  * PACKAGING.md documents the wasm build, including `wasm-opt` notes.
  
  ## Benchmarks
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | ascii | 85 MB/s | 1070 MB/s | 12.5x |
  | ascii-wrap | 84 MB/s | 1103 MB/s | 13.1x |
  | clear-redraw | 85 MB/s | 913 MB/s | 10.7x |
  | scroll | 79 MB/s | 304 MB/s | 3.8x |
  | cursor | 120 MB/s | 255 MB/s | 2.1x |
  | utf8 | 99 MB/s | 169 MB/s | 1.7x |
  | sgr16 | 81 MB/s | 133 MB/s | 1.6x |
  | sgr-truecolor | 62 MB/s | 88 MB/s | 1.4x |
  
  End result: wasm at roughly 50-85% of the native ReleaseFast+SIMD build
  on the same workloads. Plain ASCII was at 6% of native before.
  
  **AI usage:** Lots of Fable help. As always, the human language stuff
  like this commit and comments were rewritten by me.
  ```
- [`2f72b04`](https://github.com/ghostty-org/ghostty/commit/2f72b041f65932867baef177e8f3be9c92b0f2ed) libghostty: much faster vt_write on wasm targets ([#13821](https://github.com/ghostty-org/ghostty/issues/13821)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes `ghostty_terminal_vt_write` on wasm32-freestanding anywhere
  from 1.4x to 13x faster depending on the input, measured in V8 via Node
  for Chrome as well as `jsc` for Safari.
  
  This changes the default Wasm build to default to enabling the `simd128`
  CPU feature because baseline doesn't have that and every major browser
  has supported it for years. This results in massive performance
  improvements (like, 50%+ on all streams).
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions.
  
  ## Changes
  
  * stream: the batched parse path (bulk UTF-8 decode, print_slice runs)
  is used even when `build_options.simd` is false. The per-byte loop is
  now debug-only.
  * simd/vt: the scalar `utf8DecodeUntilControlSeq` gets a vectorized
  ASCII bulk path that is compatible with wasm simd128.
  * style: on wasm, `Style.eql` compares canonical `PackedStyle` forms
  which is faster by like 11%. On native its slower so we only do this for
  wasm.
  * build: wasm targets now default to the `simd128` CPU feature since
  every browser engine has supported it for years. Opt out with
  `-Dcpu=generic`.
  * PACKAGING.md documents the wasm build, including `wasm-opt` notes.
  
  ## Benchmarks
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | ascii | 85 MB/s | 1070 MB/s | 12.5x |
  | ascii-wrap | 84 MB/s | 1103 MB/s | 13.1x |
  | clear-redraw | 85 MB/s | 913 MB/s | 10.7x |
  | scroll | 79 MB/s | 304 MB/s | 3.8x |
  | cursor | 120 MB/s | 255 MB/s | 2.1x |
  | utf8 | 99 MB/s | 169 MB/s | 1.7x |
  | sgr16 | 81 MB/s | 133 MB/s | 1.6x |
  | sgr-truecolor | 62 MB/s | 88 MB/s | 1.4x |
  
  End result: wasm at roughly 50-85% of the native ReleaseFast+SIMD build
  on the same workloads. Plain ASCII was at 6% of native before.
  
  **AI usage:** Lots of Fable help. As always, the human language stuff
  like this commit and comments were rewritten by me.
  ```
- [`29a70bc`](https://github.com/ghostty-org/ghostty/commit/29a70bc3674e7a95c47a54f9660833a86c87f3b5) ci: publish wasm tip artifacts ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds and publishes `ghostty-vt.wasm` binaries into our tip
  GitHub releases. These are built with the proper optimization, `simd128`
  CPU feature set, and run through `wasm-opt`.
  
  This allows wasm consumers to use libghostty without a Zig toolkit.
  
  Published two: `ghostty-vt.wasm` and `ghostty-vt-small.wasm`. The latter
  is ReleaseSmall, but is 10 to 20% slower. Users choice.
  ```
- [`8f485a7`](https://github.com/ghostty-org/ghostty/commit/8f485a7f478fc497ec02d60f274a33af542f1819) ci: publish wasm tip artifacts ([#13822](https://github.com/ghostty-org/ghostty/issues/13822)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds and publishes `ghostty-vt.wasm` binaries into our tip GitHub
  releases. These are built with the proper optimization, `simd128` CPU
  feature set, and run through `wasm-opt`.
  
  This allows wasm consumers to use libghostty without a Zig toolkit.
  
  Published two: `ghostty-vt.wasm` and `ghostty-vt-small.wasm`. The latter
  is ReleaseSmall, but is 10 to 20% slower. Users choice.
  ```
- [`74a233b`](https://github.com/ghostty-org/ghostty/commit/74a233b5439c6721cee8ae1f453c308e02ca9d74) libghostty: faster render state reads and updates on wasm targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the `ghostty_render_state_*` C API significantly faster on
  wasm32-freestanding, measured in V8 via Node for Chrome. Also verified
  in `jsc` for Safari.
  
  The major change is a new bulk row read API that makes full-screen cell reads
  roughly 10x faster for wasm embedders. This should help any embedder with
  high FFI overhead, such as Go, Python, etc. too.
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions (two of the changes are native wins as well).
  
  ## Changes
  
  * color: the "vectorized" palette conversion loop was silently
    scalarized by LLVM into per-byte ops because it loaded/stored through
    array-typed pointers. Zig 0.16 disables the LLVM loop vectorizer, so
    manually vectorized loops must go through vector-typed pointers.
  * C styles: major optimizations to converting Zig styles to C styles.
    This is a heavy operation for render state.
  * render: `endUpdate`'s style-run fill (`@memset` with a struct value)
    re-loaded its source every iteration and stored field by field. Now
    manually vectorized.
  * render: new `GHOSTTY_RENDER_STATE_ROW_DATA_CELLS_RAW` returns a
    borrowed `GhosttyCellsView` of the current row's raw cell values, valid
    until the next update. One call per row instead of 3-6 calls per cell.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | colors_get | 114 ns | 35 ns | 3.3x |
  | style get, per styled cell | 7.8 ns | 6.7 ns | 1.2x |
  | raw+style read, per cell | 8.6 ns | 7.7 ns | 1.1x |
  | full-screen text read, per cell | 7.5 ns | 0.7 ns | 10.7x |
  | full-screen text+style read, per cell | 8.6 ns | 1.7 ns | 5.1x |
  | render state update, styled full frame | 3.4 us | 2.6 us | 1.3x |
  
  **AI usage:** Fable did the implementation and benchmarking and drafted
  this message. Comments were partially rewritten by me.
  ```
- [`16833f5`](https://github.com/ghostty-org/ghostty/commit/16833f5e5f58589c3d6ba876a73eb0c5f550231d) libghostty: faster render state reads and updates on wasm targets ([#13825](https://github.com/ghostty-org/ghostty/issues/13825)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the `ghostty_render_state_*` C API significantly faster on
  wasm32-freestanding, measured in V8 via Node for Chrome. Also verified
  in `jsc` for Safari.
  
  The major change is a new bulk row read API that makes full-screen cell
  reads roughly 10x faster for wasm embedders. This should help any
  embedder with high FFI overhead, such as Go, Python, etc. too.
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions (two of the changes are native wins as well).
  
  ## Changes
  
  * color: the "vectorized" palette conversion loop was silently
  scalarized by LLVM into per-byte ops because it loaded/stored through
  array-typed pointers. Zig 0.16 disables the LLVM loop vectorizer, so
  manually vectorized loops must go through vector-typed pointers.
  * C styles: major optimizations to converting Zig styles to C styles.
  This is a heavy operation for render state.
  * render: `endUpdate`'s style-run fill (`@memset` with a struct value)
  re-loaded its source every iteration and stored field by field. Now
  manually vectorized.
  * render: new `GHOSTTY_RENDER_STATE_ROW_DATA_CELLS_RAW` returns a
  borrowed `GhosttyCellsView` of the current row's raw cell values, valid
  until the next update. One call per row instead of 3-6 calls per cell.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | colors_get | 114 ns | 35 ns | 3.3x |
  | style get, per styled cell | 7.8 ns | 6.7 ns | 1.2x |
  | raw+style read, per cell | 8.6 ns | 7.7 ns | 1.1x |
   | full-screen text read, per cell | 7.5 ns | 0.7 ns | 10.7x |
   | full-screen text+style read, per cell | 8.6 ns | 1.7 ns | 5.1x |
  | render state update, styled full frame | 3.4 us | 2.6 us | 1.3x |
  
  **AI usage:** Fable did the implementation and benchmarking and drafted
  this message. Comments were partially rewritten by me.
  ```
- [`3d9b2b4`](https://github.com/ghostty-org/ghostty/commit/3d9b2b483cd807c05e72e2827559572c38bcbe66) libghostty: much faster grapheme-heavy IO throughput ([@mitchellh](https://github.com/mitchellh))
  ```text
  Processing grapheme-heavy input (ZWJ sequences, emoji modifiers, flags,
  combining marks) through is now almost 3x faster.
  
  ### Primary Change: PageList Capacity Projection
  
  This workload was heavily bound by `PageList.increaseCapacity` because
  pathological cases of single-dimensional growth cause repeated page
  capacity doublings which get increasingly expensive because each time we
  do a full allocation + clone.
  
  So the major change is that for grapheme bytes in particular, when we
  reach a capacity limit, we take the current usage for the current set of
  rows and project it out to the remaining capacity of rows. Basically, we
  assume that a similar workload will continue. So rather than doubling,
  we're _guessing_ how much you're going to need.
  
  In the real world, I'm not really sure if this matters at all. There are
  no regressions on any regular corpus streams (asciinema, wikipedia dumps, etc.).
  
  ### Other Changes
  
  There are some other changes here, all found on the path to improving
  grapheme IO throughput:
  
  * The bitmap allocator now maintains `search_start` hint we update on
    every allocation so that future free-scans are much faster. This is
    the lowest possible place we don't have a full bitmap.
  
  * For wasm32, we use an alternate hashing structure for small keys
    since Wyhash's 64bit * 64bit multiplication is very very slow because
    wasm has no widening instruction.
  
  * Terminal `printSlice` now checks the fast path compatibility once up front
    rather than on every fast-path attempt.
  
  ### Benchmarks
  
  Data: ZWJ family/profession sequences, skin-tone modifiers,
  flags, and combining marks streamed in 64 KiB chunks into an 80x24
  terminal, default modes.
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | wasm, V8, 16 MiB stream | 52 MB/s | 151 MB/s | 2.9x |
  | native, terminal-stream, 64 MiB | 894 ms | 305 ms | 2.9x |
  
  Sorry the native stuff is in ms, that's how our native `ghostty-bench`
  does things versus the custom little V8 harness.
  
  **AI usage:** Developed alongside Fable: profiling, implementation, and
  benchmarks. All human language messages written myself. Validated myself.
  ```
- [`6b22215`](https://github.com/ghostty-org/ghostty/commit/6b22215c5d46019f94b658f7665941f951d0de1e) libghostty: much faster grapheme-heavy IO throughput ([#13826](https://github.com/ghostty-org/ghostty/issues/13826)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Processing grapheme-heavy input (ZWJ sequences, emoji modifiers, flags,
  combining marks) through is now almost 3x faster.
  
  ### Primary Change: PageList Capacity Projection
  
  This workload was heavily bound by `PageList.increaseCapacity` because
  pathological cases of single-dimensional growth cause repeated page
  capacity doublings which get increasingly expensive because each time we
  do a full allocation + clone.
  
  So the major change is that for grapheme bytes in particular, when we
  reach a capacity limit, we take the current usage for the current set of
  rows and project it out to the remaining capacity of rows. Basically, we
  assume that a similar workload will continue. So rather than doubling,
  we're _guessing_ how much you're going to need.
  
  In the real world, I'm not really sure if this matters at all. There are
  no regressions on any regular corpus streams (asciinema, wikipedia
  dumps, etc.).
  
  ### Other Changes
  
  There are some other changes here, all found on the path to improving
  grapheme IO throughput:
  
  * The bitmap allocator now maintains `search_start` hint we update on
  every allocation so that future free-scans are much faster. This is the
  lowest possible place we don't have a full bitmap.
  
  * For wasm32, we use an alternate hashing structure for small keys since
  Wyhash's 64bit * 64bit multiplication is very very slow because wasm has
  no widening instruction.
  
  * Terminal `printSlice` now checks the fast path compatibility once up
  front rather than on every fast-path attempt.
  
  ### Benchmarks
  
  Data: ZWJ family/profession sequences, skin-tone modifiers, flags, and
  combining marks streamed in 64 KiB chunks into an 80x24 terminal,
  default modes.
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | wasm, V8, 16 MiB stream | 52 MB/s | 151 MB/s | 2.9x |
  | native, terminal-stream, 64 MiB | 894 ms | 305 ms | 2.9x |
  
  Sorry the native stuff is in ms, that's how our native `ghostty-bench`
  does things versus the custom little V8 harness.
  
  **AI usage:** Developed alongside Fable: profiling, implementation, and
  benchmarks. All human language messages written myself. Validated
  myself.
  ```
- [`88ed6be`](https://github.com/ghostty-org/ghostty/commit/88ed6bebf4abfa8deb1b0cdd73dde4b07c7e0a3e) libghostty: much faster wide-character reflow on resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  Resizing a terminal whose buffer is heavy with wide characters (CJK,
  emoji) is now 3-5x faster on the reflow path.
  
  This was relatively simple work. We already have a bulk fast path for
  same-style cells. We previously omitted ANY wide characters from this.
  We relaxed this by making it work with complete wide pairs (wide followed
  by spacer tail).
  
  ### Benchmarks
  
  Resize dance (13 column resizes, 80 -> 40 -> 132 and back and forth again)
  over a ~2,000-row scrollback buffer.
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | cjk | 0.938 | 0.296 | 3.2x |
  | emoji | 0.875 | 0.191 | 4.6x |
  | mixed build-log | 0.306 | 0.155 | 2.0x |
  | grapheme | 2.449 | 1.831 | 1.3x |
  | ascii-short | 0.115 | 0.117 | 1.0x |
  | ascii-long | 0.109 | 0.112 | 1.0x |
  | latin | 0.093 | 0.095 | 1.0x |
  | sgr-truecolor | 0.939 | 0.965 | 1.0x |
  
  **AI usage:** Profiled, implemented, benchmarked, and written by Fable.
  Plan validated by me before doing it, I wrote all the
  comments/commits/blah.
  ```
- [`d760ee9`](https://github.com/ghostty-org/ghostty/commit/d760ee96e54657416eb427b793c7e839f003df7d) terminal: much faster wide-character reflow on resize ([#13827](https://github.com/ghostty-org/ghostty/issues/13827)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Resizing a terminal whose buffer is heavy with wide characters (CJK,
  emoji) is now 3-5x faster on the reflow path.
  
  This was relatively simple work. We already have a bulk fast path for
  same-style cells. We previously omitted ANY wide characters from this.
  We relaxed this by making it work with complete wide pairs (wide
  followed by spacer tail).
  
  ### Benchmarks
  
  Resize dance (13 column resizes, 80 -> 40 -> 132 and back and forth
  again) over a ~2,000-row scrollback buffer.
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | cjk | 0.938 | 0.296 | 3.2x |
  | emoji | 0.875 | 0.191 | 4.6x |
  | mixed build-log | 0.306 | 0.155 | 2.0x |
  | grapheme | 2.449 | 1.831 | 1.3x |
  | ascii-short | 0.115 | 0.117 | 1.0x |
  | ascii-long | 0.109 | 0.112 | 1.0x |
  | latin | 0.093 | 0.095 | 1.0x |
  | sgr-truecolor | 0.939 | 0.965 | 1.0x |
  
  **AI usage:** Profiled, implemented, benchmarked, and written by Fable.
  Plan validated by me before doing it, I wrote all the
  comments/commits/blah.
  ```
- [`d61920d`](https://github.com/ghostty-org/ghostty/commit/d61920d80e0e6d2c2a058c96d1b916c7300ddab5) lib-vt: disable logging in wasm release builds ([@mitchellh](https://github.com/mitchellh))
- [`51a4311`](https://github.com/ghostty-org/ghostty/commit/51a4311ef18b0971c112967cf24a538a2c71ea36) terminal: clean up overzealous inlining ([@mitchellh](https://github.com/mitchellh))
- [`e84dd30`](https://github.com/ghostty-org/ghostty/commit/e84dd3015543d695e51993e02a01283cfdab2439) Update VOUCHED list ([#13829](https://github.com/ghostty-org/ghostty/issues/13829)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13828#discussioncomment-18024891)
  from @jcollie.
  
  Vouch: @diego-moment
  ```
- [`0e0893a`](https://github.com/ghostty-org/ghostty/commit/0e0893adff219b80f8837f685bfd54f643036fc6) libghostty: attacking wasm binary size ([#13830](https://github.com/ghostty-org/ghostty/issues/13830)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This should release our ReleaseFast bundle from 1.1MB to ~800KB.
  
  The major win is disabling logging in ReleaseFast wasm builds (~200KB).
  
  The next is removing aggressive inlining in paths that don't make sense
  for performance. Verified with benchmarks on native to not affect
  anything really.
  
  The third was really dumb: `var buf: [4096]u32 = @splat(c)` in LLVM
  releasefast for wasm was lowering to 4096 separate `i32.store`...
  like... 30KB of code. Replacing this with a for loop reduced by 30KB and
  made REP (a rare sequence) 11x faster lol.
  ```
- [`348f714`](https://github.com/ghostty-org/ghostty/commit/348f714ff97a4b323ee2ce195bb16387ba6a1dbe) Update VOUCHED list ([#13833](https://github.com/ghostty-org/ghostty/issues/13833)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13831#discussioncomment-18025282)
  from @jcollie.
  
  Vouch: @DiegoArmstrong
  ```
- [`1fdbb8c`](https://github.com/ghostty-org/ghostty/commit/1fdbb8c912231bdbe039614a70f10772a3e50d23) libghostty: -Dvt-features to compile out unused features ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a `-Dvt-features` build option for libghostty-vt that
  compiles out optional feature areas, primarily so size-conscious
  embedders (e.g. wasm) can significantly trim the binary.
  
  The flag is similar to `-Dcpu`, `+feature` or `feature` to enable it,
  `-feature` to disable, magic word `all` to turn all features on or off.
  Example: `-Dvt-features=-all,+render-state` builds only the render
  state API.
  
  ### Sizes
  
  | Build | Bytes | Brotli |
  |---|---|---|
  | default (all features) | 876,500 | 218,309 |
  | web interactive (`-all,+render-state,+input-encode,+selection,+color,+grid-introspection`) | 661,119 | 168,994 |
  | read-only viewer (`-all,+render-state`) | 537,441 | 132,858 |
  | bare VT core (`-all`) | 515,422 | 125,756 |
  | xterm.js browser bundle (incl. renderers) | 488,663 | 99,311 |
  | @xterm/headless | 182,672 | 39,651 |
  
  Note: xterm versions are stable as of this commit.
  ```
- [`794515b`](https://github.com/ghostty-org/ghostty/commit/794515ba60a8c6d537b5f3a427374b23b2673492) libghostty: -Dvt-features to compile out unused features ([#13834](https://github.com/ghostty-org/ghostty/issues/13834)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a `-Dvt-features` build option for libghostty-vt that
  compiles out optional feature areas, primarily so size-conscious
  embedders (e.g. wasm) can significantly trim the binary.
  
  The flag is similar to `-Dcpu`, `+feature` or `feature` to enable it,
  `-feature` to disable, magic word `all` to turn all features on or off.
  Example: `-Dvt-features=-all,+render-state` builds only the render state
  API.
  
  Added CI to verify the lib and tests _compile_ (we don't run it) for
  each individual feature.
  
  ### Sizes
  
  wasm32, ReleaseFast:
  
  | Build | Bytes | Brotli |
  |---|---|---|
  | default (all features) | 876,500 | 218,309 |
  | web interactive
  (`-all,+render-state,+input-encode,+selection,+color,+grid-introspection`)
  | 661,119 | 168,994 |
  | read-only viewer (`-all,+render-state`) | 537,441 | 132,858 |
  | bare VT core (`-all`) | 515,422 | 125,756 |
  | xterm.js browser bundle (incl. renderers) | 488,663 | 99,311 |
  | @xterm/headless | 182,672 | 39,651 |
  
  Note: xterm versions are stable as of this commit.
  
  ### C Header Note
  
  I didn't do a `vt/features.h` style header that has macros to guard
  symbols for the various features. This is something we should do in the
  future. The way it is now, the C header always declares everything, and
  its not a problem unless an unavailable function is referenced at link
  time.
  ```
- [`b5aa8e7`](https://github.com/ghostty-org/ghostty/commit/b5aa8e7a071f53dec2c203fc521e147ce6e8cce0) i18n: complete Kazakh (kk) translation for v1.4 ([#13778](https://github.com/ghostty-org/ghostty/issues/13778)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translates the 180 remaining strings, mainly command palette entries
  introduced for v1.4 localization.
  ```
- [`53c6fdb`](https://github.com/ghostty-org/ghostty/commit/53c6fdbe7d53eb8c61f7af5e311d04956c4fe283) apprt: own desktop notification truncation ([@dolzenko](https://github.com/dolzenko))
  ```text
  Make the fixed-size desktop notification payload a named Message type and initialize it through a constructor.
  
  Keeping UTF-8 boundary truncation with the payload owns the buffer capacities and sentinel termination at the message boundary, while stream_handler only forwards the title and body.
  ```
- [`946422d`](https://github.com/ghostty-org/ghostty/commit/946422dbc5832bb1d8e3298e339c89577da86bca) terminal: replace std.fmt.parseFloat with custom fraction parsing ([@mitchellh](https://github.com/mitchellh))
  ```text
  We have exactly two callers of `parseFloat` and they both have very
  limited expect input shapes: values 0-1, simple decimals. parseFloat
  brings in ~26KB of binary size, so replace it with a custom parser for
  our exact shape.
  ```
- [`e3939d0`](https://github.com/ghostty-org/ghostty/commit/e3939d0f6224f2d9d16d030e7c1c04f082b0f39e) terminal: replace std.fmt.parseFloat with custom fraction parsing ([#13839](https://github.com/ghostty-org/ghostty/issues/13839)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We have exactly two callers of `parseFloat` and they both have very
  limited expect input shapes: values 0-1, simple decimals. parseFloat
  brings in ~26KB of binary size, so replace it with a custom parser for
  our exact shape.
  ```
- [`f748b17`](https://github.com/ghostty-org/ghostty/commit/f748b17e27f5ee089494044179dea1c493ce63cc) feat: expand tildes in config theme path to HOME ([@preiter93](https://github.com/preiter93))
  ````text
  When loading a theme from a path that includes a tilde:
  ```
  theme="~/.cache/wal/colors-ghostty"
  ```
  currently fails with the following error:
  ```
  cannot include path separators unless it is an absolute path
  ```
  
  This PR tries to expand the ~ of the path. If there is no ~
  or expansion fails, it falls back to the unexpanded value.
  ````
- [`cecf816`](https://github.com/ghostty-org/ghostty/commit/cecf81678e47f967b0354acada67e69d229f436b) Update VOUCHED list ([#13843](https://github.com/ghostty-org/ghostty/issues/13843)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13841#discussioncomment-18031969)
  from @jcollie.
  
  Vouch: @preiter93
  ```
- [`fff9f62`](https://github.com/ghostty-org/ghostty/commit/fff9f62f38cfef56ada5239ea22555b35c1e063c) cli: always install embedded SSH terminfo ([@jparise](https://github.com/jparise))
  ```text
  Remove the remote infocmp short-circuit from +ssh setup. The command
  already sends Ghostty's embedded terminfo source to tic, so accepting
  any existing entry leaves the payload unused and can preserve stale
  data.
  ```
- [`06b63c4`](https://github.com/ghostty-org/ghostty/commit/06b63c48594ea04d2a68dd8249250d1477722296) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`69b9abf`](https://github.com/ghostty-org/ghostty/commit/69b9abf09ebad2b11a6850a28271676f6bfeb108) cli: version SSH terminfo cache entries ([@jparise](https://github.com/jparise))
  ```text
  Derive a version from the encoded Ghostty terminfo and require callers
  to pass it explicitly when reading or writing the SSH cache. Cache
  entries created for older or different payloads no longer suppress a
  required installation.
  ```
- [`c121734`](https://github.com/ghostty-org/ghostty/commit/c1217342958b90ed3a25413c1616dfd2dd8cd1bf) move shell expand of theme from theme.zig to config.zig ([@preiter93](https://github.com/preiter93))
- [`36d8e3f`](https://github.com/ghostty-org/ghostty/commit/36d8e3f77779939a4413ddcd72c05ab08aeae57d) terminal/snapshot: slicing-by-16 software CRC32C ([@mitchellh](https://github.com/mitchellh))
  ```text
  The software CRC32C fallback (WebAssembly and any other target without a
  dedicated instruction) was the std byte-at-a-time table walk, which
  profiled at ~65% of snapshot encode and ~70% of decode self-time in V8.
  Replace it with slicing-by-16: sixteen bytes fold per iteration through
  comptime per-position tables, so the serial dependency advances one block
  at a time instead of one byte.
  
  The hardware backends (aarch64 CRC, x86_64 SSE4.2) are unchanged, so
  native is expected to be unaffected; its deltas below are run-to-run
  noise.
  
  Benchmarks: wasm is V8 (node 25), ReleaseFast + wasm-opt -O3, 80x24
  terminal, 2 MiB VT corpus per workload, complete snapshot including
  scrollback, best-of-5. Native is aarch64 macOS, hyperfine mean,
  ghostty-bench +terminal-snapshot --loops=20. "base" is the parent commit.
  
  | wasm      | encode base | encode   | decode base | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     7.07 ms |  3.43 ms |     6.45 ms |  2.81 ms |
  | styled    |    10.54 ms |  3.14 ms |    14.37 ms |  7.12 ms |
  | truecolor |    15.23 ms |  5.33 ms |    21.76 ms | 12.11 ms |
  | cjk       |    25.41 ms |  5.95 ms |    30.83 ms | 12.04 ms |
  | grapheme  |    27.67 ms | 14.18 ms |    27.00 ms | 13.16 ms |
  
  | native | mode   | base    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 40.6 ms | 41.7 ms |
  | ascii  | decode | 51.2 ms | 53.2 ms |
  | utf8   | encode | 45.2 ms | 47.2 ms |
  | utf8   | decode | 59.8 ms | 61.6 ms |
  ```
- [`c1a61fd`](https://github.com/ghostty-org/ghostty/commit/c1a61fddda00e907c7e66bd3609d6c558cccd26d) terminal/snapshot: borrow fully buffered record payloads ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the record source already has the complete payload buffered — always
  the case for in-memory snapshots such as ghostty_snapshot_decoder_new_buf
  — the record reader now borrows the payload straight out of the source
  buffer instead of streaming it through the limited and hashing reader
  adapters. Payload decoders parse a fixed reader over the borrowed bytes,
  `finish` validates the CRC with a single bulk update, and the source
  advances only after validation.
  
  The page decoder takes a matching fast path: a fully buffered payload is
  parsed in place, skipping the staging allocation and copy it previously
  made per PAGE record. Streaming sources are unchanged.
  
  This is a modest win on its own; it is also the foundation for later
  commits whose buffered fast paths rely on the payload being contiguous.
  
  Benchmarks (see the first commit in this series for methodology; "prev"
  is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     3.43 ms |  3.50 ms |     2.81 ms |  2.68 ms |
  | styled    |     3.14 ms |  3.15 ms |     7.12 ms |  7.04 ms |
  | truecolor |     5.33 ms |  5.27 ms |    12.11 ms | 12.04 ms |
  | cjk       |     5.95 ms |  5.92 ms |    12.04 ms | 11.89 ms |
  | grapheme  |    14.18 ms | 14.33 ms |    13.16 ms | 13.14 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 41.7 ms | 41.8 ms |
  | ascii  | decode | 53.2 ms | 52.4 ms |
  | utf8   | encode | 47.2 ms | 47.4 ms |
  | utf8   | decode | 61.6 ms | 61.2 ms |
  ```
- [`973f619`](https://github.com/ghostty-org/ghostty/commit/973f619a2371c50fffb2062bd59a0c5134c783b1) terminal/snapshot: vectorize grid row encoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Row encoding previously made two scalar passes over every row (a backward
  scan for the encoded cell count and a validation pass accumulating the
  width-selection OR), then wrote a 3-byte header and per-width chunked
  cells through separate writer calls.
  
  Three changes, all bulk-codec only with the portable path unchanged:
  
    - scanRow computes the count and word-OR in @Vector(4, u64) strides.
      Trailing default cells are all-zero words, so the OR over the whole
      row equals the OR over the encoded prefix.
    - The per-cell wide-pair validation loop is skipped entirely when the
      OR carries no wide bits, which is every row of plain text.
    - Rows are emitted with a single reservation in the destination's spare
      buffer capacity (header plus cells, no writer calls), using explicit
      i8x16.shuffle truncation for the 1/2/4-byte cell widths. Zig 0.16
      disables loop auto-vectorization, so the previous "vectorizable"
      truncating loop was actually scalar. Destinations without buffered
      capacity (counting writers, a still-growing scratch) fall through to
      the streaming path.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     3.50 ms |  2.09 ms |     2.68 ms |  2.67 ms |
  | styled    |     3.15 ms |  2.23 ms |     7.04 ms |  7.00 ms |
  | truecolor |     5.27 ms |  4.95 ms |    12.04 ms | 11.85 ms |
  | cjk       |     5.92 ms |  6.03 ms |    11.89 ms | 11.67 ms |
  | grapheme  |    14.33 ms | 13.08 ms |    13.14 ms | 13.28 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 41.8 ms | 24.5 ms |
  | ascii  | decode | 52.4 ms | 53.4 ms |
  | utf8   | encode | 47.4 ms | 47.6 ms |
  | utf8   | decode | 61.2 ms | 60.9 ms |
  ```
- [`593762c`](https://github.com/ghostty-org/ghostty/commit/593762cfa11afdd3eaefc9e0bdd9d979d85ab39f) terminal/snapshot: batch grapheme suffix codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Grapheme suffix encoding made two full passes over the grid (a counting
  pass, then an emit pass) and issued three writer calls per entry plus one
  per codepoint. Every grapheme cell owns exactly one entry in the page's
  grapheme map, so the section count now comes straight from
  page.graphemeCount() with no counting pass, and entries are batched
  through a 4 KB buffer with one writer call per flush. The per-entry size
  check moved into the emit loop; an error still cancels the whole record
  before any of it is emitted, so error behavior is unchanged.
  
  Decoding similarly parsed entry headers and codepoints with one reader
  call per integer. Fully buffered payloads (the common case after the
  borrowed-payload commit) now parse entry headers and codepoint runs
  directly from the buffered bytes, and entries whose target cell cannot
  carry a suffix discard their codepoints in bulk.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.09 ms |  2.07 ms |     2.67 ms |  2.69 ms |
  | styled    |     2.23 ms |  2.29 ms |     7.00 ms |  7.06 ms |
  | truecolor |     4.95 ms |  4.91 ms |    11.85 ms | 11.99 ms |
  | cjk       |     6.03 ms |  6.14 ms |    11.67 ms | 11.83 ms |
  | grapheme  |    13.08 ms |  8.26 ms |    13.28 ms | 11.18 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.5 ms | 24.3 ms |
  | ascii  | decode | 53.4 ms | 50.9 ms |
  | utf8   | encode | 47.6 ms | 41.2 ms |
  | utf8   | decode | 60.9 ms | 59.5 ms |
  ```
- [`2aaad3c`](https://github.com/ghostty-org/ghostty/commit/2aaad3ca99a27d36eff57d6e59e2044005ef2ba4) terminal/snapshot: vectorize grid cell decoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoding one- and two-byte cells widened them to their 8-byte words one
  scalar store at a time. The bulk codec now widens sixteen transported
  bytes per step with byte shuffles against a zero vector, degrading
  width-two surrogate lanes to U+FFFD with a vector select, exactly
  matching the scalar path. Short row tails reprocess the final full
  window with overlapping stores that rewrite identical bytes.
  
  This is a native win: the shuffles lower to NEON and take ascii decode
  from 38.9 ms to 34.0 ms (measured by toggling this path at the tip of
  this series). On wasm, V8 runs the scalar fallback at the same speed as
  the shuffle version — the loop is store-bound either way — so the wasm
  deltas below are flat.
  
  Row decoding also drops per-field packed-struct read-modify-writes in
  favor of one load and one store per row header, and rows that are fully
  default (zero header byte, zero encoded cells) skip all work: decoded
  pages start zeroed, which is exactly the default row and cell state.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.07 ms |  2.18 ms |     2.69 ms |  2.68 ms |
  | styled    |     2.29 ms |  2.28 ms |     7.06 ms |  6.93 ms |
  | truecolor |     4.91 ms |  4.93 ms |    11.99 ms | 11.91 ms |
  | cjk       |     6.14 ms |  6.11 ms |    11.83 ms | 11.72 ms |
  | grapheme  |     8.26 ms |  8.28 ms |    11.18 ms | 11.38 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.3 ms | 24.3 ms |
  | ascii  | decode | 50.9 ms | 46.7 ms |
  | utf8   | encode | 41.2 ms | 41.0 ms |
  | utf8   | decode | 59.5 ms | 59.5 ms |
  ```
- [`7c1014e`](https://github.com/ghostty-org/ghostty/commit/7c1014ef662cd4e9b968b5bac6ca062fa17a3b56) terminal/snapshot: resolve wide pairs in a per-row pass ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cell decoding ran wide-pair normalization inline for every decoded cell:
  two neighbor loads and a switch per cell, even though the overwhelming
  majority of rows contain no wide cells at all. Normalization is defined
  against already-stored predecessors, so running it as an ordered pass
  over the stored row afterward is exactly equivalent to interleaving it.
  
  The word-cell decoders now accumulate the bitwise OR of the row's wire
  words as they apply cells, and the pass is gated on it: rows without
  wide bits are already normalized (every cell narrow), and width-four and
  narrower transports cannot encode wide bits at all, so their rows skip
  the check at comptime. That removes the per-cell neighbor traffic from
  all styled text, which decodes through the four-byte width.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.18 ms |  2.06 ms |     2.68 ms |  2.70 ms |
  | styled    |     2.28 ms |  2.41 ms |     6.93 ms |  6.56 ms |
  | truecolor |     4.93 ms |  5.02 ms |    11.91 ms | 11.86 ms |
  | cjk       |     6.11 ms |  6.03 ms |    11.72 ms | 11.60 ms |
  | grapheme  |     8.28 ms |  8.36 ms |    11.38 ms | 11.39 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.3 ms | 25.6 ms |
  | ascii  | decode | 46.7 ms | 48.1 ms |
  | utf8   | encode | 41.0 ms | 41.7 ms |
  | utf8   | decode | 59.5 ms | 58.5 ms |
  ```
- [`47a5182`](https://github.com/ghostty-org/ghostty/commit/47a5182621e324f3351683ca2cc422562b3ff792) terminal/snapshot: skip remap tables for pages without styles ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoding a page allocated and zeroed two full remap tables (a 128 KB
  entries array plus an 8 KB seen bitmap each for styles and hyperlinks)
  even when the page declared no table entries at all, which is every page
  of plain scrollback. Empty tables now use a shared `.empty` remap that
  allocates nothing; `get` reads it as all-unmapped through a length check.
  Pages that do declare entries are unchanged.
  
  (Leaving the entries array unzeroed behind a seen-bitmap-gated `get` was
  also tried and measured no better than the plain memset, so the table
  keeps its simple zero-means-unmapped representation.)
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.06 ms |  2.13 ms |     2.70 ms |  2.54 ms |
  | styled    |     2.41 ms |  2.29 ms |     6.56 ms |  6.75 ms |
  | truecolor |     5.02 ms |  4.95 ms |    11.86 ms | 12.05 ms |
  | cjk       |     6.03 ms |  6.23 ms |    11.60 ms | 11.39 ms |
  | grapheme  |     8.36 ms |  8.72 ms |    11.39 ms | 11.27 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 25.6 ms | 24.4 ms |
  | ascii  | decode | 48.1 ms | 45.1 ms |
  | utf8   | encode | 41.7 ms | 41.9 ms |
  | utf8   | decode | 58.5 ms | 58.6 ms |
  ```
- [`1359973`](https://github.com/ghostty-org/ghostty/commit/1359973aefb37a9beaa2ec3e8f79df78290ea6f5) terminal/snapshot: single-pass style entry codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Style entries went through roughly five writer or reader vtable calls
  each: encode wrote three 4-byte colors and two u16s separately, and
  decode read 16 bytes into a stack buffer only to re-parse it through a
  nested fixed reader, one small read per field. Style-heavy pages carry
  hundreds of entries per page, so encode now assembles each entry in a
  16-byte buffer with a single write, and decode parses the fixed-size
  entry directly from a byte array. Entries additionally parse straight
  from the buffered payload (ID and value together) when it is contiguous.
  
  Inserting a decoded style also hashed twice: an explicit `lookup` before
  `add`, even though `add` already returns the existing entry for repeated
  values. Insert with `add` alone, taking one reference per accepted table
  entry, and surrender those references through the encoded-ID remap after
  grid decoding, the same scheme hyperlink entries already use. Refcount
  outcomes are identical: each distinct style nets its cell references.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.13 ms |  2.12 ms |     2.54 ms |  2.59 ms |
  | styled    |     2.29 ms |  2.23 ms |     6.75 ms |  6.43 ms |
  | truecolor |     4.95 ms |  3.44 ms |    12.05 ms |  8.35 ms |
  | cjk       |     6.23 ms |  5.99 ms |    11.39 ms | 11.39 ms |
  | grapheme  |     8.72 ms |  8.33 ms |    11.27 ms | 10.89 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.4 ms | 24.7 ms |
  | ascii  | decode | 45.1 ms | 47.5 ms |
  | utf8   | encode | 41.9 ms | 41.9 ms |
  | utf8   | decode | 58.6 ms | 58.8 ms |
  ```
- [`eb09bf8`](https://github.com/ghostty-org/ghostty/commit/eb09bf82918de51f22b805dc705ed67b2968b984) terminal/snapshot: interleave software CRC32C streams ([@mitchellh](https://github.com/mitchellh))
  ```text
  Slicing tables removed the byte-at-a-time dependency chain, but each
  16-byte fold still depends serially on the previous one, leaving the
  software CRC latency-bound at roughly 2.5-3 GB/s in V8 while snapshot
  payloads run through it once per direction. wasm has no carry-less
  multiply, so wider tables are the only classic escape — and measuring
  slicing-by-32 against interleaving showed the extra 16 KB of tables buys
  nothing once the chain is hidden.
  
  Instead, inputs of 4 KiB and up split into thirds processed as three
  independent fold chains in one loop, then merge with the GF(2) zero-shift
  operator: crc(A ++ B, s) = crc(B, 0) XOR zeroShift(crc(A, s), |B|). The
  shift matrices are comptime, storing only even powers of two (an odd
  power applies the preceding matrix twice), 4 KB total. Software CRC
  throughput roughly doubles; hardware backends are untouched, so native
  is unaffected (tables below are noise).
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.12 ms |  1.73 ms |     2.59 ms |  2.17 ms |
  | styled    |     2.23 ms |  1.47 ms |     6.43 ms |  5.38 ms |
  | truecolor |     3.44 ms |  2.30 ms |     8.35 ms |  7.17 ms |
  | cjk       |     5.99 ms |  3.89 ms |    11.39 ms |  9.50 ms |
  | grapheme  |     8.33 ms |  6.94 ms |    10.89 ms |  9.24 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.7 ms | 24.8 ms |
  | ascii  | decode | 47.5 ms | 49.2 ms |
  | utf8   | encode | 41.9 ms | 42.4 ms |
  | utf8   | decode | 58.8 ms | 59.5 ms |
  ```
- [`433b16b`](https://github.com/ghostty-org/ghostty/commit/433b16bcb1226a5d840318f88a1fb59e089b0649) terminal/apc: limit glyf decode allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocations made while decoding registered glyf
  outlines to 64 KB.
  
  Carefully crafted glyf outlines could expand into ~768KB of memory per
  glossary entry, which adds up to hundreds of MB per terminal surface.
  Across many terminals this could cause issues.
  
  The 64KB number was chosen by inspecting every glyph across Apple
  symbols and Noto emoji and the largest single glyph found was 40KB. So,
  64KB is generous while limiting each terminal to ~68MB of RAM for max
  glyph glossaries.
  ```
- [`746a11c`](https://github.com/ghostty-org/ghostty/commit/746a11c721a1cf31d2691008340c719bb0a84b03) libghostty: much faster terminal snapshot encode and decode for wasm ([#13848](https://github.com/ghostty-org/ghostty/issues/13848)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Snapshot encode is now 4-7x faster, decode is 3x faster for wasm builds.
  
  Snapshot decode is particularly important for wasm builds because
  libghostty is mainly used on web as a terminal _viewer_ and snapshots
  are the best, most efficient way to ship down full terminal state.
  
  The biggest change here is a totally custom software CRC32
  implementation, which accounted for ~70% of total decode time. Native
  builds on aarch64/x86_64 use dedicated hardware instructions that wasm
  doesn't have. We've written a custom CRC32 impl (verified against Zig
  stdlib through randomized unit tests) that goes from 0.3 GB/s to 5 GB/s
  throughput in V8.
  
  ## Benchmarks
  
  Wasm on V8:
  
  | Workload | Encode Before | Encode After | Speedup | Decode Before |
  Decode After | Speedup |
  |---|---|---|---|---|---|---|
  | ascii | 290 MB/s | 1182 MB/s | 4.1x | 318 MB/s | 946 MB/s | 3.0x |
  | styled (sgr16) | 387 MB/s | 2771 MB/s | 7.2x | 284 MB/s | 758 MB/s |
  2.7x |
  | sgr-truecolor | 361 MB/s | 2382 MB/s | 6.6x | 252 MB/s | 766 MB/s |
  3.0x |
  | cjk | 411 MB/s | 2686 MB/s | 6.5x | 339 MB/s | 1100 MB/s | 3.2x |
  | grapheme | 280 MB/s | 1117 MB/s | 4.0x | 287 MB/s | 839 MB/s | 2.9x |
  
  Native on aarch64:
  
  | Corpus | Mode | Before | After |
  |---|---|---|---|
  | ascii | encode | 40.6 ms | 24.8 ms |
  | ascii | decode | 51.2 ms | 49.2 ms |
  | utf8 | encode | 45.2 ms | 42.4 ms |
  | utf8 | decode | 59.8 ms | 59.5 ms |
  
  **AI usage:** Fable did everything here except write this PR and the
  comments. It also wrote the commit messages in this case. I reviewed
  everything.
  ```
- [`e524df6`](https://github.com/ghostty-org/ghostty/commit/e524df6c829ec11eccc88d1a01e1a7a0416d5454) terminal/apc: limit glyf decode allocations ([#13849](https://github.com/ghostty-org/ghostty/issues/13849)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocations made while decoding registered glyf
  outlines to 64 KB.
  
  Carefully crafted glyf outlines could expand into ~768KB of memory per
  glossary entry, which adds up to hundreds of MB per terminal surface.
  Across many terminals this could cause issues.
  
  The 64KB number was chosen by inspecting every glyph across Apple
  symbols and Noto emoji and the largest single glyph found was 40KB. So,
  64KB is generous while limiting each terminal to ~68MB of RAM for max
  glyph glossaries.
  
  AI was used only to write initial tests, I rewrote em.
  ```
- [`cbe8a0e`](https://github.com/ghostty-org/ghostty/commit/cbe8a0ed4eb27e1530bc8132e52a6c45c135332c) cli: keep cached SSH terminfo installs current ([#13844](https://github.com/ghostty-org/ghostty/issues/13844)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On a local cache miss, always send our embedded terminfo source to the
  remote `tic` instead of accepting any existing entry reported by
  `infocmp`.
  
  We also version cache entries using a content-derived hash of our
  embedded terminfo. Non-matching entries produce a cache miss and trigger
  (re)installation.
  ```
- [`9009122`](https://github.com/ghostty-org/ghostty/commit/9009122953f59d4900143aad587202a70c2136f4) macos: send all `insertText` commits as key events ([#13817](https://github.com/ghostty-org/ghostty/issues/13817)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Partially addresses #13796. Extends #13222.
  
  Previously, `insertText` commits without marked text were delivered via
  `sendText`, which applies paste semantics and wraps the text in
  bracketed
  paste when the program enables it. macOS dictation and other input
  methods often commit without marked text, so programs treated dictated
  text as a paste: opencode collapsed it into a `"[Pasted ~N lines]"` chip
  and Neovim applied paste-mode handling.
  
  `insertText` is only invoked by input methods (IME, dictation, emoji
  picker, character viewer); real paste operations use a separate path.
  Every non-empty commit is now sent as a key event — the same path
  already used for preedit commits since #13222 — so input method text
  always arrives as typed input.
  
  Typing is unaffected (the accumulator path returns earlier) and Cmd+V
  pastes are unaffected. `committedPreeditTextAction` is renamed to
  `committedTextAction` since it no longer only handles preedit commits.
  
  Testing:
  
  - 311 macOS unit tests pass.
  - Manually verified on macOS 26: dictation into Opencode and Neovim
    arrives inline with no paste handling; emoji picker inserts inline;
    Chinese IME composition unchanged; dictation in Neovim normal mode now
    behaves as keystrokes, matching Terminal.app.
  
  Notes:
  
  - Dictated "new line" now matches Terminal.app behavior (no newline
    with typed-text semantics). The previous behavior came from the paste
    path preserving the newline; a follow-up could deliver it as an
    Enter keypress if desired.
  
  AI usage: drafted with OMO + OpenCode + DeepSeek V4 Pro assistance;
  reviewed, edited, and manually tested by the author.
  ```
- [`f2897f3`](https://github.com/ghostty-org/ghostty/commit/f2897f31dec839352302369b3cb8009c4cec180b) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`02436fd`](https://github.com/ghostty-org/ghostty/commit/02436fd4eb0fca179f6d58717e9bc7a0ce106272) Update iTerm2 colorschemes ([#13850](https://github.com/ghostty-org/ghostty/issues/13850)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260810-152212-0173c3c
  ```
- [`b4079f0`](https://github.com/ghostty-org/ghostty/commit/b4079f00c8946207e4db8571e3209f2de7ac4a27) libghostty: add render state structured cursor read ([@mitchellh](https://github.com/mitchellh))
  ```text
  A normal renderer would have to call `ghostty_render_state_get`
  _eight times_ to reconstruct the cursor. In languages where FFI is
  expensive (Go, wasm, etc.), this showed up in profiles of every frame.
  
  Add a sized cursor snapshot and expose it. Also expose the existing color
  snapshot through ghostty_render_state_get and remove the older
  dedicated color getter.
  ```
- [`0d37f2d`](https://github.com/ghostty-org/ghostty/commit/0d37f2d34dabd6bc6f7cf094e0d6466186b8c783) libghostty: add dedicated dirty row iteration + clear functions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add render state C APIs for iterating only rows that require a redraw
  and for marking a completed frame clean in one call.
  
  A one-row update in a 24-row viewport reduces dirty-row discovery from
  50 calls to two, while cleanup becomes one call instead of O(N) of rows.
  
  This lower call count is massive for environments where FFI is expensive
  (Go, wasm).
  
  The dirty next API outputs the viewport y because it jumps, unlike the
  normal sequential next where its trivial for a caller to keep track.
  ```
- [`16c833c`](https://github.com/ghostty-org/ghostty/commit/16c833c5f1ffa9511909199ef1fab389493be1ef) libghostty: add render state structured cursor read ([#13851](https://github.com/ghostty-org/ghostty/issues/13851)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A normal renderer would have to call `ghostty_render_state_get` _eight
  times_ to reconstruct the cursor. In languages where FFI is expensive
  (Go, wasm, etc.), this showed up in profiles of every frame.
  
  Add a sized cursor snapshot and expose it. Also expose the existing
  color snapshot through ghostty_render_state_get and remove the older
  dedicated color getter.
  
  Found during my normal Go/wasm adventures.
  ```
- [`ad6e72d`](https://github.com/ghostty-org/ghostty/commit/ad6e72ddc4e9e259c9b70bff6e2b389e0ce91949) libghostty: add dedicated dirty row iteration + clear functions ([#13852](https://github.com/ghostty-org/ghostty/issues/13852)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add render state C APIs for iterating only rows that require a redraw
  and for marking a completed frame clean in one call.
  
  A one-row update in a 24-row viewport reduces dirty-row discovery from
  50 calls to two, while cleanup becomes one call instead of O(N) of rows.
  
  This lower call count is massive for environments where FFI is expensive
  (Go, wasm).
  
  The dirty next API outputs the viewport y because it jumps, unlike the
  normal sequential next where its trivial for a caller to keep track.
  ```
- [`9673a22`](https://github.com/ghostty-org/ghostty/commit/9673a22b01317ac6493240694a2451c8287253d1) libghostty: expand ABI type metadata ([@mitchellh](https://github.com/mitchellh))
  ```text
  The type metadata export only described extern struct layouts, leaving embedders to mirror enum values and tagged union relationships.
  
  Describe every public C type in a versioned manifest with target and build metadata. Keep union field renames alongside their source tagged unions so the manifest uses public C names without changing Zig value layouts.
  ```
- [`c755595`](https://github.com/ghostty-org/ghostty/commit/c75559589e41721ab5a3de8e336d8476f4290535) libghostty: add ABI manifest schema ([@mitchellh](https://github.com/mitchellh))
  ```text
  The ABI manifest previously had no machine-readable grammar or test that
  the public export conformed to it.
  
  Define a Draft 2020-12 schema and add a build check that executes
  ghostty_type_json for native and wasm libraries before validation. Run
  both forms in CI and publish the schema with the generated API docs.
  ```
- [`0e8b7be`](https://github.com/ghostty-org/ghostty/commit/0e8b7bea63ccf8b89d15a82bdaf6a9bb3fc8c43d) vt: expose packed cell layout ([@mitchellh](https://github.com/mitchellh))
  ```text
  GhosttyCell was exposed as a raw integer while its manifest entry was only an alias, forcing bulk-read consumers to duplicate the internal cell bit layout.\n\nAdd reflection helpers for packed structs and tagged unions, and keep the C-facing layout metadata next to Cell itself. Extend the ABI manifest and schema with recursive bit descriptors so every content arm, including palette and RGB backgrounds, can be decoded without hardcoded masks.\n\nDocument manifest-driven cell decoding and test the metadata against Zig reflection and real cell values.
  ```
- [`37174c7`](https://github.com/ghostty-org/ghostty/commit/37174c73b0600cc3b2d8579fa7a210086ee3bbed) add helper and expand also if light/dark is specified ([@preiter93](https://github.com/preiter93))
- [`26df373`](https://github.com/ghostty-org/ghostty/commit/26df373ec83fb1cebb4fee0a8394144ae984a9b8) i18n: update Hebrew translations for v1.4 ([#13785](https://github.com/ghostty-org/ghostty/issues/13785)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update the Hebrew translations in po/he.po with the 181 new strings for
  v1.4, as requested in issue #13766 :)
  ```
- [`0ba6250`](https://github.com/ghostty-org/ghostty/commit/0ba6250388641f52135414b38c4259aa682c489b) libghostty: `ghostty_type_json` expanded with more metadata, every enum member, packed layouts, etc. ([#13856](https://github.com/ghostty-org/ghostty/issues/13856)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This PR makes `ghostty_type_json` contain more metadata necessary for
  FFI without access to the C header to produce safe, ABI compliant field
  access.
  
  The existing `ghostty_type_json` didn't expose enough information:
  embedders still had to hardcode enum values, tagged union values, and
  packed bit layouts. For wasm this meant copying offsets and masks from
  Zig internals and hoping they didn't drift. This isn't an ABI I want to
  promise.
  
  This also includes a formal JSON schema included in Doxygen docs and
  used in CI to continuously validate our output structure. I'd like to
  expand in the future comparing to actual C headers too.
  
  ## Examples
  
  ### Named References, Arrays
  
  ```json
  "GhosttyRenderStateColors": {
    "kind": "struct",
    "size": 792,
    "align": 8,
    "fields": {
      "background": {
        "offset": 8,
        "size": 3,
        "type": "GhosttyColorRgb"
      },
      "palette": {
        "offset": 18,
        "size": 768,
        "type": "array",
        "elem": "GhosttyColorRgb",
        "count": 256
      }
    }
  }
  ```
  
  ### Pointers
  
  ```json
  "GhosttyCellsView": {
    "kind": "struct",
    "size": 16,
    "align": 8,
    "fields": {
      "ptr": {
        "offset": 0,
        "size": 8,
        "type": "pointer",
        "elem": "GhosttyCell",
        "const": true,
        "nullable": true
      },
      "len": {
        "offset": 8,
        "size": 8,
        "type": "u64"
      }
    }
  }
  ```
  
  ### Enums
  
  ```json
  "GhosttyStyleColorTag": {
    "kind": "enum",
    "size": 4,
    "align": 4,
    "underlying": "i32",
    "prefix": "GHOSTTY_STYLE_COLOR_",
    "values": {
      "NONE": 0,
      "PALETTE": 1,
      "RGB": 2,
      "TAG_MAX_VALUE": 2147483647
    }
  }
  ```
  
  ### Packed Struct
  
  ```json
  "GhosttyCell": {
    "kind": "packed",
    "size": 8,
    "align": 8,
    "underlying": "u64",
    "bits": {
      "content_tag": {
        "lsb": 0,
        "width": 2,
        "type": "GhosttyCellContentTag"
      },
      "content": {
        "lsb": 2,
        "width": 24,
        "kind": "union",
        "tag": "content_tag",
        "arms": {
          "BG_COLOR_RGB": {
            "kind": "packed",
            "width": 24,
            "bits": {
              "r": {"lsb": 0, "width": 8, "type": "u8"},
              "g": {"lsb": 8, "width": 8, "type": "u8"},
              "b": {"lsb": 16, "width": 8, "type": "u8"}
            }
          }
        }
      }
    }
  }
  ```
  ````
- [`68a2008`](https://github.com/ghostty-org/ghostty/commit/68a2008b340959b2a94f27f37ca98257109f6396) fix: format ([@preiter93](https://github.com/preiter93))
- [`bd64703`](https://github.com/ghostty-org/ghostty/commit/bd647035e97da4aadfe1003877ecf64a3a655059) input: don't emit fallback text on key release ([@tsacha](https://github.com/tsacha))
  ```text
  Key events without a kitty entry fall back to writing their UTF-8 text
  directly. On GTK, keys whose unshifted keysym is a dead key or level 5
  latch have no unshifted codepoint and take this path. With event type
  reporting enabled, releases therefore emitted the same text as presses
  and duplicated characters in applications such as Neovim.
  
  Skip the raw text fallback for release events while retaining it for
  presses and repeats. Keep the guard in the shared encoder so release
  events for identified keys still retain the UTF-8 data used to derive
  alternate keys.
  
  Cover releases with and without report-all mode, and verify that repeat
  events continue to emit fallback text.
  ```
- [`7b57c0a`](https://github.com/ghostty-org/ghostty/commit/7b57c0a02942beb3217a751e6d26955e3c3c1d72) Update VOUCHED list ([#13859](https://github.com/ghostty-org/ghostty/issues/13859)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13858#discussioncomment-18043290)
  from @jcollie.
  
  Vouch: @tsacha
  ```
- [`a8e9b41`](https://github.com/ghostty-org/ghostty/commit/a8e9b413f13cfeec77efd95c3ba9b4750fcbfada) libghostty: simplify Wasm allocation API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace a bunch of type-specific Wasm allocation functions with a generic
  byte allocator and reusable opaque out-parameters for pointers. This
  makes it a lot more ergonomic (relatively) to use the Wasm interface
  and removes a dozen or so exports.
  
  This also updates the `ghostty_type_json` `abi` field with a maximum
  alignment value that host sides can use to keep every allocation aligned
  properly, easily, without hardcoding numbers.
  
  This adds a test to verify this all works as intended and runs in CI.
  ```
- [`3790fb7`](https://github.com/ghostty-org/ghostty/commit/3790fb78fecb3577dee30c40efe1ced3e3f0d9a1) libghostty: simplify Wasm allocation API ([#13860](https://github.com/ghostty-org/ghostty/issues/13860)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace a bunch of type-specific Wasm allocation functions with a
  generic byte allocator and reusable opaque out-parameters for pointers.
  This makes it a lot more ergonomic (relatively) to use the Wasm
  interface and removes a dozen or so exports.
  
  This also updates the `ghostty_type_json` `abi` field with a maximum
  alignment value that host sides can use to keep every allocation aligned
  properly, easily, without hardcoding numbers.
  
  This adds a test to verify this all works as intended and runs in CI.
  ```
- [`7557944`](https://github.com/ghostty-org/ghostty/commit/7557944b4f1fb9eebe451c636227a04e7a4a2704) feat: expand tildes in config theme path to HOME ([#13840](https://github.com/ghostty-org/ghostty/issues/13840)) ([@jcollie](https://github.com/jcollie))
  ````text
  When loading a theme from a path that includes a tilde:
  ```
  theme="~/.cache/wal/colors-ghostty"
  ```
  ghostty currently fails with the following error:
  ```
  cannot include path separators unless it is an absolute path
  ```
  
  This PR tries to expand the ~ of the path. If there is no ~ or expansion
  fails, it falls back to the unexpanded value.
  ````
- [`29b82dd`](https://github.com/ghostty-org/ghostty/commit/29b82dd80c46de16f5aaa405e51b2148831e2061) config: preserve bytes in hex escapes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13855
  
  Make the config string parser preserve hexadecimal escapes as bytes.
  Previously all escaped values were encoded as Unicode codepoints.
  ```
- [`f8856a7`](https://github.com/ghostty-org/ghostty/commit/f8856a78a291193fbfab081a894d16fc21f4a42e) config: preserve bytes in hex escapes ([#13862](https://github.com/ghostty-org/ghostty/issues/13862)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13855
  
  Make the config string parser preserve hexadecimal escapes as bytes.
  Previously all escaped values were encoded as Unicode codepoints.
  ```
- [`602497e`](https://github.com/ghostty-org/ghostty/commit/602497e9b96c62b05c4c6418538192ad974e4326) input: skip text fallback for kitty key releases ([#13861](https://github.com/ghostty-org/ghostty/issues/13861)) ([@jcollie](https://github.com/jcollie))
  ```text
  Key events without a kitty entry fall back to writing their UTF-8 text
  directly. On GTK, keys whose unshifted keysym is a dead key or level 5
  latch have no unshifted codepoint and take this path. With event type
  reporting enabled, releases therefore emitted the same text as presses
  and duplicated characters in applications such as Neovim.
  
  Skip the raw text fallback for release events while retaining it for
  presses and repeats. Keep the guard in the shared encoder so release
  events for identified keys still retain the UTF-8 data used to derive
  alternate keys.
  
  Cover releases with and without report-all mode, and verify that repeat
  events continue to emit fallback text.
  
    - https://github.com/ghostty-org/ghostty/discussions/12192
    - https://github.com/ghostty-org/ghostty/discussions/12084
    - https://github.com/ghostty-org/ghostty/discussions/12433
    - https://github.com/ghostty-org/ghostty/discussions/13816
  
  ## Testing
  
    - `zig build test-lib-vt -Dtarget=x86_64-linux-gnu`
    - `zig build -Demit-lib-vt -Dtarget=x86_64-linux-gnu`
    - `zig build`
    - Verified the regression test fails without the release guard
  - Manually tested the GTK backend under Wayland/Sway and X11/XWayland,
  with the GTK simple input context and ibus 1.5.34:
      - Ergo-L `!` and `'`
      - Spanish `[`, `{`, `]`, and `}`
  - Presses, repeats, and both modifier-release orders in `nvim --clean`
      - Dead-key composition and cancellation
      - Unicode hexadecimal input
  - Full kitty keyboard mode with `kitty +kitten show_key -m kitty`,
  including composed text
  
  ## AI disclosure
  
  OpenAI Codex assisted with investigating the reports, reviewing the GTK
  and kitty input paths, extending the regression tests, running
  validation, and drafting this description. I reviewed the final code,
  edited this description, manually performed the tests listed above, and
  understand how the change interacts with the input encoder.
  ```
- [`820ed68`](https://github.com/ghostty-org/ghostty/commit/820ed688efa5b914c2779449f260d369caca0b2c) i18n(be): fix translation issues per review ([@iweuhi2kjrnkw](https://github.com/iweuhi2kjrnkw))
  ```text
  - Drop redundant 'было' copula with short-form participles (lines 1767, 1769)
  - Use short predicative form 'недаступна' (line 1780)
  - 'у двух фарматах:' instead of dash-construction (line 156)
  - 'Аднавіць' instead of 'Паўтарыць' for Redo (semantic pair with Undo)
  - Fix 'у' → 'ў' after 'ANSI' (7 places)
  - Align label/description wording for Split Zoom, Read-Only, Float on Top, Secure Input
  - 'усе акны' instead of 'усе вокны' (consistent with 'акно')
  - 'калі яна ёсць' instead of 'даступная' (if present ≠ available)
  - Infinitive 'Дадаць' instead of imperative 'Дадайце'
  ```
- [`7a96643`](https://github.com/ghostty-org/ghostty/commit/7a966438fcf5b3b209bb754b67155d34ae93b217) build(deps): bump cachix/install-nix-action from 31.11.0 to 31.11.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.0 to 31.11.1.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/630ae543ea3a38a9a4166f03376c02c50f408342...13d8dd58da0234aa297dedd986986ccb8e7f3e24)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`9a770be`](https://github.com/ghostty-org/ghostty/commit/9a770be61c39757cdb1a0d7670b8265100d3b2a6) build(deps): bump cachix/install-nix-action from 31.11.0 to 31.11.1 ([#13863](https://github.com/ghostty-org/ghostty/issues/13863)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.0 to 31.11.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.1 -&gt; 2.35.2 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/281">cachix/install-nix-action#281</a>
  Fixes a crash (<a
  href="https://redirect.github.com/NixOS/nix/issues/16005"><code>Assertion
  '!awake.empty()' failed</code></a>) that could abort builds.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.0...v31.11.1">https://github.com/cachix/install-nix-action/compare/v31.11.0...v31.11.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/13d8dd58da0234aa297dedd986986ccb8e7f3e24"><code>13d8dd5</code></a>
  fix(ci): skip latest installer on x86_64-darwin</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/875018fe555aee647c21ea81888659240cd8e27b"><code>875018f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/281">#281</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/6624a11f6c07674a3ff71d2431865aecf3587190"><code>6624a11</code></a>
  nix: 2.35.1 -&gt; 2.35.2</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/630ae543ea3a38a9a4166f03376c02c50f408342...13d8dd58da0234aa297dedd986986ccb8e7f3e24">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.0&new-version=31.11.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`5364e51`](https://github.com/ghostty-org/ghostty/commit/5364e5158f171e4d87fdfa43d0fffebc0c3775fa) libghostty: reduce Wasm stack reservation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig default's Wasm stacks to 1MB. Change it to 128 KB instead.
  
  This removes 896 KiB from every Wasm instance's initial linear memory
  reservation. That means that simply _loading_ `ghostty-vt.wasm` is down
  this much.
  
  Through various workload benchmarks of real terminal snapshots,
  artificial worst case full ascii, full styled, full emoji, full mixed,
  etc. workloads, I wasn't able to get a stack to go above 17 KB, so 128 KB
  is VERY generous. Lets start here.
  ```
- [`8d70c5d`](https://github.com/ghostty-org/ghostty/commit/8d70c5dca0346dcba94f8812547ff325e62bc340) libghostty: reduce Wasm stack reservation ([#13864](https://github.com/ghostty-org/ghostty/issues/13864)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig default's Wasm stacks to 1MB. Change it to 128 KB instead.
  
  This removes 896 KiB from every Wasm instance's initial linear memory
  reservation. That means that simply _loading_ `ghostty-vt.wasm` is down
  this much.
  
  Through various workload benchmarks of real terminal snapshots,
  artificial worst case full ascii, full styled, full emoji, full mixed,
  etc. workloads, I wasn't able to get a stack to go above 17 KB, so 128
  KB is VERY generous. Lets start here.
  ```
- [`492c260`](https://github.com/ghostty-org/ghostty/commit/492c26067c9f342f46507ade392cfad2e1400360) libghostty: use custom memory pool for Wasm ([@mitchellh](https://github.com/mitchellh))
  ```text
  A custom memory pool for Wasm that grows by exactly one item size per
  growth and shares the pool across the entire Wasm-module instead of
  per-terminal.
  
  Some background on why `std.heap.MemoryPool` is considered harmful for
  WebAssembly:
  
  First, the std.heap.MemoryPool grows 1.5x at each growth point. The backing
  allocator for that is usually a GPA which is the BrkAllocator for wasm.
  This grows by power-of-two big-allocation slots. If you pair these together
  you get a massive permanent linear memory growth. On non-wasm targets,
  this doesn't matter because these are virtual memory mappings that don't
  cost physical memory, but wasm doesn't work that way.
  
  Second, we were using one pool per terminal. On wasm, this meant that
  we paid for the free list N times. On non-wasm, this makes sense because
  the synchronization overhead has so far been measurable enough under
  load to be prohibitive (although, I'm still skeptical about this and want
  to look into it). On wasm, we build single-threaded modules, so we can use
  a global free list without any extra overhead.
  
  ## Benchmarks
  
  80x24 terminal with 1000-line scrollack processing 16MB of plain ASCII.
  
  | Scenario                        |    Before |     After |
  | ------------------------------- | --------: | --------: |
  | Fresh instance                  |  0.56 MiB |  0.56 MiB |
  | First `terminal_new` (delta)    | +3.44 MiB | +0.88 MiB |
  | One filled terminal (total)     |  4.00 MiB |  1.88 MiB |
  | Each additional filled terminal | +3.00 MiB | +0.44 MiB |
  | 5 filled terminals (total)      | 16.00 MiB |  4.06 MiB |
  
  Throughput numbers are unchanged on wasm and native (to be expected in
  the latter because this is all gated on wasm).
  ```
- [`e9db8d2`](https://github.com/ghostty-org/ghostty/commit/e9db8d2b0b827be035ab75658ea9faf4f0f56d3f) libghostty: use custom memory pool for Wasm, reduce terminal memory by ~75% ([#13865](https://github.com/ghostty-org/ghostty/issues/13865)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A custom memory pool for Wasm that grows by exactly one item size per
  growth and shares the pool across the entire Wasm-module instead of
  per-terminal.
  
  Some background on why `std.heap.MemoryPool` is considered harmful for
  WebAssembly:
  
  First, the std.heap.MemoryPool grows 1.5x at each growth point. The
  backing allocator for that is usually a GPA which is the BrkAllocator
  for wasm. This grows by power-of-two big-allocation slots. If you pair
  these together you get a massive permanent linear memory growth.
  
  On non-wasm targets, the memory growth doesn't matter because these are
  virtual memory mappings that don't cost physical memory, but wasm
  doesn't work that way. Also on native targets, the syscalls to allocate
  memory are very expensive (relatively), so it makes sense to allocate
  large virtual memory chunks and avoid them. Again, wasm doesn't work
  this way.
  
  Second, we were using one pool per terminal. On wasm, this meant that we
  paid for the free list N times. On non-wasm, this makes sense because
  the synchronization overhead has so far been measurable enough under
  load to be prohibitive (although, I'm still skeptical about this and
  want to look into it). On wasm, we build single-threaded modules, so we
  can use a global free list without any extra overhead.
  
  ## Benchmarks
  
  80x24 terminal with 1000-line scrollack processing 16MB of plain ASCII.
  
  | Scenario                        |    Before |     After |
  | ------------------------------- | --------: | --------: |
  | Fresh instance                  |  0.56 MiB |  0.56 MiB |
  | First `terminal_new` (delta)    | +3.44 MiB | +0.88 MiB |
  | One filled terminal (total)     |  4.00 MiB |  1.88 MiB |
  | Each additional filled terminal | +3.00 MiB | +0.44 MiB |
  | 5 filled terminals (total)      | 16.00 MiB |  4.06 MiB |
  
  Throughput numbers are unchanged on wasm and native (to be expected in
  the latter because this is all gated on
  wasm).
  
  Note I'm still very much optimizing the above numbers! This is just my
  first big win.
  
  **AI usage:** None used except to validate and judge.
  ```
- [`b97b17f`](https://github.com/ghostty-org/ghostty/commit/b97b17f06b1ffd694f80edd3df5dd2134a0bcb9e) i18n: translate v1.4 strings (be) ([#13771](https://github.com/ghostty-org/ghostty/issues/13771)) ([@trag1c](https://github.com/trag1c))
  ```text
  Continues the Belarusian (`be`) translation for v1.4 per #13766.
  Translates the remaining 181 strings (mostly the newly-localized command
  palette), bringing `be` to 253/253.
  ```
- [`3924a32`](https://github.com/ghostty-org/ghostty/commit/3924a3255686b2b646d2ee8730ad5528f4542a26) Update VOUCHED list ([#13870](https://github.com/ghostty-org/ghostty/issues/13870)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13838#discussioncomment-18052745)
  from @mitchellh.
  
  Vouch: @basteez
  ```
- [`f430905`](https://github.com/ghostty-org/ghostty/commit/f4309055fbb8cfd74bf0559a054e5eb7ddc361d8) macos: don't put 0x7F as text in key event ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13869
  
  We already checked `< 0x20` but missed `0x7F` which causes similar
  problems.
  ```
- [`6c30dc1`](https://github.com/ghostty-org/ghostty/commit/6c30dc1bfff7e22a9198931411ae862a6bb6277b) i18n: Update ko_KR translations ([#13815](https://github.com/ghostty-org/ghostty/issues/13815)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update all missing Korean translations for 1.4.
  
  Part of #13766
  ```
- [`2349e97`](https://github.com/ghostty-org/ghostty/commit/2349e974b866ae4d9a8c5193a885388ddd4f2b4b) inspector: remove obsolete detachable header helper ([@jparise](https://github.com/jparise))
  ```text
  Remove the unused, callback-based detachable header implementation. It
  supported the previous terminal inspector, which has since been deleted
  (fdbe4343c). The current inspector uses DetachableHeader directly.
  ```
- [`d19f8f7`](https://github.com/ghostty-org/ghostty/commit/d19f8f7f9d3204d37fd1c47f9b51f682238a8423) macos: remove unused hosting window helper ([@jparise](https://github.com/jparise))
  ```text
  Remove the unused SwiftUI environment key intended to expose a hosting
  window. Nothing sets or reads the value.
  ```
- [`c8980b8`](https://github.com/ghostty-org/ghostty/commit/c8980b853b5e822509946c7c62188fe549731376) macos: don't put 0x7F as text in key event ([#13871](https://github.com/ghostty-org/ghostty/issues/13871)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13869
  
  We already checked `< 0x20` but missed `0x7F` which causes similar
  problems.
  ```
- [`924c8a9`](https://github.com/ghostty-org/ghostty/commit/924c8a90ded98fb643def9d7b814efa55e590298) libghostty: C api to stream formatter output through a GhosttyWriter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `ghostty_formatter_format` which uses a streaming GhosttyWriter
  type to write. Update the example to show this.
  ```
- [`0baa0fd`](https://github.com/ghostty-org/ghostty/commit/0baa0fd545365d388922d37370c4da2412aa4ace) inspector: remove obsolete detachable header helper ([#13874](https://github.com/ghostty-org/ghostty/issues/13874)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the unused, callback-based detachable header implementation. It
  supported the previous terminal inspector, which has since been deleted
  (fdbe4343c). The current inspector uses DetachableHeader directly.
  ```
- [`faaf07e`](https://github.com/ghostty-org/ghostty/commit/faaf07e7c001e24e0bd725cc1bb3cb899815d53b) macos: remove unused hosting window helper ([#13873](https://github.com/ghostty-org/ghostty/issues/13873)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the unused SwiftUI environment key intended to expose a hosting
  window. Nothing sets or reads the value.
  ```
- [`ee57b94`](https://github.com/ghostty-org/ghostty/commit/ee57b94170ab5261315cb9345eb67663e8d1908c) libghostty: C api to stream formatter output through a GhosttyWriter ([#13875](https://github.com/ghostty-org/ghostty/issues/13875)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `ghostty_formatter_format` which uses a streaming GhosttyWriter type
  to write. Update the example to show this.
  ```
- [`5c952ac`](https://github.com/ghostty-org/ghostty/commit/5c952ac977b30f3e4e01417827d4d7745015f50c) macos: simplify command palette sort keys ([@jparise](https://github.com/jparise))
  ```text
  Store the Comparable ObjectIdentifier directly instead of wrapping the
  only sort key type in AnySortKey.
  
  The expected deterministic ordering of equal terminal command titles is
  also now verified by a unit test.
  ```
- [`997a2af`](https://github.com/ghostty-org/ghostty/commit/997a2aff2afce88cdf5fa7a3d5dca047c0d65254) terminal: preserve pending wrap in VT formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, formatting a cursor at the right edge emitted CUP, which
  cleared pending wrap. Replayed output then overwrote the edge cell
  instead of wrapping before the next printable character.
  
  When pending wrap is set, move to and reformat the final cell to restore
  the flag through normal VT behavior. Emit cursor pen state afterward and
  cover replay plus pin-map behavior with a regression test.
  ```
- [`0073976`](https://github.com/ghostty-org/ghostty/commit/00739762316a0ad05c7d412705b5f6111bae3288) terminal: preserve pending wrap in VT formatter ([#13876](https://github.com/ghostty-org/ghostty/issues/13876)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, formatting a cursor at the right edge emitted CUP, which
  cleared pending wrap. Replayed output then overwrote the edge cell
  instead of wrapping before the next printable character.
  
  When pending wrap is set, move to and reformat the final cell to restore
  the flag through normal VT behavior. Emit cursor pen state afterward and
  cover replay plus pin-map behavior with a regression test.
  ```
- [`4816afc`](https://github.com/ghostty-org/ghostty/commit/4816afc74201c4a8170223fb43e7e6fdbaa34a0a) macos: simplify command palette sort keys ([#13872](https://github.com/ghostty-org/ghostty/issues/13872)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Store the Comparable ObjectIdentifier directly instead of wrapping the
  only sort key type in AnySortKey.
  
  The expected deterministic ordering of equal terminal command titles is
  also now verified by a unit test.
  ```
- [`385a378`](https://github.com/ghostty-org/ghostty/commit/385a378fe58425482eb1df8ed614433e06b891de) termio: preserve UTF-8 in desktop notification truncation ([#13811](https://github.com/ghostty-org/ghostty/issues/13811)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - Prevent desktop notification title and body truncation from producing
  invalid UTF-8.
  - Truncate fixed-size buffers to the longest valid UTF-8 prefix.
  - Add regression tests for multibyte characters at the buffer boundary.
  
  Fixes #13795
  
  ## Testing
  
  - Confirmed the original reproducer produces `[Invalid UTF-8]` with the
  installed Ghostty.
  - Confirmed the patched Ghostty displays a valid, truncated
  notification.
  - Added tests covering both notification title and body truncation.
  
  ## AI Usage Disclosure
  
  I used OpenAI Codex to investigate the root cause, implement the fix and
  regression tests, run validation, and help prepare the issue and PR
  descriptions. I reviewed and understand the submitted change.
  ```
- [`159cf6d`](https://github.com/ghostty-org/ghostty/commit/159cf6d7e7fef0f477d400c3f801b9f02dbcfd19) pkg/wuffs: use C-only mirror of wuffs ([#13789](https://github.com/ghostty-org/ghostty/issues/13789)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prevents us from pulling in test images that trigger some
  anti-virus scanners. It's also smaller since it only has the necessary
  bits that we need.
  
  This also updates to the latest release: 0.4.0-alpha.10.
  ```
- [`846d24e`](https://github.com/ghostty-org/ghostty/commit/846d24e12b3bc12c5623cabf311f3e8c13621ea4) libghostty: buffer the writer adapter used by streaming C APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyWriter adapter was unbuffered, so for streaming writers that
  make small writes like the formatter, it produces a crazy amount of callbacks:
  one styled HTML page invoked the callback ~50,000 times in a benchmark lol.
  
  Change WriterAdapter to have an optional buffer (initBuffered) and use
  a 4 KB buffer for all current callers. Also optimize single byte splats
  to use memset.
  
  Results: that same styled HTML example goes from ~50K callbacks to 124.
  And throughput through the C API also improved across every workload
  I tested (styled and unstyled text in every format).
  ```
- [`56e1f3a`](https://github.com/ghostty-org/ghostty/commit/56e1f3a62e26407e8c020ef5881df3e8584be20f) libghostty: buffer the writer adapter used by streaming C APIs ([#13877](https://github.com/ghostty-org/ghostty/issues/13877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyWriter adapter was unbuffered, so for streaming writers that
  make small writes like the formatter, it produces a crazy amount of
  callbacks: one styled HTML page invoked the callback ~50,000 times in a
  benchmark lol. This has a particularly large impact on callers who are
  supplying callbacks through an expensive FFI interface, like Go.
  
  Change WriterAdapter to have an optional buffer (initBuffered) and use a
  4 KB buffer for all current callers. Also optimize single byte splats to
  use memset.
  
  Results: that same styled HTML example goes from ~50K callbacks to 124.
  And throughput through the C API also improved across every workload I
  tested (styled and unstyled text in every format).
  ```
- [`9be6c2e`](https://github.com/ghostty-org/ghostty/commit/9be6c2ea2870f409f3e73337f3f5ac74db806ba3) libghostty: option to retain continuations on snapshot decode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a snapshot decoder option that leaves continuation tracking
  enabled on decoded terminals. This lets caller access the continuation
  bytes (if any) that were applied to the terminal.
  
  This lets replay callers export an unfinished parser or UTF-8 sequence
  from the returned terminal.
  
  This defaults to off.
  ```
- [`12967b6`](https://github.com/ghostty-org/ghostty/commit/12967b68f7d46bdbfb2cfffb6768332fb9db68c0) libghostty: option to retain continuations on snapshot decode ([#13878](https://github.com/ghostty-org/ghostty/issues/13878)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a snapshot decoder option that leaves continuation tracking enabled
  on decoded terminals. This lets caller access the continuation bytes (if
  any) that were applied to the terminal.
  
  This lets replay callers export an unfinished parser or UTF-8 sequence
  from the returned terminal.
  
  This defaults to off.
  ```
- [`07af461`](https://github.com/ghostty-org/ghostty/commit/07af4612ba17afe13fcba1de8d8a1258bc666a10) terminal: report size when mode 2048 is enabled ([@elias8](https://github.com/elias8))
- [`5b9a77f`](https://github.com/ghostty-org/ghostty/commit/5b9a77f203865e73de885df743afc73af96fba50) terminal: document mode 2048 size reports ([@elias8](https://github.com/elias8))
- [`0a16db3`](https://github.com/ghostty-org/ghostty/commit/0a16db3c686045fe5ac8a58d3c91dc53d108e662) fix(lib-vt): report size when mode 2048 is enabled ([#13885](https://github.com/ghostty-org/ghostty/issues/13885)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Mode 2048 requires terminals to report the current rows, columns, and
  pixel dimensions [when the mode is
  enabled](https://gist.github.com/rockorager/e695fb2924d36b2bcf1fff4a3704bd83#:~:text=When%20first%20enabled%2C%20the%20terminal%20MUST%20send%20a%20report%20of%20the%20current%20size.),
  then report updated geometry after later resizes. The native termio
  stream already queues the initial report, but the terminal stream only
  reported from `resize`, so libghostty consumers that enabled the mode
  after committing geometry received nothing until another resize.
  
  This makes the generic handler match termio by requesting current
  geometry through the existing size callback and writing the encoded
  report through `write_pty` on every enable.
  ```
- [`afb61e1`](https://github.com/ghostty-org/ghostty/commit/afb61e1b6292f56b863ad0fe61bcdbad47392a5e) terminal/kitty: place cursor after tall images properly ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #13886
  
  This fixes an incompatibility between Ghostty and Kitty 0.47.1+.
  
  Previously, Ghostty handled `C=0` by moving down at most one terminal
  height and then clamping the horizontal destination to the screen. The
  limit protected against an image command requesting billions of rows,
  but it counted ordinary movement to the bottom as well as scrolling.
  
  Kitty defines `C=0` as leaving the cursor after the image and implements
  the movement as rows minus one, plus one row when the image reaches the
  right edge:
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1256-L1260
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L1903-L1915
  
  (Had to view Kitty source to verify what the spec meant)
  
  For example, an eight-row, full-width image in a five-row terminal needs
  four moves to reach the bottom and four more to scroll. The old limit
  allowed only five moves in total, so the next image started four rows
  inside the first one. Clamping the horizontal destination also left the
  cursor at the final column instead of wrapping to column one of the next
  row. Consecutive images could therefore overlap in both directions.
  ```
- [`d4d72f3`](https://github.com/ghostty-org/ghostty/commit/d4d72f3205f7a995fa4578f4b5369937f0b17a18) terminal/kitty: place cursor after tall images properly ([#13887](https://github.com/ghostty-org/ghostty/issues/13887)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #13886
  
  This fixes an incompatibility between Ghostty and Kitty 0.47.1+.
  
  Previously, Ghostty handled `C=0` by moving down at most one terminal
  height and then clamping the horizontal destination to the screen. The
  limit protected against an image command requesting billions of rows,
  but it counted ordinary movement to the bottom as well as scrolling.
  
  Kitty defines `C=0` as leaving the cursor after the image and implements
  the movement as rows minus one, plus one row when the image reaches the
  right edge:
  
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1256-L1260
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L1903-L1915
  
  (Had to view Kitty source to verify what the spec meant)
  
  For example, an eight-row, full-width image in a five-row terminal needs
  four moves to reach the bottom and four more to scroll. The old limit
  allowed only five moves in total, so the next image started four rows
  inside the first one. Clamping the horizontal destination also left the
  cursor at the final column instead of wrapping to column one of the next
  row. Consecutive images could therefore overlap in both directions.
  ```
- [`83145c0`](https://github.com/ghostty-org/ghostty/commit/83145c0a374852b6c1c2b6e7eab94b4db63c10f7) terminal/kitty: reject conflicting image identifiers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reject Kitty graphics commands that specify both an image ID and an
  image number across every protocol action.
  
  These commands previously produced no wire response for transmissions,
  while put and delete actions could proceed using one identifier and
  mutate terminal state.
  
  Retain the original command identifiers, validate them before action
  dispatch, and preserve them in the EINVAL response. Add regression
  coverage for every action, response encoding, quiet suppression, and
  pre-mutation rejection.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal
  ```
- [`52190a5`](https://github.com/ghostty-org/ghostty/commit/52190a5d8da4e21e628bb01f12f32da7b06b3a54) terminal/kitty: intersect source rectangles before sizing ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics placements previously calculated pixel and grid geometry
  from requested source dimensions before intersecting them with the image.
  The renderer clamped explicit dimensions later but treated omitted
  source dimensions as the full image.
  
  This stretched clipped crops into incorrectly sized destinations and
  exposed inconsistent geometry through storage, rendering, and
  libghostty.
  
  Resolve the source rectangle once against the image bounds and reuse it
  for placement sizing, renderer preparation, and the C API. Add
  regression tests for omitted and explicit dimensions and renderer
  geometry.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  Reference: https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1225-L1240
  ```
- [`409e682`](https://github.com/ghostty-org/ghostty/commit/409e682c832198be782071c7b6c182c29227d3aa) terminal/kitty: reject conflicting image identifiers ([#13889](https://github.com/ghostty-org/ghostty/issues/13889)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reject Kitty graphics commands that specify both an image ID and an
  image number across every protocol action.
  
  These commands previously produced no wire response for transmissions,
  while put and delete actions could proceed using one identifier and
  mutate terminal state.
  
  Retain the original command identifiers, validate them before action
  dispatch, and preserve them in the EINVAL response. Add regression
  coverage for every action, response encoding, quiet suppression, and
  pre-mutation rejection.
  
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal
  ```
- [`9848cb1`](https://github.com/ghostty-org/ghostty/commit/9848cb15fae7eb6abfc74d563ff98b24c830900f) terminal/kitty: intersect source rectangles before sizing ([#13890](https://github.com/ghostty-org/ghostty/issues/13890)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics placements previously calculated pixel and grid geometry
  from requested source dimensions before intersecting them with the
  image. The renderer clamped explicit dimensions later but treated
  omitted source dimensions as the full image.
  
  This stretched clipped crops into incorrectly sized destinations and
  exposed inconsistent geometry through storage, rendering, and
  libghostty.
  
  Resolve the source rectangle once against the image bounds and reuse it
  for placement sizing, renderer preparation, and the C API. Add
  regression tests for omitted and explicit dimensions and renderer
  geometry.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  Reference:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1225-L1240
  ```
- [`c5a3c7e`](https://github.com/ghostty-org/ghostty/commit/c5a3c7e2e5b4e39ce59c14cb35c55be971058575) terminal/kitty: constrain placement offsets to cell bounds ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clamp X and Y offsets when a placement is created and normalize them
  again against current cell geometry when sizing and rendering. The
  protocol requires offsets to remain within the first cell and not
  enlarge explicit c/r rectangles:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  
  Previously, explicit placements were sized to the full c/r rectangle
  before the offset was applied. This extended their far edge into
  neighboring cells and let unbounded offsets reach renderer geometry.
  ```
- [`7e5dfa0`](https://github.com/ghostty-org/ghostty/commit/7e5dfa09eb601fedb9bdf5816d02890108ac1f04) terminal/kitty: constrain placement offsets to cell bounds ([#13891](https://github.com/ghostty-org/ghostty/issues/13891)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clamp X and Y offsets when a placement is created and normalize them
  again against current cell geometry when sizing and rendering. The
  protocol requires offsets to remain within the first cell and not
  enlarge explicit c/r rectangles:
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  
  Previously, explicit placements were sized to the full c/r rectangle
  before the offset was applied. This extended their far edge into
  neighboring cells and let unbounded offsets reach renderer geometry.
  ```
- [`abd7706`](https://github.com/ghostty-org/ghostty/commit/abd77067def1653692987588913b83c975ab4893) terminal/kitty: graphics `S` value is exact byte, not max ([@mitchellh](https://github.com/mitchellh))
  ```text
  File transmissions with exactly S bytes or trailing file data previously
  failed because appendRemaining reports StreamTooLong when it reaches its
  limit. This broke the protocol's partial-file transmission path.
  
  Use an exact-length allocation and read when S is nonzero, rejecting
  premature EOF and values above the image limit. Preserve the existing
  bounded read-to-EOF behavior for S=0.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#local-client
  ```
- [`364f8e9`](https://github.com/ghostty-org/ghostty/commit/364f8e9ac1e6dd79233e59fd46435c54e2117caf) terminal/kitty: graphics `S` value is exact byte, not max ([#13892](https://github.com/ghostty-org/ghostty/issues/13892)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  File transmissions with exactly S bytes or trailing file data previously
  failed because appendRemaining reports StreamTooLong when it reaches its
  limit. This broke the protocol's partial-file transmission path.
  
  Use an exact-length allocation and read when S is nonzero, rejecting
  premature EOF and values above the image limit. Preserve the existing
  bounded read-to-EOF behavior for S=0.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#local-client
  ```
- [`e5747cf`](https://github.com/ghostty-org/ghostty/commit/e5747cf0b603e4cad0ab6642c44738c9cfb50fa5) terminal/kitty: abort incomplete graphics loads ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, delete left partial bytes alive for the next upload, while
  failed or incomplete retransmissions kept stale placements visible.
  
  Abort incomplete chunked image uploads on delete commands and remove an
  existing image and its placements when retransmission of an explicit ID
  begins.
  ```
- [`55dac8f`](https://github.com/ghostty-org/ghostty/commit/55dac8fc47c239c54540fa30f3bea882d359d07f) terminal/kitty: abort incomplete graphics loads ([#13893](https://github.com/ghostty-org/ghostty/issues/13893)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, delete left partial bytes alive for the next upload, while
  failed or incomplete retransmissions kept stale placements visible.
  
  Abort incomplete chunked image uploads on delete commands and remove an
  existing image and its placements when retransmission of an explicit ID
  begins.
  ```
- [`f8b40a0`](https://github.com/ghostty-org/ghostty/commit/f8b40a02356f5ed945d4c2fa981394776186228b) terminal/kitty: fix various graphics deletion mismatches with spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Limit d=a/A to non-virtual placements that intersect the active screen.
  - Keep unrelated unplaced image data when processing d=A.
  - Make d=R delete matching unused images even when they have no
    placements, and default an omitted x bound to zero.
  - Give ED2 a separate clear path that preserves scrollback references
    while reclaiming every unreferenced image.
  
  References:
  - Spec:
    https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  - Delete reference implementation:
    https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L2114-L2363
  - ED2 reference implementation:
    https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L2919-L2958
  ```
- [`2ced1e5`](https://github.com/ghostty-org/ghostty/commit/2ced1e5c8e55bdc1cd77c7ecada4d0ef1cb28226) terminal/kitty: fix various graphics deletion mismatches with spec ([#13895](https://github.com/ghostty-org/ghostty/issues/13895)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Limit d=a/A to non-virtual placements that intersect the active
  screen.
  - Keep unrelated unplaced image data when processing d=A.
  - Make d=R delete matching unused images even when they have no
  placements, and default an omitted x bound to zero.
  - Give ED2 a separate clear path that preserves scrollback references
  while reclaiming every unreferenced image.
  
  References:
  - Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  - Delete reference implementation:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L2114-L2363
  - ED2 reference implementation:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L2919-L2958
  ```
- [`cfc5a96`](https://github.com/ghostty-org/ghostty/commit/cfc5a96501d72d0c43a73a9ed2f74c6381ba046c) terminal/kitty: validate graphics query image data ([@mitchellh](https://github.com/mitchellh))
  ```text
  Graphics query commands previously initialized their loading state but
  returned success before completing the image load.
  
  This allowed truncated, malformed, or otherwise invalid image data to
  return OK, giving capability probes a false positive.
  
  Complete and validate queried images through the normal load path, then
  discard the result without modifying image storage. Add coverage for
  invalid data and preserving an existing image with the queried ID.
  ```
- [`86d94f1`](https://github.com/ghostty-org/ghostty/commit/86d94f150a2c3a8e83c4dcab004e1a89af07b1c6) terminal/kitty: preserve chunked response identifiers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Chunked image responses used the final command even though only the
  initial chunk carries the image and placement identifiers. Successful
  replies lost image numbers and placement IDs. Final validation errors
  could also be suppressed entirely.
  
  Save the initial response identifiers with the in-progress image and use
  them when the final chunk completes. Continue replacing the response ID
  with the generated image ID after a successful load. Cover successful
  image-number replies and invalid final payloads with unit tests.
  ```
- [`306a169`](https://github.com/ghostty-org/ghostty/commit/306a169033cd945a5bcd8b5c31fdeae218006648) terminal/kitty: preserve data on unmatched delete ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make uppercase Kitty graphics deletes with a nonzero placement ID
  leave the image intact when the named placement does not exist.
  
  Previously, d=I,i=...,p=... could free unreferenced image data after
  matching no placement. A later put then failed with ENOENT, diverging
  from the protocol and Kitty.
  ```
- [`72b6cd7`](https://github.com/ghostty-org/ghostty/commit/72b6cd71247086eaa8f93edcc49d6d689045b715) terminal/kitty: validate graphics query image data ([#13896](https://github.com/ghostty-org/ghostty/issues/13896)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Graphics query commands previously initialized their loading state but
  returned success before completing the image load.
  
  This allowed truncated, malformed, or otherwise invalid image data to
  return OK, giving capability probes a false positive.
  
  Complete and validate queried images through the normal load path, then
  discard the result without modifying image storage. Add coverage for
  invalid data and preserving an existing image with the queried ID.
  ```
- [`fe12e30`](https://github.com/ghostty-org/ghostty/commit/fe12e30b3468b7afb92744f96af33f4ce484f4a9) terminal/kitty: preserve chunked response identifiers ([#13897](https://github.com/ghostty-org/ghostty/issues/13897)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Chunked image responses used the final command even though only the
  initial chunk carries the image and placement identifiers. Successful
  replies lost image numbers and placement IDs. Final validation errors
  could also be suppressed entirely.
  
  Save the initial response identifiers with the in-progress image and use
  them when the final chunk completes. Continue replacing the response ID
  with the generated image ID after a successful load. Cover successful
  image-number replies and invalid final payloads with unit tests.
  ```
- [`7f62fe7`](https://github.com/ghostty-org/ghostty/commit/7f62fe70a288c5d35ebd3097e75c46017950bcc7) terminal/kitty: preserve data on unmatched delete ([#13898](https://github.com/ghostty-org/ghostty/issues/13898)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make uppercase Kitty graphics deletes with a nonzero placement ID leave
  the image intact when the named placement does not exist.
  
  Previously, d=I,i=...,p=... could free unreferenced image data after
  matching no placement. A later put then failed with ENOENT, diverging
  from the protocol and Kitty.
  ```
- [`bed20eb`](https://github.com/ghostty-org/ghostty/commit/bed20eb36453c61c6aff76bdfda0c15235b8e513) terminal: clear tabstop bit on unset instead of toggling ([@fornwall](https://github.com/fornwall))
  ```text
  Tabstops.unset used XOR, so unsetting a column without a tabstop set
  one instead. This made TBC (CSI 0 g) and CTC (CSI 2 W) create a
  tabstop at the cursor column when none existed.
  ```
- [`4c6215b`](https://github.com/ghostty-org/ghostty/commit/4c6215bb8ee186b5c829457a9a9a9c936f2337bf) terminal: clear tabstop bit on unset instead of toggling ([#13900](https://github.com/ghostty-org/ghostty/issues/13900)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make `Tabstops.unset` (backing [Tab Clear
  (TBC)](https://ghostty.org/docs/vt/csi/tbc) with `n=0`) not set a tab
  stop when clearing a column that has no tab stop.
  ```

