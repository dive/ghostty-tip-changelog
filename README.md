> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 24, 2026 at 21:23 UTC.

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
Summary: 5 runs • 45 commits • 7 authors

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

## August 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32176127114), [2](https://github.com/ghostty-org/ghostty/actions/runs/32172263374), [3](https://github.com/ghostty-org/ghostty/actions/runs/32169188975), [4](https://github.com/ghostty-org/ghostty/actions/runs/32168669864), [5](https://github.com/ghostty-org/ghostty/actions/runs/32160637749), [6](https://github.com/ghostty-org/ghostty/actions/runs/32145015115)  
Summary: 6 runs • 23 commits • 2 authors

### Changes

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

