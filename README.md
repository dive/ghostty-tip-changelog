> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 3, 2026 at 07:40 UTC.

## September 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33716226971), [2](https://github.com/ghostty-org/ghostty/actions/runs/33712675217)  
Summary: 2 runs • 7 commits • 3 authors

### Changes

- [`e01e75b`](https://github.com/ghostty-org/ghostty/commit/e01e75bbb228cfbb5fc08cdd53316928761c020b) terminal: don't touch me! keep the page pool free list unobtrusive ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with
  a custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for
  its items which causes every item to be touched, which forces a full
  page-in of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free
  list entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed,
  but not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`31bdcd5`](https://github.com/ghostty-org/ghostty/commit/31bdcd5a79639bbac97c1a94e0f41d0f5ff84ca2) terminal: don't touch me! keep the page pool free list unobtrusive ([#14130](https://github.com/ghostty-org/ghostty/issues/14130)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with a
  custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for its
  items which causes every item to be touched, which forces a full page-in
  of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free list
  entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed, but
  not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`5dfb672`](https://github.com/ghostty-org/ghostty/commit/5dfb672986b57b6246d0c5d2c3c9a8fd3d138543) surface: restore mouse_shape when modifier overrides end ([@j-c-m](https://github.com/j-c-m))
  ```text
  hard-coded .default & .text overrode a previously set OSC22 pointer
  shape, this was a regression introduced in 6e8ed4e8b.
  ```
- [`6674aa3`](https://github.com/ghostty-org/ghostty/commit/6674aa3ba88e4e316af4106746e4b2091868df79) surface: update keyToMouseShape tests to expect mouse_shape ([@j-c-m](https://github.com/j-c-m))
  ```text
  Update the tests to expect the mouse_shape back, not the hardcoded
  .default or .text
  ```
- [`3a766cc`](https://github.com/ghostty-org/ghostty/commit/3a766ccf501c669298e5b648a47d217e99bff618) surface: show .text (i-beam) while shift is held without mouse tracking ([@j-c-m](https://github.com/j-c-m))
  ```text
  I think this is the expected behavoir when a custom OSC22 pointer is set. Once
  shift is released it will return to mouse_shape (whatever the pointer
  was before shit held).
  ```
- [`0fb6d29`](https://github.com/ghostty-org/ghostty/commit/0fb6d29404aab9c54c6fbce3cebd630960938117) SurfaceMouse: simplify keyToMouseShape ([@vancluever](https://github.com/vancluever))
  ```text
  keyToMouseShape was initially designed with more of a transition table
  model in mind to handle key presses/overrides based on very specific
  cursor states. This never materialized, so I think it's safe to just
  simply the process of handling overrides and/or passing along the
  current cursor state from the terminal in the event of key presses.
  
  Also removed a test that is essentially a duplicate of one before it now
  (returning current surface shape in the event of no overrides).
  ```
- [`6000034`](https://github.com/ghostty-org/ghostty/commit/600003455a9b6e7cf06b3127a490d6ab3c1b05df) surface: restore application mouse shape after modifier overrides ([#14128](https://github.com/ghostty-org/ghostty/issues/14128)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a regression of 9a6469743 introduced in 6e8ed4e8b.
  
  With this fix the mouse pointer will be restored to the previous (which
  could have be set to something else via OSC22), not a hardcoded .text or
  .default.
  
  It also will change the cursor to a text selection if shift is held even
  without mouse tracking, I think this is the expected behavior when a
  cursor is set via OSC22. (Kitty additionaly, once you start selecting
  changes to text (I-beam), this would be a follow-up if we desire to
  behave like kitty with OSC22 pointers).
  ```

## September 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33661468264), [2](https://github.com/ghostty-org/ghostty/actions/runs/33651663049)  
Summary: 2 runs • 31 commits • 8 authors

### Changes

- [`807a51e`](https://github.com/ghostty-org/ghostty/commit/807a51e3e238b7ae81fdcb03f93e2e3e7d990716) updated localization file (andrejd-magix)
- [`36015c9`](https://github.com/ghostty-org/ghostty/commit/36015c99d06d671ba961c83b74d01d7ef45dc8d3) updated revision date (andrejd-magix)
- [`ee10453`](https://github.com/ghostty-org/ghostty/commit/ee10453a26dfc8ec5d7b612f5e4a5763da7cfa82) fix unclosed quote (andrejd-magix)
- [`59141ad`](https://github.com/ghostty-org/ghostty/commit/59141ad21d7e86e48eec8ab8cbfe0095cb814303) add eu translation ([@erral](https://github.com/erral))
- [`58aa59d`](https://github.com/ghostty-org/ghostty/commit/58aa59d0e176b57d27e685dee86d3e9b7e165ef9) Update po/eu.po ([@erral](https://github.com/erral))
- [`6a51526`](https://github.com/ghostty-org/ghostty/commit/6a5152651c8744bf5058d49ee45fdb6aee63d570) Update po/eu.po ([@erral](https://github.com/erral))
- [`4c731b5`](https://github.com/ghostty-org/ghostty/commit/4c731b5d89708ae742d4809ef1ce6a81c5c551da) Update po/eu.po ([@erral](https://github.com/erral))
- [`4ffec4b`](https://github.com/ghostty-org/ghostty/commit/4ffec4bda7ed603be297564a7b23c1d21707106e) Update po/eu.po ([@erral](https://github.com/erral))
- [`f407316`](https://github.com/ghostty-org/ghostty/commit/f407316c84a313a7f9694a2d6f3e1acabc19a416) Update po/eu.po ([@erral](https://github.com/erral))
  ```text
  applying but both eskuma and eskuina are OK.
  ```
- [`63039a6`](https://github.com/ghostty-org/ghostty/commit/63039a688e765c448ca7cc80b77d83d2177e6f51) update ([@erral](https://github.com/erral))
- [`f184d3c`](https://github.com/ghostty-org/ghostty/commit/f184d3ceb5eaee08f92f6302ac2a499bcd7dc015) update ([@erral](https://github.com/erral))
- [`4da902b`](https://github.com/ghostty-org/ghostty/commit/4da902b3c9929333f7cf78147ec714f34d5619c0) update ([@erral](https://github.com/erral))
- [`9801423`](https://github.com/ghostty-org/ghostty/commit/9801423d01e0e883c32f95a210afd98919520562) update ([@erral](https://github.com/erral))
- [`7520175`](https://github.com/ghostty-org/ghostty/commit/75201750213200fba1537cf724fac5ba3dec4318) more fixes ([@erral](https://github.com/erral))
- [`3b8141f`](https://github.com/ghostty-org/ghostty/commit/3b8141fbd8e2f5770809d3df2fe0077849866dde) os/open: consume the newline when draining opener stderr ([@jzillmann](https://github.com/jzillmann))
  ```text
  takeDelimiterExclusive never consumes the delimiter: it tosses only the
  exclusive length, so the '\n' stays buffered. Once the spawned opener
  writes a single line to stderr, every subsequent call returns an empty
  slice without advancing the stream, and openThread's loop spins forever
  - one pinned core per affected open(), logging empty
  "open stderr=" warnings at tens of thousands of messages per second for
  the lifetime of the process. The thread also never reaches exe.wait(),
  so the child is never reaped.
  
  Read inclusively instead (which does consume the delimiter) and trim
  the '\n' for logging.
  
  Repro: open a link whose handler writes to stderr, e.g. an OSC 8 link
  with an unknown scheme; watch a core disappear and the unified log
  flood with "os-open: open stderr=".
  
  See discussion #14100.
  ```
- [`372d691`](https://github.com/ghostty-org/ghostty/commit/372d6914b8615610e290f8e8446d75cf4b53efeb) i18n: complete eu translation ([#14095](https://github.com/ghostty-org/ghostty/issues/14095)) ([@trag1c](https://github.com/trag1c))
- [`e212b73`](https://github.com/ghostty-org/ghostty/commit/e212b73cdaf381f2d57edc11307b06c1f520df4b) Update mk localization for v1.4 ([#14088](https://github.com/ghostty-org/ghostty/issues/14088)) ([@trag1c](https://github.com/trag1c))
  ```text
  Addressing #13766 for mk.
  ```
- [`349f026`](https://github.com/ghostty-org/ghostty/commit/349f026087d948f8f898dca3231ff91438f83ab8) os/open: consume the newline when draining opener stderr ([#14125](https://github.com/ghostty-org/ghostty/issues/14125)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the runaway-thread bug reported in #14100 (vouched there).
  
  `openThread` drains the spawned opener's stderr with
  `takeDelimiterExclusive('\n')`. That function tosses only the exclusive
  length, so the `'\n'` is never consumed. Once the child writes one line
  to stderr, every subsequent call returns an empty slice without
  advancing the stream: the `while (true)` loop spins forever — one pinned
  core per affected `open()`, logging empty `os-open: open stderr=`
  warnings at tens of thousands of messages per second for the lifetime of
  the process — and `exe.wait()` is never reached, so the child is never
  reaped.
  
  This change reads inclusively (`takeDelimiterInclusive`, which does
  consume the delimiter) and trims the `'\n'` for logging.
  
  Observed in the wild embedding libghostty on macOS: several days of
  uptime accumulated six leaked opener threads at ~70% of a core each
  (~4.4 cores), from six link clicks whose `/usr/bin/open` wrote to
  stderr. After the fix, the same workload shows zero `os-open` log
  traffic and no leaked threads.
  
  Repro without the fix: open a link whose handler writes to stderr (e.g.
  an OSC 8 link with an unknown scheme), then watch a core pin and `log
  stream --predicate 'subsystem == "com.mitchellh.ghostty"'` flood.
  
  **AI disclosure** (per `AI_POLICY.md`): the bug was diagnosed and this
  patch drafted with Claude Code (thread sampling, log analysis, and
  reading the Zig 0.16 `std.Io.Reader` source to confirm
  `takeDelimiterExclusive`/`takeDelimiterInclusive` toss semantics). I
  reviewed the analysis and the change, understand both, and verified the
  fix in a production build of the embedding app.
  ```
- [`2ba7576`](https://github.com/ghostty-org/ghostty/commit/2ba75764f6002baab9cb439dfff7ec37ac7704e8) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions) from 6.7 to 6.8.
  - [Release notes](https://github.com/flatpak/flatpak-github-actions/releases)
  - [Commits](https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3)
  
  ---
  updated-dependencies:
  - dependency-name: flatpak/flatpak-github-actions/flatpak-builder
    dependency-version: '6.8'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7358067`](https://github.com/ghostty-org/ghostty/commit/7358067d1a014e0dc36545046f2df41255f2ea26) build(deps): bump cachix/cachix-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Changelog](https://github.com/cachix/cachix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: 38b082610b782e7e93e209c35fd730d399dee866
    dependency-type: direct:production
  ...
  ```
- [`310797d`](https://github.com/ghostty-org/ghostty/commit/310797df1d912bccd63ef624395a2458e99f6cf7) macOS: fix cascading without affecting other new-window behaviours ([@bo2themax](https://github.com/bo2themax))
- [`a8b0855`](https://github.com/ghostty-org/ghostty/commit/a8b0855b630022db2933f402d9c964a111c8751c) macOS: fix cascading for HiddenTitlebarTerminalWindow ([@bo2themax](https://github.com/bo2themax))
- [`5d6615f`](https://github.com/ghostty-org/ghostty/commit/5d6615fc43ce5bc7ba9981e0c925d4e3d9dfb0d7) bash: upgrade to bash-preexec 0.7.0 ([@jparise](https://github.com/jparise))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use
  the preexec command argument, which is no longer true because we use it
  for the window title. The comment now explains the current reasoning:
  our bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  ```
- [`aafacb1`](https://github.com/ghostty-org/ghostty/commit/aafacb1cb940e3599cb4ec2c4f9cb975532a12a4) macOS: fix flickering when creating new tab with glass style ([@bo2themax](https://github.com/bo2themax))
- [`fec89f2`](https://github.com/ghostty-org/ghostty/commit/fec89f2541e412b1a2556e56742c7612118f1b72) macOS: fix flickering when creating new tab with glass style ([#14121](https://github.com/ghostty-org/ghostty/issues/14121)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A regression from #13985.
  
  
  https://github.com/user-attachments/assets/cc7d76d7-7d86-4566-921c-a6531ce4087d
  
  
  
  
  ### AI Disclosure
  
  Used Claude to investigate, I reviewed and tested.
  ```
- [`0c1909d`](https://github.com/ghostty-org/ghostty/commit/0c1909d09a0db148913b79c684db1cef58e214ee) bash: upgrade to bash-preexec 0.7.0 ([#14120](https://github.com/ghostty-org/ghostty/issues/14120)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use the
  preexec command argument, which is no longer true because we use it for
  the window title. The comment now explains the current reasoning: our
  bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  
  *AI Usage:* I asked Fable 5.1 to run a verification pass after my manual
  upgrade, and it confirmed the expected behavior.
  ```
- [`084316a`](https://github.com/ghostty-org/ghostty/commit/084316aa825a210dedc9c2fce07772cf36ade3cb) macOS: fix cascading without affecting other new-window behaviours ([#14118](https://github.com/ghostty-org/ghostty/issues/14118)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found another regression when investigating #14107 after the last fix.
  This regression appears on macOS 15 and 26 as well: **New window by
  Shortcuts.app or service menu while a window is visible would create a
  tab**.
  
  It appears that for `new-window` triggered by Shortcuts/Service, a small
  delay is needed to avoid automatic tabbing. It's either removing
  `NSWindow.userTabbingPreference == .always` completely or adding another
  "delay" for cascading. The latter should be better.
  
  Also fixes another cascading for `macos-titlebar-style = hidden`
  previously missed.
  ```
- [`41004c6`](https://github.com/ghostty-org/ghostty/commit/41004c6e2204494a2cbc0b4b78dd3b9c671d7488) build(deps): bump cachix/cachix-action from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866 ([#14116](https://github.com/ghostty-org/ghostty/issues/14116)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 5f2d7c5294214f71b873db4b969586b980625e71 to
  38b082610b782e7e93e209c35fd730d399dee866.
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/blob/master/RELEASE.md">cachix/cachix-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Release</h1>
  <ol>
  <li>
  <p>Create and push a new tag:</p>
  <pre lang="console"><code>git tag v17
  git push origin v17
  </code></pre>
  </li>
  <li>
  <p>Wait for CI to pass.</p>
  </li>
  <li>
  <p><a href="https://github.com/cachix/cachix-action/releases/new">Create
  a release</a> for the new tag.</p>
  </li>
  <li>
  <p>Move the major version tag to the latest release:</p>
  <pre lang="console"><code>git tag -fa v17
  git push origin v17 --force
  </code></pre>
  </li>
  </ol>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/38b082610b782e7e93e209c35fd730d399dee866"><code>38b0826</code></a>
  dev: cleanup tests and dev files</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/0fe030c2864be690428363af3bc7016b7b1925d8"><code>0fe030c</code></a>
  dist</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/792dafcfd01b48d3df8424b641db396602252fc3"><code>792dafc</code></a>
  deps: bump dependencies</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/b690244fb5c76a5486c33b0fbbc6fd55c857d1fe"><code>b690244</code></a>
  ci: improve Nix compatibility test coverage</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/f495f3ffa2f3810a92e5cc0abc2c5d6a2a07ec82"><code>f495f3f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/217">#217</a>
  from cachix/dependabot/github_actions/actions/checkout-7</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/9ee3c77d45d24a8b7557d22cbba3454f2a4f8a7b"><code>9ee3c77</code></a>
  chore(deps): bump actions/checkout from 6 to 7</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
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
- [`dd167cc`](https://github.com/ghostty-org/ghostty/commit/dd167cc464f8f8b30cc561fb07e09e9fb2986c14) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder from 6.7 to 6.8 ([#14115](https://github.com/ghostty-org/ghostty/issues/14115)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions)
  from 6.7 to 6.8.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/flatpak/flatpak-github-actions/releases">flatpak/flatpak-github-actions/flatpak-builder's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.8</h2>
  <ul>
  <li>Add saveCache flag</li>
  <li>Add ability to override artifact name</li>
  <li>Add buildDebugBundle flag</li>
  <li>Update tests, documentation and dependencies</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/79327416609af08178ad73b352877e51450790b3"><code>7932741</code></a>
  Update all dependencies and regenerate dist</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/09e3d61868ecd92a1c5b298a31bcc4bae17ae217"><code>09e3d61</code></a>
  readme: Don't specify setting cache key to github.sha (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/261">#261</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/23e622281a14ba5350ce2ab1ae700ac7d08cc841"><code>23e6222</code></a>
  Update runtime versions and docker images to latest</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a3ab43f58191aa8dc105e572c0a62eaac0a7555a"><code>a3ab43f</code></a>
  flatpak-builder: Add saveCache flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/8e357b1556f526e3642244bdf1a6d585be36de54"><code>8e357b1</code></a>
  ci: Remove unnecessary 'needs' from debug bundle job</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/26e19caa3a954b1d36898a0e239a67d8e856f99c"><code>26e19ca</code></a>
  ci: Add test for artifact-name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/06d246b4d5459d93c166243236f8a086d5578746"><code>06d246b</code></a>
  flatpak-builder: Add ability to override artifact name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a2622647717d8185d0f8cf01bb1ea2341e357ae0"><code>a262264</code></a>
  ci: Add job that uses build-debug-bundle</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/f7362292df659c06960a8c0dc309ab5990454a29"><code>f736229</code></a>
  flatpak-builder: Add buildDebugBundle flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/3b10954431df173eb3b564bb9adfddf3842ff91c"><code>3b10954</code></a>
  ci: Update actions to versions using Node 24</li>
  <li>See full diff in <a
  href="https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=flatpak/flatpak-github-actions/flatpak-builder&package-manager=github_actions&previous-version=6.7&new-version=6.8)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`06178ee`](https://github.com/ghostty-org/ghostty/commit/06178eeaad7648216a0da5eb73537e9dba2266cb) terminal/search: resume a complete search when history is prepended ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`b0481f5`](https://github.com/ghostty-org/ghostty/commit/b0481f5aa76a97e652bb842937ae4fa0eda68f3c) terminal/search: resume a complete search when history is prepended ([#14123](https://github.com/ghostty-org/ghostty/issues/14123)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```

## September 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33539641645), [2](https://github.com/ghostty-org/ghostty/actions/runs/33479788466)  
Summary: 2 runs • 7 commits • 4 authors

### Changes

- [`38c984e`](https://github.com/ghostty-org/ghostty/commit/38c984e6760f59a634b6538f5e8669ec829019f1) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.2 to 3.0.3.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`d4a5ff5`](https://github.com/ghostty-org/ghostty/commit/d4a5ff58b6bc4a1fcc79a69f5cff94a678d97f42) macOS: fix window cascading ([@bo2themax](https://github.com/bo2themax))
- [`d2e2488`](https://github.com/ghostty-org/ghostty/commit/d2e2488ef7539124122d346399a5e5cca152f259) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([#14098](https://github.com/ghostty-org/ghostty/issues/14098)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.2 to 3.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  <h2>3.0.2</h2>
  <p><code>3.0.2</code> is a patch release focused on release reliability
  and compatibility. It
  reuses existing draft releases when publishing prereleases, supports
  replacing
  release assets on Gitea, hardens streamed asset uploads, and provides
  clearer
  release-creation diagnostics. It also includes TypeScript, coverage, and
  tooling
  maintenance merged since <code>3.0.1</code>.</p>
  <p>This release fixes <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/795">#795</a>,
  <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/438">#438</a>,
  and <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/803">#803</a>.
  The upload transport hardening covers the
  historical failure reported in <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/790">#790</a>,
  although current hosted Node 24 runners did
  not reproduce it naturally. The diagnostics work is related to <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/786">#786</a>
  and does not
  claim a reproducible release-creation fix.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: improve release error reporting and test coverage by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/813">softprops/action-gh-release#813</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: publish existing draft releases as prereleases by <a
  href="https://github.com/godfengliang"><code>@​godfengliang</code></a>
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/801">softprops/action-gh-release#801</a></li>
  <li>fix: upload small checksum assets reliably by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/815">softprops/action-gh-release#815</a></li>
  <li>fix: replace existing release assets on Gitea by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/816">softprops/action-gh-release#816</a></li>
  <li>fix: clarify release creation 404 errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/817">softprops/action-gh-release#817</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): upgrade TypeScript to 7 by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/812">softprops/action-gh-release#812</a></li>
  <li>chore(deps): remove unused TypeScript tooling by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/814">softprops/action-gh-release#814</a></li>
  <li>dependency, Node 24 pin, and CI maintenance merged since
  <code>3.0.1</code></li>
  </ul>
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/efb35369e0ad2afab669f228072c1b0d510eae64"><code>efb3536</code></a>
  release 3.0.3 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/840">#840</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/6441963a7597ab67f36fea0287a7ae58a9bfd8fe"><code>6441963</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/839">#839</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/e5ee6bc58a36b838b92fc1217f2e4b414b5abcc8"><code>e5ee6bc</code></a>
  chore(deps): bump esbuild from 0.28.1 to 0.28.2 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/837">#837</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/d1e66170d32c9ec7bbcb7fae044d3d686ce304d3"><code>d1e6617</code></a>
  chore(deps): bump undici from 6.27.0 to 6.28.0 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/831">#831</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/64037519ba20f54c01bc1dc90342c929aac5a2fa"><code>6403751</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/835">#835</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/7c7184b6876126a5df15adc5b679dc450a393725"><code>7c7184b</code></a>
  chore(deps): bump postcss from 8.5.19 to 8.5.25 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/833">#833</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/0f3f0d2943676d58f9698b3ab590c2056023d77d"><code>0f3f0d2</code></a>
  chore(deps): bump brace-expansion from 5.0.8 to 5.0.9 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/832">#832</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/77fb938f2f95e717ce6705d2909af527263360a0"><code>77fb938</code></a>
  chore(deps): bump prettier from 3.9.5 to 3.9.6 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/830">#830</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/5a6f51711ce2ba103b78f5e9550f810679f11e0e"><code>5a6f517</code></a>
  chore(deps): bump brace-expansion from 5.0.7 to 5.0.8 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/828">#828</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/a3c91c98f80000f5b06c7fc0327c54f51c6ab7d8"><code>a3c91c9</code></a>
  chore(deps): bump the github-actions group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/825">#825</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.2&new-version=3.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`b7a680b`](https://github.com/ghostty-org/ghostty/commit/b7a680bc40b76cf7ed6b21044ac3f291ea0056be) macOS: fix window cascading ([#14106](https://github.com/ghostty-org/ghostty/issues/14106)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression from https://github.com/ghostty-org/ghostty/pull/13722
  ```
- [`451e224`](https://github.com/ghostty-org/ghostty/commit/451e224c64ddd0a9d9e9df045cdfb27c38fa8ff2) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([@bo2themax](https://github.com/bo2themax))
- [`3c1ef5b`](https://github.com/ghostty-org/ghostty/commit/3c1ef5b32fc5ea6b93d28493fabf193f595139cf) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([#14111](https://github.com/ghostty-org/ghostty/issues/14111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I don't know what happened to me, but I didn't notice that I should
  delete this🫪
  ```
- [`20abdb5`](https://github.com/ghostty-org/ghostty/commit/20abdb50a6216c450d6d4d010c41c7edf5ab15b2) Update VOUCHED list ([#14101](https://github.com/ghostty-org/ghostty/issues/14101)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14100#discussioncomment-18229353)
  from @jcollie.
  
  Vouch: @jzillmann
  ```

## August 31, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33443931836), [2](https://github.com/ghostty-org/ghostty/actions/runs/33421529945), [3](https://github.com/ghostty-org/ghostty/actions/runs/33398446520), [4](https://github.com/ghostty-org/ghostty/actions/runs/33352467854), [5](https://github.com/ghostty-org/ghostty/actions/runs/33343337803)  
Summary: 5 runs • 60 commits • 8 authors

### Changes

- [`300a0df`](https://github.com/ghostty-org/ghostty/commit/300a0dfcb6a6081ea2ead620445965d036f2ae74) Add the Serbian and Serbian Latin translations ([@kostich](https://github.com/kostich))
- [`74e0bfd`](https://github.com/ghostty-org/ghostty/commit/74e0bfdf24dc02d9cc43d5e9356b7887467abe21) Register code ownership ([@kostich](https://github.com/kostich))
- [`7aa4767`](https://github.com/ghostty-org/ghostty/commit/7aa47671482a29875664f112dd503235d8c421ff) Add new translations to locales file ([@kostich](https://github.com/kostich))
- [`635abb7`](https://github.com/ghostty-org/ghostty/commit/635abb7ee81c8f3f4969255d24e0c24bb47f56cc) Update po/sr.po ([@kostich](https://github.com/kostich))
- [`e8ba5d2`](https://github.com/ghostty-org/ghostty/commit/e8ba5d2c2749e3ac85a280a6f854d9cf3e1646cc) Standardize how config/setting/preference is translated ([@kostich](https://github.com/kostich))
- [`1ae448c`](https://github.com/ghostty-org/ghostty/commit/1ae448c23b42a14b209f50e2b2de4415bfed37c9) Fix translation of sequences ([@kostich](https://github.com/kostich))
- [`2a0371b`](https://github.com/ghostty-org/ghostty/commit/2a0371b28f2077b5553a72d8f1cb5ff878634855) Apply batched suggestions from code review ([@kostich](https://github.com/kostich))
- [`17a2474`](https://github.com/ghostty-org/ghostty/commit/17a24746c4785c24bb3ff6f6758cdccf4bcb38c1) Use the correct accusative form for inanimata ([@kostich](https://github.com/kostich))
- [`e3969ab`](https://github.com/ghostty-org/ghostty/commit/e3969ab494e62bf5a66270e6bae56665faf8fce3) Align translations for current and to left/right ([@kostich](https://github.com/kostich))
- [`84c8e7d`](https://github.com/ghostty-org/ghostty/commit/84c8e7d829ce67f7c079e40cff646e0784986e9b) Align translation for Focus ([@kostich](https://github.com/kostich))
- [`a542359`](https://github.com/ghostty-org/ghostty/commit/a5423592cde24222c0d1719f780c54434b5b5d34) libghostty: use caller allocation on native freestanding ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Native freestanding targets have neither an OS page allocator nor a usable default SMP allocator. Use the allocator supplied through libghostty for terminal page storage and make a missing C allocator fail with out-of-memory instead of instantiating hosted allocation machinery. Document that native freestanding C callers must supply an allocator for allocating operations.
  ```
- [`3376153`](https://github.com/ghostty-org/ghostty/commit/3376153a44e5269b9aee5e6d2524954c171e717b) build: support native freestanding libghostty-vt ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Native freestanding targets cannot emit shared libraries and do not provide an OS page size, stack unwinder, hosted SIMD dependencies, or filesystem-backed Kitty graphics. Build only the static artifact for those targets, define the minimum alignment used for terminal pages, disable hosted-only defaults, and install the public headers with the archive.
  ```
- [`10b7158`](https://github.com/ghostty-org/ghostty/commit/10b7158e8cd57f21f7327c73a6b2cdb2f498fdae) ci: cross-compile freestanding libghostty-vt ([@Uzaaft](https://github.com/Uzaaft))
- [`fc7bfa6`](https://github.com/ghostty-org/ghostty/commit/fc7bfa60b4b5b40183387e52b782612f417812f3) ci: move freestanding build into test workflow ([@Uzaaft](https://github.com/Uzaaft))
- [`028af92`](https://github.com/ghostty-org/ghostty/commit/028af92ce3876ce1627163ce777f516b8218b410) terminal: clarify page allocator fallback ([@Uzaaft](https://github.com/Uzaaft))
- [`e8709b1`](https://github.com/ghostty-org/ghostty/commit/e8709b1f9ee1a1275c8ca2b3c22f40a4e4663137) Merge remote-tracking branch 'upstream/main' into add-serbian-translation ([@kostich](https://github.com/kostich))
- [`90f7759`](https://github.com/ghostty-org/ghostty/commit/90f775976328cd90b8cf12637b776f0689f2f4f8) Fix HTML/URL acronyms as agreed ([@kostich](https://github.com/kostich))
- [`8bf7e51`](https://github.com/ghostty-org/ghostty/commit/8bf7e517f0571c605a206aae00977c2e8e0cc7ce) Regenerate sr@latin.po from sr.po ([@kostich](https://github.com/kostich))
- [`5e02d00`](https://github.com/ghostty-org/ghostty/commit/5e02d0014de36ab776ac947e60ae5641c9674ca4) ci: require freestanding libghostty-vt builds ([@Uzaaft](https://github.com/Uzaaft))
- [`458f079`](https://github.com/ghostty-org/ghostty/commit/458f079f176632bf98d503bef1726472be505f07) Use the informal form ([@kostich](https://github.com/kostich))
- [`2c854a1`](https://github.com/ghostty-org/ghostty/commit/2c854a1aa42c96ec484f136fdd38d060bd6a7683) freestanding support ([#14076](https://github.com/ghostty-org/ghostty/issues/14076)) ([@mitchellh](https://github.com/mitchellh))
- [`149c9f5`](https://github.com/ghostty-org/ghostty/commit/149c9f562af3933493eb7dd275259eee9ce26f79) terminal: extract whole-terminal search orchestration from the search thread ([@mitchellh](https://github.com/mitchellh))
- [`32601cd`](https://github.com/ghostty-org/ghostty/commit/32601cd79a23618d0e64fd0c73bfd47e713be1ef) terminal/c: add search wrapper implementing the whole-terminal search API ([@mitchellh](https://github.com/mitchellh))
- [`cdef14a`](https://github.com/ghostty-org/ghostty/commit/cdef14a1fddd223b63fec60a8f59832a7e2a4db9) Remove X-Generator from the sr.po file ([@kostich](https://github.com/kostich))
- [`f0c918f`](https://github.com/ghostty-org/ghostty/commit/f0c918fc4b72c6c7e746db68f753d102a02bb206) terminal/c: allow freeing a search and its terminal in any order ([@mitchellh](https://github.com/mitchellh))
- [`f920291`](https://github.com/ghostty-org/ghostty/commit/f9202919f71951e7b5af2837afc30f181ad2168c) libghostty: add ghostty_search_* terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`674abd8`](https://github.com/ghostty-org/ghostty/commit/674abd8a1940c928d3a0fb0ca27d6ed6dfc5e3c0) example: add c-vt-search demonstrating the terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`76d9fce`](https://github.com/ghostty-org/ghostty/commit/76d9fcefef592617360577c9208490dc44d04a65) libghostty: set the search needle via ghostty_search_set, drop GhosttySearchOptions ([@mitchellh](https://github.com/mitchellh))
- [`4b51f52`](https://github.com/ghostty-org/ghostty/commit/4b51f521d4080f1bbdb113180f1b109404b6ad7f) libghostty: add terminal search API ([#14097](https://github.com/ghostty-org/ghostty/issues/14097)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This exposes the terminal search API through libghostty C and Zig APIs.
  
  This was previously available through the Zig APIs but forced our
  threading model. I've now extracted the full terminal search state to a
  new `terminal.search.TerminalSearch` structure so threading isn't
  forced. The C API is completely new.
  
  ## Example (C)
  
  ```c
  GhosttySearch search;
  ghostty_search_new(NULL, &search, terminal);
  
  GhosttyString needle = { (const uint8_t *)"error", 5 };
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_NEEDLE, &needle);
  ghostty_search_run(search);
  
  // Find bar chrome: "k of n"
  size_t total, idx;
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_TOTAL_MATCHES, &total);
  
  // Enter: select the next match (wraps, scrolls the viewport if needed)
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_SELECT_NEXT, NULL);
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_SELECTED_INDEX, &idx);
  
  ghostty_search_free(search);
  ```
  ````
- [`8168115`](https://github.com/ghostty-org/ghostty/commit/81681158b1f04b9900c3e58ba6db790384f5b6f5) Add Serbian translation ([#13842](https://github.com/ghostty-org/ghostty/issues/13842)) ([@00-kat](https://github.com/00-kat))
  ```text
  ## Summary
  - Adds Serbian translations for both Cyrillic (`sr`) and Latin
  (`sr@latin`) scripts, registered in `src/os/i18n_locales.zig` and
  `CODEOWNERS`.
  - `po/sr@latin.po` is generated from `po/sr.po` with `msgfilter
  recode-sr-latin` and should not be translated by hand.
  - Replaces the closed #13030; strings are rebased onto current `main`.
  
  Cc @slowdub for a review.
  
  EDIT: AI disclosure: I used Cursor (Grok 4.6) for mechanical repo work
  only, not for writing the Serbian translations. The agent fetched
  ghostty-org/ghostty, branched from current main, ran msgmerge on
  po/sr.po against the template, generated po/sr@latin.po with msgfilter
  recode-sr-latin, registered sr / sr@latin in src/os/i18n_locales.zig and
  CODEOWNERS, rebased my three commits onto later main, pushed the branch,
  and opened this PR (I had intended to open the PR myself, s***** thing
  ignored my instructions). I translated and reviewed sr.po and the Latin
  file is a recode of that catalog, not a separate translation since
  Serbian Cyrillic can be perfectly transcoded to the Latin script via
  [recode-sr-latin](https://linux.die.net/man/1/recode-sr-latin).
  ```
- [`d23af9e`](https://github.com/ghostty-org/ghostty/commit/d23af9e397dfe06760ce2ad8f54fb178e7d82e62) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`80b8e49`](https://github.com/ghostty-org/ghostty/commit/80b8e4957625195e85727a6c28200f3bf6c54941) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`5546750`](https://github.com/ghostty-org/ghostty/commit/5546750a75cf44f881c43f44204aa6a9012ab296) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`1510d2b`](https://github.com/ghostty-org/ghostty/commit/1510d2b42a284c183e1fd71749290c220e23ce3d) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`b5817a3`](https://github.com/ghostty-org/ghostty/commit/b5817a35a493eb68dbe3737802384792c561ef06) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`f6244f7`](https://github.com/ghostty-org/ghostty/commit/f6244f7d7f2d555382192e701cd6bc33859b64b6) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`320ba75`](https://github.com/ghostty-org/ghostty/commit/320ba75dc925096bc9b31d4de756b2779380dcd3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`1054be4`](https://github.com/ghostty-org/ghostty/commit/1054be4b6ff66c63f4f703c38d06a547c12d79ba) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`6758251`](https://github.com/ghostty-org/ghostty/commit/675825163b3aa975fe66f577e99b75982b15d45b) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`768bc2e`](https://github.com/ghostty-org/ghostty/commit/768bc2ed475ede520dbe0695184a9e2c4aec9128) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`4c696b9`](https://github.com/ghostty-org/ghostty/commit/4c696b90c5c2db61fd0929f102e9701bbcdfb809) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`9af9348`](https://github.com/ghostty-org/ghostty/commit/9af934813a32262ab525673840ccd76ed7df2f52) Merge from upstream ([@mohshami](https://github.com/mohshami))
- [`58f43d5`](https://github.com/ghostty-org/ghostty/commit/58f43d56289d234271e1e829712e2f043c88278f) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`c8c4526`](https://github.com/ghostty-org/ghostty/commit/c8c4526e43e6f832ab5d88759cde98a7b2129886) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`81d28be`](https://github.com/ghostty-org/ghostty/commit/81d28beaa2e3c507299d0c1a5271c2af718212e3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`5f54958`](https://github.com/ghostty-org/ghostty/commit/5f5495826c7ad143c113c25f40cf2ef39d55e459) terminal: fix living item over-count in RefCountedSet.addWithId ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of `addWithIdContext`
  incremented `living` unconditionally even if `upsert` resolved the value
  to an item that was already alive under a different ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style memory
  to be over-provisioned.
  ```
- [`abac4c2`](https://github.com/ghostty-org/ghostty/commit/abac4c2cb8122540d99f30645581918022a31fc8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`0dc2032`](https://github.com/ghostty-org/ghostty/commit/0dc2032e6ab5f197f1d93f8eb1f1735a2b5091e1) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`0254a7f`](https://github.com/ghostty-org/ghostty/commit/0254a7f06f8b955f9107090581b22ad14f010fe8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`dfccdb2`](https://github.com/ghostty-org/ghostty/commit/dfccdb2d4dfdfa9da14664ae06f56f3db923d1e2) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600) ([@mohshami](https://github.com/mohshami))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Run zig fmt
  
  Move true/false options for copy-on-select to the compatibility handler
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/Surface.zig
  
  
  Update src/Surface.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/Surface.zig
  
  
  Update src/Surface.zig
  
  
  Reorder switch items
  
  Apply comment from kat
  
  Remove redundent code
  ```
- [`e80ce2e`](https://github.com/ghostty-org/ghostty/commit/e80ce2ed4cc603c0b52f9cb344f39c64048478e0) Fix build error ([@mohshami](https://github.com/mohshami))
- [`f6113ea`](https://github.com/ghostty-org/ghostty/commit/f6113ea2f5da697351ffe9dd91653427c4d27f90) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600), more flexible copy-on-select and middle-click-action ([#12604](https://github.com/ghostty-org/ghostty/issues/12604)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Note: No AI was used, Even though I don't know Zig, I looked at the code
  and the modifications seemed easy enough
  
  Closes #12600
  ```
- [`c290639`](https://github.com/ghostty-org/ghostty/commit/c2906398be63f7eed567eee294ec09f291844b95) terminal: fix living item over-count in RefCountedSet.addWithId ([#14081](https://github.com/ghostty-org/ghostty/issues/14081)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of
  `addWithIdContext` incremented `living` unconditionally even if `upsert`
  resolved the value to an item that was already alive under a different
  ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style
  memory to be over-provisioned.
  
  cc @qwerasd205 since its ref counted set, but I did this work manually
  ❤️
  ```
- [`0525c18`](https://github.com/ghostty-org/ghostty/commit/0525c18f60ade456a484d9dc26e751d3c1b3993d) i18n: adjust and extend Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`c50288c`](https://github.com/ghostty-org/ghostty/commit/c50288c35fd147482dbd7e30cfcc414c7612c7dd) i18n: address comments for Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`2a51bdf`](https://github.com/ghostty-org/ghostty/commit/2a51bdf1266df638e9ba49ad5cfad6ee7c780ca3) i18n: return Ghostty to Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`1026a00`](https://github.com/ghostty-org/ghostty/commit/1026a00c19b3cbf254c0b85dced92ab8e63d77bf) i18n: adjust Ukrainian translations ([@chernetskyi](https://github.com/chernetskyi))
- [`d4d8f62`](https://github.com/ghostty-org/ghostty/commit/d4d8f62262cb1a974a7d2470d5f79f811fab15e4) i18n: adjust and extend Ukrainian translation ([#13854](https://github.com/ghostty-org/ghostty/issues/13854)) ([@trag1c](https://github.com/trag1c))
- [`e8aa098`](https://github.com/ghostty-org/ghostty/commit/e8aa098674a42e2b4ed1b8c42f4224564ad9fc1e) Update VOUCHED list ([#14092](https://github.com/ghostty-org/ghostty/issues/14092)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14091#discussioncomment-18212381)
  from @pluiedev.
  
  Denounce: @thomas-trijindev
  ```
- [`ec3e384`](https://github.com/ghostty-org/ghostty/commit/ec3e384d2d7d86206fc3c71aa23a76b7bdb5eae9) Sync CODEOWNERS vouch list ([#14090](https://github.com/ghostty-org/ghostty/issues/14090)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @jakeriksen
  - @Kleshzz
  ```

## August 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33336500501), [2](https://github.com/ghostty-org/ghostty/actions/runs/33304806060), [3](https://github.com/ghostty-org/ghostty/actions/runs/33301014311), [4](https://github.com/ghostty-org/ghostty/actions/runs/33290237904), [5](https://github.com/ghostty-org/ghostty/actions/runs/33288542884), [6](https://github.com/ghostty-org/ghostty/actions/runs/33286306984)  
Summary: 6 runs • 15 commits • 7 authors

### Changes

- [`c181983`](https://github.com/ghostty-org/ghostty/commit/c181983253129f2803891a2d801951244ae5313c) build: update Sparkle to 2.9.6 and pin SPM ([@bo2themax](https://github.com/bo2themax))
- [`7fd93e0`](https://github.com/ghostty-org/ghostty/commit/7fd93e09ca6cbca7c4c4c0dbf2817ca49a82a2a4) build: update Sparkle to 2.9.6 and pin SPM ([#14082](https://github.com/ghostty-org/ghostty/issues/14082)) ([@mitchellh](https://github.com/mitchellh))
- [`3e2c0fa`](https://github.com/ghostty-org/ghostty/commit/3e2c0fa2db39215ee3b8098181baca7feb04ec27) gtk: do not warn when gtk-xft-dpi is -1 ([@mgsloan](https://github.com/mgsloan))
  ````text
  Before this change, ghostty frequently logs the following warning, even though a `gtk-xft-dpi` value of `-1` is valid and indicates default scaling.
  
  ```
  warning(gtk_ghostty_surface): gtk-xft-dpi has invalid value (-1), using default
  ```
  
  From [the gtk docs](https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html):
  
  > The font resolution, in 1024 * dots/inch.
  >
  > -1 to use the default value.
  ````
- [`860cfb1`](https://github.com/ghostty-org/ghostty/commit/860cfb1d7958d0c5af09ff23488cfa6ea6665b46) Address review feedback ([@mgsloan](https://github.com/mgsloan))
- [`8af6897`](https://github.com/ghostty-org/ghostty/commit/8af6897c0afc63037a8a3efee4162a380e3a4572) gtk: do not warn when gtk-xft-dpi is -1 ([#14085](https://github.com/ghostty-org/ghostty/issues/14085)) ([@jcollie](https://github.com/jcollie))
  ````text
  Before this change, ghostty frequently logs the following warning, even
  though a `gtk-xft-dpi` value of `-1` is valid and indicates default
  scaling.
  
  ```
  warning(gtk_ghostty_surface): gtk-xft-dpi has invalid value (-1), using default
  ```
  
  From [the gtk
  docs](https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html):
  
  > The font resolution, in 1024 * dots/inch.
  >
  > -1 to use the default value.
  ````
- [`6d850fe`](https://github.com/ghostty-org/ghostty/commit/6d850fef7780f3461ee526eba16077ea9d7df8a6) Update VOUCHED list ([#14084](https://github.com/ghostty-org/ghostty/issues/14084)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14083#discussioncomment-18204946)
  from @jcollie.
  
  Vouch: @mgsloan
  ```
- [`97f57ed`](https://github.com/ghostty-org/ghostty/commit/97f57edccc10cb5ccef34d9d4c94276748bbd953) renderer: vsync unfocused surfaces while dirty ([@j-c-m](https://github.com/j-c-m))
  ```text
  6ae1784f4
  
  Unfocused surfaces stopped the CVDisplayLink and encoded a GPU
  frame on every PTY wakeup. A burst of close writes became that many
  Metal submits instead of one vsync.
  
  Keep the link running while the surface is visible and dirty or
  animating, whether or not it is focused. Idle surfaces still park.
  Focus continues to gate cursor blink, custom-shader animation, and
  QoS.
  ```
- [`166d2fe`](https://github.com/ghostty-org/ghostty/commit/166d2fe34d65bd1fa393fd8a213c57bc6119dfb9) build: update Sparkle to 2.9.4 ([@Svector-anu](https://github.com/Svector-anu))
- [`090fca4`](https://github.com/ghostty-org/ghostty/commit/090fca451d2c63bc2a5ccec23ea54cedce62c6a6) terminal/kitty: validate POSIX shared memory names ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update shared memory name validation according to the new spec:
  
  https://github.com/kovidgoyal/kitty/commit/22042970cf3a4668d02a1a7bcccca778ec864c21
  ```
- [`7035647`](https://github.com/ghostty-org/ghostty/commit/70356472faa9768eb37577430602fa30495eca81) build: update Sparkle to 2.9.4 ([#14072](https://github.com/ghostty-org/ghostty/issues/14072)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update the macOS Sparkle dependency from 2.9.0 to 2.9.4.
  
  This keeps the Swift package resolution and all tag/tip release workflow
  downloads aligned on the same version. Sparkle 2.9.2 included fixes for
  GHSA-g3hp-f6mg-559v and GHSA-hg88-v3cw-3qrh; 2.9.4 is the current stable
  release.
  
  Validation:
  - verified the 2.9.4 release contains
  `Sparkle-for-Swift-Package-Manager.zip`
  - verified the lockfile revision matches the 2.9.4 tag
  - `jq empty` on `Package.resolved`
  - `git diff --check`
  
  I could not run Xcode package resolution locally because the active
  developer directory is Command Line Tools rather than a full Xcode
  installation.
  ```
- [`ec7929c`](https://github.com/ghostty-org/ghostty/commit/ec7929c9c2fffb1c46096f94cc9bdd6d57c85b72) terminal/kitty: validate POSIX shared memory names ([#14080](https://github.com/ghostty-org/ghostty/issues/14080)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update shared memory name validation according to the new spec:
  
  
  https://github.com/kovidgoyal/kitty/commit/22042970cf3a4668d02a1a7bcccca778ec864c21
  ```
- [`83c5671`](https://github.com/ghostty-org/ghostty/commit/83c56715773d2b5f0e8b1d5bee68424514bb43e3) renderer: vsync unfocused surfaces while dirty ([#14068](https://github.com/ghostty-org/ghostty/issues/14068)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A follow on for #14035, we can now fix a long standing
  effiency/performance bug now that we park the display link while idle.
  This actually could cause "animated" un-focused windows to use more GPU
  than their focused counterparts. (AI Agent interfaces seem to love
  animation).
  
  6ae1784f4
  
  Unfocused surfaces stopped the CVDisplayLink and encoded a GPU frame on
  every PTY wakeup. A burst of close writes became that many Metal submits
  instead of one vsync.
  
  Keep the link running while the surface is visible and dirty or
  animating, whether or not it is focused. Idle surfaces still park.
  ```
- [`98cd670`](https://github.com/ghostty-org/ghostty/commit/98cd670c0c2ccdd3f22c40c65a3306e933643ada) Update VOUCHED list ([#14079](https://github.com/ghostty-org/ghostty/issues/14079)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14078#discussioncomment-18203195)
  from @jcollie.
  
  Vouch: @and-rs
  ```
- [`094d175`](https://github.com/ghostty-org/ghostty/commit/094d175efa506f87c296fd8a51371c68eea191b9) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`0a76c31`](https://github.com/ghostty-org/ghostty/commit/0a76c311527a20727764e3281eb4efa8c350058a) Update iTerm2 colorschemes ([#14077](https://github.com/ghostty-org/ghostty/issues/14077)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260824-153547-75c93ee
  ```

## August 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33261764252), [2](https://github.com/ghostty-org/ghostty/actions/runs/33259592247)  
Summary: 2 runs • 5 commits • 3 authors

### Changes

- [`7b47213`](https://github.com/ghostty-org/ghostty/commit/7b47213f94058c3715205ce8fa73f7ae581a652c) Update VOUCHED list ([#14074](https://github.com/ghostty-org/ghostty/issues/14074)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14072#issuecomment-5463405035)
  from @bo2themax.
  
  Vouch: @Svector-anu
  ```
- [`6cd684d`](https://github.com/ghostty-org/ghostty/commit/6cd684d5d3b2a83c9966b6c5ba239d36fbd937a9) gtk: fix stale pointers to property bindings ([@dkinzler](https://github.com/dkinzler))
  ```text
  Previously, the property binding created in `Surface.bindIsSplit` would
  get freed automatically when the source object (the SplitTree widget)
  got finalized. A subsequent call to `bindIsSplit` could then cause a
  crash by using the stale pointer to the binding. This bug could e.g. be
  triggered by dragging the surface from a single-surface tab to another
  tab.
  
  We now create an extra reference to the binding object so that Surface
  essentially owns the binding and is responsible for freeing it.
  
  Updated the binding in `SurfaceScrolledWindow` to use the same pattern.
  That one was probably fine, because the binding is only created once,
  but let's be safe.
  ```
- [`caf48a4`](https://github.com/ghostty-org/ghostty/commit/caf48a41ee5c3861c786270d64bac950f2513012) main: fix inverted allow_stack_tracing condition ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.16.0 update dropped the negation from the std default
  (!strip_debug_info), disabling stack traces in every unstripped build.
  
  AI disclosure: Claude Fable was used to diagnose the problem and find the
  fix. Commit message was written by me.
  
  Claude-Session: https://claude.ai/code/session_01QfzQME46DQXwMWa43bQaa3
  ```
- [`069497e`](https://github.com/ghostty-org/ghostty/commit/069497e0ca7d02c073d69e80003c1e0f0b067ee6) gtk: fix stale pointers to property bindings ([#14065](https://github.com/ghostty-org/ghostty/issues/14065)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14037 where dragging the surface from a tab with just a single
  surface to another tab causes a crash.
  
  The cause of the crash is a stale pointer to the property binding
  created in `Surface.bindIsSplit`. When the surface is moved,
  `SplitTree.moveSplit` first updates the two split tree data structures
  of the source/target tab and then calls `bindIsSplit` to bind the
  `is-split` property of the moved surface to the `SplitTree` widget in
  the target tab. When `bindIsSplit` is called, the `SplitTree` widget in
  the source tab has already been destroyed (because the source tab is now
  empty) which causes the old binding to be freed automatically and the
  pointer `Surface.is_split_binding` becomes stale. `bindIsSplit` then
  tries to run `is_split_binding.unbind()` which causes the crash.
  
  When you create a binding with `bindProperty`, the binding itself owns
  the initially created reference and it gets freed when the source or
  target object of the binding is finalized. To prevent this, we now
  create an extra reference to the binding object so that the Surface
  widget owns it and is responsible for freeing it. The binding can still
  get severed automatically, but the binding object itself will not be
  destroyed. This is the solution mentioned in the [GObject
  docs](https://docs.gtk.org/gobject/method.Object.bind_property.html).
  Alternatively, using a WeakRef for the pointer would have also worked.
  
  Updated the binding in `SurfaceScrolledWindow` to use the same pattern.
  That one was probably fine, because the binding should only be created
  once, but it doesn't hurt to be safe.
  
  I reproduced the crash on KDE, on Hyprland I just got a glib critical
  error message about the invalid pointer. That probably has to do with
  what exactly happens to the freed memory, or maybe differing versions.
  
  #### AI Disclosure
  
  Code and comments were written by myself, used GPT5.6 in researching
  gobject binding lifecycles.
  ```
- [`3baff3a`](https://github.com/ghostty-org/ghostty/commit/3baff3a069cb64a9d3739c2ff25423524b3b80ee) main: fix inverted allow_stack_tracing condition ([#14069](https://github.com/ghostty-org/ghostty/issues/14069)) ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.16.0 update dropped the negation from the std default
  (!strip_debug_info), disabling stack traces in every unstripped build.
  
  AI disclosure: Claude Fable was used to diagnose the problem and find
  the fix. Commit message was written by me.
  
  
  Claude-Session: https://claude.ai/code/session_01QfzQME46DQXwMWa43bQaa3
  ```

## August 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33201228282), [2](https://github.com/ghostty-org/ghostty/actions/runs/33140987507)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`777929a`](https://github.com/ghostty-org/ghostty/commit/777929a8fe603574474f6e1c9c0a35c08af1a2d9) macOS: review windows when closing multiple tabs ([@bo2themax](https://github.com/bo2themax))
- [`4540d49`](https://github.com/ghostty-org/ghostty/commit/4540d499ae463ad7b90f28f6f852f64f844c160f) macOS: review windows when closing multiple tabs ([#14062](https://github.com/ghostty-org/ghostty/issues/14062)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We can also make close undoable when quitting, i'll add it as a follow
  up pr.
  
  <img width="573" height="450" alt="Xnip2026-08-28_19-25-02"
  src="https://github.com/user-attachments/assets/3b4f34f4-9ee6-4180-beb7-f90e98c8aa40"
  />
  ```
- [`eb722cb`](https://github.com/ghostty-org/ghostty/commit/eb722cb26dfe3fb5dc481181ae463940492cd742) terminal: mark the previous row dirty when clearing its spacer head ([@fornwall](https://github.com/fornwall))
  ```text
  Erasing a wrapped wide character at the start of a row (ECH or DCH)
  also clears the spacer head it left at the end of the previous row,
  but that row was never marked dirty. With both rows visible, an
  incremental render kept the stale spacer head on screen until
  something unrelated redrew that row.
  
  The clearing happens in the row-start branch of splitCellBoundary.
  clearCells doesn't do dirty tracking, and both callers only mark
  the cursor row, so mark the previous row at the point it's mutated.
  
  The added dirty assertions fail without the fix.
  ```
- [`76e568b`](https://github.com/ghostty-org/ghostty/commit/76e568b475fe88f5506be33ad1a684f3c1eae85e) terminal: mark the previous row dirty when clearing its spacer head ([#14054](https://github.com/ghostty-org/ghostty/issues/14054)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erasing a wrapped wide character at the start of a row (`ECH` or `DCH`)
  also clears the spacer head it left at the end of the previous row, but
  that row was never marked dirty. With both rows visible, an incremental
  render kept the stale spacer head on screen until something unrelated
  redrew that row.
  
  The clearing happens in the row-start branch of `splitCellBoundary`.
  `clearCells` doesn't do dirty tracking, and both callers only mark the
  cursor row, so mark the previous row at the point it's mutated.
  
  The added dirty assertions fail without the fix.
  
  ## AI Disclaimer
  Claude did the heavy lifting - identifying the root cause, generating
  code and description. I reviewed and iterated on it to move around and
  tweak tests, comments and reduce verboseness. Verified the end user
  visible behaviour improvement with a script that coloured the wide
  character, which made the stale rendering visible until a switch to the
  alt screen and back cleared it it.
  ```

