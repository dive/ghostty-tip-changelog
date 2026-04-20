> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 20, 2026 at 15:30 UTC.

## April 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24640880436), [2](https://github.com/ghostty-org/ghostty/actions/runs/24639757175), [3](https://github.com/ghostty-org/ghostty/actions/runs/24639013884), [4](https://github.com/ghostty-org/ghostty/actions/runs/24632124947), [5](https://github.com/ghostty-org/ghostty/actions/runs/24631013589)  
Summary: 5 runs • 17 commits • 7 authors

### Changes

- [`adb0d79`](https://github.com/ghostty-org/ghostty/commit/adb0d793af755841f3dcea8c5e466ea9b8295e11) android: Avoid referencing POSIX shared memory functions ([@fornwall](https://github.com/fornwall))
  ```text
  Stop trying to use POSIX shared memory functions such as
  `shm_open` on Android as it's unsupported and the platform libc does not
  have those symbols.
  
  This avoids an error such as the below when trying to use
  `libghostty-vt` on Android:
  
  > dlopen failed: cannot locate symbol "shm_open" referenced by [..]
  ```
- [`dcc39dc`](https://github.com/ghostty-org/ghostty/commit/dcc39dcd401975ee77a642fa15ba7bb9f6d85b96) android: Avoid referencing POSIX shared memory functions ([#12341](https://github.com/ghostty-org/ghostty/issues/12341)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Stop trying to use POSIX shared memory functions such as `shm_open` on
  Android as it's unsupported and the platform libc does not have those
  symbols.
  
  This avoids an error such as the below when trying to use
  `libghostty-vt` on Android:
  
  > dlopen failed: cannot locate symbol "shm_open" referenced by [..]
  ```
- [`d69d937`](https://github.com/ghostty-org/ghostty/commit/d69d937a93750e64d1a4396715f81e74fa25aefe) Update VOUCHED list ([#12340](https://github.com/ghostty-org/ghostty/issues/12340)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12339#discussioncomment-16627477)
  from @jcollie.
  
  Vouch: @fornwall
  ```
- [`9cbca54`](https://github.com/ghostty-org/ghostty/commit/9cbca54597a21fae7d6ff9b80d9796d71a2dfb4e) Fix typo + improve fluency in README_TRANSLATORS § Viewing translations. ([@00-kat](https://github.com/00-kat))
- [`8a6c664`](https://github.com/ghostty-org/ghostty/commit/8a6c664686f57100f456bad35b08bc323f59184e) Fix typo in i18n_locales.zig. ([@00-kat](https://github.com/00-kat))
- [`49cd2ba`](https://github.com/ghostty-org/ghostty/commit/49cd2ba80bdb28ca8a56247712ed53c0b9f12669) Mark i18n_locales.zig as owned by ghostty-org/localization/manager. ([@00-kat](https://github.com/00-kat))
- [`2e33589`](https://github.com/ghostty-org/ghostty/commit/2e33589e23acb5f7e24f74ea384225b67485d3e6) Avoid marking files as owned by ghostty-org/localization. ([@00-kat](https://github.com/00-kat))
  ```text
  That team and its children have a very large number of members, so
  requests for review from them would make for a mass ping.
  ```
- [`ed29fd5`](https://github.com/ghostty-org/ghostty/commit/ed29fd56ddb45522bc151ebff3a9576bc5a68931) Translation documentation-related typos + CODEOWNERS update ([#12336](https://github.com/ghostty-org/ghostty/issues/12336)) ([@00-kat](https://github.com/00-kat))
- [`4f3a9cb`](https://github.com/ghostty-org/ghostty/commit/4f3a9cb0c6ce501a69d32a38e200812070b08d7e) i18n: add Belarusian translation (be) (illia krauchanka)
- [`ff9ca55`](https://github.com/ghostty-org/ghostty/commit/ff9ca55b58c7728f031af062b46b07bdf6cc83c3) i18n: fix terminology in Belarusian translation (be) (illia krauchanka)
- [`3ee0b0a`](https://github.com/ghostty-org/ghostty/commit/3ee0b0a77b5c8a317f3075e28d022af3098b66c0) i18n: fix gender agreement for match translations (be) (illia krauchanka)
- [`4381153`](https://github.com/ghostty-org/ghostty/commit/43811534b9e2ad5017a9c7365f3269260a356cb9) i18n: replace змесціва with змест (be) (illia krauchanka)
- [`053dee8`](https://github.com/ghostty-org/ghostty/commit/053dee8db23830ca03fb62af976f842dccceaa91) i18n: replace гартаць with пракручваць (be) (illia krauchanka)
- [`f370099`](https://github.com/ghostty-org/ghostty/commit/f370099d34f8ae8295be1a1dffce88fb80f02971) i18n: address review feedback (be) (Illia Krauchanka)
- [`28b7ef1`](https://github.com/ghostty-org/ghostty/commit/28b7ef12c338cba5dbb640b41b25a4478c612cf2) i18n: add Belarusian translation (be) ([#12284](https://github.com/ghostty-org/ghostty/issues/12284)) ([@00-kat](https://github.com/00-kat))
  ```text
  This PR adds Belarusian (be) language support to Ghostty.
  
  ## Changes
  
  - `po/be.po` — new Belarusian translation file (80 strings)
  - `src/os/i18n_locales.zig` — added `be` locale
  - `CODEOWNERS` — added `/po/be.po @ghostty-org/be_BY`
  
  ## Notes
  
  Terminology was cross-referenced with:
  - KDE Belarusian translations (l10n.kde.org)
  - qBittorrent Belarusian translation
  - far2l Belarusian translation
  - Ubuntu Belarusian Translators Dictionary
  ```
- [`5939b8c`](https://github.com/ghostty-org/ghostty/commit/5939b8c1be511020b5ec46c73509dc9d29a964a1) macOS: fix 12266 by using the correct coordinates for the hitTest ([@bo2themax](https://github.com/bo2themax))
  ```text
  Regression of #11872
  ```
- [`7a3e3dc`](https://github.com/ghostty-org/ghostty/commit/7a3e3dc8d20b7e287cc2b2b8e023c89f44879721) macOS: fix [#12266](https://github.com/ghostty-org/ghostty/issues/12266) by using the correct coordinates for the hitTest ([#12322](https://github.com/ghostty-org/ghostty/issues/12322)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes #12266, regression of #11872.
  ```

## April 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24546719001)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`b7d0be8`](https://github.com/ghostty-org/ghostty/commit/b7d0be8e74c471971e0d26fdd66614b44ae5af22) macOS: move KeyStateIndicator on top of exit bar ([@bo2themax](https://github.com/bo2themax))
- [`ca7516b`](https://github.com/ghostty-org/ghostty/commit/ca7516bea60190ee2e9a4f9182b61d318d107c6e) macOS: move KeyStateIndicator on top of exit bar ([#12282](https://github.com/ghostty-org/ghostty/issues/12282)) ([@mitchellh](https://github.com/mitchellh))

## April 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24480459490), [2](https://github.com/ghostty-org/ghostty/actions/runs/24479115337), [3](https://github.com/ghostty-org/ghostty/actions/runs/24472495002)  
Summary: 3 runs • 11 commits • 4 authors

### Changes

- [`9e080c5`](https://github.com/ghostty-org/ghostty/commit/9e080c5a403475dcbee93c40eeb22cf6f92121f4) Update VOUCHED list ([#12302](https://github.com/ghostty-org/ghostty/issues/12302)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12301#issuecomment-4255856979)
  from @trag1c.
  
  Vouch: @bleikurr
  ```
- [`858e856`](https://github.com/ghostty-org/ghostty/commit/858e856e2e1c4572585f6e043876d7d2f0ef79b4) macOS: fix shortcuts not showing on menu item for `scroll_to_selection` and `search_selection` ([@bo2themax](https://github.com/bo2themax))
  ```text
  Incorrect link after 9b6a3be99339bcefcc49b7791b7b9761d24e6093 and 7d0157e69a7b8082b4c56baa466304768f68cbc6
  ```
- [`815ccb0`](https://github.com/ghostty-org/ghostty/commit/815ccb060b1f983272dab86af6bacb156dfcbfd9) terminal: fix viewport pin during resize reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Maybe related to #12298?
  
  When Screen resize forwards the active cursor into PageList reflow, a
  history-pinned viewport can be remapped into the active area before the
  preserved-cursor grow step finishes. The old code kept treating that
  viewport as a history pin during the intermediate grow calls, which left
  too few rows beneath the pin and tripped the viewport integrity checks.
  
  Fix this by normalizing the viewport back to active as soon as reflow
  moves the pinned row into the active area. Add a Screen-level regression
  test that exercises the full resize path with bounded scrollback and
  wrapped rows, and document the setup so the unwrap and viewport
  transition are clear.
  ```
- [`551bf0a`](https://github.com/ghostty-org/ghostty/commit/551bf0af3fab6ff8b7567fc77b53698a944fce60) terminal: fix viewport pin during resize reflow ([#12300](https://github.com/ghostty-org/ghostty/issues/12300)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Maybe related to #12298?
  
  When Screen resize forwards the active cursor into PageList reflow, a
  history-pinned viewport can be remapped into the active area before the
  preserved-cursor grow step finishes. The old code kept treating that
  viewport as a history pin during the intermediate grow calls, which left
  too few rows beneath the pin and tripped the viewport integrity checks.
  
  Fix this by normalizing the viewport back to active as soon as reflow
  moves the pinned row into the active area. Add a Screen-level regression
  test that exercises the full resize path with bounded scrollback and
  wrapped rows, and document the setup so the unwrap and viewport
  transition are clear.
  ```
- [`d85051a`](https://github.com/ghostty-org/ghostty/commit/d85051a530690450148e558216d6f399ef978dfc) macOS: fix shortcuts not showing on menu item for `scroll_to_selection` and `search_selection` ([#12281](https://github.com/ghostty-org/ghostty/issues/12281)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  …
  
  Incorrect link after 9b6a3be99339bcefcc49b7791b7b9761d24e6093 and
  7d0157e69a7b8082b4c56baa466304768f68cbc6
  
  Reload following config and see the menu
  ```
  keybind = cmd+j=scroll_to_selection
  keybind = cmd+m=search_selection
  ```
  
  <img width="473" height="222" alt="image"
  src="https://github.com/user-attachments/assets/f92c6024-e7f4-496d-9aed-43103c21794d"
  />
  ````
- [`9c49c34`](https://github.com/ghostty-org/ghostty/commit/9c49c343569791071603d63138aa1a6f7d9dd2dc) benchmark: add AGENTS, improve UTF-8 synthetic data ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates our synthetic generator for UTF-8 to expose:
  
    - Flags to change 1/2/3/4-byte UTF-8 character distribution
    - Flags to have only printable characters so we can benchmark
      pure UTF-8 vs our control sequence finder.
    - Flags to have invalid characters so we can benchmark our error
      handling.
  
  This also adds an AGENTS.md to src/benchmark so agents can do the right
  thing more easily.
  ```
- [`29f92c0`](https://github.com/ghostty-org/ghostty/commit/29f92c0c8bb8428ccddb90efe095b114c3ff2950) benchmark: add AGENTS, improve UTF-8 synthetic data ([#12297](https://github.com/ghostty-org/ghostty/issues/12297)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates our synthetic generator for UTF-8 to expose:
  
    - Flags to change 1/2/3/4-byte UTF-8 character distribution
  - Flags to have only printable characters so we can benchmark pure UTF-8
  vs our control sequence finder.
  - Flags to have invalid characters so we can benchmark our error
  handling.
  
  This also adds an AGENTS.md to src/benchmark so agents can do the right
  thing more easily.
  
  These are necessary to robustly benchmark our libc++ removal PR.
  ```
- [`f53d3ab`](https://github.com/ghostty-org/ghostty/commit/f53d3ab8a35fe5a0cf077838e541bd450b09863a) nix: update to the latest zon2nix ([@jcollie](https://github.com/jcollie))
- [`efa8da6`](https://github.com/ghostty-org/ghostty/commit/efa8da6aea1e9cc099412c86405791bb0734ec0e) nix: update to the latest zon2nix ([#12299](https://github.com/ghostty-org/ghostty/issues/12299)) ([@mitchellh](https://github.com/mitchellh))
- [`e51de8b`](https://github.com/ghostty-org/ghostty/commit/e51de8b58faba2c851604b813e569f926910f522) libghostty: Remove all libc++ and libc++ ABI dependencies ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates simdutf to my fork which has a SIMDUTF_NO_LIBCXX option
  that removes all libc++ and libc++ ABI dependencies.
  
  From there, the hand-written simd code we have has been updated to also
  no longer use any libc++ features. Part of this required removing utfcpp
  since it depended on libc++ (`<iterator>`).
  
  libghostty-vt now only depends on libc.
  ```
- [`43a05dc`](https://github.com/ghostty-org/ghostty/commit/43a05dc968eda9bfa2196d66ba1819daf510b62a) libghostty: Remove all libc++ and libc++ ABI dependencies ([#12291](https://github.com/ghostty-org/ghostty/issues/12291)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates simdutf to my fork which has a SIMDUTF_NO_LIBCXX option
  that removes all libc++ and libc++ ABI dependencies. The plan is to open
  an upstream PR with this, but I want to verify it here first.
  
  From there, the hand-written simd code we have has been updated to also
  no longer use any libc++ features. Part of this required removing utfcpp
  since it depended on libc++ (`<iterator>`).
  
  libghostty-vt now only depends on libc.
  
  ## Benchmark Results
  
  | Corpus | Current `HEAD` median | `main` median | Delta vs `main` |
  Notes |
  | --- | ---: | ---: | ---: | --- |
  | `valid-mixed-1g-seed1.bin` | `9.245s` | `9.111s` | `1.5%` slower |
  Near tie; `main` remains slightly faster on fully valid input |
  | `malformed-mixed-1g-seed1-rate0.005.bin` | `9.251s` | `12.705s` |
  `37.3%` faster | Large improvement on malformed UTF-8 input |
  
  Approximate throughput from the medians:
  
  - Valid corpus: current `HEAD` `110.8 MiB/s`, `main` `112.4 MiB/s`
  - Malformed corpus: current `HEAD` `110.7 MiB/s`, `main` `80.6 MiB/s`
  ```

## April 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24422513385), [2](https://github.com/ghostty-org/ghostty/actions/runs/24404590083)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`49a43bf`](https://github.com/ghostty-org/ghostty/commit/49a43bf560322eac0ba5d30c20a8b212106e3883) Update VOUCHED list ([#12285](https://github.com/ghostty-org/ghostty/issues/12285)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12284#issuecomment-4247088526)
  from @trag1c.
  
  Vouch: @illiakrauchanka
  ```
- [`fe8a646`](https://github.com/ghostty-org/ghostty/commit/fe8a6464b94e7f11a3514627b8344442ab9e63c4) macOS: update MenuShortcutKey ([@bo2themax](https://github.com/bo2themax))
- [`6033c12`](https://github.com/ghostty-org/ghostty/commit/6033c12790aaf0e9e7cee44118aa8745c4dfaadd) macOS: reset menu shortcuts when its not updated ([@bo2themax](https://github.com/bo2themax))
- [`79a470d`](https://github.com/ghostty-org/ghostty/commit/79a470d9a3b0a2b2cde3e939f0cb25968a162183) macOS: refactor MenuShortcutManager ([#12271](https://github.com/ghostty-org/ghostty/issues/12271)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #11995
  
  Yet another small step to fix menu shortcut-related issues.
  
  1. Create `MenuShortcutKey` from `NSMenuItem` and `KeyboardShortcut`.
  2. Add `updateMenuShortcut` to update to Ghostty ones only.
  
  Doesn't contain any actual changes to pass previous test cases.
  ```

