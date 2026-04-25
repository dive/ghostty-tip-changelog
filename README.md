> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 25, 2026 at 06:31 UTC.

## April 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24923989307)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`57b5e1e`](https://github.com/ghostty-org/ghostty/commit/57b5e1e2507cd65ab8197d39baa4ce2505185510) Update VOUCHED list ([#12425](https://github.com/ghostty-org/ghostty/issues/12425)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12308#discussioncomment-16709130)
  from @jcollie.
  
  Vouch: @alaviss
  ```

## April 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24914171209), [2](https://github.com/ghostty-org/ghostty/actions/runs/24911997879), [3](https://github.com/ghostty-org/ghostty/actions/runs/24907048466), [4](https://github.com/ghostty-org/ghostty/actions/runs/24889534540), [5](https://github.com/ghostty-org/ghostty/actions/runs/24873393693)  
Summary: 5 runs • 24 commits • 7 authors

### Changes

- [`7c91cef`](https://github.com/ghostty-org/ghostty/commit/7c91cef28de31a9b2238d83b0f63b03a9841bd49) config: use Config to check key binding instead of App ([@bo2themax](https://github.com/bo2themax))
  ```text
  Previously `ghostty_app_key_is_binding` (unlike Surface) is just using `config.keybind` to check whether a KeyEvent is in the set or not.
  
  After this, I can add unit tests for keybinding more easily, with dummy configs.
  ```
- [`4ceeba4`](https://github.com/ghostty-org/ghostty/commit/4ceeba4851030e75398cf1e5d3f7d8c7ed645e87) config: use Config to check key binding instead of App ([#12415](https://github.com/ghostty-org/ghostty/issues/12415)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously `ghostty_app_key_is_binding` (unlike Surface) is just using
  `config.keybind` to check whether a KeyEvent is in the set or not.
  
  After this, I can add unit tests for keybinding more easily with dummy
  configs.
  
  I didn't find any usages of this in GTK, so it shouldn't affect
  anything. ci will see if this is the case:)
  ```
