> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 29, 2026 at 00:33 UTC.

## October 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40788698089), [2](https://github.com/ghostty-org/ghostty/actions/runs/40775317812), [3](https://github.com/ghostty-org/ghostty/actions/runs/40736162338), [4](https://github.com/ghostty-org/ghostty/actions/runs/40627109889)  
Summary: 4 runs • 21 commits • 9 authors

### Changes

- [`7ee1074`](https://github.com/ghostty-org/ghostty/commit/7ee1074fbda91f0ed19ea34a6ba08a0c30bee2b2) Update VOUCHED list ([#14915](https://github.com/ghostty-org/ghostty/issues/14915)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14914#discussioncomment-19255908)
  from @jcollie.
  
  Vouch: @clinta
  ```
- [`4c8ad98`](https://github.com/ghostty-org/ghostty/commit/4c8ad9817e9e0fbb6060695ba50aa85e1174bf00) config: fix formatting of long environment values ([@12ya](https://github.com/12ya))
  ```text
  Write map entries directly to the output writer instead of using a
  256-byte buffer. Add a regression test for a 300-byte value.
  ```
- [`9ee1031`](https://github.com/ghostty-org/ghostty/commit/9ee1031ba7c5a0436388072e3f11a199d2c0a602) config: use allocator printing in long-value test ([@12ya](https://github.com/12ya))
  ```text
  #14908
  
  Replace both deprecated std.fmt.allocPrint calls with alloc.print.
  
  AI assistance: Codex updated both calls and ran the targeted tests.
  ```
- [`0b8b998`](https://github.com/ghostty-org/ghostty/commit/0b8b9984ee560456194262d190aa850224edb1f4) config: fix formatting of long environment values ([#14908](https://github.com/ghostty-org/ghostty/issues/14908)) ([@jcollie](https://github.com/jcollie))
  ```text
  Write map entries directly to the output writer instead of using a
  256-byte buffer. Add a regression test for a 300-byte value.
  
  <img width="654" height="77" alt="Screenshot 2026-10-29 at 2 50 41 AM"
  src="https://github.com/user-attachments/assets/82ba4f78-2137-4bc5-bd6f-2f2afe6cd96c"
  />
  ```
- [`aa16f94`](https://github.com/ghostty-org/ghostty/commit/aa16f9429caa2aa6fc9bc32983a0f7bb902551e3) nix: drop the revision from the zig deps derivation name ([@mitchellh](https://github.com/mitchellh))
- [`04c7597`](https://github.com/ghostty-org/ghostty/commit/04c75975052a657081a1f568b0f36ec8c57a46b0) ci: gate expensive jobs on a quick build instead of the full test suite ([@mitchellh](https://github.com/mitchellh))
- [`68b8377`](https://github.com/ghostty-org/ghostty/commit/68b837766217cea65cfe802dc79d4103a732c38f) ci: split build-nix into one job per target and architecture ([@mitchellh](https://github.com/mitchellh))
- [`ecc8792`](https://github.com/ghostty-org/ghostty/commit/ecc87922ecbde7cea6289dcd9e3dfbc38716c04f) ci: build the source tarball without waiting on its tests ([@mitchellh](https://github.com/mitchellh))
- [`1848241`](https://github.com/ghostty-org/ghostty/commit/184824102aa269350132eed4242493c739d3e53c) ci: run the full test suite once across the GTK and SIMD legs ([@mitchellh](https://github.com/mitchellh))
- [`c27ef4c`](https://github.com/ghostty-org/ghostty/commit/c27ef4c1b109fb2b9947730c391f1a7d06eaa62f) ci: improvements to speed things up, step one shorten critical paths for tests ([#14911](https://github.com/ghostty-org/ghostty/issues/14911)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Test on main takes over an hour and I'm tired of it. Almost all of that
  is one chain: every expensive job waits on `test` (~13 min), and then
  the arm64 `build-nix` job runs six `nix build`s serially (~50 min),
  rebuilding the Zig deps derivation every commit because its name embeds
  the git revision so that forces a rebuild.
  
  This breaks that chain up. By commit:
  
  - **nix: drop the revision from the zig deps derivation name.** The deps
  derivation now matches `.#deps`, so it only rebuilds when
  `build.zig.zon` changes and Cachix actually hits. This was costing ~8
  minutes of arm64 time per run.
  - **ci: gate expensive jobs on a quick build.** A new `build-gate` job
  (just `zig build`, ~2 min) replaces `needs: test`. Cheap jobs that don't
  need a compile gate now only wait on `skip`. `test` runs in parallel
  with everything else.
  - **ci: split build-nix into one job per target and architecture.** 12
  parallel jobs instead of 2 long serial ones. `required` checks them by
  result like everything else.
  - **ci: build the source tarball without waiting on its tests.**
  `build-dist` now runs `zig build dist`, so the Debian, snap, and flatpak
  jobs get the tarball in a few minutes instead of ~13. The full
  `distcheck` (unchanged) runs as `test-dist` on an md runner in parallel.
  - **ci: run the full test suite once across the GTK and SIMD legs.** The
  x11/wayland options don't change anything the unit tests cover, and
  `-Dsimd=true` is the default, so we were running the same full suite
  four extra times. The GTK legs still all build. This saves about 46
  runner-minutes per run. Also pins `nix-installer-action` to v23 instead
  of `@main`.
  
  Some tradeoffs worth knowing:
  
  - If `test` fails, the expensive jobs still run, since they're only
  gated on a compile now. Failing PRs cost more compute; passing PRs get
  much faster feedback. I think that's fine.
  - The first run after this merges will be a bit slow for Nix since all
  12 jobs build the deps derivation cold. After that it comes from Cachix.
  
  I plan to continue looking for improvements after this.
  
  **AI disclosure:** I used Fable to measure the existing CI runs and
  propose plans to break it down. I massaged those plans pretty
  significantly. I used Opus to write YAML because fuck writing YAML. I
  read it all.
  ```
- [`c16d204`](https://github.com/ghostty-org/ghostty/commit/c16d204bf72fbaa6b0ef0855e9439d34ba347eea) deps: update z2d to v0.13.2 ([@vancluever](https://github.com/vancluever))
  ```text
  Just a small update that I did to catch a bit of missing API that I
  wanted to expose in Context, nothing that affects Ghostty, however.
  
  Had to skip 0.13.1 because of an issue with the release tooling.
  ```
- [`44a4911`](https://github.com/ghostty-org/ghostty/commit/44a4911e9124e64f5da85255e29c21cdfc3d3941) terminal: implement DECIC, DECDC, DECBI, and DECFI ([@jcollie](https://github.com/jcollie))
  ```text
  Add the VT420 horizontal scrolling sequences:
  
  - DECIC (CSI Pn ' }) inserts columns at the cursor in every row of
    the scrolling region.
  - DECDC (CSI Pn ' ~) deletes columns at the cursor in every row of
    the scrolling region.
  - DECBI (ESC 6) moves the cursor left, or at the left margin scrolls
    the region right.
  - DECFI (ESC 9) moves the cursor right, or at the right margin
    scrolls the region left, losing the column at the left margin.
  
  DECIC and DECDC do nothing when the cursor is outside the scrolling
  region. The new stream actions are appended to the C ABI action list
  so that existing values are unchanged.
  
  This fixes 20 esctest failures (DECICTests, DECDCTests, DECBITests,
  and DECFITests now pass in full).
  ```
- [`316ab91`](https://github.com/ghostty-org/ghostty/commit/316ab91e49df9b2a87fd786a9650e0c3e270b6ef) po: update code sources ([@trag1c](https://github.com/trag1c))
- [`bcc1b9f`](https://github.com/ghostty-org/ghostty/commit/bcc1b9faf3394aca0920b1bc57eef24c3dfdc60f) i18n: don't localize the "Ghostty" command's title ([@trag1c](https://github.com/trag1c))
- [`0cb81fe`](https://github.com/ghostty-org/ghostty/commit/0cb81fe084684d8f81b99cf26c2015a37b11eaf1) datastruct/split_tree: assert goto() is given a valid handle ([@Huge](https://github.com/Huge))
  ```text
  goto() indexes the node and spatial slot arrays with `from` unchecked.
  The only caller (GTK SplitTree.goto) never reaches it with an empty
  tree, so make the precondition explicit like remove() does instead of
  silently returning null.
  ```
- [`acd72a4`](https://github.com/ghostty-org/ghostty/commit/acd72a42f72da136606807322212886226322f89) i18n: don't localize the "Ghostty" command's title ([#14888](https://github.com/ghostty-org/ghostty/issues/14888)) ([@00-kat](https://github.com/00-kat))
  ```text
  also updated the stale code sources
  ```
- [`057f148`](https://github.com/ghostty-org/ghostty/commit/057f14896c5a903511dbbc86206fa7acd11b3b8e) deps: update z2d to v0.13.2 ([#14869](https://github.com/ghostty-org/ghostty/issues/14869)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Just a small update that I did to catch a bit of missing API that I
  wanted to expose in `Context`, nothing that affects Ghostty, however.
  
  Had to skip 0.13.1 because of an issue with my release tooling.
  :man_facepalming:
  ```
- [`86d9721`](https://github.com/ghostty-org/ghostty/commit/86d97211ae167da14d38d8f30064f7802094b9c8) terminal: implement DECIC, DECDC, DECBI, and DECFI ([#14884](https://github.com/ghostty-org/ghostty/issues/14884)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add the VT420 horizontal scrolling sequences:
  
  - DECIC (CSI Pn ' }) inserts columns at the cursor in every row of the
  scrolling region.
  - DECDC (CSI Pn ' ~) deletes columns at the cursor in every row of the
  scrolling region.
  - DECBI (ESC 6) moves the cursor left, or at the left margin scrolls the
  region right.
  - DECFI (ESC 9) moves the cursor right, or at the right margin scrolls
  the region left, losing the column at the left margin.
  
  DECIC and DECDC do nothing when the cursor is outside the scrolling
  region. The new stream actions are appended to the C ABI action list so
  that existing values are unchanged.
  
  This fixes 20 esctest failures (DECICTests, DECDCTests, DECBITests, and
  DECFITests now pass in full).
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`20ba646`](https://github.com/ghostty-org/ghostty/commit/20ba6462d7de682a43839a469717f0cf3d5ceb5a) datastruct/split_tree: assert goto() is given a valid handle ([#14904](https://github.com/ghostty-org/ghostty/issues/14904)) ([@jcollie](https://github.com/jcollie))
  ```text
  `SplitTree.goto()` indexes `self.nodes` / the spatial slots with `from`
  without checking it. On an empty tree, `.previous_wrapped`,
  `.next_wrapped` and `.spatial` hit `index out of bounds: index 0, len
  0`; `.previous` and `.next` just return null.
  
  This is not reachable today: the only caller, the GTK
  `SplitTree.goto()`, gets `from` from `getActiveSurfaceHandle()`, which
  returns null for an empty tree, so it bails out first. So this is not a
  bug fix, only the contract made explicit, the same way `remove()`
  asserts `at.idx() < self.nodes.len`:
  
  - doc comment: `from` must be a valid handle, so the tree must not be
  empty
  - `assert(from.idx() < self.nodes.len)` at the top of `goto()`
  
  I first sent a `return null` guard with a test and overstated the
  impact; this replaces it. Can close it if you'd rather not have the
  assert.
  
  Tested: `zig build test -Dtest-filter=SplitTree`, `zig fmt --check`.
  
  AI disclosure: written with LM-based assistants - Antigravity for the
  first version, Opus for the slightly improved rework. I reviewed the
  changeset of both.
  ```
- [`50e5d21`](https://github.com/ghostty-org/ghostty/commit/50e5d217817e03df64f9af018540b88b6780b087) example: bump minimum zig version to 0.17.0 ([@paaloeye](https://github.com/paaloeye))
- [`6ba1441`](https://github.com/ghostty-org/ghostty/commit/6ba144158577d033ccb6ed4b574e4013957c9161) example: bump minimum zig version to 0.17.0 ([#14893](https://github.com/ghostty-org/ghostty/issues/14893)) ([@jcollie](https://github.com/jcollie))

## October 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40584098988), [2](https://github.com/ghostty-org/ghostty/actions/runs/40568497398), [3](https://github.com/ghostty-org/ghostty/actions/runs/40546649739), [4](https://github.com/ghostty-org/ghostty/actions/runs/40541589904), [5](https://github.com/ghostty-org/ghostty/actions/runs/40535055733), [6](https://github.com/ghostty-org/ghostty/actions/runs/40526449383), [7](https://github.com/ghostty-org/ghostty/actions/runs/40450332918)  
Summary: 7 runs • 19 commits • 6 authors

### Changes

- [`5c1d15f`](https://github.com/ghostty-org/ghostty/commit/5c1d15f9b571982afe4376e8cb38b6f3fbb52bc0) config: prevent panic on truncated UTF-8 ([@12ya](https://github.com/12ya))
  ```text
  #14879
  
  Check that the full UTF-8 sequence is available before slicing it so
  truncated configuration strings return InvalidString instead of panicking.
  Cover incomplete two-, three-, and four-byte sequences and verify that
  SelectionWordChars.parseCLI reports InvalidValue.
  ```
- [`46e9dc9`](https://github.com/ghostty-org/ghostty/commit/46e9dc9a927b2e7e7cba79e6902c176127dbdf2c) config: prevent panic on truncated UTF-8 ([#14879](https://github.com/ghostty-org/ghostty/issues/14879)) ([@jcollie](https://github.com/jcollie))
  ```text
  `CodepointIterator` could panic on incomplete UTF-8, such as a lone 0xC2
  byte, when slicing beyond the available input.
  
  Check the remaining byte count before slicing and return `InvalidString`
  for truncated sequences. Test incomplete two-, three-, and four-byte
  sequences in the iterator and `SelectionWordChars.parseCLI`.
  
  Validation:
  - `zig build test -Dtest-filter=SelectionWordChars
  -Dtest-filter=codepointIterator -Demit-macos-app=false`: 91 tests
  passed.
  - Standalone string helper tests: 13 passed.
  - Formatting and whitespace checks passed.
  
  AI disclosure: OpenAI Codex assisted with the code, tests, and PR
  description.
  ```
- [`241a7bc`](https://github.com/ghostty-org/ghostty/commit/241a7bca3b14fa3a136dfb9860eb0d9d183bb3f4) cli: fix Unicode escape validation ([@12ya](https://github.com/12ya))
  ```text
  #14876
  
  Interpret hexadecimal letters as 10 through 15 when checking Unicode
  escapes so oversized values are rejected.
  
  Cover lowercase and uppercase letters in quoted and unquoted escapes.
  Run quoted cases on every platform.
  ```
- [`b84594f`](https://github.com/ghostty-org/ghostty/commit/b84594f9783e9ca924ba7c703ab7d633b38c4bbe) build: fix the snap and flatpak builds ([@mitchellh](https://github.com/mitchellh))
  ```text
  These have been broken since Zig 0.17, I think snap since before that.
  
  The snap moves to core26 (Ubuntu 26.04), which ships new enough GTK,
  libadwaita, and harfbuzz. It also uses the system gtk4-layer-shell now
  that Ubuntu packages it, and redirects `-lbzip2` to `libbz2.so` with a
  one-line linker script, the same way the flatpak already does.
  ```
- [`b840b24`](https://github.com/ghostty-org/ghostty/commit/b840b2457cc0f5ee63cb324b3af9bb8e753e512c) cli: fix Unicode escape validation ([#14876](https://github.com/ghostty-org/ghostty/issues/14876)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fix hexadecimal letter conversion in CommaSplitter's Unicode escape
  validation. Letters a-f and A-F were interpreted as 0-5 instead of
  10-15, allowing oversized escapes such as \u{aaaaaa} to pass validation.
  
  Add regression tests for lowercase and uppercase escapes.
  
  Validation:
  - Standalone tests: 27 passed, 3 Windows tests skipped.
  - Formatting: passed.
  
  AI assistance: Used OpenAI Codex for diagnosis, explanations, code/test
  suggestions, validation, and PR wording.
  ```
- [`919dca5`](https://github.com/ghostty-org/ghostty/commit/919dca5c848d43a489a4cb2e1feade016f0fa2db) build: fix the snap and flatpak builds ([#14881](https://github.com/ghostty-org/ghostty/issues/14881)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  These have been broken since Zig 0.17, I think snap since before that.
  
  The snap moves to core26 (Ubuntu 26.04), which ships new enough GTK,
  libadwaita, and harfbuzz. It also uses the system gtk4-layer-shell now
  that Ubuntu packages it, and redirects `-lbzip2` to `libbz2.so` with a
  one-line linker script, the same way the flatpak already does.
  ```
- [`4a4fc01`](https://github.com/ghostty-org/ghostty/commit/4a4fc017940bec38c93b278c10c6a18c591f3e63) up to 1.4.1-dev ([@mitchellh](https://github.com/mitchellh))
- [`83fb956`](https://github.com/ghostty-org/ghostty/commit/83fb95624b0439ee660c2679b43b38c8b63769cd) Bump version to 1.4.0 ([@mitchellh](https://github.com/mitchellh))
- [`155bbbe`](https://github.com/ghostty-org/ghostty/commit/155bbbe5343d6579a20121673702937cee96572f) i18n: polish the Polish ([@Rayzerrek](https://github.com/Rayzerrek))
- [`d87c497`](https://github.com/ghostty-org/ghostty/commit/d87c497aff312f8bfcaeffbb53813dcccea4492b) i18n: polish the Polish ([#14874](https://github.com/ghostty-org/ghostty/issues/14874)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Picked from #14598
  ```
- [`c46e292`](https://github.com/ghostty-org/ghostty/commit/c46e292eda4fb217fbbc2763a7ed6f73f04db4de) Update VOUCHED list ([#14878](https://github.com/ghostty-org/ghostty/issues/14878)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14877#discussioncomment-19221073)
  from @jcollie.
  
  Vouch: @rtgibbons
  ```
- [`f9c3b20`](https://github.com/ghostty-org/ghostty/commit/f9c3b20f7ecb8fe145e595469b62841c8fe5cb7d) macOS: increase test coverage for NSPasteboard ([@francislata](https://github.com/francislata))
- [`a732580`](https://github.com/ghostty-org/ghostty/commit/a7325808ad17249b356824102c4c0e917352b686) macOS: increase test coverage for NSPasteboard ([#14870](https://github.com/ghostty-org/ghostty/issues/14870)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Picked and amended from #14868
  ```
- [`99dae4d`](https://github.com/ghostty-org/ghostty/commit/99dae4d8700a63040b4131a5b43bf7f50d5d13d8) ci: add freebsd builds for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
- [`445e234`](https://github.com/ghostty-org/ghostty/commit/445e23496414d870a0407d145b285381fc031bc1) some freebsd fixes ([@mitchellh](https://github.com/mitchellh))
- [`f13b528`](https://github.com/ghostty-org/ghostty/commit/f13b52851a744f14cb22101dc29d78babdc6e656) terminal: memory decommit/recommit for FreeBSD ([@mitchellh](https://github.com/mitchellh))
- [`4d429ec`](https://github.com/ghostty-org/ghostty/commit/4d429ecfdeed4e08473602a3071fda897cd18a39) ci: run libghostty-vt tests in CI ([@mitchellh](https://github.com/mitchellh))
- [`1b9bb3a`](https://github.com/ghostty-org/ghostty/commit/1b9bb3aeb1236e2151539c695fbb03e171fe1e4c) build: -Demit-test-exe only emits the libghostty c tests for libghostty ([@mitchellh](https://github.com/mitchellh))
- [`68640f3`](https://github.com/ghostty-org/ghostty/commit/68640f3049d5ae76d7d5eebb5bbdf713a3a98713) libghostty-vt: support FreeBSD, test in CI ([#14867](https://github.com/ghostty-org/ghostty/issues/14867)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for FreeBSD to libghostty-vt and validates it in CI.
  
  There were only a few places we really need to make compatibility fixes:
  
  - The memory decommit/recommit stuff, which is very OS specific.
  - Kitty graphics shared memory paths
  - TinyIO, one method
  ```

## October 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40396684066), [2](https://github.com/ghostty-org/ghostty/actions/runs/40393630080), [3](https://github.com/ghostty-org/ghostty/actions/runs/40389935061), [4](https://github.com/ghostty-org/ghostty/actions/runs/40364482308), [5](https://github.com/ghostty-org/ghostty/actions/runs/40361578719), [6](https://github.com/ghostty-org/ghostty/actions/runs/40359380687), [7](https://github.com/ghostty-org/ghostty/actions/runs/40330121151), [8](https://github.com/ghostty-org/ghostty/actions/runs/40267247680), [9](https://github.com/ghostty-org/ghostty/actions/runs/40259139232)  
Summary: 9 runs • 38 commits • 9 authors

### Changes

- [`9ee02ae`](https://github.com/ghostty-org/ghostty/commit/9ee02ae601d3eec567723287e1c20bd0e9f1489c) i18n: Irish translation for Ghostty 1.4 ([#13837](https://github.com/ghostty-org/ghostty/issues/13837)) ([@aindriu80](https://github.com/aindriu80))
- [`afbbbe1`](https://github.com/ghostty-org/ghostty/commit/afbbbe15887c8a83db9c3f1df30411bbfff87bd0) macos/applescript: add AppleScript name override property ([@paaloeye](https://github.com/paaloeye))
  ````text
  - expose read-write `name override` property on tab and terminal classes in Ghostty.sdef
  - implement `titleOverride` accessors in `ScriptTab` and `ScriptTerminal`
  - add `titleOverride` property to `SurfaceView` to manage manual terminal title overrides
  - fix minor inconsistencies in comments
  
  AppleScript API usage:
  
  ```applescript
  -- Setting and clearing a tab name override via AppleScript
  tell application "Ghostty"
      -- Target the selected tab of the front window
      set targetTab to selected tab of front window
  
      -- Set name override
      set name override of targetTab to "My Custom Tab Title"
      log "Tab title: " & (name of targetTab)
      log "Tab override: " & (name override of targetTab)
      delay 2.0 -- delay is here only for illustrative purposes
  
      -- Clear override
      set name override of targetTab to ""
  end tell
  ```
  
  AI disclosure: Antigravity CLI was used for the first draft. Iterated, minimised, reviewed, and tested by me.
  
  Closes: https://github.com/ghostty-org/ghostty/issues/12048
  Discussion: https://github.com/ghostty-org/ghostty/discussions/12047
  Agent-Session: cdd11bbe-928a-4a00-a085-c8f87a57966f
  ````
- [`b279b2c`](https://github.com/ghostty-org/ghostty/commit/b279b2ccb8f6d7bb86afa44bd5bf5529c29fdce0) macos: clear split zoom indicator when tree is not split ([@paaloeye](https://github.com/paaloeye))
  ```text
  When closing sibling splits down to a single terminal leaf while
  zoomed via AppleScript, `SplitTree` retained its zoomed node
  reference because the target being removed was not the zoomed node itself.
  
  Because the tree was no longer split but the zoomed property remained non-nil,
  the window's zoom state stayed active and the reset zoom indicator remained visible.
  
  `SplitTree` now validates that a tree can only have a zoomed node if
  it actually contains splits and the zoomed node exists in root. In
  addition, `SplitTree` exposes an `isZoomed` property, and the terminal
  controller and window reactively update the zoom state and accessory
  controls accordingly.
  
  AI disclosure: Antigravity CLI wrote the tests initially. Iterated, reviewed, and tested by me.
  ```
- [`91d198c`](https://github.com/ghostty-org/ghostty/commit/91d198cc32b6056fede5625e0c60302d01bbb846) macos/applescript: add AppleScript name override property ([#14733](https://github.com/ghostty-org/ghostty/issues/14733)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  - expose read-write `name override` property on tab and terminal classes
  in Ghostty.sdef
  - implement `titleOverride` accessors in `ScriptTab` and
  `ScriptTerminal`
  - add `titleOverride` property to `SurfaceView` to manage manual
  terminal title overrides
  - fix minor inconsistencies in comments
  
  AppleScript API usage:
  
  ```applescript
  -- Setting and clearing a tab name override via AppleScript
  tell application "Ghostty"
      -- Target the selected tab of the front window
      set targetTab to selected tab of front window
  
      -- Set name override
      set name override of targetTab to "My Custom Tab Title"
      log "Tab title: " & (name of targetTab)
      log "Tab override: " & (name override of targetTab)
      delay 2.0 -- delay is here only for illustrative purposes
  
      -- Clear override
      set name override of targetTab to ""
  end tell
  ```
  
  AI disclosure: Antigravity CLI was used for the first draft. Iterated,
  minimised, reviewed, and tested by me.
  
  Closes: https://github.com/ghostty-org/ghostty/issues/12048
  Discussion: https://github.com/ghostty-org/ghostty/discussions/12047
  ````
- [`18f0963`](https://github.com/ghostty-org/ghostty/commit/18f09635d9e2e27df1d332f49a82d27cdcc03a48) macos: clear split zoom indicator when tree is not split ([#14703](https://github.com/ghostty-org/ghostty/issues/14703)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  When closing sibling splits down to a single terminal leaf while zoomed
  via AppleScript, `SplitTree` retained its zoomed node reference because
  the target being removed was not the zoomed node itself.
  
  Because the tree was no longer split but the zoomed property remained
  non-nil, the window's zoom state stayed active and the reset zoom
  indicator remained visible.
  
  `SplitTree` now validates that a tree can only have a zoomed node if it
  actually contains splits and the zoomed node exists in root. In
  addition, `SplitTree` exposes an `isZoomed` property, and the terminal
  controller and window reactively update the zoom state and accessory
  controls accordingly.
  
  AI disclosure: Antigravity CLI wrote the tests initially. Iterated,
  reviewed, and tested by me.
  
  <details>
  <summary>UX before:</summary>
  <video
  src="https://github.com/user-attachments/assets/263557d1-1be8-41ca-9070-85075c659afb"
  width="100%"></video>
  </details>
  
  <details>
  <summary>UX after:</summary>
  <video
  src="https://github.com/user-attachments/assets/55ba6778-0901-4722-aa51-8ea0b0c83a1c"
  width="100%"></video>
  </details>
  
  Minimal reproducible example (MRE) using `AppleScript`:
  ```applescript
  tell application id "com.mitchellh.ghostty"
      activate
  
      -- Get the current focused terminal
      set t1 to focused terminal of selected tab of front window
  
      -- Create 4 splits (2x2 grid)
      --   [ t1 | t2 ]
      --   [ t3 | t4 ]
      set t2 to split t1 direction right
      delay 0.5
  
      set t3 to split t1 direction down
      delay 0.5
  
      set t4 to split t2 direction down
      delay 0.5
  
      -- Zoom one of the splits (t1)
      perform action "toggle_split_zoom" on t1
      delay 0.5
  
      -- Close other splits
      try
          close t4
      on error
          perform action "close_surface" on t4
      end try
      delay 0.2
  
      try
          close t3
      on error
          perform action "close_surface" on t3
      end try
      delay 0.2
  
      try
          close t2
      on error
          perform action "close_surface" on t2
      end try
  end tell
  ```
  ````
- [`6ce1e60`](https://github.com/ghostty-org/ghostty/commit/6ce1e605819a9db6f62efb6e1eb98fe1327c3a50) mirror deps ([@mitchellh](https://github.com/mitchellh))
- [`efc5105`](https://github.com/ghostty-org/ghostty/commit/efc51050badfff9a444e5f7750bca9d2ff379bf9) ci: use macOS Golden Gate with Xcode 27.1 ([@mitchellh](https://github.com/mitchellh))
- [`de956a2`](https://github.com/ghostty-org/ghostty/commit/de956a2c2f1c03efb314668e33db9a809097e5de) mirror deps ([#14861](https://github.com/ghostty-org/ghostty/issues/14861)) ([@mitchellh](https://github.com/mitchellh))
- [`da5936c`](https://github.com/ghostty-org/ghostty/commit/da5936c2287cd7f466acdad3cc000de5ce35ccaa) ci: use macOS Golden Gate with Xcode 27.1 ([#14862](https://github.com/ghostty-org/ghostty/issues/14862)) ([@mitchellh](https://github.com/mitchellh))
- [`6eb24a0`](https://github.com/ghostty-org/ghostty/commit/6eb24a0f0f38cabd24457b31c44d6b6bde5540f5) shell-integration: don't let directory names inject escape sequences ([@mitchellh](https://github.com/mitchellh))
  ```text
  The zsh integration reported the working directory with `print`, which
  expands backslash escapes in every argument, including `$PWD`. A
  directory named `x\a\e]52;c;SGVsbG8=\a` ended our OSC 7 early and sent
  a real OSC 52 sequence. A directory name containing a raw ESC or BEL
  byte did the same thing in both zsh and bash.
  
  zsh now uses `print -r` so backslashes in the path are printed as-is,
  and writes the ESC and BEL framing bytes with `$'...'` quoting. Both
  zsh and bash strip control bytes from the hostname and directory
  before sending them, the same way the zsh title code already does.
  Fish was already safe because it percent-encodes the path.
  ```
- [`ebd4499`](https://github.com/ghostty-org/ghostty/commit/ebd449995d321e90d6c73be3decb15558512b2ed) shell-integration: don't let directory names inject escape sequences ([#14859](https://github.com/ghostty-org/ghostty/issues/14859)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The zsh integration reported the working directory with `print`, which
  expands backslash escapes in every argument, including `$PWD`. A
  directory named `x\a\e]52;c;SGVsbG8=\a` ended our OSC 7 early and sent a
  real OSC 52 sequence. A directory name containing a raw ESC or BEL byte
  did the same thing in both zsh and bash.
  
  zsh now uses `print -r` so backslashes in the path are printed as-is,
  and writes the ESC and BEL framing bytes with `$'...'` quoting. Both zsh
  and bash strip control bytes from the hostname and directory before
  sending them, the same way the zsh title code already does. Fish was
  already safe because it percent-encodes the path.
  ```
- [`1851e12`](https://github.com/ghostty-org/ghostty/commit/1851e121baec1f02b31065a8c4ae3ee845bbc4d1) terminal/tmux: reject zero-sized and oversized panes in layouts ([@mitchellh](https://github.com/mitchellh))
  ```text
  A program running in the terminal can enter tmux control mode with
  `ESC P 1000 p` and then send its own `%layout-change` notifications or
  `list-windows` output. The layout parser accepted nodes with a width or
  height of zero, and the viewer cast pane sizes to `u16` without checking
  them.
  
  A bad layout now makes the tmux viewer defunct with a logged warning,
  the same as any other layout error, instead of crashing Ghostty. Real
  tmux never sends zero-sized panes, so normal sessions are unaffected.
  ```
- [`bf14ea1`](https://github.com/ghostty-org/ghostty/commit/bf14ea1fbda2d069112003b80ec3b9186b7688f6) terminal/tmux: reject zero-sized and oversized panes in layouts ([#14858](https://github.com/ghostty-org/ghostty/issues/14858)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A program running in the terminal can enter tmux control mode with `ESC
  P 1000 p` and then send its own `%layout-change` notifications or
  `list-windows` output. The layout parser accepted nodes with a width or
  height of zero, and the viewer cast pane sizes to `u16` without checking
  them.
  
  A bad layout now makes the tmux viewer defunct with a logged warning,
  the same as any other layout error, instead of crashing Ghostty. Real
  tmux never sends zero-sized panes, so normal sessions are unaffected.
  ```
- [`297ff52`](https://github.com/ghostty-org/ghostty/commit/297ff52922127fd7a2b7f8fe856d39f2b48ace07) gtk: implement the Kitty clipboard protocol (OSC 5522) ([@jcollie](https://github.com/jcollie))
  ```text
  Implement the kitty_read, kitty_write, and list (paste event) requests
  in the GTK apprt on top of the existing core protocol support, and wire
  the confirmation dialog up to Kitty requests, including session-grant
  remember support.
  
  Also fix two adjacent issues found while testing: the clipboard-write
  signal now carries a "cleared" flag so image-only writes toast as
  copies instead of clears, and a failed OSC 52 text read now answers
  with an empty reply instead of leaving the client waiting forever.
  
  TODO: the new remember-row strings in the confirmation dialog are
  deliberately not marked for translation; wrap them in i18n._() and
  regenerate the translation files once they should be translated.
  ```
- [`54b6544`](https://github.com/ghostty-org/ghostty/commit/54b65443e0247280ce2d4826c02870f887166578) gtk: show an image preview in the clipboard confirmation dialog ([@jcollie](https://github.com/jcollie))
  ```text
  Decode the first image/* representation of a Kitty clipboard request
  with gdk_texture_new_from_bytes and show it in the dialog in place of
  the text preview, falling back to the text preview when there is no
  decodable image. The picture's paintable and the visible preview page
  are bound declaratively to the clipboard-image property.
  ```
- [`3ea78b0`](https://github.com/ghostty-org/ghostty/commit/3ea78b066715891e9855d56644c9fd9b04335227) gtk: fix crash denying an OSC 52 read with "remember" checked ([@jcollie](https://github.com/jcollie))
  ```text
  Remembering the denial set clipboard-read to deny before the request was
  answered, and the OSC 52 reply is written by the same path that serves an
  allowed read, which asserts reads aren't denied.
  ```
- [`1ebbfe9`](https://github.com/ghostty-org/ghostty/commit/1ebbfe9a1996b29d4c4561be7ae977d2fddc7a30) gtk: preview every representation of a clipboard request ([@jcollie](https://github.com/jcollie))
  ```text
  A multipart payload was reduced to one preview — the first decodable
  image, else the first text, else a bare list of MIME types — so the user
  authorized data they were never shown. The dialog now gives each
  representation its own page, named by MIME type.
  ```
- [`1306fab`](https://github.com/ghostty-org/ghostty/commit/1306fab94d15f1b01ddfba5644f695610697bde6) test: wait for the clipboard status reply ([@jcollie](https://github.com/jcollie))
  ```text
  The script exited as soon as it had written the transaction, so the
  terminal's status packet arrived with nothing left to read it and
  printed itself on the next shell prompt. It also carries a name and a
  session password now, so a run exercises the permission prompt.
  ```
- [`7169fea`](https://github.com/ghostty-org/ghostty/commit/7169fea55bfd58a57e4139fd90300cc93f8d187f) gtk: reword the Kitty clipboard remember subtitle ([@jcollie](https://github.com/jcollie))
- [`a6a1a46`](https://github.com/ghostty-org/ghostty/commit/a6a1a4664237841dc171da28686be256ef92cf3e) terminal: mark pins on erased history rows as garbage ([@noib3](https://github.com/noib3))
- [`b97e426`](https://github.com/ghostty-org/ghostty/commit/b97e42691c44bc0e35eb7750b06273145f89c4dc) set TERM for +ssh without clobbering the user's SetEnv ([@mitchellh](https://github.com/mitchellh))
  ```text
  `+ssh` passed `-o SetEnv=TERM=...` to ssh. ssh only uses the first
  SetEnv it finds, so the one on the command line replaced every SetEnv
  entry in the user's ssh config. This brings back the bug that #11518
  fixed in the old shell integration wrapper, now in `+ssh` (#12582).
  
  `TERM` was also only set with `--forward-env`, so `--forward-env=false`
  (what `ssh-terminfo`-only users get) left the inherited
  `TERM=xterm-ghostty` in place even when the terminfo install failed.
  
  ssh sends the SetEnv entries in the user's ssh config again, and
  a failed terminfo install falls back to `xterm-256color` like it
  did in 1.3.1, no matter which `ssh-*` features are enabled.
  
  `TERM` is now set in the environment of the ssh process instead of
  with SetEnv, the same way the 1.3.1 wrapper did. ssh sends `TERM` on
  its own when it opens a remote terminal, so the server doesn't need
  `AcceptEnv TERM`. This happens whenever `--forward-env` or
  `--terminfo` is enabled. With both disabled, ssh runs with the user's
  environment unchanged. The `+ssh` help is updated to explain how
  `TERM` is chosen.
  
  Docs: https://man.openbsd.org/ssh_config#SetEnv
  ```
- [`9438bd3`](https://github.com/ghostty-org/ghostty/commit/9438bd3e54931b1aceefc6037dc0674f4b844bf6) terminal: mark pins on erased history rows as garbage ([#14838](https://github.com/ghostty-org/ghostty/issues/14838)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR makes tracked grid refs report no value when the history row
  they point to is erased (e.g. by `CSI 3 J`), the same way they already
  do when the row is pruned.
  
  That's what the
  [docs](https://github.com/ghostty-org/ghostty/blob/cec8b92/include/ghostty/vt/grid_ref.h#L52-L58)
  describe, but erased refs were silently moved to the top-left of the
  remaining rows instead, so callers couldn't tell their row was gone.
  
  AI disclosure: I used Claude to investigate the issue, write the change
  and add/update tests. I understand what it did, and I wrote this PR
  description.
  ```
- [`1607438`](https://github.com/ghostty-org/ghostty/commit/16074385fa98fdbf54fb09182bb93635ceb97ee4) deps: update z2d to v0.13.0 ([@vancluever](https://github.com/vancluever))
  ```text
  Release notes at:
   https://github.com/vancluever/z2d/blob/v0.13.0/CHANGELOG.md
  
  A few bug fixes that will ultimately pertain to Ghostty's use of z2d,
  but there is a bunch more utility now for text shaping and path
  serialization that could prove useful in a pinch. :) This release also
  now puts Zig 0.17.0 support at a stable tag.
  
  The tarball commit hash here is the tag's corresponding commit.
  ```
- [`37b7101`](https://github.com/ghostty-org/ghostty/commit/37b71016bffab818bcda8be60efe808882c7b947) set TERM for +ssh without clobbering the user's SetEnv ([#14854](https://github.com/ghostty-org/ghostty/issues/14854)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `+ssh` passed `-o SetEnv=TERM=...` to ssh. ssh only uses the first
  SetEnv it finds, so the one on the command line replaced every SetEnv
  entry in the user's ssh config. This brings back the bug that #11518
  fixed in the old shell integration wrapper, now in `+ssh` (#12582).
  
  `TERM` was also only set with `--forward-env`, so `--forward-env=false`
  (what `ssh-terminfo`-only users get) left the inherited
  `TERM=xterm-ghostty` in place even when the terminfo install failed.
  
  ssh sends the SetEnv entries in the user's ssh config again, and a
  failed terminfo install falls back to `xterm-256color` like it did in
  1.3.1, no matter which `ssh-*` features are enabled.
  
  `TERM` is now set in the environment of the ssh process instead of with
  SetEnv, the same way the 1.3.1 wrapper did. ssh sends `TERM` on its own
  when it opens a remote terminal, so the server doesn't need `AcceptEnv
  TERM`. This happens whenever `--forward-env` or `--terminfo` is enabled.
  With both disabled, ssh runs with the user's environment unchanged. The
  `+ssh` help is updated to explain how `TERM` is chosen.
  
  Docs: https://man.openbsd.org/ssh_config#SetEnv
  ```
- [`79bd880`](https://github.com/ghostty-org/ghostty/commit/79bd880d6b0dfbad5a9505fa88ab2b3c598efefe) gtk: implement kitty clipboard protocol ([#14061](https://github.com/ghostty-org/ghostty/issues/14061)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR wires up the kitty clipboard protocol in the GTK apprt after all
  of the work to implement the protocol in the core and the macOS apprt.
  Adds an image preview to the confirmation dialog.
  
  Since we are in string freeze for 1.4, two new strings added for the
  confirmation dialog were not marked for translation. Once 1.4 is
  released they can be marked for translation for 1.5.
  
  Fixes #10549
  
  AI disclosure: Claude Fable 5 was used to develop this PR but the author
  has thoroughly reviewed the code and has rewritten sections.
  ```
- [`4bcd00d`](https://github.com/ghostty-org/ghostty/commit/4bcd00d636e2a8156135dfaebdd99f900664aa39) deps: update z2d to v0.13.0 ([#14855](https://github.com/ghostty-org/ghostty/issues/14855)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release notes at:
   https://github.com/vancluever/z2d/blob/v0.13.0/CHANGELOG.md
  
  A few bug fixes that will ultimately pertain to Ghostty's use of z2d,
  but there is a bunch more utility now for text shaping and path
  serialization that could prove useful in a pinch.
  :slightly_smiling_face: This release also now puts Zig 0.17.0 support at
  a stable tag.
  
  The tarball commit hash here is the tag's corresponding commit.
  ```
- [`84983d0`](https://github.com/ghostty-org/ghostty/commit/84983d060db826a07501c4fc4b7165233ba0df6d) terminal: cap the rows computed by Capacity.adjust ([@mitchellh](https://github.com/mitchellh))
  ```text
  `Capacity.adjust` computed how many rows fit in the page's memory at
  the new column count and stored that number in a 16-bit row count
  without checking it. Narrowing a very wide page can free room for
  more than 65535 rows.
  
  `adjust` now caps the row count at the largest value a page can hold
  before fitting rows to the memory size. This matches the cap that
  `maxCols` already applies to columns. U
  ```
- [`e257bb4`](https://github.com/ghostty-org/ghostty/commit/e257bb45e6d4d61c14eacdc717be89c6110f99ff) terminal: keep cursor style and hyperlink valid after scrollClear prunes ([@mitchellh](https://github.com/mitchellh))
  ```text
  `scrollClear` now checks whether the cursor pin changed pages. If it
  did, it clears the pin's garbage flag and calls `cursorPageReplaced`,
  which registers the style and hyperlink on the new page without
  touching the freed one. This matches how `cursorDownScroll` already
  handles the single row case. The doc comment for `scrollClear` is also
  rewritten to describe where the cursor ends up.
  ```
- [`0af5c9e`](https://github.com/ghostty-org/ghostty/commit/0af5c9e55c5b790de15aa7c7fcd90472b41c53cd) terminal: cap the rows computed by Capacity.adjust ([#14856](https://github.com/ghostty-org/ghostty/issues/14856)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `Capacity.adjust` computed how many rows fit in the page's memory at the
  new column count and stored that number in a 16-bit row count without
  checking it. Narrowing a very wide page can free room for more than
  65535 rows.
  
  `adjust` now caps the row count at the largest value a page can hold
  before fitting rows to the memory size. This matches the cap that
  `maxCols` already applies to columns. U
  ```
- [`1c2ea72`](https://github.com/ghostty-org/ghostty/commit/1c2ea72225e4c4f64dee4411f52035ecf23f336b) terminal: keep cursor style and hyperlink valid after scrollClear prunes ([#14857](https://github.com/ghostty-org/ghostty/issues/14857)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `scrollClear` now checks whether the cursor pin changed pages. If it
  did, it clears the pin's garbage flag and calls `cursorPageReplaced`,
  which registers the style and hyperlink on the new page without touching
  the freed one. This matches how `cursorDownScroll` already handles the
  single row case. The doc comment for `scrollClear` is also rewritten to
  describe where the cursor ends up.
  ```
- [`f63124c`](https://github.com/ghostty-org/ghostty/commit/f63124ca3a8d28d63d1e12d8a93d8932037174da) fontconfig: handle when lang is string and not langset ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fontconfig accepts strings when a langset is expected. This by itself is
  not a problem. But for some ungodly reason it can also *return* a string
  in place of a langset, for example when a `FcPattern` doesn't match any
  language and it falls back to `"en"`. Just why would you do this? What
  reason can there ever be to do this??????
  ```
- [`8112f76`](https://github.com/ghostty-org/ghostty/commit/8112f7676007b7823798f8a1259ab274058e8bf6) fontconfig: handle when lang is string and not langset ([#14853](https://github.com/ghostty-org/ghostty/issues/14853)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fontconfig accepts strings when a langset is expected. This by itself is
  not a problem. But for some ungodly reason it can also *return* a string
  in place of a langset, for example when a `FcPattern` doesn't match any
  language and it [falls
  back](https://github.com/fontconfig/fontconfig/blob/b25ffeabd15b76f86c0c6736f6df2f1b89858010/src/fccfg.c#L2062-L2065)
  to `"en"`. Just why would you do this? What reason can there ever be to
  do this??????
  ```
- [`297507f`](https://github.com/ghostty-org/ghostty/commit/297507f498ef6fd33b7514e143e2d641144457a4) termio: send the config change color scheme report directly ([@jcollie](https://github.com/jcollie))
  ```text
  StreamHandler.changeConfig queued a color_scheme_report message into the
  termio mailbox. changeConfig runs on the io thread, which is the only
  reader of that mailbox, so when the mailbox was full (for example, from
  a burst of query replies queued by the reader thread) the io thread
  blocked forever pushing to itself. Every other thread then blocked on
  its next send to the same mailbox, freezing Ghostty on a config reload.
  
  Write the report from Termio.changeConfig instead, using the same
  colorSchemeReportLocked the message handler uses. The report still
  follows the config update in order with other output.
  
  Fixes: #14833
  ```
- [`509e5fb`](https://github.com/ghostty-org/ghostty/commit/509e5fbec4ddf78f884b4cd21a8a4d7346636d44) macos: fix flash of neighbor tab when moving titlebar tabs ([@lehni](https://github.com/lehni))
  ```text
  With titlebar tabs on macOS 26, move_tab removed the selected tab from its group and added it back at the new position. Removing the selected tab makes AppKit select and draw a neighbor until the tab is made key again, which showed up as a flash of the other tab's content. Instead, move the tabs being passed over to the other side of the selected tab, so the selected tab never leaves the group.
  ```
- [`87b6596`](https://github.com/ghostty-org/ghostty/commit/87b65966dfadc42dacd8d55b99ebc430e6a52455) termio: send the config change color scheme report directly ([#14834](https://github.com/ghostty-org/ghostty/issues/14834)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  StreamHandler.changeConfig queued a color_scheme_report message into the
  termio mailbox. changeConfig runs on the io thread, which is the only
  reader of that mailbox, so when the mailbox was full (for example, from
  a burst of query replies queued by the reader thread) the io thread
  blocked forever pushing to itself. Every other thread then blocked on
  its next send to the same mailbox, freezing Ghostty on a config reload.
  
  Write the report from Termio.changeConfig instead, using the same
  colorSchemeReportLocked the message handler uses. The report still
  follows the config update in order with other output.
  
  Fixes: #14833
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`0fe113a`](https://github.com/ghostty-org/ghostty/commit/0fe113a35370667d8c4d6970ee5c1704825dce6b) macos: fix flash of neighbor tab when moving titlebar tabs ([#14847](https://github.com/ghostty-org/ghostty/issues/14847)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With `macos-titlebar-style = tabs` on macOS 26, `move_tab` briefly shows
  the content of the neighboring tab before the moved tab is shown again.
  
  The macOS 26 workaround from 09246780b removes the selected tab from its
  tab group and adds it back at the new position, then makes it key on the
  next run loop turn. Removing the selected tab makes AppKit select and
  draw a neighbor in the meantime, which is the flash.
  
  This instead moves the tabs that are passed over to the other side of
  the selected tab. The selected tab never leaves the group and stays
  selected throughout, so nothing else is drawn. The resulting order is
  the same as before, and the titlebar glitches the workaround was added
  for don't come back in my testing.
  
  Only the macOS 26 titlebar tabs path changes. The path for the other
  window styles is untouched.
  
  ## Before
  
  
  https://github.com/user-attachments/assets/2de82693-98bb-4c48-b05d-6abd87935584
  
  ## After
  
  
  https://github.com/user-attachments/assets/e4d829a3-71de-46cd-a1fd-2b46cb6e7e4d
  
  ## AI disclosure
  
  Diagnosed and written with Claude Code. I reviewed the change and tested
  it by hand on macOS 26 with titlebar tabs.
  ```
- [`d773509`](https://github.com/ghostty-org/ghostty/commit/d7735095de636a7014651e23e94620f498979233) build(deps): bump cachix/install-nix-action from 31.11.2 to 31.11.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.2 to 31.11.3.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/448cde739abec1eaf0646249e3d25bb8d9bc7702...75c75c31ebece974e48ebc36b4ad125bd97bd97b)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`3aec944`](https://github.com/ghostty-org/ghostty/commit/3aec9443422758d2cadb90d50ede788a599d633f) build(deps): bump cachix/install-nix-action from 31.11.2 to 31.11.3 ([#14851](https://github.com/ghostty-org/ghostty/issues/14851)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.2 to 31.11.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>31.11.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.3 -&gt; 2.35.4 by <a
  href="https://github.com/xokdvium"><code>@​xokdvium</code></a> in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/283">cachix/install-nix-action#283</a>
  <strong>Security</strong>: Updates the bundled certificates shipped with
  the installer to remove the compromised eMudhra certificates.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.2...31.11.3">https://github.com/cachix/install-nix-action/compare/v31.11.2...31.11.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/75c75c31ebece974e48ebc36b4ad125bd97bd97b"><code>75c75c3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/283">#283</a>
  from xokdvium/cacert-bump</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/37360376014064afef043dd1cddb9f6710a05e63"><code>3736037</code></a>
  nix: 2.35.3 -&gt; 2.35.4</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/448cde739abec1eaf0646249e3d25bb8d9bc7702...75c75c31ebece974e48ebc36b4ad125bd97bd97b">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.2&new-version=31.11.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## October 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40229290745), [2](https://github.com/ghostty-org/ghostty/actions/runs/40225977480), [3](https://github.com/ghostty-org/ghostty/actions/runs/40157524465)  
Summary: 3 runs • 9 commits • 4 authors

### Changes

- [`f63508e`](https://github.com/ghostty-org/ghostty/commit/f63508e5a1e0b3a5ce2f6cff591339e5b871aea0) Update VOUCHED list ([#14848](https://github.com/ghostty-org/ghostty/issues/14848)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14846#discussioncomment-19183173)
  from @jcollie.
  
  Vouch: @lehni
  ```
- [`fb13fa9`](https://github.com/ghostty-org/ghostty/commit/fb13fa9602f47590ccfaaea4cd8e178fac2ec8cc) Update VOUCHED list ([#14845](https://github.com/ghostty-org/ghostty/issues/14845)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14844#discussioncomment-19182684)
  from @jcollie.
  
  Denounce: @ifmael
  ```
- [`17001b8`](https://github.com/ghostty-org/ghostty/commit/17001b8f23ea548276c55df84bba720f82561c07) gtk: never resize a split smaller than one cell ([@thomasfedb](https://github.com/thomasfedb))
  ```text
  Also clamp keyboard split resizes to the split size, which fixed an
  assertion failure when resize_split moved past the edge of a split.
  ```
- [`cc84a42`](https://github.com/ghostty-org/ghostty/commit/cc84a42f9c6d0e7b7281d8fe2e7bb79872000b8d) gtk: clamp the split position and keep the ratio in sync ([@thomasfedb](https://github.com/thomasfedb))
- [`859f06f`](https://github.com/ghostty-org/ghostty/commit/859f06fc99c8f01d78ba1c1fced0079dd533ab92) gtk: update the split minimum when the config changes ([@thomasfedb](https://github.com/thomasfedb))
- [`79fecfa`](https://github.com/ghostty-org/ghostty/commit/79fecfa62d3d84da8a68ca68683f52f401e42669) gtk: keep split ratios on window resize and sync on min-position ([@thomasfedb](https://github.com/thomasfedb))
- [`59e565e`](https://github.com/ghostty-org/ghostty/commit/59e565ea0be6f133763540e33300effea40266e8) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`1ee9b25`](https://github.com/ghostty-org/ghostty/commit/1ee9b25636335521deca003e582fb3ea28fd31b8) Update iTerm2 colorschemes ([#14835](https://github.com/ghostty-org/ghostty/issues/14835)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261019-151001-86a776d
  ```
- [`cec8b92`](https://github.com/ghostty-org/ghostty/commit/cec8b92f1ecd176a20a56aa405021e7ae991b996) gtk: never resize a split smaller than one cell ([#14476](https://github.com/ghostty-org/ghostty/issues/14476)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes a regression of #1297 on GTK.
  
  **Issue**
  Splits can be dragged or resized down to 0px, which just looks like a
  thick divider. The 10px minimum from #1323 was lost in the GTK rewrite.
  
  **Fix**
  Splits are now at least one cell plus padding in size, and the divider
  can't be dragged past that. This also clamps keyboard resizes.
  
  Tested on Fedora 44. Dragging and `resize_split` stop at one column or
  line. I believe that macOS already has its own minimum and is unchanged.
  
  First pass written with Claude Code (Claude Opus 5.5), reviewed and
  reprompted by me.
  ```

## October 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40135767958), [2](https://github.com/ghostty-org/ghostty/actions/runs/40048552838)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`9cac2bd`](https://github.com/ghostty-org/ghostty/commit/9cac2bd0cf5a4de233e05851d1aaa1347f5baf7f) terminal/kitty: remove placements in erased history ([@jcollie](https://github.com/jcollie))
  ```text
  Erasing scrollback (ED3) moved Kitty image placements anchored in the
  erased rows onto the top-left of the active area, where they became
  visible again until the next screen clear. PageList.eraseRows moves
  tracked pins in erased rows to the top-left of the retained rows
  without marking them garbage, so the image storage never noticed the
  placement had lost its row.
  
  Remove pin-backed placements in the erased history range (and any
  relative placements orphaned by that) before erasing the rows, while
  their pins still identify them. The PageList pin semantics are left
  unchanged since search relies on erased pins not being garbage.
  
  Fixes: #14831
  ```
- [`bcfe577`](https://github.com/ghostty-org/ghostty/commit/bcfe5775454aebe2103e4dde906177b54fe61a94) terminal/kitty: remove placements in erased history ([#14832](https://github.com/ghostty-org/ghostty/issues/14832)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erasing scrollback (ED3) moved Kitty image placements anchored in the
  erased rows onto the top-left of the active area, where they became
  visible again until the next screen clear. PageList.eraseRows moves
  tracked pins in erased rows to the top-left of the retained rows without
  marking them garbage, so the image storage never noticed the placement
  had lost its row.
  
  Remove pin-backed placements in the erased history range (and any
  relative placements orphaned by that) before erasing the rows, while
  their pins still identify them. The PageList pin semantics are left
  unchanged since search relies on erased pins not being garbage.
  
  Fixes: #14831
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`8ef0ec1`](https://github.com/ghostty-org/ghostty/commit/8ef0ec1238220a5a714be452ed2844f0691fcf83) Update VOUCHED list ([#14824](https://github.com/ghostty-org/ghostty/issues/14824)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14822#discussioncomment-19157195)
  from @jcollie.
  
  Vouch: @AlJohri
  ```

## October 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40003456956)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`a743c4e`](https://github.com/ghostty-org/ghostty/commit/a743c4e53ed62ff7ebca286200d251c4999f398e) docs: replace stale function name. `ghostty_vt_osc_free()` should be `ghostty_osc_free` ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Change-Id: I4efdf6a51f568b4bc2678ef4a6aa1c106a6a6964
  ```
- [`22f100c`](https://github.com/ghostty-org/ghostty/commit/22f100c6367045bb5fc86172f837047dee2f7670) docs: replace stale function name. `ghostty_vt_osc_free()` should be `ghostty_osc_free` ([#14818](https://github.com/ghostty-org/ghostty/issues/14818)) ([@jcollie](https://github.com/jcollie))

