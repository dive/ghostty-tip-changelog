> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 28, 2026 at 14:49 UTC.

## August 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33140987507)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

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

## August 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33124382421), [2](https://github.com/ghostty-org/ghostty/actions/runs/33121250277), [3](https://github.com/ghostty-org/ghostty/actions/runs/33114064367), [4](https://github.com/ghostty-org/ghostty/actions/runs/33096957391), [5](https://github.com/ghostty-org/ghostty/actions/runs/33036403965), [6](https://github.com/ghostty-org/ghostty/actions/runs/33034019716)  
Summary: 6 runs • 25 commits • 7 authors

### Changes

- [`4bb135e`](https://github.com/ghostty-org/ghostty/commit/4bb135e2de19b2ce8bddec77ba964ddaebbadc1e) i18n(ru): start updating Russian translation ([@derVedro](https://github.com/derVedro))
- [`1dd31f9`](https://github.com/ghostty-org/ghostty/commit/1dd31f9e9458ac1bf44860d55021f9d54e53c646) i18n(ru): work in progress on Russian translation ([@derVedro](https://github.com/derVedro))
- [`3f87b2e`](https://github.com/ghostty-org/ghostty/commit/3f87b2e5817429fd123af2c980cf6798017b75a1) i18n(ru): second part of Russian translation ([@derVedro](https://github.com/derVedro))
- [`32159b6`](https://github.com/ghostty-org/ghostty/commit/32159b6fe6714a8401d5ad21ce8487ac0266afd8) i18n(ru): small fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`0a396b4`](https://github.com/ghostty-org/ghostty/commit/0a396b43dccee62e61e2f17643262b800fd7699b) i18n(ru): context menu fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`ba35746`](https://github.com/ghostty-org/ghostty/commit/ba35746377788b8953a895559a91c6e1733c18da) i18n(ru): improve Russian translation ([@derVedro](https://github.com/derVedro))
- [`6244458`](https://github.com/ghostty-org/ghostty/commit/6244458a11f7c83c9c8774d2f5d27aba027c00fc) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`84dff76`](https://github.com/ghostty-org/ghostty/commit/84dff76b1383f0535657902b64cb614a34bd48e8) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`915977a`](https://github.com/ghostty-org/ghostty/commit/915977a484da9d9b93b3a30ac80ff068c5c3c6a8) i18n(ru): equalize splits ([@derVedro](https://github.com/derVedro))
- [`278b4e2`](https://github.com/ghostty-org/ghostty/commit/278b4e2fc7aab0c5073afdfe2570f27a5a4b9142) i18n(ru): refine Russian translation ([@derVedro](https://github.com/derVedro))
- [`2de1596`](https://github.com/ghostty-org/ghostty/commit/2de15961157343ff7dbeacc1281df97a3af6c624) macos: normalize action working directory paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #14048
  
  Directory URLs no longer export a trailing slash through PWD, which
  keeps zsh's %1~ prompt expansion from resolving to an empty string.
  
  A shared URL helper removes trailing separators while preserving the
  filesystem root and percent-decoding behavior. Tests cover normal,
  repeated, encoded, and root paths.
  ```
- [`07abbd1`](https://github.com/ghostty-org/ghostty/commit/07abbd1e7ee1f98d40cffacf537577e0bcb3522b) Update macos/Sources/Helpers/Extensions/URL+Extension.swift ([@mitchellh](https://github.com/mitchellh))
- [`1c3a4a8`](https://github.com/ghostty-org/ghostty/commit/1c3a4a8314669a97177e4b39cd5d6451f4c257f3) Update macos/Sources/Helpers/Extensions/URL+Extension.swift ([@mitchellh](https://github.com/mitchellh))
- [`fac595c`](https://github.com/ghostty-org/ghostty/commit/fac595c741aaec126d1cf0085dacfa63019a02c4) macos: normalize action working directory paths ([#14051](https://github.com/ghostty-org/ghostty/issues/14051)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #14048
  
  Directory URLs no longer export a trailing slash through PWD, which
  keeps zsh's %1~ prompt expansion from resolving to an empty string.
  
  A shared URL helper removes trailing separators while preserving the
  filesystem root and percent-decoding behavior. Tests cover normal,
  repeated, encoded, and root paths.
  ```
- [`5aeb693`](https://github.com/ghostty-org/ghostty/commit/5aeb693b7727b0dc6fcc9193bc1d2453af3bcb9a) i18n: Russian translation for 1.4 ([#13809](https://github.com/ghostty-org/ghostty/issues/13809)) ([@trag1c](https://github.com/trag1c))
- [`572fd58`](https://github.com/ghostty-org/ghostty/commit/572fd5837728da2363168f035743597767b5b237) macOS: use the same default BellFeatures as config ([@bo2themax](https://github.com/bo2themax))
- [`4f4589f`](https://github.com/ghostty-org/ghostty/commit/4f4589f31f2ca196fc88731dfcdc77e1cbde9852) macOS: use the same default BellFeatures as config ([#14049](https://github.com/ghostty-org/ghostty/issues/14049)) ([@mitchellh](https://github.com/mitchellh))
- [`28b5bf9`](https://github.com/ghostty-org/ghostty/commit/28b5bf905986f9e795466b7995640d80c44c16bc) font: update embedded Noto emoji fonts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14046
  
  Update Noto Color Emoji from v2.034 to v2.051 and Noto Emoji
  Regular from v1.002 to v3.005.
  
  The old assets predate Unicode 15.0 and decompose newer ZWJ sequences
  into separate glyphs. This causes sequences such as the Emoji 15.1
  head-shaking faces to overlap neighboring terminal cells. The new
  assets provide the missing sequence glyphs through Unicode 17.0.
  
  New supported glyphs too:
  
  | Codepoint | Glyph | Name |
  |-----------|-------|------|
  | U+1F6D8 | 🛘 | LANDSLIDE |
  | U+1F6DC | 🛜 | WIRELESS |
  | U+1FA75 | 🩵 | LIGHT BLUE HEART |
  | U+1FA76 | 🩶 | GREY HEART |
  | U+1FA77 | 🩷 | PINK HEART |
  | U+1FA87 | 🪇 | MARACAS |
  | U+1FA88 | 🪈 | FLUTE |
  | U+1FA89 | 🪉 | HARP |
  | U+1FA8A | 🪊 | TROMBONE |
  | U+1FA8E | 🪎 | TREASURE CHEST |
  | U+1FA8F | 🪏 | SHOVEL |
  | U+1FAAD | 🪭 | FOLDING HAND FAN |
  | U+1FAAE | 🪮 | HAIR PICK |
  | U+1FAAF | 🪯 | KHANDA |
  | U+1FABB | 🪻 | HYACINTH |
  | U+1FABC | 🪼 | JELLYFISH |
  | U+1FABD | 🪽 | WING |
  | U+1FABE | 🪾 | LEAFLESS TREE |
  | U+1FABF | 🪿 | GOOSE |
  | U+1FAC6 | 🫆 | FINGERPRINT |
  | U+1FAC8 | 🫈 | HAIRY CREATURE |
  | U+1FACD | 🫍 | ORCA |
  | U+1FACE | 🫎 | MOOSE |
  | U+1FACF | 🫏 | DONKEY |
  | U+1FADA | 🫚 | GINGER ROOT |
  | U+1FADB | 🫛 | PEA POD |
  | U+1FADC | 🫜 | ROOT VEGETABLE |
  | U+1FADF | 🫟 | SPLATTER |
  | U+1FAE8 | 🫨 | SHAKING FACE |
  | U+1FAE9 | 🫩 | FACE WITH BAGS UNDER EYES |
  | U+1FAEA | 🫪 | DISTORTED FACE |
  | U+1FAEF | 🫯 | FIGHT CLOUD |
  | U+1FAF7 | 🫷 | LEFTWARDS PUSHING HAND |
  | U+1FAF8 | 🫸 | RIGHTWARDS PUSHING HAND |
  ```
- [`890aa63`](https://github.com/ghostty-org/ghostty/commit/890aa63dbbd586c6687a60b3736109203649d8dc) font: update embedded Noto emoji fonts ([#14047](https://github.com/ghostty-org/ghostty/issues/14047)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14046
  
  Update Noto Color Emoji from v2.034 to v2.051 and Noto Emoji Regular
  from v1.002 to v3.005.
  
  The old assets predate Unicode 15.0 and decompose newer ZWJ sequences
  into separate glyphs. This causes sequences such as the Emoji 15.1
  head-shaking faces to overlap neighboring terminal cells. The new assets
  provide the missing sequence glyphs through Unicode 17.0.
  
  New supported glyphs too:
  
  | Codepoint | Glyph | Name |
  |-----------|-------|------|
  | U+1F6D8 | 🛘 | LANDSLIDE |
  | U+1F6DC | 🛜 | WIRELESS |
  | U+1FA75 | 🩵 | LIGHT BLUE HEART |
  | U+1FA76 | 🩶 | GREY HEART |
  | U+1FA77 | 🩷 | PINK HEART |
  | U+1FA87 | 🪇 | MARACAS |
  | U+1FA88 | 🪈 | FLUTE |
  | U+1FA89 | 🪉 | HARP |
  | U+1FA8A | 🪊 | TROMBONE |
  | U+1FA8E | 🪎 | TREASURE CHEST |
  | U+1FA8F | 🪏 | SHOVEL |
  | U+1FAAD | 🪭 | FOLDING HAND FAN |
  | U+1FAAE | 🪮 | HAIR PICK |
  | U+1FAAF | 🪯 | KHANDA |
  | U+1FABB | 🪻 | HYACINTH |
  | U+1FABC | 🪼 | JELLYFISH |
  | U+1FABD | 🪽 | WING |
  | U+1FABE | 🪾 | LEAFLESS TREE |
  | U+1FABF | 🪿 | GOOSE |
  | U+1FAC6 | 🫆 | FINGERPRINT |
  | U+1FAC8 | 🫈 | HAIRY CREATURE |
  | U+1FACD | 🫍 | ORCA |
  | U+1FACE | 🫎 | MOOSE |
  | U+1FACF | 🫏 | DONKEY |
  | U+1FADA | 🫚 | GINGER ROOT |
  | U+1FADB | 🫛 | PEA POD |
  | U+1FADC | 🫜 | ROOT VEGETABLE |
  | U+1FADF | 🫟 | SPLATTER |
  | U+1FAE8 | 🫨 | SHAKING FACE |
  | U+1FAE9 | 🫩 | FACE WITH BAGS UNDER EYES |
  | U+1FAEA | 🫪 | DISTORTED FACE |
  | U+1FAEF | 🫯 | FIGHT CLOUD |
  | U+1FAF7 | 🫷 | LEFTWARDS PUSHING HAND |
  | U+1FAF8 | 🫸 | RIGHTWARDS PUSHING HAND |
  ```
- [`6229d4e`](https://github.com/ghostty-org/ghostty/commit/6229d4eb62f9e2483b3ea00c11fcde70590d2d84) macOS: fix AppleScript send key for non-control keys ([@bo2themax](https://github.com/bo2themax))
- [`e9ad4b1`](https://github.com/ghostty-org/ghostty/commit/e9ad4b1d631ec91c8cad401700fee1754612ef33) macOS: fix non control keys are not working for AppleScript ([#13205](https://github.com/ghostty-org/ghostty/issues/13205)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `send key` only works for control keys like `enter` currently; this adds
  (fixes) the support for other keys listed as available. Found by
  @paaloeye in #13180
  
  The core of this fix is relying on `UCKeyTranslate` to get the
  corresponding character and code point from a key code using
  `KeyboardLayout.character(for:modifiers:)`.
  
  ScriptKeyEventCommand now respects `macos-option-as-alt`, and attach
  `text`, `unshifted_codepoint` and `consumed_mods` under the same
  condition as a manual input events like in `performKeyEquivalent` and
  `localEventKeyDown`.
  
  ## AI Disclosure
  
  Claude did the heavy lifting, I reviewed and rephrased some of the
  comments it generated. And ofc reviewed and tested myself.
  ```
- [`ee8095d`](https://github.com/ghostty-org/ghostty/commit/ee8095d37d9813669688cf2f666756e607b84713) terminal/snapshot: use stack fallback for record scratch ([@jparise](https://github.com/jparise))
  ```text
  Use a bounded 512-byte stack fallback for complete-snapshot record
  scratch. Small records avoid heap growth while larger records continue
  through the heap allocator.
  ```
- [`f2d5758`](https://github.com/ghostty-org/ghostty/commit/f2d5758f6305867dc36b36293c6165d8152b853e) terminal/snapshot: use stack fallback for record scratch ([#14018](https://github.com/ghostty-org/ghostty/issues/14018)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use a bounded 512-byte stack fallback for complete-snapshot record
  scratch. Small records avoid heap growth while larger records continue
  through the heap allocator.
  
  This usually means 2 fewer allocations per encode, resulting in a small
  performance improvement in a local benchmark:
  
  | Workload | `main` median | Branch median | Change |
  |---|---:|---:|---:|
  | Empty, 50k encodes | 135.06 ms | 130.76 ms | **3.2% faster** |
  | 1 MiB ASCII, 500 encodes | 280.75 ms | 281.25 ms | **0.2% slower**,
  within noise |
  | 1 MiB styled, 200 encodes | 1,023.02 ms | 996.32 ms | **2.6% faster**
  |
  ```
- [`522ebdd`](https://github.com/ghostty-org/ghostty/commit/522ebdd0a313ef366d3567694e3588b780fae8ee) build(deps): bump hustcer/milestone-action from 3.1 to 3.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [hustcer/milestone-action](https://github.com/hustcer/milestone-action) from 3.1 to 3.2.
  - [Release notes](https://github.com/hustcer/milestone-action/releases)
  - [Changelog](https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/hustcer/milestone-action/compare/ebed8d5daafd855a600d7e665c1b130f06d24130...2f38355153344ccaaa44b5b5fcff9f604dff1b45)
  
  ---
  updated-dependencies:
  - dependency-name: hustcer/milestone-action
    dependency-version: '3.2'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`f349d10`](https://github.com/ghostty-org/ghostty/commit/f349d108431007dac0d908af33301e3cc460b2f3) build(deps): bump hustcer/milestone-action from 3.1 to 3.2 ([#14040](https://github.com/ghostty-org/ghostty/issues/14040)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [hustcer/milestone-action](https://github.com/hustcer/milestone-action)
  from 3.1 to 3.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/releases">hustcer/milestone-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.2</h2>
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
  <p>This release introduces changes that may impact some users. If the
  action fails due to insufficient permissions, please add the
  <code>issues: write</code> and <code>pull-requests: write</code>
  permissions to your workflow. Additionally, the API for binding
  milestones has been modified. Due to these changes, the major version
  has been incremented to 3.</p>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Try to fix GitHub Projects (classic) deprecation warning by using
  REST API instead of GraphQL (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/157">#157</a>)</li>
  <li>Fix &quot;Resource not accessible by integration&quot; error for
  issue milestone binding by adding <code>issues: write</code>
  permission</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/2f38355153344ccaaa44b5b5fcff9f604dff1b45"><code>2f38355</code></a>
  Bump to v3.2</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/90d61222172fcab928f4097d7ac0f9b777f8c6a6"><code>90d6122</code></a>
  deps: Upgrade Nu to 0.115.1</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/e587063f374a27424be13284709902ef21d0e7e2"><code>e587063</code></a>
  fix: Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/cc2b756fd4aa0c6296b7268f41108dc88bfb8228"><code>cc2b756</code></a>
  fix: Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/f8cedae0c15efb735341ecea49835c86190dee13"><code>f8cedae</code></a>
  fix: Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/b57a2e26d7ae416cd8f283c8ddcf0022639b0a99"><code>b57a2e2</code></a>
  fix: Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/3ba8f40c9539a0d3b5ac92732bd3a26f3a9e80df"><code>3ba8f40</code></a>
  fix: Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/1e6a3fcc554f6c07ada4feabb0b1935aa60243d3"><code>1e6a3fc</code></a>
  deps: Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/913159549289b377b4d0c9c830101da8d4c82387"><code>9131595</code></a>
  deps: Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>See full diff in <a
  href="https://github.com/hustcer/milestone-action/compare/ebed8d5daafd855a600d7e665c1b130f06d24130...2f38355153344ccaaa44b5b5fcff9f604dff1b45">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=hustcer/milestone-action&package-manager=github_actions&previous-version=3.1&new-version=3.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## August 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33015847463), [2](https://github.com/ghostty-org/ghostty/actions/runs/33003643945), [3](https://github.com/ghostty-org/ghostty/actions/runs/32980266736), [4](https://github.com/ghostty-org/ghostty/actions/runs/32953632696), [5](https://github.com/ghostty-org/ghostty/actions/runs/32932472332), [6](https://github.com/ghostty-org/ghostty/actions/runs/32929311994)  
Summary: 6 runs • 15 commits • 4 authors

### Changes

- [`b6ac6e1`](https://github.com/ghostty-org/ghostty/commit/b6ac6e1d479f29fb8194f86ec24b72901aa94c21) Revert "macOS: use same ResetZoomAccessoryView ([#14028](https://github.com/ghostty-org/ghostty/issues/14028))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 15ff186f65ca0bdbd1fa397ab03908d59de16463, reversing
  changes made to 1abd53ee537a93bb33107a415fe4f4131bcf0f5b.
  ```
- [`0a9f47c`](https://github.com/ghostty-org/ghostty/commit/0a9f47cae0bc3cb653ea52fbd4e1d632b79dd91a) macOS: update note about tab accessory view ([@bo2themax](https://github.com/bo2themax))
- [`b69f612`](https://github.com/ghostty-org/ghostty/commit/b69f612672f4e31e20dec2ee2684d295aec149f1) macOS: update note about tab accessory view ([#14038](https://github.com/ghostty-org/ghostty/issues/14038)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reverts: #14028
  ```
- [`6688aa0`](https://github.com/ghostty-org/ghostty/commit/6688aa072f87dcb169fa1a49dcf5eadc9ed87956) renderer: park DisplayLink while idle ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14033
  
  Pause the CVDisplayLink when there isn't any real work to do.
  
  Start the link after updateFrame rebuilds cells, keep it running while
  cell changes or animations remain pending, and resync it from the
  no-redraw path to sleep it again.
  
  I also did some benchmark to measure the cost of starting/stopping the
  display link since this includes a lot more of that and I found that
  a continuously running link used 29 to 35 us of CPU per callback, while
  starting and stopping it for every frame used 103 to 121 us. So, in some
  pathological case this can be worse, but its still microseconds, and in
  the normal case this helps Ghostty sleep a lot more.
  ```
- [`d9840f3`](https://github.com/ghostty-org/ghostty/commit/d9840f3c8fc230c7768ae760c412974e9fc923bb) renderer: park DisplayLink while idle ([#14035](https://github.com/ghostty-org/ghostty/issues/14035)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14033
  
  Pause the CVDisplayLink when there isn't any real work to do.
  
  Start the link after updateFrame rebuilds cells, keep it running while
  cell changes or animations remain pending, and resync it from the
  no-redraw path to sleep it again.
  
  I also did some benchmark to measure the cost of starting/stopping the
  display link since this includes a lot more of that and I found that a
  continuously running link used 29 to 35 us of CPU per callback, while
  starting and stopping it for every frame used 103 to 121 us. So, in some
  pathological case this can be worse, but its still microseconds, and in
  the normal case this helps Ghostty sleep a lot more.
  ```
- [`851751a`](https://github.com/ghostty-org/ghostty/commit/851751a1167a05d83f08c010a7b1e92f435f783f) macOS: clean up deprecated toolbar button ([@bo2themax](https://github.com/bo2themax))
- [`7a15898`](https://github.com/ghostty-org/ghostty/commit/7a15898bc813558a25c4beffd7391dad14cbb20c) macOS: use same ResetZoomAccessoryView ([@bo2themax](https://github.com/bo2themax))
- [`1abd53e`](https://github.com/ghostty-org/ghostty/commit/1abd53ee537a93bb33107a415fe4f4131bcf0f5b) macOS: clean up deprecated toolbar button ([#14027](https://github.com/ghostty-org/ghostty/issues/14027)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This button is a leftover from cf6017e777cda0e0c131b616f408c9a81644b5d7,
  we're now using tab's and titlebar's accessory view to display unzoom
  buttons, no need to keep them.
  ```
- [`15ff186`](https://github.com/ghostty-org/ghostty/commit/15ff186f65ca0bdbd1fa397ab03908d59de16463) macOS: use same ResetZoomAccessoryView ([#14028](https://github.com/ghostty-org/ghostty/issues/14028)) ([@mitchellh](https://github.com/mitchellh))
- [`73e53ce`](https://github.com/ghostty-org/ghostty/commit/73e53ceeac4d81b59d228db32de933d8114d42cd) i18n: update fr_FR translations ([@flou](https://github.com/flou))
- [`5f5b988`](https://github.com/ghostty-org/ghostty/commit/5f5b988c5236facfe8d2439203d9ee9d5b636cf8) i18n: update fr_FR translations ([#13971](https://github.com/ghostty-org/ghostty/issues/13971)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update missing french translations for Ghostty 1.4
  (https://github.com/ghostty-org/ghostty/issues/13766)
  ```
- [`40a40f8`](https://github.com/ghostty-org/ghostty/commit/40a40f848dfca8c5edbc0098dd828aec03ae8e64) terminal: ignore UTF-8-decoded C1 controls in the ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Drop UTF-8 decoded C1 controls entirely. This matches xterm's default
  behavior which is our standard policy (but note it diverges from libvte
  which executes them). There isn't really any standard I could find
  around this.
  
  The ground state UTF-8 fast paths (both the scalar decoder and the
  batched SIMD path) previously treated decoded codepoints C1 control
  codepoints as normal UTF-8 text and routed them to print.
  ```
- [`88f57ee`](https://github.com/ghostty-org/ghostty/commit/88f57ee66eeaad4da77b414b245f7b6693348985) terminal: ignore UTF-8-decoded C1 controls in the ground state ([#14023](https://github.com/ghostty-org/ghostty/issues/14023)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Drop UTF-8 decoded C1 controls entirely. This matches xterm's default
  behavior which is our standard policy (but note it diverges from libvte
  which executes them). There isn't really any standard I could find
  around this.
  
  The ground state UTF-8 fast paths (both the scalar decoder and the
  batched SIMD path) previously treated decoded codepoints C1 control
  codepoints as normal UTF-8 text and routed them to print.
  ```
- [`0f35043`](https://github.com/ghostty-org/ghostty/commit/0f35043c9ac588811f22c732ac5392850f22381e) terminal: execute C0 controls 0x10-0x1F in the ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14021
  
  The ground state UTF-8 fast paths only classified 0x00-0x0F plus 0x1B (escape)
  as C0 controls. The remaining C0 bytes (0x10-0x1A, 0x1C-0x1F) were decoded
  as ordinary codepoints and routed to print as if they were text.
  
  This resulted in incorrect grids but also very weird font fallback, e.g.
  U+0014 would find CJK fonts.
  
  This commit fixes this by routing every ground state C0 byte except ESC to
  execute as it should be.
  ```
- [`6dcf68f`](https://github.com/ghostty-org/ghostty/commit/6dcf68fc0b12e8caebbfc43770d66edac124b4f8) terminal: execute C0 controls 0x10-0x1F in the ground state ([#14022](https://github.com/ghostty-org/ghostty/issues/14022)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14021
  
  The ground state UTF-8 fast paths only classified 0x00-0x0F plus 0x1B
  (escape) as C0 controls. The remaining C0 bytes (0x10-0x1A, 0x1C-0x1F)
  were decoded as ordinary codepoints and routed to print as if they were
  text.
  
  This resulted in incorrect grids but also very weird font fallback, e.g.
  U+0014 would find CJK fonts.
  
  This commit fixes this by routing every ground state C0 byte except ESC
  to execute as it should be.
  ```

## August 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32885561859), [2](https://github.com/ghostty-org/ghostty/actions/runs/32868574536), [3](https://github.com/ghostty-org/ghostty/actions/runs/32863067913), [4](https://github.com/ghostty-org/ghostty/actions/runs/32861518453), [5](https://github.com/ghostty-org/ghostty/actions/runs/32852280188), [6](https://github.com/ghostty-org/ghostty/actions/runs/32811372816)  
Summary: 6 runs • 25 commits • 5 authors

### Changes

- [`c4e1697`](https://github.com/ghostty-org/ghostty/commit/c4e16970a803b170e352432424f44192cb59f3ac) renderer: release GPU resources for hidden surfaces (macOS) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ref #12034
  
  This commit releases many GPU resources when a surface becomes invisible and
  rebuilds it on the next draw. I don't say "all" because there are still
  some things we can improve on (Kitty images).
  
  We previously held onto all GPU resources for the lifetime of the surface
  regardless of its visibility state. This is 3x (for triple-buffering):
  screen render targets, uniform/cell/custom shader buffers, font textures,
  and more.
  
  Measured on macOS (Metal):
  
  | Measurement (1 visible + 20 hidden tabs)    | Before    | After   |
  |---------------------------------------------|-----------|---------|
  | Tracked GPU allocations (steady state)      | 384.6 MiB | 18.3 MiB |
  | `MTLDevice.currentAllocatedSize`            | 393.3 MiB | 19.7 MiB |
  | `footprint` IOSurface (dirty)               | 309 MB    | 15 MB   |
  | Swap chain rebuild on unhide (42 switches)  | n/a       | avg 0.43 ms, max 0.55 ms |
  
  As you can see, importantly, swap chain rebuild is fast: 0.43ms average.
  That means that the rebuild is imperceptible and happens well within
  a frame draw time.
  
  This is macOS only, but most of the work was in the generic renderer.
  GTK only needs to call `releaseGpuResources` when it becomes invisible
  to get the same benefits. I didn't have my VM handy to test this yet so
  I didn't include it.
  ```
- [`683d8db`](https://github.com/ghostty-org/ghostty/commit/683d8db643b95cf229bfb5fe9fab9ae677920343) renderer: release GPU resources for hidden surfaces (macOS) ([#14017](https://github.com/ghostty-org/ghostty/issues/14017)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ref #12034
  
  This commit releases many GPU resources when a surface becomes invisible
  and rebuilds it on the next draw. I don't say "all" because there are
  still some things we can improve on (Kitty images).
  
  We previously held onto all GPU resources for the lifetime of the
  surface regardless of its visibility state. This is 3x (for
  triple-buffering): screen render targets, uniform/cell/custom shader
  buffers, font textures, and more.
  
  Measured on macOS (Metal):
  
  | Measurement (1 visible + 20 hidden tabs)    | Before    | After   |
  |---------------------------------------------|-----------|---------|
  | Tracked GPU allocations (steady state)      | 384.6 MiB | 18.3 MiB |
  | `MTLDevice.currentAllocatedSize`            | 393.3 MiB | 19.7 MiB |
  | `footprint` IOSurface (dirty)               | 309 MB    | 15 MB   |
  | Swap chain rebuild on unhide (42 tab switches) | n/a | avg 0.43 ms,
  max 0.55 ms |
  
  As you can see, importantly, swap chain rebuild is fast: 0.43ms average.
  That means that the rebuild is imperceptible and happens well within a
  frame draw time.
  
  This is macOS only, but most of the work was in the generic renderer.
  GTK only needs to call `releaseGpuResources` when it becomes invisible
  to get the same benefits. I didn't have my VM handy to test this yet so
  I didn't include it.
  ```
- [`48a9e29`](https://github.com/ghostty-org/ghostty/commit/48a9e29f79e918d4f73a13c1ce27646d029811e4) nix: update nixpkgs-unstable ([@jcollie](https://github.com/jcollie))
  ```text
  Update nixpkgs-unstable to pick up fontconfig 2.18. Currently we are linking against 2.17 and you get errors
  like this on standard error when using config files meant for fontconfig 2.18:
  
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 20: invalid constant used :
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 23: invalid constant used : monospace
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 42: invalid attribute 'xsi:nil'
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 43: invalid constant used :
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 46: invalid constant used : sans-serif
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 68: invalid attribute 'xsi:nil'
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 69: invalid constant used :
  
  This also removes an override for libfyaml on Darwin that was merged upstream into nixpkgs.
  ```
- [`d9857ea`](https://github.com/ghostty-org/ghostty/commit/d9857eabae06baebc9685121bfe78c49090643af) cli: update list-themes preview sample to valid Zig 0.16 syntax ([@tacheraSasi](https://github.com/tacheraSasi))
- [`bc2f7d7`](https://github.com/ghostty-org/ghostty/commit/bc2f7d7d2fa589a3abf9e4f6696e0a7f7c204e4f) terminal: update Kitty clipboard base64 handling to spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty clipboard protocol now specifies base64 handling:
  All OSC 5522 payloads and the base64 metadata values (mime, name, pw)
  use strict RFC 4648 with the standard alphabet. Characters outside
  the alphabet (including whitespace) and incorrect padding must be
  rejected, never silently skipped.
  
  For wdata payloads for one MIME type, the base64 stream can be split
  at arbitrary packet boundaries and only the concatenation must be
  correctly padded.
  
  Simdutf has a strict mode for base64 so we got this for free.
  Benchmarks to be safe:
  
  | Decoder                       | Time  | Throughput |
  |-------------------------------|-------|------------|
  | permissive (previous)         | 99ms  | 10.8 GB/s  |
  | strict                        | 97ms  | 11.1 GB/s  |
  | strict, streaming 4KiB chunks | 102ms | 10.5 GB/s  |
  | strict w/ separate scan pass  | 143ms | 7.5 GB/s   |
  | std.base64 scalar             | 234ms | 4.6 GB/s   |
  
  Spec changes upstream:
  https://github.com/kovidgoyal/kitty/commit/479872838f7536ab87b8133471eb49d06804951b
  https://sw.kovidgoyal.net/kitty/clipboard/#encoding-of-payloads
  ```
- [`82ccf12`](https://github.com/ghostty-org/ghostty/commit/82ccf12ca22131d2c845387806b6a924f86abe5f) nix: update nixpkgs-unstable ([#13678](https://github.com/ghostty-org/ghostty/issues/13678)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update nixpkgs-unstable to pick up fontconfig 2.18. Currently we are
  linking against 2.17 and you get errors like this on standard error when
  using config files meant for fontconfig 2.18:
  
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 20:
  invalid constant used :
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 23:
  invalid constant used : monospace
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 42:
  invalid attribute 'xsi:nil'
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 43:
  invalid constant used :
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 46:
  invalid constant used : sans-serif
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 68:
  invalid attribute 'xsi:nil'
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 69:
  invalid constant used :
  ```
- [`557253d`](https://github.com/ghostty-org/ghostty/commit/557253d8f64f8b08da33f5a7f3cb33a75960b09d) terminal: update Kitty clipboard base64 handling to spec ([#14015](https://github.com/ghostty-org/ghostty/issues/14015)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty clipboard protocol now specifies base64 handling: All OSC 5522
  payloads and the base64 metadata values (mime, name, pw) use strict RFC
  4648 with the standard alphabet. Characters outside the alphabet
  (including whitespace) and incorrect padding must be rejected, never
  silently skipped.
  
  For wdata payloads for one MIME type, the base64 stream can be split at
  arbitrary packet boundaries and only the concatenation must be correctly
  padded.
  
  Simdutf has a strict mode for base64 so we got this for free. Benchmarks
  to be safe:
  
  | Decoder                       | Time  | Throughput |
  |-------------------------------|-------|------------|
  | permissive (previous)         | 99ms  | 10.8 GB/s  |
  | strict                        | 97ms  | 11.1 GB/s  |
  | strict, streaming 4KiB chunks | 102ms | 10.5 GB/s  |
  | strict w/ separate scan pass  | 143ms | 7.5 GB/s   |
  | std.base64 scalar             | 234ms | 4.6 GB/s   |
  
  Spec changes upstream:
  
  https://github.com/kovidgoyal/kitty/commit/479872838f7536ab87b8133471eb49d06804951b
  https://sw.kovidgoyal.net/kitty/clipboard/#encoding-of-payloads
  ```
- [`4e817e7`](https://github.com/ghostty-org/ghostty/commit/4e817e79a1d7e3fe7393297e3c8f1269abb6523a) terminal: treat high bytes in DCS strings as payload data ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #11216
  
  The dcs_passthrough state only forwarded bytes 0x00-0x7E to the DCS
  handler. Bytes 0x80-0x9F hit the "anywhere" C1 transitions and exited
  the string, while 0xA0-0xFF fell through to the default transition and
  were silently dropped. **This breaks any DCS payload carrying UTF-8. **
  
  A continuation byte in the C1 range terminates or corrupts the string:
  "Ü" is 0xC3 0x9C, so the 0xC3 is dropped and the 0x9C acts as 8-bit ST,
  ending the DCS mid-character.
  
  Also, a payload byte such as 0x9B (second byte of "Û") transitions to
  csi_entry, so the remainder of the payload executes as a live control sequence.
  This is a prerequisite for tmux control mode (#1935), whose %output
  notifications carry raw UTF-8 pane content.
  
  Fix this in the parse table only: override 0x80-0xFF in
  dcs_passthrough to put and in dcs_ignore to ignore, exactly how
  osc_string already claims 0x20-0xFF (including 0x9C) as data. This
  deviates from the vt100.net state machine
  (https://vt100.net/emu/dec_ansi_parser) deliberately and includes
  0x9C: a raw 0x9C is indistinguishable from a UTF-8 continuation byte,
  and we don't honor 8-bit C1 controls in the ground state either.
  ```
- [`b260da2`](https://github.com/ghostty-org/ghostty/commit/b260da24f8f10bebc92539eef640dbfd26c5a854) cli: update list-themes preview sample to valid Zig 0.16 syntax ([#14012](https://github.com/ghostty-org/ghostty/issues/14012)) ([@jcollie](https://github.com/jcollie))
  ````text
  The demo code shown in the `+list-themes` theme preview was stale from
  before the Zig 0.16 migration (context: #12228). It referenced
  `std.Io.getStdOut().writer()`, which never existed in any Zig release,
  and `pub fn main() !void`. This rewrites the rendered sample to valid
  Zig 0.16 idioms:
  
  ```zig
  const std = @import("std");
  
  pub fn main(init: std.process.Init) !void {
      var buf: [1024]u8 = undefined;
      var stdout = std.Io.File.stdout().writer(init.io, &buf);
      const w = &stdout.interface;
  
      var i: usize = 1;
      while (i <= 16) : (i += 1) {
          if (i % 15 == 0) {
              try w.writeAll("ZiggZagg\n");
          } else if (i % 3 == 0) {
              try w.writeAll("Zigg\n");
          } else if (i % 5 == 0) {
              try w.writeAll("Zagg\n");
          } else {
              try w.print("{d}\n", .{i});
          }
      }
      try w.flush();
  }
  ```
  
  The gutter line numbers, row offsets, and child window height were
  renumbered to match, and the zig version shown in the demo prompt line
  was updated from v0.13.0 to v0.16.0.
  ````
- [`9c3ec93`](https://github.com/ghostty-org/ghostty/commit/9c3ec931d64561a8407dde7ac984ce156ae91539) terminal: treat high bytes in DCS strings as payload data ([#14016](https://github.com/ghostty-org/ghostty/issues/14016)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #11216
  
  The dcs_passthrough state only forwarded bytes 0x00-0x7E to the DCS
  handler. Bytes 0x80-0x9F hit the "anywhere" C1 transitions and exited
  the string, while 0xA0-0xFF fell through to the default transition and
  were silently dropped. **This breaks any DCS payload carrying UTF-8. **
  
  A continuation byte in the C1 range terminates or corrupts the string:
  "Ü" is 0xC3 0x9C, so the 0xC3 is dropped and the 0x9C acts as 8-bit ST,
  ending the DCS mid-character.
  
  Also, a payload byte such as 0x9B (second byte of "Û") transitions to
  csi_entry, so the remainder of the payload executes as a live control
  sequence. This is a prerequisite for tmux control mode (#1935), whose
  %output notifications carry raw UTF-8 pane content.
  
  Fix this in the parse table only: override 0x80-0xFF in dcs_passthrough
  to put and in dcs_ignore to ignore, exactly how osc_string already
  claims 0x20-0xFF (including 0x9C) as data. This deviates from the
  vt100.net state machine
  (https://vt100.net/emu/dec_ansi_parser) deliberately and includes 0x9C:
  a raw 0x9C is indistinguishable from a UTF-8 continuation byte, and we
  don't honor 8-bit C1 controls in the ground state either.
  ```
- [`bb00a5c`](https://github.com/ghostty-org/ghostty/commit/bb00a5c988245a10f7d96dfdadcbfbd03f977dc4) Update VOUCHED list ([#14013](https://github.com/ghostty-org/ghostty/issues/14013)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14012#issuecomment-5412366760)
  from @jcollie.
  
  Vouch: @tacheraSasi
  ```
- [`8c5bc3d`](https://github.com/ghostty-org/ghostty/commit/8c5bc3d29f17ebc42b81d4b61ec1fe86886332d4) terminal: optimize OSC string reading with SIMD ([@mitchellh](https://github.com/mitchellh))
  ```text
  We now have large OSCs (e.g. Kitty clipboard protocol) on the order
  of megabytes. OSC was still byte-at-a-time. This adds a vector-optimized
  plus bulk storing path to OSC, similar to APC.
  
  Throughput measured with the terminal-stream benchmark:
  
  | Corpus                   | Before | After | Speedup |
  |--------------------------|--------|-------|---------|
  | OSC 52, 1MiB payloads    | 446ms  | 14ms  | 32x     |
  | OSC 5522, 1MiB payloads  | 446ms  | 15ms  | 30x     |
  | OSC 5522, 64KiB payloads | 448ms  | 14ms  | 32x     |
  | OSC 5522, 4KiB payloads  | 448ms  | 16ms  | 29x     |
  | Tiny titles (~24B each)  | 450ms  | 73ms  | 6.2x    |
  | Mixed OSCs (16MiB)       | 595ms  | 531ms | 1.13x   |
  
  Used Fable to help validate this with a barrage of differential tests.
  The actual implementation was AI-written but was guided to basically
  mimic the APC path and then I hand verified everything too.
  ```
- [`8144ef4`](https://github.com/ghostty-org/ghostty/commit/8144ef4e73e70a4e9942fceb319819005f07fd37) terminal: optimize OSC string reading with SIMD ([#14011](https://github.com/ghostty-org/ghostty/issues/14011)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We now have large OSCs (e.g. Kitty clipboard protocol) on the order of
  megabytes. OSC was still byte-at-a-time. This adds a vector-optimized
  plus bulk storing path to OSC, similar to APC.
  
  Throughput measured with the terminal-stream benchmark:
  
  | Corpus                   | Before | After | Speedup |
  |--------------------------|--------|-------|---------|
  | OSC 52, 1MiB payloads    | 446ms  | 14ms  | 32x     |
  | OSC 5522, 1MiB payloads  | 446ms  | 15ms  | 30x     |
  | OSC 5522, 64KiB payloads | 448ms  | 14ms  | 32x     |
  | OSC 5522, 4KiB payloads  | 448ms  | 16ms  | 29x     |
  | Tiny titles (~24B each)  | 450ms  | 73ms  | 6.2x    |
  | Mixed OSCs (16MiB)       | 595ms  | 531ms | 1.13x   |
  
  Used Fable to help validate this with a barrage of differential tests.
  The actual implementation was AI-written but was guided to basically
  mimic the APC path and then I hand verified everything too.
  ```
- [`a2212a5`](https://github.com/ghostty-org/ghostty/commit/a2212a5b1229d580ceb25d67cf3353b679eddf3b) macos: replace legacy aspectRatio with scaledToFit in clipboard preview ([@bo2themax](https://github.com/bo2themax))
- [`d7f5ba3`](https://github.com/ghostty-org/ghostty/commit/d7f5ba3b4f4745660dbb5ada6fde6f841aba07af) macOS: add test cases for ScriptKeyEventCommand ([@bo2themax](https://github.com/bo2themax))
- [`f1b9efe`](https://github.com/ghostty-org/ghostty/commit/f1b9efed802650ffaccc0b53da026314909bae53) macOS: update default behaviour of KeyboardLayout.character(for:modifiers:) ([@bo2themax](https://github.com/bo2themax))
- [`719def7`](https://github.com/ghostty-org/ghostty/commit/719def70f3df246695881f571f0edde28b95f0a3) macOS: update default behaviour of KeyboardLayout.character(for:modifiers:) ([#14009](https://github.com/ghostty-org/ghostty/issues/14009)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up for #13888, and prepare for #13205.
  
  The comments are copied from the history commit.
  
  ## AI Disclosure
  
  The tests are updated by Claude, I cherrypicked them.
  ```
- [`1c73935`](https://github.com/ghostty-org/ghostty/commit/1c739350c31a8340fdbf56cd7e703f860f69bed4) macOS: add test cases for ScriptKeyEventCommand ([#14008](https://github.com/ghostty-org/ghostty/issues/14008)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Partial changes for #13205, known issues are marked as warnings.
  
  ### AI Disclosure
  
  Claude generated these tests from linked pr, I cherrypicked and reviewed
  myself.
  ```
- [`6d2b436`](https://github.com/ghostty-org/ghostty/commit/6d2b43652950b417431145147dd445d32e04119c) macos: replace legacy aspectRatio with scaledToFit in clipboard preview ([#14006](https://github.com/ghostty-org/ghostty/issues/14006)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the swiftlint legacy_swiftui_aspect_ratio violation.
  
  ### AI Disclosure
  
  By Claude, but it's really simple.
  ```
- [`b31fbc8`](https://github.com/ghostty-org/ghostty/commit/b31fbc846474bf6082f1a3f13290e17f2d984a25) terminal: fully reset row metadata when recycling row storage ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13940
  
  Various operations like scroll, line insert, erase, etc. operations
  would clear cells but remain row metadata such as wrap flags and
  semantic prompt state.
  
  When we had fast paths in `grow` and other places like resize
  we would adopt that without knowing it because we didn't properly clear.
  
  Fix this by properly clearing row metadata too at the points where we
  erase a row that might be reused.
  
  Benchmarked with terminal-stream workloads for each affected path.
  The added cost is 2-4 instructions per recycled row next to the existing
  full-row cell clear. There was no measurable wall-clock change on any
  workload.
  
  AI helped run the benchmarks for me and analyze for missing places (it found
  some!) but otherwise this was hand-designed.
  ```
- [`046a45a`](https://github.com/ghostty-org/ghostty/commit/046a45a5fcacf427573b81de6e03de37fe01bb16) terminal: fully reset row metadata when recycling row storage ([#14010](https://github.com/ghostty-org/ghostty/issues/14010)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13940
  
  Various operations like scroll, line insert, erase, etc. operations
  would clear cells but remain row metadata such as wrap flags and
  semantic prompt state.
  
  When we had fast paths in `grow` and other places like resize we would
  adopt that without knowing it because we didn't properly clear.
  
  Fix this by properly clearing row metadata too at the points where we
  erase a row that might be reused.
  
  Benchmarked with terminal-stream workloads for each affected path. The
  added cost is 2-4 instructions per recycled row next to the existing
  full-row cell clear. There was no measurable wall-clock change on any
  workload.
  
  AI helped run the benchmarks for me and analyze for missing places (it
  found some!) but otherwise this was hand-designed.
  ```
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

