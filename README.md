> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 8, 2026 at 07:44 UTC.

## September 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34187628915)  
Summary: 1 runs • 2 commits • 1 authors

### Changes

- [`dd2edd7`](https://github.com/ghostty-org/ghostty/commit/dd2edd760da6b90b01ef88f75e1bea8a71b31e3f) libvt: return safe pointers for empty output ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```
- [`b0c421f`](https://github.com/ghostty-org/ghostty/commit/b0c421fcd2e290629d4285c181b52fe2f2095f06) libghostty: return safe pointers for empty output ([#14177](https://github.com/ghostty-org/ghostty/issues/14177)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```

## September 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34145900617), [2](https://github.com/ghostty-org/ghostty/actions/runs/34143207969), [3](https://github.com/ghostty-org/ghostty/actions/runs/34075296265), [4](https://github.com/ghostty-org/ghostty/actions/runs/34068510483)  
Summary: 4 runs • 11 commits • 5 authors

### Changes

- [`5909690`](https://github.com/ghostty-org/ghostty/commit/5909690de1d942c8b846dfd51c8a26e510436ade) config: rebuild RepeatableCommand's C mirror on clone ([@i999rri](https://github.com/i999rri))
  ```text
  Cloning value_c copied Command.C structs whose string pointers
  still referenced the source config's memory; once the source was
  freed, an embedded host reading the command list after a config
  replace (ghostty_config_clone + ghostty_config_free of the old
  one) hit use-after-free, caught by ASan. Rebuild the mirror from
  the cloned commands with the same cval path parseCLI uses, and add
  a regression test asserting the clone's C strings do not alias the
  source's.
  ```
- [`72cf508`](https://github.com/ghostty-org/ghostty/commit/72cf508551cb1c559c9ca32330e9647399031ebb) renderer: never stop the display link while holding the draw mutex ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes
  the same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`623106c`](https://github.com/ghostty-org/ghostty/commit/623106cc4ea9ad5b8cc070e5e5c5260eb6eeaa7b) config: rebuild RepeatableCommand's C mirror on clone ([#14170](https://github.com/ghostty-org/ghostty/issues/14170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Why
  
  `RepeatableCommand.clone` copies `value_c` shallowly: the cloned
  `Command.C` structs keep string pointers into the *source* config's
  memory, so the clone only stays valid as long as its source lives. Every
  other field of a config clone is a deep copy — this is the one spot
  where the clone silently borrows.
  
  The macOS app never notices because of how it rotates configs: its
  clone's source is the core-owned live config, and both are replaced
  together on the next reload, so a clone never outlives its source. An
  embedder that clones a config and then frees the source — a legal
  sequence, e.g. promoting the clone to be the new active config — reads
  freed memory the next time it fetches `command-palette-entry` through
  the C API. Caught by AddressSanitizer.
  
  History: the shallow copy is as old as the C exposure itself.
  `dbe6035da` introduced `RepeatableCommand` with a correct deep `clone`
  (zig-side `value` only); `017021787` added the `value_c` mirror for
  `ghostty_config_get`, maintaining it carefully in `init`/`parseCLI` but
  extending `clone` with only the mechanical `ArrayList.clone` — the
  struct array copies, the string ownership doesn't. Nothing in-tree
  exercises clone-then-free-source, so it stayed latent.
  
  ## What
  
  Rebuild the C mirror from the cloned commands using the same
  `Command.cval` path `parseCLI` uses, so the clone's C strings live in
  the clone's own allocation. A regression test asserts the clone's C
  strings do not alias the source's while staying equal in content.
  
  ## AI disclosure
  
  Developed with AI assistance (Claude Code). The bug was found by
  AddressSanitizer while testing the Windows embedding host; the
  root-cause analysis, the fix, and the regression test were produced in
  an AI-assisted session, then reviewed and verified by the submitter
  (ASan clean after the fix, `RepeatableCommand` tests passing).
  ```
- [`82232ec`](https://github.com/ghostty-org/ghostty/commit/82232ecde55405559dec29c5466cb9e39938cb41) renderer: never stop the display link while holding the draw mutex ([#14171](https://github.com/ghostty-org/ghostty/issues/14171)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes the
  same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`258c057`](https://github.com/ghostty-org/ghostty/commit/258c057c0ac7d23b8a908fc1f4c5636670ccdcd1) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action) from 1.4 to 1.5.
  - [Release notes](https://github.com/ryand56/r2-upload-action/releases)
  - [Commits](https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317)
  
  ---
  updated-dependencies:
  - dependency-name: ryand56/r2-upload-action
    dependency-version: '1.5'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e9283ba`](https://github.com/ghostty-org/ghostty/commit/e9283ba872bfb2135dbaadea68d08980dbae5f88) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts) from 1.4.0 to 1.8.0.
  - [Release notes](https://github.com/c-hive/gha-remove-artifacts/releases)
  - [Commits](https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61)
  
  ---
  updated-dependencies:
  - dependency-name: c-hive/gha-remove-artifacts
    dependency-version: 1.8.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`ccaf7c7`](https://github.com/ghostty-org/ghostty/commit/ccaf7c776144cb5200fa0de605159cb90788a286) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([#14164](https://github.com/ghostty-org/ghostty/issues/14164)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action)
  from 1.4 to 1.5.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/ryand56/r2-upload-action/releases">ryand56/r2-upload-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.9.0
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/524">ryand56/r2-upload-action#524</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.686.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/526">ryand56/r2-upload-action#526</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.687.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/527">ryand56/r2-upload-action#527</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.688.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/528">ryand56/r2-upload-action#528</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.689.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/529">ryand56/r2-upload-action#529</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.691.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/530">ryand56/r2-upload-action#530</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v16 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/531">ryand56/r2-upload-action#531</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/532">ryand56/r2-upload-action#532</a></li>
  <li>chore(deps): update dependency <code>@​vercel/ncc</code> to v0.38.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/534">ryand56/r2-upload-action#534</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/533">ryand56/r2-upload-action#533</a></li>
  <li>chore(deps): update dependency typescript to v5.7.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/537">ryand56/r2-upload-action#537</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.700.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/536">ryand56/r2-upload-action#536</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.701.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/538">ryand56/r2-upload-action#538</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.703.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/539">ryand56/r2-upload-action#539</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.1
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/535">ryand56/r2-upload-action#535</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/540">ryand56/r2-upload-action#540</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/541">ryand56/r2-upload-action#541</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.705.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/542">ryand56/r2-upload-action#542</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.709.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/543">ryand56/r2-upload-action#543</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.2
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/544">ryand56/r2-upload-action#544</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.712.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/545">ryand56/r2-upload-action#545</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.713.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/546">ryand56/r2-upload-action#546</a></li>
  <li>fix(deps): update dependency mime to v4.0.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/548">ryand56/r2-upload-action#548</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.715.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/547">ryand56/r2-upload-action#547</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.717.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/549">ryand56/r2-upload-action#549</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/550">ryand56/r2-upload-action#550</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.5
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/551">ryand56/r2-upload-action#551</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.722.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/552">ryand56/r2-upload-action#552</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.723.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/553">ryand56/r2-upload-action#553</a></li>
  <li>chore(deps): update dependency typescript to v5.7.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/554">ryand56/r2-upload-action#554</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.726.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/555">ryand56/r2-upload-action#555</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.6
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/556">ryand56/r2-upload-action#556</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.731.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/557">ryand56/r2-upload-action#557</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.7
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/558">ryand56/r2-upload-action#558</a></li>
  <li>chore(deps): update determinatesystems/magic-nix-cache-action action
  to v9 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/560">ryand56/r2-upload-action#560</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.10.10 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/561">ryand56/r2-upload-action#561</a></li>
  <li>chore(deps): update dependency typescript to v5.8.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/564">ryand56/r2-upload-action#564</a></li>
  <li>ci(test-nix): replace magic nix cache with flakehub cache by <a
  href="https://github.com/ryand56"><code>@​ryand56</code></a> in <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/567">ryand56/r2-upload-action#567</a></li>
  <li>chore(deps): update dependency typescript to v5.8.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/566">ryand56/r2-upload-action#566</a></li>
  <li>fix(deps): update dependency mime to v4.0.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/565">ryand56/r2-upload-action#565</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v17 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/569">ryand56/r2-upload-action#569</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.810.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/559">ryand56/r2-upload-action#559</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.19 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/572">ryand56/r2-upload-action#572</a></li>
  <li>chore(deps): update stefanzweifel/git-auto-commit-action action to
  v6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/576">ryand56/r2-upload-action#576</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.832.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/571">ryand56/r2-upload-action#571</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.33 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/573">ryand56/r2-upload-action#573</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.837.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/577">ryand56/r2-upload-action#577</a></li>
  <li>chore(deps): update dependency dotenv to v16.6.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/578">ryand56/r2-upload-action#578</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317"><code>33ebb7a</code></a>
  chore: update to nodejs 24</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/61474c8f6a21b0dd8fc877a0b93c2c2078c88f60"><code>61474c8</code></a>
  chore: update mappings [skip ci]</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/7d9e7c27f8702296342da8daf84e76b24e43622d"><code>7d9e7c2</code></a>
  chore(deps): update typescript to v6</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/6e86c77f4ab91d5b532f6156c15509ef35fd905a"><code>6e86c77</code></a>
  fix(renovate): increase minimumReleaseAge and add packageRules for
  ts</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/fd3d3d4ccdcea99f8e7cc84bbb0a468147e9235e"><code>fd3d3d4</code></a>
  chore(deps): update dependency jest to v30.5.1</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/0b5990b910991eb1c068df9f99384b66e0b49e41"><code>0b5990b</code></a>
  chore(deps): update dependency github-action-ts-run-api to v3.1.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/4196309eee620f2cd556648b16b4b45fd959cee9"><code>4196309</code></a>
  chore(deps): update dependency dotenv to v17.4.2</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/d62fd1388703f08312d5f62fdef74f4b363a2802"><code>d62fd13</code></a>
  chore(deps): update dependency <code>@​vercel/ncc</code> to ^0.45.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/5124bb99384f12af4f3947f0c6a8f6509d580079"><code>5124bb9</code></a>
  chore(deps): update dependency ts-jest to v29.4.12</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/820995a4f185d5c18d4c60e6e371494e3046b336"><code>820995a</code></a>
  chore(deps): update dependency <code>@​actions/core</code> to
  v3.0.1</li>
  <li>Additional commits viewable in <a
  href="https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=ryand56/r2-upload-action&package-manager=github_actions&previous-version=1.4&new-version=1.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`da9e216`](https://github.com/ghostty-org/ghostty/commit/da9e21602f918d47a46399c458937eff7c7a74ac) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([#14165](https://github.com/ghostty-org/ghostty/issues/14165)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts)
  from 1.4.0 to 1.8.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/c-hive/gha-remove-artifacts/releases">c-hive/gha-remove-artifacts's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.8.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>skip-recent-commits</code> input keeps every artifact of
  the N most recent commits, regardless of how many artifacts each commit
  produced. Applied before <code>skip-recent</code>, so the two can be
  combined. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/28">#28</a></li>
  <li><code>GITHUB_TOKEN</code> can now be set on both <code>env:</code>
  and <code>with:</code> (for example when it is exported for all steps)
  without the action failing. The input takes precedence. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/48">#48</a></li>
  </ul>
  <h2>v1.7.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>dry-run</code> input: logs which artifacts would be
  removed without deleting anything.</li>
  <li>Stricter input validation. <code>age</code> now rejects fractional
  amounts and units that are not durations (for example <code>30 D</code>,
  which moment silently treated as zero); <code>skip-recent</code> and
  <code>max-retries</code> must be non-negative integers. Previously such
  values could make every artifact eligible for deletion.</li>
  <li>Artifacts without commit information are reported separately from
  tagged ones when <code>skip-tags</code> is on.</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>Rewritten in TypeScript under <code>src/</code>, bundled with
  esbuild</li>
  <li>Unit tests for input parsing and the cleanup plan, plus end-to-end
  tests against a mock GitHub API covering deletion, rate limit retries
  and failure handling</li>
  <li>CI split into lint, typecheck, test, build and run jobs</li>
  <li>Dropped dependencies: yn, dotenv-safe, cross-env,
  eslint-plugin-import</li>
  </ul>
  <h2>v1.6.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>Artifacts are now listed repo-wide instead of per workflow run. This
  cuts API requests by roughly two orders of magnitude and removes the
  hardcoded 90-day window, so artifacts on repositories with longer
  retention are now cleaned up too. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/62">#62</a></li>
  <li>A failed deletion no longer aborts the run: remaining artifacts are
  still processed and the action fails at the end with a count.</li>
  <li>With <code>skip-tags</code>, artifacts without commit information
  are kept rather than deleted.</li>
  <li>The log ends with a summary of removed and skipped artifacts. Fixes
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/21">#21</a></li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>CI checks that <code>dist/</code> matches the source instead of
  auto-committing it</li>
  <li>Removed CodeQL workflow, pre-commit hooks and
  eslint-plugin-import</li>
  <li>Dependency purposes documented in <code>package.json</code></li>
  </ul>
  <h2>v1.5.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>max-retries</code> input caps how often a rate-limited
  request is retried before the action fails. <strong>Default: 5.</strong>
  Previously requests were retried indefinitely; set a larger value to
  keep the old behaviour. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/36">#36</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/49">#49</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/51">#51</a></li>
  <li>Action runtime updated to Node 24 (<a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/63">#63</a>)</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>All dependencies upgraded (<code>@actions/core</code> 3,
  <code>@octokit/action</code> 8, <code>@octokit/plugin-throttling</code>
  11, moment 2.30). <code>pnpm audit</code> reports no known
  vulnerabilities.</li>
  <li>Source converted to ESM, bundled with <code>@vercel/ncc</code></li>
  <li>Tooling: pnpm, ESLint 10, Prettier 3, CI on Node 24</li>
  <li>Docs: <code>action.yml</code> description, updated retention docs
  link</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/62c2fbea931baa7dd4a6b73ea5a799984a818f61"><code>62c2fbe</code></a>
  Bump version to 1.8.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/449a616233a48dbdd28ba5e08f4c2fb62913afa8"><code>449a616</code></a>
  Add skip-recent-commits input and accept GITHUB_TOKEN from env and
  input</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/4bff15786ba0b91dd8ed7c32459eb72441ac1b6c"><code>4bff157</code></a>
  Bump version to 1.7.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/a52e55eb4fd2dd1ce50f4e125d7e5855873bb38a"><code>a52e55e</code></a>
  Add end-to-end tests against a mock GitHub API</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/03f14e2351077f8bc463a7887eba3d4c062347b1"><code>03f14e2</code></a>
  Simplify config parsing, logging and tsconfig</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/04de7b0694b817261c05361cebc55090c8be4fb8"><code>04de7b0</code></a>
  Address review findings on the TypeScript rewrite</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/8b74b1b6fcb2881415de6d93701d4f4de6b170b1"><code>8b74b1b</code></a>
  Rewrite in TypeScript, add tests, merge CI workflows</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/73aaf4a5bf7a8fc25eca958284e770e44493029a"><code>73aaf4a</code></a>
  Bump version to 1.6.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/c4da97c8ee1e02b19ba57ae62c3fafd4b618e06d"><code>c4da97c</code></a>
  Ignore CLAUDE.local.md</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/614c11c542a610a4eec69c8e2faa27904004155f"><code>614c11c</code></a>
  Describe each dependency in package.json</li>
  <li>Additional commits viewable in <a
  href="https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=c-hive/gha-remove-artifacts&package-manager=github_actions&previous-version=1.4.0&new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`2b3b893`](https://github.com/ghostty-org/ghostty/commit/2b3b893919e0bee74b567598e741a735777c9687) deps: update translate-c backport ([@vancluever](https://github.com/vancluever))
- [`82938b6`](https://github.com/ghostty-org/ghostty/commit/82938b633ba646db38591d969c3c526332bd7e65) deps: update translate-c backport ([#14126](https://github.com/ghostty-org/ghostty/issues/14126)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is just a monthly refresh, things have been pretty quiet on both
  the Aro and translate-c sides.
  
  https://github.com/vancluever/arocc/compare/ecbc5c7...f97cdfc
  
  https://codeberg.org/vancluever/translate-c/compare/05e7b9dd87...4e879eb8ab
  ```
- [`97f2ddb`](https://github.com/ghostty-org/ghostty/commit/97f2ddb06e43ed73948385944cd1b0c19c282807) Sync CODEOWNERS vouch list ([#14163](https://github.com/ghostty-org/ghostty/issues/14163)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @slowdub
  ```

## September 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34063395508)  
Summary: 1 runs • 4 commits • 3 authors

### Changes

- [`501e7b5`](https://github.com/ghostty-org/ghostty/commit/501e7b5c1cf04162305c56e85204d2b1ac9427fb) pkg/fontconfig: update to 2.18.3 ([@vancluever](https://github.com/vancluever))
  ```text
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`11d1cc4`](https://github.com/ghostty-org/ghostty/commit/11d1cc4fc8decc84048bde1b746f3a013493e36f) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`955d902`](https://github.com/ghostty-org/ghostty/commit/955d902fa6abb3aaf71cac60d6b81bd83fa7fc69) pkg/fontconfig: update to 2.18.3 ([#14113](https://github.com/ghostty-org/ghostty/issues/14113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #14071 (just additional review and local re-generation/re-org
  of needed headers).
  
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`f426f6f`](https://github.com/ghostty-org/ghostty/commit/f426f6f181ba95f45d33f683fb754b6359d9e04f) Update iTerm2 colorschemes ([#14159](https://github.com/ghostty-org/ghostty/issues/14159)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260831-151010-752a9c0
  ```

## September 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33902692149), [2](https://github.com/ghostty-org/ghostty/actions/runs/33895939538)  
Summary: 2 runs • 9 commits • 1 authors

### Changes

- [`636a2f3`](https://github.com/ghostty-org/ghostty/commit/636a2f35b4a37fbb1b58dd801ae14513d355e95e) input: preserve numeric keypad output with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`e7bdda9`](https://github.com/ghostty-org/ghostty/commit/e7bdda9918a87f74178e15132c2894e29a8bf271) input: encode F13 through F25 ([@mitchellh](https://github.com/mitchellh))
- [`37e3cdd`](https://github.com/ghostty-org/ghostty/commit/37e3cdd2d281feb2bb403600974289406f891461) input: encode alt+escape with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`cc3fd8a`](https://github.com/ghostty-org/ghostty/commit/cc3fd8a773300371e2d1f41265128a7bf10adfa2) input: encode help and context menu keys ([@mitchellh](https://github.com/mitchellh))
- [`b97654f`](https://github.com/ghostty-org/ghostty/commit/b97654fe76a8badbbb0c51c0c0e2156fd12f0731) input: improve xterm modifyOtherKeys 2 compatibility ([#14145](https://github.com/ghostty-org/ghostty/issues/14145)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #14144
  
  I wrote a harness that created all possible US-layout keyboard input
  combinations with xterm patch 411 and Ghostty main and compared their
  full encoding sequence. There are various miscompatibilities on purpose
  but these were definitely bugs I wanted to address first.
  
  - Normal-mode numeric keypad keys now preserve their numeric output
  instead of falling through to generic MOK2 encoding. Application keypad
  behavior is unchanged.
  - F13 through F25 now emit their xterm-compatible function-key
  sequences, including modifier parameters.
  - Help and Context Menu now emit editing-key codes 28 and 29.
  - Alt+Escape now emits `CSI 27;3;27~` under MOK2 while retaining the
  traditional `ESC ESC` encoding otherwise.
  
  After these changes, 2,081 of 2,096 cases match xterm exactly. The
  remaining 15 differences are intentional.
  ```
- [`587e08f`](https://github.com/ghostty-org/ghostty/commit/587e08f3f70d29c7bc196e2cd919bd4b11f9b5bb) input: encode non-ASCII alt prefixes as UTF-8 ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to
  the UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without changing
  MOK2. The cases I'm talking about are in my comparison harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`492300c`](https://github.com/ghostty-org/ghostty/commit/492300cad104195411d12217dd22f1cd05f31376) input: encode non-ASCII alt prefixes as UTF-8 ([#14146](https://github.com/ghostty-org/ghostty/issues/14146)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to the
  UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without
  changing MOK2. The cases I'm talking about are in my comparison
  harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`4406cea`](https://github.com/ghostty-org/ghostty/commit/4406cea3e9fde88876551cedfef10d3b245b75b6) input: encode ctrl keys with modifyOtherKeys 2 ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still encoded
  as C0 bytes. This is wrong. I'm going to do a more in depth audit if
  possible with every possible key combination against xterm to see where
  we diverge but this fixes this for now without regressing any tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```
- [`1f5bb57`](https://github.com/ghostty-org/ghostty/commit/1f5bb5769fbb5e717546073d33d3985604a315b2) input: encode ctrl keys with modifyOtherKeys 2 ([#14144](https://github.com/ghostty-org/ghostty/issues/14144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still
  encoded as C0 bytes. This is wrong. I'm going to do a more in depth
  audit if possible with every possible key combination against xterm to
  see where we diverge but this fixes this for now without regressing any
  tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```

## September 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33819135265), [2](https://github.com/ghostty-org/ghostty/actions/runs/33796979743), [3](https://github.com/ghostty-org/ghostty/actions/runs/33777214262), [4](https://github.com/ghostty-org/ghostty/actions/runs/33716226971), [5](https://github.com/ghostty-org/ghostty/actions/runs/33712675217)  
Summary: 5 runs • 21 commits • 4 authors

### Changes

- [`efa3c66`](https://github.com/ghostty-org/ghostty/commit/efa3c66ed16ea9251d5b2a74b606aabc248d2c00) terminal: PageList nodes are pooled individually from the gpa instead of an arena ([@mitchellh](https://github.com/mitchellh))
- [`35a6fb7`](https://github.com/ghostty-org/ghostty/commit/35a6fb747f5d60ee6d92a7f5667474914a47cf21) terminal: PageList preheats only the viewport and cursor pins ([@mitchellh](https://github.com/mitchellh))
- [`105d0a5`](https://github.com/ghostty-org/ghostty/commit/105d0a5453654f15cbe9e902df9e72ed62fa5474) terminal: C terminal wrapper allocates the kitty temp dir path only when it is set ([@mitchellh](https://github.com/mitchellh))
- [`d1cd56a`](https://github.com/ghostty-org/ghostty/commit/d1cd56a56c4244d9d9fadae028cbffc23a1d3d1a) terminal: dynamic palette shares the built-in default instead of copying it per terminal ([@mitchellh](https://github.com/mitchellh))
- [`c81f0b2`](https://github.com/ghostty-org/ghostty/commit/c81f0b26871c7fbbe2fc35549fdad1f64ed29094) terminal: cut the fixed heap cost of a new terminal nearly in half ([#14138](https://github.com/ghostty-org/ghostty/issues/14138)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This focuses explicitly on the non-mmap allocations for a
  `ghostty_terminal_new` result. The result is that we lower this portion
  of the memory by almost half. The total benefit is smaller since 70% of
  a terminal is mmap'd allocations, but this still yields an absolute ~5KB
  savings on macOS on every new terminal (not just empty, but also with a
  normal prompt and so on).
  
  Four changes to make it happy, broken down into individual commits.
  Nothing crazy:
  
  - **Page list nodes are pooled individually.** The node pool was a
  `std.heap.MemoryPool`, which sits on an arena that preheats and grows
  1.5x, so we paid for wasted space. Nodes now come from `UntouchedPool`
  (the same pool as page buffers) with a preheat of one, so the cost is
  exactlyone node (well, exactly one bucket element size in whatever
  allocator).
  - **Pin pool and tracked pin set are sized for two pins.** Every screen
  tracks exactly a viewport pin and a cursor pin at creation, but we
  preheated eight pins and let the tracked pin map grow to 17 slots on the
  first insert via doubling.
  - **The kitty temp dir path is allocated only when set.** The C wrapper
  embedded a 1 KiB `max_path_bytes` buffer that only embedders that set
  `kitty_image_medium_temp_file` ever wrote to.
  - **The default palette is shared instead of copied.** `DynamicPalette`
  carried two full 1 KiB palettes, `current` and `original`, and
  `original` was almost always the built-in default. It is now a pointer
  to the shared built-in default, or to an allocator-owned copy when a
  custom default is set. This introduces a new OOM path but we gracefully
  handle it by either ignoring or resetting.
  
  Memory measurements:
  
  | Per terminal                                | Before   | After    |
  |---------------------------------------------|----------|----------|
  | phys_footprint delta, fresh                 | 30,066 B | 25,069 B |
  | phys_footprint delta, styled prompt written | 47,023 B | 41,944 B |
  | malloc zone bytes dirtied, fresh            | 12,698 B | 7,782 B  |
  | malloc blocks live after `terminal_new`     | 11,904 B | 6,688 B  |
  | malloc blocks live after the prompt         | 12,320 B | 7,104 B  |
  
  I ran `ghostty-bench +terminal-stream` on a 500 MB ascii corpus, main vs
  this branch interleaved, and there is no noticeable change.
  
  **AI usage:** Fable did validation of the work, I did the
  implementations, commit messages, and PR notes.
  ```
- [`ffe015e`](https://github.com/ghostty-org/ghostty/commit/ffe015ee55d1ab39cbf1525823ff18092433eab9) terminal: bitmap allocator marks free chunks with zero bits ([@mitchellh](https://github.com/mitchellh))
- [`c0a4f80`](https://github.com/ghostty-org/ghostty/commit/c0a4f80d80d75f7d3250d12554501fd7197e9bb0) terminal: hash map and ref counted set can initialize from zeroed memory ([@mitchellh](https://github.com/mitchellh))
- [`6112935`](https://github.com/ghostty-org/ghostty/commit/6112935a2fe9b7f5fd6c7595225c53406bee3bb1) terminal: hash map keeps its capacity and entry pointers in the struct ([@mitchellh](https://github.com/mitchellh))
- [`d2ff6d7`](https://github.com/ghostty-org/ghostty/commit/d2ff6d77a05d9e9b247684fad6bcb7979d0b2aca) terminal: pages initialize from zeroed memory and cache-line align their cells ([@mitchellh](https://github.com/mitchellh))
- [`07bccf7`](https://github.com/ghostty-org/ghostty/commit/07bccf7a311acdfa6afc77f2016160d49b1f1982) terminal: make all page data structures treat zero as empty to avoid eagerly paging in mmap pages ([#14137](https://github.com/ghostty-org/ghostty/issues/14137)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates all our page data structures so that the `0` value
  (literally `@memset(0)`) means empty. This way, when we initialize a new
  page via mmap (OS-guaranteed zeroed), we don't need to write to it, and
  don't trigger the kernel to physically map the memory.
  
  From Ghostty 1.3.1, our empty terminal physical memory usage goes from
  128 KB to 48 KB (#14130) to 16 KB (this PR). And even with an empty
  prompt written on my machine, it holds at 16KB, only increasing to two
  pages (32 KB) with 24 rows written.
  
  Here are some measurements.
  
  | Per terminal | Before (macOS) | After (macOS) | Before (Linux) | After
  (Linux) |
  
  |-------------------------------------------------------|----------------|---------------|----------------|---------------|
  | Page-list memory dirty, fresh | 48 KiB | 16 KiB | 24 KiB | 8 KiB |
  | Page-list memory dirty, 24 visible rows written | 64 KiB | 32 KiB | 36
  KiB | 20 KiB |
  
  Note macOS uses 16KB pages and Linux generally uses 4 KB pages.
  
  I ran `ghostty-bench +terminal-stream` main vs this branch and with
  every normal workload the results are within noise (sometimes faster
  sometimes slower).
  
  **AI usage:** It was used as a judge/validator. The actual changes were
  me, commit messages and PR messages all me.
  ```
- [`e347482`](https://github.com/ghostty-org/ghostty/commit/e347482fba62fd905fab2d4c8ec6a8c6f3664385) macOS: fix find previous action when search is focused ([@bo2themax](https://github.com/bo2themax))
- [`e8936b8`](https://github.com/ghostty-org/ghostty/commit/e8936b8969e78e07d9a8bf2b6a22ce59a38f5dfb) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Didn't respect the comment above before when reverting and testing hidden title 🫪
  ```
- [`3cca3e0`](https://github.com/ghostty-org/ghostty/commit/3cca3e0b956f07e008a4c66bb5f1a8ce266259a3) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([#14132](https://github.com/ghostty-org/ghostty/issues/14132)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Didn't respect the comment above. Sorry for the back&forth changes 🫪
  ```
- [`09ff85b`](https://github.com/ghostty-org/ghostty/commit/09ff85b2ac7b4204bbc48b5c7010adf0bdfb36d8) macOS: fix find previous action when search is focused ([#14131](https://github.com/ghostty-org/ghostty/issues/14131)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Typo found by @lrytz.
  ```
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