- [`6b69ea0`](https://github.com/ghostty-org/ghostty/commit/6b69ea05170435ee6abd79b9a3da7a2609d5aaa3) libghostty: enable cross-compiling macOS from Linux/Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  This allows libghostty-vt to be cross-compiled for macOS from non-macOS
  platforms. I've updated pkg/apple-sdk to fallback to Zig's embedded
  macOS headers if the macOS SDK is not found.
  
  Additionally, CombineArchivesStep has been updated to use Linux
  tooling on Linux.
  ```
- [`2ed382a`](https://github.com/ghostty-org/ghostty/commit/2ed382a15566b267c32fae440b065f7844b15bfb) libghostty: enable cross-compiling macOS from Linux/Windows ([#12417](https://github.com/ghostty-org/ghostty/issues/12417)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This allows libghostty-vt to be cross-compiled for macOS from non-macOS
  platforms. I've updated pkg/apple-sdk to fallback to Zig's embedded
  macOS headers if the macOS SDK is not found. Additionally,
  CombineArchivesStep has been updated to use Linux tooling on Linux. CI
  updated to test this.
  ```
- [`4204dec`](https://github.com/ghostty-org/ghostty/commit/4204dec94a45ee7ce3990af33b301053191232c5) build: respect config.emit_xcframework for building libghostty-vt.xcframework on Darwin (0xDVC)
  ```text
  This fixes a hardcoded build issue on macOS where Zig unconditionally forces xcodebuild -create-xcframework to run during compilation, even when the caller explicitly specifies that they only want the raw standard C objects/headers (-Demit-lib-vt).
  
  The Bug:
  Around line 155 in build.zig, the libghostty-vt xcframework was being packaged unconditionally for Darwin builds. This caused developers (and wrappers like go-libghostty) attempting to natively build the vt library locally using only the minimal macOS Command Line Tools to experience an immediate crash, as xcodebuild -create-xcframework strictly demands a full Xcode application installation.
  
  The Fix:
  Guarded the GhosttyLibVt xcframework creation step with config.emit_xcframework. Because src/build/Config.zig intuitively forces emit_xcframework to default to false whenever emit_lib_vt is invoked, this structurally allows lightweight macOS builds to safely skip the xcodebuild invocation while still correctly compiling the standard .a object library files.
  ```
- [`38e8e54`](https://github.com/ghostty-org/ghostty/commit/38e8e54f98a8d5574962cfd34649d0740643a6ff) build: make libghostty-vt xcframework emission explicit via -Demit-lib-vt-xcframework (0xDVC)
- [`4e2e765`](https://github.com/ghostty-org/ghostty/commit/4e2e765fd4e70d94a0d7fca36fd742e5b77d8842) Merge branch 'main' into fix/xcframework-macos-dependency ([@0xDVC](https://github.com/0xDVC))
- [`caad13e`](https://github.com/ghostty-org/ghostty/commit/caad13e2323ff74f2ca9c7eecab4db0963842498) chore(fmt): zig fmt build.zig to pass test (0xDVC)
- [`44a2d87`](https://github.com/ghostty-org/ghostty/commit/44a2d8740a4a701d3eeded5261035db8e85ff8d7) build: gate lib-vt xcframework on emit-xcframework with xcodebuild detection (0xDVC)
- [`33fc2aa`](https://github.com/ghostty-org/ghostty/commit/33fc2aac97420466137a9b34fe7630f677f1a2e3) cleanups ([@mitchellh](https://github.com/mitchellh))
- [`5f892b6`](https://github.com/ghostty-org/ghostty/commit/5f892b691b8ef887525df16c85fc0cc799e24ec7) ci: fix ([@mitchellh](https://github.com/mitchellh))
- [`d35f02d`](https://github.com/ghostty-org/ghostty/commit/d35f02d83c195f02bf0c333f8af0e7913e0ee673) build: respect config.emit_xcframework for building libghostty-vt.xcframework on Darwin ([#12267](https://github.com/ghostty-org/ghostty/issues/12267)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a hardcoded build issue on macOS where Zig unconditionally
  forces xcodebuild -create-xcframework to run during compilation, even
  when the caller explicitly specifies that they only want the raw
  standard C objects/headers (-Demit-lib-vt).
  ```
- [`eee1018`](https://github.com/ghostty-org/ghostty/commit/eee10189885c7b730ca1c87d0ef7a8c8d29b4c27) Update VOUCHED list ([#12418](https://github.com/ghostty-org/ghostty/issues/12418)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11461#issuecomment-4315618982)
  from @jcollie.
  
  Vouch: @seyoungjeong
  ```
- [`2f067e1`](https://github.com/ghostty-org/ghostty/commit/2f067e14f15582fe7e13c366f18e952b70f3fd4e) ci: fix vouch-check-issue to checkout the template file ([@trag1c](https://github.com/trag1c))
- [`48ccec1`](https://github.com/ghostty-org/ghostty/commit/48ccec182a932c2ec04c344d45a5fc553861cb13) ci: fix vouch-check-issue to checkout the template file ([#12412](https://github.com/ghostty-org/ghostty/issues/12412)) ([@trag1c](https://github.com/trag1c))
- [`c642e31`](https://github.com/ghostty-org/ghostty/commit/c642e3104bb8b22ab29e2fd700132ed5d62203cf) pkg/highway: Darwin builds don't rely on Apple headers ([@mitchellh](https://github.com/mitchellh))
  ```text
  This uses a custom fork of `hwy/targtes.cpp` that uses an extern
  function written in Zig to use Zig's standard CPU detection to avoid
  a dependency on Apple SDK headers.
  
  This is on the path to removing Apple SDK requirements to build
  libghostty-vt, but will require a lot more work outside of this. The goal
  is to get this out of our external dependencies first and then we can
  work on removing the internal side.
  ```
- [`bdb164a`](https://github.com/ghostty-org/ghostty/commit/bdb164a6e561daa767e3e81f892f221548d5a1da) pkg/highway: expand detection to all platforms not just darwin ([@mitchellh](https://github.com/mitchellh))
- [`f3f9af6`](https://github.com/ghostty-org/ghostty/commit/f3f9af612967154c419b63976bc5b0e718d57ab6) pkg/highway: vendor and modify to remain all libc usage ([@mitchellh](https://github.com/mitchellh))
- [`055922f`](https://github.com/ghostty-org/ghostty/commit/055922faaa6e1e164b3c5306dc25b0e42c49c5c0) more zon2nix update for improved 0.16 compatibility ([@jcollie](https://github.com/jcollie))
- [`3c0b976`](https://github.com/ghostty-org/ghostty/commit/3c0b976d071dab71df687f371c1de0a1eca60b3c) pkg/highway: requires libc headers ([@mitchellh](https://github.com/mitchellh))
- [`00dfd67`](https://github.com/ghostty-org/ghostty/commit/00dfd67beea63148d7779613756200952b0b9ab0) pkg/highway: replace resolveTargetQuery with direct CPU detection ([@mitchellh](https://github.com/mitchellh))
  ```text
  The previous runtime_detect.zig called std.zig.system.resolveTargetQuery
  which pulled in the entire Zig target/CPU model table infrastructure for
  every architecture (~4,000 symbols, ~175 KB of data tables, ~130 KB of
  code). This bloated the binary by ~500 KB and shifted code layout enough
  to cause a measurable icache/branch-predictor regression in unrelated
  hot paths like the terminal parser (~20% more cycles for identical
  instruction counts).
  
  Replace with minimal, direct CPU feature detection per architecture:
  CPUID + XGETBV inline assembly on x86, sysctlbyname on Darwin AArch64,
  and getauxval/prctl via std.os.linux (direct syscalls, no libc) on
  Linux for AArch64, PPC, S390x, RISC-V, and LoongArch.
  
  Split into per-architecture files under src/detect/ for
  maintainability.
  ```
- [`bf3047b`](https://github.com/ghostty-org/ghostty/commit/bf3047b9b21972acc1f017a930e9b3ed6048e037) benchmark: isolate parser hot loop from code-layout shifts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract the tight per-byte parsing loop from TerminalParser.step into
  a separate noinline function (parseAll). This eliminates a ~20%
  benchmark regression that appeared after the highway vendor changes
  despite zero changes to the parser source code.
  
  The root cause: the parser benchmark processes 50 MB of input through
  a byte-at-a-time DFA loop that is highly sensitive to instruction
  cache-line placement on Apple Silicon. The M-series cores fetch
  aligned 16-byte blocks; when the loop head lands near the end of a
  64-byte cache line (offset 60), only one instruction fits in the
  first fetch versus four when aligned to offset 48. This causes ~29%
  more cycles for identical instruction counts.
  
  Previously the loop was inlined into the large step() function, so
  any code change anywhere in the binary (like the highway vendor
  restructuring) could shift the loop across a cache-line boundary.
  By making parseAll noinline, the loop gets its own function placement
  that is stable regardless of surrounding code changes.
  ```
- [`5f43437`](https://github.com/ghostty-org/ghostty/commit/5f43437576ce1bf88a9a8236d6df0753ec13ce15) pkg/highway: no libc requirement ([#12402](https://github.com/ghostty-org/ghostty/issues/12402)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This uses a custom fork Google Highway that removes all libc usage. For
  most, it was logging and we can just remove it. For detection, we moved
  this to an extern func implemented in Zig built using the Zig standard
  library so we can avoid libc.
  
  # Benchmark Results
  
  All benchmarks use 50 MB pre-generated inputs (`ghostty-gen +utf8
  --seed=42`)
  built and run with `-Doptimize=ReleaseFast` on Apple Silicon
  (aarch64-macos).
  
  ## Input Descriptions
  
  | Input | Description |
  |:------|:------------|
  | ascii-only | 1-byte sequences only, printable ASCII |
  | 2byte-only | 2-byte sequences only (Latin/Cyrillic/etc.) |
  | 3byte-only | 3-byte sequences only (CJK/BMP) |
  | 4byte-only | 4-byte sequences only (emoji/supplementary planes) |
  | mixed-equal | Equal weight across all 4 lengths |
  | mostly-ascii | ~80% ASCII, ~20% multibyte |
  | cjk-heavy | ~80% 3-byte, ~20% other |
  | 10pct-invalid | Equal-weight mix with 10% malformed sequences |
  
  ## Terminal Parser (byte-by-byte DFA, no SIMD)
  
  | Input | Mean [ms] | Min [ms] | Max [ms] | Relative |
  |:------|----------:|---------:|---------:|---------:|
  | ascii-only | 46.3 ± 0.8 | 45.4 | 48.1 | 1.00 |
  | 2byte-only | 59.1 ± 1.2 | 57.8 | 62.7 | 1.28 ± 0.03 |
  | 3byte-only | 65.4 ± 2.1 | 64.1 | 78.6 | 1.41 ± 0.05 |
  | 4byte-only | 59.3 ± 1.3 | 57.2 | 63.5 | 1.28 ± 0.04 |
  | mixed-equal | 180.7 ± 0.7 | 179.5 | 182.3 | 3.90 ± 0.07 |
  | mostly-ascii | 59.3 ± 1.0 | 57.3 | 61.1 | 1.28 ± 0.03 |
  | cjk-heavy | 142.4 ± 2.0 | 140.4 | 149.9 | 3.08 ± 0.07 |
  | 10pct-invalid | 180.2 ± 1.5 | 178.4 | 184.9 | 3.89 ± 0.08 |
  
  ## Terminal Stream (SIMD UTF-8 decode + terminal handling)
  
  | Input | Mean [ms] | Min [ms] | Max [ms] | Relative |
  |:------|----------:|---------:|---------:|---------:|
  | ascii-only | 377.0 ± 8.7 | 357.1 | 386.4 | 2.42 ± 0.08 |
  | 2byte-only | 664.5 ± 4.0 | 656.9 | 672.6 | 4.27 ± 0.11 |
  | 3byte-only | 233.5 ± 0.9 | 231.1 | 234.8 | 1.50 ± 0.04 |
  | 4byte-only | 155.5 ± 4.0 | 149.6 | 161.3 | 1.00 |
  | mixed-equal | 467.0 ± 3.4 | 461.8 | 473.9 | 3.00 ± 0.08 |
  | mostly-ascii | 470.8 ± 7.2 | 459.6 | 482.8 | 3.03 ± 0.09 |
  | cjk-heavy | 338.4 ± 2.4 | 334.3 | 341.7 | 2.18 ± 0.06 |
  | 10pct-invalid | 635.1 ± 3.5 | 630.5 | 640.8 | 4.08 ± 0.11 |
  
  ## Branch Comparison: `main` vs `fixed`
  
  ### Terminal Parser
  
  | Input | main [ms] | fixed [ms] | Δ |
  |:------|----------:|-----------:|:--|
  | ascii-only | 46.9 ± 0.7 | 47.3 ± 0.9 | ~same |
  | 2byte-only | 59.0 ± 0.5 | 59.1 ± 1.2 | ~same |
  | 3byte-only | 65.9 ± 2.1 | 65.4 ± 2.1 | ~same |
  | 4byte-only | 58.8 ± 0.5 | 59.3 ± 1.3 | ~same |
  | mixed-equal | 182.5 ± 0.9 | 180.7 ± 0.7 | fixed 1% faster |
  | mostly-ascii | 59.0 ± 0.5 | 59.3 ± 1.0 | ~same |
  | cjk-heavy | 144.1 ± 1.7 | 142.4 ± 2.0 | ~same |
  | 10pct-invalid | 181.7 ± 1.0 | 180.2 ± 1.5 | ~same |
  
  ### Terminal Stream
  
  | Input | main [ms] | fixed [ms] | Δ |
  |:------|----------:|-----------:|:--|
  | ascii-only | 388.4 ± 8.8 | 383.1 ± 7.6 | ~same |
  | 2byte-only | 687.7 ± 4.8 | 672.9 ± 2.6 | fixed 2% faster |
  | 3byte-only | 235.5 ± 1.2 | 236.3 ± 2.5 | ~same |
  | 4byte-only | 166.2 ± 2.9 | 159.9 ± 3.1 | fixed 4% faster |
  | mixed-equal | 481.8 ± 3.3 | 480.7 ± 6.3 | ~same |
  | mostly-ascii | 483.8 ± 6.7 | 475.9 ± 4.3 | ~same |
  | cjk-heavy | 341.7 ± 3.1 | 341.6 ± 2.0 | ~same |
  | 10pct-invalid | 647.6 ± 3.3 | 640.4 ± 3.4 | ~same |
  
  No regressions in either benchmark. Fixed branch is equal or slightly
  faster
  across all inputs.
  
  ## Reproduction
  
  ```bash
  # Generate inputs (do NOT regenerate when comparing branches)
  for profile in \
    "--weight-one=1 --weight-two=0 --weight-three=0 --weight-four=0 --ascii-printable-only=true" \
    "--weight-one=0 --weight-two=1 --weight-three=0 --weight-four=0" \
    "--weight-one=0 --weight-two=0 --weight-three=1 --weight-four=0" \
    "--weight-one=0 --weight-two=0 --weight-three=0 --weight-four=1" \
    "--weight-one=1 --weight-two=1 --weight-three=1 --weight-four=1" \
    "--weight-one=10 --weight-two=1 --weight-three=1 --weight-four=0.5 --ascii-printable-only=true" \
    "--weight-one=1 --weight-two=0.5 --weight-three=10 --weight-four=0.5" \
    "--weight-one=1 --weight-two=1 --weight-three=1 --weight-four=1 --invalid-rate=0.1"; do
    ghostty-gen +utf8 --seed=42 $profile | head -c 50000000 > /tmp/ghostty-bench-data/<name>.dat
  done
  
  # Build
  zig build -Demit-bench -Doptimize=ReleaseFast -Demit-macos-app=false
  
  # Run
  hyperfine --warmup 3 --min-runs 10 \
    './zig-out/bin/ghostty-bench +terminal-stream --data=<path>'
  ```
  ````
- [`b0d359c`](https://github.com/ghostty-org/ghostty/commit/b0d359cbbd945f9f3807327526ef79fcaf0477df) more zon2nix update for improved 0.16 compatibility ([#12405](https://github.com/ghostty-org/ghostty/issues/12405)) ([@mitchellh](https://github.com/mitchellh))

## April 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24850309126), [2](https://github.com/ghostty-org/ghostty/actions/runs/24847728869), [3](https://github.com/ghostty-org/ghostty/actions/runs/24846534553), [4](https://github.com/ghostty-org/ghostty/actions/runs/24839189784), [5](https://github.com/ghostty-org/ghostty/actions/runs/24814161245), [6](https://github.com/ghostty-org/ghostty/actions/runs/24812939117), [7](https://github.com/ghostty-org/ghostty/actions/runs/24810009508)  
Summary: 7 runs • 40 commits • 8 authors

### Changes

- [`61fce4d`](https://github.com/ghostty-org/ghostty/commit/61fce4d0a4a117c4433be0fff4b4e7681f33bdf1) font: add Windows font discovery backend ([@mattn](https://github.com/mattn))
  ```text
  Adds a FreeType-based Discover implementation for Windows that walks
  the system (C:\Windows\Fonts) and per-user
  (%LOCALAPPDATA%\Microsoft\Windows\Fonts) font directories, matching
  descriptors via family_name / SFNT name table and optionally codepoint
  presence.
  
  Wired up as a new .freetype_windows backend which Backend.default() now
  returns on Windows. Existing freetype-only paths are untouched.
  
  With this in place, standard code paths -- +list-fonts, SharedGridSet
  font-family lookup, CodepointResolver fallback -- work on Windows
  without any os.tag == .windows branches in the caller.
  ```
- [`fe2a909`](https://github.com/ghostty-org/ghostty/commit/fe2a909782607b6046b2a93d866b4ba86b361a94) font/discovery: use %SYSTEMROOT%\Fonts instead of a hardcoded path ([@mattn](https://github.com/mattn))
  ```text
  Resolve the system font directory from SYSTEMROOT rather than assuming
  it lives on C:. If SYSTEMROOT is somehow unset we skip the system
  directory instead of falling back to a literal drive letter.
  ```
- [`5aef254`](https://github.com/ghostty-org/ghostty/commit/5aef2541b044e1c68bf830aa6878e07e7128c301) address review: Discover.init takes a Library across all backends ([@mattn](https://github.com/mattn))
  ```text
  Per review feedback, drop the `if (Discover == Windows)` comptime
  branches in SharedGridSet and list_fonts by making every backend's
  `init` take a Library and ignore it when unused. Call sites just do
  `Discover.init(self.font_lib)` now.
  
  Also adds a discovery test for the Windows backend that looks up
  Arial and checks the returned face has the 'A' codepoint.
  ```
- [`fe725b5`](https://github.com/ghostty-org/ghostty/commit/fe725b5da19d5019f3b4d1338cfe342f63257e5f) address review: update shaper test discover callsites ([@mattn](https://github.com/mattn))
  ```text
  CI on Windows (MSVC) surfaced three remaining callers of the old
  zero-arg `Discover.init()` in shaper test helpers that the earlier
  commit missed. Pass `lib` to match the new signature.
  ```
- [`0343a4d`](https://github.com/ghostty-org/ghostty/commit/0343a4d98fdecb58306f8d8712455b496cf8b2d1) address review: update DeferredFace test discover callsites ([@mattn](https://github.com/mattn))
  ```text
  Two more holdouts in DeferredFace.zig test helpers calling
  Fontconfig.init / CoreText.init with no args; Nix test CI surfaced
  them for the fontconfig path.
  ```
- [`e89cc0b`](https://github.com/ghostty-org/ghostty/commit/e89cc0b34cd6a62d3a0f6e9b722a8306178dd901) pkg/simdutf: upgrade to simdutf v9, off our fork for nolibcxx ([@mitchellh](https://github.com/mitchellh))
- [`48db54d`](https://github.com/ghostty-org/ghostty/commit/48db54d7ef12d4506704bbc5b6eb2075658376eb) pkg/simdutf: upgrade to simdutf v9, off our fork for nolibcxx ([#12399](https://github.com/ghostty-org/ghostty/issues/12399)) ([@mitchellh](https://github.com/mitchellh))
- [`2f1a30d`](https://github.com/ghostty-org/ghostty/commit/2f1a30ddb047162a4d3acc20c2f83aadfcfe3fbb) font: add Windows font discovery backend ([#12386](https://github.com/ghostty-org/ghostty/issues/12386)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds a FreeType-based `Discover` implementation for Windows. It walks
  the system font directory (`%SYSTEMROOT%\Fonts`) and the per-user
  directory (`%LOCALAPPDATA%\Microsoft\Windows\Fonts`), matches
  descriptors by FreeType `family_name` (falling back to the SFNT name
  table), and, when a codepoint is in the descriptor, filters on CMap
  coverage.
  
  Wired up as a new `.freetype_windows` backend which `Backend.default()`
  now returns on Windows. Existing freetype-only paths are untouched and
  no other platform is affected; cross-platform switches were extended to
  handle the new enum value the same way they handle `.freetype`.
  
  With this in place, the standard code paths (`+list-fonts`,
  `SharedGridSet` font-family lookup, `CodepointResolver` fallback) work
  on Windows without any `os.tag == .windows` branches in the caller.
  
  Verified by the `build-libghostty-windows-gnu` CI job. No runtime binary
  ships yet on Windows (no apprt), but this is a drop-in for the discovery
  API that the Win32 apprt (and the revisited `+list-fonts` PR #12384)
  will use. Once this lands, #12384 can be closed and `+list-fonts` will
  work on Windows through the ordinary discovery code path, which
  addresses the review feedback that `+list-fonts` should only show fonts
  the internal discovery can find.
  
  ---
  
  AI usage disclosure: developed with Claude Code (Claude Opus 4.7).
  Claude drafted the implementation based on my design direction -- I
  picked the "add a Discover backend" shape over the ad-hoc approach in
  the earlier `+list-fonts` PR. I reviewed each diff and validated it with
  a Windows GNU-ABI smoke build before pushing.
  
  Part of the Win32 apprt upstreaming series (see discussion #2563 /
  mattn/ghostty#1).
  ```
- [`d778be2`](https://github.com/ghostty-org/ghostty/commit/d778be20dd47c6caf3b11bc730fecfe0e8c3ebee) font/opentype: add glyf table entry validation ([@qwerasd205](https://github.com/qwerasd205))
  ```text
  We want to have this for the glyph protocol so that we can validate
  passed glyf data in libghostty without having to link freetype or
  anything like that.
  ```
- [`5086995`](https://github.com/ghostty-org/ghostty/commit/50869952afe4d3187af7b01deae455612bd93117) font/opentype: use packed struct for glyf point flags ([@qwerasd205](https://github.com/qwerasd205))
  ```text
  Also fixes a logic bug where we weren't counting the length of x
  coordinates and y coordinates correctly when we had repeated flags.
  ```
- [`94e638d`](https://github.com/ghostty-org/ghostty/commit/94e638d08415255a5231d901714abeb95492e253) build: produce fat static archive on all platforms ([@deblasis](https://github.com/deblasis))
  ```text
  The static libghostty archive previously only bundled vendored
  dependencies on macOS (via libtool). On Windows and Linux the
  archive contained only the Zig-compiled code, leaving consumers
  to discover and link freetype, harfbuzz, glslang, spirv-cross,
  simdutf, oniguruma, and other vendored deps separately.
  
  Now all platforms produce a single fat archive:
  - macOS: libtool (unchanged)
  - Windows: zig ar qcL --format=coff (LLVM archiver with the L
    flag to flatten nested archives; MSVC's lib.exe cannot read
    Zig-produced GNU-format archives)
  - Linux: ar -M with MRI scripts (same as libghostty-vt)
  
  This makes the static library self-contained for consumers like
  .NET NativeAOT that link via the platform linker (MSVC link.exe)
  and need all symbols resolved from a single archive.
  ```
- [`a108546`](https://github.com/ghostty-org/ghostty/commit/a10854654d47e43c5a8240cdbbe8cebac7195b07) build: disable ubsan in C deps for MSVC static linking ([@deblasis](https://github.com/deblasis))
  ```text
  Zig's ubsan runtime cannot be bundled on Windows (LNK4229),
  leaving __ubsan_handle_* symbols unresolved when the static
  archive is consumed by an external linker like MSVC link.exe.
  
  freetype, glslang, spirv-cross, and highway already suppress
  ubsan unconditionally. Add MSVC-conditional suppression to the
  seven C dependencies that were missing it: harfbuzz, libpng,
  dcimgui, wuffs, oniguruma, zlib, and stb.
  
  The fix is gated on abi == .msvc so ubsan coverage is preserved
  on Linux and macOS where bundle_ubsan_rt works.
  ```
- [`08a2d9b`](https://github.com/ghostty-org/ghostty/commit/08a2d9b224210208ab795835c1ad4187309e289a) build: share combineArchives and fix internal archive names ([@deblasis](https://github.com/deblasis))
  ```text
  Extract CombineArchivesStep.zig so both GhosttyLib and GhosttyLibVt
  use the same archive-combining logic. Uses libtool on Darwin and the
  cross-platform combine_archives build tool elsewhere.
  
  Renames the internal library's fat archive outputs from ghostty to
  ghostty-internal, matching the pkg-config rename from PR 12214.
  ```
- [`bc90a51`](https://github.com/ghostty-org/ghostty/commit/bc90a51282a290d11427b4ca66a88f4fd61ffe47) build: fat static archive and ubsan fix for external linkers ([#12217](https://github.com/ghostty-org/ghostty/issues/12217)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  > [!IMPORTANT]
  > Stacked on #12214. Review that first. (i am targeting `main` so here
  you will see the full changeset, including 12214
  
  Two changes that make the static libghostty archive consumable by
  external linkers (MSVC link.exe, .NET NativeAOT, Rust, Go, etc.):
  
  **Fat static archive on all platforms**
  
  The static archive previously only bundled vendored deps on macOS (via
  libtool). On Windows and Linux the archive contained only the
  Zig-compiled code, requiring consumers to find and link freetype,
  harfbuzz, glslang, spirv-cross, simdutf, oniguruma, etc. separately.
  
  Now all platforms produce a single fat archive:
  - macOS: libtool (unchanged)
  - Windows: zig ar qcL --format=coff (MSVC's lib.exe can't read
  Zig-produced GNU-format archives, so we use the bundled LLVM archiver)
  - Linux: ar -M with MRI scripts (same approach as libghostty-vt)
  
  **MSVC ubsan suppression for C deps**
  
  Zig's ubsan runtime can't be bundled on Windows (LNK4229), leaving
  __ubsan_handle_* symbols unresolved. freetype, glslang, spirv-cross, and
  highway already suppress ubsan. This adds MSVC-conditional suppression
  to seven more: harfbuzz, libpng, dcimgui, wuffs, oniguruma, zlib, and
  stb.
  
  Gated on abi == .msvc so ubsan coverage is preserved on Linux/macOS.
  
  ## Test plan
  
  - [x] zig build produces a fat ghostty-static.lib (~230MB) with ~200
  object files
  - [x] MSVC's lib /LIST can read the archive
  - [x] .NET NativeAOT consumer resolves all symbols (0 unresolved)
  - [x] Linux/macOS builds unaffected (ubsan remains enabled)
  ```
- [`464c504`](https://github.com/ghostty-org/ghostty/commit/464c50457ba2a8b56c781cb0124240d984dce9ae) font/opentype: accept header-only simple glyf entry ([@qwerasd205](https://github.com/qwerasd205))
- [`c1b685b`](https://github.com/ghostty-org/ghostty/commit/c1b685bc6275d6ca4cd1ebb3b16e3aea54ab62ff) Add code for validating OpenType GLYF table entries ([#12375](https://github.com/ghostty-org/ghostty/issues/12375)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This code was motivated by the need for the glyph protocol handler
  (#12352) to be able to validate the provided `glyf` payload, without
  having to link freetype or anything (because libghostty-vt needs to be
  static). As such it's written specifically to meet those needs, but in
  such a way that it can be expanded if we find a need for more in-depth
  inspection of `glyf`s in the future.
  ```
- [`ef7ecbd`](https://github.com/ghostty-org/ghostty/commit/ef7ecbd3e5f389402d5030163462ab39ba897630) termio: run Windows shell commands without a cmd.exe wrapper ([@mattn](https://github.com/mattn))
  ```text
  On Windows the shell value was always executed as `cmd.exe /C <shell>`.
  For even a simple `command = wsl ~` this spawned two processes (the
  cmd wrapper and the user's actual shell) and had visible side effects:
  an extra cmd.exe in the process tree, and cmd AutoRun state (DOSKEY
  aliases, `cd` in init.cmd, etc.) running in the wrapper rather than
  the user's shell, since AutoRun is per-process.
  
  Run the shell value directly. If it contains whitespace, split on
  whitespace into argv. Bare `cmd.exe` is resolved via %COMSPEC% which
  is the documented path to the current command processor; other bare
  values are left to PATH resolution in Command.startWindows.
  
  The simple whitespace split does not honor Windows CLI quoting rules.
  Users who need quoted arguments should use the direct command form.
  
  Also skip the termios focus timer on Windows since Windows has no
  termios; the focusGained callback was starting a timer whose callback
  would then do nothing.
  ```
- [`c32e88c`](https://github.com/ghostty-org/ghostty/commit/c32e88c6a7700d38de3b695c2991c0d7e11eaf71) Command: let CreateProcessW resolve the program via PATH ([@mattn](https://github.com/mattn))
  ```text
  Pass null for lpApplicationName and put the program as the first
  token of lpCommandLine. Per the Windows docs, this makes
  CreateProcessW perform the standard program search (parent-app dir,
  CWD, system dirs, PATH) and append ".exe" when the name has no
  extension.
  
  So a bare command name like `wsl` or `pwsh` from the Ghostty config
  now resolves without any PATH/PATHEXT handling on our side. The
  child also sees its argv[0] exactly as written rather than replaced
  with the resolved absolute path.
  ```
- [`8c5b8ac`](https://github.com/ghostty-org/ghostty/commit/8c5b8ac3c0ad607e78611dcae2b1743cd99e50d5) address review: add unit tests for Windows execCommand paths ([@mattn](https://github.com/mattn))
  ```text
  Per review feedback, cover the four Windows branches added in the
  parent commit:
  
  - bare `cmd.exe` resolves via `%COMSPEC%` (with documented fallback)
  - bare non-cmd shell (`pwsh.exe`) is passed through unchanged
  - shell value with arguments (`wsl ~`) is split on whitespace
  - direct command is passed through without modification
  ```
- [`1ae27f9`](https://github.com/ghostty-org/ghostty/commit/1ae27f95b43edeece2bdade3dbcecc9d455f0e5f) os: trim trailing path separators from tmpdir ([@jparise](https://github.com/jparise))
  ```text
  Because we generally read this value from an environment variable, we
  the resulting value can include a trailing slash (as on macOS). This
  results in less-friendly path operations for callers who are building
  paths based on this value.
  
  `std.fs.path.join()` handles trailing slashes just fine, but it's an
  allocating API. For callers who just want to format a path, they have to
  assume they need to include their own path separator.
  
  We can make this friendlier by always trimming trailing path separators
  from the environment variable values before returning the slice.
  
  This behavior matches "higher-level" languages' standard libraries (I
  checked Python, Node, Ruby, and Perl). Other "systems" languages (Go,
  Rust) just return the system value as-is, like we were doing before.
  ```
- [`b34c62b`](https://github.com/ghostty-org/ghostty/commit/b34c62bf043aeadfe60b4d84da61b62b2ba44d92) Command: let CreateProcessW resolve the program via PATH ([#12387](https://github.com/ghostty-org/ghostty/issues/12387)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Windows users often set bare command names in the Ghostty config
  (`command = bash`) or pass them via `-e`, matching how they would on
  Linux/macOS. Today that fails because `CreateProcessW` does not do
  program search for `lpApplicationName` on its own.
  
  Thanks to @qwerasd205 for pointing out that passing `NULL` for
  `lpApplicationName` is exactly how Windows docs say to get program
  search for free. This PR does that: drop the explicit utf16 conversion
  for `lpApplicationName`, pass `null`, and make sure the program name is
  the first token of `lpCommandLine`. Windows then walks parent-app dir,
  CWD, system dirs, and PATH (and appends `.exe` for extensionless names).
  The child also sees its `argv[0]` exactly as we wrote it rather than a
  resolved absolute path, which is less surprising.
  
  Net change is +15 / -7 in `src/Command.zig`; no new helpers, no changes
  outside that file. The earlier version of this PR (which added
  PATH/PATHEXT handling in `internal_os.path.expand`) is obsoleted by this
  approach and has been force-pushed away.
  
  ---
  
  AI usage disclosure: developed with Claude Code (Claude Opus 4.7).
  Claude drafted the implementation based on my direction after
  @qwerasd205's review suggested the NULL-lpApplicationName approach. I
  reviewed the diff, built and verified it on the Windows GNU-ABI target,
  and am responsible for the code landing here.
  
  Part of the Win32 apprt upstreaming series (see discussion #2563 /
  mattn/ghostty#1).
  ```
- [`04accc0`](https://github.com/ghostty-org/ghostty/commit/04accc001d0683db0a8b046c868f7da563993407) os: trim trailing path separators from tmpdir ([#12397](https://github.com/ghostty-org/ghostty/issues/12397)) ([@jparise](https://github.com/jparise))
  ```text
  Because we generally read this value from an environment variable, we
  the resulting value can include a trailing slash (as on macOS). This
  results in less-friendly path operations for callers who are building
  paths based on this value.
  
  `std.fs.path.join()` handles trailing slashes just fine, but it's an
  allocating API. For callers who just want to format a path, they have to
  assume they need to include their own path separator.
  
  We can make this friendlier by always trimming trailing path separators
  from the environment variable values before returning the slice.
  
  This behavior matches "higher-level" languages' standard libraries (I
  checked Python, Node, Ruby, and Perl). Other "systems" languages (Go,
  Rust) just return the system value as-is, like we were doing before.
  ```
- [`239b97e`](https://github.com/ghostty-org/ghostty/commit/239b97eccc9319f0b23fe7da3ca8475ee9ebcee0) termio: run Windows shell commands without a cmd.exe wrapper ([#12389](https://github.com/ghostty-org/ghostty/issues/12389)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On Windows the configured shell was always executed as `cmd.exe /C
  <shell>`. That inserts a cmd.exe even for simple values like `command =
  wsl ~` or `command = pwsh -NoLogo`, producing two processes where one
  would do.
  
  Two concrete side effects:
  
  An extra cmd.exe appears in every Windows terminal's process tree
  (visible in Task Manager / process listings), two processes per surface
  where only one is the user's shell.
  
  cmd.exe state set by AutoRun (`HKCU\Software\Microsoft\Command
  Processor\AutoRun`, used commonly for DOSKEY aliases or `cd` in
  `init.cmd`) lives in the wrapping cmd process, not in the user's shell.
  Since AutoRun state like DOSKEY aliases is per-process, the user's
  aliases don't reach the shell they actually interact with.
  
  Run the shell value directly instead. If it contains whitespace, split
  on whitespace into argv. A bare `cmd.exe` is resolved via `%COMSPEC%`
  (the documented path to the current command processor). Other bare
  values are left to PATH resolution in `Command.startWindows` (#12387).
  
  The simple whitespace split does not honor Windows CLI quoting rules;
  users who need quoted arguments should use the direct command form,
  which takes an argv array as-is. For the common case (`wsl ~`, `pwsh
  -NoLogo`, `cmd.exe /k init.cmd`, etc.) this covers the shapes users
  actually write today.
  
  Also skips the termios focus timer on Windows in `focusGained`, since
  Windows has no termios -- the callback was arming a timer whose tick did
  nothing and just added noise.
  
  ---
  
  AI usage disclosure: developed with Claude Code (Claude Opus 4.7).
  Claude drafted the implementation based on my design direction -- I
  picked which pieces belong in this PR (drop the cmd wrapper, use
  `%COMSPEC%`, skip the termios focus timer) and which belong in sibling
  PRs. I reviewed each diff and validated it with a Windows GNU-ABI smoke
  build before pushing.
  
  Part of the Win32 apprt upstreaming series (see discussion #2563 /
  mattn/ghostty#1).
  ```
- [`ae1dd56`](https://github.com/ghostty-org/ghostty/commit/ae1dd5666dbd024825a988a0d20efa3af22479a0) fuzz: fix macOS AFL toolchain and linker setup for macOS 26.4 ([@mitchellh](https://github.com/mitchellh))
  ```text
  On macOS 26.4, AFL builds were picking up Nix compiler-wrapper
  variables and Apple SDK target settings from the shell environment.
  That caused afl-cc to drive the wrong linker and target configuration,
  which broke even simple fuzz harness builds. Unset the Nix compiler and
  linker environment in the fuzz dev shell so AFL++ uses the system or
  Homebrew Apple toolchain directly.
  
  Also force afl-cc to link with lld because the newer Apple linker
  asserts on the custom sections emitted by AFL's LLVM
  instrumentation. Finally, pin fuzz-libghostty to the host target so the
  build does not inherit stray SDK targets from the environment.
  ```
- [`d6d7bdb`](https://github.com/ghostty-org/ghostty/commit/d6d7bdbee50202b3b67b6dcd09e92f01189e15b7) fuzz: fix macOS AFL toolchain and linker setup for macOS 26.4 ([#12398](https://github.com/ghostty-org/ghostty/issues/12398)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  * Unset the Nix compiler and linker environment in the fuzz dev shell so
  AFL++ uses the system or Homebrew Apple toolchain directly.
  * Force afl-cc to link with lld because the newer Apple linker asserts
  on the custom sections emitted by AFL's LLVM instrumentation.
  * Pin fuzz-libghostty to the host target so the build does not inherit
  stray SDK targets from the environment.
  ```
- [`a8ed37a`](https://github.com/ghostty-org/ghostty/commit/a8ed37a791dae5db4c966efbaeb183a63914ff65) macOS: fix command parsing in NewTerminalIntent ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes #12391, regression from #10765
  ```
- [`b0b23f5`](https://github.com/ghostty-org/ghostty/commit/b0b23f53a706a0742548a2d535b414379c048040) macOS: check abnormal-command-exit-runtime when process exits ([@bo2themax](https://github.com/bo2themax))
- [`70bd66c`](https://github.com/ghostty-org/ghostty/commit/70bd66c081eb3401fd56c0ea61367f41da8d9219) macOS: check `abnormal-command-exit-runtime` when process exits ([#12393](https://github.com/ghostty-org/ghostty/issues/12393)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="849" height="434" alt="image"
  src="https://github.com/user-attachments/assets/81c89d8d-6f0a-4bb9-b942-6734ff616bf9"
  />
  ```
- [`7629c4b`](https://github.com/ghostty-org/ghostty/commit/7629c4ba84a810930b1ebc195464137318e765c5) macOS: fix command parsing in NewTerminalIntent ([#12392](https://github.com/ghostty-org/ghostty/issues/12392)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #12391, regression from #10765
  ```
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

