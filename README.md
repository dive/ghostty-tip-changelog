> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 23, 2026 at 09:34 UTC.

## April 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24814161245), [2](https://github.com/ghostty-org/ghostty/actions/runs/24812939117), [3](https://github.com/ghostty-org/ghostty/actions/runs/24810009508)  
Summary: 3 runs • 11 commits • 3 authors

### Changes

- [`8f49ed6`](https://github.com/ghostty-org/ghostty/commit/8f49ed6c32abfb58209bc8c7526ef83bd98414ce) ci: add GNU-ABI Windows library build job ([@mattn](https://github.com/mattn))
  ```text
  The existing `build-libghostty-vt-windows` job builds libghostty-vt
  with the MSVC ABI. The Win32 apprt (discussion #2563) will target
  the GNU ABI, so add a parallel job that exercises the GNU-ABI path
  to catch bitrot.
  
  The job runs `zig build -Dtarget=native-native-gnu -Dapp-runtime=none`
  which produces ghostty-vt.dll and ghostty-internal.dll without
  requiring a platform-specific apprt.
  ```
- [`e88c6c0`](https://github.com/ghostty-org/ghostty/commit/e88c6c099152dd6d2d7e517516e1f3c183c152f7) ci: add GNU-ABI Windows library build job ([#12383](https://github.com/ghostty-org/ghostty/issues/12383)) ([@jcollie](https://github.com/jcollie))
  ```text
  Adds a new CI job `build-libghostty-windows-gnu` that exercises the
  GNU-ABI Windows library build path. The existing
  `build-libghostty-vt-windows` job covers the MSVC ABI; with the recent
  fixes (#12373 / #12381 / #12382) the GNU path is now viable, and this
  job catches regressions before the upcoming Win32 apprt (discussion
  #2563) starts to depend on it.
  
  Named `build-libghostty-windows-gnu` rather than following the
  `build-libghostty-vt-*` convention because this job also builds
  `ghostty-internal.dll`, not just libghostty-vt. Happy to rename if you
  prefer a different convention.
  
  Part of the Win32 apprt upstreaming series (see discussion #2563 /
  mattn/ghostty#1).
  ```
- [`ce3c319`](https://github.com/ghostty-org/ghostty/commit/ce3c319ab1e93f1b5a3808c4dcc963a91d77a629) build(deps): bump cachix/install-nix-action from 31.10.4 to 31.10.5 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.4 to 31.10.5.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/616559265b40713947b9c190a8ff4b507b5df49b...ab739621df7a23f52766f9ccc97f38da6b7af14f)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.5
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`83a3e5a`](https://github.com/ghostty-org/ghostty/commit/83a3e5aba719bd8bb8c3141bad2e1cfb4a1dd9df) windows: disable C++ ubsan regardless of ABI ([@mattn](https://github.com/mattn))
  ```text
  The existing `-fno-sanitize=undefined` flag was gated on `abi == .msvc`
  to avoid undefined `__ubsan_handle_*` references from simdutf/highway.
  The same linker error reproduces on Windows GNU ABI for the same
  reason: the Zig-bundled libraries don't provide a matching UBSan
  runtime for these C/C++ objects in our build configurations.
  
  Widen the condition to `os.tag == .windows` so both MSVC and GNU
  Windows targets skip ubsan for these C++ deps.
  ```
- [`5c4ab6c`](https://github.com/ghostty-org/ghostty/commit/5c4ab6c0de60def3ff6b0ca49f367fdf36abd50a) build: pass zig exe path to combine_archives ([@mattn](https://github.com/mattn))
  ```text
  `combine_archives` spawns `zig ar -M` to combine static archives via
  an MRI script. It hard-coded the command name `"zig"` and relied on
  the binary being on `PATH`, which fails on Windows when the build is
  driven by an absolute zig.exe path (common in CI and in Scoop/winget
  installs where PATH isn't populated at build time). The failure
  surfaces as `error: FileNotFound` from `Child.spawn`.
  
  Pass `b.graph.zig_exe` as the first argument so the tool always uses
  the exact zig binary that is driving the build, matching how other
  build tools in this repo spawn zig subcommands.
  ```
- [`b526175`](https://github.com/ghostty-org/ghostty/commit/b52617578208f427cf229819cc129160997979b8) build(deps): bump cachix/install-nix-action from 31.10.4 to 31.10.5 ([#12380](https://github.com/ghostty-org/ghostty/issues/12380)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.4 to 31.10.5.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.5</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.5 -&gt; 2.34.6 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/274">cachix/install-nix-action#274</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31...v31.10.5">https://github.com/cachix/install-nix-action/compare/v31...v31.10.5</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/ab739621df7a23f52766f9ccc97f38da6b7af14f"><code>ab73962</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/274">#274</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/41e4d4a5ae81b05c01f2e2e77bfbf2fe219b53c1"><code>41e4d4a</code></a>
  nix: 2.34.5 -&gt; 2.34.6</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/616559265b40713947b9c190a8ff4b507b5df49b...ab739621df7a23f52766f9ccc97f38da6b7af14f">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.4&new-version=31.10.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`1979b1c`](https://github.com/ghostty-org/ghostty/commit/1979b1c8d6903faeecf7e28ab0fe65a37f173179) build: pass zig exe path to combine_archives ([#12382](https://github.com/ghostty-org/ghostty/issues/12382)) ([@jcollie](https://github.com/jcollie))
  ```text
  `combine_archives` spawns `zig ar -M`, hard-coding the command name
  `"zig"` and relying on the binary being on `PATH`. On Windows when the
  build is driven by an absolute zig.exe path (common in CI and
  Scoop/winget installs), this surfaces as `error: FileNotFound`.
  
  Pass `b.graph.zig_exe` explicitly so the tool always uses the exact zig
  binary driving the build, matching how other build tools in this repo
  spawn zig subcommands.
  
  Part of the Win32 apprt upstreaming series (see discussion #2563 /
  mattn/ghostty#1).
  ```
- [`db210e4`](https://github.com/ghostty-org/ghostty/commit/db210e4d7f1c63c61f5b7afa131188663486f6b6) windows: disable C++ ubsan regardless of ABI ([#12381](https://github.com/ghostty-org/ghostty/issues/12381)) ([@jcollie](https://github.com/jcollie))
  ```text
  Widens the existing `-fno-sanitize=undefined` gate from `abi == .msvc`
  to `os.tag == .windows`. The same undefined `__ubsan_handle_*` link
  errors from simdutf/highway also reproduce on Windows GNU ABI, and the
  fix is identical.
  
  Part of the Win32 apprt upstreaming series (see discussion #2563 /
  mattn/ghostty#1).
  ```
- [`2d4d47e`](https://github.com/ghostty-org/ghostty/commit/2d4d47ed82bbfb560f8a7fe42c7aa043d8ebf90b) windows: provide DllMain stub for non-MSVC ABI ([@mattn](https://github.com/mattn))
  ```text
  Part of preparation for upstreaming a Win32 application runtime
  (see discussion #2563). This is one of three small build-related
  fixes that unblock the Windows GNU-ABI library build.
  
  When targeting Windows with GNU ABI, the existing `DllMain` declaration
  falls through to `void` (a type), which Zig stdlib's `start.zig` then
  attempts to call as a function via `root.DllMain(...)` - producing the
  compile error "type 'type' not a function".
  
  Restructure the conditional so that:
    - non-Windows builds keep `DllMain = void`
    - Windows + MSVC keeps the existing CRT-init handler (unchanged)
    - Windows + non-MSVC gets a no-op `BOOL` handler
  
  This unblocks `zig build -Dtarget=native-native-gnu -Dapp-runtime=none`
  on Windows.
  ```
- [`5a84afe`](https://github.com/ghostty-org/ghostty/commit/5a84afef29e2b46cb20db78278f46926bcc61a5d) address review: collapse DllMain into a single struct ([@mattn](https://github.com/mattn))
  ```text
  Per review feedback (#12373), fold the nested `if/else if/else` into a
  single Windows-gated struct whose handler picks up the abi difference
  via a comptime check. This removes the duplicated `const BOOL = ...`
  block that the two per-abi structs shared.
  ```
- [`880a599`](https://github.com/ghostty-org/ghostty/commit/880a599d66c0678c9d1709097b38beb5c0730175) windows: provide DllMain stub for non-MSVC ABI ([#12373](https://github.com/ghostty-org/ghostty/issues/12373)) ([@jcollie](https://github.com/jcollie))
  ```text
  Part of preparation for adding a Win32 application runtime (discussion
  #2563). One of three small, independent build fixes that together
  unblock the Windows GNU-ABI library build.
  
  On Windows with non-MSVC ABI, `pub const DllMain` resolved to `void` (a
  type), and Zig's stdlib `start.zig` then tried to call it as a function
  via `root.DllMain(...)`, failing to compile with "type 'type' not a
  function".
  
  This restructures the conditional so MSVC keeps its existing CRT-init
  handler unchanged, non-MSVC Windows gets a no-op `BOOL` handler, and
  non-Windows continues to resolve to `void`.
  
  Verified: `zig build -Dtarget=native-native-gnu -Dapp-runtime=none
  [-Doptimize=ReleaseSafe]` now builds cleanly on Windows.
  ```

## April 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24788531835), [2](https://github.com/ghostty-org/ghostty/actions/runs/24788358243)  
Summary: 2 runs • 4 commits • 4 authors

### Changes

- [`2a3d93f`](https://github.com/ghostty-org/ghostty/commit/2a3d93f77ba42ebb099bc7d686e65f6978ff4a94) Update VOUCHED list ([#12374](https://github.com/ghostty-org/ghostty/issues/12374)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12168#discussioncomment-16672511)
  from @jcollie.
  
  Vouch: @mattn
  ```
- [`38d6451`](https://github.com/ghostty-org/ghostty/commit/38d6451d73f342877db2d83651e4de60573a57ad) libghostty-vt: emit resolved include/lib dirs in .pc files ([@domenkozar](https://github.com/domenkozar))
  ```text
  `${prefix}/include` and `${prefix}/lib` are wrong under split-prefix installs (e.g. Nix multi-output).
  Use `b.h_dir` / `b.lib_dir` instead and drop the unneeded Nix postInstall/postFixup hooks.
  ```
- [`733abbc`](https://github.com/ghostty-org/ghostty/commit/733abbcc391f99c4bea3b91058486fe038ccfae2) libghostty-vt: revert .pc changes and use Nix to fix them ([@sandydoo](https://github.com/sandydoo))
  ```text
  Keeps the .pc files templated and instead uses Nix to rewrite the libdir for the static library.
  ```
- [`98b7ad4`](https://github.com/ghostty-org/ghostty/commit/98b7ad4c49607803376e46714417d43533f7bcb8) libghostty-vt: fix broken dynamic linking with pkg-config ([#12364](https://github.com/ghostty-org/ghostty/issues/12364)) ([@jcollie](https://github.com/jcollie))
  ```text
  ~`${prefix}/include` and `${prefix}/lib` are incorrect under
  split-prefix installs (e.g. Nix multi-output). Use `b.h_dir` /
  `b.lib_dir` instead and drop the unneeded Nix postInstall/postFixup
  hooks.~
  
  Refactors the libghostty-vt derivation to:
  
  - fix `libdir` pointing to the wrong output in the pkg-config files.
  This would throw a missing library error at runtime.
  - reduce the amount of manual copying, linking, and patching of files.
  
  An earlier version of this PR used the zig compiler + `.pc` files to do
  this. People pointed out concerns, so I came up with a simpler solution.
  
  Claude Code was used to debug and write an initial fix. Final changes
  rewritten and simplified by me. No AI was used to write comments,
  descriptions, etc.
  ```

## April 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24736321995), [2](https://github.com/ghostty-org/ghostty/actions/runs/24734679646), [3](https://github.com/ghostty-org/ghostty/actions/runs/24729914540), [4](https://github.com/ghostty-org/ghostty/actions/runs/24703080862)  
Summary: 4 runs • 12 commits • 7 authors

### Changes

- [`d2f8602`](https://github.com/ghostty-org/ghostty/commit/d2f86028bb2104f1582d40c8dfc1feaa3fe383c4) Use patched Zig 0.15.2 on macOS to avoid Xcode 26.4 issue ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates our Nix flake to use the Homebrew bottled Zig 0.15.2 which
  contains a patch to work around the issue with Zig 0.15.x and Xcode
  26.4.
  ```
- [`6e0b031`](https://github.com/ghostty-org/ghostty/commit/6e0b0311e49243fb0f04c96df1fc9e79ab5c710d) Use patched Zig 0.15.2 on macOS to avoid Xcode 26.4 issue ([#12363](https://github.com/ghostty-org/ghostty/issues/12363)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates our Nix flake to use the Homebrew bottled Zig 0.15.2 which
  contains a patch to work around the issue with Zig 0.15.x and Xcode
  26.4.
  ```
- [`9bad936`](https://github.com/ghostty-org/ghostty/commit/9bad9365b008633292ac271cd804a32459288686) macOS: open preferred config if exists ([@bo2themax](https://github.com/bo2themax))
- [`22f9233`](https://github.com/ghostty-org/ghostty/commit/22f9233a0f7b85747483ce713411c67be4643d8f) contributing: don't encourage opening an issue ([@trag1c](https://github.com/trag1c))
- [`cb518e6`](https://github.com/ghostty-org/ghostty/commit/cb518e6afdef4481fc385e153a054a75555b72ec) ci: use a custom template for ghostty-vouch issue comments ([@trag1c](https://github.com/trag1c))
- [`e9a196c`](https://github.com/ghostty-org/ghostty/commit/e9a196c67bf5377be1787feb562ecadb5f630a33) build(xcframework): exclude libghostty-vt headers from GhosttyKit ([@claude](https://github.com/claude))
  ```text
  The GhosttyKit xcframework previously shipped the entire include/
  directory, which pulled in the libghostty-vt headers under
  include/ghostty/. Because those headers are not referenced from the
  ghostty.h umbrella, Clang's module system emitted "umbrella header for
  module 'GhosttyKit' does not include header 'ghostty/vt/*.h'" warnings
  in Xcode builds.
  
  Stage only ghostty.h and module.modulemap via addWriteFiles so the
  xcframework Headers directory contains exactly the GhosttyKit API,
  mirroring the pattern used in GhosttyLibVt.xcframework.
  ```
- [`a6105b3`](https://github.com/ghostty-org/ghostty/commit/a6105b3b10bb388cb724667dd875d6ae9362ce53) build(xcframework): exclude libghostty-vt headers from GhosttyKit ([#12360](https://github.com/ghostty-org/ghostty/issues/12360)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyKit xcframework previously shipped the entire include/
  directory, which pulled in the libghostty-vt headers under
  include/ghostty/. Because those headers are not referenced from the
  ghostty.h umbrella, Clang's module system emitted "umbrella header for
  module 'GhosttyKit' does not include header 'ghostty/vt/*.h'" warnings
  in Xcode builds.
  
  Stage only ghostty.h and module.modulemap via addWriteFiles so the
  xcframework Headers directory contains exactly the GhosttyKit API,
  mirroring the pattern used in GhosttyLibVt.xcframework.
  
  ## AI disclosure
  
  Claude made the changes (including the commit message), I reviewed and
  tested them.
  ```
- [`95c61e2`](https://github.com/ghostty-org/ghostty/commit/95c61e2880b88c18d7a10b0b3329b9f97e8c3946) docs,ci: clarify that users can never open issues ([#12335](https://github.com/ghostty-org/ghostty/issues/12335)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I removed the entire paragraph in CONTRIBUTING.md because the "Quick
  Guide" section explains it all better already.
  ```
- [`62fdd88`](https://github.com/ghostty-org/ghostty/commit/62fdd885e017b779dce9407f98c2e7d65cfb3d8e) macOS: open preferred config if exists ([#12321](https://github.com/ghostty-org/ghostty/issues/12321)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This helps developers like me to use a separate config for debugging
  (which is already supported by the environment variable
  `GHOSTTY_CONFIG_PATH`).
  
  I can already use the local scheme to load a debugging config file, but
  when opening the config file through Ghostty, it will still open the
  default config.
  
  This changes doesn't affect the release build, since `configPath` is
  only set in the DEBUG build.
  ```
- [`58af471`](https://github.com/ghostty-org/ghostty/commit/58af471a0164153eac4287a7188761db0711cbf3) Update VOUCHED list ([#12362](https://github.com/ghostty-org/ghostty/issues/12362)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12361#discussioncomment-16656763)
  from @jcollie.
  
  Vouch: @sandydoo
  ```
- [`5eeb4d9`](https://github.com/ghostty-org/ghostty/commit/5eeb4d9d687d52b8b0650857afd3601790ca7ad8) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.2 to 1.4.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.4.2 to 1.4.3.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9...15799a6b54e5765f85b2aac25b3f0df43ed571c0)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.4.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`3a1482d`](https://github.com/ghostty-org/ghostty/commit/3a1482d1a2794801b4ac9a168da21a4d7dc0cfda) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.2 to 1.4.3 ([#12355](https://github.com/ghostty-org/ghostty/issues/12355)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.4.2 to 1.4.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.4.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>
  <p>Add npm mode by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/118">namespacelabs/nscloud-cache-action#118</a></p>
  </li>
  <li>
  <p>Use repeated --path arguments instead of comma-separated values by <a
  href="https://github.com/annervisser"><code>@​annervisser</code></a> in
  <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/112">namespacelabs/nscloud-cache-action#112</a></p>
  </li>
  <li>
  <p>Bump the minor-actions-dependencies group across 1 directory with 7
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/115">namespacelabs/nscloud-cache-action#115</a></p>
  </li>
  <li>
  <p>Add manual-paths mode test with multiple paths by <a
  href="https://github.com/annervisser"><code>@​annervisser</code></a> in
  <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/111">namespacelabs/nscloud-cache-action#111</a></p>
  </li>
  <li>
  <p>Bump the minor-npm-dependencies group across 1 directory with 6
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/116">namespacelabs/nscloud-cache-action#116</a></p>
  </li>
  <li>
  <p>Add major-actions-dependencies Dependabot group by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/119">namespacelabs/nscloud-cache-action#119</a></p>
  </li>
  <li>
  <p>Upgrade <code>@​namespacelabs/actions-toolkit</code> to 0.3.0 by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/125">namespacelabs/nscloud-cache-action#125</a></p>
  </li>
  <li>
  <p>Bump the major-actions-dependencies group across 1 directory with 4
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/123">namespacelabs/nscloud-cache-action#123</a></p>
  </li>
  <li>
  <p>Bump the minor-actions-dependencies group across 1 directory with 3
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/122">namespacelabs/nscloud-cache-action#122</a></p>
  </li>
  <li>
  <p>Bump eslint from 9.39.4 to 10.2.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/121">namespacelabs/nscloud-cache-action#121</a></p>
  </li>
  <li>
  <p>Bump typescript from 5.9.3 to 6.0.2 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/120">namespacelabs/nscloud-cache-action#120</a></p>
  </li>
  <li>
  <p>Bump <code>@​eslint/js</code> from 9.39.4 to 10.0.1 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/102">namespacelabs/nscloud-cache-action#102</a></p>
  </li>
  <li>
  <p>Bump typescript from 6.0.2 to 6.0.3 in the minor-npm-dependencies
  group by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/126">namespacelabs/nscloud-cache-action#126</a></p>
  </li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.4.3">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.4.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/15799a6b54e5765f85b2aac25b3f0df43ed571c0"><code>15799a6</code></a>
  Bump typescript from 6.0.2 to 6.0.3 in the minor-npm-dependencies group
  (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/126">#126</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/a74ba09be4eecba86290920825b0b74efab518e2"><code>a74ba09</code></a>
  Add npm mode test (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/118">#118</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/3accca63b228cb1a9847e533466b497d5422da59"><code>3accca6</code></a>
  Bump <code>@​eslint/js</code> from 9.39.2 to 10.0.1 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/102">#102</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/320beceb2e4cff95a23363a5c81fd0d0326ba5d6"><code>320bece</code></a>
  Bump typescript from 5.9.3 to 6.0.2 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/120">#120</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/7b579df1e212c05a2e3ad697a5d9780c934e0cb3"><code>7b579df</code></a>
  Bump eslint from 9.39.4 to 10.2.0 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/121">#121</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/0170534ed677e581623af217e966496a2d96699a"><code>0170534</code></a>
  Bump the minor-actions-dependencies group with 3 updates (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/122">#122</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/04d1d76ca05cb8ce5c021032972983806b0a8c4c"><code>04d1d76</code></a>
  Bump the major-actions-dependencies group across 1 directory with 4
  updates (...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/0496385e4a2a0ba41f6ad494948696fa90c60f72"><code>0496385</code></a>
  Upgrade <code>@​namespacelabs/actions-toolkit</code> to 0.3.0 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/125">#125</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/e14531ae78967dc1dc2ba26fdc3b6d461dcdb525"><code>e14531a</code></a>
  Add major-actions-dependencies Dependabot group (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/119">#119</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/1f34f9763c6fa1cb6986aacb3c0211a87fdfa87a"><code>1f34f97</code></a>
  Bump the minor-npm-dependencies group across 1 directory with 6 updates
  (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/116">#116</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9...15799a6b54e5765f85b2aac25b3f0df43ed571c0">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.4.2&new-version=1.4.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## April 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24685410722), [2](https://github.com/ghostty-org/ghostty/actions/runs/24678140846)  
Summary: 2 runs • 10 commits • 4 authors

### Changes

- [`2db58a6`](https://github.com/ghostty-org/ghostty/commit/2db58a63feb7d052985d9c46039f03bf58cef3c7) update zon2nix ([@jcollie](https://github.com/jcollie))
- [`c7a7307`](https://github.com/ghostty-org/ghostty/commit/c7a73076e9c3ebb395faa51d5f92f49327a62df5) macOS: fix App Icon update in Finders ([@bo2themax](https://github.com/bo2themax))
  ```text
  Looks like  `NSWorkspace.shared.setIcon` can only be called from the main App, DockTilePlugin is sandboxed and doesn't have the permission to `file-write-finderinfo`.
  
  It works fine in debug, but not in release. This fixes #11489, #11290
  ```
- [`61363e8`](https://github.com/ghostty-org/ghostty/commit/61363e80d1f235bbacb7ebcccf418f24a3fabadd) macOS: fix App Icon update in Finder ([#12344](https://github.com/ghostty-org/ghostty/issues/12344)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Looks like `NSWorkspace.shared.setIcon` can only be called from the main
  App, DockTilePlugin is sandboxed and doesn't have the permission to
  `file-write-finderinfo`.
  
  <img width="1186" height="144" alt="image"
  src="https://github.com/user-attachments/assets/e5ea4f1c-718c-493a-bda2-32787881881e"
  />
  
  
  It works fine in debug, but not in release. This fixes #11489
  ```
- [`c3c8572`](https://github.com/ghostty-org/ghostty/commit/c3c8572f7fd6309645bf70f74958691c6294bef0) update zon2nix ([#12337](https://github.com/ghostty-org/ghostty/issues/12337)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds better Zig 0.16 compatibility.
  ```
- [`9a90022`](https://github.com/ghostty-org/ghostty/commit/9a9002202b8767e6e99c2bb48fad09fc0ae02870) macos: add pid and tty properties to AppleScript terminal class ([@TweedBeetle](https://github.com/TweedBeetle))
  ```text
  Expose the foreground process PID and TTY device path as read-only properties on the AppleScript terminal class and App Intents TerminalEntity. This enables reliable process-to-terminal mapping for automation tools when multiple terminals share the same CWD.
  
  Closes #11592
  Closes #10756
  
  Session: 019d341c-a165-7843-a2f7-2f426114cf17
  ```
- [`8302740`](https://github.com/ghostty-org/ghostty/commit/83027407e66e47248a4bdf9a82b438764caf43d5) terminal: fix memory leak that could happen with invalid Kitty image cmd ([@mitchellh](https://github.com/mitchellh))
- [`0509f00`](https://github.com/ghostty-org/ghostty/commit/0509f00ad2f0e56dc4c0807d2e22f80baf1688f9) terminal/apc: introduce a max_bytes parameter to prevent DoS ([@mitchellh](https://github.com/mitchellh))
- [`0069e28`](https://github.com/ghostty-org/ghostty/commit/0069e28cc6f681797f1424317f46d52da9d9e635) libghostty: expose the APC max byte limits ([@mitchellh](https://github.com/mitchellh))
- [`4446dba`](https://github.com/ghostty-org/ghostty/commit/4446dbae3360f87ed8ac577f7c5d04f36a570ed0) Misc APC improvements ([#12349](https://github.com/ghostty-org/ghostty/issues/12349)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  * Fix a memory leak when invalid Kitty graphics data is sent via APC
  (this is the only commit for backporting to 1.3.2)
  * Add `max_bytes` to limit size of buffered APC data by protocol to
  prevent DoS, default to reasonable values
  * libghostty: expose max bytes APC options
  ```
- [`afdae72`](https://github.com/ghostty-org/ghostty/commit/afdae7293abfdf5daa684dc50c35420b61a1d575) macos: add pid and tty properties to AppleScript terminal and App Intents TerminalEntity ([#11922](https://github.com/ghostty-org/ghostty/issues/11922)) ([@bo2themax](https://github.com/bo2themax))

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

