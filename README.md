> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 2, 2026 at 10:27 UTC.

## November 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41388327846), [2](https://github.com/ghostty-org/ghostty/actions/runs/41364959727)  
Summary: 2 runs • 10 commits • 4 authors

### Changes

- [`f7b25c8`](https://github.com/ghostty-org/ghostty/commit/f7b25c8129d84d53cf0cda4ffa024a692aca019e) termio: don't require RFC 1123 hostnames in OSC 7 ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.17 port switched reportPwd from `uri.getHost` to
  `std.Io.net.HostName.fromUri`, which also validates the host as an
  RFC 1123 hostname. Local hostnames often aren't: macOS allows names
  like "Foo's MacBook Pro", some systems use underscores, and our URI
  parser deliberately accepts MAC addresses. Any OSC 7 report from such
  a machine was dropped, so new tabs, splits and windows stopped
  inheriting the working directory.
  
  The host only has to match the local hostname, which `isLocal` already
  checks, so extract it without validating it, as 1.3 did.
  
  Fixes: #14970
  Ref: https://github.com/ghostty-org/ghostty/discussions/14952
  ```
- [`881fc68`](https://github.com/ghostty-org/ghostty/commit/881fc68902a5d819fdac96bcb597a2d99feb9729) terminal: skip clearing rows that are already blank ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase display (ED, `CSI J`) now skips rows that are already blank instead
  of clearing them again. On a mostly empty screen, full-screen erases are
  now 2x to 14x faster depending on screen size. Plain text and scrolling
  are unaffected.
  
  Programs that redraw by clearing (shells redrawing prompts, `clear`,
  `watch`, TUIs) usually erase a screen that is mostly empty already.
  Previously, every erase cleared every row cell by cell anyway, even
  when the cells were already zero.
  
  ## How
  
  Rows get a new `blank` bit, taken from the row's padding. It is set when
  a whole row is cleared with a zero blank cell and cleared by anything
  that writes cells. `clearRows` sees the bit and only resets the row's
  metadata, leaving the cells alone. Skipped rows aren't marked dirty
  because nothing about how they look changed.
  
  The bit is a hint that can be false for a blank row but never true for
  a row with content. We verify this with integrity checks.
  
  The tricky part was not slowing down printing. My first attempt cleared
  the bit whenever a row was marked dirty, which happens on every cursor
  move, and made scrolling about 3% slower. Now `writeCell` clears it,
  which also covers the spacer head a wide char writes before it wraps.
  `Row.markWritten` sets dirty and clears blank in one load and store,
  because doing them separately was measurable on the print path.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)    | blank-track (ms) | Speedup |
  | --------------- | ------- | ------------ | ---------------- | ------- |
  | erase.vt        | 120x80  | 362.6 ± 1.1  | 49.9 ± 0.1       | 7.27x   |
  | erase.vt        | 120x12  | 89.0 ± 0.3   | 49.0 ± 0.3       | 1.82x   |
  | erase.vt        | 300x100 | 1149 ± 16    | 82.6 ± 0.2       | 13.91x  |
  | ascii.vt        | 120x80  | 40.6 ± 0.2   | 40.5 ± 0.2       | 1.00x   |
  | styled-plain.vt | 120x80  | 64.1 ± 0.5   | 63.5 ± 0.5       | 1.01x   |
  | styled-mixed.vt | 120x80  | 576.0 ± 1.6  | 579.7 ± 5.9      | 0.99x   |
  | utf8.vt         | 120x80  | 380.5 ± 2.3  | 386.5 ± 6.5      | 0.98x   |
  | osc.vt          | 120x80  | 1142 ± 5     | 1140 ± 3         | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5911         | 5589             | 1.06x   |
  
  `out.txt` is the asciinema data dump, a real world workload. It gets
  faster because real sessions erase a lot! The vtebench vim inputs are
  1 to 2% faster for the same reason. The vtebench scrolling inputs are
  unchanged. utf8.vt looks 2% slower but it is noisy, and it executes
  only 0.3% more instructions, so this is probably noise.
  ```
- [`fd29936`](https://github.com/ghostty-org/ghostty/commit/fd29936f0914f5a303e1d67fd09201f981b7eff1) macos: make Surface main actor-isolated ([@jparise](https://github.com/jparise))
  ```text
  Calls into libghostty must happen on the main actor, and nearly every
  Surface function was already annotated with `@MainActor`.
  
  Main actor isolation makes the class implicitly Sendable, so the
  explicit conformance goes away. `deinit` remains `nonisolated`, so the
  surface handle stays `nonisolated(unsafe)` for it to read the value and
  hand it to the main actor to be freed.
  ```
- [`6573de6`](https://github.com/ghostty-org/ghostty/commit/6573de67e9990ebf0308f5cb07e4e40895d748ec) Replace std.ArrayListUnmanaged and std.ArrayListAligned ([@jcollie](https://github.com/jcollie))
  ```text
  Both are deprecated aliases in Zig 0.17: std.ArrayListUnmanaged is
  std.ArrayList, which has been unmanaged since 0.15, and
  std.ArrayListAligned is std.array_list.Aligned. Zig 0.18 removes them,
  so use the names they alias. No behavior change.
  ```
- [`2178e63`](https://github.com/ghostty-org/ghostty/commit/2178e635dffc71e0c679b143680665bf09857bb8) terminal: mark reset rows blank and test the blank bit bookkeeping ([@mitchellh](https://github.com/mitchellh))
- [`59093e3`](https://github.com/ghostty-org/ghostty/commit/59093e3aadb1478e6642061059b1882cfa1b6cf3) terminal: skip clearing rows that are already blank ([#14997](https://github.com/ghostty-org/ghostty/issues/14997)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase display (ED, `CSI J`) now skips rows that are already blank
  instead of clearing them again. On a mostly empty screen, full-screen
  erases are now 2x to 14x faster depending on screen size. Plain text and
  scrolling are unaffected.
  
  Programs that redraw by clearing (shells redrawing prompts, `clear`,
  `watch`, TUIs) usually erase a screen that is mostly empty already.
  Previously, every erase cleared every row cell by cell anyway, even when
  the cells were already zero.
  
  ## How
  
  Rows get a new `blank` bit, taken from the row's padding. It is set when
  a whole row is cleared with a zero blank cell and cleared by anything
  that writes cells. `clearRows` sees the bit and only resets the row's
  metadata, leaving the cells alone. Skipped rows aren't marked dirty
  because nothing about how they look changed.
  
  The bit is a hint that can be false for a blank row but never true for a
  row with content. We verify this with integrity checks.
  
  The tricky part was not slowing down printing. My first attempt cleared
  the bit whenever a row was marked dirty, which happens on every cursor
  move, and made scrolling about 3% slower. Now `writeCell` clears it,
  which also covers the spacer head a wide char writes before it wraps.
  `Row.markWritten` sets dirty and clears blank in one load and store,
  because doing them separately was measurable on the print path.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | blank-track (ms) | Speedup |
  | --------------- | ------- | ------------ | ---------------- | -------
  |
  | erase.vt | 120x80 | 362.6 ± 1.1 | 49.9 ± 0.1 | 7.27x |
  | erase.vt | 120x12 | 89.0 ± 0.3 | 49.0 ± 0.3 | 1.82x |
  | erase.vt | 300x100 | 1149 ± 16 | 82.6 ± 0.2 | 13.91x |
  | ascii.vt | 120x80 | 40.6 ± 0.2 | 40.5 ± 0.2 | 1.00x |
  | styled-plain.vt | 120x80 | 64.1 ± 0.5 | 63.5 ± 0.5 | 1.01x |
  | styled-mixed.vt | 120x80 | 576.0 ± 1.6 | 579.7 ± 5.9 | 0.99x |
  | utf8.vt | 120x80 | 380.5 ± 2.3 | 386.5 ± 6.5 | 0.98x |
  | osc.vt | 120x80 | 1142 ± 5 | 1140 ± 3 | 1.00x |
  | out.txt (2.6GB) | 120x80 | 5911 | 5589 | 1.06x |
  
  `out.txt` is the asciinema data dump, a real world workload. It gets
  faster because real sessions erase a lot! The vtebench vim inputs are 1
  to 2% faster for the same reason. The vtebench scrolling inputs are
  unchanged. utf8.vt looks 2% slower but it is noisy, and it executes only
  0.3% more instructions, so this is probably noise.
  
  **AI usage:** I came up with the change, Opus helped with benchmarking
  and validating, I wrote the text. Fable helped come up with an alternate
  idea for my original design which had the 3% slowdown :(
  ```
- [`ada6e3d`](https://github.com/ghostty-org/ghostty/commit/ada6e3d722fde00e7171e2d4e93c7392052f2720) Replace std.ArrayListUnmanaged and std.ArrayListAligned ([#15001](https://github.com/ghostty-org/ghostty/issues/15001)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Both are deprecated aliases in Zig 0.17: std.ArrayListUnmanaged is
  std.ArrayList, which has been unmanaged since 0.15, and
  std.ArrayListAligned is std.array_list.Aligned. Zig 0.18 removes them,
  so use the names they alias. No behavior change.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`5c6d43e`](https://github.com/ghostty-org/ghostty/commit/5c6d43eeecaf4eff506a96d0f5310b5682c80c88) macos: make Surface main actor-isolated ([#14999](https://github.com/ghostty-org/ghostty/issues/14999)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Calls into libghostty must happen on the main actor, and nearly every
  Surface function was already annotated with `@MainActor`.
  
  Main actor isolation makes the class implicitly Sendable, so the
  explicit conformance goes away. `deinit` remains `nonisolated`, so the
  surface handle stays `nonisolated(unsafe)` for it to read the value and
  hand it to the main actor to be freed.
  ```
- [`042b16b`](https://github.com/ghostty-org/ghostty/commit/042b16b6146ada29877dfeeea9f286889e4adeb1) termio: don't require RFC 1123 hostnames in OSC 7 ([#14971](https://github.com/ghostty-org/ghostty/issues/14971)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Zig 0.17 port switched reportPwd from `uri.getHost` to
  `std.Io.net.HostName.fromUri`, which also validates the host as an RFC
  1123 hostname. Local hostnames often aren't: macOS allows names like
  "Foo's MacBook Pro", some systems use underscores, and our URI parser
  deliberately accepts MAC addresses. Any OSC 7 report from such a machine
  was dropped, so new tabs, splits and windows stopped inheriting the
  working directory.
  
  The host only has to match the local hostname, which `isLocal` already
  checks, so extract it without validating it, as 1.3 did.
  
  Fixes: #14970
  Ref: https://github.com/ghostty-org/ghostty/discussions/14952
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`7cd6fa0`](https://github.com/ghostty-org/ghostty/commit/7cd6fa0215a1299c69c27fe543f48ecab45b775f) Sync CODEOWNERS vouch list ([#15002](https://github.com/ghostty-org/ghostty/issues/15002)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @mangkoran
  ```

## November 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41334104825), [2](https://github.com/ghostty-org/ghostty/actions/runs/41316706444), [3](https://github.com/ghostty-org/ghostty/actions/runs/41315316132), [4](https://github.com/ghostty-org/ghostty/actions/runs/41300698848), [5](https://github.com/ghostty-org/ghostty/actions/runs/41270777866), [6](https://github.com/ghostty-org/ghostty/actions/runs/41265367781), [7](https://github.com/ghostty-org/ghostty/actions/runs/41262969399)  
Summary: 7 runs • 13 commits • 5 authors

### Changes

- [`5e7714e`](https://github.com/ghostty-org/ghostty/commit/5e7714e71cd41ac0095aefa2120838842dfeca48) datastruct: prevent overflow in circular buffer arithmetic ([@12ya](https://github.com/12ya))
  ```text
  Check capacity growth and slice bounds before addition. Calculate
  wrapped indexes without overflowing intermediate sums and reuse the
  index calculation in the iterator.
  
  Add regression tests for capacity requests and index operations near
  the usize limit.
  ```
- [`0aa2f7c`](https://github.com/ghostty-org/ghostty/commit/0aa2f7caf52988bbfa42290cd3afbfbf550c0ef6) datastruct: use checked addition for buffer capacity ([@12ya](https://github.com/12ya))
  ```text
  #14987
  
  Use std.math.add to reject overflowing capacity requests while preserving the OutOfMemory error.
  ```
- [`c7eb3e8`](https://github.com/ghostty-org/ghostty/commit/c7eb3e8b96288e47e12f045056d270f8ba7f45f0) datastruct: restore circular buffer explanations ([@12ya](https://github.com/12ya))
  ```text
  #14987
  
  Restore iterator and head/tail explanations removed during overflow hardening. Describe saturating seeks and wrapping arithmetic accurately.
  ```
- [`a7e8e4d`](https://github.com/ghostty-org/ghostty/commit/a7e8e4d15bd0f12ad2a1123bf157b338e526c23e) datastruct: prevent overflow in circular buffer arithmetic ([#14987](https://github.com/ghostty-org/ghostty/issues/14987)) ([@jcollie](https://github.com/jcollie))
  ```text
  Check capacity growth and slice bounds before addition. Calculate
  wrapped indexes without overflowing intermediate sums and reuse the
  index calculation in the iterator.
  
  Add regression tests for capacity requests and index operations near the
  usize limit.
  
  AI disclosure: OpenAI Codex
  ```
- [`54d162d`](https://github.com/ghostty-org/ghostty/commit/54d162da5bea1d95399574495bde4ddb91df0784) terminal: apply every attribute of an SGR sequence at once ([@mitchellh](https://github.com/mitchellh))
  ```text
  An SGR sequence with several attributes, such as `CSI 0;1;38;5;100 m`,
  now updates the cursor style once after all of its attributes are
  applied.
  
  Previously, we applied per-attribute: 0, then 1, then 38, etc. Each forced
  a lookup, a hash, etc.
  
  Multi-attribute SGRs are common. Programs like Neovim, ncurses programs,
  btop, etc. In the 2.6 GB asciinema dump, about 9% of all SGR sequences
  are multi-attribute.
  
  ## How
  
  The action carries the whole sequence rather than keeping per-attribute
  actions and adding a trailing "end of sequence" marker. A handler that
  wants the old per-attribute view iterates `value.parser()`, and a
  handler that wants to batch gets the sequence boundary for free, with
  no state carried between actions.
  
  Unknown attributes are ignored silently in the app handler now, the
  same as libghostty-vt already did.
  
  There are no behavioral changes here.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)   | sgr-multi (ms) | Speedup |
  | --------------- | ----------- | -------------- | ------- |
  | styled-multi.vt | 367.7 ± 0.8 | 233.7 ± 0.6    | 1.57x   |
  | out.txt (2.6GB) | 5929 ± 26   | 5679 ± 8       | 1.04x   |
  | styled-heavy.vt | 238.7 ± 0.8 | 231.5 ± 0.8    | 1.03x   |
  | styled-mixed.vt | 573.9 ± 1.9 | 571.3 ± 2.3    | 1.00x   |
  | osc.vt          | 1124 ± 7    | 1119 ± 3       | 1.00x   |
  | utf8.vt         | 379.1 ± 1.5 | 378.5 ± 1.2    | 1.00x   |
  | styled-plain.vt | 64.2 ± 0.4  | 64.2 ± 0.4     | 1.00x   |
  | ascii.vt        | 40.3 ± 0.2  | 40.3 ± 0.2     | 1.00x   |
  
  Importantly: normal non-SGR workloads are unaffected.
  ```
- [`2f967e3`](https://github.com/ghostty-org/ghostty/commit/2f967e3a6ab231188c29a97fb422e479a254e97c) terminal: apply every attribute of an SGR sequence at once ([#14995](https://github.com/ghostty-org/ghostty/issues/14995)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  An SGR sequence with several attributes, such as `CSI 0;1;38;5;100 m`,
  now updates the cursor style once after all of its attributes are
  applied.
  
  Previously, we applied per-attribute: 0, then 1, then 38, etc. Each
  forced a lookup, a hash, etc.
  
  Multi-attribute SGRs are common. Programs like Neovim, ncurses programs,
  btop, etc. In the 2.6 GB asciinema dump, about 9% of all SGR sequences
  are multi-attribute.
  
  ## How
  
  The action carries the whole sequence rather than keeping per-attribute
  actions and adding a trailing "end of sequence" marker. A handler that
  wants the old per-attribute view iterates `value.parser()`, and a
  handler that wants to batch gets the sequence boundary for free, with no
  state carried between actions.
  
  Unknown attributes are ignored silently in the app handler now, the same
  as libghostty-vt already did.
  
  There are no behavioral changes here.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)   | sgr-multi (ms) | Speedup |
  | --------------- | ----------- | -------------- | ------- |
  | styled-multi.vt | 367.7 ± 0.8 | 233.7 ± 0.6    | 1.57x   |
  | out.txt (2.6GB) | 5929 ± 26   | 5679 ± 8       | 1.04x   |
  | styled-heavy.vt | 238.7 ± 0.8 | 231.5 ± 0.8    | 1.03x   |
  | styled-mixed.vt | 573.9 ± 1.9 | 571.3 ± 2.3    | 1.00x   |
  | osc.vt          | 1124 ± 7    | 1119 ± 3       | 1.00x   |
  | utf8.vt         | 379.1 ± 1.5 | 378.5 ± 1.2    | 1.00x   |
  | styled-plain.vt | 64.2 ± 0.4  | 64.2 ± 0.4     | 1.00x   |
  | ascii.vt        | 40.3 ± 0.2  | 40.3 ± 0.2     | 1.00x   |
  
  Importantly: normal non-SGR workloads are unaffected.
  
  **AI usage:** My normal: I came up with the change, Opus helped with
  benchmarking and validating, I wrote the text.
  ```
- [`a3e349f`](https://github.com/ghostty-org/ghostty/commit/a3e349f7a02709130d4cb83b24bac56a5d334d52) i18n: update Bahasa Indonesia translation ([#14991](https://github.com/ghostty-org/ghostty/issues/14991)) ([@clavinjune](https://github.com/clavinjune))
- [`a5b4403`](https://github.com/ghostty-org/ghostty/commit/a5b44039d10f25d2d0a5992137cd6517f49e72aa) Update VOUCHED list ([#14992](https://github.com/ghostty-org/ghostty/issues/14992)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14991#issuecomment-6557130969)
  from @trag1c.
  
  Vouch: @clavinjune
  ```
- [`a3b5946`](https://github.com/ghostty-org/ghostty/commit/a3b5946a59b94bf097da1aac889cf95f9c704675) terminal: new pages keep the capacity recent pages needed ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Headline performance number:** all data shapes other than plain-text
  is anywhere from 20% to 380% faster. Plain text is unaffected.
  
  `PageList.grow` now gives a new page the style, grapheme, string, and
  hyperlink capacity that the last two full pages needed, instead of
  always starting over from the standard capacity.
  
  Previously, every `grow` would allocate a new standard sized page and
  force the caller to call repeat `increaseCapacity` calls as needed. For
  similar data shapes, this would force a LOT of page copies and
  allocations.
  
  ## How
  
  So, I've tried this a few times before! And I've failed multiple times
  to get the right mix of logic to make this speedup the benchmarks but
  NOT regress standard workloads.
  
  I think I've got it this time though. Well, I know I have something
  because the benchmarks show it.
  
  The way it works: when we need to grow a new page, we keep the capacity
  of any managed dimension (style, grapheme, etc.) so long as 1/3rd of it
  is actually utilized. Otherwise, we shrink it back to standard size or
  1.5x what was used, whichever is BIGGER (so, it leans towards similar
  data). After that, we raise all dimensions to what the page _before_
  used, so that it takes _two full pages_ of low utilization to start
  shrinking.
  
  **We call these "carried pages," since the usage is carried forward.**
  
  If a carried page is larger than a pooled memory size, we shrink rows so
  that it fits in the pool. If we can't do this reasonably, we heap
  allocate but we try very hard to avoid this.
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)     | page-grow (ms) | Speedup |
  | --------------- | ------------- | -------------- | ------- |
  | styled-mixed.vt | 2284.1 ± 43.6 | 611.3 ± 1.3    | 3.74x   |
  | osc.vt          | 2616.3 ± 25.6 | 1173.7 ± 4.8   | 2.23x   |
  | burst.vt        | 250.3 ± 12.8  | 90.6 ± 0.7     | 2.76x   |
  | alternating.vt  | 443.9 ± 11.2  | 123.4 ± 4.4    | 3.60x   |
  | hyperlinks.vt   | 211.1 ± 5.6   | 55.1 ± 1.7     | 3.83x   |
  | styled-heavy.vt | 301.7 ± 1.4   | 246.0 ± 1.1    | 1.23x   |
  | utf8.vt         | 439.1 ± 2.0   | 385.6 ± 0.8    | 1.14x   |
  | ascii.vt        | 42.5 ± 0.6    | 42.0 ± 0.2     | 1.01x   |
  | styled-plain.vt | 65.7 ± 0.4    | 65.7 ± 0.4     | 1.00x   |
  | erase.vt        | 362.9 ± 4.2   | 372.4 ± 4.4    | 0.97x   |
  | out.txt (2.6GB) | 5857 ± 13     | 5922 ± 31      | 0.99x   |
  
  `out.txt` is the asciinema data dump. It is unaffected because diverse,
  heterogenous data (honestly, real world workloads!) don't behave this
  way. But because of that, its important to see that its all the same!
  
  It's important to note that while `out.txt` looks 1% slower, CPU metrics
  point to less instructions executed, less memory copies (2105 page
  copies instead of 2270, 1838 heap pages instead of 1934). So this is
  probably noise.
  
  Homogenous data is often used for benchmarks, and quite frankly I'm
  tired of people pointing out stuff like pure-SGR streams being very slow
  in Ghostty. So, this fixes that while not affecting normal workloads.
  ```
- [`dc8f599`](https://github.com/ghostty-org/ghostty/commit/dc8f59943ce94b75ffadc45cc4f36eca6a7ed2ae) terminal: new pages keep the capacity recent pages needed ([#14985](https://github.com/ghostty-org/ghostty/issues/14985)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Headline performance number:** all streams of heavily loaded
  homogeneous data shapes other than plain-text is anywhere from 20% to
  380% faster. Plain text is unaffected.
  
  `PageList.grow` now gives a new page the style, grapheme, string, and
  hyperlink capacity that the last two full pages needed, instead of
  always starting over from the standard capacity.
  
  Previously, every `grow` would allocate a new standard sized page and
  force the caller to call repeat `increaseCapacity` calls as needed. For
  similar data shapes, this would force a LOT of page copies and
  allocations.
  
  ## How
  
  So, I've tried this a few times before! And I've failed multiple times
  to get the right mix of logic to make this speedup the benchmarks but
  NOT regress standard workloads.
  
  I think I've got it this time though. Well, I know I have something
  because the benchmarks show it.
  
  The way it works: when we need to grow a new page, we keep the capacity
  of any managed dimension (style, grapheme, etc.) so long as 1/3rd of it
  is actually utilized. Otherwise, we shrink it back to standard size or
  1.5x what was used, whichever is BIGGER (so, it leans towards similar
  data). After that, we raise all dimensions to what the page _before_
  used, so that it takes _two full pages_ of low utilization to start
  shrinking.
  
  **We call these "carried pages," since the usage is carried forward.**
  
  If a carried page is larger than a pooled memory size, we shrink rows so
  that it fits in the pool. If we can't do this reasonably, we heap
  allocate but we try very hard to avoid this.
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)     | page-grow (ms) | Speedup |
  | --------------- | ------------- | -------------- | ------- |
  | styled-mixed.vt | 2284.1 ± 43.6 | 611.3 ± 1.3    | 3.74x   |
  | osc.vt          | 2616.3 ± 25.6 | 1173.7 ± 4.8   | 2.23x   |
  | burst.vt        | 250.3 ± 12.8  | 90.6 ± 0.7     | 2.76x   |
  | alternating.vt  | 443.9 ± 11.2  | 123.4 ± 4.4    | 3.60x   |
  | hyperlinks.vt   | 211.1 ± 5.6   | 55.1 ± 1.7     | 3.83x   |
  | styled-heavy.vt | 301.7 ± 1.4   | 246.0 ± 1.1    | 1.23x   |
  | utf8.vt         | 439.1 ± 2.0   | 385.6 ± 0.8    | 1.14x   |
  | ascii.vt        | 42.5 ± 0.6    | 42.0 ± 0.2     | 1.01x   |
  | styled-plain.vt | 65.7 ± 0.4    | 65.7 ± 0.4     | 1.00x   |
  | erase.vt        | 362.9 ± 4.2   | 372.4 ± 4.4    | 0.97x   |
  | out.txt (2.6GB) | 5857 ± 13     | 5922 ± 31      | 0.99x   |
  
  `out.txt` is the asciinema data dump. It is unaffected because diverse,
  heterogenous data (honestly, real world workloads!) don't behave this
  way. But because of that, its important to see that its all the same!
  
  It's important to note that while `out.txt` looks 1% slower, CPU metrics
  point to less instructions executed, less memory copies (2105 page
  copies instead of 2270, 1838 heap pages instead of 1934). So this is
  probably noise.
  
  Homogenous data is often used for benchmarks, and quite frankly I'm
  tired of people pointing out stuff like pure-SGR streams being very slow
  in Ghostty. So, this fixes that while not affecting normal workloads.
  
  **AI usage:** I've done the laddering before so I did a NUMBER of messy
  passes. I had Opus running benchmarks for each of my attempts. I think I
  tried 6 or 7 different logical choices before settling on this. Fable
  chased down the alignment issue in the benchmark (cause I was seeing
  like a consistent 4% slowdown in vtebench dense cells but it didn't make
  sense to me because this codepath didn't get touched!). I wrote this
  whole PR message.
  ```
- [`845736e`](https://github.com/ghostty-org/ghostty/commit/845736e1df59e637a614aee78009217c9b480988) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`2fc8d02`](https://github.com/ghostty-org/ghostty/commit/2fc8d02c253bc09ff7456c65e7f63dd6eebaf4de) Update iTerm2 colorschemes ([#14981](https://github.com/ghostty-org/ghostty/issues/14981)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261026-153024-27cbbb5
  ```
- [`c42f6fb`](https://github.com/ghostty-org/ghostty/commit/c42f6fb4740102b678773f4bfdd4ef7613afe818) Update VOUCHED list ([#14983](https://github.com/ghostty-org/ghostty/issues/14983)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14982#discussioncomment-19325417)
  from @jcollie.
  
  Vouch: @cammeresi
  ```

## October 31, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41244998361), [2](https://github.com/ghostty-org/ghostty/actions/runs/41221492187), [3](https://github.com/ghostty-org/ghostty/actions/runs/41208691947), [4](https://github.com/ghostty-org/ghostty/actions/runs/41167071786), [5](https://github.com/ghostty-org/ghostty/actions/runs/41160759341), [6](https://github.com/ghostty-org/ghostty/actions/runs/41159681318)  
Summary: 6 runs • 11 commits • 5 authors

### Changes

- [`c7be56a`](https://github.com/ghostty-org/ghostty/commit/c7be56a04696249a2c33abac88586338aba7fc7a) fuzz: exercise hierarchical context in osc harness ([@paaloeye](https://github.com/paaloeye))
  ```text
  The OSC fuzzer harness previously discarded the parsed command returned
  by the OSC parser without evaluating lazily parsed metadata. **OSC 3008**
  hierarchical context sequences parse metadata fields on demand through
  readOption, leaving option parsing, type conversions, and unescaping
  unexercised by the fuzzer.
  
  When a hierarchical context command is produced, query every defined
  context field to fuzz option extraction and validation. For string
  fields with escape sequences, exercise both the streaming character
  iterator and heap-allocated decoding paths. Seed inputs for **OSC 3008** in
  the initial and minimized corpora are updated with escaped metadata.
  
  Also align the fuzzer package minimum Zig version with the root build
  and pass the target macOS deployment version and `-Wno-override-module`
  to afl-cc to silence target triple and linker version mismatch warnings.
  
  AI disclosure: AI helped to discover AFL++ args and drafted this commit message.
  
  Spec: https://github.com/uapi-group/specifications/blob/5e61460b42b91bb1e402b50a6149774d78fc0d8e/specs/osc_context.md
  Assited-By: Gemini 4 Argon (Medium)
  Assited-By: Antigravity CLI 1.3.5
  Agent-Session: 0c644e81-47c4-4768-95ee-5660020523dd
  ```
- [`83b57ac`](https://github.com/ghostty-org/ghostty/commit/83b57ac5ead868e133adb509f7ef0a4ffa3ffe01) fuzz: exercise hierarchical context in osc harness ([#14977](https://github.com/ghostty-org/ghostty/issues/14977)) ([@jcollie](https://github.com/jcollie))
  ```text
  The OSC fuzzer harness previously discarded the parsed command returned
  by the OSC parser without evaluating lazily parsed metadata. **OSC
  3008** hierarchical context sequences parse metadata fields on demand
  through `readOption`, leaving option parsing, type conversions, and
  unescaping unexercised by the fuzzer.
  
  When a hierarchical context command is produced, query every defined
  context field to fuzz option extraction and validation. Seed inputs for
  **OSC 3008** in the initial and minimized corpora are updated with
  escaped metadata.
  
  Also align the fuzzer package minimum Zig version with the root build
  and pass the target macOS deployment version and `-Wno-override-module`
  to `afl-cc` to silence target triple and linker version mismatch
  warnings.
  
  AI disclosure: AI helped to discover AFL++ args and drafted this commit
  message.
  
  Spec:
  https://github.com/uapi-group/specifications/blob/5e61460b42b91bb1e402b50a6149774d78fc0d8e/specs/osc_context.md
  ```
- [`b01ca00`](https://github.com/ghostty-org/ghostty/commit/b01ca003ca76687072b1cac6f1e3dd1bd0e27fa5) benchmark: add shaper-rows benchmark ([@AryanHamedani](https://github.com/AryanHamedani))
  ```text
  Measures turning terminal rows into text runs (`--mode=runs`) and
  shaping them (`--mode=shape`), which the renderer does for every dirty
  row on every frame. Shaped runs are cached by the renderer but run
  iteration is not, so `runs` isolates the per-frame cost a cache can't
  hide. The data file fills a screen during setup, which is not timed.
  ```
- [`1461f06`](https://github.com/ghostty-org/ghostty/commit/1461f068745a4b9524e197a38a876072a9a220f0) benchmark: end a shaper frame after each shaper-rows pass ([@AryanHamedani](https://github.com/AryanHamedani))
  ```text
  CoreText shapers keep CoreFoundation objects in a release pool until
  endFrame(). The renderer calls it once per frame, so do the same once
  per pass instead of letting every pass accumulate in the pool.
  ```
- [`3bd54e0`](https://github.com/ghostty-org/ghostty/commit/3bd54e025cc3349ee76ab1af7ec1ff8f7353632b) benchmark: add shaper-rows benchmark ([#14965](https://github.com/ghostty-org/ghostty/issues/14965)) ([@jcollie](https://github.com/jcollie))
  ```text
  Adds `ghostty-bench +shaper-rows`, as suggested in
  https://github.com/ghostty-org/ghostty/pull/11079#issuecomment-6524841018.
  
  None of the existing benchmarks cover the font shaper. This one fills a
  screen from `--data` during setup, which isn't timed, and then makes
  `--iterations` passes (default 200) over every row:
  
  - `--mode=runs` only splits rows into text runs. The renderer does this
  for every dirty row on every frame, and unlike shaping it isn't cached,
  so this shows the per-frame cost.
  - `--mode=shape` also shapes each run.
  
  It uses the embedded Inconsolata face with the embedded Arabic face as
  fallback, so RTL input gets shaped by a real font. Terminal size is
  `--terminal-rows`/`--terminal-cols` (80x120), same as `screen-clone`.
  
  On main (Linux, HarfBuzz, ReleaseFast), with hyperfine, 10 runs each:
  
  | data | runs | shape |
  |---|---|---|
  | 2000 lines of `src/terminal/Terminal.zig` | 34.7 ms ±1.0 | 84.3 ms
  ±2.0 |
  | 2000 lines of Persian prose | 58.2 ms ±3.2 | 246.7 ms ±12.7 |
  
  On #11079 it picked up a 2x slowdown in `runs` on plain ASCII.
  
  *AI disclosure: I used Claude Code to write and port this benchmark and
  to draft this description. I've read the code and can explain it, and I
  ran the numbers above myself.*
  ```
- [`ce92029`](https://github.com/ghostty-org/ghostty/commit/ce920296c891d0f9e266cfb908057716304182ab) terminal: skip the ED2 prompt scan when OSC 133 was never seen ([@mitchellh](https://github.com/mitchellh))
  ```text
  Full-screen `eraseDisplay` now skips finding the last prompt line when
  we haven't seen semantic prompts. For screens without OSC133,
  full-screen erases are now ~2x faster.
  
  Programs that redraw by clearing the screen (TUIs, `watch`, etc.)
  would hit this unnecessary path every clear because they never emit
  OSC133.
  
  This also adds a `+erase` generator to `ghostty-gen` that produces a
  stream of full-screen clears and cursor movement to simulate
  pathological inputs that hit this optimization.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)     | erase-opt (ms) | Speedup |
  | --------------- | ------- | ------------- | -------------- | ------- |
  | erase.vt        | 120x80  | 748.7 ± 51.6  | 421.8 ± 6.2    | 1.78x   |
  | erase.vt        | 120x12  | 114.0 ± 2.4   | 102.5 ± 1.1    | 1.11x   |
  | erase.vt        | 300x100 | 2597.1 ± 54.1 | 1227.0 ± 14.2  | 2.12x   |
  | ascii.vt        | 120x80  | 45.7 ± 0.3    | 45.8 ± 0.3     | 1.00x   |
  | styled-plain.vt | 120x80  | 70.4 ± 0.4    | 69.9 ± 0.6     | 1.01x   |
  | styled-heavy.vt | 120x80  | 311.9 ± 7.0   | 313.5 ± 6.9    | 0.99x   |
  | utf8.vt         | 120x80  | 473.1 ± 4.5   | 476.9 ± 5.3    | 0.99x   |
  | osc.vt          | 120x80  | 2770 ± 30     | 2726 ± 25      | 1.02x   |
  
  This also fixes a couple places where we wern't properly setting
  `seen`.
  ```
- [`9bfa8ee`](https://github.com/ghostty-org/ghostty/commit/9bfa8ee9a1d73f99208c1f056c4e4b5783402ead) terminal: skip the ED2 prompt scan when OSC 133 was never seen ([#14975](https://github.com/ghostty-org/ghostty/issues/14975)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Full-screen `eraseDisplay` now skips finding the last prompt line when
  we haven't seen semantic prompts. For screens without OSC133,
  full-screen erases are now ~2x faster.
  
  Programs that redraw by clearing the screen (TUIs, `watch`, etc.) would
  hit this unnecessary path every clear because they never emit OSC133.
  
  This also adds a `+erase` generator to `ghostty-gen` that produces a
  stream of full-screen clears and cursor movement to simulate
  pathological inputs that hit this optimization.
  
  This also fixes a couple places where we wern't properly setting `seen`.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)     | erase-opt (ms) | Speedup |
  | --------------- | ------- | ------------- | -------------- | ------- |
  | erase.vt        | 120x80  | 748.7 ± 51.6  | 421.8 ± 6.2    | 1.78x   |
  | erase.vt        | 120x12  | 114.0 ± 2.4   | 102.5 ± 1.1    | 1.11x   |
  | erase.vt        | 300x100 | 2597.1 ± 54.1 | 1227.0 ± 14.2  | 2.12x   |
  | ascii.vt        | 120x80  | 45.7 ± 0.3    | 45.8 ± 0.3     | 1.00x   |
  | styled-plain.vt | 120x80  | 70.4 ± 0.4    | 69.9 ± 0.6     | 1.01x   |
  | styled-heavy.vt | 120x80  | 311.9 ± 7.0   | 313.5 ± 6.9    | 0.99x   |
  | utf8.vt         | 120x80  | 473.1 ± 4.5   | 476.9 ± 5.3    | 0.99x   |
  | osc.vt          | 120x80  | 2770 ± 30     | 2726 ± 25      | 1.02x   |
  
  The benchmarks most importantly show not just the speedup but that
  existing data shapes are unaffected.
  
  **AI disclosure:** Fable found the slowdown cause (reported by a
  libghostty user), I fixed it, Fable+Opus validated my work and found a
  couple bugs (e.g. missing setting `seen` in cursor copy and snapshot).
  Opus wrote the synthetic generator and ran the benchmarks. I wrote all
  the comments and this PR body.
  ```
- [`51e7fe5`](https://github.com/ghostty-org/ghostty/commit/51e7fe51db607773a651b161527beb10ce92a611) terminal/tmux: parse %output without a regex ([@jcollie](https://github.com/jcollie))
  ```text
  Parse `%output %<pane> <data>` by hand instead of compiling an
  Oniguruma regex for every pane write, matching how %window-close and
  %session-window-changed are already parsed.
  
  The pane id now goes through parseDecimalId, so an id that overflows
  usize is logged and dropped rather than hitting `catch unreachable`.
  Empty data is accepted rather than rejected.
  
  The data is sliced from the line directly rather than through
  std.mem.cutPrefix, which returns a const slice, so that it keeps the
  mutability of the parser buffer it points into.
  ```
- [`ae0dc1b`](https://github.com/ghostty-org/ghostty/commit/ae0dc1b7136c2baddc3e067663aa041cd555cfda) terminal/tmux: parse %output without a regex ([#14947](https://github.com/ghostty-org/ghostty/issues/14947)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Parse `%output %<pane> <data>` by hand instead of compiling an Oniguruma
  regex for every pane write, matching how %window-close and
  %session-window-changed are already parsed.
  
  The pane id now goes through parseDecimalId, so an id that overflows
  usize is logged and dropped rather than hitting `catch unreachable`.
  Empty data is accepted rather than rejected.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`c911f96`](https://github.com/ghostty-org/ghostty/commit/c911f96ee8fedd4594b5b69f1128fcb03f560622) Update VOUCHED list ([#14969](https://github.com/ghostty-org/ghostty/issues/14969)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14963#discussioncomment-19307157)
  from @jcollie.
  
  Vouch: @hamidp
  ```
- [`0a672a9`](https://github.com/ghostty-org/ghostty/commit/0a672a914479354aa8599c75927485b22905c394) Update VOUCHED list ([#14968](https://github.com/ghostty-org/ghostty/issues/14968)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14964#discussioncomment-19306948)
  from @jcollie.
  
  Vouch: @edsarmiento
  ```

## October 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41126163986), [2](https://github.com/ghostty-org/ghostty/actions/runs/41124653536), [3](https://github.com/ghostty-org/ghostty/actions/runs/41119470525), [4](https://github.com/ghostty-org/ghostty/actions/runs/41115877636), [5](https://github.com/ghostty-org/ghostty/actions/runs/41105956349), [6](https://github.com/ghostty-org/ghostty/actions/runs/41088392462), [7](https://github.com/ghostty-org/ghostty/actions/runs/41066122923), [8](https://github.com/ghostty-org/ghostty/actions/runs/41009687911), [9](https://github.com/ghostty-org/ghostty/actions/runs/40999068173), [10](https://github.com/ghostty-org/ghostty/actions/runs/40992707017)  
Summary: 10 runs • 30 commits • 9 authors

### Changes

- [`8bb4f45`](https://github.com/ghostty-org/ghostty/commit/8bb4f45846ecde0ab53a846ee1bca5533dca8c5f) fuzz: fix replay crash detection and add osc target ([@paaloeye](https://github.com/paaloeye))
- [`a0706b7`](https://github.com/ghostty-org/ghostty/commit/a0706b79b3d791873177b1fda4b155267769e8c5) fuzz: fix replay crash detection and add osc target ([#14896](https://github.com/ghostty-org/ghostty/issues/14896)) ([@jcollie](https://github.com/jcollie))
  ```text
  In Nushell, running an external command that exits successfully returns
  stdout as an empty string. The previous error check tested whether the
  result was not `null`, which always evaluated to `true` for clean exits.
  
  Use the `complete` command to inspect the process exit code.
  
  Additionally, add "osc" to the default list of fuzzers so OSC crashes
  are replayed by default.
  
  Ref: https://www.nushell.sh/commands/docs/complete.html
  ```
- [`fbed180`](https://github.com/ghostty-org/ghostty/commit/fbed180a5f181915c92a8f2f561903a6e4645b5a) Update VOUCHED list ([#14960](https://github.com/ghostty-org/ghostty/issues/14960)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14959#discussioncomment-19301732)
  from @jcollie.
  
  Vouch: @AryanHamedani
  ```
- [`4d7de0a`](https://github.com/ghostty-org/ghostty/commit/4d7de0a483e40e2c1dc542315b2a87be96977df2) fix(ssh): show authentication messages during terminfo setup ([@clinta](https://github.com/clinta))
  ```text
  Suppressing SSH stderr hid keyboard-interactive login instructions.
  Inherit it instead; installer output remains suppressed by default.
  ```
- [`9644c75`](https://github.com/ghostty-org/ghostty/commit/9644c7571d43f988415b3ed38f40be76e5964dd4) datastruct: fix clearing circular buffers with zero capacity ([@12ya](https://github.com/12ya))
  ```text
  Keep buffers with zero capacity marked full after clear(), so append()
  returns error.OutOfMemory instead of panicking.
  
  Add a regression test for this case.
  ```
- [`f040f0a`](https://github.com/ghostty-org/ghostty/commit/f040f0ab0ee30d77794b98d87e27fc9105ee6ab9) datastruct: fix clearing circular buffers with zero capacity ([#14958](https://github.com/ghostty-org/ghostty/issues/14958)) ([@jcollie](https://github.com/jcollie))
  ```text
  Keep buffers with zero capacity marked full after clear(), so append()
  returns error.OutOfMemory instead of panicking.
  
  Add a regression test for this case.
  
  AI disclosure: OpenAI Codex
  ```
- [`4489314`](https://github.com/ghostty-org/ghostty/commit/44893148d009bd372f5f7e8d2edbd0340fc82b65) cli: show SSH authentication messages during terminfo setup ([#14916](https://github.com/ghostty-org/ghostty/issues/14916)) ([@jcollie](https://github.com/jcollie))
  ```text
  `+ssh` suppresses stderr during terminfo setup. OpenSSH still displays
  authentication prompts through `/dev/tty`, but accompanying
  informational messages from custom SSH servers are hidden. This can make
  authentication appear to stall.
  
  Inherit SSH stderr without disabling interactive authentication.
  Installer output remains suppressed by default, and `--verbose` behavior
  is preserved. SSH warnings and login banners can now also appear during
  setup.
  
  Tested with 114 focused SSH tests and nine real OpenSSH scenarios
  covering keyboard-interactive setup and login, the Bash shell wrapper,
  installation, fallback, caching, environment forwarding, and exit-status
  propagation.
  
  Oh-My-Pi using GPT-6.1 Sol assisted with diagnosis, implementation,
  validation, and drafting this change.
  ```
- [`32da5e4`](https://github.com/ghostty-org/ghostty/commit/32da5e47b26cad0dadb36c279ae9e020a2e60959) snap: avoid trailing colon in LD_LIBRARY_PATH ([@12ya](https://github.com/12ya))
  ```text
  Add the separator only when appending a nonempty inherited path.
  A trailing colon adds the working directory to library lookup,
  which can make launcher commands load a conflicting local library
  and fail before Ghostty starts.
  ```
- [`1d23d02`](https://github.com/ghostty-org/ghostty/commit/1d23d02ae16f86d9c9a3792098cb906b94208bcc) snap: avoid trailing colon in LD_LIBRARY_PATH ([#14954](https://github.com/ghostty-org/ghostty/issues/14954)) ([@jcollie](https://github.com/jcollie))
  ```text
  Add the separator only when appending a nonempty inherited path. A
  trailing colon adds the working directory to library lookup, which can
  make launcher commands load a conflicting local library and fail before
  Ghostty starts.
  
  Verified with the extracted Ghostty 1.4.0 ARM64 Snap in Docker:
  the original launcher exits 127 with an empty libc.so.6 in the
  working directory, while the corrected launcher exits 0.
  
  I intended to open an issue documenting this investigation, but
  issue creation is restricted. I can provide the Docker commands
  used to reproduce the failure in the follow up comments instead.
  
  
  AI disclosure: OpenAI Codex assisted with investigating the issue,
  proposing the fix, running Docker reproductions, reviewing the
  change, and drafting this commit message.
  ```
- [`93404a4`](https://github.com/ghostty-org/ghostty/commit/93404a48a9a8bf265bb1671e0e6d9985322f6682) Update VOUCHED list ([#14957](https://github.com/ghostty-org/ghostty/issues/14957)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14956#discussioncomment-19300741)
  from @jcollie.
  
  Vouch: @yeager
  ```
- [`86c704a`](https://github.com/ghostty-org/ghostty/commit/86c704afdde5a8ee67300d924d1c52b4d82b4ff4) gtk: fix jumps when resizing splits via keybind ([@dkinzler](https://github.com/dkinzler))
  ```text
  `syncSplitRatio` now exits early if GTK size allocation has not yet
  computed a value for the `max-position` property of the `GtkPaned`
  widget. Initially `max-position` has the max value for a `c_int`, so
  that calculations in the function would overflow and set the split ratio
  to 0. This could happen when resizing a split multiple times by holding
  down a keybind.
  ```
- [`ca91d0a`](https://github.com/ghostty-org/ghostty/commit/ca91d0a24e67b3eecdb23c943227cd2b3908747b) gtk: fix jumps when resizing splits via keybind ([#14951](https://github.com/ghostty-org/ghostty/issues/14951)) ([@jcollie](https://github.com/jcollie))
  ```text
  `syncSplitRatio` now exits early if GTK size allocation has not yet
  computed a value for the `max-position` property of the `GtkPaned`
  widget. Initially `max-position` has the max value for a `c_int`, so
  that calculations in the function would overflow and set the split ratio
  to 0. This could happen when resizing a split multiple times by holding
  down a keybind.
  
  Fixes a regression introduced by #14476 where the split ratio sometimes
  jumps to the minimum when holding down the resize keybind. See the video
  below. When `syncSplitRatio` is called from `SplitTree.resize` it is not
  guaranteed that the `GtkPaned` widget has already been size allocated.
  This can happen with many resizes in a short time because the `GtkPaned`
  widget is rebuilt on every one.
  
  
  https://github.com/user-attachments/assets/442adf44-3a1c-41ee-bdc4-aa971848893e
  ```
- [`90ed851`](https://github.com/ghostty-org/ghostty/commit/90ed851dea8a7f328ad937adc5521c809f2cd41d) config: ignore repeated space in direct commands ([@12ya](https://github.com/12ya))
  ```text
  Repeated spaces in direct: commands produced empty arguments.
  Use tokenizeScalar to skip those empty fields and add a regression
  case for repeated spaces between arguments.
  ```
- [`e2593c1`](https://github.com/ghostty-org/ghostty/commit/e2593c1496cbf9f34f13e53d2d83b80283c8f24f) config: ignore repeated space in direct commands ([#14950](https://github.com/ghostty-org/ghostty/issues/14950)) ([@jcollie](https://github.com/jcollie))
  ```text
  Repeated spaces in direct: commands produced empty arguments. Use
  tokenizeScalar to skip those empty fields and add a regression case for
  repeated spaces between arguments.
  
  
  follow up to https://github.com/ghostty-org/ghostty/pull/14921
  ```
- [`854e514`](https://github.com/ghostty-org/ghostty/commit/854e51422732c00088ceb79b09a61e504b89800d) snap: bundle gstreamer plugins so audio bell works ([@aaron-ang](https://github.com/aaron-ang))
  ```text
  When `bell-features = audio` is enabled, GTK plays the bell through its
  GStreamer media backend. GTK links GStreamer itself, but GStreamer also
  needs playback, decode and audio sink plugins to build a pipeline, and
  the snap ships none of them, so the bell silently fails to play.
  
  Stage gstreamer1.0-plugins-base/-good/-pulseaudio for the decode and
  audio sink pipeline (typefind, playbin/decodebin, vorbis, audioconvert,
  autoaudiosink, pulsesink). In the launcher, export
  GST_PLUGIN_SYSTEM_PATH, GST_PLUGIN_SCANNER and GST_REGISTRY so
  GStreamer finds the bundled plugins and keeps a per-user registry cache
  under SNAP_USER_COMMON, and unset GST_PLUGIN_PATH plus the `_1_0`
  variants so host settings can't override the bundled paths.
  ```
- [`ff23824`](https://github.com/ghostty-org/ghostty/commit/ff23824213b8d7ab7a07dca6a7e0d68cad51b802) snap: bundle gstreamer plugins so audio bell works ([#12676](https://github.com/ghostty-org/ghostty/issues/12676)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  
  With `bell-features = audio` and a valid `bell-audio-path` configured,
  no sound plays in the snap build of Ghostty.
  
  On core26, GTK links GStreamer directly. GStreamer still needs playback,
  decode and audio-sink plugins to build a pipeline, and the snap ships
  none of them, so the bell fails silently.
  
  `bell-features = system` (the compositor sound, via
  `gdk_surface_beep()`) already works and is unchanged.
  
  ## Fix
  
  - Stage `gstreamer1.0-plugins-base`, `gstreamer1.0-plugins-good` and
  `gstreamer1.0-pulseaudio`. This gives the snap `typefind`,
  `playbin`/`decodebin`, `ogg`, `vorbis`, `audioconvert`, `autoaudiosink`,
  `pulsesink`, etc.
  - In `snap/local/launcher`, export `GST_PLUGIN_SYSTEM_PATH`,
  `GST_PLUGIN_SCANNER` and `GST_REGISTRY`. GStreamer then uses only the
  bundled plugins and keeps a per-user registry cache under
  `SNAP_USER_COMMON`.
  - Unset `GST_PLUGIN_PATH`, `GST_PLUGIN_PATH_1_0`,
  `GST_PLUGIN_SYSTEM_PATH_1_0`, `GST_PLUGIN_SCANNER_1_0` and
  `GST_REGISTRY_1_0`. GStreamer prefers the `_1_0` variants over the
  unversioned ones, so host settings could otherwise override the bundled
  paths.
  
  `gstreamer1.0-pipewire` is not included. PipeWire registers
  `pipewiresink` with rank none
  ([source](https://github.com/PipeWire/pipewire/blob/master/src/gst/gstpipewire.c)),
  so `autoaudiosink` never selects it. On PipeWire hosts the bell plays
  through `pulsesink` and pipewire-pulse. The package would also pull in
  the `pipewire` daemon package without changing behavior.
  
  ## Local build
  
  The snap CI builds from a release tarball. Building
  `snap/snapcraft.yaml` from a git checkout needs two changes that are
  *not* part of this PR:
  
  1. A `VERSION` file at the repo root, e.g. `echo 1.4.0-dev > VERSION`.
  2. `blueprint-compiler` 0.20.0 or newer on `PATH` during the build.
  Ubuntu 26.04 ships 0.19.0. I ran v0.20.0 from source and added
  `python3-gi`, `gir1.2-gtk-4.0` and `gir1.2-adw-1` to `build-packages`.
  
  ## Test plan
  
  I built the snap on core26 (arm64) and installed it on an Ubuntu 24.04
  host.
  
  - [x] The snap contains the plugins above, and `gst-plugin-scanner` sits
  at the path the launcher exports.
  - [x] I ran `playbin` on `/usr/share/sounds/freedesktop/stereo/bell.oga`
  with the snap's own GStreamer libraries and the launcher's `GST_*`
  environment:
    - It played to EOS.
    - `autoaudiosink` selected the bundled `pulsesink`.
    - Audio was captured from a null sink.
  - [x] With an empty plugin directory, the same test fails to create
  `playbin`. This shows the plugins come from the snap.
  
  ## AI Disclosure
  
  Claude Code was used throughout:
  - diagnosing the missing plugins
  - drafting the `snapcraft.yaml` and launcher changes
  - rebasing onto core26 and addressing review feedback
  - driving the core26 snap build and the GStreamer playback test
  
  I reviewed every line of the diff and understand what each change does.
  ```
- [`8c04d7c`](https://github.com/ghostty-org/ghostty/commit/8c04d7c2e8c37a4044b1af4c58e529c714c83b20) config: reject empty prefixed commands ([@12ya](https://github.com/12ya))
  ```text
  Commands containing only `direct:` or `shell:` were accepted because
  the empty-input check ran before prefix removal.
  ```
- [`cf0ab14`](https://github.com/ghostty-org/ghostty/commit/cf0ab14aed55315a53de668bc1bbcf4a13ce0ddd) config: reject empty prefixed commands ([#14921](https://github.com/ghostty-org/ghostty/issues/14921)) ([@jcollie](https://github.com/jcollie))
  ```text
  Commands containing only `direct:` or `shell:` were accepted because the
  empty-input check ran before prefix removal.
  
  AI assistance: Used OpenAI Codex
  ```
- [`7e79688`](https://github.com/ghostty-org/ghostty/commit/7e7968826f02f846e04706729cdccc4b85b85258) tmux: unescape %output and handle window-close ([@MisterTea](https://github.com/MisterTea))
  ```text
  %output payload bytes that cannot travel in the control stream are
  octal-escaped. Unescape them in place so pane data is the original
  bytes. Also parse %window-close / %unlinked-window-close and
  %session-window-changed, and emit an active_window action so callers
  can track tmux's current window.
  
  #1935
  ```
- [`c2d9362`](https://github.com/ghostty-org/ghostty/commit/c2d93620efc6364b95641fa317d428b8a4e1f9ab) tmux: do not unescape %output in the parser ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  Decoding octal escapes while parsing %output is wasted work if a
  control client never reads pane bytes. Leave the payload as tmux
  sent it; callers that need the original stream can decode later.
  Window-close, session-window-changed, and active_window are unchanged.
  ```
- [`dc6ab39`](https://github.com/ghostty-org/ghostty/commit/dc6ab39fb1f31c6e0ffe2fadfc0b3e2d4d347442) termio: handle tmux active_window action ([@MisterTea](https://github.com/MisterTea))
  ```text
  The viewer emits active_window when the current tmux window
  changes. The stream handler switch did not cover that tag, so
  the GTK build failed. Accept the action and leave GUI
  notification for a later change, matching the windows case.
  ```
- [`9a92081`](https://github.com/ghostty-org/ghostty/commit/9a920818820f0885e9302b6831cdfe5a2aab67a4) tmux: honor session id on active window changes ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  %session-window-changed is broadcast to every control client for
  every session. Emit active_window only when the notification's
  session matches the one this viewer is attached to.
  %window-pane-changed stays ignored, since an active pane change
  does not mean the current window changed. If recording the action
  runs out of memory, the viewer becomes defunct.
  ```
- [`7e4cc4f`](https://github.com/ghostty-org/ghostty/commit/7e4cc4fae011dc3a133ce625d6cf6f0d546be64a) tmux: reject oversized control ids without leaking ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  %window-close and %session-window-changed are split with prefix
  cuts instead of compiling a regex on every notification. An id
  that is not decimal digits or does not fit in usize is ignored
  rather than crashing. If a later list-windows line fails to
  parse, layout arenas from the lines that already parsed are freed.
  ```
- [`539a7f1`](https://github.com/ghostty-org/ghostty/commit/539a7f1ce770b12071ca146e9824b9d9e5a1b88f) nix: use store paths for propagated GStreamer packages ([@romen](https://github.com/romen))
  ```text
  postFixup wrote the literal attribute names (e.g.
  "gst_all_1.gstreamer") into nix-support/propagated-user-env-packages
  instead of store paths. Anything that builds an environment from that
  file fails, e.g. `nix shell github:ghostty-org/ghostty/v1.4.0`:
  
      error: not an absolute path: 'gst_all_1.gstreamer'
  
  Interpolate the packages so the file contains their store paths.
  
  
  Change-Id: I37035d027b3ec2396f7d39911fe7dc336a6a6964
  ```
- [`2ddcda8`](https://github.com/ghostty-org/ghostty/commit/2ddcda8e80fdf53d2a6fdee9d36f4986d858d477) tmux: test %exit with and without a reason ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  The parser already accepts a bare %exit and one with a reason
  such as "server exited", and drops the reason. Cover both forms.
  Use std.mem.find for the session-window split; indexOf is deprecated.
  ```
- [`0a5a6a6`](https://github.com/ghostty-org/ghostty/commit/0a5a6a6e1a20928f4b097d51ec9fcf06de353024) Merge remote-tracking branch 'origin/main' into tmux-pr4-protocol ([@MisterTea](https://github.com/MisterTea))
- [`cd00d09`](https://github.com/ghostty-org/ghostty/commit/cd00d09c64c34c3074b0b2c2f584fce6fbab2ca9) tmux: ignore active_window in raw startup tests ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  Main's raw startup viewer test switches on every viewer action.
  The active_window action added for %session-window-changed was
  unhandled, so CI failed to compile that test. This startup path
  does not change the active window, so the test ignores the action.
  ```
- [`eec45a5`](https://github.com/ghostty-org/ghostty/commit/eec45a52dda2a3080023ef45d37797a091b486bd) tmux: handle window-close and active window ([#14273](https://github.com/ghostty-org/ghostty/issues/14273)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  
  - Parse `%window-close` / `%unlinked-window-close` and
  `%session-window-changed`.
  - Emit an `active_window` viewer action so later layers can track tmux's
  current window.
  - Parse `%exit` as soon as the notification line is seen.
  
  `%output` is left escaped on purpose. A control client that is not
  reading pane bytes should not pay to decode octal sequences up front;
  callers that need the original stream can unescape later (see #12076).
  
  This is stacked on #14262. GitHub will also show that commit until it
  merges, because we cannot target another PR's branch from a fork.
  
  **Depends on:** #14262
  
  CI / compile may fail until that PR is on `main`. That is expected.
  
  ## Test plan
  
  - [ ] `zig build test-lib-vt -Dtest-filter="tmux"` after #14262 is
  merged
  - [ ] Close a tmux window and change the active window; parser emits the
  new notifications (still log-only on `main` until later PRs)
  
  ## AI disclosure
  
  This change was written with [Cursor](https://cursor.com). I directed
  the work, reviewed the diff, and am responsible for it.
  
  Related: #1935
  
  Made with [Cursor](https://cursor.com)
  ```
- [`e1e05c1`](https://github.com/ghostty-org/ghostty/commit/e1e05c1cd13efc4bc962f4a3fd8c4e310267b340) nix: use store paths for propagated GStreamer packages ([#14929](https://github.com/ghostty-org/ghostty/issues/14929)) ([@jcollie](https://github.com/jcollie))
  ````text
  `nix/package.nix` writes the GStreamer entries in
  `nix-support/propagated-user-env-packages` as plain strings
  (`gst_all_1.gstreamer`) rather than store paths. The package builds
  fine, but anything that reads that file to assemble an environment fails
  afterwards. With 1.4.0:
  
      $ nix shell github:ghostty-org/ghostty/v1.4.0
      error: not an absolute path: 'gst_all_1.gstreamer'
  
  `nix run` is unaffected since it doesn't read propagated packages.
  
  This interpolates the three packages so their store paths are written,
  matching the `$terminfo`, `$shell_integration` and `$vim` lines above.
  
  Tested on x86_64-linux:
  
  ```
  nix build .#default
  cat result/nix-support/propagated-user-env-packages   # all store paths now
  nix shell .#default -c ghostty --version
  
  # Also tested a long-running GUI session with the resulting environment and tested AV playing with `mpv -vo kitty`
  nix shell .#default
  which ghostty # points to the path of the just build derivation
  ghostty # opens a new ghostty window
  # within that new window
  mpv -vo kitty ~/Downloads/some_random_video.mp4
  # Video and Audio both play properly
  ```
  
  AI disclosure: Claude Opus 5.5, used to diagnose the issue, edit the
  commit message, and draft the initial version of this PR description.
  I (a human being) manually patched the nix file (admittedly it was a
  trivial fix), and tested the patch.
  
  
  ---
  
  **Note: I know this will be automatically closed until I am vouched, but
  I'd like to store here the PR description, while the fix is fresh,
  rather than having to craft a new one if the vouching process takes
  days.**
  ````
- [`7c6e101`](https://github.com/ghostty-org/ghostty/commit/7c6e1011c237aaac3d19d094b3c4bdada3b21bc8) Update VOUCHED list ([#14943](https://github.com/ghostty-org/ghostty/issues/14943)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14942#discussioncomment-19283760)
  from @jcollie.
  
  Vouch: @tonypapousek
  ```

## October 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40944541875), [2](https://github.com/ghostty-org/ghostty/actions/runs/40905187830), [3](https://github.com/ghostty-org/ghostty/actions/runs/40882266997), [4](https://github.com/ghostty-org/ghostty/actions/runs/40863292794), [5](https://github.com/ghostty-org/ghostty/actions/runs/40807604373)  
Summary: 5 runs • 9 commits • 6 authors

### Changes

- [`f761046`](https://github.com/ghostty-org/ghostty/commit/f761046d6b8a30ad49181ad330ae2f18532cb193) formatter: restore a pending wrap at the right margin ([@robmorgan](https://github.com/robmorgan))
  ```text
  The VT formatter restores a pending wrap by reprinting the cell under the
  cursor, but only when the cursor is in the last column. With left and
  right margins (DECLRMM and DECSLRM), a wrap is pending at the right margin
  when the cursor is within the margins, so there it wrote a CUP, which
  clears the wrap, and the next character overwrote the margin's column
  instead of wrapping.
  
  The terminal formatter restores the modes and the margins before the
  cursor, so when it emits both it now tells the screen formatter to
  reprint the cell at the right margin when the cursor is within the
  margins. The screen formatter alone, and a terminal formatter without
  those extras, still only reprint in the last column, since the margins
  are not in force when their output is replayed.
  ```
- [`9781c0a`](https://github.com/ghostty-org/ghostty/commit/9781c0afc8225510e33127466f0815eb51086d7d) formatter: restore a pending wrap at the right margin ([#14918](https://github.com/ghostty-org/ghostty/issues/14918)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The VT formatter restores a pending wrap by reprinting the cell under
  the cursor, but only when the cursor is in the last column. With left
  and right margins (`DECLRMM` and `DECSLRM`), a wrap is pending at the
  right margin when the cursor is within the margins, so it writes a CUP,
  which clears the wrap, and the next character overwrites the margin's
  column instead of wrapping.
  
  The terminal formatter restores the modes and the margins before the
  cursor, so when it emits both, it now tells the screen formatter to
  reprint the cell at the right margin when the cursor is within the
  margins. The screen formatter alone, and a terminal formatter without
  those extras, still only reprints in the last column, since the margins
  are not in force when their output is replayed.
  
  I haven't benchmarked this because the change only does a fixed amount
  of work once per format call and never touches the per-cell loops where
  formatting spends most of its time.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ```
- [`108d503`](https://github.com/ghostty-org/ghostty/commit/108d503ac591d5a3b3a13a4bc11bbea8c09a42fb) Update VOUCHED list ([#14936](https://github.com/ghostty-org/ghostty/issues/14936)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14935#discussioncomment-19271347)
  from @jcollie.
  
  Vouch: @jglanz
  ```
- [`4071344`](https://github.com/ghostty-org/ghostty/commit/40713449c609158017801c6dd39f465a281741a5) i18n: command palette - Focus and Untitled translation support ([@EriksRemess](https://github.com/EriksRemess))
- [`93967b7`](https://github.com/ghostty-org/ghostty/commit/93967b7f9478e94dcbb42125c8a90f34feb40d75) i18n: command palette - Focus and Untitled translation support ([#14055](https://github.com/ghostty-org/ghostty/issues/14055)) ([@jcollie](https://github.com/jcollie))
  ```text
  "Focus: {s}" and "Untitled" was not included in command palette
  translations. This PR adds support and placeholders in .po files for
  those strings.
  ```
- [`df1c99c`](https://github.com/ghostty-org/ghostty/commit/df1c99c8a5ec32c73963e5dc3fad3c9df7a3d137) Update VOUCHED list ([#14930](https://github.com/ghostty-org/ghostty/issues/14930)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14928#discussioncomment-19265783)
  from @pluiedev.
  
  Vouch: @romen
  ```
- [`5ee2150`](https://github.com/ghostty-org/ghostty/commit/5ee215000ebe4354cd388962bc372152d16dacc6) nix: drop removed gnome-photos from VM excludes ([@gaborbernat](https://github.com/gaborbernat))
  ```text
  The nixpkgs update for Zig 0.17 removed gnome-photos, so evaluating
  any GNOME VM check fails with "'gnome-photos' has been removed".
  Excluding a package that no longer exists is unnecessary.
  ```
- [`f563ced`](https://github.com/ghostty-org/ghostty/commit/f563ceda37c51e6e3b0212f5c6965ff3113628d0) nix: apply GNOME Shell unsafe mode to the user unit ([@gaborbernat](https://github.com/gaborbernat))
  ```text
  The pinned GNOME starts org.gnome.Shell@user, so the --unsafe-mode
  override on org.gnome.Shell@wayland never applies. Without it,
  org.gnome.Shell.Eval returns nothing and basic-window-check-gnome
  times out waiting for the focused window.
  ```
- [`b2c78c9`](https://github.com/ghostty-org/ghostty/commit/b2c78c9bd9bc88a16d9c3769b0fb17ddde1b78b1) nix: fix GNOME VM tests on main ([#14910](https://github.com/ghostty-org/ghostty/issues/14910)) ([@jcollie](https://github.com/jcollie))
  ```text
  The GNOME VM checks fail on main, unnoticed because CI doesn't build
  them: `gnome-photos` was removed from nixpkgs in 3110fb358, breaking
  evaluation, and the `--unsafe-mode` override targets
  `org.gnome.Shell@wayland` while GNOME now starts `org.gnome.Shell@user`,
  so `Shell.Eval` returns nothing. Dropping the exclude and retargeting
  the override makes `basic-window-check-gnome` and
  `bell-leak-check-gnome` pass again.
  
  **AI assistance:** I used Claude Code (Claude Opus 5.5) to find and
  verify this. I reviewed the change.
  ```

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

