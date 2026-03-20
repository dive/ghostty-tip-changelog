> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 20, 2026 at 12:10 UTC.

## March 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23327743605), [2](https://github.com/ghostty-org/ghostty/actions/runs/23326999168)  
Summary: 2 runs • 18 commits • 5 authors

### Changes

- [`f168b3c`](https://github.com/ghostty-org/ghostty/commit/f168b3c098eae1db30811173ac7cc5d5ac4da3c2) vt: add ghostty_terminal_get for reading terminal state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a typed data query API to the terminal C interface, following
  the same OutType pattern used by the OSC command data API. The new
  ghostty_terminal_get function takes a GhosttyTerminalData tag and
  an output pointer, returning GhosttyResult.
  
  Currently exposes cols, rows, cursor x/y position, and cursor
  pending wrap state. The GhosttyTerminalData enum is placed with the
  other types in the header (before functions) per the ordering
  convention.
  ```
- [`7f36e8b`](https://github.com/ghostty-org/ghostty/commit/7f36e8bd43bdc52aa3398125ce8c42e5211adceb) vt: add style C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose the terminal Style struct to the C API as GhosttyStyle, a
  sized struct with foreground, background, and underline colors
  (as tagged unions) plus boolean text decoration flags.
  
  Add ghostty_style_default() to obtain the default style and
  ghostty_style_is_default() to check whether a style has all
  default values. Wire both through c/style.zig, main.zig, and
  lib_vt.zig with the corresponding header in vt/style.h.
  ```
- [`d62f6df`](https://github.com/ghostty-org/ghostty/commit/d62f6df1d5370b6ec7a5de80dd15718a424e727e) vt: expose cursor_style via terminal_get ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add cursor_style to TerminalData, returning the current SGR style
  of the cursor (the style applied to newly printed characters) as a
  GhosttyStyle.
  
  Refactor the C style conversion helpers: replace the standalone
  convertStyle and convertColor functions with fromStyle and fromColor
  initializers on the Style and Color extern structs respectively.
  ```
- [`d827225`](https://github.com/ghostty-org/ghostty/commit/d827225573b673bc5c1756f2d14971638a472d53) vt: expand padding for color union to 64-bit to allow for a pointer ([@mitchellh](https://github.com/mitchellh))
- [`5c8b9f3`](https://github.com/ghostty-org/ghostty/commit/5c8b9f3f434abee1e70f454ec00301010ea01edf) vt: add GhosttyCell and GhosttyRow C API with data getters ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add opaque GhosttyCell (uint64_t) and GhosttyRow (uint64_t) types that
  bitcast to the internal packed Cell and Row structs from page.zig. Each
  type has a corresponding data enum and getter function following the
  same pattern as ghostty_terminal_get.
  
  ghostty_cell_get supports extracting codepoint, content tag, wide
  property, has_text, has_styling, style_id, has_hyperlink, protected,
  and semantic_content. ghostty_row_get supports wrap, wrap_continuation,
  grapheme, styled, hyperlink, semantic_prompt, kitty_virtual_placeholder,
  and dirty.
  
  The cell and row types and functions live in a new screen.h header,
  separate from terminal.h, with terminal.h including screen.h for
  convenience.
  ```
- [`057f227`](https://github.com/ghostty-org/ghostty/commit/057f227145fcce8d92678c16591d936f54f202b8) terminal: convert Point to lib.Enum/lib.TaggedUnion with C header ([@mitchellh](https://github.com/mitchellh))
- [`0400de2`](https://github.com/ghostty-org/ghostty/commit/0400de28b40bc47b0fcd0f5a78a908413cb86be6) vt: add ghostty_terminal_cell for point-based cell lookup ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new C API function ghostty_terminal_cell that retrieves the
  opaque cell and row values at a given point in the terminal grid.
  The point is a tagged union supporting active, viewport, screen, and
  history coordinate systems.
  ```
- [`2a952b4`](https://github.com/ghostty-org/ghostty/commit/2a952b4dfeac0acda22e67779dabdc415757a0a7) bash: move __ghostty_preexec_hook into __ghostty_hook ([@jparise](https://github.com/jparise))
  ```text
  We previously used a readonly variable (__ghostty_ps0) to define the
  best __ghostty_preexec_hook expansion for the current bash version.
  
  This works pretty well, but it had the downside of managing another
  variable (#11258).
  
  We can instead simplify this a bit by moving this into __ghostty_hook. I
  didn't take that approach originally because I wanted to avoid the bash
  version check on each command, but slightly loosening our guard check to
  just look for "__ghostty_preexec_hook" (rather than the full expansion
  expression) means we can bury the bash version check to the cold path.
  
  One small gap here is that we may not update PS0 to the correct syntax
  if we start switching between significantly different bash versions in
  interactive subshells, but that seems like a pretty rare case to handle
  given the benefits of this approach.
  ```
- [`df8813b`](https://github.com/ghostty-org/ghostty/commit/df8813bf1b0a0526ee5da340b4398f85f0852c52) vt: replace ghostty_terminal_cell with GhosttyGridRef API ([@mitchellh](https://github.com/mitchellh))
- [`5498248`](https://github.com/ghostty-org/ghostty/commit/549824842dd72b2e77caf0d443a3b3951480c764) vt: add style and grapheme accessors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_grid_ref_style and ghostty_grid_ref_graphemes to the grid
  ref C API, allowing callers to extract the full style and grapheme
  cluster directly from a grid reference without manually resolving
  the page internals.
  ```
- [`93c597c`](https://github.com/ghostty-org/ghostty/commit/93c597ce6bb36179065d93a465d6ee679f7472f7) example: add grid reference traversal example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a c-vt-grid-ref example that demonstrates the terminal and grid
  reference APIs end-to-end. The example creates a small 10x3 terminal,
  writes text with mixed styles via VT sequences, then iterates over
  every cell in the active area using ghostty_terminal_grid_ref. For
  each cell it extracts the codepoint, and for each row it inspects
  the wrap flag and the style bold attribute.
  
  The grid_ref.h defgroup gains a @snippet reference to the new example,
  and vt.h gets the corresponding @example entry and @ref listing.
  ```
- [`d2a29de`](https://github.com/ghostty-org/ghostty/commit/d2a29de95989d739d2b2dfcf2df8762fbbb9b1c8) libghostty: terminal data, grid point and cell inspection APIs ([#11676](https://github.com/ghostty-org/ghostty/issues/11676)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds a complete set of APIs for inspecting individual cells and
  rows in the terminal grid from C. Callers can now resolve any point in
  the grid to a reference, then extract codepoints, grapheme clusters,
  styles, wide-character state, semantic prompt tags, and row-level
  metadata like wrap and dirty flags.
  
  This also adds a robust `ghostty_terminal_get` API for extracting
  information like rows, cols, active screen, cursor information, etc.
  from the terminal.
  
  ## Example
  
  ```c
  // Write bold red text via SGR sequences
  const char *text = "\033[1;31mHello\033[0m";
  ghostty_terminal_vt_write(terminal, (const uint8_t *)text, strlen(text));
  
  // Resolve cell (0,0) to a grid reference
  GhosttyGridRef ref = GHOSTTY_INIT_SIZED(GhosttyGridRef);
  GhosttyPoint pt = {
    .tag = GHOSTTY_POINT_TAG_ACTIVE,
    .value = { .coordinate = { .x = 0, .y = 0 } },
  };
  ghostty_terminal_grid_ref(terminal, pt, &ref);
  
  // Read the codepoint ('H')
  GhosttyCell cell;
  ghostty_grid_ref_cell(&ref, &cell);
  uint32_t codepoint = 0;
  ghostty_cell_get(cell, GHOSTTY_CELL_DATA_CODEPOINT, &codepoint);
  
  // Read the resolved style (bold=true, fg=red)
  GhosttyStyle style = GHOSTTY_INIT_SIZED(GhosttyStyle);
  ghostty_grid_ref_style(&ref, &style);
  assert(style.bold);
  ```
  
  ## API Changes
  
  ### New Types
  
  | Type | Description |
  |------|-------------|
  | `GhosttyCell` | Opaque 64-bit cell value |
  | `GhosttyRow` | Opaque 64-bit row value |
  | `GhosttyCellData` | Enum for `ghostty_cell_get` data kinds (codepoint,
  content tag, wide, has_text, etc.) |
  | `GhosttyCellContentTag` | Cell content kind (codepoint, grapheme, bg
  color palette/RGB) |
  | `GhosttyCellWide` | Cell width (narrow, wide, spacer tail/head) |
  | `GhosttyCellSemanticContent` | Semantic content type (output, input,
  prompt) |
  | `GhosttyRowData` | Enum for `ghostty_row_get` data kinds (wrap,
  grapheme, styled, dirty, etc.) |
  | `GhosttyRowSemanticPrompt` | Row-level semantic prompt state |
  | `GhosttyGridRef` | Sized struct — resolved reference to a cell
  position in the page structure |
  | `GhosttyPoint` | Tagged union specifying a grid position in a given
  coordinate system |
  | `GhosttyPointTag` | Coordinate system tag: `ACTIVE`, `VIEWPORT`,
  `SCREEN`, `HISTORY` |
  | `GhosttyPointCoordinate` | x/y coordinate pair |
  | `GhosttyStyleId` | Style identifier type (uint16) |
  
  ### New Functions
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_cell_get` | Extract typed data from a cell (codepoint, wide,
  style ID, etc.) |
  | `ghostty_row_get` | Extract typed data from a row (wrap, dirty,
  semantic prompt, etc.) |
  | `ghostty_terminal_grid_ref` | Resolve a `GhosttyPoint` to a
  `GhosttyGridRef` |
  | `ghostty_grid_ref_cell` | Extract the `GhosttyCell` from a grid ref |
  | `ghostty_grid_ref_row` | Extract the `GhosttyRow` from a grid ref |
  | `ghostty_grid_ref_graphemes` | Get the full grapheme cluster
  (codepoints) for the cell |
  | `ghostty_grid_ref_style` | Get the resolved `GhosttyStyle` for the
  cell |
  ````
- [`7966740`](https://github.com/ghostty-org/ghostty/commit/7966740b48b287f1ed1aa2a355afde3b81197933) bash: move __ghostty_preexec_hook into __ghostty_hook ([#11674](https://github.com/ghostty-org/ghostty/issues/11674)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We previously used a readonly variable (__ghostty_ps0) to define the
  best __ghostty_preexec_hook expansion for the current bash version.
  
  This worked pretty well, but it had the downside of managing another
  variable (#11258).
  
  We can instead simplify this a bit by moving this into __ghostty_hook. I
  didn't take that approach originally because I wanted to avoid the bash
  version check on each command, but slightly loosening our guard check to
  just look for "__ghostty_preexec_hook" (rather than the full expansion
  expression) means we can bury the bash version check to the cold path.
  
  One small gap here is that we may not update PS0 to the correct syntax
  if we start switching between significantly different bash versions in
  interactive subshells, but that seems like a pretty rare case to handle
  given the benefits of this approach.
  ```
- [`10e6938`](https://github.com/ghostty-org/ghostty/commit/10e69384d7e6a59253dda2cc00482210f6e63ee7) build(deps): bump namespacelabs/nscloud-setup from 0.0.11 to 0.0.12 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup) from 0.0.11 to 0.0.12.
  - [Release notes](https://github.com/namespacelabs/nscloud-setup/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-setup/compare/f378676225212387f1283f4da878712af2c4cd60...df198f982fcecfb8264bea3f1274b56a61b6dfdc)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-setup
    dependency-version: 0.0.12
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`7c14aec`](https://github.com/ghostty-org/ghostty/commit/7c14aecd3fb96cbc6c9c2035ebe830a38f1693e1) build(deps): bump namespacelabs/nscloud-setup-buildx-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-setup-buildx-action](https://github.com/namespacelabs/nscloud-setup-buildx-action) from 0.0.22 to 0.0.23.
  - [Release notes](https://github.com/namespacelabs/nscloud-setup-buildx-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-setup-buildx-action/compare/f5814dcf37a16cce0624d5bec2ab879654294aa0...d059ed7184f0bc7c8b27e8810cea153d02bcc6dd)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-setup-buildx-action
    dependency-version: 0.0.23
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`4531594`](https://github.com/ghostty-org/ghostty/commit/4531594d51f76b4350f6ec23d8916b59ae261ddc) build(deps): bump namespacelabs/nscloud-setup-buildx-action from 0.0.22 to 0.0.23 ([#11673](https://github.com/ghostty-org/ghostty/issues/11673)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-setup-buildx-action](https://github.com/namespacelabs/nscloud-setup-buildx-action)
  from 0.0.22 to 0.0.23.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup-buildx-action/commit/d059ed7184f0bc7c8b27e8810cea153d02bcc6dd"><code>d059ed7</code></a>
  Update to node24 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-setup-buildx-action/issues/15">#15</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-setup-buildx-action/compare/f5814dcf37a16cce0624d5bec2ab879654294aa0...d059ed7184f0bc7c8b27e8810cea153d02bcc6dd">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-setup-buildx-action&package-manager=github_actions&previous-version=0.0.22&new-version=0.0.23)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`e9eac7d`](https://github.com/ghostty-org/ghostty/commit/e9eac7d4758c5b7692c59e4dda89b2184ad18960) build(deps): bump namespacelabs/nscloud-setup from 0.0.11 to 0.0.12 ([#11672](https://github.com/ghostty-org/ghostty/issues/11672)) ([@jcollie](https://github.com/jcollie))
  ```text
  [//]: # (dependabot-start)
  ⚠️  **Dependabot is rebasing this PR** ⚠️
  
  Rebasing might not happen immediately, so don't worry if this takes some
  time.
  
  Note: if you make any changes to this PR yourself, they will take
  precedence over the rebase.
  
  ---
  
  [//]: # (dependabot-end)
  
  Bumps
  [namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup)
  from 0.0.11 to 0.0.12.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup/commit/df198f982fcecfb8264bea3f1274b56a61b6dfdc"><code>df198f9</code></a>
  Update to node24 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-setup/issues/10">#10</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-setup/compare/f378676225212387f1283f4da878712af2c4cd60...df198f982fcecfb8264bea3f1274b56a61b6dfdc">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-setup&package-manager=github_actions&previous-version=0.0.11&new-version=0.0.12)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`1f89ce9`](https://github.com/ghostty-org/ghostty/commit/1f89ce91d97065f04c196b84c391c7212bd50de0) Update VOUCHED list ([#11675](https://github.com/ghostty-org/ghostty/issues/11675)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11671#discussioncomment-16218675)
  from @jcollie.
  
  Vouch: @unphased
  ```

## March 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23303726826), [2](https://github.com/ghostty-org/ghostty/actions/runs/23294986782)  
Summary: 2 runs • 6 commits • 4 authors

### Changes

- [`c08a211`](https://github.com/ghostty-org/ghostty/commit/c08a21180aa98ee813bc97bf04e1d0c31ec2f65d) build(deps): bump cachix/cachix-action from 16 to 17 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 16 to 17.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Commits](https://github.com/cachix/cachix-action/compare/3ba601ff5bbb07c7220846facfa2cd81eeee15a1...1eb2ef646ac0255473d23a5907ad7b04ce94065c)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: '17'
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`b1ad24e`](https://github.com/ghostty-org/ghostty/commit/b1ad24e24f3c04d854ed2c516fd0b947cf800420) bash: emit 133;P (instead of 133;A) under ble.sh ([@jparise](https://github.com/jparise))
  ```text
  ble.sh performs its own cursor positioning so we get multiple newlines
  with 133;A's fresh-line behavior. ble.sh is a large enough project to
  justify this additional, unambiguous conditional.
  
  See: akinomyoga/ble.sh#684
  See: wezterm/wezterm#5072
  ```
- [`2bbbca3`](https://github.com/ghostty-org/ghostty/commit/2bbbca369d5fc67da8f2084f0b8973ef4619ba78) bash: emit 133;P (instead of 133;A) under ble.sh ([#11644](https://github.com/ghostty-org/ghostty/issues/11644)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ble.sh performs its own cursor positioning so we get multiple newlines
  with 133;A's fresh-line behavior. ble.sh is a large enough project to
  justify this additional, unambiguous conditional.
  
  See: akinomyoga/ble.sh#684
  See: wezterm/wezterm#5072
  ```
- [`c2e9de2`](https://github.com/ghostty-org/ghostty/commit/c2e9de224eaf09a2ce3e7cb2f6c26d6d577ed8f0) build(deps): bump cachix/cachix-action from 16 to 17 ([#11643](https://github.com/ghostty-org/ghostty/issues/11643)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 16 to 17.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/releases">cachix/cachix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v17</h2>
  <h2>What's Changed</h2>
  <h3>Breaking changes</h3>
  <ul>
  <li>Upgrade action to use Node 24 by <a
  href="https://github.com/sandydoo"><code>@​sandydoo</code></a> in <a
  href="https://redirect.github.com/cachix/cachix-action/pull/212">cachix/cachix-action#212</a>
  <a
  href="https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/">https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/cachix-action/compare/v16...v17">https://github.com/cachix/cachix-action/compare/v16...v17</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/1eb2ef646ac0255473d23a5907ad7b04ce94065c"><code>1eb2ef6</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/212">#212</a>
  from cachix/upgrade-node-24</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/75ce400143912180b47fa504676215ca47e1634f"><code>75ce400</code></a>
  dist: re-build using esbuild targeting node24</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/2b33705a8232e51ac94414b3b8c203d0a5e42ca3"><code>2b33705</code></a>
  deps: update devenv inputs</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/04937db281cae63d98e660f990648ab4eef1cec1"><code>04937db</code></a>
  breaking: update action to Node 24</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/ca2e51995f0edefbb31bc858102abd109580c99c"><code>ca2e519</code></a>
  ci: use 25.11 for tests</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/e7c5c1add25228c774d40ae0adbd520ea7c919c0"><code>e7c5c1a</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/208">#208</a>
  from cachix/dependabot/github_actions/actions/checkout-6</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/bea8a506457e59a062336709ee10a5677fd9a59e"><code>bea8a50</code></a>
  ci: allow running tests manually and with a custom nix version</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/2e35755955435b7976b76834528c38a0fcf725c0"><code>2e35755</code></a>
  chore(deps): bump actions/checkout from 5 to 6</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/3ba601ff5bbb07c7220846facfa2cd81eeee15a1...1eb2ef646ac0255473d23a5907ad7b04ce94065c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/cachix-action&package-manager=github_actions&previous-version=16&new-version=17)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`c9729fb`](https://github.com/ghostty-org/ghostty/commit/c9729fbd269d72a20eb4a53846dd3cd7ae1dfc4a) ci: use local git commands for path-filter action ([@jparise](https://github.com/jparise))
  ```text
  Passing a `token` value causes this action to use the GitHub REST API,
  which is subject to rate limits. We can chew through that allowance
  quickly (1,000 requests/hour) given that we run two of these actions per
  workflow run.
  
  `token` defaults to the workflow's token, but by setting it explicitly
  to an empty string, the action will instead use `git diff` to determine
  the modified paths. This works fine for our case because we're already
  running the checkout action, so we have an up-to-date repository view.
  
  This also has the advantage of working around the 300 files GitHub REST
  API limit for listing changed files.
  
  Ref: https://github.com/dorny/paths-filter
  ```
- [`69e0673`](https://github.com/ghostty-org/ghostty/commit/69e0673478b4e92d1a5f0a1e1c41091218f853af) ci: use local git commands for path-filter action ([#11652](https://github.com/ghostty-org/ghostty/issues/11652)) ([@jcollie](https://github.com/jcollie))
  ```text
  Passing a `token` value causes this action to use the GitHub REST API,
  which is subject to rate limits. We can chew through that allowance
  quickly (1,000 requests/hour) given that we run two of these actions per
  workflow run.
  
  `token` defaults to the workflow's token, but by setting it explicitly
  to an empty string, the action will instead use `git diff` to determine
  the modified paths. This works fine for our case because we're already
  running the checkout action, so we have an up-to-date repository view.
  
  This also has the advantage of working around the 300 files GitHub REST
  API limit for listing changed files.
  
  Ref: https://github.com/dorny/paths-filter
  ```

## March 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23257063138), [2](https://github.com/ghostty-org/ghostty/actions/runs/23255200023), [3](https://github.com/ghostty-org/ghostty/actions/runs/23253545237), [4](https://github.com/ghostty-org/ghostty/actions/runs/23248995028), [5](https://github.com/ghostty-org/ghostty/actions/runs/23222237491)  
Summary: 5 runs • 17 commits • 5 authors

### Changes

- [`2d51401`](https://github.com/ghostty-org/ghostty/commit/2d514013d51e9805305b5e93c5bd9eb9ada774a4) fix "open terminal here" action on Plasma ([@heddxh](https://github.com/heddxh))
- [`4b1e48b`](https://github.com/ghostty-org/ghostty/commit/4b1e48b71e7e7b0317651a8c3173defff9ffffaa) swap arguments ([@heddxh](https://github.com/heddxh))
- [`c9e1006`](https://github.com/ghostty-org/ghostty/commit/c9e1006213eb9234209924c91285d6863e59ce4c) Fix: correct "Open Ghostty Here" Dolphin action for Plasma ([#11614](https://github.com/ghostty-org/ghostty/issues/11614)) ([@jcollie](https://github.com/jcollie))
  ```text
  See #11594
  
  The change allows "Open Ghostty Here" Dolphin action to launch new
  ghostty window with gtk single instance.
  ```
- [`1f3a3b4`](https://github.com/ghostty-org/ghostty/commit/1f3a3b41f785d10906678394d13c180657d35210) bash: handle PROMPT_COMMAND ending in a newline ([@jparise](https://github.com/jparise))
  ```text
  We need to handle on more case: when an existing PROMPT_COMMAND ends in
  a newline, we don't want to append a ; because that already counts as a
  command separator.
  
  We now handle all of these PROMPT_COMMAND cases:
  
  - Ends with ; — no ; added
  - Ends with \n or other whitespace — no ; added
  - Ends with a command name — ; added as separator
  
  See: #11245
  ```
- [`3dc6998`](https://github.com/ghostty-org/ghostty/commit/3dc69981d2abf7e66eeb973229b86c6bb847c734) bash: handle PROMPT_COMMAND ending in a newline ([#11621](https://github.com/ghostty-org/ghostty/issues/11621)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We need to handle on more case: when an existing PROMPT_COMMAND ends in
  a newline, we don't want to append a ; because that already counts as a
  command separator.
  
  We now handle all of these PROMPT_COMMAND cases:
  
  - Ends with ; — no ; added
  - Ends with \n or other whitespace — no ; added
  - Ends with a command name — ; added as separator
  
  See: #11245
  ```
- [`e01046a`](https://github.com/ghostty-org/ghostty/commit/e01046af158cef2e324ae153e73381d544ed3cc6) docs: extract focus encoding example into standalone project ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract the inline code example from focus.h into a standalone
  buildable example at example/c-vt-encode-focus. The header now
  uses a Doxygen @snippet tag to include the code from the example
  source file, so the documentation stays in sync with code that
  is verified to compile and run.
  ```
- [`bb3b3ba`](https://github.com/ghostty-org/ghostty/commit/bb3b3ba6150b55c251e05fd205a1da5b8c34ec5f) ci: dynamically discover example directories for build-examples ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the hardcoded matrix list in the build-examples job with a
  dynamic list-examples job that discovers all subdirectories under
  example/ at runtime. This uses ls/jq to produce a JSON array and
  fromJSON() to feed it into the matrix, so new examples are picked
  up automatically without updating the workflow.
  ```
- [`15b8976`](https://github.com/ghostty-org/ghostty/commit/15b8976d643de69df2168aa99320557e6b95bc02) docs: extract inline code examples into standalone projects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract inline @code blocks from vt headers (size_report.h, modes.h,
  sgr.h, paste.h, mouse.h, key.h) into standalone buildable examples
  under example/. Each header now uses Doxygen @snippet tags to include
  code from the example source files, keeping documentation in sync
  with code that is verified to compile and run.
  
  New example projects: c-vt-size-report and c-vt-modes. Existing
  examples (c-vt-sgr, c-vt-paste, c-vt-mouse-encode, c-vt-key-encode)
  gain snippet markers so their code can be referenced from the headers.
  Conceptual snippets in key.h, mouse.h, and key/encoder.h that show
  terminal-state usage patterns remain inline since they cannot be
  compiled standalone.
  ```
- [`ceef806`](https://github.com/ghostty-org/ghostty/commit/ceef8065b02a8cf007e7a6ed3f6e71965fa20ad6) ci: filter build-examples to directories with build.zig.zon ([@mitchellh](https://github.com/mitchellh))
  ```text
  The dynamic example directory discovery added in bb3b3ba included
  all subdirectories under example/, but some (wasm-key-encode,
  wasm-sgr) are pure HTML examples with no build.zig.zon. Running
  zig build in those directories falls back to the root build.zig
  and attempts a full GTK binary build, which fails on CI.
  
  Filter the listing to only include directories that contain a
  build.zig.zon file so non-Zig examples are excluded from the
  build matrix.
  ```
- [`f037f41`](https://github.com/ghostty-org/ghostty/commit/f037f41f78fd96a98b4f612f40e117f80af6ca31) Add example AGENTS file ([@mitchellh](https://github.com/mitchellh))
- [`383a7e1`](https://github.com/ghostty-org/ghostty/commit/383a7e14a7e4043dbfbd45aaa19781bba442952b) example: add README ([@mitchellh](https://github.com/mitchellh))
- [`996ce03`](https://github.com/ghostty-org/ghostty/commit/996ce03f0b9e9407c0164e4a3c4f341ed91cc817) example: rename some examples ([@mitchellh](https://github.com/mitchellh))
- [`9e6c875`](https://github.com/ghostty-org/ghostty/commit/9e6c875f334c43f1b1ea4cb8d23c1ec07c6d9f9c) Ensure all examples in libghostty C docs build and run in CI ([#11609](https://github.com/ghostty-org/ghostty/issues/11609)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This moves all our examples away from embedded source to `@snippet` and
  files so that we can use our CI to actually run the builds and keep them
  working.
  
  Note: I used AI to extract the examples, and it did some weird merging
  stuff. It all works but I want to make sure all these examples are still
  human friendly so I need to go back and review all that. I clicked
  through the web docs and they look good, just need to verify the GitHub
  flow.
  ```
- [`a74f437`](https://github.com/ghostty-org/ghostty/commit/a74f43760edce5a4b51d73c44cc39066cb24539e) Update VOUCHED list ([#11623](https://github.com/ghostty-org/ghostty/issues/11623)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11622#issuecomment-4082875090)
  from @00-kat.
  
  Vouch: @EkaterinePapava
  ```
- [`a1d7ad9`](https://github.com/ghostty-org/ghostty/commit/a1d7ad92434a6c1c5b5a2b436a15e0573790b6cc) terminal: extract size report encoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  Size report escape sequences were previously formatted inline in
  Termio.sizeReportLocked, and termio.Message carried a duplicate enum for
  report styles. That made the encoding logic harder to reuse and kept
  the style type scoped to termio.
  
  Move the encoding into terminal.size_report and export it through
  terminal.main. The encoder now takes renderer.Size directly and derives
  grid and pixel dimensions from one source of truth. termio.Message now
  aliases terminal.size_report.Style, and Termio writes reports via the
  shared encoder.
  ```
- [`7bf8974`](https://github.com/ghostty-org/ghostty/commit/7bf89740dd86c28f40c2d5ab9cd001cbf41b864a) vt: expose size_report encoding in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_size_report_encode() to libghostty-vt, following the
  same pattern as focus encoding: a single stateless function that
  writes a terminal size report escape sequence into a caller-provided
  buffer.
  
  The size_report.zig Style enum and Size struct now use lib.Enum and
  lib.Struct so the types are automatically C-compatible when building
  with c_abi, eliminating the need for duplicate type definitions in
  the C wrapper. The C wrapper in c/size_report.zig re-exports these
  types directly and provides the callconv(.c) encode entry point.
  
  Supports mode 2048 in-band reports and XTWINOPS responses (CSI 14 t,
  CSI 16 t, CSI 18 t).
  ```
- [`d3bd224`](https://github.com/ghostty-org/ghostty/commit/d3bd224081d3c7c5ee54df6815e44f0b5d25357b) terminal/vt: extract size report encoding to its own file ([#11607](https://github.com/ghostty-org/ghostty/issues/11607)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Extract size report encoding into a reusable module and expose it
  through the libghostty-vt C API as `ghostty_size_report_encode()`.
  
  Size report escape sequences (mode 2048 in-band reports, XTWINOPS CSI
  14/16/18 t responses) were formatted inline in
  `Termio.sizeReportLocked`, and `termio.Message` carried its own
  duplicate enum for report styles. This made the encoding logic
  impossible to reuse from the C library and kept the style type
  unnecessarily scoped to termio.
  
  ## Example
  
  ```c
  GhosttySizeReportSize size = {
      .rows = 24, .columns = 80,
      .cell_width = 9, .cell_height = 18,
  };
  
  char buf[64];
  size_t written = 0;
  ghostty_size_report_encode(
      GHOSTTY_SIZE_REPORT_MODE_2048, size,
      buf, sizeof(buf), &written);
  // buf contains: "\x1b[48;24;80;432;720t"
  ```
  ````

## March 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23216414166), [2](https://github.com/ghostty-org/ghostty/actions/runs/23208321171), [3](https://github.com/ghostty-org/ghostty/actions/runs/23205740733), [4](https://github.com/ghostty-org/ghostty/actions/runs/23202794242), [5](https://github.com/ghostty-org/ghostty/actions/runs/23179110345), [6](https://github.com/ghostty-org/ghostty/actions/runs/23176582607), [7](https://github.com/ghostty-org/ghostty/actions/runs/23172468303)  
Summary: 7 runs • 13 commits • 7 authors

### Changes

- [`45ccc69`](https://github.com/ghostty-org/ghostty/commit/45ccc69a4984af7dcda08ec34920b6a78031fee1) Update VOUCHED list ([#11605](https://github.com/ghostty-org/ghostty/issues/11605)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11603#discussioncomment-16184007)
  from @jcollie.
  
  Vouch: @philocalyst
  ```
- [`978abde`](https://github.com/ghostty-org/ghostty/commit/978abdeebc4b346b8e9bc4395234b7bb046dc87f) Fix tmux control block terminator parsing ([@wyounas](https://github.com/wyounas))
- [`4a88f46`](https://github.com/ghostty-org/ghostty/commit/4a88f460c4e505deeca7e4fea4135e958be06c74) terminal/tmux: stylistic cleanups ([@mitchellh](https://github.com/mitchellh))
- [`d9070db`](https://github.com/ghostty-org/ghostty/commit/d9070dbee202bcf86411c8cbd2bd157609c9aee2) Fix tmux control parser premature %end/%error block termination ([#11597](https://github.com/ghostty-org/ghostty/issues/11597)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes [#11935.](https://github.com/ghostty-org/ghostty/issues/11395)
  
  I’m new to Zig, so I used AI assistance (Codex) while preparing this
  change. Before opening this PR, I manually reviewed every line of the
  final patch and stepped through the parser in LLDB to verify the
  behavior. Happy to make any changes.
  
  To better understand the parser, I also built a small model-checker
  model
  [here](https://gist.github.com/wyounas/284036272ba5893b6e413cafe2fe2a24).
  
  Separately from this fix, I think formal verification and modeling could
  be useful for parser work in Ghostty. The model is written in FizzBee,
  which uses a Python-like Starlark syntax and is fairly readable. If that
  seems useful, I’d be happy to open a separate discussion about whether
  something like that belongs in the repository as executable
  documentation or an additional safety net for future parser changes.
  ```
- [`b173b2d`](https://github.com/ghostty-org/ghostty/commit/b173b2dfb72e89075b4abc01587f059202692248) Update VOUCHED list ([#11599](https://github.com/ghostty-org/ghostty/issues/11599)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11594#discussioncomment-16180979)
  from @jcollie.
  
  Vouch: @heddxh
  ```
- [`3e0d434`](https://github.com/ghostty-org/ghostty/commit/3e0d434e8a52577a1296acd29495924253497894) zsh: use OSC 133;P;k=s for secondary prompts ([@jparise](https://github.com/jparise))
  ```text
  This is consistent with our bash prompt handling and also lets us
  simplify our multiline prompt logic (because it no longer needs to work
  around 133;A's fresh-line behavior).
  ```
- [`3a65bd5`](https://github.com/ghostty-org/ghostty/commit/3a65bd5c4f1c4a2773bf520fe79da78f7cd40187) zsh: use OSC 133;P;k=s for secondary prompts ([#11596](https://github.com/ghostty-org/ghostty/issues/11596)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is consistent with our bash prompt handling and also lets us
  simplify our multiline prompt logic (because it no longer needs to work
  around 133;A's fresh-line behavior).
  ```
- [`739da49`](https://github.com/ghostty-org/ghostty/commit/739da492b8f21e8b129434ae2b2f685510d19587) Update VOUCHED list ([#11598](https://github.com/ghostty-org/ghostty/issues/11598)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11537#issuecomment-4075954392)
  from @mitchellh.
  
  Unvouch: @cadebrown
  ```
- [`7916227`](https://github.com/ghostty-org/ghostty/commit/79162279d9d8a5fea5a26bbc2abda98e90ec5988) gtk: move audio playback into separate file, enabling reuse ([@jcollie](https://github.com/jcollie))
- [`71d6f08`](https://github.com/ghostty-org/ghostty/commit/71d6f08e9bf51965fb8b5ef6f0ea58633692c9a0) gtk: move audio playback into separate file, enabling reuse ([#11588](https://github.com/ghostty-org/ghostty/issues/11588)) ([@pluiedev](https://github.com/pluiedev))
- [`9f4e42a`](https://github.com/ghostty-org/ghostty/commit/9f4e42a52377a77c8e2f3ce5ce7ce26009947917) Update VOUCHED list ([#11587](https://github.com/ghostty-org/ghostty/issues/11587)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11585#discussioncomment-16170774)
  from @jcollie.
  
  Vouch: @heaths
  ```
- [`67dcac0`](https://github.com/ghostty-org/ghostty/commit/67dcac02f9b4c40745f374d7f77d71761d21616d) build(deps): bump softprops/action-gh-release from 2.6.0 to 2.6.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 2.6.0 to 2.6.1.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/26e8ad27a09a225049a7075d7ec1caa2df6ff332...153bb8e04406b158c6c84fc1615b65b24149a1fe)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 2.6.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`5e0db1b`](https://github.com/ghostty-org/ghostty/commit/5e0db1b60586d43ebaa2c7b9b7b9340183dcd305) build(deps): bump softprops/action-gh-release from 2.6.0 to 2.6.1 ([#11582](https://github.com/ghostty-org/ghostty/issues/11582)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 2.6.0 to 2.6.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v2.6.1</h2>
  <p><code>2.6.1</code> is a patch release focused on restoring linked
  discussion thread creation when
  <code>discussion_category_name</code> is set. It fixes
  <code>[#764](https://github.com/softprops/action-gh-release/issues/764)</code>,
  where the draft-first publish flow
  stopped carrying the discussion category through the final publish
  step.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: preserve discussion category on publish by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/765">softprops/action-gh-release#765</a></li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>2.6.1</h2>
  <p><code>2.6.1</code> is a patch release focused on restoring linked
  discussion thread creation when
  <code>discussion_category_name</code> is set. It fixes
  <code>[#764](https://github.com/softprops/action-gh-release/issues/764)</code>,
  where the draft-first publish flow
  stopped carrying the discussion category through the final publish
  step.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: preserve discussion category on publish by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/765">softprops/action-gh-release#765</a></li>
  </ul>
  <h2>2.6.0</h2>
  <p><code>2.6.0</code> is a minor release centered on
  <code>previous_tag</code> support for
  <code>generate_release_notes</code>,
  which lets workflows pin GitHub's comparison base explicitly instead of
  relying on the default range.
  It also includes the recent concurrent asset upload recovery fix, a
  <code>working_directory</code> docs sync,
  a checked-bundle freshness guard for maintainers, and clearer
  immutable-prerelease guidance where
  GitHub platform behavior imposes constraints on how prerelease asset
  uploads can be published.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: support previous_tag for generate_release_notes by <a
  href="https://github.com/pocesar"><code>@​pocesar</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/372">softprops/action-gh-release#372</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: recover concurrent asset metadata 404s by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/760">softprops/action-gh-release#760</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>docs: clarify reused draft release behavior by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/759">softprops/action-gh-release#759</a></li>
  <li>docs: clarify working_directory input by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/761">softprops/action-gh-release#761</a></li>
  <li>ci: verify dist bundle freshness by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/762">softprops/action-gh-release#762</a></li>
  <li>fix: clarify immutable prerelease uploads by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/763">softprops/action-gh-release#763</a></li>
  </ul>
  <h2>2.5.3</h2>
  <p><code>2.5.3</code> is a patch release focused on the remaining
  path-handling and release-selection bugs uncovered after
  <code>2.5.2</code>.
  It fixes
  <code>[#639](https://github.com/softprops/action-gh-release/issues/639)</code>,
  <code>[#571](https://github.com/softprops/action-gh-release/issues/571)</code>,
  <code>[#280](https://github.com/softprops/action-gh-release/issues/280)</code>,
  <code>[#614](https://github.com/softprops/action-gh-release/issues/614)</code>,
  <code>[#311](https://github.com/softprops/action-gh-release/issues/311)</code>,
  <code>[#403](https://github.com/softprops/action-gh-release/issues/403)</code>,
  and
  <code>[#368](https://github.com/softprops/action-gh-release/issues/368)</code>.
  It also adds documentation clarifications for
  <code>[#541](https://github.com/softprops/action-gh-release/issues/541)</code>,
  <code>[#645](https://github.com/softprops/action-gh-release/issues/645)</code>,
  <code>[#542](https://github.com/softprops/action-gh-release/issues/542)</code>,
  <code>[#393](https://github.com/softprops/action-gh-release/issues/393)</code>,
  and
  <code>[#411](https://github.com/softprops/action-gh-release/issues/411)</code>,
  where the current behavior is either usage-sensitive or constrained by
  GitHub platform limits rather than an action-side runtime bug.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/153bb8e04406b158c6c84fc1615b65b24149a1fe"><code>153bb8e</code></a>
  release 2.6.1</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/569deb874d08cd8cc0aa24af7c0b21160fe4b0e4"><code>569deb8</code></a>
  fix: preserve discussion category when publishing releases (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/765">#765</a>)</li>
  <li>See full diff in <a
  href="https://github.com/softprops/action-gh-release/compare/26e8ad27a09a225049a7075d7ec1caa2df6ff332...153bb8e04406b158c6c84fc1615b65b24149a1fe">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=2.6.0&new-version=2.6.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## March 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23171373890), [2](https://github.com/ghostty-org/ghostty/actions/runs/23171148499), [3](https://github.com/ghostty-org/ghostty/actions/runs/23169456226), [4](https://github.com/ghostty-org/ghostty/actions/runs/23168451781), [5](https://github.com/ghostty-org/ghostty/actions/runs/23159262528), [6](https://github.com/ghostty-org/ghostty/actions/runs/23156954925), [7](https://github.com/ghostty-org/ghostty/actions/runs/23156018197), [8](https://github.com/ghostty-org/ghostty/actions/runs/23155406087), [9](https://github.com/ghostty-org/ghostty/actions/runs/23143106693), [10](https://github.com/ghostty-org/ghostty/actions/runs/23138543301), [11](https://github.com/ghostty-org/ghostty/actions/runs/23131302018), [12](https://github.com/ghostty-org/ghostty/actions/runs/23129702400), [13](https://github.com/ghostty-org/ghostty/actions/runs/23126902982), [14](https://github.com/ghostty-org/ghostty/actions/runs/23123185713), [15](https://github.com/ghostty-org/ghostty/actions/runs/23122447798)  
Summary: 15 runs • 55 commits • 9 authors

### Changes

- [`8a40e37`](https://github.com/ghostty-org/ghostty/commit/8a40e37b863aa42ae4f4d6b7d25f242d050e3333) gtk: refactor application id and resource path ([@jcollie](https://github.com/jcollie))
- [`f6e92b6`](https://github.com/ghostty-org/ghostty/commit/f6e92b6895bd4429090a70da0a45765180bdb20c) gtk: refactor application id and resource path ([#11580](https://github.com/ghostty-org/ghostty/issues/11580)) ([@jcollie](https://github.com/jcollie))
- [`25679f3`](https://github.com/ghostty-org/ghostty/commit/25679f3ae736d94a93d4778fbe3aa095633cd5cb) vt: add C API header for terminal mode tags ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add modes.h with GhosttyModeTag, a uint16_t typedef matching the
  Zig ModeTag packed struct layout (bits 0-14 for the mode value,
  bit 15 for the ANSI flag). Three inline helper functions provide
  construction and inspection: ghostty_mode_tag_new,
  ghostty_mode_tag_value, and ghostty_mode_tag_ansi.
  ```
- [`1c03770`](https://github.com/ghostty-org/ghostty/commit/1c03770e2be4700ee60db01750a323005ef5dc8b) vt: expose terminal modes to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add modes.h with GhosttyModeTag (uint16_t) matching the Zig ModeTag
  packed struct layout, along with inline helpers for constructing and
  inspecting mode tags. Provide GHOSTTY_MODE_* macros for all 39
  built-in modes (4 ANSI, 35 DEC), parenthesized for safety.
  
  Add ghostty_terminal_mode_get and ghostty_terminal_mode_set to
  terminal.h, both returning GhosttyResult so that null terminals
  and unknown mode tags return GHOSTTY_INVALID_VALUE. The get function
  writes its result through a bool out-parameter.
  
  Add a note in the Zig mode entries reminding developers to update
  modes.h when adding new modes.
  ```
- [`a460743`](https://github.com/ghostty-org/ghostty/commit/a460743b2ac036577ac46ee9c34946b37b214e67) vt: add mode report encoding to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_mode_report_encode() which encodes a DECRPM response
  sequence into a caller-provided buffer. The function takes a mode
  tag, a report state integer, an output buffer, and writes the
  appropriate CSI sequence (with ? prefix for DEC private modes).
  
  The Zig-side ReportState is a non-exhaustive c_int enum that uses
  std.meta.intToEnum for safe conversion to the internal type,
  returning GHOSTTY_INVALID_VALUE on overflow. The C header exposes
  a GhosttyModeReportState enum with named constants for the five
  standard DECRPM state values.
  ```
- [`bfaab04`](https://github.com/ghostty-org/ghostty/commit/bfaab044684e0209c9996e5b7b6bc77a778b1b89) vt: rename mode tag to mode ([@mitchellh](https://github.com/mitchellh))
- [`b18705c`](https://github.com/ghostty-org/ghostty/commit/b18705c4697119fd86af690f0e85f644583a4d0a) libghostty: expose terminal modes and DECRPM report encoding through the C API. ([#11579](https://github.com/ghostty-org/ghostty/issues/11579)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Previously libghostty-vt had no way for C consumers to query, set, or
  report on terminal modes. Callers that needed to respond to DECRPM
  requests or inspect mode state had no public interface to do so.
  
  This adds three layers of mode support to the C API:
  
  - `GhosttyMode` — a 16-bit packed type with inline helpers to construct
  and inspect mode tags, plus `GHOSTTY_MODE_*` macros for all supported
  ANSI and DEC private modes.
  - `ghostty_terminal_mode_get` / `ghostty_terminal_mode_set` — query and
  set mode values on a terminal handle.
  - `ghostty_mode_report_encode` — encode a DECRPM response sequence (`CSI
  [?] Ps1 ; Ps2 $ y`) into a caller-provided buffer.
  
  ## Example
  
  ```c
  #include <stdio.h>
  #include <ghostty/vt.h>
  
  int main() {
      char buf[32];
      size_t written = 0;
  
      // Query a terminal's cursor visibility and encode a DECRPM report
      GhosttyMode mode = GHOSTTY_MODE_CURSOR_VISIBLE;
      bool value = false;
      ghostty_terminal_mode_get(terminal, mode, &value);
  
      GhosttyModeReportState state = value
          ? GHOSTTY_MODE_REPORT_SET
          : GHOSTTY_MODE_REPORT_RESET;
  
      if (ghostty_mode_report_encode(mode, state, buf, sizeof(buf), &written)
              == GHOSTTY_SUCCESS) {
          // writes ESC[?25;1$y or ESC[?25;2$y
          fwrite(buf, 1, written, stdout);
      }
  }
  ```
  ````
- [`6abed20`](https://github.com/ghostty-org/ghostty/commit/6abed20fc89607134063f38107b210ed1ab31d25) Update VOUCHED list ([#11581](https://github.com/ghostty-org/ghostty/issues/11581)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11557#issuecomment-4071331120)
  from @mitchellh.
  
  Unvouch: @mvanhorn
  ```
- [`d6b37ba`](https://github.com/ghostty-org/ghostty/commit/d6b37ba38f9b238b5bf30aebbeae261dd45290cd) terminal: extract DECRPM mode report encoding to terminal package ([@mitchellh](https://github.com/mitchellh))
  ```text
  This extracts our mode reporting from being hardcoded in termio
  to being reusable in the existing `terminal.modes` namespace. The goal
  is to expose this via the Zig API libghostty (done) and C API (to do
  later).
  ```
- [`21eb30d`](https://github.com/ghostty-org/ghostty/commit/21eb30d9bcc94e3b1e39ba1294c7b390211ea7c1) terminal: extract DECRPM mode report encoding to terminal package ([#11578](https://github.com/ghostty-org/ghostty/issues/11578)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This extracts our mode reporting from being hardcoded in termio to being
  reusable in the existing `terminal.modes` namespace. The goal is to
  expose this via the Zig API libghostty (done) and C API (to do later).
  ```
- [`bed9d92`](https://github.com/ghostty-org/ghostty/commit/bed9d92f048835cfcae372361d3c741db8a3ed78) vt: expose focus encoding in C and Zig APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add focus event encoding (CSI I / CSI O) to the libghostty-vt public
  API, following the same patterns as key and mouse encoding.
  
  The focus Event enum uses lib.Enum for C ABI compatibility. The C API
  provides ghostty_focus_encode() which writes into a caller-provided
  buffer and returns GHOSTTY_OUT_OF_SPACE with the required size when
  the buffer is too small.
  
  Also update key and mouse encoders to return GHOSTTY_OUT_OF_SPACE
  instead of GHOSTTY_OUT_OF_MEMORY for buffer-too-small errors,
  reserving OUT_OF_MEMORY for actual allocation failures. Update all
  corresponding header documentation.
  ```
- [`e90dbc9`](https://github.com/ghostty-org/ghostty/commit/e90dbc9da697816ef661156cb50cc320cada730c) vt: expose focus encoding in C and Zig APIs ([#11577](https://github.com/ghostty-org/ghostty/issues/11577)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add focus event encoding (CSI I / CSI O) to the libghostty-vt public
  API, following the same patterns as key and mouse encoding.
  
  The focus Event enum uses lib.Enum for C ABI compatibility. The C API
  provides ghostty_focus_encode() which writes into a caller-provided
  buffer and returns GHOSTTY_OUT_OF_SPACE with the required size when the
  buffer is too small.
  
  Also update key and mouse encoders to return GHOSTTY_OUT_OF_SPACE
  instead of GHOSTTY_OUT_OF_MEMORY for buffer-too-small errors, reserving
  OUT_OF_MEMORY for actual allocation failures. Update all corresponding
  header documentation.
  ```
- [`8966d37`](https://github.com/ghostty-org/ghostty/commit/8966d37985a22af8529f407686afdfd51c52cdce) gtk/wayland: refactor global handling ([@pluiedev](https://github.com/pluiedev))
  ```text
  The way we originally handled globals gradually escalated into an unholy
  mess of ad-hoc helper functions and special-case handlers, which proved
  to be hard to scale. Using a type-erased EnumMap like this makes
  everything *far* easier to work and reason with, I think.
  
  Also nuked the `xdg_wm_dialog_v1` hack that was necessary to prevent
  old versions of gtk4-layer-shell crashing. If by the time of 1.4's
  release people are still using those versions, it's on them.
  ```
- [`2318e18`](https://github.com/ghostty-org/ghostty/commit/2318e18df3577151f8c1fd130bd6b698e8ffde21) gtk/wayland: refactor global handling ([#11559](https://github.com/ghostty-org/ghostty/issues/11559)) ([@pluiedev](https://github.com/pluiedev))
- [`c1326c5`](https://github.com/ghostty-org/ghostty/commit/c1326c57f92758065bfc18ffc610be03909d7c5c) Update VOUCHED list ([#11572](https://github.com/ghostty-org/ghostty/issues/11572)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10478#discussioncomment-16163586)
  from @mitchellh.
  
  Denounce: @highimpact-dev
  ```
- [`6fabf77`](https://github.com/ghostty-org/ghostty/commit/6fabf775bba63ae41396057fe0ee9458082e0723) Lots of duplicate word typos + typo. ([@00-kat](https://github.com/00-kat))
- [`cef1f19`](https://github.com/ghostty-org/ghostty/commit/cef1f19d24d6aff9839dc67ae125c2a358b093de) cli: add +explain-config ([@jparise](https://github.com/jparise))
  ```text
  This is a new CLI action that prints an option or keybind's help
  documentation to stdout.
  
      ghostty +explain-config font-size
      ghostty +explain-config copy_to_clipboard
      ghostty +explain-config --option=font-size
      ghostty +explain-config --keybind=copy_to_clipboard
  
  The --option and --keybind flags perform a specific lookup. A string
  passed as a positional argument attempts to look up the name first as an
  option and then as a keybind.
  
  Our vim plugin uses this with &keywordprg, which allows you to look up
  the documentation for the config option or keybind under the cursor (K).
  ```
- [`9783f6c`](https://github.com/ghostty-org/ghostty/commit/9783f6c79c7934efd590c7c13db6e5720848e028) cli: tests for +explain-config explain functions ([@jparise](https://github.com/jparise))
- [`cce205d`](https://github.com/ghostty-org/ghostty/commit/cce205d01b122c7490183ca394ddee1d81a9408a) cli: add +explain-config ([#11546](https://github.com/ghostty-org/ghostty/issues/11546)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a new CLI action that prints an option or keybind's help
  documentation to stdout.
  
      ghostty +explain-config font-size
      ghostty +explain-config copy_to_clipboard
      ghostty +explain-config --option=font-size
      ghostty +explain-config --keybind=copy_to_clipboard
  
  The --option and --keybind flags perform a specific lookup. A string
  passed as a positional argument attempts to look up the name first as an
  option and then as a keybind.
  
  Our vim plugin uses this with &keywordprg, which allows you to look up
  the documentation for the config option or keybind under the cursor (K).
  ```
- [`a811b60`](https://github.com/ghostty-org/ghostty/commit/a811b6074b6ec285471246525ef36cd10db8c447) Lots of duplicate word typos + typo ([#11539](https://github.com/ghostty-org/ghostty/issues/11539)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  TL;DR: this description is (intentionally) nonsense but I ran
  `\b(\w+)\s\1\b` over `src` and stole a singular typo fix from #11528.
  
  Replacement of #11528 with 100% less slop and 99% less AI; I didn't feel
  like saying no to free(ish) typo checking. Note that many of the fixes
  there were outright incorrect (and clearly had no review from sentient
  lifeforms, contrary to its—sorry, it's—description). A lot of extra
  double words were caught with a handy `rg --pcre2 '\b(\w+)\s+\1\b' src`;
  you could say this PR was “ripgrep-assisted” the way that one was
  “AI-assisted”. Rather ironic since that PR also claims to have used grep
  via Claude Code, but missed a lot of them.
  
  The its → it's changes from that PR were elided; I decided to run a `rg
  "\bit'?s\b" src`, but someone REALLY likes their its, so I reverted my
  changes as there were an extremely large number of changes (probably a
  hundred files with multiple hundred cases). The only other change was
  “baout” → “about”.
  
  # AI Usage
  
  Claude Code was used by proxy for finding baout. Claude Code was used by
  proxy for realizing that the correct spelling is about. Claude Code was
  not used for fixing it. Oh my god it was so difficult to fix, the
  original PR had it so easy. I had to type out the file name (fish's AI
  sorry I mean autocomplete helped though) and like, type /baout, press R,
  press ab, then save and exit. This is so difficult you know we should
  use an AI for this, like this is so hard I don't know how people manage.
  
  All changes were verified by me: I consulted the dictionary to delve
  into double-checkment of “in existence; being in evidence; apparent.”
  Uhhh insert assorted other AI impersonation here maybe? THE LLM IN ME
  WANTS TO ESCAPE PLEASE HELP
  ```
- [`2d2d913`](https://github.com/ghostty-org/ghostty/commit/2d2d913f808934bcd0298c5cf7d0b3ce1390d8ff) ci: skip milestone workflow for bot-authored PRs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The milestone action currently runs for all merged pull_request_target
  close events, including PRs opened by bots such as dependabot and
  ghostty-vouch. That causes milestone binding to run on automated PRs
  that should be ignored.
  
  Gate the update-milestone job so pull request events only run when the
  author is not a bot, while still allowing closed-issue events to run.
  This preserves existing issue milestone behavior and prevents bot PRs
  from triggering the workflow.
  ```
- [`03806da`](https://github.com/ghostty-org/ghostty/commit/03806dad3aa0bb55d1f3b057a05748072ed2c103) ci: skip milestone workflow for bot-authored PRs ([#11570](https://github.com/ghostty-org/ghostty/issues/11570)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The milestone action currently runs for all merged pull_request_target
  close events, including PRs opened by bots such as dependabot and
  ghostty-vouch. That causes milestone binding to run on automated PRs
  that should be ignored.
  
  Gate the update-milestone job so pull request events only run when the
  author is not a bot, while still allowing closed-issue events to run.
  This preserves existing issue milestone behavior and prevents bot PRs
  from triggering the workflow.
  ```
- [`69554f4`](https://github.com/ghostty-org/ghostty/commit/69554f414c1402a69d4648952aa13ad5bf43b673) shell-integration: fix ssh-env SetEnv clobbering user SSH config ([@j0hnm4r5](https://github.com/j0hnm4r5))
- [`925992a`](https://github.com/ghostty-org/ghostty/commit/925992abd98d83f08dc367f6b6c6265ee0510e60) shell-integration: fix ssh-env SetEnv clobbering user SSH config ([#11518](https://github.com/ghostty-org/ghostty/issues/11518)) ([@jparise](https://github.com/jparise))
  ````text
  ## Problem
  
  Ghostty's `ssh-env` shell integration uses `-o "SetEnv
  COLORTERM=truecolor"` when wrapping SSH commands. OpenSSH treats
  command-line `-o SetEnv` options as **replacements** for all `SetEnv`
  entries in `~/.ssh/config`, not additions. This silently drops any
  user-configured `SetEnv` variables.
  
  For example, a user with this in their SSH config:
  ```
  Host myserver
    SetEnv MY_VAR=hello
  ```
  ...would find `MY_VAR` empty after SSHing through Ghostty with `ssh-env`
  enabled.
  
  Reference: https://github.com/ghostty-org/ghostty/discussions/10871
  
  ## Fix
  
  Replace `-o "SetEnv COLORTERM=truecolor"` with the additive pattern: set
  `COLORTERM=truecolor` locally before the SSH call and forward it via
  `SendEnv`.
  
  `SendEnv` is additive — it does not clobber `SetEnv` entries in
  `~/.ssh/config`.
  
  **Trade-off:** `SendEnv` requires `AcceptEnv COLORTERM` on the remote
  server (unlike `SetEnv`). But this was already the case for
  `TERM_PROGRAM`/`TERM_PROGRAM_VERSION`, so it's a consistent and
  acceptable approach.
  
  ## Changes
  
  All 5 shell integration files updated with the same pattern:
  
  - `SetEnv COLORTERM=truecolor` option removed
  - `COLORTERM` added to the existing `SendEnv` option
  - `COLORTERM=truecolor` set as a local env var on the execute line (so
  `SendEnv` has something to forward)
  
  ## Test plan
  
  - [ ] Enable `ssh-env` in Ghostty config: `shell-integration-features =
  ssh-env`
  - [ ] Add `SetEnv MY_VAR=hello` under a host in `~/.ssh/config` and
  `AcceptEnv MY_VAR` in `/etc/ssh/sshd_config` on the remote
  - [ ] SSH to that host — `echo $MY_VAR` should return `hello` (was empty
  before this fix)
  - [ ] `echo $COLORTERM` returns `truecolor` (requires `AcceptEnv
  COLORTERM`)
  - [ ] `echo $TERM_PROGRAM` still propagates (same `AcceptEnv`
  requirement as before)
  ````
- [`3b60ef3`](https://github.com/ghostty-org/ghostty/commit/3b60ef3b34006fbf20030e17ad268cf3952d4228) Add missing plural forms (or, the lack thereof) for Chinese. ([@00-kat](https://github.com/00-kat))
- [`a3fe597`](https://github.com/ghostty-org/ghostty/commit/a3fe5974e8b476fcba7db07b576ce95fe170ca73) Add missing plural forms for Chinese ([#11562](https://github.com/ghostty-org/ghostty/issues/11562)) ([@pluiedev](https://github.com/pluiedev))
- [`96f8f0d`](https://github.com/ghostty-org/ghostty/commit/96f8f0d93c19efec5cc349f71965a405f5c9c2a3) gtk: add setMonitor binding and kde-output-order-v1 protocol ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Add the missing setMonitor() function to the gtk4-layer-shell Zig
  bindings and provide the gdk module so it can reference gdk.Monitor.
  
  Register the kde-output-order-v1 Wayland protocol from
  plasma-wayland-protocols and generate its scanner binding. This
  protocol reports the compositor's monitor priority ordering and is
  needed to correctly identify the primary monitor for
  quick-terminal-screen support on Linux.
  ```
- [`6da660a`](https://github.com/ghostty-org/ghostty/commit/6da660a9a5eb9e57175035d23434b4c44b1b4151) gtk: implement quick-terminal-screen for Wayland ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Implement the quick-terminal-screen config option on Linux/Wayland so
  users can pin the quick terminal to a specific monitor instead of
  always following the mouse cursor.
  
  Use the kde_output_order_v1 protocol to identify the compositor's
  primary monitor by connector name (e.g. "DP-1"). When the protocol is
  unavailable, fall back to the first monitor in the GDK list.
  
  - Add resolveQuickTerminalMonitor() to map config values to a
    gdk.Monitor: .mouse returns null (compositor decides), .main and
    .macos-menu-bar match by connector name via the protocol
  - Call layer_shell.setMonitor() in both initQuickTerminal and
    syncQuickTerminal so config reloads take effect
  - Update enteredMonitor to size the window using the configured
    monitor rather than whichever monitor was entered
  - Update config documentation to reflect Linux support
  ```
- [`630c2df`](https://github.com/ghostty-org/ghostty/commit/630c2dff190af14b7915f3e0d4df639e95c4f21b) gtk: fix monitor ref ownership in Wayland quick terminal ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Handle g_list_model_get_object transfer-full semantics in resolveQuickTerminalMonitor by retaining exactly one monitor reference to return and unreffing the rest.
  
  Update init/sync/sizing call sites to unref the resolved monitor after setMonitor/getGeometry so monitor lifetimes are explicit and consistent.
  ```
- [`e25d8a6`](https://github.com/ghostty-org/ghostty/commit/e25d8a6f2f4a1d384866ab222f920f351b8905da) gtk: harden quick-terminal output-order state handling ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Install Wayland protocol listeners at bind time so late-added globals
  still receive events and listener setup stays tied to object lifetime.
  
  Track whether kde_output_order_v1 emitted any outputs in a cycle and
  clear cached primary-output state on empty or invalid updates. Also
  reset this cycle tracking when the protocol global is removed to avoid
  stale monitor selection.
  ```
- [`34473b0`](https://github.com/ghostty-org/ghostty/commit/34473b069bd74a729d001e3f71df3b03e890a739) gtk: simplify quick-terminal monitor resolution and state management ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Restructure resolveQuickTerminalMonitor into a two-phase approach
  (match by name, then fall back to first monitor) to eliminate the
  interleaved fallback/match ref tracking. Remove redundant switch in
  enteredMonitor that duplicated the .mouse handling already in
  resolveQuickTerminalMonitor. Hoist the primary_output_match_failed_logged
  reset above the name-length branches in outputOrderListener.
  ```
- [`19feaa0`](https://github.com/ghostty-org/ghostty/commit/19feaa058b333a559697fa21f7d600db0f2386fc) gtk: improve readability of Wayland quick-terminal monitor code ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Flatten resolveQuickTerminalMonitor by replacing the labeled-block
  switch with early returns, extract max_output_name_len constant, and
  reduce nesting in the output-order event handler.
  ```
- [`c982253`](https://github.com/ghostty-org/ghostty/commit/c9822535436c60587d136129a7c5beb44829d81b) gtk: handle replacement Wayland globals before remove ([@jguthmiller](https://github.com/jguthmiller))
  ```text
  Track registry global names for kde decoration manager and kde_output_order bindings so we can distinguish same-global duplicates from valid replacements announced before global_remove.
  
  On global_remove, match and clear these bindings by registry global name to avoid dropping a replacement when the old global is removed.
  ```
- [`18fa161`](https://github.com/ghostty-org/ghostty/commit/18fa161222916c537fb5e71e6d7bbe2479805fb1) gtk: simplify Wayland output-order state handling ([@jguthmiller](https://github.com/jguthmiller))
- [`beeb810`](https://github.com/ghostty-org/ghostty/commit/beeb810c04d0b7c93cd74d215dd194eb03759cdb) gtk: address PR review feedback for quick-terminal-screen ([@jguthmiller](https://github.com/jguthmiller))
- [`b823c07`](https://github.com/ghostty-org/ghostty/commit/b823c07ae30635b4641d45db0f06f6f416756b94) PR feedback - simplify ([@jguthmiller](https://github.com/jguthmiller))
- [`bec4c61`](https://github.com/ghostty-org/ghostty/commit/bec4c61d4dbbd1ad667e7cdcafaf15d0836c3143) PR feedback: heap-allocate primary_output_name ([@jguthmiller](https://github.com/jguthmiller))
- [`600f59a`](https://github.com/ghostty-org/ghostty/commit/600f59ae313adf377c0bf0d754fa258257f5f65f) gtk: implement quick-terminal-screen for Linux/Wayland ([#11117](https://github.com/ghostty-org/ghostty/issues/11117)) ([@pluiedev](https://github.com/pluiedev))
- [`44f403b`](https://github.com/ghostty-org/ghostty/commit/44f403bfe1b45fdd1b8be2ea5b3eb6bc4b593aa3) Update VOUCHED list ([#11556](https://github.com/ghostty-org/ghostty/issues/11556)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11536#discussioncomment-16152546)
  from @pluiedev.
  
  Vouch: @mvanhorn
  ```
- [`f9f92f2`](https://github.com/ghostty-org/ghostty/commit/f9f92f2e0f590ece488e06718ccbbeb4bd6fc601) terminal: consolidate mouse types into mouse.zig ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move MouseEvent and MouseFormat out of Terminal.zig and MouseShape out
  of mouse_shape.zig into a new mouse.zig file. The types are named
  without the Mouse prefix inside the module (Event, Format, Shape) and
  re-exported with the prefix from terminal/main.zig for external use.
  
  Update all call sites (mouse_encode.zig, surface_mouse.zig, stream.zig)
  to import through terminal/main.zig or directly from mouse.zig. Remove
  the now-unused mouse_shape.zig.
  ```
- [`37efac9`](https://github.com/ghostty-org/ghostty/commit/37efac99b0c777a89d28503e7cace78cb394b4d2) terminal/mouse: convert Event and Format to lib.Enum ([@mitchellh](https://github.com/mitchellh))
  ```text
  Convert the Event and Format enums from fixed-size Zig enums to
  lib.Enum so they are C ABI compatible when targeting C. The motion
  method on Event becomes a free function eventIsMotion since lib.Enum
  types cannot have declarations.
  ```
- [`79e023b`](https://github.com/ghostty-org/ghostty/commit/79e023b65eebcf56ee0a17ff3fca2609463b1bc3) terminal,renderer: convert structs to extern ([@mitchellh](https://github.com/mitchellh))
  ```text
  Convert Coordinate in terminal/point.zig and CellSize, ScreenSize,
  GridSize, and Padding in renderer/size.zig to extern structs. All
  fields are already extern-compatible types, so this gives them a
  guaranteed C ABI layout with no functional change.
  ```
- [`9b35c2b`](https://github.com/ghostty-org/ghostty/commit/9b35c2bb65ef900c9eab5ab6920d582cb5333035) vt: add mouse encoding C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose the internal mouse encoding functionality through the C API,
  following the same pattern as the existing key encoding API. This
  allows external consumers of libvt to encode mouse events into
  terminal escape sequences (X10, UTF-8, SGR, URxvt, SGR-Pixels).
  
  The API is split into two opaque handle types: GhosttyMouseEvent
  for building normalized mouse events (action, button, modifiers,
  position) and GhosttyMouseEncoder for converting those events into
  escape sequences. The encoder is configured via a setopt interface
  supporting tracking mode, output format, renderer geometry, button
  state, and optional motion deduplication by last cell.
  
  Encoder state can also be bulk-configured from a terminal handle
  via ghostty_mouse_encoder_setopt_from_terminal. Failed encodes due
  to insufficient buffer space report the required size without
  mutating deduplication state.
  ```
- [`33b05b9`](https://github.com/ghostty-org/ghostty/commit/33b05b9876ab8940e7ad2f98d3cf5ede277cf4d9) example: add C mouse encoding example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new c-vt-mouse-encode example that demonstrates how to use the
  mouse encoder C API. The example creates a mouse encoder configured
  with SGR format and normal tracking mode, sets up terminal geometry
  for pixel-to-cell coordinate mapping, and encodes a left button press
  event into a terminal escape sequence.
  
  Mirrors the structure of the existing c-vt-key-encode example. Also
  adds the corresponding @example doxygen reference in vt.h.
  ```
- [`de87456`](https://github.com/ghostty-org/ghostty/commit/de87456a9b662065e7dbdc6433d1ff283bbf13af) lib/vt: export mouse encoding API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Export mouse_encode types and functions through the lib_vt public
  input API, mirroring the existing key encoding exports. This adds
  MouseAction, MouseButton, MouseEncodeOptions, MouseEncodeEvent,
  and encodeMouse so that consumers of the Zig module can encode
  mouse events without reaching into internal packages.
  ```
- [`0f2eaed`](https://github.com/ghostty-org/ghostty/commit/0f2eaed68cd2feb5a48e733fe7b39a73d341e5f2) libghostty: add mouse encoding Zig + C API ([#11553](https://github.com/ghostty-org/ghostty/issues/11553)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds a Zig and C API for mouse event encoding.
  
  With these APIs in place, users can now create mouse events, configure a
  mouse encoder with tracking mode, output format, and terminal size, and
  encode those events into terminal escape sequences. All standard mouse
  protocols are supported: X10, UTF-8, SGR, URxvt, and SGR-Pixels.
  
  ## Example
  
  ```c
  #include <assert.h>
  #include <stddef.h>
  #include <stdio.h>
  #include <ghostty/vt.h>
  
  int main() {
    GhosttyMouseEncoder encoder;
    GhosttyResult result = ghostty_mouse_encoder_new(NULL, &encoder);
    assert(result == GHOSTTY_SUCCESS);
  
    // Set tracking mode to normal (button press/release)
    ghostty_mouse_encoder_setopt(encoder, GHOSTTY_MOUSE_ENCODER_OPT_EVENT,
                                 &(GhosttyMouseTrackingMode){GHOSTTY_MOUSE_TRACKING_NORMAL});
  
    // Set output format to SGR
    ghostty_mouse_encoder_setopt(encoder, GHOSTTY_MOUSE_ENCODER_OPT_FORMAT,
                                 &(GhosttyMouseFormat){GHOSTTY_MOUSE_FORMAT_SGR});
  
    // Set terminal geometry so the encoder can map pixel positions to cells
    ghostty_mouse_encoder_setopt(encoder, GHOSTTY_MOUSE_ENCODER_OPT_SIZE,
                                 &(GhosttyMouseEncoderSize){
                                     .size = sizeof(GhosttyMouseEncoderSize),
                                     .screen_width = 800, .screen_height = 600,
                                     .cell_width = 10, .cell_height = 20,
                                 });
  
    // Create mouse event: left button press at pixel position (50, 40)
    GhosttyMouseEvent event;
    result = ghostty_mouse_event_new(NULL, &event);
    assert(result == GHOSTTY_SUCCESS);
    ghostty_mouse_event_set_action(event, GHOSTTY_MOUSE_ACTION_PRESS);
    ghostty_mouse_event_set_button(event, GHOSTTY_MOUSE_BUTTON_LEFT);
    ghostty_mouse_event_set_position(event, (GhosttyMousePosition){.x = 50.0f, .y = 40.0f});
  
    // Encode the mouse event
    char buf[128];
    size_t written = 0;
    result = ghostty_mouse_encoder_encode(encoder, event, buf, sizeof(buf), &written);
    assert(result == GHOSTTY_SUCCESS);
  
    fwrite(buf, 1, written, stdout);
  
    ghostty_mouse_event_free(event);
    ghostty_mouse_encoder_free(encoder);
    return 0;
  }
  ```
  
  ## New APIs
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_mouse_event_new` | Create a new mouse event instance |
  | `ghostty_mouse_event_free` | Free a mouse event instance |
  | `ghostty_mouse_event_set_action` | Set the event action (press,
  release, motion) |
  | `ghostty_mouse_event_get_action` | Get the event action |
  | `ghostty_mouse_event_set_button` | Set the event button |
  | `ghostty_mouse_event_clear_button` | Clear the event button (for
  motion events) |
  | `ghostty_mouse_event_get_button` | Get the event button (returns
  whether one is set) |
  | `ghostty_mouse_event_set_mods` | Set keyboard modifiers held during
  the event |
  | `ghostty_mouse_event_get_mods` | Get keyboard modifiers held during
  the event |
  | `ghostty_mouse_event_set_position` | Set position in surface-space
  pixels |
  | `ghostty_mouse_event_get_position` | Get position in surface-space
  pixels |
  | `ghostty_mouse_encoder_new` | Create a new mouse encoder instance |
  | `ghostty_mouse_encoder_free` | Free a mouse encoder instance |
  | `ghostty_mouse_encoder_setopt` | Set an encoder option (tracking mode,
  format, size, etc.) |
  | `ghostty_mouse_encoder_setopt_from_terminal` | Sync encoder options
  from a terminal's current state |
  | `ghostty_mouse_encoder_reset` | Reset internal encoder state (motion
  deduplication) |
  | `ghostty_mouse_encoder_encode` | Encode a mouse event into a terminal
  escape sequence |
  ````
- [`ef1560c`](https://github.com/ghostty-org/ghostty/commit/ef1560ce50d73632d55d879ce72a9aab006280fa) Add missing plural forms. ([@00-kat](https://github.com/00-kat))
  ```text
  mk and zh_* are still missing theirs, but neither gettext's table [1]
  nor the documentation it copied from [2] list them.
  
  [1]: https://cgit.git.savannah.gnu.org/cgit/gettext.git/tree/gettext-tools/src/plural-table.c?id=dbf9d71e0c4707ca1b14359256b3dcccecb8e837
  [2]: https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html
  ```
- [`0fb1519`](https://github.com/ghostty-org/ghostty/commit/0fb1519cf2ca8a8e39a29e5a389c1272625a954b) build(deps): bump actions/create-github-app-token from 2.2.1 to 3.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 2.2.1 to 3.0.0.
  - [Release notes](https://github.com/actions/create-github-app-token/releases)
  - [Commits](https://github.com/actions/create-github-app-token/compare/29824e69f54612133e76f7eaac726eef6c875baf...f8d387b68d61c58ab83c6c016672934102569859)
  
  ---
  updated-dependencies:
  - dependency-name: actions/create-github-app-token
    dependency-version: 3.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`d08c8e0`](https://github.com/ghostty-org/ghostty/commit/d08c8e0dbca944e40cc20f07e84a51d518116356) build(deps): bump softprops/action-gh-release from 2.5.0 to 2.6.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 2.5.0 to 2.6.0.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/a06a81a03ee405af7f2048a818ed3f03bbf83c7b...26e8ad27a09a225049a7075d7ec1caa2df6ff332)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 2.6.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7f81e12`](https://github.com/ghostty-org/ghostty/commit/7f81e12dc0197e8d055f1d722f2df4ae61c57081) build(deps): bump dorny/paths-filter from 4.0.0 to 4.0.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 4.0.0 to 4.0.1.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/9d7afb8d214ad99e78fbd4247752c4caed2b6e4c...fbd0ab8f3e69293af611ebaee6363fc25e6d187d)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`f8e8a3f`](https://github.com/ghostty-org/ghostty/commit/f8e8a3fd71d37df193583a7ac194ab95f84fc8b6) build(deps): bump actions/create-github-app-token from 2.2.1 to 3.0.0 ([#11543](https://github.com/ghostty-org/ghostty/issues/11543)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
  from 2.2.1 to 3.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.0</h2>
  <h1><a
  href="https://github.com/actions/create-github-app-token/compare/v2.2.2...v3.0.0">3.0.0</a>
  (2026-03-14)</h1>
  <ul>
  <li>feat!: node 24 support (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/275">#275</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/2e564a0bb8e7cc2b907b2401a2afe177882d4325">2e564a0</a>)</li>
  <li>fix!: require <code>NODE_USE_ENV_PROXY</code> for proxy support (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/342">#342</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/4451bcbc139f8124b0bf04f968ea2586b17df458">4451bcb</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li>remove custom proxy handling (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/143">#143</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/dce0ab05f36f30b22fd14289fd36655c618e4e8e">dce0ab0</a>)</li>
  </ul>
  <h3>BREAKING CHANGES</h3>
  <ul>
  <li>Custom proxy handling has been removed. If you use HTTP_PROXY or
  HTTPS_PROXY, you must now also set NODE_USE_ENV_PROXY=1 on the action
  step.</li>
  <li>Requires <a
  href="https://github.com/actions/runner/releases/tag/v2.327.1">Actions
  Runner v2.327.1</a> or later if you are using a self-hosted runner.</li>
  </ul>
  <h2>v3.0.0-beta.6</h2>
  <h1><a
  href="https://github.com/actions/create-github-app-token/compare/v3.0.0-beta.5...v3.0.0-beta.6">3.0.0-beta.6</a>
  (2026-03-13)</h1>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump <code>@​actions/core</code> from 1.11.1
  to 3.0.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/337">#337</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/b04413352d4644ac2131b9a90c074f5e93ca18a1">b044133</a>)</li>
  <li><strong>deps:</strong> bump minimatch from 9.0.5 to 9.0.9 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/335">#335</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/5cbc65624c9ddc4589492bda7c8b146223e8c3e4">5cbc656</a>)</li>
  <li><strong>deps:</strong> bump the production-dependencies group with 4
  updates (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/336">#336</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/6bda5bc1410576b9a0879ce6076d53345485bba9">6bda5bc</a>)</li>
  <li><strong>deps:</strong> bump undici from 7.16.0 to 7.18.2 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/323">#323</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/b4f638f48ee0dcdbb0bc646c48e4cb2a2de847fe">b4f638f</a>)</li>
  </ul>
  <h2>v3.0.0-beta.5</h2>
  <h1><a
  href="https://github.com/actions/create-github-app-token/compare/v3.0.0-beta.4...v3.0.0-beta.5">3.0.0-beta.5</a>
  (2026-03-13)</h1>
  <ul>
  <li>fix!: require <code>NODE_USE_ENV_PROXY</code> for proxy support (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/342">#342</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/d53a1cdfde844c958786293adcaf739ecb8b5eb9">d53a1cd</a>)</li>
  </ul>
  <h3>BREAKING CHANGES</h3>
  <ul>
  <li>Custom proxy handling has been removed. If you use HTTP_PROXY or
  HTTPS_PROXY, you must now also set NODE_USE_ENV_PROXY=1 on the action
  step.</li>
  </ul>
  <h2>v3.0.0-beta.4</h2>
  <h1><a
  href="https://github.com/actions/create-github-app-token/compare/v3.0.0-beta.3...v3.0.0-beta.4">3.0.0-beta.4</a>
  (2026-03-13)</h1>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump <code>@​octokit/auth-app</code> from
  7.2.1 to 8.0.1 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/257">#257</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/bef1eaf1c0ac2b148ee2a0a74c65fbe6db0631f1">bef1eaf</a>)</li>
  <li><strong>deps:</strong> bump <code>@​octokit/request</code> from
  9.2.3 to 10.0.2 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/256">#256</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/5d7307be63501c0070c634b0ae8fec74e8208130">5d7307b</a>)</li>
  <li><strong>deps:</strong> bump glob from 10.4.5 to 10.5.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/305">#305</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/5480f4325a18c025ee16d7e081413854624e9edc">5480f43</a>)</li>
  <li><strong>deps:</strong> bump p-retry from 6.2.1 to 7.1.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/294">#294</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/dce3be8b284f45e65caed11a610e2bef738d15b4">dce3be8</a>)</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/f8d387b68d61c58ab83c6c016672934102569859"><code>f8d387b</code></a>
  build(release): 3.0.0 [skip ci]</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/d2129bd463d4feb8723edeea9437baa7db58e41e"><code>d2129bd</code></a>
  style: remove extra blank line in release workflow</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/77b94efc3e5f99a45abdd163fe04a4ebb95e98d6"><code>77b94ef</code></a>
  build: refresh generated artifacts</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/3ab4c6689898955f913a485593b36b197c6dbbdc"><code>3ab4c66</code></a>
  chore: move undici to devDependencies</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/739cf66feb937a443e4b6b7626bedd98f9fef6df"><code>739cf66</code></a>
  docs: update README action versions</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/db40289976a36527816d4f6f45765fdee71f134b"><code>db40289</code></a>
  build(deps): bump actions versions in test.yml</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/496a7ac4eb472eeac44d67818d1ce7f5e9e5fc97"><code>496a7ac</code></a>
  test: migrate from AVA to Node.js native test runner (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/346">#346</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/3870dc3051e3f1fc3a2faa17bcbb00f31fe1dd6c"><code>3870dc3</code></a>
  Rename end-to-end proxy job in test workflow</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/4451bcbc139f8124b0bf04f968ea2586b17df458"><code>4451bcb</code></a>
  fix!: require <code>NODE_USE_ENV_PROXY</code> for proxy support (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/342">#342</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/dce0ab05f36f30b22fd14289fd36655c618e4e8e"><code>dce0ab0</code></a>
  fix: remove custom proxy handling (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/143">#143</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/create-github-app-token/compare/29824e69f54612133e76f7eaac726eef6c875baf...f8d387b68d61c58ab83c6c016672934102569859">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=2.2.1&new-version=3.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`671301c`](https://github.com/ghostty-org/ghostty/commit/671301c8075e01c4bcc47077697cbc36765b76ba) build(deps): bump softprops/action-gh-release from 2.5.0 to 2.6.0 ([#11544](https://github.com/ghostty-org/ghostty/issues/11544)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 2.5.0 to 2.6.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v2.6.0</h2>
  <p><code>2.6.0</code> is a minor release centered on
  <code>previous_tag</code> support for
  <code>generate_release_notes</code>,
  which lets workflows pin GitHub's comparison base explicitly instead of
  relying on the default range.
  It also includes the recent concurrent asset upload recovery fix, a
  <code>working_directory</code> docs sync,
  a checked-bundle freshness guard for maintainers, and clearer
  immutable-prerelease guidance where
  GitHub platform behavior imposes constraints on how prerelease asset
  uploads can be published.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: support previous_tag for generate_release_notes by <a
  href="https://github.com/pocesar"><code>@​pocesar</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/372">softprops/action-gh-release#372</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: recover concurrent asset metadata 404s by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/760">softprops/action-gh-release#760</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>docs: clarify reused draft release behavior by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/759">softprops/action-gh-release#759</a></li>
  <li>docs: clarify working_directory input by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/761">softprops/action-gh-release#761</a></li>
  <li>ci: verify dist bundle freshness by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/762">softprops/action-gh-release#762</a></li>
  <li>fix: clarify immutable prerelease uploads by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/763">softprops/action-gh-release#763</a></li>
  </ul>
  <h2>v2.5.3</h2>
  <!-- raw HTML omitted -->
  <p><code>2.5.3</code> is a patch release focused on the remaining
  path-handling and release-selection bugs uncovered after
  <code>2.5.2</code>.
  It fixes
  <code>[#639](https://github.com/softprops/action-gh-release/issues/639)</code>,
  <code>[#571](https://github.com/softprops/action-gh-release/issues/571)</code>,
  <code>[#280](https://github.com/softprops/action-gh-release/issues/280)</code>,
  <code>[#614](https://github.com/softprops/action-gh-release/issues/614)</code>,
  <code>[#311](https://github.com/softprops/action-gh-release/issues/311)</code>,
  <code>[#403](https://github.com/softprops/action-gh-release/issues/403)</code>,
  and
  <code>[#368](https://github.com/softprops/action-gh-release/issues/368)</code>.
  It also adds documentation clarifications for
  <code>[#541](https://github.com/softprops/action-gh-release/issues/541)</code>,
  <code>[#645](https://github.com/softprops/action-gh-release/issues/645)</code>,
  <code>[#542](https://github.com/softprops/action-gh-release/issues/542)</code>,
  <code>[#393](https://github.com/softprops/action-gh-release/issues/393)</code>,
  and
  <code>[#411](https://github.com/softprops/action-gh-release/issues/411)</code>,
  where the current behavior is either usage-sensitive or constrained by
  GitHub platform limits rather than an action-side runtime bug.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: prefer token input over GITHUB_TOKEN by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/751">softprops/action-gh-release#751</a></li>
  <li>fix: clean up duplicate drafts after canonicalization by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/753">softprops/action-gh-release#753</a></li>
  <li>fix: support Windows-style file globs by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/754">softprops/action-gh-release#754</a></li>
  <li>fix: normalize refs-tag inputs by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/755">softprops/action-gh-release#755</a></li>
  <li>fix: expand tilde file paths by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/756">softprops/action-gh-release#756</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>docs: clarify token precedence by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/752">softprops/action-gh-release#752</a></li>
  <li>docs: clarify GitHub release limits by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/758">softprops/action-gh-release#758</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>2.6.0</h2>
  <p><code>2.6.0</code> is a minor release centered on
  <code>previous_tag</code> support for
  <code>generate_release_notes</code>,
  which lets workflows pin GitHub's comparison base explicitly instead of
  relying on the default range.
  It also includes the recent concurrent asset upload recovery fix, a
  <code>working_directory</code> docs sync,
  a checked-bundle freshness guard for maintainers, and clearer
  immutable-prerelease guidance where
  GitHub platform behavior imposes constraints on how prerelease asset
  uploads can be published.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: support previous_tag for generate_release_notes by <a
  href="https://github.com/pocesar"><code>@​pocesar</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/372">softprops/action-gh-release#372</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: recover concurrent asset metadata 404s by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/760">softprops/action-gh-release#760</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>docs: clarify reused draft release behavior by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/759">softprops/action-gh-release#759</a></li>
  <li>docs: clarify working_directory input by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/761">softprops/action-gh-release#761</a></li>
  <li>ci: verify dist bundle freshness by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/762">softprops/action-gh-release#762</a></li>
  <li>fix: clarify immutable prerelease uploads by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/763">softprops/action-gh-release#763</a></li>
  </ul>
  <h2>2.5.3</h2>
  <p><code>2.5.3</code> is a patch release focused on the remaining
  path-handling and release-selection bugs uncovered after
  <code>2.5.2</code>.
  It fixes
  <code>[#639](https://github.com/softprops/action-gh-release/issues/639)</code>,
  <code>[#571](https://github.com/softprops/action-gh-release/issues/571)</code>,
  <code>[#280](https://github.com/softprops/action-gh-release/issues/280)</code>,
  <code>[#614](https://github.com/softprops/action-gh-release/issues/614)</code>,
  <code>[#311](https://github.com/softprops/action-gh-release/issues/311)</code>,
  <code>[#403](https://github.com/softprops/action-gh-release/issues/403)</code>,
  and
  <code>[#368](https://github.com/softprops/action-gh-release/issues/368)</code>.
  It also adds documentation clarifications for
  <code>[#541](https://github.com/softprops/action-gh-release/issues/541)</code>,
  <code>[#645](https://github.com/softprops/action-gh-release/issues/645)</code>,
  <code>[#542](https://github.com/softprops/action-gh-release/issues/542)</code>,
  <code>[#393](https://github.com/softprops/action-gh-release/issues/393)</code>,
  and
  <code>[#411](https://github.com/softprops/action-gh-release/issues/411)</code>,
  where the current behavior is either usage-sensitive or constrained by
  GitHub platform limits rather than an action-side runtime bug.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: prefer token input over GITHUB_TOKEN by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/751">softprops/action-gh-release#751</a></li>
  <li>fix: clean up duplicate drafts after canonicalization by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/753">softprops/action-gh-release#753</a></li>
  <li>fix: support Windows-style file globs by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/754">softprops/action-gh-release#754</a></li>
  <li>fix: normalize refs-tag inputs by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/755">softprops/action-gh-release#755</a></li>
  <li>fix: expand tilde file paths by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/756">softprops/action-gh-release#756</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>docs: clarify token precedence by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/752">softprops/action-gh-release#752</a></li>
  <li>docs: clarify GitHub release limits by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/758">softprops/action-gh-release#758</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/26e8ad27a09a225049a7075d7ec1caa2df6ff332"><code>26e8ad2</code></a>
  release 2.6.0</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/b959f31e968fb47fb7bb823087fc092d5613e0a4"><code>b959f31</code></a>
  fix: clarify immutable prerelease uploads (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/763">#763</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/8a8510e3a0d8dfc9296171fd405ca8c8ea6206a4"><code>8a8510e</code></a>
  ci: verify dist bundle freshness (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/762">#762</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/438c15ddf5b01e992ef98dc29cea3f9992ab54ac"><code>438c15d</code></a>
  docs: clarify working_directory input (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/761">#761</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/6ca3b5d96e3a0fac11dc53f0809c2cb029e64902"><code>6ca3b5d</code></a>
  fix: recover concurrent asset metadata 404s (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/760">#760</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/11f917660b31d6d56980ea3261f210556a812bd0"><code>11f9176</code></a>
  chore: add RELEASE.md</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/1f3f350167714515d2bcf8a18afcc5e8e0a362a8"><code>1f3f350</code></a>
  feat: add AGENTS.md</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/37819cb191890d306d21cfb5ac4e7a358f0a6e4f"><code>37819cb</code></a>
  docs: clarify reused draft release behavior (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/759">#759</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/93128644907200fa339c3d25d38cbc775278b05a"><code>9312864</code></a>
  feat: support previous_tag for generate_release_notes (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/372">#372</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/1853d73993c8ca1b2c9c1a7fede39682d0ab5c2a"><code>1853d73</code></a>
  release 2.5.3</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/a06a81a03ee405af7f2048a818ed3f03bbf83c7b...26e8ad27a09a225049a7075d7ec1caa2df6ff332">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=2.5.0&new-version=2.6.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`36986f0`](https://github.com/ghostty-org/ghostty/commit/36986f0374c987fe4f3ed378e0bd49246250702f) build(deps): bump dorny/paths-filter from 4.0.0 to 4.0.1 ([#11545](https://github.com/ghostty-org/ghostty/issues/11545)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  4.0.0 to 4.0.1.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/fbd0ab8f3e69293af611ebaee6363fc25e6d187d"><code>fbd0ab8</code></a>
  feat: add merge_group event support</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/efb1da7ce8d89bbc261191e5a2dc1453c3837339"><code>efb1da7</code></a>
  feat: add dist/ freshness check to PR workflow</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/d8f7b061b24c30a325ff314b76c37adb05b041ce"><code>d8f7b06</code></a>
  Merge pull request <a
  href="https://redirect.github.com/dorny/paths-filter/issues/302">#302</a>
  from dorny/issue-299</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/addbc147a95845176e1bc013a012fbf1d366389a"><code>addbc14</code></a>
  Update README for v4</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/9d7afb8d214ad99e78fbd4247752c4caed2b6e4c...fbd0ab8f3e69293af611ebaee6363fc25e6d187d">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=4.0.0&new-version=4.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`41c7321`](https://github.com/ghostty-org/ghostty/commit/41c7321e94995347d74a66c9847ad0e2d45c4ad0) Add missing plural forms ([#11541](https://github.com/ghostty-org/ghostty/issues/11541)) ([@00-kat](https://github.com/00-kat))
  ```text
  Supersedes #11529; I did not use their plural forms because I trust
  ctrl+c more than Claude Code.
  
  `mk` and `zh_*` are still missing theirs, but neither [gettext's table]
  nor the [documentation it copied from] list them. That PR has them too,
  with values magicked from… somewhere? The [data they linked] is
  illegible to me.
  
  [gettext's table]:
  https://cgit.git.savannah.gnu.org/cgit/gettext.git/tree/gettext-tools/src/plural-table.c?id=dbf9d71e0c4707ca1b14359256b3dcccecb8e837
  [documentation it copied from]:
  https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html
  [data they linked]:
  https://www.unicode.org/cldr/charts/48/supplemental/language_plural_rules.html
  ```
- [`a945115`](https://github.com/ghostty-org/ghostty/commit/a945115d2f5004df9448df1cfe375bec931b9d79) Sync CODEOWNERS vouch list ([#11542](https://github.com/ghostty-org/ghostty/issues/11542)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @alosarjos
  - @anhthang
  - @AnmiTaliDev
  - @crayxt
  - @MicaelJarniac
  ```

## March 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23121125985), [2](https://github.com/ghostty-org/ghostty/actions/runs/23114086713), [3](https://github.com/ghostty-org/ghostty/actions/runs/23114065115), [4](https://github.com/ghostty-org/ghostty/actions/runs/23112492758), [5](https://github.com/ghostty-org/ghostty/actions/runs/23104004789)  
Summary: 5 runs • 10 commits • 3 authors

### Changes

- [`ac5e57c`](https://github.com/ghostty-org/ghostty/commit/ac5e57ce67d3c6913935aa265617cb4d3f46aba4) input: extract mouse encoding to a pure, testable file ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move mouse event encoding logic from Surface.zig into a new
  input/mouse_encode.zig file.
  
  The new file encapsulates event filtering (shouldReport),
  button code computation, viewport bounds checking, motion
  deduplication, and all five wire formats (X10, UTF-8, SGR,
  urxvt, SGR-pixels). This makes the encoding independently
  testable and adds unit tests covering each format and edge
  case.
  
  Additionally, Surface `mouseReport` can no longer fail, since the only
  failure mode is no buffer space which should be impossible. Updated
  the signature to remove the error set.
  ```
- [`f1fd21f`](https://github.com/ghostty-org/ghostty/commit/f1fd21fd762ce8c6a7fa415734f63b08f05e36e1) input: extract mouse encoding to a pure, testable file ([#11538](https://github.com/ghostty-org/ghostty/issues/11538)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move mouse event encoding logic from Surface.zig into a new
  input/mouse_encode.zig file.
  
  The new file encapsulates event filtering (shouldReport), button code
  computation, viewport bounds checking, motion deduplication, and all
  five wire formats (X10, UTF-8, SGR, urxvt, SGR-pixels). This makes the
  encoding independently testable and adds unit tests covering each format
  and edge case.
  
  Additionally, Surface `mouseReport` can no longer fail, since the only
  failure mode is no buffer space which should be impossible. Updated the
  signature to remove the error set.
  ```
- [`a2b2b88`](https://github.com/ghostty-org/ghostty/commit/a2b2b883e8e74328463c23a6e925b31475b78330) Update VOUCHED list ([#11540](https://github.com/ghostty-org/ghostty/issues/11540)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11518#issuecomment-4064084617)
  from @jparise.
  
  Vouch: @j0hnm4r5
  ```
- [`33263db`](https://github.com/ghostty-org/ghostty/commit/33263dbe6fea331b1be1acd4a7420d89f98ae806) Update VOUCHED list ([#11532](https://github.com/ghostty-org/ghostty/issues/11532)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11250#discussioncomment-16143210)
  from @mitchellh.
  
  Vouch: @PowerUser64
  ```
- [`57428f3`](https://github.com/ghostty-org/ghostty/commit/57428f33c6af820a30efbb57600c030a4df693f6) Update VOUCHED list ([#11533](https://github.com/ghostty-org/ghostty/issues/11533)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11237#discussioncomment-16143212)
  from @mitchellh.
  
  Vouch: @cadebrown
  ```
- [`0e272bf`](https://github.com/ghostty-org/ghostty/commit/0e272bfa10475cf98dc4967aa2b18f0257fafee5) Update VOUCHED list ([#11531](https://github.com/ghostty-org/ghostty/issues/11531)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11041#discussioncomment-16143204)
  from @mitchellh.
  
  Vouch: @davidsanchez222
  ```
- [`943d3d2`](https://github.com/ghostty-org/ghostty/commit/943d3d2e8906cbd610868c36eccfc3a1360e0fd2) vt: add setopt_from_terminal to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose the key encoder Options.fromTerminal function to the C API as
  ghostty_key_encoder_setopt_from_terminal. This lets C callers sync all
  terminal-derived encoding options (cursor key application mode, keypad
  mode, alt escape prefix, modifyOtherKeys, and Kitty flags) in a single
  call instead of setting each option individually.
  ```
- [`a7514d3`](https://github.com/ghostty-org/ghostty/commit/a7514d389b6c2d543fa7d548989cbd219e96c758) vt: add setopt_from_terminal to C API ([#11524](https://github.com/ghostty-org/ghostty/issues/11524)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose the key encoder Options.fromTerminal function to the C API as
  ghostty_key_encoder_setopt_from_terminal. This lets C callers sync all
  terminal-derived encoding options (cursor key application mode, keypad
  mode, alt escape prefix, modifyOtherKeys, and Kitty flags) in a single
  call instead of setting each option individually.
  ```
- [`86d9a04`](https://github.com/ghostty-org/ghostty/commit/86d9a04ece47f2309e4882c1ca3334fbba23ba3c) config: add `equal` option to `window-padding-balance` ([@devsunb](https://github.com/devsunb))
  ```text
  Change `window-padding-balance` from `bool` to an enum with three
  values:
  
  - `false` - no balancing (default, unchanged)
  - `true` - balance with vshift that caps top padding and shifts excess
    to bottom (existing behavior, unchanged)
  - `equal` - balance whitespace equally on all four sides
  
  This gives users who prefer truly equal padding a way to opt in without
  changing the default behavior.
  ```
- [`c923655`](https://github.com/ghostty-org/ghostty/commit/c9236558b10da592bbb0b928140bea8cb94c74ae) config: add `equal` option to `window-padding-balance` ([#11491](https://github.com/ghostty-org/ghostty/issues/11491)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Change `window-padding-balance` from `bool` to an enum with three
  values:
  
  - `false` - no balancing (default, unchanged)
  - `true` - balance with vshift that caps top padding and shifts excess
  to bottom (existing behavior, unchanged)
  - `equal` - balance whitespace equally on all four sides
  
  This gives users who prefer truly equal padding a way to opt in without
  changing the default behavior.
  ```

## March 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23098143300), [2](https://github.com/ghostty-org/ghostty/actions/runs/23090671545), [3](https://github.com/ghostty-org/ghostty/actions/runs/23088656823)  
Summary: 3 runs • 20 commits • 2 authors

### Changes

- [`302e68f`](https://github.com/ghostty-org/ghostty/commit/302e68fd3d9891919a3b6f32f47ee7f954bef848) vt: expose ghostty_terminal_new/free ([@mitchellh](https://github.com/mitchellh))
- [`18fdc15`](https://github.com/ghostty-org/ghostty/commit/18fdc15357a2f519d93987d09a2957b9369340cb) vt: ghostty_terminal_vt_write ([@mitchellh](https://github.com/mitchellh))
- [`8b9afe3`](https://github.com/ghostty-org/ghostty/commit/8b9afe35a706ea230473c81637c3f43f07d736b7) vt: ghostty_terminal_scroll_viewport ([@mitchellh](https://github.com/mitchellh))
- [`fe6e7fb`](https://github.com/ghostty-org/ghostty/commit/fe6e7fbc6b54c835f9a5229f0b19ee9f96ec5a92) vt: ghostty_terminal_resize ([@mitchellh](https://github.com/mitchellh))
- [`aa3e6e2`](https://github.com/ghostty-org/ghostty/commit/aa3e6e23a227cfe4ba0026d844b54e7a89ea880b) vt: ghostty_terminal_reset ([@mitchellh](https://github.com/mitchellh))
- [`34acdfc`](https://github.com/ghostty-org/ghostty/commit/34acdfcc4eca388d3d4fa1a5ce03525384db8e3e) vt: update terminal.h docs ([@mitchellh](https://github.com/mitchellh))
- [`8e6bf82`](https://github.com/ghostty-org/ghostty/commit/8e6bf829a746be199bd30d4670fe855035562433) terminal/osc: don't export context/semantic prompts to libvt yet ([@mitchellh](https://github.com/mitchellh))
- [`b5fb7ec`](https://github.com/ghostty-org/ghostty/commit/b5fb7ecaaaa2d788093809614d88b6294baaf672) vt: wip formatter api ([@mitchellh](https://github.com/mitchellh))
- [`4e494cc`](https://github.com/ghostty-org/ghostty/commit/4e494ccd688cd44f92d010cdd6fa46412339f69e) lib: lib.Struct can convert packed structs to extern structs ([@mitchellh](https://github.com/mitchellh))
- [`09d3ebd`](https://github.com/ghostty-org/ghostty/commit/09d3ebd80df2988dd48cc94a4826a226a7c2d269) vt: use explicit options structs ([@mitchellh](https://github.com/mitchellh))
- [`a2d570b`](https://github.com/ghostty-org/ghostty/commit/a2d570b51e059fc9fc572dcb155e81215a9c51bc) vt: add sized struct pattern and types.h ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a size field as the first member of formatter option structs
  (TerminalOptions, TerminalOptions.Extra, ScreenOptions.Extra) for ABI
  compatibility. This allows adding new fields without breaking callers
  compiled against older versions of the struct.
  
  Introduce include/ghostty/vt/types.h as the foundational header
  containing GhosttyResult and the GHOSTTY_INIT_SIZED macro for
  zero-initializing sized structs. Remove the separate result.h header,
  moving its contents into types.h.
  ```
- [`7c12d6e`](https://github.com/ghostty-org/ghostty/commit/7c12d6e35d9e1cc28f71877559c17b4088f32532) agents: skill for writing commit messages ([@mitchellh](https://github.com/mitchellh))
- [`3c8feda`](https://github.com/ghostty-org/ghostty/commit/3c8feda118cc4bd51cadc5f4c98e54158716a2c0) vt: add format_alloc to C API formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename the existing format function to format_buf to clarify that it
  writes into a caller-provided buffer. Add a new format_alloc variant
  that allocates the output buffer internally using the provided
  allocator (or the default if NULL). The caller receives the allocated
  pointer and length and is responsible for freeing it.
  
  This is useful for consumers that do not know the required buffer size
  ahead of time and want to avoid the two-pass query-then-format pattern
  needed with format_buf.
  ```
- [`1e21ac1`](https://github.com/ghostty-org/ghostty/commit/1e21ac119079bf7bc4d965666ce1f691ce4d84c5) example: add c-vt-formatter example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an example showing how to use the ghostty-vt terminal and
  formatter APIs from C. The example creates a terminal, writes
  VT-encoded content with cursor movement and styling sequences,
  then formats the screen contents as plain text using the formatter
  API.
  ```
- [`4ad7d03`](https://github.com/ghostty-org/ghostty/commit/4ad7d03c56de3216f2a82c8790d0c8edb216db07) terminal/formatter: safely cast discarding.count to usize ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Discarding writer count field is u64, but appendNTimes expects
  usize which is u32 on 32-bit targets like arm-linux-androideabi.
  Use std.math.cast instead of @intCast to safely handle the
  conversion, returning WriteFailed on overflow rather than risking
  undefined behavior.
  ```
- [`647f5ad`](https://github.com/ghostty-org/ghostty/commit/647f5adf556e13abcbe4b38c185fb81458aa5711) terminal/formatter: safely cast discarding.count to usize ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Discarding writer count field is u64, but several call sites
  pass it where a usize is expected. On wasm32-freestanding, usize is
  32-bit, so this caused compilation errors.
  
  Use std.math.cast instead of a bare @intCast so that overflow is
  handled gracefully, returning WriteFailed rather than triggering
  safety-checked undefined behavior at runtime.
  ```
- [`f730eed`](https://github.com/ghostty-org/ghostty/commit/f730eed213143db6e3082311f54afbf0c87bdd2d) vt: fix missing formatter docs in doxygen ([@mitchellh](https://github.com/mitchellh))
- [`952fbce`](https://github.com/ghostty-org/ghostty/commit/952fbce0e50ded8fd8e6ee5f64e9650af962cd19) libghostty: add initial C API for terminal, formatter ([#11506](https://github.com/ghostty-org/ghostty/issues/11506)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds an initial C API for terminals and formatting. There is a new
  example that shows how to use this.
  
  With these APIs in place, users of the C API can now create a terminal,
  pass raw VT streams to it, and dump the terminal viewport to various
  formats. As noted in the docs, **the formatter API is not a rendering
  API**, it isn't high performance enough for that. But it's a simpler API
  to implement than the render state API so I started with that.
  
  Both APIs are purposely fairly minimal, we're just setting the stage for
  future functionality.
  
  ## Example
  
  ```c
  #include <ghostty/vt.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main() {
    GhosttyTerminal term;
    GhosttyTerminalOptions opts = { .cols = 80, .rows = 24, .max_scrollback = 0 };
    ghostty_terminal_new(NULL, &term, opts);
  
    const char *input = "Hello, \033[1mBold\033[0m World!\r\nLine 2\r\n";
    ghostty_terminal_vt_write(term, (const uint8_t *)input, strlen(input));
  
    GhosttyFormatterTerminalOptions fmt = GHOSTTY_INIT_SIZED(GhosttyFormatterTerminalOptions);
    fmt.emit = GHOSTTY_FORMATTER_FORMAT_PLAIN;
    fmt.trim = true;
  
    GhosttyFormatter fmtr;
    ghostty_formatter_terminal_new(NULL, &fmtr, term, fmt);
  
    uint8_t *buf;
    size_t len;
    ghostty_formatter_format_alloc(fmtr, NULL, &buf, &len);
    fwrite(buf, 1, len, stdout);
  
    free(buf);
    ghostty_formatter_free(fmtr);
    ghostty_terminal_free(term);
  }
  ```
  
  ## New APIs
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_terminal_new` | Create a new terminal instance |
  | `ghostty_terminal_free` | Free a terminal instance |
  | `ghostty_terminal_reset` | Full reset of the terminal (RIS) |
  | `ghostty_terminal_resize` | Resize the terminal to given dimensions |
  | `ghostty_terminal_vt_write` | Write VT-encoded data to the terminal |
  | `ghostty_terminal_scroll_viewport` | Scroll the terminal viewport |
  | `ghostty_formatter_terminal_new` | Create a formatter for a terminal's
  active screen |
  | `ghostty_formatter_format_buf` | Format into a caller-provided buffer
  |
  | `ghostty_formatter_format_alloc` | Format into an allocated buffer |
  | `ghostty_formatter_free` | Free a formatter instance |
  
  ## Future
  
  - Obviously need to expose a lot more from the terminal:
    * Read current set modes
    * Read cursor information
    * Read screen information
    * etc...
  - Need an optional callback system so that `vt_write` can invoke
  callbacks for side effect sequences like clipboards, title setting,
  responses, etc.
  - `terminal.RenderState` C API so that people can build high performance
  renderers on top of libghostty-vt
  
  And so on...
  ````
- [`1844a5f`](https://github.com/ghostty-org/ghostty/commit/1844a5f7bafbade1305e95d515eedcb010aae104) Update VOUCHED list ([#11492](https://github.com/ghostty-org/ghostty/issues/11492)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11491#issuecomment-4060704311)
  from @mitchellh.
  
  Vouch: @devsunb
  ```
- [`6368b00`](https://github.com/ghostty-org/ghostty/commit/6368b00604e4543088eda552a8aa3f6776500332) Update VOUCHED list ([#11488](https://github.com/ghostty-org/ghostty/issues/11488)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11485#discussioncomment-16130186)
  from @mitchellh.
  
  Vouch: @jesusvazquez
  ```

