> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 13, 2026 at 09:54 UTC.

## May 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25658156161), [2](https://github.com/ghostty-org/ghostty/actions/runs/25657875662)  
Summary: 2 runs • 3 commits • 1 authors

### Changes

- [`611525a`](https://github.com/ghostty-org/ghostty/commit/611525ac3f6cc3e2c63988ad8111d7ace093950e) Update VOUCHED list ([#12655](https://github.com/ghostty-org/ghostty/issues/12655)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12618#discussioncomment-16876561)
  from @pluiedev.
  
  Vouch: @thirstycrow
  ```
- [`64131dc`](https://github.com/ghostty-org/ghostty/commit/64131dcd413ef27147378e2139efe1d2d81e092a) Update VOUCHED list ([#12656](https://github.com/ghostty-org/ghostty/issues/12656)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12616#discussioncomment-16876564)
  from @pluiedev.
  
  Vouch: @00JCIV00
  ```
- [`4c68594`](https://github.com/ghostty-org/ghostty/commit/4c6859447cd794a96b79ae549d1e8e48a5c9874e) Update VOUCHED list ([#12654](https://github.com/ghostty-org/ghostty/issues/12654)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12650#discussioncomment-16876487)
  from @pluiedev.
  
  Vouch: @athaapa
  ```

## May 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25630689955)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`ce6a00b`](https://github.com/ghostty-org/ghostty/commit/ce6a00bfbfc7f0fed25e9385ac9100f7b4b0e098) Update VOUCHED list ([#12647](https://github.com/ghostty-org/ghostty/issues/12647)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12644#issuecomment-4415471290)
  from @jcollie.
  
  Denounce: @f1813483-netizen
  ```

## May 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25609668241), [2](https://github.com/ghostty-org/ghostty/actions/runs/25606064691), [3](https://github.com/ghostty-org/ghostty/actions/runs/25604916760)  
Summary: 3 runs • 8 commits • 5 authors

### Changes

- [`2b48045`](https://github.com/ghostty-org/ghostty/commit/2b480457316b3b21739d3ed26b301e456f5856c7) macos: simplify workingDirectory setter ([@jparise](https://github.com/jparise))
  ```text
  This is a minor improvement to the computed property's `set` logic: we
  can just use `.map {}` to unify the two optional paths.
  ```
- [`e3e9b51`](https://github.com/ghostty-org/ghostty/commit/e3e9b51b79c538c3f70a49e4dbda02ccb3cab731) macos: simplify workingDirectory setter ([#12639](https://github.com/ghostty-org/ghostty/issues/12639)) ([@jparise](https://github.com/jparise))
  ```text
  This is a minor improvement to the computed property's `set` logic: we
  can just use `.map {}` to unify the two optional paths.
  ```
- [`cbd43fd`](https://github.com/ghostty-org/ghostty/commit/cbd43fd4834a7969480866c037f8650ca0912a25) feature: add basque translation ([@erral](https://github.com/erral))
- [`afb8fc7`](https://github.com/ghostty-org/ghostty/commit/afb8fc7eb3042196b7e1d0fb5ec0eb0601efaf85) Update po/eu.po ([@erral](https://github.com/erral))
- [`ec145bc`](https://github.com/ghostty-org/ghostty/commit/ec145bca9f1b24df3c6c8321892e60fb68f05c3d) Fix translation errors in eu ([@erral](https://github.com/erral))
- [`a330ee9`](https://github.com/ghostty-org/ghostty/commit/a330ee93e8cb01844a4442eb692ac1769ab1d35d) i18n: add Basque (eu) translation ([#12544](https://github.com/ghostty-org/ghostty/issues/12544)) ([@00-kat](https://github.com/00-kat))
  ```text
  Same as with icelandic (#12301) we may be even fewer than them but let's
  have this translated into Basque.
  
  I also volunteer for the basque translation team.
  ```
- [`607152e`](https://github.com/ghostty-org/ghostty/commit/607152ec6d2487ab10fb1cf5de6e0519baf8a21b) macOS: normalize working directory paths with FilePath ([@bo2themax](https://github.com/bo2themax))
  ```text
  This fixes for nuShell when opening Ghostty via Finder service and Shortcuts, also makes path parsing more robust in AppleScript.
  ```
- [`4bd8fa1`](https://github.com/ghostty-org/ghostty/commit/4bd8fa1e3e7a9538ad0b2433c2ddabeaa051eedc) macOS: normalize working directory paths with FilePath ([#12614](https://github.com/ghostty-org/ghostty/issues/12614)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes for
  [Nushell](https://github.com/nushell/nushell/blob/f342d8acfa81bd9543bb38e3e08b1a93ecafe5d1/crates/nu-protocol/src/engine/engine_state.rs#L1012)
  when opening Ghostty via Finder service and Shortcuts, also makes path
  parsing more robust in AppleScript.
  
  <img width="976" height="690" alt="image"
  src="https://github.com/user-attachments/assets/d3c19481-39ce-4797-ba31-d431af16651d"
  />
  ```

## May 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25486122457)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`063ac3e`](https://github.com/ghostty-org/ghostty/commit/063ac3ecc5adae6360ae2044dc54e7a68c64f3a1) Update VOUCHED list ([#12613](https://github.com/ghostty-org/ghostty/issues/12613)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12612#issuecomment-4395645191)
  from @trag1c.
  
  Vouch: @raphamorim
  ```

