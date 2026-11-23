> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 23, 2026 at 01:20 UTC.

## November 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/45058933013), [2](https://github.com/ghostty-org/ghostty/actions/runs/44979798109)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`c56b66e`](https://github.com/ghostty-org/ghostty/commit/c56b66e630daed7155c0df3c44ed13e4776b376d) ci: compare committed `.po` files in translation check ([@trag1c](https://github.com/trag1c))
- [`4dd09c4`](https://github.com/ghostty-org/ghostty/commit/4dd09c4688ada3315daf235135b6cb15cacfa9a2) ci: compare committed `.po` files in translation check ([#15308](https://github.com/ghostty-org/ghostty/issues/15308)) ([@jcollie](https://github.com/jcollie))
  ```text
  Previously, a `.po` file that was missing strings from the template
  could never fail CI, because the `msgcmp` loop ran on files that had
  just been regenerated, and so only the initial `.pot` comparison was
  actually doing something useful (though that by itself has been mostly
  sufficient; it's moreso about correctness). Such cases are now caught.
  
  | Scenario                              | `main` | This PR |
  | ------------------------------------- | :----: | :-----: |
  | Do nothing                            | ✅     | ✅      |
  | Delete an entry from a `.po` file     | ✅     | ❌      |
  | Add to source, regen `.pot` only      | ✅     | ❌      |
  | Remove from source, regen `.pot` only | ✅     | ❌      |
  | Add to source, regen nothing          | ❌     | ❌      |
  | Remove from source, regen nothing     | ✅     | ❌      |
  
  **AI disclosure:** Claude Haiku 5.5 brought this up. I verified its
  claims and wrote the fix myself.
  ```
- [`3283674`](https://github.com/ghostty-org/ghostty/commit/328367470e915571a8e009117ef28c5ee1bac61a) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`11ed660`](https://github.com/ghostty-org/ghostty/commit/11ed660d99fd0dd8dadcaf456db31b71f0f21beb) Update iTerm2 colorschemes ([#15311](https://github.com/ghostty-org/ghostty/issues/15311)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261116-150709-494b809
  ```

## November 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44945642861)  
Summary: 1 runs • 4 commits • 1 authors

### Changes

- [`0c7d595`](https://github.com/ghostty-org/ghostty/commit/0c7d595bf4f9119bbe3b44bf017c4f3816dbf3d6) terminal/kitty: read drag and drop drop data lazily ([@jcollie](https://github.com/jcollie))
  ```text
  Drops captured every representation eagerly when they landed, so the
  native drag session ended at drop time and only a curated set of MIME
  types could be served. Drop data is now read from the native drop when
  the program requests it, queued as kitty does.
  
  The drag_and_drop effect gains a data_request event for this, and one
  command can now produce several events. The effect may serve a request
  from within the callback, writing its answer with Handler.ptyWriter.
  The MIME types the program accepted for a drag are now available too,
  for the embedder to choose what to read.
  ```
- [`13069b8`](https://github.com/ghostty-org/ghostty/commit/13069b880070ec6f9d127b05fee01eebeebbe524) terminal/kitty: split the drag and drop state from the drop target ([@jcollie](https://github.com/jcollie))
  ```text
  The drop target's behavior lived in methods on State, next to the
  command dispatch, and the slot being null was how an unregistered
  client was told apart. Move the drop target into a DropTarget with its
  own methods and a registered flag, leaving State as the chunk
  reassembly plus the drop target, and move State, its events and
  handleCommand into dnd_state.zig.
  
  Commands from an unregistered client now run against an empty state on
  the stack, which answers with the same errors as before without
  allocating, and the state is freed once the client is no longer
  registered. Embedders reach the drop target through state.drop.
  ```
- [`5b0690d`](https://github.com/ghostty-org/ghostty/commit/5b0690da08e11d9ca570a0fe3c2851da74ed8ade) terminal: protocol independent drag and drop drop effect ([@jcollie](https://github.com/jcollie))
  ```text
  The effect that tells the embedder about drops was tied to Kitty's
  protocol, so it is now a protocol-independent drop effect whose events
  carry their details. The protocol module does the mapping both ways,
  from its events to the drop effect's and from native drop activity back
  to the protocol, so every embedder shares it rather than doing its own.
  
  Without a drop effect OSC 72 is now ignored entirely, so programs fall
  back instead of registering with a terminal that can never deliver a
  drop.
  ```
- [`6d24420`](https://github.com/ghostty-org/ghostty/commit/6d244209978e599277904ff3ced7b8a2ebcc528d) terminal/kitty: read drag and drop drop data lazily ([#14536](https://github.com/ghostty-org/ghostty/issues/14536)) ([@jcollie](https://github.com/jcollie))
  ```text
  Drops captured every representation eagerly when they landed, so the
  native drag session ended at drop time and only a curated set of MIME
  types could be served. Drop data is now read from the native drop when
  the program requests it, queued as kitty does.
  
  The effect that tells the embedder about drops was tied to Kitty's
  protocol, so it is now a protocol-independent drop effect whose events
  carry their details.
  
  Without a drop effect OSC 72 is now ignored entirely, so programs fall
  back instead of registering with a terminal that can never deliver a
  drop.
  
  Zig API only.
  
  The plan for this PR series is as follows:
  
  1. Get current drop support in the Zig libghostty-vt API pulling data
  lazily (this PR).
    a. convert existing drop support to lazily read.
  b. extract state that will be shared with drag support to a new shared
  file
  c. add a protocol-independent layer in case there's ever another DnD
  protocol
  4. Add drag support to the Zig libghostty-vt API.
  5. Add support to the C libghostty-vt API for drag & drop (including a C
  example).
  6. Run kitten dnd in CI.
  7. Connect DnD into the apprt core.
  8. Add support for DnD in the GTK apprt.
  9. Add support for remote drops.
  10. Add support for remote drags.
  11. Wire the GTK apprt for remote drag & drop.
  
  Once 5 has been accomplished someone can add the macOS DnD support.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```

## November 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44838354067)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`9ad3c42`](https://github.com/ghostty-org/ghostty/commit/9ad3c422222e45b32c5f9ab9f4cd32e0e3694ef7) Update VOUCHED list ([#15298](https://github.com/ghostty-org/ghostty/issues/15298)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15297#discussioncomment-19786018)
  from @jcollie.
  
  Vouch: @gourneau
  ```

## November 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44626228815), [2](https://github.com/ghostty-org/ghostty/actions/runs/44569520203), [3](https://github.com/ghostty-org/ghostty/actions/runs/44554316282)  
Summary: 3 runs • 6 commits • 5 authors

### Changes

- [`47495a5`](https://github.com/ghostty-org/ghostty/commit/47495a53f4f1ae4d26946f1f717334b0e812128f) i18n: remove dead code in `os/i18n.zig` ([@trag1c](https://github.com/trag1c))
- [`d69f9ed`](https://github.com/ghostty-org/ghostty/commit/d69f9ed83ca7275fa5afbba0fa968d0d9ada9f5a) i18n: remove dead code in `os/i18n.zig` ([#15289](https://github.com/ghostty-org/ghostty/issues/15289)) ([@jcollie](https://github.com/jcollie))
  ```text
  Originally introduced in #6619, slipped under the radar but never used.
  ```
- [`e15b14b`](https://github.com/ghostty-org/ghostty/commit/e15b14ba53ec3c1f6faedd51b8c9db427e219f9e) terminal: hash hyperlink strings in one update ([@teddytennant](https://github.com/teddytennant))
- [`2f5c8b1`](https://github.com/ghostty-org/ghostty/commit/2f5c8b17f75e39df9fb5ac81e55814f47b2d939c) terminal: hash hyperlink strings in one update ([#15285](https://github.com/ghostty-org/ghostty/issues/15285)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Hyperlink IDs and URIs are hashed on main with `autoHashStrat(.Deep)`,
  which ends up giving Wyhash one byte at a time. This hashes each string
  in one `update` and its length, which produces the same hash with far
  less work.
  
  `ghostty-bench +terminal-stream` on 50 MB of `ls -laR
  --hyperlink=always` output speeds up 429 ms to 323 ms on an intel
  i7-11700K.
  ```
- [`5e12d3a`](https://github.com/ghostty-org/ghostty/commit/5e12d3a624facb05074e82def5e54f574db73c6e) font/shaper/coretext: invalidate font cache by grid id, not address ([@orion0616](https://github.com/orion0616))
  ```text
  Shaper.getFont decided whether its cached CoreText fonts were still valid
  by comparing the SharedGrid pointer. A grid is heap-allocated and freed
  by SharedGridSet, so a new grid can be allocated at the address of a
  freed one. The shaper then kept fonts from the old grid, and since
  fallback face indexes are assigned in discovery order, the same index can
  refer to a different font in the new grid. Glyph indexes from one font
  were then rendered with another, showing the wrong glyphs.
  
  This can happen in practice when the display DPI flips back and forth in
  a short time, e.g. 72 -> 144 -> 72 on wake from sleep with a Retina and a
  non-Retina display. The 144 dpi grid is never shaped with, and the new
  72 dpi grid lands on the old grid's address (discussion #15018).
  
  Give each SharedGrid a process-unique id assigned in init, and compare
  that instead of the pointer. Add a regression test that reinitializes
  the grid in place with a different embedded font and shapes again.
  ```
- [`3576c31`](https://github.com/ghostty-org/ghostty/commit/3576c311811e2358a7819aa78d0aab81f4b4b7c8) font/shaper/coretext: invalidate font cache by grid id, not address ([#15280](https://github.com/ghostty-org/ghostty/issues/15280)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In 1.4.0 on macOS, text sometimes gets garbled. Only characters rendered
  with fallback fonts (e.g. Japanese and symbols) are affected.
  
  When a grid is recreated, the CoreText shaper may reuse fonts it cached
  for the old grid. This happens because the shaper decides whether the
  grid is the same one by its address; if the new grid happens to be
  allocated at the same address, the cache is reused.
  Since fallback face indexes are assigned in the order they are
  discovered, the same index may point to a different font in the new
  grid. As a result, glyph IDs from one font are rendered with a different
  font.
  
  I stopped using the grid's address for this check. Each grid now gets an
  id from an incrementing counter, and the shaper compares that id
  instead.
  
  I reproduced this on my machine by waking my Mac from sleep while it was
  connected to both a built-in Retina display and an external non-Retina
  display: the new grid was allocated at the old address and the cache was
  reused. With the counter instead of the address, the text stayed correct
  under the same conditions.
  I also added a regression test that replaces the grid at the same
  address and then shapes text again. It fails without the fix and passes
  with it.
  
  Discussion: #15018
  Vouch request: #15276
  
  AI disclosure: I used Claude Code for investigating the cause, writing
  the patch and testing. I read and understood the whole diff. I wrote
  this description in Japanese, translated it with DeepL, and Claude Code
  reviewed and corrected the English.
  ```

## November 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44324235659), [2](https://github.com/ghostty-org/ghostty/actions/runs/44247634968)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`3f2fe14`](https://github.com/ghostty-org/ghostty/commit/3f2fe1472882349ca140a83deca150573a7018fb) Update VOUCHED list ([#15277](https://github.com/ghostty-org/ghostty/issues/15277)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15276#discussioncomment-19710658)
  from @jcollie.
  
  Vouch: @orion0616
  ```
- [`d9d56b6`](https://github.com/ghostty-org/ghostty/commit/d9d56b6c26d778e360257f119885eee24000505d) build(deps): bump hustcer/milestone-action from 3.2 to 3.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [hustcer/milestone-action](https://github.com/hustcer/milestone-action) from 3.2 to 3.3.
  - [Release notes](https://github.com/hustcer/milestone-action/releases)
  - [Changelog](https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/hustcer/milestone-action/compare/2f38355153344ccaaa44b5b5fcff9f604dff1b45...815f8224db33f809c5063c66e2e4f530208f401e)
  
  ---
  updated-dependencies:
  - dependency-name: hustcer/milestone-action
    dependency-version: '3.3'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7a8ff4d`](https://github.com/ghostty-org/ghostty/commit/7a8ff4d992edd2aad7537e5bef73ec911aa126bf) build(deps): bump hustcer/milestone-action from 3.2 to 3.3 ([#15271](https://github.com/ghostty-org/ghostty/issues/15271)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [hustcer/milestone-action](https://github.com/hustcer/milestone-action)
  from 3.2 to 3.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/releases">hustcer/milestone-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.3</h2>
  <h2>[3.3] - 2026-11-15</h2>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade nushell from 0.115.1 to 0.117.0</li>
  <li>Upgrade hustcer/setup-nu from v3.27 to v3.30</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md">hustcer/milestone-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.3] - 2026-11-15</h2>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade nushell from 0.115.1 to 0.117.0</li>
  <li>Upgrade hustcer/setup-nu from v3.27 to v3.30</li>
  </ul>
  <h2>[3.2] - 2026-08-25</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li>Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li>Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li>Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li>Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li>Upgrade Nu to 0.115.1</li>
  </ul>
  <h2>[3.1] - 2026-01-23</h2>
  <h3>Documentation</h3>
  <ul>
  <li>Update milestone-action version in README (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/162">#162</a>)</li>
  </ul>
  <h3>Features</h3>
  <ul>
  <li>Break before sleep when milestone found</li>
  </ul>
  <h3>Miscellaneous Tasks</h3>
  <ul>
  <li>Update README.md (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/166">#166</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Update Nu to 0.109.1</li>
  <li>Update Nushell to 0.110.0 (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/167">#167</a>)</li>
  <li>Upgrade hustcer/setup-nu to v3.22</li>
  </ul>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.0] - 2025-10-26</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/815f8224db33f809c5063c66e2e4f530208f401e"><code>815f822</code></a>
  chore: update CHANGELOG.md</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/13801ea24afcdea4b80608b936582475ba55bdd3"><code>13801ea</code></a>
  Bump to v3.3</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/916b5dc899cb31ea0c72f86d09288bf76c9a9a5e"><code>916b5dc</code></a>
  deps: Upgrade hustcer/setup-nu &amp; Nu to latest version</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/93633102e028c297578c8e156312d16ba7dc2998"><code>9363310</code></a>
  deps: Upgrade hustcer/setup-nu &amp; Nu to latest version</li>
  <li>See full diff in <a
  href="https://github.com/hustcer/milestone-action/compare/2f38355153344ccaaa44b5b5fcff9f604dff1b45...815f8224db33f809c5063c66e2e4f530208f401e">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=hustcer/milestone-action&package-manager=github_actions&previous-version=3.2&new-version=3.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## November 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44197412683), [2](https://github.com/ghostty-org/ghostty/actions/runs/44177280756), [3](https://github.com/ghostty-org/ghostty/actions/runs/44140849876), [4](https://github.com/ghostty-org/ghostty/actions/runs/44116065599)  
Summary: 4 runs • 6 commits • 4 authors

### Changes

- [`c688263`](https://github.com/ghostty-org/ghostty/commit/c68826391717a5f12e3408000e6623f3df926d6c) benchmark: add scrollback-search benchmark ([@teddytennant](https://github.com/teddytennant))
- [`f3e1f65`](https://github.com/ghostty-org/ghostty/commit/f3e1f65bb602ac3d441ffdd5f9645bef66a39648) benchmark: add scrollback-search benchmark ([#15267](https://github.com/ghostty-org/ghostty/issues/15267)) ([@jcollie](https://github.com/jcollie))
  ```text
  Adds `ghostty-bench +scrollback-search` (#15262). It loads `--data` into
  the primary screen, then searches all of it with `ScreenSearch`.
  
  - `typing` searches each prefix of `--needle` from scratch, like the
  search thread does while you type.
  - `report` prints per-prefix timings, including time in `feed`, which
  runs under the terminal lock.
  - `--compress` compresses history first.
  
  On a full default scrollback of Ghostty's source (47,560 rows,
  i7-11700K), each keystroke takes about 18 ms, 15.5 of it in `feed`.
  Compressed, 27 ms and 24 ms.
  
  AI disclosure: I had fable 5.2 help me explore the codebase and review
  my code
  ```
- [`9ba17be`](https://github.com/ghostty-org/ghostty/commit/9ba17be7b95dab894f259329b4a568a6667f276c) gtk: preserve IME commits triggered by key release ([@aohanhongzhi](https://github.com/aohanhongzhi))
- [`47b5c20`](https://github.com/ghostty-org/ghostty/commit/47b5c2026927b0d8a38d224c5d34008589fd6d19) gtk: preserve IME commits triggered by key release ([#15246](https://github.com/ghostty-org/ghostty/issues/15246)) ([@jcollie](https://github.com/jcollie))
  ```text
  When client preedit is disabled in Fcitx5, tapping Shift to commit
  pending Latin input can lose the text in Ghostty. For example, typing
  `abc` in WowType and tapping Shift produces no terminal input, even
  though the IME commits `abc`.
  
  Without client preedit, `im_composing` remains false. A commit emitted
  synchronously during `filterKeypress` is therefore buffered as ordinary
  key text. When the triggering event is a key release, legacy key
  encoding discards that text.
  
  Track key releases separately in `IMKeyEvent` and send their IME commits
  through the existing independent-text path. Press/repeat commits retain
  their existing handling.
  
  Validation:
  - Reproduced with Ghostty 1.3.1, Fcitx5/WowType, GTK 4.14.5 and
  libadwaita 1.5.0 under an isolated Xvfb/D-Bus session: client preedit
  off loses `abc`; client preedit on commits it.
  - Backported the fix to 1.3.1 and built with Zig 0.15.2. With client
  preedit off, left Shift, right Shift and Return each commit `abc`;
  typing `XYZ` after the left-Shift switch produces `abcXYZ`.
  - The installed backport was also confirmed working by the affected
  user.
  - On this PR's main-based change, `zig fmt --check` and `git diff
  --check` pass. Main's build/tests could not complete locally because
  they require libadwaita >= 1.7, while this system has 1.5.0. Runtime
  results above are for the backport, not main.
  
  AI disclosure: OpenAI Codex assisted with investigation, implementation,
  building, automated reproduction, and this PR description. The user
  reproduced the original problem and confirmed the installed fix.
  ```
- [`356b3b3`](https://github.com/ghostty-org/ghostty/commit/356b3b399290c12a2723a613ebee0c49eeee4b72) Update VOUCHED list ([#15269](https://github.com/ghostty-org/ghostty/issues/15269)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/15268#issuecomment-6956126500)
  from @mitchellh.
  
  Vouch: @davidbrochart
  ```
- [`b634352`](https://github.com/ghostty-org/ghostty/commit/b634352b739dbe4a0389ae7c6ae4585462cfa96e) Update VOUCHED list ([#15263](https://github.com/ghostty-org/ghostty/issues/15263)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15262#discussioncomment-19683634)
  from @jcollie.
  
  Vouch: @teddytennant
  ```

