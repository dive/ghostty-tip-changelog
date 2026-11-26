> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 26, 2026 at 20:50 UTC.

## November 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/45803745959), [2](https://github.com/ghostty-org/ghostty/actions/runs/45727229222)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`4ebafeb`](https://github.com/ghostty-org/ghostty/commit/4ebafeb70b3dde9de578040f90fa9d8c13dfa2d0) Update VOUCHED list ([#15362](https://github.com/ghostty-org/ghostty/issues/15362)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/15360#issuecomment-7189692822)
  from @bo2themax.
  
  Vouch: @joariasl
  ```
- [`68bd03f`](https://github.com/ghostty-org/ghostty/commit/68bd03ffaf7be2c584d28780158c3a678d894e89) gtk: tidy tab color lifecycle ([@jcollie](https://github.com/jcollie))
  ```text
  Release the dialog's Tab reference in dispose rather than finalize.
  Cache the indicator texture on the Tab so it is rendered only when the
  color changes, not each time the tab is attached to a window.
  ```
- [`69023b8`](https://github.com/ghostty-org/ghostty/commit/69023b8169389ff57c9453b390691e543f5438e8) i18n: Added Dutch translation for tab colors ([#15341](https://github.com/ghostty-org/ghostty/issues/15341)) ([@mtak](https://github.com/mtak))
  ```text
  Added translations for new tab colors feature.
  ```

## November 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/45669916609), [2](https://github.com/ghostty-org/ghostty/actions/runs/45655415768), [3](https://github.com/ghostty-org/ghostty/actions/runs/45640498209), [4](https://github.com/ghostty-org/ghostty/actions/runs/45586322325), [5](https://github.com/ghostty-org/ghostty/actions/runs/45549462296)  
Summary: 5 runs • 19 commits • 6 authors

### Changes

- [`6be3e37`](https://github.com/ghostty-org/ghostty/commit/6be3e37f320be45865e575cd58133f7842283f5e) gtk: wait for the bell test's pipelines before dropping them ([@jcollie](https://github.com/jcollie))
  ```text
  GTK's GStreamer backend unrefs its source element on dispose without
  checking that it was created, which happens asynchronously. The test
  dropped each MediaFile within milliseconds, logging a g_object_unref
  critical. Wait until each stream is prepared or has failed first.
  ```
- [`b3f3248`](https://github.com/ghostty-org/ghostty/commit/b3f32483e02d724452249857b494584a83329f8e) gtk: wait for the bell test's pipelines before dropping them ([#15355](https://github.com/ghostty-org/ghostty/issues/15355)) ([@jcollie](https://github.com/jcollie))
  ```text
  GTK's GStreamer backend unrefs its source element on dispose without
  checking that it was created, which happens asynchronously. The test
  dropped each MediaFile within milliseconds, logging a g_object_unref
  critical. Wait until each stream is prepared or has failed first.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`107f448`](https://github.com/ghostty-org/ghostty/commit/107f44866c1af539f44f72a636c742fc1f604543) Update VOUCHED list ([#15356](https://github.com/ghostty-org/ghostty/issues/15356)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15349#discussioncomment-19897234)
  from @jcollie.
  
  Vouch: @abhinavgautam01
  ```
- [`ee01281`](https://github.com/ghostty-org/ghostty/commit/ee01281f1bb4d7dbe2af97c72f771fc21c04a844) i18n: add missing Polish translations ([@trag1c](https://github.com/trag1c))
- [`8fd700c`](https://github.com/ghostty-org/ghostty/commit/8fd700c872ba2e18bcf5760332d5c28a2f0c1fce) i18n: add missing Polish translations ([#15340](https://github.com/ghostty-org/ghostty/issues/15340)) ([@trag1c](https://github.com/trag1c))
- [`70cee58`](https://github.com/ghostty-org/ghostty/commit/70cee5810605052227608295f2b097322d20e49b) valgrind: suppress definite leaks from the fontconfig init thread ([@mitchellh](https://github.com/mitchellh))
  ```text
  This was from the new GTK tests we expose. These are out of control so
  we shuld suppress like our other fontconfig leaks.
  ```
- [`b445ef1`](https://github.com/ghostty-org/ghostty/commit/b445ef1967621c9bde7c053dea4215094ab3b4b0) terminal: HTML formatter only links allowlist of OSC 8 URI schemes ([@mitchellh](https://github.com/mitchellh))
  ```text
  The formatter now only writes the URI as the link target if it starts
  with `http://`, `https://`, `mailto:` or `file://`. Any other link
  keeps its text and its tag but points at `#`. This allowlist is based on
  a broad survey of tools like Go's `html/template`, `ansi2html`,
  `terminal-to-html` and others.
  
  Previously, the HTML formatter wrote the URI of an OSC 8 hyperlink
  into the `href` exactly as sent on the pty. A program could print
  
      printf '\033]8;;javascript:alert(1)\033\\click me\033]8;;\033\\'
  
  and the HTML for that screen had `<a href="javascript:alert(1)">`.
  Clicking that link in a browser runs the script in whatever origin the
  HTML was opened from.
  
  `file://` is allowed with any host so that links from programs like
  `ls --hyperlink` are kept, since those write `file://hostname/path`.
  The tradeoff is that on Windows a `file://` link that specifies a host is
  a network path, so following it connects to that host. Only Edge,
  though. Chrome and Firefox reject it.
  
  This also fixes non-ASCII URIs in HTML output. Each byte of the URI was
  written as its own character reference, so a URI with `café` in it
  pointed at `cafÃ©` instead. Bytes outside printable ASCII are now
  percent-encoded, which keeps the bytes the program sent whether or not
  they are valid UTF-8.
  ```
- [`c50ec0b`](https://github.com/ghostty-org/ghostty/commit/c50ec0bb5549bcca37d8ea6f078676fa99734ea8) terminal: HTML formatter only links allowlist of OSC 8 URI schemes ([#15347](https://github.com/ghostty-org/ghostty/issues/15347)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The formatter now only writes the URI as the link target if it starts
  with `http://`, `https://`, `mailto:` or `file://`. Any other link keeps
  its text and its tag but points at `#`. This allowlist is based on a
  broad survey of tools like Go's `html/template`, `ansi2html`,
  `terminal-to-html` and others.
  
  Previously, the HTML formatter wrote the URI of an OSC 8 hyperlink into
  the `href` exactly as sent on the pty. A program could print
  
      printf '\033]8;;javascript:alert(1)\033\\click me\033]8;;\033\\'
  
  and the HTML for that screen had `<a href="javascript:alert(1)">`.
  Clicking that link in a browser runs the script in whatever origin the
  HTML was opened from.
  
  `file://` is allowed with any host so that links from programs like `ls
  --hyperlink` are kept, since those write `file://hostname/path`. The
  tradeoff is that on Windows a `file://` link that specifies a host is a
  network path, so following it connects to that host. Only Edge, though.
  Chrome and Firefox reject it.
  
  This also fixes non-ASCII URIs in HTML output. Each byte of the URI was
  written as its own character reference, so a URI with `café` in it
  pointed at `cafÃ©` instead. Bytes outside printable ASCII are now
  percent-encoded, which keeps the bytes the program sent whether or not
  they are valid UTF-8.
  
  **AI usage:** Opus for tests and Fable for adversarial validation.
  ```
- [`9fd1ebf`](https://github.com/ghostty-org/ghostty/commit/9fd1ebf21f04f81b0cc21ad28fcef91aa51b016f) gtk: skip display tests when GTK has no display ([@mitchellh](https://github.com/mitchellh))
- [`c97b4d0`](https://github.com/ghostty-org/ghostty/commit/c97b4d0b26f114a5e2e96e9f9c9788d7fc42a7bc) i18n: Latvian color names and other string translations ([@EriksRemess](https://github.com/EriksRemess))
- [`17e7851`](https://github.com/ghostty-org/ghostty/commit/17e7851f7b1a85a38eded59cc8a198bf8afc0808) fix(i18n/id_ID): update Bahasa Indonesia translation ([@clavinjune](https://github.com/clavinjune))
- [`b78ea4c`](https://github.com/ghostty-org/ghostty/commit/b78ea4c69bc3aac5fb30d8830b47a528999fcf6d) fix(i18n/id_ID): update Bahasa Indonesia translation ([#15335](https://github.com/ghostty-org/ghostty/issues/15335)) ([@trag1c](https://github.com/trag1c))
- [`57c8bb9`](https://github.com/ghostty-org/ghostty/commit/57c8bb9dbc97b416980d7c84483666a88245a5f7) i18n: Latvian color names and other string translations ([#15333](https://github.com/ghostty-org/ghostty/issues/15333)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translated new tab color related strings in Latvian
  ```
- [`18c4192`](https://github.com/ghostty-org/ghostty/commit/18c4192f5238b0dd1b2cc9002f8d1e88c19f86fd) gtk: use adw.AccentColor directly for tab colors ([@jcollie](https://github.com/jcollie))
  ```text
  Replace the TabColor enum, a copy of adw.AccentColor plus `none`, with
  `?adw.AccentColor`. Move swatch drawing into tab_color_swatch.zig.
  
  The old tests never ran, since class.zig's refAllDecls doesn't reach
  class/. Replace them with a test of the dialog's choices and wire the
  dialog into the GTK test root.
  ```
- [`f9704a3`](https://github.com/ghostty-org/ghostty/commit/f9704a382d9e6752e760cece09ead0b49f31929b) gtk: run tests in tab.zig, gsettings.zig and media.zig ([@jcollie](https://github.com/jcollie))
  ```text
  Their tests were never collected, since those files are only reached
  through private imports. Import them from the GTK test blocks.
  
  That shows the bellMediaFile test could not pass: fromFilename needs the
  file to exist and GtkMediaFile needs GTK initialized. Create the files in
  a temporary directory, and skip when GTK cannot initialize.
  ```
- [`e6ad393`](https://github.com/ghostty-org/ghostty/commit/e6ad393d7917776914716b3fd474b96b67ae6e73) ci: download Zig from the community mirrors in the Debian build ([@jcollie](https://github.com/jcollie))
  ```text
  ziglang.org is slow enough at times to time out the Debian job. Add
  download-zig.sh, which tries the community mirrors in random order with
  ziglang.org last, skips slow ones, and verifies each download with
  minisign, checking that the signature names the requested file.
  ```
- [`5f1681c`](https://github.com/ghostty-org/ghostty/commit/5f1681c3b5d7d989817c002f663ec6765986ca03) ci: download Zig from the community mirrors in the Debian build ([#15345](https://github.com/ghostty-org/ghostty/issues/15345)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ziglang.org is slow enough at times to time out the Debian job. Add
  download-zig.sh, which tries the community mirrors in random order with
  ziglang.org last, skips slow ones, and verifies each download with
  minisign, checking that the signature names the requested file.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`0b2a612`](https://github.com/ghostty-org/ghostty/commit/0b2a61201948f954e303a97c1fbc2453b17df8a7) gtk: run tests in tab.zig, gsettings.zig and media.zig ([#15344](https://github.com/ghostty-org/ghostty/issues/15344)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Their tests were never collected, since those files are only reached
  through private imports. Import them from the GTK test blocks.
  
  That shows the bellMediaFile test could not pass: fromFilename needs the
  file to exist and GtkMediaFile needs GTK initialized. Create the files
  in a temporary directory, and skip when GTK cannot initialize.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`10473f6`](https://github.com/ghostty-org/ghostty/commit/10473f62e2e5fc60e3098da9f28057e67b696135) gtk: use adw.AccentColor directly for tab colors ([#15343](https://github.com/ghostty-org/ghostty/issues/15343)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the TabColor enum, a copy of adw.AccentColor plus `none`, with
  `?adw.AccentColor`. Move swatch drawing into tab_color_swatch.zig.
  
  The old tests never ran, since class.zig's refAllDecls doesn't reach
  class/. Replace them with a test of the dialog's choices and wire the
  dialog into the GTK test root.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```

## November 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/45511088642), [2](https://github.com/ghostty-org/ghostty/actions/runs/45457981464), [3](https://github.com/ghostty-org/ghostty/actions/runs/45447070333), [4](https://github.com/ghostty-org/ghostty/actions/runs/45443043723), [5](https://github.com/ghostty-org/ghostty/actions/runs/45315443751)  
Summary: 5 runs • 12 commits • 4 authors

### Changes

- [`aeceee1`](https://github.com/ghostty-org/ghostty/commit/aeceee152f534e53b99c38590b230df0b9697948) fix(i18n/ja_JP): update Japanese translation ([@clavinjune](https://github.com/clavinjune))
- [`64a6fed`](https://github.com/ghostty-org/ghostty/commit/64a6fedfd26d1fa687733f9f411db5eb8e205ebe) bump for lib-vt 1.0.3-dev ([@mitchellh](https://github.com/mitchellh))
- [`ee1ceb2`](https://github.com/ghostty-org/ghostty/commit/ee1ceb20da187f9bbc3e018bd405dd948b2be7e5) fix(i18n/ja_JP): update Japanese translation ([#15336](https://github.com/ghostty-org/ghostty/issues/15336)) ([@trag1c](https://github.com/trag1c))
- [`5e48fe3`](https://github.com/ghostty-org/ghostty/commit/5e48fe30295bdd499c8c631236aa7869992515be) build: lower minimum required version to 0.17.0 ([@mitchellh](https://github.com/mitchellh))
  ```text
  We don't NEED 0.17.1, so we should support environments that have any
  0.17.x. This was caught during an audit prior to a new libghostty-vt
  release. We shouldn't force that ecosystem to update Zig versions here.
  ```
- [`16c7a73`](https://github.com/ghostty-org/ghostty/commit/16c7a734648011d0e4a6bf763e2f4e2f3bd27d8a) build: lower minimum required version to 0.17.0 ([#15339](https://github.com/ghostty-org/ghostty/issues/15339)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We don't NEED 0.17.1, so we should support environments that have any
  0.17.x. This was caught during an audit prior to a new libghostty-vt
  release. We shouldn't force that ecosystem to update Zig versions here.
  
  Our builds and CI still run 0.17.1.
  ```
- [`573c4a2`](https://github.com/ghostty-org/ghostty/commit/573c4a21e02311ae87844af26b6a7a179f82858e) libghostty-vt: v1.0.2 ([@mitchellh](https://github.com/mitchellh))
- [`7a1dbc2`](https://github.com/ghostty-org/ghostty/commit/7a1dbc2152f6cc71a4f1ffe873f4f9def4f28b3d) font: skin tone modifiers imply emoji presentation for shaping ([@mitchellh](https://github.com/mitchellh))
  ```text
  See #15315 #15337
  
  UTS #51 says a skin tone modifier implies emoji presentation for its
  base, with no VS16 needed. The shaper only looked for VS15 and VS16,
  so these clusters had no preference and took the first font that had
  every code point. If the first codepoint (such as U+1F590) defaults to
  text, then the whole thing stayed text.
  
  A modifier now asks for emoji presentation like VS16 does. Unlike
  VS16, it is only a preference: if no font supports the cluster as an
  emoji, we search again with no preference, so a font setup with no
  color emoji font still draws the cluster as text instead of a
  replacement character.
  
  macOS was never affected since Apple Color Emoji is the only emoji
  fallback there, and it resolves the same way before and after.
  ```
- [`65f9061`](https://github.com/ghostty-org/ghostty/commit/65f90613a9551c7136d78a97ba680a37f2c14b8c) font: skin tone modifiers imply emoji presentation for shaping ([#15338](https://github.com/ghostty-org/ghostty/issues/15338)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  See #15315 #15337
  
  UTS #51 says a skin tone modifier implies emoji presentation for its
  base, with no VS16 needed. The shaper only looked for VS15 and VS16, so
  these clusters had no preference and took the first font that had every
  code point. If the first codepoint (such as U+1F590) defaults to text,
  then the whole thing stayed text.
  
  A modifier now asks for emoji presentation like VS16 does. Unlike VS16,
  it is only a preference: if no font supports the cluster as an emoji, we
  search again with no preference, so a font setup with no color emoji
  font still draws the cluster as text instead of a replacement character.
  
  macOS was never affected since Apple Color Emoji is the only emoji
  fallback there, and it resolves the same way before and after.
  
  **AI usage:** Opus helped run the tests as well as do graphical runs for
  me with screenshots across platforms.
  ```
- [`a0e3e25`](https://github.com/ghostty-org/ghostty/commit/a0e3e2592646d3dbc6cea7fe7051171e86f1c666) unicode: a skin tone modifier widens its grapheme cluster ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15315
  
  With grapheme clustering (mode 2027), a skin tone modifier
  (U+1F3FB through U+1F3FF) after an emoji that is drawn as text by
  default left the cluster 1 cell wide. For example, U+261D U+1F3FB
  (index pointing up, light skin tone) took 1 cell, while U+261D U+FE0F
  took 2. A modifier asks for the emoji form of its base (UTS #51,
  section 2.4), so it should widen the cluster just like VS16 does.
  
  This is free, this just modifies our LUT and doesn't change any of the
  actual print logic. I ran benchmarks to verify though.
  ```
- [`77c2f8b`](https://github.com/ghostty-org/ghostty/commit/77c2f8b9f706c9e7692de8eecb86c759ddc6dbc8) unicode: a skin tone modifier widens its grapheme cluster ([#15337](https://github.com/ghostty-org/ghostty/issues/15337)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15315
  
  With grapheme clustering (mode 2027), a skin tone modifier (U+1F3FB
  through U+1F3FF) after an emoji that is drawn as text by default left
  the cluster 1 cell wide. For example, U+261D U+1F3FB (index pointing up,
  light skin tone) took 1 cell, while U+261D U+FE0F took 2. A modifier
  asks for the emoji form of its base (UTS #51, section 2.4), so it should
  widen the cluster just like VS16 does.
  
  Note uucode does the right thing here because it applies this logic in
  its width function. We don't use that because we use a LUT, and our LUT
  didn't handle this property properly.
  
  This is free, this just modifies our LUT and doesn't change any of the
  actual print logic. I ran benchmarks to verify though.
  ```
- [`7059ea9`](https://github.com/ghostty-org/ghostty/commit/7059ea928cbe495c3da61397be8e06399c33f715) build(deps): bump cachix/install-nix-action from 31.11.5 to 32.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.5 to 32.0.0.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/3dc140bfc76c49fbd4dd958429132e3746bcb086...bb0495a1086c46893eee56f32fd192dfe4a15bb9)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 32.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`167acf0`](https://github.com/ghostty-org/ghostty/commit/167acf0c4e3c29c1037c4fa935dfe5c053e04849) build(deps): bump cachix/install-nix-action from 31.11.5 to 32.0.0 ([#15329](https://github.com/ghostty-org/ghostty/issues/15329)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.5 to 32.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v32.0.0</h2>
  <h2>Breaking changes</h2>
  <ul>
  <li>Drop support for <code>x86_64-darwin</code> (Intel Macs).
  Nix no longer provides installers and binaries for this platform.
  Older Nix releases (&lt; 2.36) can still be installed by setting
  <code>install_url</code>, but this action no longer tests against the
  platform.</li>
  </ul>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.6 -&gt; 2.36.0 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/288">cachix/install-nix-action#288</a>
  Release notes: <a
  href="https://discourse.nixos.org/t/nix-2-36-0-released/81345">https://discourse.nixos.org/t/nix-2-36-0-released/81345</a>
  <a
  href="https://github.com/NixOS/nix/compare/2.35.6...2.36.0">https://github.com/NixOS/nix/compare/2.35.6...2.36.0</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.5...v32.0.0">https://github.com/cachix/install-nix-action/compare/v31.11.5...v32.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/blob/master/RELEASE.md">cachix/install-nix-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Release</h1>
  <p>As of v31, releases of this action follow Semantic Versioning.</p>
  <h3>Publishing a new release</h3>
  <h4>Publish the release</h4>
  <p>Draft <a
  href="https://github.com/cachix/install-nix-action/releases">a new
  release on GitHub</a>:</p>
  <ul>
  <li>In <code>Choose a tag</code>, create a new tag, like
  <code>v32.0.0</code>, following semver.</li>
  <li>Click <code>Generate release notes</code>.</li>
  <li><code>Set as the latest release</code> should be selected
  automatically.</li>
  <li>Publish release</li>
  </ul>
  <h4>Update the major tag</h4>
  <p>The major tag, like <code>v32</code>, allows downstream users to
  opt-in to automatic non-breaking updates.</p>
  <p>This process follows GitHub's own guidelines:
  <a
  href="https://github.com/actions/toolkit/blob/main/docs/action-versioning.md">https://github.com/actions/toolkit/blob/main/docs/action-versioning.md</a></p>
  <h5>Fetch the latest tags</h5>
  <pre><code>git pull --tags --force
  </code></pre>
  <h5>Move the tag</h5>
  <pre><code>git tag -fa v32
  </code></pre>
  <pre><code>git push origin v32 --force
  </code></pre>
  <h4>Update the release notes for the major tag</h4>
  <p>Find the release on GitHub: <a
  href="https://github.com/cachix/install-nix-action/releases">https://github.com/cachix/install-nix-action/releases</a></p>
  <p>Edit the release and click <code>Generate release notes</code>.
  Edit the formatting and publish.</p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/bb0495a1086c46893eee56f32fd192dfe4a15bb9"><code>bb0495a</code></a>
  docs: bump v31 -&gt; v32</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/48ee3e5ae067ae2bb929cce004084bc74e1edfc7"><code>48ee3e5</code></a>
  ci: bump pinned actions</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/e32e2cb6c76c7320968aa550ec16f80167b1dfb5"><code>e32e2cb</code></a>
  docs: bump action versions in README</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/00bbf4d7087036fe23c1a44c11055447c60edb31"><code>00bbf4d</code></a>
  breaking: drop support for x86_64-darwin</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/3546cc0ab361ed3b839171fd3984533b608ec6cf"><code>3546cc0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/288">#288</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/e224a58dbd8cd5d9687bc4a1936bd554da152c1b"><code>e224a58</code></a>
  nix: 2.35.6 -&gt; 2.36.0</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/3dc140bfc76c49fbd4dd958429132e3746bcb086...bb0495a1086c46893eee56f32fd192dfe4a15bb9">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.5&new-version=32.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## November 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/45282518117), [2](https://github.com/ghostty-org/ghostty/actions/runs/45246685675), [3](https://github.com/ghostty-org/ghostty/actions/runs/45198570135), [4](https://github.com/ghostty-org/ghostty/actions/runs/45158528108), [5](https://github.com/ghostty-org/ghostty/actions/runs/45155969664), [6](https://github.com/ghostty-org/ghostty/actions/runs/45108393933), [7](https://github.com/ghostty-org/ghostty/actions/runs/45100290092)  
Summary: 7 runs • 35 commits • 7 authors

### Changes

- [`ff61ef6`](https://github.com/ghostty-org/ghostty/commit/ff61ef60dca4db5d846adee62b17d746a94f07fc) url: exclude trailing punctuation from path matches ([@Davey-Hughes](https://github.com/Davey-Hughes))
  ```text
  Path matches kept sentence punctuation that followed them, so
  cmd-clicking "See /etc/hosts." tried to open "/etc/hosts." and failed.
  Paths already dropped a trailing ":"; they now also drop ".", "?", "!"
  and ";", and no longer continue across a space after any of them
  except ".". The dots of a final "." or ".." segment are kept, so
  "cd ../.." still matches in full.
  
  A trailing period also no longer counts as the dot that bare relative
  paths require, so "see foo/bar." still doesn't match.
  
  This also stops "~/.config/ghostty/config again." from matching
  through "again.".
  
  Discussion: #12527
  ```
- [`0cc1fc6`](https://github.com/ghostty-org/ghostty/commit/0cc1fc64e1e7a4c5b841ed4f16fb106d9411c0ec) url: exclude trailing punctuation from path matches ([#15324](https://github.com/ghostty-org/ghostty/issues/15324)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### Now
  Path matches include sentence punctuation that follows them, so
  cmd-clicking a path at the end of a sentence fails: `See /etc/hosts.`
  opens `/etc/hosts.`.
  
  ### Change
  The scheme URL branch already drops a trailing `.` and `,`, but the path
  branches only dropped `:`. Paths now also drop a trailing `.`, `?`, `!`
  and `;`, and no longer continue across a space after `?`, `!` or `;`
  (they already couldn't after `:`).
  
  | Input | Before | After |
  |---|---|---|
  | `See /etc/hosts.` | `/etc/hosts.` | `/etc/hosts` |
  | `Is it in /etc/hosts?` | `/etc/hosts?` | `/etc/hosts` |
  | `see /etc/hosts; then reload` | `/etc/hosts; then reload` |
  `/etc/hosts` |
  | `~/.config/ghostty/config again.` | `~/.config/ghostty/config again.`
  | `~/.config/ghostty/config` |
  | `cd ../../..` | `../../..` | `../../..` |
  
  The dots of a final `.` or `..` segment are kept. A plain `(?<![:.])`
  would turn `../../..` into `../../`.
  
  A trailing period also no longer counts as the dot that bare relative
  paths need, so `see foo/bar.` still doesn't match, same as `foo/bar`.
  
  Tradeoff: a file whose name really ends in `.`, `?`, `!` or `;` loses
  that character. Those names are valid on Linux, macOS and FreeBSD, which
  allow any character except `/` and NUL. They're unportable, though:
  Windows reserves `?` and strips a trailing `.`. #14675 (from #14602)
  instead retries without the period at click time when the path doesn't
  exist. That keeps such names, but the hover underline still includes the
  period.
  
  
  Depending on what behavior a maintainer deems is better we could take
  #14675 instead.
  
  This doesn't touch the scheme URL branch (#15049).
  
  Discussion: #12527
  
  AI disclosure: Claude-Code, Claude Opus 5.5, most of the code was
  written by AI but the decisions and research of other issues/PRs were
  mine, and review was mine.
  ```
- [`805b44a`](https://github.com/ghostty-org/ghostty/commit/805b44a118285e0878f746f738fcba21b6be4d24) core: ignore lock and sided mods when checking if mouse mods changed ([@teddytennant](https://github.com/teddytennant))
  ```text
  The mouse mods are stored with Mods.binding(), which drops caps lock,
  num lock and the modifier sides, but modsChanged and keyCallback
  compared them against the raw event mods. With num lock on (GTK sets it
  on every key event), caps lock on, or a right-side modifier held on
  macOS, the two never match, so every key press and release that isn't
  consumed by a binding counted as a mods change: it marked the whole
  screen dirty, woke the renderer, and either reran link detection under
  the mouse or, with mouse reporting on, sent the mouse shape and link
  state to the apprt again. With caps lock on or a right-side modifier
  held on macOS, mouse moves and clicks marked the screen dirty too.
  
  Both checks now go through Mouse.modsEqual, which only compares the
  binding mods.
  ```
- [`d7c36d2`](https://github.com/ghostty-org/ghostty/commit/d7c36d2e8261a37effb5c92927c61060a2e54338) terminal: keep soft wraps when shifting rows with IL/DL ([@cammeresi](https://github.com/cammeresi))
  ```text
  insertLines and deleteLines cleared wrap state when the scroll region
  was full width.  Programs like vim scroll with a scroll region and
  IL/DL, after which a soft-wrapped line within a scrolled region loses
  its wrap status.  That in turn causes a URL spanning a soft wrap to be
  incorrectly treated as two separate links until the program redraws the
  screen.
  
  Keep the wrap state and spacer heads of rows that move together, and
  reset the wrap only for rows whose next row changed.
  
  Spacer heads have to be kept along with the wrap state.  Shifted rows
  previously had their spacer heads turned into empty cells because their
  wrap status was cleared.  Once the wrapped status is maintained through
  a scroll, an empty cell there would put a hard space in the middle of
  the text that had been only soft wrapped.  That changes the expected
  result of the deleteLines wide character spacer head test, whose two
  wrapped rows now stay joined.
  ```
- [`f07c80a`](https://github.com/ghostty-org/ghostty/commit/f07c80a7c2009e7f23eb9e34f0d42395c1b8a565) core: inline the binding mods comparison ([@teddytennant](https://github.com/teddytennant))
- [`df293fe`](https://github.com/ghostty-org/ghostty/commit/df293fe86c012659d3b70335dbbbc38b7a87850f) terminal: clear wrap continuation on rows orphaned by IL/DL ([@mitchellh](https://github.com/mitchellh))
- [`41b7254`](https://github.com/ghostty-org/ghostty/commit/41b72544691ff4eee4199d3eac7cd72a94195adc) terminal: keep semantic prompt marks across partial row moves ([@mitchellh](https://github.com/mitchellh))
  ```text
  Insert and delete lines w/ left and right margins didn't properly
  preserve semantic prompt marks.
  
  Both now combine the two rows' marks, with a prompt start winning over
  a continuation. A wrong start only adds an extra stop when jumping
  between prompts, but a wrong continuation would skip a prompt.
  ```
- [`4917fd8`](https://github.com/ghostty-org/ghostty/commit/4917fd8a1a8776eaa5ae39c95cee91492c6b8ee1) terminal: keep soft wraps when shifting rows with IL/DL ([#15309](https://github.com/ghostty-org/ghostty/issues/15309)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  insertLines and deleteLines cleared wrap state when the scroll region
  was full width. Programs like vim scroll with a scroll region and IL/DL,
  after which a soft-wrapped line within a scrolled region loses its wrap
  status. That in turn causes a URL spanning a soft wrap to be incorrectly
  treated as two separate links until the program redraws the screen.
  
  Keep the wrap state and spacer heads of rows that move together, and
  reset the wrap only for rows whose next row changed.
  
  Spacer heads have to be kept along with the wrap state. Shifted rows
  previously had their spacer heads turned into empty cells because their
  wrap status was cleared. Once the wrapped status is maintained through a
  scroll, an empty cell there would put a hard space in the middle of the
  text that had been only soft wrapped. That changes the expected result
  of the deleteLines wide character spacer head test, whose two wrapped
  rows now stay joined.
  
  I attempted to get the idea of a fix pre-approved by opening a
  discussion according to the contribution protocol, but since there has
  yet been no further discussion or acknowledgement, I decided to risk
  posting a patch anyway.
  
  Discussion:  https://github.com/ghostty-org/ghostty/discussions/14984
  
  AI advertisement: This defect was analyzed and located by Claude with
  Opus 5.5, which thereafter produced the bytes in this patch to my order.
  Those bytes were contemporaneously viewed in context and reviewed by me,
  who rejected 77% of proposed changes.
  ```
- [`e50c178`](https://github.com/ghostty-org/ghostty/commit/e50c178007ebe7022725ebf971348298ce17e7f9) terminal: keep semantic prompt marks across partial row moves ([#15327](https://github.com/ghostty-org/ghostty/issues/15327)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Insert and delete lines w/ left and right margins didn't properly
  preserve semantic prompt marks.
  
  Both now combine the two rows' marks, with a prompt start winning over a
  continuation. A wrong start only adds an extra stop when jumping between
  prompts, but a wrong continuation would skip a prompt.
  
  **AI usage:** Test written by Opus
  ```
- [`130288f`](https://github.com/ghostty-org/ghostty/commit/130288ffb2ac155d8d35558d7e40ec7acf3d9cc5) libghostty: restored snapshot keeps a pending wrap at any column ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15265
  
  Snapshot decode dropped the cursor's pending wrap unless the cursor was
  on the last column of the screen. Without margins that is the only
  place a wrap can be pending, but with left and right margins (DECLRMM
  and DECSLRM) printing up to the right margin leaves the wrap pending at
  the margin instead. A saved cursor (DECSC) keeps it there too, and
  restoring that cursor (DECRC) or turning DECLRMM off can leave a wrap
  pending at a column that is neither a margin nor the last column.
  
  The decoder now keeps the flag as encoded, for both the cursor and the
  saved cursor. The encoder already wrote the flag as-is, so only decode
  changes and the snapshot format is the same.
  ```
- [`f61fe7b`](https://github.com/ghostty-org/ghostty/commit/f61fe7b5d11d4ca4c08fed8105d32a4f923f27c3) libghostty: restored snapshot keeps a pending wrap at any column ([#15328](https://github.com/ghostty-org/ghostty/issues/15328)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15265
  
  Snapshot decode dropped the cursor's pending wrap unless the cursor was
  on the last column of the screen. Without margins that is the only place
  a wrap can be pending, but with left and right margins (DECLRMM and
  DECSLRM) printing up to the right margin leaves the wrap pending at the
  margin instead. A saved cursor (DECSC) keeps it there too, and restoring
  that cursor (DECRC) or turning DECLRMM off can leave a wrap pending at a
  column that is neither a margin nor the last column.
  
  The decoder now keeps the flag as encoded, for both the cursor and the
  saved cursor. The encoder already wrote the flag as-is, so only decode
  changes and the snapshot format is the same.
  
  **AI usage:** Tests by Opus.
  ```
- [`2474129`](https://github.com/ghostty-org/ghostty/commit/24741298a98489a1c5beb621ee271eb8b3675a27) core: ignore lock and sided mods when checking if mouse mods changed ([#15318](https://github.com/ghostty-org/ghostty/issues/15318)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With Num Lock or Caps Lock on, every key press and release redraws the
  whole screen. The mouse mods are stored with `Mods.binding()`, which
  drops the lock keys and sides, but `modsChanged` and `keyCallback`
  compared them to the raw event mods, so every key looked like a mods
  change.
  
  In a GTK build with Num Lock on, 100 keys took 302 frames and 200 full
  rebuilds. Now it's 202 and none, same as with Num Lock off.
  
  *AI disclosure: I used Claude Fable 5.2 to draft the fix and to review
  it. I've read and understand all of it.*
  ```
- [`aa7d1b6`](https://github.com/ghostty-org/ghostty/commit/aa7d1b66e567e68c0c62fdcb1cddfc931ed002c3) terminal: move styled cells with a single copy ([@teddytennant](https://github.com/teddytennant))
  ```text
  moveCells copied a row's cells in one pass only when the row had no
  styles, graphemes or hyperlinks, and otherwise went cell by cell. Styles
  don't need that: the copy carries each style ID along with the reference
  it holds. Only rows with graphemes, hyperlinks or placeholders take the
  per-cell path now.
  
  insertLines and deleteLines call this for every row they shift when
  left and right margins are set, which is how tmux scrolls a pane that
  has another pane beside it and how Neovim scrolls a vertical split.
  
  This also fixes a row that had Kitty placeholders but no other managed
  memory: it took the single copy, so the destination row never got its
  placeholder flag.
  ```
- [`3e9b1cc`](https://github.com/ghostty-org/ghostty/commit/3e9b1cca3775bc31dcc055b5172832a3dcd1d66c) terminal: move styled cells with a single copy ([#15313](https://github.com/ghostty-org/ghostty/issues/15313)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `moveCells` only took its single copy for rows with no styles, graphemes
  or hyperlinks. Styles are keyed by ID, so a styled row can take it too.
  `insertLines` and `deleteLines` call this for every row when left and
  right margins are set, which is how tmux scrolls a pane with another one
  beside it.
  
  `ghostty-bench +terminal-stream` at 120x40 on the stream below goes from
  1716 ms to 936 ms on an i7-11700K, and from 1100 ms to 695 ms on an M1
  Pro.
  
  ```
  awk 'BEGIN { printf "\033[?69h\033[1;40r\033[61;120s"; for (i = 0; i < 300000; i++) printf "\033[40;61H\n\033[3%dmline %d of output in the right-hand pane\033[m", i % 6 + 1, i }' > margins.vt
  ```
  
  A row with Kitty placeholders but no styles used to take the single copy
  and lose its placeholder flag. It takes the per-cell path now.
  
  *AI disclosure: I used Claude Fable 5.2 to draft the fix and to review
  it. I've read and understand all of it.*
  ````
- [`4ca667f`](https://github.com/ghostty-org/ghostty/commit/4ca667f7f9e14371b63d01939327424e213a9a9f) gtk: emit RenderSurface resizes at most once per frame ([@jcollie](https://github.com/jcollie))
  ```text
  A widget can be allocated more than once in a single layout pass. A
  GtkScrolledWindow with non-overlay scrollbars ("Always Show Scrollbars")
  allocates its child as if the scrollbar were hidden, checks the
  adjustment, and allocates it again narrower to make room for the
  scrollbar. RenderSurface emitted `resize` on every allocation, so each
  layout pass resized the terminal twice, and since the two sizes really
  differ, the size-change guard from #11970 let both through. The resize
  overlay then relabels itself, which queues another layout pass, and the
  loop never settles: the overlay stays up and the terminal keeps
  resizing between the two widths.
  
  GtkGLArea never had this problem because it only flagged a pending
  resize in size-allocate and emitted it from its snapshot, with the
  final size. Do the same: emit the first allocation immediately, so that
  the core surface is still initialized on the first resize, and defer the
  rest to snapshot.
  
  Fixes: #15078
  ```
- [`dd9cbff`](https://github.com/ghostty-org/ghostty/commit/dd9cbff037946f3fe9d72a546a429d6f4f03fa42) gtk: paste a single dropped file ([@jcollie](https://github.com/jcollie))
  ```text
  Dropping a single file built its shell-escaped path but never pasted
  it, and leaked the path.
  ```
- [`df28358`](https://github.com/ghostty-org/ghostty/commit/df28358dd4a228749a237ed031de2f8dde163d99) gtk: coalesce mouse cursor updates ([@jcollie](https://github.com/jcollie))
  ```text
  Programs can change the mouse shape many times in a single write. tmux
  with `mouse on` resets mouse reporting after every passthrough chunk,
  so a Kitty graphics image sent through tmux toggles the shape between
  text and default hundreds of times. Each change was applied to the
  render surface immediately, and on Wayland each one is a separate
  wp_cursor_shape_device_v1.set_shape request. A large enough burst
  fills the client's socket buffer and GTK exits with "Error flushing
  display: Resource temporarily unavailable", taking every window with
  it.
  
  Apply the mouse shape and hidden state on an idle tick instead, and
  only when the resulting cursor differs from the one last set. A burst
  now produces at most one request. A reproducer that sends 2000 mouse
  mode resets in one write went from ~3900 set_shape requests to 10.
  
  See discussions #11944 and #11909.
  
  Fixes #14886
  ```
- [`bf6bd1f`](https://github.com/ghostty-org/ghostty/commit/bf6bd1fa58391fdae1a31552d1baeb456f45cdee) gtk: add per-tab color indicators ([@edsarmiento](https://github.com/edsarmiento))
  ```text
  #14979
  
  Add a tab context menu action that opens a small color dialog and
  shows the chosen color as an AdwTabPage indicator icon.
  ```
- [`1cef2dc`](https://github.com/ghostty-org/ghostty/commit/1cef2dce47de1b2db5fe9b561108abb40b2bad95) gtk: address tab color review feedback ([@edsarmiento](https://github.com/edsarmiento))
  ```text
  Draw color swatches with gtk.Snapshot vector paths instead of a
  16x16 pixel bitmap, including a slashed outline for none and a
  selection ring for the current color in the picker dialog. Update
  translation catalogs for the new strings.
  ```
- [`1cd7dc0`](https://github.com/ghostty-org/ghostty/commit/1cd7dc0e33520207a82a038c22c546344f8d7189) gtk: shorten tab color comments ([@edsarmiento](https://github.com/edsarmiento))
- [`9451230`](https://github.com/ghostty-org/ghostty/commit/9451230b4e60758b4b446d1de3a53f7ecabedd2c) gtk: address second tab color review ([@edsarmiento](https://github.com/edsarmiento))
- [`8de4824`](https://github.com/ghostty-org/ghostty/commit/8de4824a294d830471e13dbd1c8e05e1cd907092) gtk: add TabColor unit tests ([@edsarmiento](https://github.com/edsarmiento))
- [`36fcc8c`](https://github.com/ghostty-org/ghostty/commit/36fcc8cebd9a9ec4ebf0bef20eee5efdea02042b) gtk: use Adwaita accents and fix tab color review nits ([@edsarmiento](https://github.com/edsarmiento))
  ```text
  #14986
  
  Draw tab color swatches from adw.AccentColor instead of hardcoded
  RGB values, share the empty indicator texture fallback helper, and
  use a ToggleButton group so the selected swatch exposes a checked
  accessible state. Initialize graphene Point/Rect with struct
  literals so CI does not need a direct graphene link.
  ```
- [`dcf9c1a`](https://github.com/ghostty-org/ghostty/commit/dcf9c1aef65def805c16437fa297c118cc6f7157) gtk: simplify tab color selection UX ([@edsarmiento](https://github.com/edsarmiento))
- [`56de3f0`](https://github.com/ghostty-org/ghostty/commit/56de3f0f6786a3ff4f971d075a28f73409212983) i18n: refresh catalogs for tab color dialog ([@edsarmiento](https://github.com/edsarmiento))
  ```text
  Regenerate the translation template after rebasing onto main so the
  tab color strings and their source locations stay in sync with the code.
  ```
- [`5749a0f`](https://github.com/ghostty-org/ghostty/commit/5749a0f67469f5bbb50353bee2a1d0011b146396) font: stop runs at the last cell with text ([@teddytennant](https://github.com/teddytennant))
- [`7f8b1c9`](https://github.com/ghostty-org/ghostty/commit/7f8b1c956daa010c0687caeec307303dd212f246) font: trim runs in init with Cell.isBlank ([@teddytennant](https://github.com/teddytennant))
- [`6874ea6`](https://github.com/ghostty-org/ghostty/commit/6874ea6dd80e7b96f68c28ba4c6642b771ca5308) font: trim a trailing spacer head ([@teddytennant](https://github.com/teddytennant))
- [`65ad366`](https://github.com/ghostty-org/ghostty/commit/65ad366e36d773c4a54afebb78ee958ef43d6357) libghostty: keep mouse encoder last cell across syncs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The mouse encoder now remembers the "last cell" state across option
  changes that don't impact it.
  
  This is important because we document and recommend that every mouse
  encoding you resync from terminal (so you get latest terminal modes).
  Even if nothing changed, this was dropping last cell state, meaning we
  were over-encoding mouse position in otherwise well-behaved programs.
  
  From a VT perspective, there's nothing WRONG about that, but it actually
  did cause a real bug: Codex expects a mouse click to behave as a
  back-to-back "press" then "release" event. I think that's a bug and I
  reported it upstream but this revealed this behavior because we'd do
  "press" then "motion" then "release."
  ```
- [`8411b95`](https://github.com/ghostty-org/ghostty/commit/8411b9551e65d92913ab7028318a981c0495d4cb) terminal: keep the kitty placeholder flag in partial row clones ([@jcollie](https://github.com/jcollie))
  ```text
  A partial clonePartialRowFrom took the source row's
  kitty_virtual_placeholder flag, so placeholders in the destination
  outside the copied range stopped rendering. This happens when
  insertLines or deleteLines with left and right margins move a row
  across a page boundary.
  
  Keep the flag if either row has it.
  ```
- [`74d1983`](https://github.com/ghostty-org/ghostty/commit/74d1983f27eb004ef442c8353bd703eba19c93b6) libghostty: keep mouse encoder last cell across syncs ([#15317](https://github.com/ghostty-org/ghostty/issues/15317)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The mouse encoder now remembers the "last cell" state across option
  changes that don't impact it.
  
  This is important because we document and recommend that every mouse
  encoding you resync from terminal (so you get latest terminal modes).
  Even if nothing changed, this was dropping last cell state, meaning we
  were over-encoding mouse position in otherwise well-behaved programs.
  
  From a VT perspective, there's nothing WRONG about that, but it actually
  did cause a real bug: Codex expects a mouse click to behave as a
  back-to-back "press" then "release" event. I think that's a bug and I
  reported it upstream but this revealed this behavior because we'd do
  "press" then "motion" then "release."
  ```
- [`dc42b86`](https://github.com/ghostty-org/ghostty/commit/dc42b864e7ba365a91ce85e7b68c6e49cc9759aa) terminal: keep the kitty placeholder flag in partial row clones ([#15320](https://github.com/ghostty-org/ghostty/issues/15320)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A partial clonePartialRowFrom took the source row's
  kitty_virtual_placeholder flag, so placeholders in the destination
  outside the copied range stopped rendering. This happens when
  insertLines or deleteLines with left and right margins move a row across
  a page boundary.
  
  Keep the flag if either row has it.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`7424140`](https://github.com/ghostty-org/ghostty/commit/74241405fe457d6a569a110cffe9d75a1c9a53b7) font: stop runs at the last cell with text ([#15288](https://github.com/ghostty-org/ghostty/issues/15288)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Background-only cells don't count as empty to `Cell.isEmpty`. Terminal
  apps that fill rows with their own background color (e.g. nvim's default
  scheme, most colorschemes, tmux status lines) get blank cells shaped all
  the way to the right edge. Now the trim stops at the last cell with
  text, and it's only computed once per row.
  
  `ghostty-bench +shaper-rows --mode=shape` on a captured nvim screen goes
  from 173 ms to 77 ms on an i7-11700K and 321 ms to 203 ms on an M1 Pro.
  
  *AI disclosure: I used Claude Opus 5.5 to draft the fix and to review
  it. I've read and understand all of it.*
  ```
- [`a063249`](https://github.com/ghostty-org/ghostty/commit/a0632495d4507d46d972ab92d7a7180e9e011032) build(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 3.3.0 to 3.4.0.
  - [Release notes](https://github.com/actions/create-github-app-token/releases)
  - [Changelog](https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/create-github-app-token/compare/64ab729a6294000f5aa4a4bc0b73d1f32bc45510...f418cff399f7aef4c2f0ad47e25ca7a6abbdd6fc)
  
  ---
  updated-dependencies:
  - dependency-name: actions/create-github-app-token
    dependency-version: 3.4.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`ec5925a`](https://github.com/ghostty-org/ghostty/commit/ec5925acf948c00f8204c420329f142f6e1471bb) build(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0 ([#15322](https://github.com/ghostty-org/ghostty/issues/15322)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
  from 3.3.0 to 3.4.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.4.0</h2>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.3.0...v3.4.0">3.4.0</a>
  (2026-11-18)</h2>
  <h3>Features</h3>
  <ul>
  <li>bump actions/setup-node from 6 to 7 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/410">#410</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/09c1ab7079f14af5f0d64c9325739c49a8541f56">09c1ab7</a>)</li>
  <li>bump actions/stale from 10 to 11 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/409">#409</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/679345a20e2e07130130e6cf0301b9e897f18cd5">679345a</a>)</li>
  <li>bump stefanzweifel/git-auto-commit-action from 7.2.0 to 7.2.1 in the
  github-actions group (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/408">#408</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/660c44c8ce22207448fbba2730cd2913052c9de3">660c44c</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump undici (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/406">#406</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/18e9994c8d13ac7c7e2bbcc3355a1a4f31d30de7">18e9994</a>)</li>
  </ul>
  <h2>v3.4.0-beta</h2>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.3.0...v3.4.0-beta">3.4.0-beta</a>
  (2026-11-17)</h2>
  <h3>Features</h3>
  <ul>
  <li>support GitHub Actions OIDC authentication (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/411">#411</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/8240f10d3ae05b4d450da83e8e247111a36eaf2c">8240f10</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md">actions/create-github-app-token's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.3.0...v3.4.0">3.4.0</a>
  (2026-11-18)</h2>
  <h3>Features</h3>
  <ul>
  <li>bump actions/setup-node from 6 to 7 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/410">#410</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/09c1ab7079f14af5f0d64c9325739c49a8541f56">09c1ab7</a>)</li>
  <li>bump actions/stale from 10 to 11 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/409">#409</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/679345a20e2e07130130e6cf0301b9e897f18cd5">679345a</a>)</li>
  <li>bump stefanzweifel/git-auto-commit-action from 7.2.0 to 7.2.1 in the
  github-actions group (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/408">#408</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/660c44c8ce22207448fbba2730cd2913052c9de3">660c44c</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump undici (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/406">#406</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/18e9994c8d13ac7c7e2bbcc3355a1a4f31d30de7">18e9994</a>)</li>
  </ul>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.2.0...v3.3.0">3.3.0</a>
  (2026-10-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e">a47236f</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb">12461a3</a>)</li>
  <li><strong>deps:</strong> bump the production-dependencies group across
  1 directory with 3 updates (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/395">#395</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807">a69c19d</a>)</li>
  </ul>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.1.1...v3.2.0">3.2.0</a>
  (2026-05-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>add support for enterprise-level GitHub Apps (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/263">#263</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/952a2a7073df6bfa5f49bc469ec895b6ec1acea4">952a2a7</a>)</li>
  <li>support full repository names in <code>repositories</code> input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/372">#372</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/85eb8dd41472213aed25d1a126460e0069138ab6">85eb8dd</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump <code>@​actions/core</code> from 3.0.0
  to 3.0.1 in the production-dependencies group (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/364">#364</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/43e5c345bfd4d4f3ecea019ad0042001a09dd857">43e5c34</a>)</li>
  <li>validate private-key input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/376">#376</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/f24bbd89643991c0de27ae823c01791b2c6bafdd">f24bbd8</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/f418cff399f7aef4c2f0ad47e25ca7a6abbdd6fc"><code>f418cff</code></a>
  chore(main): release 3.4.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/415">#415</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/09c1ab7079f14af5f0d64c9325739c49a8541f56"><code>09c1ab7</code></a>
  feat: bump actions/setup-node from 6 to 7 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/410">#410</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/01b8009bd6d3d8cce95b612d9793c2b76ef46ee3"><code>01b8009</code></a>
  test: strip ANSI escape codes from snapshot output (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/412">#412</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/e05686484174f08cd73b6c67321c77132a9ace91"><code>e056864</code></a>
  build(deps-dev): bump undici from 8.12.3 to 8.12.4 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/416">#416</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/679345a20e2e07130130e6cf0301b9e897f18cd5"><code>679345a</code></a>
  feat: bump actions/stale from 10 to 11 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/409">#409</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/660c44c8ce22207448fbba2730cd2913052c9de3"><code>660c44c</code></a>
  feat: bump stefanzweifel/git-auto-commit-action from 7.2.0 to 7.2.1 in
  the gi...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/18e9994c8d13ac7c7e2bbcc3355a1a4f31d30de7"><code>18e9994</code></a>
  fix(deps): bump undici (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/406">#406</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/create-github-app-token/compare/64ab729a6294000f5aa4a4bc0b73d1f32bc45510...f418cff399f7aef4c2f0ad47e25ca7a6abbdd6fc">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=3.3.0&new-version=3.4.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

