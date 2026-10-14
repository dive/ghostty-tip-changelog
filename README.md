> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 14, 2026 at 19:07 UTC.

## October 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38542450833), [2](https://github.com/ghostty-org/ghostty/actions/runs/38515836993)  
Summary: 2 runs • 16 commits • 3 authors

### Changes

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

## October 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38089240001), [2](https://github.com/ghostty-org/ghostty/actions/runs/38083192720), [3](https://github.com/ghostty-org/ghostty/actions/runs/38081318922), [4](https://github.com/ghostty-org/ghostty/actions/runs/38080640871), [5](https://github.com/ghostty-org/ghostty/actions/runs/38050071133)  
Summary: 5 runs • 16 commits • 8 authors

### Changes

- [`9fa2e3a`](https://github.com/ghostty-org/ghostty/commit/9fa2e3aaffdc7ae30f7cc417d1ce706957ae58a0) libghostty-vt: add prompt-based viewport scrolling ([@elias8](https://github.com/elias8))
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
- [`4144f6d`](https://github.com/ghostty-org/ghostty/commit/4144f6dea4dbf9586c797e535a04f1cfd381d8a7) core: demote 'adjusting page capacity' log message to debug ([@jcollie](https://github.com/jcollie))
- [`6161591`](https://github.com/ghostty-org/ghostty/commit/61615915c8f423b1497ac2a1ae68885cad353892) core: demote 'adjusting page capacity' log message to debug ([#14631](https://github.com/ghostty-org/ghostty/issues/14631)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This can really spam the logs, and isn't really useful outside of a
  developer context anyway.
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
- [`1da3ac4`](https://github.com/ghostty-org/ghostty/commit/1da3ac43bef626ec1155c366c1960cb0f4f74d1f) Update VOUCHED list ([#14623](https://github.com/ghostty-org/ghostty/issues/14623)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14486#issuecomment-6097215618)
  from @trag1c.
  
  Denounce: @rebecca-bell-2001
  ```

## October 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37960020956), [2](https://github.com/ghostty-org/ghostty/actions/runs/37902855280), [3](https://github.com/ghostty-org/ghostty/actions/runs/37884767144)  
Summary: 3 runs • 6 commits • 4 authors

### Changes

- [`7f1219f`](https://github.com/ghostty-org/ghostty/commit/7f1219fd701449fa3e5de33b9ba9ce85f008ac33) cli/list-themes: add ctrl-d/u paging ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  Ctrl-D and Ctrl-U move down and up 20 themes, like PgDn and PgUp.
  This helps keyboards without page keys and matches the less/vi-style
  keys that already exist (g/G).
  ```
- [`246f702`](https://github.com/ghostty-org/ghostty/commit/246f702876b924a1cb7cade1e99274d1470302fc) cli/list-themes: add ctrl-d/u paging ([#14607](https://github.com/ghostty-org/ghostty/issues/14607)) ([@jcollie](https://github.com/jcollie))
  ```text
  discussion #14604
  
  ## Ctrl-D and Ctrl-U paging
  
  `Ctrl-D` and `Ctrl-U` move down and up 20 themes. `PgDn` and `PgUp`
  already do this. `g` and `G` already exist (#13376), so vim-like paging
  fits. It also helps users who have no `PgUp` or `PgDn` key.
  ```
- [`9d479dc`](https://github.com/ghostty-org/ghostty/commit/9d479dcb1664e8dc3c66c7302ce596dc56b36d6d) Update VOUCHED list ([#14614](https://github.com/ghostty-org/ghostty/issues/14614)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14582#discussioncomment-18831499)
  from @pluiedev.
  
  Denounce: @Martzcode
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

## October 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37856874364), [2](https://github.com/ghostty-org/ghostty/actions/runs/37844704694), [3](https://github.com/ghostty-org/ghostty/actions/runs/37805457756), [4](https://github.com/ghostty-org/ghostty/actions/runs/37794266921), [5](https://github.com/ghostty-org/ghostty/actions/runs/37790076764), [6](https://github.com/ghostty-org/ghostty/actions/runs/37789831587), [7](https://github.com/ghostty-org/ghostty/actions/runs/37742721150)  
Summary: 7 runs • 12 commits • 7 authors

### Changes

- [`54ba7b1`](https://github.com/ghostty-org/ghostty/commit/54ba7b1dd98dfaf14ee82ae7cbf435e867986da9) cli/list-themes: fix keypad page down binding ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  The move-down-by-20 binding listed kp_down instead of kp_page_down.
  Pressing keypad down matched both this binding and the move-down-by-1
  binding, so it moved 21 themes. The move-up-by-20 binding already uses
  kp_page_up.
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
- [`55424c1`](https://github.com/ghostty-org/ghostty/commit/55424c1ccb34bff8f5534b5bc918ea859b3a9278) i18n: use "konfiguration" consistently in Danish (da) translation ([@kgni](https://github.com/kgni))
- [`e2ced6b`](https://github.com/ghostty-org/ghostty/commit/e2ced6b710427ea69dc6795bf00a787c81554452) i18n: update Danish (da) PO-Revision-Date ([@kgni](https://github.com/kgni))
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
- [`bad5854`](https://github.com/ghostty-org/ghostty/commit/bad5854f358332f3168b35c5052f41b45a2671b3) Update VOUCHED list ([#14603](https://github.com/ghostty-org/ghostty/issues/14603)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14595#issuecomment-6062284415)
  from @mitchellh.
  
  Vouch: @Huge
  ```
- [`0f171f6`](https://github.com/ghostty-org/ghostty/commit/0f171f650a1cbbd6df4a2573b6b0c7de57cc6d90) Update VOUCHED list ([#14600](https://github.com/ghostty-org/ghostty/issues/14600)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14597#issuecomment-6061673855)
  from @pluiedev.
  
  Denounce: @riskirills66
  ```
- [`7551c5b`](https://github.com/ghostty-org/ghostty/commit/7551c5bad4211ebf3cf20647f5b735f2dc14b1f6) Update VOUCHED list ([#14599](https://github.com/ghostty-org/ghostty/issues/14599)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14598#issuecomment-6061636878)
  from @trag1c.
  
  Vouch: @Rayzerrek
  ```
- [`7b60f9b`](https://github.com/ghostty-org/ghostty/commit/7b60f9bf5f057394038f81653eaa7cc5a55bb5df) i18n: improve Danish (da) translation ([@kgni](https://github.com/kgni))
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

