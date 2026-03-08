> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 8, 2026 at 00:20 UTC.

## March 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22803119380), [2](https://github.com/ghostty-org/ghostty/actions/runs/22802362890), [3](https://github.com/ghostty-org/ghostty/actions/runs/22800843484)  
Summary: 3 runs • 30 commits • 4 authors

### Changes

- [`4bb602b`](https://github.com/ghostty-org/ghostty/commit/4bb602b0e1a251f401e49d490400e4a2b51d0b5a) Fix snap EGL vendor dirs to include host NVIDIA ICD paths ([@04cb](https://github.com/04cb))
- [`472b926`](https://github.com/ghostty-org/ghostty/commit/472b926a4d7abbacad4deea17aa0a0c69ffc12d3) Fix snap EGL vendor dirs to include host NVIDIA ICD paths ([#11209](https://github.com/ghostty-org/ghostty/issues/11209)) ([@kenvandine](https://github.com/kenvandine))
  ```text
  Fixes #10760. The snap launcher script was overriding the default system
  EGL vendor directories, preventing NVIDIA's proprietary EGL driver from
  being discovered. This caused crashes for users with NVIDIA GPUs on snap
  systems.
  
  The fix adds the standard host system paths (/etc/glvnd/egl_vendor.d and
  /usr/share/glvnd/egl_vendor.d) to __EGL_VENDOR_LIBRARY_DIRS before the
  snap-internal path. This is safe for classic confinement snaps since the
  host filesystem is fully accessible.
  ```
- [`291fbf5`](https://github.com/ghostty-org/ghostty/commit/291fbf55cb9c6946d7c080c90d8163d0b720dfe0) macos: AppleScript starting ([@mitchellh](https://github.com/mitchellh))
- [`c90a782`](https://github.com/ghostty-org/ghostty/commit/c90a782e592aa90e3a1479b80d5b9a3acdc63dff) macos: implement basic read-only applescript stuff ([@mitchellh](https://github.com/mitchellh))
- [`52c0709`](https://github.com/ghostty-org/ghostty/commit/52c0709d88c20f05edc1450d5e7105377f03206d) macos: add ability for agents to run debug app ([@mitchellh](https://github.com/mitchellh))
- [`40c7481`](https://github.com/ghostty-org/ghostty/commit/40c74811f16236df9afeb522dcbd9a98ebcb4a3f) macos: fix perform action ([@mitchellh](https://github.com/mitchellh))
- [`ef669ee`](https://github.com/ghostty-org/ghostty/commit/ef669eeae7574335631d6897c07f60ce4015727c) macos: add AppleScript `split` command ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new `split` command to the AppleScript scripting dictionary that
  splits a terminal in a given direction (right, left, down, up) and
  returns the newly created terminal.
  
  The command is exposed as:
    split terminal <terminal> direction <direction>
  
  Also adds a `fourCharCode` String extension for converting four-character
  ASCII strings to their FourCharCode (UInt32) representation.
  ```
- [`1742aed`](https://github.com/ghostty-org/ghostty/commit/1742aeda503c57979b7faa54c9ecffa9a176abde) macos: add focus and close AppleScript commands for terminals ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add two new AppleScript commands to the scripting dictionary:
  
  - `focus terminal <terminal>` — focuses the given terminal and brings
    its window to the front.
  - `close terminal <terminal>` — closes the given terminal without a
    confirmation prompt.
  
  Each command is implemented as an NSScriptCommand subclass following
  the same pattern as the existing split command.
  ```
- [`fd5ad1f`](https://github.com/ghostty-org/ghostty/commit/fd5ad1f574e3ad084db0e2a9b2161edaf53e85e5) macos: add AppleScript commands for text input, key, and mouse events ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add five new AppleScript commands to Ghostty.sdef mirroring the existing
  App Intents for terminal input:
  
  - `input text`: send text to a terminal as if pasted
  - `send key`: simulate a keyboard event with optional action and modifiers
  - `send mouse button`: send a mouse button press/release event
  - `send mouse position`: send a mouse cursor position event
  - `send mouse scroll`: send a scroll event with precision and momentum
  
  A shared `input action` enumeration (press/release) is used by both key
  and mouse button commands. Modifier keys are passed as a comma-separated
  string parameter (shift, control, option, command).
  ```
- [`ffe622e`](https://github.com/ghostty-org/ghostty/commit/ffe622ed30c60eb2a0ed2fdd644b2b4f606b0ba0) macos: add standard application properties and commands ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add standard Cocoa scripting definitions to the AppleScript dictionary:
  
  - Application properties: name, frontmost, version
  - Standard Suite commands: exists, quit
  
  These are backed by built-in Cocoa scripting classes (NSExistsCommand,
  NSQuitCommand) and standard NSApplication KVC keys, so no Swift code
  changes are needed.
  ```
- [`547fd6f`](https://github.com/ghostty-org/ghostty/commit/547fd6f748e9c504019513b3ec95fdf5a1ec4efb) typos: ignore apple four char codes ([@mitchellh](https://github.com/mitchellh))
- [`d03338c`](https://github.com/ghostty-org/ghostty/commit/d03338c1b53e1f0bc1e5f711f91c5d474d27ceee) macos: fix iOS build ([@mitchellh](https://github.com/mitchellh))
- [`341d8bd`](https://github.com/ghostty-org/ghostty/commit/341d8bdf754b85fe0dfaa57ceabe598e7eea0c59) macos: AppleScript windows/tabs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ScriptWindow and ScriptTab classes to expose window/tab hierarchy
  to AppleScript, along with the corresponding sdef definitions.
  ```
- [`f72d416`](https://github.com/ghostty-org/ghostty/commit/f72d41675bfd1d912f71a00c1e8716ddd6ae9654) macos: fix AppleScript quit command being silently ignored ([@mitchellh](https://github.com/mitchellh))
  ```text
  The application class in Ghostty.sdef was missing a responds-to
  declaration for the quit command. Apple's Cocoa Scripting requires
  the application class to explicitly declare it responds to quit via
  handleQuitScriptCommand: for the aevtquit event to be dispatched.
  ```
- [`e514035`](https://github.com/ghostty-org/ghostty/commit/e514035519a88fa593dd1047fa22bcb39a9022c0) macos: add terminals element to window and tab AppleScript classes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose terminal surfaces as elements on both ScriptWindow and ScriptTab,
  allowing AppleScript to enumerate terminals scoped to a specific window
  or tab (e.g. `terminals of window 1`, `terminals of tab 1 of window 1`).
  
  Changes:
  - Add `<element type="terminal">` to window and tab classes in Ghostty.sdef
  - Add `terminals` computed property and `valueInTerminalsWithUniqueID:`
    lookup to ScriptWindow (returns all surfaces across all tabs)
  - Add `terminals` computed property and `valueInTerminalsWithUniqueID:`
    lookup to ScriptTab (returns surfaces within that tab)
  ```
- [`122d0ec`](https://github.com/ghostty-org/ghostty/commit/122d0ecdfd9947d0c8c34953d0babc39502556e5) macos: expose name (title) on window, tab, and terminal via AppleScript ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `name` property (code `pnam`, cocoa key `title`) to the window, tab,
  and terminal classes in the scripting definition. This follows the standard
  Cocoa scripting convention where `name`/`pnam` maps to the `title` KVC key,
  matching what Apple does in CocoaStandard.sdef for NSWindow.
  
  Also fixes the pre-existing terminal `title` property which used a custom
  four-char code (`Gttl`) that AppleScript could not resolve directly — only
  via `properties of terminal`. All three classes now use the standard `pnam`
  code so `name of window 1`, `name of tab 1 of window 1`, and
  `name of terminal 1` all work correctly.
  ```
- [`959c2f5`](https://github.com/ghostty-org/ghostty/commit/959c2f51ac524e6556fe0e8d8b2db9ff090e0dd0) macos: add AppleScript new window command ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `new window` command to the scripting dictionary and wire it to
  `NSApplication` so AppleScript can create Ghostty windows.
  
  The command returns a scripting `window` object for the created window,
  with a fallback to a direct wrapper when AppKit window ordering has not
  yet refreshed in the current run loop.
  ```
- [`a3adeb0`](https://github.com/ghostty-org/ghostty/commit/a3adeb0166b2dc896045b71f8656b2605648e9c2) macos: use value-style AppleScript surface configuration records ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `surface configuration` record type to the scripting dictionary,
  implement `new surface configuration` (with optional copy-from), and allow
  `new window` to accept `with configuration`.
  ```
- [`459eaa2`](https://github.com/ghostty-org/ghostty/commit/459eaa2640444b1b434f5508b807afd8f273e151) macos: order AppleScript dictionary definitions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Document the preferred Ghostty.sdef top-level order in AGENTS.md and reorder
  Ghostty Suite definitions to classes, records, enums, then commands.
  ```
- [`4d5de70`](https://github.com/ghostty-org/ghostty/commit/4d5de702f2613ea0130ec83eb7af867e51a9d8a0) macos: allow split command surface configuration ([@mitchellh](https://github.com/mitchellh))
- [`d271c8c`](https://github.com/ghostty-org/ghostty/commit/d271c8ccaab0f08ab0092b2f0893c8e0d0e5283d) macos: add new tab command ([@mitchellh](https://github.com/mitchellh))
- [`28b4e24`](https://github.com/ghostty-org/ghostty/commit/28b4e2495db53c707d4e6616af136eadd1eba393) macos: Add AppleScript commands for window and tab control ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add scripting dictionary commands for activating windows, selecting tabs,
  closing tabs, and closing windows.
  
  Implement the corresponding Cocoa AppleScript command handlers and expose
  minimal ScriptWindow/ScriptTab helpers needed to resolve live targets.
  
  Verified by building Ghostty and running osascript commands against the
  absolute Debug app path to exercise all four new commands.
  ```
- [`25fa581`](https://github.com/ghostty-org/ghostty/commit/25fa58143ec6d8e6eb200b459838f16376423fdf) macos: add macos-applescript config ([@mitchellh](https://github.com/mitchellh))
- [`221a163`](https://github.com/ghostty-org/ghostty/commit/221a1639af6060b485fd2ef214fa260b7aa7ddb1) swiftlint ([@mitchellh](https://github.com/mitchellh))
- [`259a41d`](https://github.com/ghostty-org/ghostty/commit/259a41d503ad24eb9af83dd7f50566cf312ef87a) macos: rename surface config working directory to not be ambiguous ([@mitchellh](https://github.com/mitchellh))
- [`038ebef`](https://github.com/ghostty-org/ghostty/commit/038ebef16cc8cea570f87a95771eb76528935210) address some PR feedback ([@mitchellh](https://github.com/mitchellh))
- [`210b01a`](https://github.com/ghostty-org/ghostty/commit/210b01ad600f0dceff9ff2be1a16bbf6c9fa7f57) macos: use direct parameters for object-targeting commands ([@mitchellh](https://github.com/mitchellh))
  ```text
  Change split, focus, close, activate window, select tab, close tab, and
  close window commands to accept their target object as a direct parameter
  instead of a named parameter. This produces natural AppleScript syntax:
  
    activate window (window 1)
    close tab (tab 1 of window 1)
    split (terminal 1) direction right
  
  instead of the awkward redundant form:
  
    activate window window (window 1)
    close tab tab (tab 1 of window 1)
    split terminal (terminal 1) direction right
  
  The implementation moves command logic from NSScriptCommand subclasses
  into responds-to handler methods on ScriptTerminal, ScriptWindow, and
  ScriptTab, which is the standard Cocoa Scripting pattern for commands
  whose direct parameter is an application class.
  ```
- [`ed9a6cb`](https://github.com/ghostty-org/ghostty/commit/ed9a6cb6488ff282a5061bbd016d9082d7c3e773) macos: implement the quit command ([@mitchellh](https://github.com/mitchellh))
- [`fd3a62b`](https://github.com/ghostty-org/ghostty/commit/fd3a62b9c1712508516bdd18fdaf652929bff4ed) AppleScript ([#11208](https://github.com/ghostty-org/ghostty/issues/11208)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds AppleScript support to the macOS app.
  
  AppleScript is still one of the best ways to script macOS apps. It is
  more CLI friendly and share-able than Apple Shortcuts and can be used by
  other CLI programs like editors (Neovim plugins), launchers
  (Raycast/Alfred), etc. It has been heavily requested to introduce more
  scriptability into Ghostty and this is a really good, powerful option on
  macOS.
  
  > [!NOTE]
  >
  > I definitely still want to do something cross-platform and more
  official as a plugin/scripting API for Ghostty. But native integrations
  like this are a goal of Ghostty as well and this implementation is just
  some thin logic over already existing internals to expose it.
  
  I plan on merging this ahead of 1.3. Normally I wouldn't ship a feature
  so late in the game but this is fairly hermetic (doesn't impact other
  systems) and I plan on documenting it as a "preview" feature since the
  API and stability are in question.
  
  ## Security
  
  Apple secures AppleScript via TCC by asking for permission when a script
  is run whether an app is allowed to be controlled. Because this is
  always asked, we do default AppleScript to being enabled. This is
  typical of macOS native applications already.
  
  AppleScript can be wholesale disabled via `macos-applescript = false`.
  
  ## Future
  
  There is a big question of what else to expose to this to make it
  useful. I'm going to make a call to action for the 1.3 cycle to gather
  feedback on this, since we can expose mostly anything!
  
  ## Capabilities
  
  ### Objects
  
  | Object | Key Properties | Key Elements |
  | --- | --- | --- |
  | `application` | `name`, `frontmost`, `version` | `windows`,
  `terminals` |
  | `window` | `id`, `name`, `selected tab` | `tabs`, `terminals` |
  | `tab` | `id`, `name`, `index`, `selected` | `terminals` |
  | `terminal` | `id`, `name`, `working directory` | None |
  
  ### Commands
  
  | Category | Command | Purpose |
  | --- | --- | --- |
  | Application | `perform action` | Execute a Ghostty action string on a
  terminal. |
  | Configuration | `new surface configuration` | Create/copy a reusable
  surface configuration record. |
  | Creation | `new window` | Open a new Ghostty window (optional
  configuration). |
  | Creation | `new tab` | Open a new tab (optional target
  window/configuration). |
  | Layout | `split` | Split a terminal and return the new terminal. |
  | Focus/Selection | `focus` | Focus a terminal. |
  | Focus/Selection | `activate window` | Bring a window to front and
  activate app. |
  | Focus/Selection | `select tab` | Select and foreground a tab. |
  | Lifecycle | `close` | Close a terminal. |
  | Lifecycle | `close tab` | Close a tab. |
  | Lifecycle | `close window` | Close a window. |
  | Input | `input text` | Paste-style text input into terminal. |
  | Input | `send key` | Send key press/release with optional modifiers. |
  | Input | `send mouse button` | Send mouse button press/release. |
  | Input | `send mouse position` | Send mouse position update. |
  | Input | `send mouse scroll` | Send scroll event with
  precision/momentum options. |
  | Standard Suite | `count`, `exists`, `quit` | Standard Cocoa scripting
  functionality. |
  
  ## Examples
  
  ### Layout
  
  ```AppleScript
  -- Tmux-like layout: 4 panes in one tab (2x2), each with a job.
  set projectDir to POSIX path of (path to home folder) & "src/ghostty"
  
  tell application "Ghostty"
      activate
  
      -- Reusable config for all panes.
      set cfg to new surface configuration
      set initial working directory of cfg to projectDir
  
      -- Create the first window/tab + split into 4 panes.
      set win to new window with configuration cfg
      set paneEditor to terminal 1 of selected tab of win
      set paneBuild to split paneEditor direction right with configuration cfg
      set paneGit to split paneEditor direction down with configuration cfg
      set paneLogs to split paneBuild direction down with configuration cfg
  
      -- Seed each pane with a command.
      input text "nvim ." to paneEditor
      send key "enter" to paneEditor
  
      input text "zig build -Demit-macos-app=false" to paneBuild
  
      input text "git status -sb" to paneGit
  
      input text "tail -f /tmp/dev.log" to paneLogs
      send key "enter" to paneLogs
  
      -- Put focus back where you want to type.
      focus paneEditor
  end tell
  ```
  
  ### Broadcast Commands
  
  ```AppleScript
  -- Run one command across every open terminal surface.
  set cmd to "echo sync && date"
  
  tell application "Ghostty"
      set allTerms to terminals
  
      repeat with t in allTerms
          input text cmd to t
          send key "enter" to t
      end repeat
  
      display dialog ("Broadcasted to " & (count of allTerms) & " terminal(s).")
  end tell
  ```
  
  ### Jump by Working Directory
  
  ```applescript
  -- Find the first terminal whose cwd contains this text.
  set needle to "ghostty"
  
  tell application "Ghostty"
      set matches to every terminal whose working directory contains needle
  
      -- Fallback: try title if cwd had no match.
      if (count of matches) = 0 then
          set matches to every terminal whose name contains needle
      end if
  
      if (count of matches) = 0 then
          display dialog ("No terminal matched: " & needle)
      else
          set t to item 1 of matches
          focus terminal t
          input text "echo '[focused by AppleScript]'" to t
          send key "enter" to t
      end if
  end tell
  ```
  ````
- [`af43af1`](https://github.com/ghostty-org/ghostty/commit/af43af13c363e2819763ede819e3279cf778e993) Update VOUCHED list ([#11211](https://github.com/ghostty-org/ghostty/issues/11211)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11209#issuecomment-4016613771)
  from @mitchellh.
  
  Vouch: @04cb
  ```

## March 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22748794179)  
Summary: 1 runs • 4 commits • 2 authors

### Changes

- [`96a5e71`](https://github.com/ghostty-org/ghostty/commit/96a5e71871dc583bdb4c04554a0ac6760e2db32a) build(deps): bump docker/build-push-action from 6.19.2 to 7.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 6.19.2 to 7.0.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/10e90e3645eae34f1e60eeb005ba3a3d33f178e8...d08e5c354a6adb9ed34480a06d141179aa583294)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`adab5f6`](https://github.com/ghostty-org/ghostty/commit/adab5f6f0e51621be1ac2549871b97ddf89e7407) build(deps): bump docker/build-push-action from 6.19.2 to 7.0.0 ([#11199](https://github.com/ghostty-org/ghostty/issues/11199)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 6.19.2 to 7.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.0</h2>
  <ul>
  <li>Node 24 as default runtime (requires <a
  href="https://github.com/actions/runner/releases/tag/v2.327.1">Actions
  Runner v2.327.1</a> or later) by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1470">docker/build-push-action#1470</a></li>
  <li>Remove deprecated <code>DOCKER_BUILD_NO_SUMMARY</code> and
  <code>DOCKER_BUILD_EXPORT_RETENTION_DAYS</code> envs by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1473">docker/build-push-action#1473</a></li>
  <li>Remove legacy export-build tool support for build summary by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1474">docker/build-push-action#1474</a></li>
  <li>Switch to ESM and update config/test wiring by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1466">docker/build-push-action#1466</a></li>
  <li>Bump <code>@​actions/core</code> from 1.11.1 to 3.0.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1454">docker/build-push-action#1454</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.62.1 to 0.79.0 in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1453">docker/build-push-action#1453</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1472">docker/build-push-action#1472</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1479">docker/build-push-action#1479</a></li>
  <li>Bump minimatch from 3.1.2 to 3.1.5 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1463">docker/build-push-action#1463</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v6.19.2...v7.0.0">https://github.com/docker/build-push-action/compare/v6.19.2...v7.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/d08e5c354a6adb9ed34480a06d141179aa583294"><code>d08e5c3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1479">#1479</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/cbd2dff9a0f0ef650dcce9c635bb2f877ab37be5"><code>cbd2dff</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/f76f51f12900bb84aa9d1a498f35870ef1f76675"><code>f76f51f</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.78.0 to
  0.79.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/7d03e66b5f24d6b390ab64b132795fd3ef4152c8"><code>7d03e66</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1473">#1473</a>
  from crazy-max/rm-deprecated-envs</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/98f853d923dd281a3bcbbb98a0712a91aa913322"><code>98f853d</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/cadccf6e8c7385c86d9cb0800cf07672645cc238"><code>cadccf6</code></a>
  remove deprecated envs</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/03fe8775e325e34fffbda44c73316f8287aea372"><code>03fe877</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1478">#1478</a>
  from docker/dependabot/github_actions/docker/setup-b...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/827e36650e1fa7386d09422b5ba3c068fdbe0a1d"><code>827e366</code></a>
  chore(deps): Bump docker/setup-buildx-action from 3 to 4</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/e25db879d025485a4eebd64fea9bb88a43632da6"><code>e25db87</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1474">#1474</a>
  from crazy-max/rm-export-build-tool</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/1ac2573b5c8b4e4621d5453ab2a99e83725242bd"><code>1ac2573</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1470">#1470</a>
  from crazy-max/node24</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/10e90e3645eae34f1e60eeb005ba3a3d33f178e8...d08e5c354a6adb9ed34480a06d141179aa583294">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=6.19.2&new-version=7.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`04aff46`](https://github.com/ghostty-org/ghostty/commit/04aff46022f679cf607b6987031c4f4fe5273b86) macos: add build script, update AGENTS.md, skip UI tests ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is an update to address common agentic issues I run into,
  but the `build.nu` script may be generally helpful to people using
  the Nix env since `xcodebuild` is broken by default in Nix due to the
  compiler/linker overrides Nix shell does.
  ```
- [`055ed28`](https://github.com/ghostty-org/ghostty/commit/055ed28580e140f2a21b752946349750b963a7aa) macos: add build script, update AGENTS.md, skip UI tests ([#11202](https://github.com/ghostty-org/ghostty/issues/11202)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is an update to address common agentic issues I run into, but the
  `build.nu` script may be generally helpful to people using the Nix env
  since `xcodebuild` is broken by default in Nix due to the
  compiler/linker overrides Nix shell does.
  ```

## March 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22736924002), [2](https://github.com/ghostty-org/ghostty/actions/runs/22723550848), [3](https://github.com/ghostty-org/ghostty/actions/runs/22723016503), [4](https://github.com/ghostty-org/ghostty/actions/runs/22722387895), [5](https://github.com/ghostty-org/ghostty/actions/runs/22707501732), [6](https://github.com/ghostty-org/ghostty/actions/runs/22704188724), [7](https://github.com/ghostty-org/ghostty/actions/runs/22703620859), [8](https://github.com/ghostty-org/ghostty/actions/runs/22703142519), [9](https://github.com/ghostty-org/ghostty/actions/runs/22702479466)  
Summary: 9 runs • 22 commits • 8 authors

### Changes

- [`acf54a9`](https://github.com/ghostty-org/ghostty/commit/acf54a91668b524d9a5e6e800c34ce2d08fd4d48) windows: use new callconv convention ([@jcollie](https://github.com/jcollie))
- [`e8aad10`](https://github.com/ghostty-org/ghostty/commit/e8aad103263297d41335a27d9d1679a7ab47c08b) windows: avoid the use of wcwidth ([@jcollie](https://github.com/jcollie))
- [`cccdb0d`](https://github.com/ghostty-org/ghostty/commit/cccdb0d2ade79c0d3ef37635c5c9fe90a0ac14bf) windows: add trivial implementation of expandHome ([@jcollie](https://github.com/jcollie))
- [`d29e1cc`](https://github.com/ghostty-org/ghostty/commit/d29e1cc1375e0a700df73604c528a550813c8b1a) windows: use explicit error sets to work around lack of file locking ([@jcollie](https://github.com/jcollie))
- [`b1d3e36`](https://github.com/ghostty-org/ghostty/commit/b1d3e36e2ea0d428dd333019c8346b6d4bcbc762) windows: add GetComputerNameA so that hostname-related functions work ([@jcollie](https://github.com/jcollie))
- [`3e220ab`](https://github.com/ghostty-org/ghostty/commit/3e220ab3757243c45bbb999c185ae33de8f70da7) Windows build fixes ([#11195](https://github.com/ghostty-org/ghostty/issues/11195)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Some more fixes to get Windows building again. `zig build` on
  x64_64-windows now succeeds but `zig build test` fails in
  `src/terminal/page.zig` because Zig/Windows lacks a POSIX `mmap`
  implementation.
  ```
- [`e1f4ee7`](https://github.com/ghostty-org/ghostty/commit/e1f4ee7fdd4d5fc4b6b86dd70986be75a0bacabd) Update VOUCHED list ([#11192](https://github.com/ghostty-org/ghostty/issues/11192)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11184#discussioncomment-16011801)
  from @mitchellh.
  
  Vouch: @mac0ne
  ```
- [`f36b903`](https://github.com/ghostty-org/ghostty/commit/f36b903479f54fc7202a95ca10509f3eac06e007) Update VOUCHED list ([#11191](https://github.com/ghostty-org/ghostty/issues/11191)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11190#issuecomment-4005537826)
  from @00-kat.
  
  Vouch: @AnthonyZhOon
  ```
- [`e07aefa`](https://github.com/ghostty-org/ghostty/commit/e07aefa6010716ccc51c745b8e0dde9598b58812) fix: zsh shell integration when `sudo` and `ssh` aliases are defined ([@Michielvk](https://github.com/Michielvk))
- [`42540f4`](https://github.com/ghostty-org/ghostty/commit/42540f44cd717a0e1169fb5008443c6ebb9a073d) fix: zsh shell integration when `sudo` and `ssh` aliases are defined ([#11185](https://github.com/ghostty-org/ghostty/issues/11185)) ([@jparise](https://github.com/jparise))
  ````text
  I encountered an issue related to
  https://github.com/ghostty-org/ghostty/discussions/8641 and
  https://github.com/ghostty-org/ghostty/pull/8647, but in `zsh` instead
  of `bash`.
  
  One of my aliases is:
  
  ```bash
  alias sudo='sudo '
  ```
  
  Which causes following error when sourcing the zsh shell integrations:
  
  ```shell
  source /usr/share/ghostty/shell-integration/zsh/ghostty-integration
  /usr/share/ghostty/shell-integration/zsh/ghostty-integration:149: defining function based on alias `sudo'
  /usr/share/ghostty/shell-integration/zsh/ghostty-integration:233: parse error near `()'
  ```
  ````
- [`c920a88`](https://github.com/ghostty-org/ghostty/commit/c920a88cdcc19ed42ab013c1ba2bb9ad41592ada) GTK: add 'move' to the drop target actions ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #11175
  ```
- [`dd575c7`](https://github.com/ghostty-org/ghostty/commit/dd575c716077e0e2d12881fe0c5f65b067978176) GTK: add 'move' to the drop target actions ([#11182](https://github.com/ghostty-org/ghostty/issues/11182)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes #11175
  ```
- [`2fe5515`](https://github.com/ghostty-org/ghostty/commit/2fe55152ca6fe74219f129ee6339b265a41d0252) i18n: add Vietnamese translation ([@anhthang](https://github.com/anhthang))
- [`4d30d88`](https://github.com/ghostty-org/ghostty/commit/4d30d886c636305875748b84ec06d489af669921) update translation ([@anhthang](https://github.com/anhthang))
- [`e2a01be`](https://github.com/ghostty-org/ghostty/commit/e2a01beca7bed7974f1e700cef1ad0eecea2d13d) Merge branch 'main' into vi_VN ([@anhthang](https://github.com/anhthang))
- [`0b802e7`](https://github.com/ghostty-org/ghostty/commit/0b802e7c2e228b246bb0daee925ab87f66c6ec5c) i18n: add Vietnamese translation ([#8912](https://github.com/ghostty-org/ghostty/issues/8912)) ([@00-kat](https://github.com/00-kat))
  ```text
  Adds support for the Vietnamese language
  ```
- [`3dde6e2`](https://github.com/ghostty-org/ghostty/commit/3dde6e2559e0aa67e04a6001485d87b80ed4c1dd) terminal: bound link regex search work with Oniguruma retry limits ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11177
  
  Use per-search Oniguruma match params (retry_limit_in_search) in
  StringMap-backed link detection to avoid pathological backtracking hangs
  on very long lines.
  
  The units are ticks in the internal loop so its kind of opaque but
  this seems to still match some very long URLs. The test case in question
  was a 169K character line (which is now rejected).
  ```
- [`fe1e25f`](https://github.com/ghostty-org/ghostty/commit/fe1e25f7a6cec06c45f3c11ef8cc259a617697d4) terminal: bound link regex search work with Oniguruma retry limits ([#11181](https://github.com/ghostty-org/ghostty/issues/11181)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11177
  
  Use per-search Oniguruma match params (retry_limit_in_search) in
  StringMap-backed link detection to avoid pathological backtracking hangs
  on very long lines.
  
  The units are ticks in the internal loop so its kind of opaque but this
  seems to still match some very long URLs. The test case in question was
  a 169K character line (which is now rejected).
  ```
- [`961bf46`](https://github.com/ghostty-org/ghostty/commit/961bf46884dc7f75a4bfd8640bf7f57baed6b540) Fix Windows test in src/Command.zig ([@jcollie](https://github.com/jcollie))
  ```text
  This was introduced in #10611. This doesn't fix all of the current
  Windows build problems, but at least fixes one that I introduced.
  ```
- [`320d9c2`](https://github.com/ghostty-org/ghostty/commit/320d9c2f1cba79a8a9ab32c4d8c337571e435c20) Fix Windows test in src/Command.zig ([#11180](https://github.com/ghostty-org/ghostty/issues/11180)) ([@jcollie](https://github.com/jcollie))
  ```text
  This was introduced in #10611. This doesn't fix all of the current
  Windows build problems, but at least fixes one that I introduced.
  ```
- [`dfa968d`](https://github.com/ghostty-org/ghostty/commit/dfa968d932ecb6928ebab9a9d460ae0ac629f985) Update VOUCHED list ([#11176](https://github.com/ghostty-org/ghostty/issues/11176)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11175#issuecomment-4001807388)
  from @jcollie.
  
  Vouch: @douglas
  ```
- [`a5327a5`](https://github.com/ghostty-org/ghostty/commit/a5327a51f3fedea890f59ad75e7666a57bb743c4) Update VOUCHED list ([#11179](https://github.com/ghostty-org/ghostty/issues/11179)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11164#discussioncomment-16005149)
  from @mitchellh.
  
  Vouch: @Michielvk
  ```

## March 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22694000891), [2](https://github.com/ghostty-org/ghostty/actions/runs/22691416275), [3](https://github.com/ghostty-org/ghostty/actions/runs/22685396526), [4](https://github.com/ghostty-org/ghostty/actions/runs/22684084893), [5](https://github.com/ghostty-org/ghostty/actions/runs/22678614686), [6](https://github.com/ghostty-org/ghostty/actions/runs/22654900798)  
Summary: 6 runs • 30 commits • 9 authors

### Changes

- [`6961c22`](https://github.com/ghostty-org/ghostty/commit/6961c2265e3b760dda9146aa285f11eee1e16abe) gtk: `+new-window` now respects `--working-directory` and `-e` ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes: #8862
  Fixes: #10716
  
  This adds the machinery to pass configuration settings received over
  DBus down to the GObject Surface so that that configuration information
  can be used to override some settings from the current "live" config
  when creating a new window. Currently it's only possible to override
  `--working-directory` and `--command`. `-e` on the `ghostty +new-window`
  CLI works as well.
  
  Adding more overridable settings is possible, but being able to fully
  override any possible setting would better be served with a major
  revamp of how Ghostty handles configs, which I is way out of scope at
  the moment.
  ```
- [`ec0f9ef`](https://github.com/ghostty-org/ghostty/commit/ec0f9ef4163ee8262a31c779a9062c21b7486d5c) gtk: `+new-window` now respects `--title` ([@jcollie](https://github.com/jcollie))
- [`f2ce7c3`](https://github.com/ghostty-org/ghostty/commit/f2ce7c348edbd635dd74cae9b3b330825768ba76) gtk: `+new-window` document `--title` ([@jcollie](https://github.com/jcollie))
- [`002a6cc`](https://github.com/ghostty-org/ghostty/commit/002a6cc76526240b19cee9792a79de05077bb09a) gtk: use simpler method for passing overrides around ([@jcollie](https://github.com/jcollie))
  ```text
  As discussed in Discord, this commit drops the `ConfigOverride` object
  in favor of a simpler method of passing the overrides around. Completely
  avoiding changes to the core wasn't possible but it's very minimal now.
  ```
- [`e27956f`](https://github.com/ghostty-org/ghostty/commit/e27956fdde1b3964d689f8f0c038b29f6e7d5157) gtk: remove modifications to the core for overrides ([@jcollie](https://github.com/jcollie))
- [`5bc5820`](https://github.com/ghostty-org/ghostty/commit/5bc5820f3255cc8dfbf6c30e3f7edb4a947add3d) gtk: simplify new-window action memory management with an arena ([@jcollie](https://github.com/jcollie))
- [`58d6021`](https://github.com/ghostty-org/ghostty/commit/58d6021ec44c2383344f2c08214ebe3dd754ea4d) apprt/gtk: reduce split-tree flicker by reusing leaf widgets ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #8208
  
  Split-tree updates currently clear `tree_bin` and then wait for every surface
  to become parentless before rebuilding. That leaves the split area blank for
  one or more frames, which is the visible flicker during split create/close/
  resize/equalize actions.
  
  Keep the previous widget tree attached until the idle rebuild runs, then
  swap in the rebuilt tree in one step. During rebuild, reuse existing
  leaf widgets by detaching and reparenting them into the new `GtkPaned`
  hierarchy instead of recreating wrappers for every leaf.
  
  This removes the parent-settling rebuild path and avoids transient blank
  frames while preserving debounced rebuild behavior.
  ```
- [`436a11d`](https://github.com/ghostty-org/ghostty/commit/436a11dd59598ddfcc74434cd6283017753eed0f) apprt/gtk: reduce split-tree flicker by reusing leaf widgets ([#11170](https://github.com/ghostty-org/ghostty/issues/11170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #8208
  
  Split-tree updates currently clear `tree_bin` and then wait for every
  surface to become parentless before rebuilding. That leaves the split
  area blank for one or more frames, which is the visible flicker during
  split create/close/ resize/equalize actions.
  
  Keep the previous widget tree attached until the idle rebuild runs, then
  swap in the rebuilt tree in one step. During rebuild, reuse existing
  leaf widgets by detaching and reparenting them into the new `GtkPaned`
  hierarchy instead of recreating wrappers for every leaf.
  
  This removes the parent-settling rebuild path and avoids transient blank
  frames while preserving debounced rebuild behavior.
  ```
- [`46522a8`](https://github.com/ghostty-org/ghostty/commit/46522a8779ba44e47d4f68ab633ace5382971624) gtk: `+new-window` now respects `--working-directory` and `-e` ([#10809](https://github.com/ghostty-org/ghostty/issues/10809)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes: #8862
  Fixes: #10716
  
  This adds the machinery to pass configuration settings received over
  DBus down to the GObject Surface so that that configuration information
  can be used to override some settings from the current "live" config
  when creating a new window. Currently it's only possible to override
  `--working-directory`, `--command`, and `--title`. `-e` on the `ghostty
  +new-window` CLI works as well.
  
  Adding more overridable settings is possible, but being able to fully
  override any possible setting would better be served with a major revamp
  of how Ghostty handles configs, which is way out of scope at the moment.
  ```
- [`05807f0`](https://github.com/ghostty-org/ghostty/commit/05807f0d72d44ba24048cce56bf716d2c629ff30) Revert "build: link to the system FontConfig by default on non-macOS systems ([#11152](https://github.com/ghostty-org/ghostty/issues/11152))" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit ee4c6f88c5517d242b73427f66da4d54d41e35a8.
  ```
- [`57d877a`](https://github.com/ghostty-org/ghostty/commit/57d877a0d622a01381688cbafd8d227612640fc7) Revert "build: link to the system FontConfig by default on non-macOS systems" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 89f9dd7848111b28287a70388d610d66227a53f4.
  ```
- [`2cfc9d3`](https://github.com/ghostty-org/ghostty/commit/2cfc9d36d8ea81722d9ecfad027ba8558879b780) Revert "build: link to the system FontConfig by default ([#11169](https://github.com/ghostty-org/ghostty/issues/11169)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit ee4c6f88c5517d242b73427f66da4d54d41e35a8.
  
  This breaks standard `zig build run` from a dev shell in Nix/NixOS. I
  think we need to rethink some of the protections here, possibly only to
  apply to packaging/release modes or something.
  
  cc @jcollie
  ```
- [`9a3dbe1`](https://github.com/ghostty-org/ghostty/commit/9a3dbe10b05912ee30061dae6d730d8d9db0bc46) zsh: fix extra newlines with leading-newline prompts ([@jparise](https://github.com/jparise))
  ```text
  In our multiline prompt logic, skip the newline immediately after the
  first mark to avoid introducing a double newline due to OSC 133;A's
  fresh-line behavior.
  
  Fixes: #11003
  ```
- [`9386fa6`](https://github.com/ghostty-org/ghostty/commit/9386fa64997db6124f1cdbd4730938edb49f2a85) zsh: emit missing prompt markers in line-init ([@jparise](https://github.com/jparise))
  ```text
  Emit semantic prompt markers at line-init if PS1 doesn't contain our
  marks. This ensures the terminal sees prompt markers even if another
  plugin (like zinit or oh-my-posh) regenerated PS1 after our precmd ran.
  We use 133;P instead of 133;A to avoid fresh-line behavior which would
  disrupt the display since the prompt has already been drawn. We also
  emit 133;B to mark the input area, which is needed for click-to-move.
  
  Fixes: #10555
  ```
- [`3ee8ef4`](https://github.com/ghostty-org/ghostty/commit/3ee8ef4f650f550698ee1e8e81e591511e195bf4) macos: suppress split-focus click mouse reports ([@rockorager](https://github.com/rockorager))
  ```text
  Amp-Thread-ID: https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`0fa12f8`](https://github.com/ghostty-org/ghostty/commit/0fa12f89151d5332233c97308bdda8925f6627b9) gtk: suppress mouse reports on focus-transfer clicks ([@rockorager](https://github.com/rockorager))
  ```text
  Amp-Thread-ID: https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`d146808`](https://github.com/ghostty-org/ghostty/commit/d1468086efcb7ae83498c4660ecfa5c3aebd8b6a) macos: defer key-window focus sync to reduce churn ([@rockorager](https://github.com/rockorager))
  ```text
  Amp-Thread-ID: https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`3bcf329`](https://github.com/ghostty-org/ghostty/commit/3bcf329c2b5894e64e129542742db305a51d463e) zsh: emit missing prompt markers in line-init ([#11165](https://github.com/ghostty-org/ghostty/issues/11165)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Emit semantic prompt markers at line-init if PS1 doesn't contain our
  marks. This ensures the terminal sees prompt markers even if another
  plugin (like zinit or oh-my-posh) regenerated PS1 after our precmd ran.
  We use 133;P instead of 133;A to avoid fresh-line behavior which would
  disrupt the display since the prompt has already been drawn. We also
  emit 133;B to mark the input area, which is needed for click-to-move.
  
  Fixes: #10572, #10555
  ```
- [`226d0b9`](https://github.com/ghostty-org/ghostty/commit/226d0b9918b6c6149d21f79a05a432d4c10da0bf) zsh: fix extra newlines with leading-newline prompts ([#11166](https://github.com/ghostty-org/ghostty/issues/11166)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In our multiline prompt logic, skip the newline immediately after the
  first mark to avoid introducing a double newline due to OSC 133;A's
  fresh-line behavior.
  
  Fixes: #11003
  ```
- [`c3febab`](https://github.com/ghostty-org/ghostty/commit/c3febabd286dfaa47c3d7d251ede22e8e382b6f3) apprt: unify split-click focus behavior across macOS and GTK; suppress focus-transfer mouse events ([#11167](https://github.com/ghostty-org/ghostty/issues/11167)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  This PR aligns split-pane click behavior across macOS and GTK when focus
  changes due to click.
  
  When a left-click is used to transfer focus (window activation or
  switching to another split), Ghostty now treats that click as focus-only
  and suppresses forwarding mouse press/release events for that
  focus-transfer click.
  
  ## Changes
  
  1. macOS: suppress focus-transfer left mouse-down and matching mouse-up
  in `SurfaceView_AppKit.swift`.
  1. GTK: suppress focus-transfer left mouse-down and matching mouse-up in
  `src/apprt/gtk/class/surface.zig`.
  1. macOS: defer key-window focus sync to next runloop tick to reduce
  transient focus churn in `BaseTerminalController.swift`.
  1. macOS build/lint: exclude generated/dependency paths from SwiftLint
  during build in `.swiftlint.yml` and
  `Ghostty.xcodeproj/project.pbxproj`.
  
  ## Behavior
  
  1. Focus-transfer split clicks are now focus-only on both macOS and GTK.
  1. Matching release is also suppressed for those clicks, avoiding
  release-without-press sequences.
  1. Platform behavior is consistent for split focus transitions.
  
  ## Validation
  
  1. Built macOS target with `xcodebuild -target Ghostty -configuration
  Debug -arch arm64`.
  1. Ran targeted Zig test command `zig build test
  -Dtest-filter=computeFraction`.
  1. Ran format/lint for touched files (`swiftlint lint --fix`, `zig
  fmt`).
  4. Build and (human) tested click scenarios on macOS
  
  ## AI Disclosure
  
  AI-assisted.
  
  Thread:
  https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`2772c90`](https://github.com/ghostty-org/ghostty/commit/2772c90885d2ffc27fdf5e7e758c5ecca2af6f8c) i18n: add Kazakh translation (kk) ([@crayxt](https://github.com/crayxt))
- [`0797b28`](https://github.com/ghostty-org/ghostty/commit/0797b281ec0268f2df65399b1aede85eaea0d31a) Add Kazakh translation ([#10670](https://github.com/ghostty-org/ghostty/issues/10670)) ([@00-kat](https://github.com/00-kat))
  ```text
  Dear maintainers,
  
  This PR adds Kazakh language translation file and necessary edits to
  CODEOWNERS and i18n file with the list of locales.
  
  Please review (and squash when committing)
  
  Thank you!
  ```
- [`a716b9c`](https://github.com/ghostty-org/ghostty/commit/a716b9c4d421a3ab94f93fe301ddc28a5a086361) macos: Ghostty.Shell.escape unit tests ([@jparise](https://github.com/jparise))
- [`53ef422`](https://github.com/ghostty-org/ghostty/commit/53ef42266a422c23b1523a3347caf7433fb63983) macos: Ghostty.Shell.escape unit tests ([#11162](https://github.com/ghostty-org/ghostty/issues/11162)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  *AI Disclosure:* These were written using the Claude Agent in Xcode
  26.3, partly as an excuse to try out that latest integration.
  ```
- [`b215291`](https://github.com/ghostty-org/ghostty/commit/b2152919141de84a71052dd6f298d24dc1b08d63) macos: implement audio bell support with bell-audio-path ([@alaasdk](https://github.com/alaasdk))
  ```text
  Extends the macOS bell implementation to support the `audio` bell
  feature by playing a user-specified audio file via NSSound.
  
  Previously, macOS only supported the `system` feature (NSSound.beep()).
  This change adds support for:
  - `audio` bell feature: plays the file at `bell-audio-path` using
    NSSound, respecting the `bell-audio-volume` setting
  - Adds `cval()` to the `Path` type so it can be returned via the C API
  
  Also removes the "(GTK only)" restriction from `bell-audio-path` and
  `bell-audio-volume` documentation, as these options now work on macOS.
  
  Example config:
    bell-features = audio
    bell-audio-path = /System/Library/Sounds/Glass.aiff
    bell-audio-volume = 0.8
  ```
- [`c93cf52`](https://github.com/ghostty-org/ghostty/commit/c93cf521088594649a6c2d54e1c916c3906c0a0f) Update VOUCHED list ([#11156](https://github.com/ghostty-org/ghostty/issues/11156)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10982#discussioncomment-15990906)
  from @jcollie.
  
  Vouch: @cmwetherell
  ```
- [`69df92b`](https://github.com/ghostty-org/ghostty/commit/69df92b56a85d1ae883dc8f034fb19665161c498) build(deps): bump cachix/install-nix-action from 31.9.1 to 31.10.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.9.1 to 31.10.0.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/2126ae7fc54c9df00dd18f7f18754393182c73cd...19effe9fe722874e6d46dd7182e4b8b7a43c4a99)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`73ce40c`](https://github.com/ghostty-org/ghostty/commit/73ce40c6235af6028dac5dfd4502b50c779b7bf5) build(deps): bump cachix/install-nix-action from 31.9.1 to 31.10.0 ([#11157](https://github.com/ghostty-org/ghostty/issues/11157)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.9.1 to 31.10.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.33.3 -&gt; 2.34.0 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/267">cachix/install-nix-action#267</a>
  Release notes: <a
  href="https://discourse.nixos.org/t/nix-2-34-0-released/75818">https://discourse.nixos.org/t/nix-2-34-0-released/75818</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.9.1...v31.10.0">https://github.com/cachix/install-nix-action/compare/v31.9.1...v31.10.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/19effe9fe722874e6d46dd7182e4b8b7a43c4a99"><code>19effe9</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/267">#267</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/d3f3b99dd19236cb244609944767f2864ec646ee"><code>d3f3b99</code></a>
  nix: 2.33.3 -&gt; 2.34.0</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/2126ae7fc54c9df00dd18f7f18754393182c73cd...19effe9fe722874e6d46dd7182e4b8b7a43c4a99">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.9.1&new-version=31.10.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`98ad1d9`](https://github.com/ghostty-org/ghostty/commit/98ad1d955cf8d66cf5548f581a6502cf10f2f852) use proper type for optional path ([@mitchellh](https://github.com/mitchellh))
- [`619e33a`](https://github.com/ghostty-org/ghostty/commit/619e33a4febec871c0d655f51d85e7f5f21ba289) macos: implement audio bell support with bell-audio-path ([#11154](https://github.com/ghostty-org/ghostty/issues/11154)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Summary
  
  This extends the macOS bell implementation to support the `audio` bell
  feature, bringing it to parity with GTK/Linux.
  
  Previously, macOS only had the `system` feature (`NSSound.beep()`). This
  PR adds:
  
  - **`audio` bell feature on macOS**: plays the file at `bell-audio-path`
  using `NSSound(contentsOfFile:)`, respecting `bell-audio-volume`
  - **`cval()` on the `Path` type**: allows `Path` values (a union type)
  to be returned through the C API, which is needed for Swift to read
  `bell-audio-path`
  - **Removes `(GTK only)` restriction** from `bell-audio-path` and
  `bell-audio-volume` documentation
  
  ## How it works
  
  In `AppDelegate.swift`, when the bell rings and the `audio` feature is
  enabled, Ghostty now:
  1. Reads `bell-audio-path` from config
  2. Loads it as an `NSSound`
  3. Applies `bell-audio-volume` and plays it
  
  Falls back gracefully if the path is not set or the file cannot be
  loaded.
  
  ## Example config
  
  ```
  bell-features = audio
  bell-audio-path = /System/Library/Sounds/Glass.aiff
  bell-audio-volume = 0.8
  ```
  
  ## Testing
  
  - Set `bell-features = audio` and `bell-audio-path` to any valid audio
  file
  - Trigger a bell with `echo -e '\a'`
  - Audio should play at the configured volume
  ````

## March 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22645694880), [2](https://github.com/ghostty-org/ghostty/actions/runs/22644801904), [3](https://github.com/ghostty-org/ghostty/actions/runs/22643251900), [4](https://github.com/ghostty-org/ghostty/actions/runs/22634551065), [5](https://github.com/ghostty-org/ghostty/actions/runs/22633830469), [6](https://github.com/ghostty-org/ghostty/actions/runs/22632962784), [7](https://github.com/ghostty-org/ghostty/actions/runs/22630103557), [8](https://github.com/ghostty-org/ghostty/actions/runs/22608444462), [9](https://github.com/ghostty-org/ghostty/actions/runs/22607408000), [10](https://github.com/ghostty-org/ghostty/actions/runs/22603105482)  
Summary: 10 runs • 26 commits • 8 authors

### Changes

- [`205c05d`](https://github.com/ghostty-org/ghostty/commit/205c05d59d016222b350b63dd10f8745b1a5d831) macos: passthrough mouse down event to TabTitleEditor if needed ([@bo2themax](https://github.com/bo2themax))
- [`6614708`](https://github.com/ghostty-org/ghostty/commit/661470897e878b766254e59f30531192d7ae2771) macos: passthrough right mouse down event to TabTitleEditor if needed ([@bo2themax](https://github.com/bo2themax))
- [`78fdff3`](https://github.com/ghostty-org/ghostty/commit/78fdff34a969d3864ae5a471f673a19ab5e064cf) macos: hide close button when editing tab title ([@bo2themax](https://github.com/bo2themax))
- [`4437707`](https://github.com/ghostty-org/ghostty/commit/44377071323b629480a367abf80862a1d7b084b0) macos: use a separated struct to hide and restore tab states ([@bo2themax](https://github.com/bo2themax))
- [`4c83872`](https://github.com/ghostty-org/ghostty/commit/4c838723173da757a16a2f3afd4c94f16732ef6a) macOS: Refine tab title editing ([#11150](https://github.com/ghostty-org/ghostty/issues/11150)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Pass through mouse down event to `TabTitleEditor` if needed
  - Pass through right mouse down event to `TabTitleEditor` if needed
  - Hide close button when editing tab title
  
  Refactor:
  - Use a separated struct to hide and restore tab states
  
  
  https://github.com/user-attachments/assets/e69838f5-e199-437c-b53b-a491e9d5b752
  ```
- [`0149fd7`](https://github.com/ghostty-org/ghostty/commit/0149fd7139ce76f89357d9ab9bbfba439d1d8445) Update VOUCHED list ([#11155](https://github.com/ghostty-org/ghostty/issues/11155)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11154#issuecomment-3993830083)
  from @mitchellh.
  
  Vouch: @alaasdk
  ```
- [`89f9dd7`](https://github.com/ghostty-org/ghostty/commit/89f9dd7848111b28287a70388d610d66227a53f4) build: link to the system FontConfig by default on non-macOS systems ([@jcollie](https://github.com/jcollie))
  ```text
  Because of the global shared state that FontConfig maintains, FontConfig
  must be linked dynamically to the same system FontConfig shared library
  that GTK uses. Ghostty's default has been changed to always link to the
  system FontConfig library on non-macOS systems. If that is overridden
  (by specifying `-fno-sys=fontconfig` during the build) Ghostty may crash
  when trying to locate glyphs that are not available in the default font.
  
  Fixes #10432
  ```
- [`ee4c6f8`](https://github.com/ghostty-org/ghostty/commit/ee4c6f88c5517d242b73427f66da4d54d41e35a8) build: link to the system FontConfig by default on non-macOS systems ([#11152](https://github.com/ghostty-org/ghostty/issues/11152)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Because of the global shared state that FontConfig maintains, FontConfig
  must be linked dynamically to the same system FontConfig shared library
  that GTK uses. Ghostty's default has been changed to always link to the
  system FontConfig library on non-macOS systems. If that is overridden
  (by specifying `-fno-sys=fontconfig` during the build) Ghostty may crash
  when trying to locate glyphs that are not available in the default font.
  
  Fixes #10432
  ```
- [`fdfc9fe`](https://github.com/ghostty-org/ghostty/commit/fdfc9fea2ff291436685e7ff6158ffbccbc8a36e) input: send composed text in kitty keyboard protocol ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the kitty keyboard protocol "report all keys as escape codes" mode
  was active, composed/IME text (e.g. from dead keys or compose sequences)
  was silently dropped.
  
  This happened because the composed text is sent within our GTK apprt
  with key=unidentified and no unshifted_codepoint, so no kitty entry was
  found and the encoder returned without producing any output. The
  plain-text fallback was also skipped because report_all bypasses it.
  
  Send composed text as raw UTF-8 when no kitty entry is found, matching
  the behavior of Kitty on Linux for me.
  
  Fixes #10049
  ```
- [`2d5bb18`](https://github.com/ghostty-org/ghostty/commit/2d5bb18e29bc9f50eb2783973f5ed4599285ac1b) input: send composed text in kitty keyboard protocol ([#11149](https://github.com/ghostty-org/ghostty/issues/11149)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the kitty keyboard protocol "report all keys as escape codes" mode
  was active, composed/IME text (e.g. from dead keys or compose sequences)
  was silently dropped.
  
  This happened because the composed text is sent within our GTK apprt
  with key=unidentified and no unshifted_codepoint, so no kitty entry was
  found and the encoder returned without producing any output. The
  plain-text fallback was also skipped because report_all bypasses it.
  
  Send composed text as raw UTF-8 when no kitty entry is found, matching
  the behavior of Kitty on Linux for me.
  
  Fixes #10049
  ```
- [`d2175d1`](https://github.com/ghostty-org/ghostty/commit/d2175d1b56e2f821745ee5ef08056bc918a43ea2) fuzz: add OSC parser fuzzer ([@mitchellh](https://github.com/mitchellh))
- [`562721e`](https://github.com/ghostty-org/ghostty/commit/562721e6d18a64f267ce1da132df2b236152434c) fuzz: add OSC parser fuzzer ([#11148](https://github.com/ghostty-org/ghostty/issues/11148)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I'm running this now, 10 minutes with nothing but I figure this is a big
  enough target we should also add this.
  ```
- [`d9d65fd`](https://github.com/ghostty-org/ghostty/commit/d9d65fdb9f20c7190609009717a680c18b977425) fix: calculate cell size before presenting gtk window ([@ajbucci](https://github.com/ajbucci))
- [`0af3477`](https://github.com/ghostty-org/ghostty/commit/0af3477e3540c5ad6748d67d7519a3092e219838) fix: remove max() and magic numbers ([@ajbucci](https://github.com/ajbucci))
- [`733d307`](https://github.com/ghostty-org/ghostty/commit/733d307bf4138fe66b8eff01f1d923941c9fe7f0) gtk: update some comments/function names, take min sizes into account ([@jcollie](https://github.com/jcollie))
- [`e6e5f3f`](https://github.com/ghostty-org/ghostty/commit/e6e5f3ffe18871359a812bdba68fd325e8ecb359) macos: finish editing tab title when the window resigns as key window ([@bo2themax](https://github.com/bo2themax))
- [`c8a0092`](https://github.com/ghostty-org/ghostty/commit/c8a0092301a3274dac0ccb982d4b05fca98d0468) fix: calculate cell size before presenting gtk window ([#10459](https://github.com/ghostty-org/ghostty/issues/10459)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #7937
  
  Added `computeInitialSize` to GTK `Surface` and call it in GTK
  `Application` before the first `present()`, so the window manager
  centers the correct size on initial show.
  
  The issue occurs because the core `Surface.recomputeInitialSize()` runs
  only after the renderer is initialized. In GTK, the `GLArea` isn’t
  realized until after `present()`, so the initial size arrives too late
  for WM centering.
  
  **Limitations**: when we precompute size before `present()` we do not
  have access to padding, so the sizing will be very slightly off... but
  since it is only off a few pixels I was unable to tell visually that it
  wasn't perfectly centered.
  
  **Other thoughts**: I was hesitant to make changes to core `Surface`
  because the issue is Linux-specific, but it may make sense to extract a
  helper from `recomputeInitialSize` to avoid duplicating the sizing math.
  
  **AI Disclosure:** I used AI to explore the project, help with any
  language / API questions (I've never used zig before and rarely use
  gtk), and make implementation suggestions.
  ```
- [`2f0039d`](https://github.com/ghostty-org/ghostty/commit/2f0039d419022cd827d3c7023947c48a478e3137) macos: finish editing tab title when the window resigns as key window ([#11147](https://github.com/ghostty-org/ghostty/issues/11147)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes #11146 and also #10993. Updated the comments added in #11052.
  
  > After finishing editing when the window resigns as the key window,
  using `labelFrame.minY` is fine with the same usage as #10993, but when
  double-clicking with text selected it will move up again 🤷🏻‍♂️.
  
  This makes focus state more accurate with cursor shape on the surface,
  when editing the title for a tab in another window group.
  
  [Incorrect
  example](https://github.com/user-attachments/assets/c3c4e774-a683-44e7-9bb6-3be79ac72ec2)
  ```
- [`4ce782b`](https://github.com/ghostty-org/ghostty/commit/4ce782b63f7348867cb6fd00695740b3970ec77a) terminfo: add support for SGR dim ([@noib3](https://github.com/noib3))
  ```text
  This PR implements the fix discussed in
  https://github.com/ghostty-org/ghostty/discussions/11128
  ```
- [`cb06b9b`](https://github.com/ghostty-org/ghostty/commit/cb06b9b0018508b04702e9a4580963eed8d00cdd) terminfo: add support for SGR dim ([#11144](https://github.com/ghostty-org/ghostty/issues/11144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR implements the fix discussed in
  https://github.com/ghostty-org/ghostty/discussions/11128.
  
  Before:
  
  <img width="818" height="96" alt="before"
  src="https://github.com/user-attachments/assets/788f981f-3d1b-4c60-bf85-0c297641cae7"
  />
  
  After:
  
  <img width="813" height="93" alt="after"
  src="https://github.com/user-attachments/assets/a530015a-053a-4680-9a85-812aa8df3d91"
  />
  ```
- [`bb64692`](https://github.com/ghostty-org/ghostty/commit/bb646926f8c4c242365cd2e915140760f95c1c75) config: respect cursor-click-to-move for OSC133 click to move ([@mitchellh](https://github.com/mitchellh))
  ```text
  When cursor-click-to-move is set to false, disable all prompt
  click-to-move mechanisms including shell-native methods such as OSC 133
  cl= (arrow key synthesis) and click_events.
  
  I forgot to port this config over when we did the OSC133 stuff.
  
  Also update the config documentation to accurately describe the current
  behavior.
  
  Fixes #11138
  ```
- [`2502ca2`](https://github.com/ghostty-org/ghostty/commit/2502ca294efe5aa9722c36e25b2252b0150054e9) config: respect cursor-click-to-move for OSC133 click to move ([#11141](https://github.com/ghostty-org/ghostty/issues/11141)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When cursor-click-to-move is set to false, disable all prompt
  click-to-move mechanisms including shell-native methods such as OSC 133
  cl= (arrow key synthesis) and click_events.
  
  I forgot to port this config over when we did the OSC133 stuff.
  
  Also update the config documentation to accurately describe the current
  behavior.
  
  Fixes #11138
  ```
- [`391c904`](https://github.com/ghostty-org/ghostty/commit/391c9044bc62bd001ab842e52bde0bd398837823) pkg/afl++: remove @@ from run target since we use in-memory targets ([@mitchellh](https://github.com/mitchellh))
- [`5e7a5cc`](https://github.com/ghostty-org/ghostty/commit/5e7a5cc9c1b4b198e226e2b88df5b3eb66299dcf) pin python depds to latest tag ([@rhodes-b](https://github.com/rhodes-b))
- [`eaa83b8`](https://github.com/ghostty-org/ghostty/commit/eaa83b82b3f637ab1c07ac78ea8e69e3f620cc4d) address comments ([@rhodes-b](https://github.com/rhodes-b))
- [`d3c3770`](https://github.com/ghostty-org/ghostty/commit/d3c37704359cdc863a85a0d67baa8a9cd09f88af) Nix pkgs pin dependencies ([#11121](https://github.com/ghostty-org/ghostty/issues/11121)) ([@pluiedev](https://github.com/pluiedev))

## March 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22592783895), [2](https://github.com/ghostty-org/ghostty/actions/runs/22591766134), [3](https://github.com/ghostty-org/ghostty/actions/runs/22583700515), [4](https://github.com/ghostty-org/ghostty/actions/runs/22581513590), [5](https://github.com/ghostty-org/ghostty/actions/runs/22562974731), [6](https://github.com/ghostty-org/ghostty/actions/runs/22562509161), [7](https://github.com/ghostty-org/ghostty/actions/runs/22561514943), [8](https://github.com/ghostty-org/ghostty/actions/runs/22558361524), [9](https://github.com/ghostty-org/ghostty/actions/runs/22558023945), [10](https://github.com/ghostty-org/ghostty/actions/runs/22556024652)  
Summary: 10 runs • 20 commits • 3 authors

### Changes

- [`177612a`](https://github.com/ghostty-org/ghostty/commit/177612a4cf239b2c3d8c36a45c9fa5e9d4a22ba0) terminal: fix insertBlanks orphaned spacer_tail beyond right margin ([@mitchellh](https://github.com/mitchellh))
  ```text
  When insertBlanks clears the entire region from cursor to the right
  margin (scroll_amount == 0), a wide character whose head is at the right
  margin gets cleared but its spacer_tail just beyond the margin is left
  behind, causing a "spacer tail not following wide" page integrity
  violation.
  
  Move the right-margin wide-char cleanup from inside the scroll_amount >
  0 block to before it, so it runs unconditionally — matching the
  rowWillBeShifted pattern of cleaning up boundary-straddling wide chars
  up front.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`5fa42dd`](https://github.com/ghostty-org/ghostty/commit/5fa42dd80235bf3493d4e8d7d6817597d8f3e1c8) Update VOUCHED list ([#11139](https://github.com/ghostty-org/ghostty/issues/11139)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11128#discussioncomment-15976454)
  from @mitchellh.
  
  Vouch: @noib3
  ```
- [`aa157c0`](https://github.com/ghostty-org/ghostty/commit/aa157c09abf6384e38cd4d9c19c35bfab8f7a3b8) terminal: fix insertBlanks orphaned spacer_tail beyond right margin ([#11137](https://github.com/ghostty-org/ghostty/issues/11137)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When insertBlanks clears the entire region from cursor to the right
  margin (scroll_amount == 0), a wide character whose head is at the right
  margin gets cleared but its spacer_tail just beyond the margin is left
  behind, causing a "spacer tail not following wide" page integrity
  violation.
  
  Move the right-margin wide-char cleanup from inside the scroll_amount >
  0 block to before it, so it runs unconditionally — matching the
  rowWillBeShifted pattern of cleaning up boundary-straddling wide chars
  up front.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`1ba9f91`](https://github.com/ghostty-org/ghostty/commit/1ba9f9187ef09a507cf58a3c38de493aacb090c4) terminal: fix no-reflow resize leaving stale spacer heads ([@mitchellh](https://github.com/mitchellh))
  ```text
  resizeWithoutReflowGrowCols has a fast path that reuses existing page
  capacity when growing columns: it simply bumps page.size.cols without
  touching cell data. If any row has a spacer_head at the old last column
  (from a wide char that did not fit), that cell is no longer at the end
  of the now-wider row, causing a page integrity violation.
  
  Fix by checking for spacer_head cells at the old last column before
  taking the fast path. If any are found, fall through to the slow path
  which handles spacer heads correctly via cloneRowFrom.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`b39a00d`](https://github.com/ghostty-org/ghostty/commit/b39a00ddfa9003572e058d6ba1e87c449e575967) terminal: fix insertLines/deleteLines orphaned cells on full clear ([@mitchellh](https://github.com/mitchellh))
  ```text
  When deleteLines or insertLines count >= scroll region height, all rows
  go through the clear-only path (no shifting). This path did not call
  rowWillBeShifted, leaving orphaned spacer_tail cells when wide characters
  straddled the right margin boundary, causing a "spacer tail not following
  wide" page integrity violation.
  
  Add rowWillBeShifted before clearCells in the else branch of both
  functions.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`678601d`](https://github.com/ghostty-org/ghostty/commit/678601d94a4d7fe0828b6f67b1a2b0d690c73aa9) terminal: fix no-reflow resize leaving stale spacer heads ([#11135](https://github.com/ghostty-org/ghostty/issues/11135)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  resizeWithoutReflowGrowCols has a fast path that reuses existing page
  capacity when growing columns: it simply bumps page.size.cols without
  touching cell data. If any row has a spacer_head at the old last column
  (from a wide char that did not fit), that cell is no longer at the end
  of the now-wider row, causing a page integrity violation.
  
  Fix by checking for spacer_head cells at the old last column before
  taking the fast path. If any are found, fall through to the slow path
  which handles spacer heads correctly via cloneRowFrom.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`4768fff`](https://github.com/ghostty-org/ghostty/commit/4768ffff7396fb78578a61a6e488f16e1e961bf7) terminal: fix insertLines/deleteLines orphaned cells on full clear ([#11136](https://github.com/ghostty-org/ghostty/issues/11136)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When deleteLines or insertLines count >= scroll region height, all rows
  go through the clear-only path (no shifting). This path did not call
  rowWillBeShifted, leaving orphaned spacer_tail cells when wide
  characters straddled the right margin boundary, causing a "spacer tail
  not following wide" page integrity violation.
  
  Add rowWillBeShifted before clearCells in the else branch of both
  functions.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`e7030e7`](https://github.com/ghostty-org/ghostty/commit/e7030e73dbafd3f986c57b1a015d16cd53e7435b) terminal: fix printCell corrupting previous row when overwriting wide char ([@mitchellh](https://github.com/mitchellh))
  ```text
  printCell, when overwriting a wide cell with a narrow cell at x<=1 and
  y>0, unconditionally sets the last cell of the previous row to .narrow.
  This is intended to clear a spacer_head left by a wrapped wide char, but
  the cell could be a spacer_tail if a wide char fit entirely on the
  previous row. Setting a spacer_tail to .narrow orphans the preceding
  .wide cell, which later causes an integrity violation in insertBlanks
  (assert that the cell after a .wide is .spacer_tail).
  
  Fix by guarding the assignment so it only fires when the previous row's
  last cell is actually a .spacer_head. The same fix is applied in both
  the .wide and .spacer_tail branches of printCell.
  
  Found by AFL++ stream fuzzer.
  ```
- [`8cddd38`](https://github.com/ghostty-org/ghostty/commit/8cddd384c6ef614a373cf52b2a0e835c7e85134a) terminal: fix printCell corrupting previous row when overwriting wide char ([#11134](https://github.com/ghostty-org/ghostty/issues/11134)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  printCell, when overwriting a wide cell with a narrow cell at x<=1 and
  y>0, unconditionally sets the last cell of the previous row to .narrow.
  This is intended to clear a spacer_head left by a wrapped wide char, but
  the cell could be a spacer_tail if a wide char fit entirely on the
  previous row. Setting a spacer_tail to .narrow orphans the preceding
  .wide cell, which later causes an integrity violation in insertBlanks
  (assert that the cell after a .wide is .spacer_tail).
  
  Fix by guarding the assignment so it only fires when the previous row's
  last cell is actually a .spacer_head. The same fix is applied in both
  the .wide and .spacer_tail branches of printCell.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`90e96a3`](https://github.com/ghostty-org/ghostty/commit/90e96a3891b7718ff98819ee51ecbd7c133d422f) terminal: fix insertBlanks integrity violation with wide char at right margin ([@mitchellh](https://github.com/mitchellh))
  ```text
  insertBlanks checks whether the last source cell being shifted is wide
  and clears it to avoid splitting, but it did not check the destination
  cells at the right edge of the scroll region. When a wide character
  straddles the right scroll margin (head at the margin, spacer_tail just
  beyond it), the swap loop displaced the wide head without clearing the
  orphaned spacer_tail, causing a page integrity violation
  (InvalidSpacerTailLocation).
  
  Fix by checking the cell at the right margin (last destination cell)
  before the swap loop and clearing it along with its spacer_tail when it
  is wide.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`9d3c46c`](https://github.com/ghostty-org/ghostty/commit/9d3c46c4bc2348594148f809c01433ce768173ce) terminal: fix insertBlanks integrity violation with wide char at right margin ([#11132](https://github.com/ghostty-org/ghostty/issues/11132)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  insertBlanks checks whether the last source cell being shifted is wide
  and clears it to avoid splitting, but it did not check the destination
  cells at the right edge of the scroll region. When a wide character
  straddles the right scroll margin (head at the margin, spacer_tail just
  beyond it), the swap loop displaced the wide head without clearing the
  orphaned spacer_tail, causing a page integrity violation
  (InvalidSpacerTailLocation).
  
  Fix by checking the cell at the right margin (last destination cell)
  before the swap loop and clearing it along with its spacer_tail when it
  is wide.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`913c120`](https://github.com/ghostty-org/ghostty/commit/913c12097bad2feb8977853cf1a60c137a968b50) Update VOUCHED list ([#11123](https://github.com/ghostty-org/ghostty/issues/11123)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11118#discussioncomment-15967576)
  from @pluiedev.
  
  Vouch: @jguthmiller
  ```
- [`22e29bb`](https://github.com/ghostty-org/ghostty/commit/22e29bb1f00b11c4ca1caf6d1302f67b2e9fa970) Update VOUCHED list ([#11122](https://github.com/ghostty-org/ghostty/issues/11122)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11121#issuecomment-3982187512)
  from @jcollie.
  
  Vouch: @rhodes-b
  ```
- [`97c11af`](https://github.com/ghostty-org/ghostty/commit/97c11af347be4ab8fd66ff0048048ee4209a03e9) terminal: fix integrity violation printing wide char with hyperlink at right edge ([@mitchellh](https://github.com/mitchellh))
  ```text
  Printing a wide character at the right edge of the screen with an active
  hyperlink triggered a page integrity violation (UnwrappedSpacerHead).
  printCell wrote the spacer_head to the cell and then called
  cursorSetHyperlink, whose internal integrity check observed the
  spacer_head before printWrap had a chance to set the row wrap flag.
  
  Fix by setting row.wrap = true before calling printCell for the
  spacer_head case, so all integrity checks see a consistent state.
  printWrap sets wrap again afterward, which is harmless. Found by AFL++
  stream fuzzer.
  ```
- [`43ec4ac`](https://github.com/ghostty-org/ghostty/commit/43ec4ace47ec47d7dea66826e0ebdfb3cae51a02) fuzz: add replay-crashes.nu to help find crash repros ([@mitchellh](https://github.com/mitchellh))
- [`f3da60a`](https://github.com/ghostty-org/ghostty/commit/f3da60aef59e3c9c645dc016e0377eb0af748a05) terminal: fix integrity violation printing wide char with hyperlink at right edge ([#11119](https://github.com/ghostty-org/ghostty/issues/11119)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Printing a wide character at the right edge of the screen with an active
  hyperlink triggered a page integrity violation (UnwrappedSpacerHead).
  printCell wrote the spacer_head to the cell and then called
  cursorSetHyperlink, whose internal integrity check observed the
  spacer_head before printWrap had a chance to set the row wrap flag.
  
  Fix by setting row.wrap = true before calling printCell for the
  spacer_head case, so all integrity checks see a consistent state.
  printWrap sets wrap again afterward, which is harmless. Found by AFL++
  stream fuzzer.
  
  #11109
  ```
- [`7665efc`](https://github.com/ghostty-org/ghostty/commit/7665efc3a161e3424267846216e913ba324aeb1c) fuzz: new stream corpus from 2 hour run ([@mitchellh](https://github.com/mitchellh))
- [`ca31828`](https://github.com/ghostty-org/ghostty/commit/ca31828c9387e2743f2b41d0405e2ed80590cd7f) Update VOUCHED list ([#11116](https://github.com/ghostty-org/ghostty/issues/11116)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11115#issuecomment-3981600125)
  from @mitchellh.
  
  Vouch: @markdorison
  ```
- [`533ad9e`](https://github.com/ghostty-org/ghostty/commit/533ad9e3fadf4eb1e5d28cb2d4b40ef4a8b311e3) i18n: update pt_BR translations ([#10635](https://github.com/ghostty-org/ghostty/issues/10635)) ([@guilhermetk](https://github.com/guilhermetk))
  ```text
  Add missing pt_BR translations reported in
  https://github.com/ghostty-org/ghostty/issues/10632 for version 1.3
  ```
- [`2454642`](https://github.com/ghostty-org/ghostty/commit/24546426c8de75d11c8448464fb4cd614663da46) Sync CODEOWNERS vouch list ([#11114](https://github.com/ghostty-org/ghostty/issues/11114)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @derVedro
  ```

