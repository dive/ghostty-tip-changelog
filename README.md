> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 12, 2026 at 05:29 UTC.

## November 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43156147800)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`73b201e`](https://github.com/ghostty-org/ghostty/commit/73b201ed3355622eb4e6ff8c3fb703fb1fed702c) docs: fix prettier error in vt release notes ([@jcollie](https://github.com/jcollie))
- [`72ac7dc`](https://github.com/ghostty-org/ghostty/commit/72ac7dced84e96a5d5214d005d59eadd10da27bb) docs: fix prettier error in vt release notes ([#15211](https://github.com/ghostty-org/ghostty/issues/15211)) ([@mitchellh](https://github.com/mitchellh))

## November 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43120465374), [2](https://github.com/ghostty-org/ghostty/actions/runs/43116343611), [3](https://github.com/ghostty-org/ghostty/actions/runs/43109502795), [4](https://github.com/ghostty-org/ghostty/actions/runs/43088927858), [5](https://github.com/ghostty-org/ghostty/actions/runs/43088194050), [6](https://github.com/ghostty-org/ghostty/actions/runs/43076356783), [7](https://github.com/ghostty-org/ghostty/actions/runs/43052067738), [8](https://github.com/ghostty-org/ghostty/actions/runs/42965895341)  
Summary: 8 runs • 17 commits • 4 authors

### Changes

- [`c6174c8`](https://github.com/ghostty-org/ghostty/commit/c6174c88f42b48adb14857c9233b16f6947ab732) Update VOUCHED list ([#15209](https://github.com/ghostty-org/ghostty/issues/15209)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15203#discussioncomment-19553167)
  from @jcollie.
  
  Vouch: @krios2146
  ```
- [`fa70e8b`](https://github.com/ghostty-org/ghostty/commit/fa70e8b28d84d8b7e30db31c176e55b5e9c851f5) Update VOUCHED list ([#15208](https://github.com/ghostty-org/ghostty/issues/15208)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15077#discussioncomment-19552828)
  from @jcollie.
  
  Vouch: @montmejat
  ```
- [`d9a9b34`](https://github.com/ghostty-org/ghostty/commit/d9a9b34fcc52cb327b8f77a9392dc1aae7bffe45) doxygen: release notes for libghostty ([@mitchellh](https://github.com/mitchellh))
- [`55ff97e`](https://github.com/ghostty-org/ghostty/commit/55ff97ec363a05e81467a928eb85df5b948d6a69) libghostty: move tree to 1.0.2 dev ([@mitchellh](https://github.com/mitchellh))
- [`108cacb`](https://github.com/ghostty-org/ghostty/commit/108cacb17ed8990840cd14abfce43d8ed8503ca1) libghostty-vt: set version to 1.0.1-dev ([@mitchellh](https://github.com/mitchellh))
- [`afeed2e`](https://github.com/ghostty-org/ghostty/commit/afeed2e6e5bef27060ec19237facf6407f68351c) ci: pin LXD to 5.21 for the snap build ([@mitchellh](https://github.com/mitchellh))
- [`f7d91fa`](https://github.com/ghostty-org/ghostty/commit/f7d91fa456b5c1ad6e8785acda1018f4a1c7009e) terminal: search thread test no longer crashes on timeout ([@mitchellh](https://github.com/mitchellh))
- [`da2a39f`](https://github.com/ghostty-org/ghostty/commit/da2a39fb7f8a918e847ed7aac69f25b97b11f2db) CI Fixes ([#15200](https://github.com/ghostty-org/ghostty/issues/15200)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes a couple issues that have been causing problems in CI:
  
  - Pin LXD for Snap builds, they fail with LXD 6 atm. I didn't look into
  this further. I'm prioritizing green first.
  - Valgrind tests found a race condition in a test where we could access
  corrupt memory. This was in a test only, so fix that to avoid the crash.
  ```
- [`af57d7e`](https://github.com/ghostty-org/ghostty/commit/af57d7eda2050e65da30010f25962c31badc746a) ci: wait for snapd before installing lxd ([@mitchellh](https://github.com/mitchellh))
- [`8ad3f60`](https://github.com/ghostty-org/ghostty/commit/8ad3f607fd951985f8657d72e7bcc989ea636a4c) terminal: prompt redraw on resize no longer leaves stale prompts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13629
  Fixes #14751
  Supersedes #14707
  
  When a resize changes the column count and the shell redraws its prompt
  (OSC 133), we previously could leave stale prompt rows behind. Each resize
  added another copy, and this caused issues most visibly with prmpts that
  used the whole line, like powerlevel10k.
  
  Two separate bugs here.
  
  (1) Reflow copied a row's semantic prompt mark onto every row it split
  the row into, and a joined row took the mark of the last row joined into it.
  
  (2) We clear the prompt after the reflow, so the clear looked for the prompt
  start using those wrong marks. Narrowing cleared from a later start and
  left the top of the prompt behind. Widening walked past the missing
  start and also cleared the previous prompt.
  
  Reflow now marks only the first row of a prompt as the prompt start,
  the same as if the prompt were printed at the new width. This also
  fixes jump to prompt and other prompt features for older prompts in
  scrollback.
  
  For the redraw, we now find the prompt start before the resize and
  track it with a pin. Column reflow writes the prompt rows as blank rows
  that each end their line (`PageList.Resize.blank`), so the prompt keeps
  the row count it had at the old width. That matters because after
  SIGWINCH, zsh moves the cursor up by the number of rows the prompt took
  at the old width and then redraws. We clear from the pin after the
  resize, so a failed resize still leaves the prompt untouched.
  ```
- [`e6076b3`](https://github.com/ghostty-org/ghostty/commit/e6076b3a6e6d4bc603a17324c7f40a859d6b8b3a) terminal: prompt redraw on resize no longer leaves stale prompts ([#15199](https://github.com/ghostty-org/ghostty/issues/15199)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13629
  Fixes #14751
  Supersedes #14707
  
  When a resize changes the column count and the shell redraws its prompt
  (OSC 133), we previously could leave stale prompt rows behind. Each
  resize added another copy, and this caused issues most visibly with
  prmpts that used the whole line, like powerlevel10k.
  
  Two separate bugs here.
  
  (1) Reflow copied a row's semantic prompt mark onto every row it split
  the row into, and a joined row took the mark of the last row joined into
  it.
  
  (2) We clear the prompt after the reflow, so the clear looked for the
  prompt start using those wrong marks. Narrowing cleared from a later
  start and left the top of the prompt behind. Widening walked past the
  missing start and also cleared the previous prompt.
  
  Reflow now marks only the first row of a prompt as the prompt start, the
  same as if the prompt were printed at the new width. This also fixes
  jump to prompt and other prompt features for older prompts in
  scrollback.
  
  For the redraw, we now find the prompt start before the resize and track
  it with a pin. Column reflow writes the prompt rows as blank rows that
  each end their line (`PageList.Resize.blank`), so the prompt keeps the
  row count it had at the old width. That matters because after SIGWINCH,
  zsh moves the cursor up by the number of rows the prompt took at the old
  width and then redraws. We clear from the pin after the resize, so a
  failed resize still leaves the prompt untouched.
  
  **AI usage:** Simultaneously found the issue with Fable, I fixed the
  primary logic, Opus wrote tests and ran differential tests across a
  variety of prompts to validate it. It did find a couple bugs in my logic
  which I then fixed.
  ```
- [`4edde79`](https://github.com/ghostty-org/ghostty/commit/4edde79c034023e35249a296803bd7e1f30bb2be) macos: fix split activation mouse handling ([@nurpax](https://github.com/nurpax))
  ```text
  Double-clicking an inactive split can select text in the previously
  focused split. The first click activates the new split, but is stopped
  before AppKit receives it. AppKit then sends the second click to the
  old split.
  
  Let AppKit receive the first click, and suppress it in mouseDown and
  mouseUp instead so it is not forwarded to the terminal.
  
  for #14901, #15168
  ```
- [`ab2f658`](https://github.com/ghostty-org/ghostty/commit/ab2f658b17fd58ce8ecf4f5f1b8a9c66991a9a9d) build: support -Demit-lib-vt and -Demit-exe together ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15080
  
  The combined install is layout and byte-identical to the two separate installs
  except for the prefix in the pkg-config files and the exe itself of
  course because our exe builds aren't perfectly reproducible.
  ```
- [`290100c`](https://github.com/ghostty-org/ghostty/commit/290100c5dbab9461ea3905e6a344f6d6db14e30f) build: support -Demit-lib-vt and -Demit-exe together ([#15196](https://github.com/ghostty-org/ghostty/issues/15196)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15080
  
  The combined install is layout and byte-identical to the two separate
  installs except for the prefix in the pkg-config files and the exe
  itself of course because our exe builds aren't perfectly reproducible.
  ```
- [`2693982`](https://github.com/ghostty-org/ghostty/commit/2693982f8e20186c9a1e1c59dfb97f41ef3f57a0) macOS: fix split activation mouse handling ([#15190](https://github.com/ghostty-org/ghostty/issues/15190)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  The original macOS bug opened in a discussion #14901. Further explained
  in my accepted vouch request #15168.
  
  In short, the issue is double-clicking an inactive split on macOS
  selects text in the previously focused split. The first click changes
  focus but is stopped before AppKit receives it, so AppKit sends
  subsequent mouse events to the old split. Discussion #14901 has a video
  capture of how it misbehaves.
  
  Tested on macOS.
  
  **AI use**: I did use Codex to draft the changes, although tbh, rewrote
  the code comments and the code by hand many times to make it as easy as
  possible to understand (for myself and for reviewers).
  ```
- [`9b848b0`](https://github.com/ghostty-org/ghostty/commit/9b848b0f5c1f5e18611d89a570540df9ad2333d1) libghostty: restored snapshot keeps final page capacity max size ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15192
  
  Typically during snapshot decode, we decode into an exact-sized page as
  requested by the snapshot. This means that the final page was allocated
  wastefully and the next write would immediately force an allocation.
  
  The SCREEN decoder now gives the last page as many rows as fit in its
  pool item (`PageList.fillPooled`), and the PAGE decoder accepts a
  destination with more rows than advertised. History pages are unchanged
  since they never grow, and so is the snapshot format.
  ```
- [`a622196`](https://github.com/ghostty-org/ghostty/commit/a622196c930138f312884382ab784e45b9ab653b) libghostty: restored snapshot keeps final page capacity max size ([#15195](https://github.com/ghostty-org/ghostty/issues/15195)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15192
  
  Typically during snapshot decode, we decode into an exact-sized page as
  requested by the snapshot. This means that the final page was allocated
  wastefully and the next write would immediately force an allocation.
  
  The SCREEN decoder now gives the last page as many rows as fit in its
  pool item (`PageList.fillPooled`), and the PAGE decoder accepts a
  destination with more rows than advertised. History pages are unchanged
  since they never grow, and so is the snapshot format.
  ```

## November 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42905364874), [2](https://github.com/ghostty-org/ghostty/actions/runs/42902207730), [3](https://github.com/ghostty-org/ghostty/actions/runs/42852875359), [4](https://github.com/ghostty-org/ghostty/actions/runs/42847509638), [5](https://github.com/ghostty-org/ghostty/actions/runs/42820231618), [6](https://github.com/ghostty-org/ghostty/actions/runs/42766626266), [7](https://github.com/ghostty-org/ghostty/actions/runs/42762275342), [8](https://github.com/ghostty-org/ghostty/actions/runs/42754218095), [9](https://github.com/ghostty-org/ghostty/actions/runs/42736069717)  
Summary: 9 runs • 24 commits • 4 authors

### Changes

- [`2abe8a7`](https://github.com/ghostty-org/ghostty/commit/2abe8a7df8a39527e500867484ca04b5e58e3b21) use glibc's memset, memcpy, memmove when dynamically linked ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up to #15189.
  
  Our Linux executables never used glibc's `memset`, `memcpy`, or
  `memmove` even though they link glibc, because Zig's bundled compiler_rt
  always took priority (a weak symbol in the same binary always takes priority
  over a linked symbol).
  
  glibc's implementation benchmark faster in every benchmark we have,
  and they do runtime CPU feature discovery. For e.g. `-Dcpu=baseline`,
  Zig's compiler_rt uses SSE2 whereas glibc gets the full CPU support of
  whatever you're running.
  
  To make this work we have to do some inline assembly to build a
  trampoline to forward to the versioned glibc symbol. For all symbols, we
  use the oldest glibc version possible for each architecture. Its
  literally the first version supported except for x86_64 since the oldest
  has a fixed SSE2 routine which makes it not worth it.
  
  Benchmarks:
  
  | Workload                | arm64 before | arm64 after | x86_64 before | x86_64 after |
  | ----------------------- | -----------: | ----------: | ------------: | -----------: |
  | ASCII                   |        146.5 |       146.1 |         238.8 |        223.9 |
  | ASCII, no scrollback    |        224.9 |       172.7 |         258.2 |        232.3 |
  | ASCII, 50 MB scrollback |        173.3 |       169.3 |         385.3 |        377.2 |
  | UTF-8                   |        244.0 |       244.3 |         380.0 |        379.8 |
  | Erase                   |        291.1 |       288.9 |         346.6 |        346.3 |
  | Erase with scroll-clear |        645.3 |       647.0 |       1,115.9 |      1,074.8 |
  | Erase, 300x100          |        488.9 |       490.7 |         438.4 |        440.5 |
  | `+terminal-resize`      |         74.6 |        67.2 |         119.5 |        114.4 |
  ```
- [`ea8b12a`](https://github.com/ghostty-org/ghostty/commit/ea8b12a8a9894b5259c441eadd8f6f0c65e215af) use glibc's memset, memcpy, memmove when dynamically linked ([#15191](https://github.com/ghostty-org/ghostty/issues/15191)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up to #15189.
  
  Our Linux executables never used glibc's `memset`, `memcpy`, or
  `memmove` even though they link glibc, because Zig's bundled compiler_rt
  always took priority (a weak symbol in the same binary always takes
  priority over a linked symbol).
  
  glibc's implementation benchmark faster in every benchmark we have, and
  they do runtime CPU feature discovery. For e.g. `-Dcpu=baseline`, Zig's
  compiler_rt uses SSE2 whereas glibc gets the full CPU support of
  whatever you're running.
  
  To make this work we have to do some inline assembly to build a
  trampoline to forward to the versioned glibc symbol. For all symbols, we
  use the oldest glibc version possible for each architecture. Its
  literally the first version supported except for x86_64 since the oldest
  has a fixed SSE2 routine which makes it not worth it.
  
  Benchmarks (ms, lower is better):
  
  | Workload | arm64 before | arm64 after | x86_64 before | x86_64 after |
  | ----------------------- | -----------: | ----------: | ------------: |
  -----------: |
  | ASCII | 146.5 | 146.1 | 238.8 | 223.9 |
  | ASCII, no scrollback | 224.9 | 172.7 | 258.2 | 232.3 |
  | ASCII, 50 MB scrollback | 173.3 | 169.3 | 385.3 | 377.2 |
  | UTF-8 | 244.0 | 244.3 | 380.0 | 379.8 |
  | Erase | 291.1 | 288.9 | 346.6 | 346.3 |
  | Erase with scroll-clear | 645.3 | 647.0 | 1,115.9 | 1,074.8 |
  | Erase, 300x100 | 488.9 | 490.7 | 438.4 | 440.5 |
  | `+terminal-resize` | 74.6 | 67.2 | 119.5 | 114.4 |
  
  **AI usage:** I wrote the Zig, Fable helped me with the inline assembly
  since I wasn't super familiar how to manually do versioned symbols that
  way, Opus ran the benchmarks and did binary inspection across a variety
  of targets and glibc versions.
  ```
- [`9899c07`](https://github.com/ghostty-org/ghostty/commit/9899c0707767d93ad26e587c896a9a2761273b26) build: don't export the memset quirk on Darwin ([@mitchellh](https://github.com/mitchellh))
- [`a5eeb89`](https://github.com/ghostty-org/ghostty/commit/a5eeb897906a6f15daf046422b001753ef68f0d6) build: make libsystem_override.sh independent of locale and PATH ([@mitchellh](https://github.com/mitchellh))
- [`58ab25a`](https://github.com/ghostty-org/ghostty/commit/58ab25af435128a30866500764f1e6c6524381cf) build: don't export the memset quirk on x86_64 ([@mitchellh](https://github.com/mitchellh))
- [`1b22f33`](https://github.com/ghostty-org/ghostty/commit/1b22f331a58a5be5ede2f1d76b7793d4130b4072) libghostty: don't export the memset quirk on Darwin or x86_64 ([#15189](https://github.com/ghostty-org/ghostty/issues/15189)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The memset we ship (see `quirks_memset.zig` on why) was causing issues
  for statically linked Darwin builds because it was taking priority when
  you really want to use libSystems (which is good enough).
  
  This PR measured our memset and found that on Darwin and Linux x86_64 we
  don't need the quirk anymore. On Darwin you get libSystem and on Linux
  you get Zig's compiler_rt which fixed the performance issues in 0.17. In
  both cases, benchmarks are a wash (within 1% both directions).
  
  For everyone else, but notably Linux aarch64, our memset is still
  significantly faster and we keep it.
  
  This adds CI checks to ensure that our macOS static archives don't
  define these symbols.
  
  **AI usage:** At my direction, it ran the benchmarks on machines with
  parameters I requested. It wrote the YAML plus libsystem override script
  changes. I wrote all the comments and everything else.
  ```
- [`c4b91fe`](https://github.com/ghostty-org/ghostty/commit/c4b91fe4c7db89e3c6300180a279237bb2737f38) terminal/kitty: keep a replaced image until its transmission ends ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15124
  
  For a chunked transmission, we now keep the old image until the
  transmission ends (success or failure). The spec mandates we do delete
  the old iamge in either cause but doesn't specify _when_.
  
  Kitty itself deletes the images immediately on the first chunk, so this
  breaks from that behavior but I think results in something nicer that is
  spec compliant.
  
  The result of this is that during chunking, the old image continues to
  show until the operation is done.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/
  Kitty: https://github.com/kovidgoyal/kitty/blob/v0.48.2/kitty/graphics.c#L725-L729
  ```
- [`de70b9f`](https://github.com/ghostty-org/ghostty/commit/de70b9f476c39ce3f5b293ecba813b674f037a80) terminal/kitty: keep a replaced image until its transmission ends ([#15184](https://github.com/ghostty-org/ghostty/issues/15184)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15124
  
  For a chunked transmission, we now keep the old image until the
  transmission ends (success or failure). The spec mandates we do delete
  the old iamge in either cause but doesn't specify _when_.
  
  Kitty itself deletes the images immediately on the first chunk, so this
  breaks from that behavior but I think results in something nicer that is
  spec compliant.
  
  The result of this is that during chunking, the old image continues to
  show until the operation is done.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/
  Kitty:
  https://github.com/kovidgoyal/kitty/blob/v0.48.2/kitty/graphics.c#L725-L729
  ```
- [`6671592`](https://github.com/ghostty-org/ghostty/commit/6671592445a400219034194b9d0116029b1c5c9d) Update VOUCHED list ([#15187](https://github.com/ghostty-org/ghostty/issues/15187)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/15185#issuecomment-6771820967)
  from @pluiedev.
  
  Denounce: @jischeng
  ```
- [`fbb6dbe`](https://github.com/ghostty-org/ghostty/commit/fbb6dbe7ea5c1ce6df14ef82e00779a568cdb2a2) i18n: Dutch translations for command palette ([#15179](https://github.com/ghostty-org/ghostty/issues/15179)) ([@mtak](https://github.com/mtak))
  ```text
  Added new translations for the command palette changes.
  ```
- [`bd1e6a4`](https://github.com/ghostty-org/ghostty/commit/bd1e6a43476325dbf37939de939eac326696b08f) Update VOUCHED list ([#15175](https://github.com/ghostty-org/ghostty/issues/15175)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15168#discussioncomment-19510462)
  from @bo2themax.
  
  Vouch: @nurpax
  ```
- [`d0addb9`](https://github.com/ghostty-org/ghostty/commit/d0addb9cdf9a30901bd953421dccada3bf610d7c) terminal: keep the pruned page's memory when grow prunes by lines ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15157
  
  The problem is that line limit is enforced in the middle of a page vs
  byte limit which is enforced only when a new page is allocated.
  
  When a line limit was hit, we would fully decommit the backing memory. A
  steadily filled terminal would then shortly fault it back in. As a
  result, there were dozens of page faults more than byte limits.
  
  The line limit being checked in the middle of `grow()` turned out not to
  be expensive. The decommit/fault was expensive. By retaining the memory
  we're able to get back pretty much all the performance compared to byte
  limits.
  
  The cost is that we always have ~1 extra allocated page (~300KB) for an
  idle terminal at its line limit. But that's a small price to pay for the
  performance win!
  
  Benchmarking from Opus: Throughput writing 166 MB of ASCII at 200x50, MB/s,
  median of 5 runs on Linux (Ryzen 5800X) and 9 runs on macOS (Apple M5 Ultra):
  
  | Scrollback limit     | Linux before | Linux after | macOS before | macOS after |
  | -------------------- | -----------: | ----------: | -----------: | ----------: |
  | default (10 MB)      |        2,003 |       2,041 |        4,242 |       4,326 |
  | max lines 1,000      |          298 |       1,983 |        2,214 |       4,093 |
  | max lines 10,000     |          293 |       1,861 |        2,157 |       4,010 |
  | max bytes 18,276,352 |        1,834 |       1,833 |        4,116 |       4,122 |
  | unlimited            |          304 |         312 |        1,626 |       1,641 |
  ```
- [`1450c11`](https://github.com/ghostty-org/ghostty/commit/1450c11b6eca1490fdcb9140d02089010d97717e) terminal: keep the pruned page's memory when grow prunes by lines ([#15173](https://github.com/ghostty-org/ghostty/issues/15173)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #15157
  
  The problem is that line limit is enforced in the middle of a page vs
  byte limit which is enforced only when a new page is allocated.
  
  When a line limit was hit, we would fully decommit the backing memory. A
  steadily filled terminal would then shortly fault it back in. As a
  result, there were dozens of page faults more than byte limits.
  
  The line limit being checked in the middle of `grow()` turned out not to
  be expensive. The decommit/fault was expensive. By retaining the memory
  we're able to get back pretty much all the performance compared to byte
  limits.
  
  The cost is that we always have ~1 extra allocated page (~300KB) for an
  idle terminal at its line limit. But that's a small price to pay for the
  performance win!
  
  Benchmarking from Opus: Throughput writing 166 MB of ASCII at 200x50,
  MB/s, median of 5 runs on Linux (Ryzen 5800X) and 9 runs on macOS (Apple
  M5 Ultra). **Higher is better (MB/s).**
  
  | Scrollback limit | Linux before | Linux after | macOS before | macOS
  after |
  | -------------------- | -----------: | ----------: | -----------: |
  ----------: |
  | default (10 MB) | 2,003 | 2,041 | 4,242 | 4,326 |
  | max lines 1,000 | 298 | 1,983 | 2,214 | 4,093 |
  | max lines 10,000 | 293 | 1,861 | 2,157 | 4,010 |
  | max bytes 18,276,352 | 1,834 | 1,833 | 4,116 | 4,122 |
  | unlimited | 304 | 312 | 1,626 | 1,641 |
  
  **AI usage:** I directed Opus what to measure for me and babysat its
  measurements while it ran them in the background. I directed it to try a
  couple paths (as noted above), which I thought of myself. Ultimately I
  picked the path that made most sense, and cleaned up that code. Opus ran
  the benchmarks.
  ```
- [`ed9a7f5`](https://github.com/ghostty-org/ghostty/commit/ed9a7f505a1c9fd9eb229d99f38dd37f21c22bf6) build(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request) from 8.1.1 to 8.1.2.
  - [Release notes](https://github.com/peter-evans/create-pull-request/releases)
  - [Commits](https://github.com/peter-evans/create-pull-request/compare/5f6978faf089d4d20b00c7766989d076bb2fc7f1...15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8)
  
  ---
  updated-dependencies:
  - dependency-name: peter-evans/create-pull-request
    dependency-version: 8.1.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`17dec4e`](https://github.com/ghostty-org/ghostty/commit/17dec4ee0ceb58bb407e228e4a9f424d82463505) build(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.2 ([#15171](https://github.com/ghostty-org/ghostty/issues/15171)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request)
  from 8.1.1 to 8.1.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/peter-evans/create-pull-request/releases">peter-evans/create-pull-request's
  releases</a>.</em></p>
  <blockquote>
  <h2>Create Pull Request v8.1.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update distribution by <a
  href="https://github.com/actions-bot"><code>@​actions-bot</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4361">peter-evans/create-pull-request#4361</a></li>
  <li>build(deps-dev): bump the npm group with 2 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4372">peter-evans/create-pull-request#4372</a></li>
  <li>refactor: replace <code>uuid</code> dep with Node.js built-in
  <code>crypto.randomUUID</code> by <a
  href="https://github.com/peter-evans"><code>@​peter-evans</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4377">peter-evans/create-pull-request#4377</a></li>
  <li>build(deps): update to jest 30 by <a
  href="https://github.com/peter-evans"><code>@​peter-evans</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4388">peter-evans/create-pull-request#4388</a></li>
  <li>build(deps-dev): bump the npm group across 1 directory with 7
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4391">peter-evans/create-pull-request#4391</a></li>
  <li>build(deps-dev): bump undici from 6.25.0 to 6.27.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4386">peter-evans/create-pull-request#4386</a></li>
  <li>build(deps-dev): bump js-yaml from 4.2.0 to 5.0.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4387">peter-evans/create-pull-request#4387</a></li>
  <li>chore: pin actions to commit shas by <a
  href="https://github.com/peter-evans"><code>@​peter-evans</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4406">peter-evans/create-pull-request#4406</a></li>
  <li>build(deps): bump actions/checkout from 6.0.3 to 7.0.0 in the
  github-actions group by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4411">peter-evans/create-pull-request#4411</a></li>
  <li>build(deps-dev): bump the npm group with 2 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4418">peter-evans/create-pull-request#4418</a></li>
  <li>build(deps-dev): bump js-yaml from 5.2.0 to 5.2.1 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4423">peter-evans/create-pull-request#4423</a></li>
  <li>build(deps-dev): bump js-yaml from 5.2.1 to 5.2.2 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4430">peter-evans/create-pull-request#4430</a></li>
  <li>build(deps-dev): bump the npm group with 4 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4436">peter-evans/create-pull-request#4436</a></li>
  <li>build(deps): bump the github-actions group with 2 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4435">peter-evans/create-pull-request#4435</a></li>
  <li>build(deps): bump brace-expansion by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4446">peter-evans/create-pull-request#4446</a></li>
  <li>build(deps-dev): bump the npm group with 4 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4452">peter-evans/create-pull-request#4452</a></li>
  <li>Update distribution by <a
  href="https://github.com/actions-bot"><code>@​actions-bot</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4457">peter-evans/create-pull-request#4457</a></li>
  <li>build(deps-dev): bump browserslist from 4.28.4 to 4.28.8 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4462">peter-evans/create-pull-request#4462</a></li>
  <li>build(deps-dev): bump js-yaml from 4.2.0 to 5.4.2 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4468">peter-evans/create-pull-request#4468</a></li>
  <li>build(deps-dev): bump undici from 6.28.0 to 6.29.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4478">peter-evans/create-pull-request#4478</a></li>
  <li>build(deps-dev): bump the npm group with 4 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4483">peter-evans/create-pull-request#4483</a></li>
  <li>build(deps): bump brace-expansion by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4486">peter-evans/create-pull-request#4486</a></li>
  <li>build(deps-dev): bump handlebars from 4.7.9 to 4.7.10 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4494">peter-evans/create-pull-request#4494</a></li>
  <li>build(deps-dev): bump undici from 6.29.0 to 6.29.1 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4504">peter-evans/create-pull-request#4504</a></li>
  <li>build(deps): bump the github-actions group with 3 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4510">peter-evans/create-pull-request#4510</a></li>
  <li>build(deps-dev): bump the npm group with 4 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4509">peter-evans/create-pull-request#4509</a></li>
  <li>Fix submodule deletion with <code>sign-commits</code> by <a
  href="https://github.com/MrSubidubi"><code>@​MrSubidubi</code></a> in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4473">peter-evans/create-pull-request#4473</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a
  href="https://github.com/MrSubidubi"><code>@​MrSubidubi</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4473">peter-evans/create-pull-request#4473</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/peter-evans/create-pull-request/compare/v8.1.1...v8.1.2">https://github.com/peter-evans/create-pull-request/compare/v8.1.1...v8.1.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8"><code>15733db</code></a>
  fix: submodule deletion with <code>sign-commits</code> (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4473">#4473</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/3afad46a91e1234a4e2800ffa47bd6c2a6b66b6c"><code>3afad46</code></a>
  build(deps-dev): bump the npm group with 4 updates (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4509">#4509</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/aee70bea9c02648f8341785c1d3c9ea1ed236345"><code>aee70be</code></a>
  build(deps): bump the github-actions group with 3 updates (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4510">#4510</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/86c87cfdd87dd582eb8b8f226cfec4e09d825326"><code>86c87cf</code></a>
  build(deps-dev): bump undici from 6.29.0 to 6.29.1 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4504">#4504</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/bd09a93810788ce61d2d5fb7d6b221b9b4a4aab7"><code>bd09a93</code></a>
  build(deps-dev): bump handlebars from 4.7.9 to 4.7.10 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4494">#4494</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/59910dc44801a4d984ba473b7c2f20b850f9a584"><code>59910dc</code></a>
  build(deps): bump brace-expansion (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4486">#4486</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/753b4376e5ffbead0e18763fa5cb8d642f91a594"><code>753b437</code></a>
  build(deps-dev): bump the npm group with 4 updates (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4483">#4483</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/abadea5d9424d1faad6a446b8c98516703d32a88"><code>abadea5</code></a>
  build(deps-dev): bump undici from 6.28.0 to 6.29.0 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4478">#4478</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/11e8dc7c9cc95aabee9cfaa85faaec8b50907340"><code>11e8dc7</code></a>
  build(deps-dev): bump js-yaml from 4.2.0 to 5.4.2 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4468">#4468</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/c9f8b51aaac1dfba340a97878061732b0e738ec1"><code>c9f8b51</code></a>
  build(deps-dev): bump browserslist from 4.28.4 to 4.28.8 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4462">#4462</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/peter-evans/create-pull-request/compare/5f6978faf089d4d20b00c7766989d076bb2fc7f1...15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=peter-evans/create-pull-request&package-manager=github_actions&previous-version=8.1.1&new-version=8.1.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`ef1649c`](https://github.com/ghostty-org/ghostty/commit/ef1649c8536132f1bb8ac80824a93ef0c2811c95) ci: shard the unit tests, run one test shard per core ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new custom Zig test runner (copied from Zig 0.17's test runner
  with ~66 lines added) to add support for sharding tests
  equally/naively.
  
  We run our unit tests now through this new runner and shard by core
  count (up to 64) and this drops out test times significantly (basically
  by a multiple of core count). Timings on my machines shown below.
  
  A couple more changes along the way to speed up CI:
  
  - We build tests using Zig's self-hosted backend instead of LLVM. This
    sped up our compile times by almost 4x.
  
  - The two slowest tests were mostly spending time in integrity checks.
    We now pause integrity and run it once per page instead of per op.
  
  - build-libghostty-vt-features builds its eleven -Dvt-features
    configurations as a matrix instead of a loop in one job. W
  
  Speed changes for me on my 16-core Linux machine (except the last one):
  
  | Step                                       |       Before |                 After |
  | ------------------------------------------ | -----------: | --------------------: |
  | Compile ghostty-test                       | 210 s (LLVM) |    66 s (self-hosted) |
  | `zig build test`, compile and run          |      ~1400 s | 243 s wall, 912 s CPU |
  | snapshot.page hyperlink map test           |        199 s |                  13 s |
  | PageList backfill pin remap test           |        111 s |                  16 s |
  | `zig build test-lib-vt` on a 30-core Mac   |      ~24 min |                 4 min |
  ```
- [`5fa3bce`](https://github.com/ghostty-org/ghostty/commit/5fa3bce60094cb95d272f8a7c9836a6d8eb1d66b) build: run the valgrind test shards at the same time ([@mitchellh](https://github.com/mitchellh))
  ```text
  | Shards | Before   | After    | Longest shard | Peak RSS per process |
  | -----: | -------: | -------: | ------------: | -------------------: |
  |      1 |          | 17.1 min |      17.0 min |              1.16 GB |
  |      2 |          | 11.3 min |      11.2 min |              0.95 GB |
  |      4 |          |  8.9 min |       8.8 min |              0.82 GB |
  |      8 |          |  7.1 min |       7.0 min |              0.76 GB |
  |     16 | 20.2 min |  7.1 min |       7.1 min |              0.71 GB |
  ```
- [`f22d3ee`](https://github.com/ghostty-org/ghostty/commit/f22d3ee243bf8faa77da98355cc34f1bb27df488) ci: run the GTK and -Dsimd=false test jobs on the 8 vCPU runner ([@mitchellh](https://github.com/mitchellh))
  ```text
  This moves the two test-running jobs to the md runner.
  
  | Job                       | Runner | Test step |    Total |
  | ------------------------- | ------ | --------: | -------: |
  | test                      | md     |   3.1 min |  5.0 min |
  | GTK x11=true wayland=true | sm     |   8.3 min | 10.1 min |
  | Test -Dsimd=false         | sm     |   8.4 min |  8.6 min |
  ```
- [`dd22777`](https://github.com/ghostty-org/ghostty/commit/dd22777727b4be15275dce40e60f50b32749a831) ci: let Zig fetch packages on macOS instead of nix build .#deps ([@mitchellh](https://github.com/mitchellh))
- [`0ae4cb5`](https://github.com/ghostty-org/ghostty/commit/0ae4cb559fcdae34e21b5dcbfe181be07d475c02) terminal: halve the op counts of the printSlice differential tests ([@mitchellh](https://github.com/mitchellh))
  ```text
  | Test | Before | After |
  | ---- | -----: | ----: |
  | printSlice differential fuzz vs print | 75.4 s | 29.6 s |
  | printSlice differential fuzz vs print, CJK with spaces | 92.5 s | 30.1 s |
  ```
- [`f53b078`](https://github.com/ghostty-org/ghostty/commit/f53b0787c972f531bf9f0b3a84b2c1d8c07f1a63) ci: set up the FreeBSD VM while the test binary builds ([@mitchellh](https://github.com/mitchellh))
  ```text
  | Step                       | Before | After |
  | -------------------------- | -----: | ----: |
  | Build the test binary      |   174s |       |
  | Set up the VM              |    70s |       |
  | Build and set up together  |        |  178s |
  | Total                      |   244s |  178s |
  ```
- [`6cf5070`](https://github.com/ghostty-org/ghostty/commit/6cf50702dd1e0eb7cf86e354a9bc1f1220e8f0d5) ci: keep the Windows libghostty-vt Zig cache across runs ([@mitchellh](https://github.com/mitchellh))
  ```text
  | Step                  |   Cold |   Warm |
  | --------------------- | -----: | -----: |
  | zig build test-lib-vt | 13m00s |  6m47s |
  | Whole job             | 16m44s | 10m03s |
  ```
- [`d180d10`](https://github.com/ghostty-org/ghostty/commit/d180d1068b97ceae99ed5724cac55ffff2df693c) ci: run build-dist-lib-vt on the md runner ([@mitchellh](https://github.com/mitchellh))
  ```text
  | distcheck -Demit-lib-vt=true, cold cache | 4 cores | 8 cores |
  | ---------------------------------------- | ------: | ------: |
  | Wall time                                |   795 s |   482 s |
  | User CPU time                            |  1751 s |  1796 s |
  ```
- [`c3b594a`](https://github.com/ghostty-org/ghostty/commit/c3b594ad2b8a4323d3bc555a84f5e579e43d7009) ci: shard the unit tests, run one test shard per core ([#15169](https://github.com/ghostty-org/ghostty/issues/15169)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new custom Zig test runner (copied from Zig 0.17's test
  runner with ~66 lines added) to add support for sharding tests
  equally/naively.
  
  We run our unit tests now through this new runner and shard by core
  count (up to 64) and this drops out test times significantly (basically
  by a multiple of core count). Timings on my machines shown below.
  
  A couple more changes along the way to speed up CI:
  
  - We build tests using Zig's self-hosted backend instead of LLVM. This
  sped up our compile times by almost 4x.
  
  - The two slowest tests were mostly spending time in integrity checks.
  We now pause integrity and run it once per page instead of per op.
  
  - build-libghostty-vt-features builds its eleven -Dvt-features
  configurations as a matrix instead of a loop in one job. W
  
  Speed changes for me on my 16-core Linux machine (except the last one):
  
  | Step | Before | After |
  | ------------------------------------------ | -----------: |
  --------------------: |
  | Compile ghostty-test | 210 s (LLVM) | 66 s (self-hosted) |
  | `zig build test`, compile and run | ~1400 s | 243 s wall, 912 s CPU |
  | snapshot.page hyperlink map test | 199 s | 13 s |
  | PageList backfill pin remap test | 111 s | 16 s |
  | `zig build test-lib-vt` on a 30-core Mac | ~24 min | 4 min |
  
  **AI usage:** Fable validated the plan (I proposed sharding), I did the
  custom build runner fork, Opus did the YAML changes, I wrote this
  message.
  ```

## November 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42668142534), [2](https://github.com/ghostty-org/ghostty/actions/runs/42642081671), [3](https://github.com/ghostty-org/ghostty/actions/runs/42618500118), [4](https://github.com/ghostty-org/ghostty/actions/runs/42547101006)  
Summary: 4 runs • 21 commits • 6 authors

### Changes

- [`96d3798`](https://github.com/ghostty-org/ghostty/commit/96d379822f53828ceb37dc49cb1e22eb39021681) terminal: look up a row's styles once per segment in endUpdate ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  All runs in a pending segment belong to the same row. Resolve its cell
  storage and style column once before filling the runs. Clamp to the
  cell count so items(.style)'s capacity check is not repeated.
  
  On Windows x86-64 and aarch64 macOS, this moves the row lookup and
  capacity handling out of the per-run loop.
  ```
- [`15a4432`](https://github.com/ghostty-org/ghostty/commit/15a44323408cbc79987406a0b46452b49e935b9a) terminal: walk pending style runs as a shrinking slice in endUpdate ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Walk the pending runs as a shrinking slice instead of tracking each
  row’s segment with two indices.
  
  This reduces per-segment setup from 11 instructions to 5 on Windows x86-64,
  and from 9 to 5 on aarch64 macOS. LLVM can now prove the segment is nonempty,
  which removes redundant checks before comparing and filling its styles.
  ```
- [`f28124c`](https://github.com/ghostty-org/ghostty/commit/f28124c734bbcd0598a521623fa573a915e37157) terminal: simplify style-run processing in endUpdate ([#15163](https://github.com/ghostty-org/ghostty/issues/15163)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A couple of small codegen improvements to `RenderState.endUpdate`: walk
  pending style runs as a shrinking slice, and look up each row’s styles
  once per segment rather than once per run.
  
  This reduces segment setup and removes redundant checks on Windows
  x86-64 and in cross-compiled aarch64 macOS output.
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`cd16aeb`](https://github.com/ghostty-org/ghostty/commit/cd16aeb0a7724b513e25725ffc0480119f7a74e8) terminal: log stream handler errors out of line ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  The stream handlers log errors inline in `vt` and `vtPrintAscii`, which
  puts logging and formatting code on the hot path.
  
  Move failure handling to a cold helper. On Windows x86-64, this
  reduces the stack allocation of `vtPrintAscii` from 2456 to 296 bytes.
  ```
- [`691d3f3`](https://github.com/ghostty-org/ghostty/commit/691d3f38b80a2c6382201e9d1164ef1a841526ad) terminal: simplify CSI digit parsing and accumulation ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `consumeCsiParams` accumulated each digit with saturating u16 operations,
  which compiled to a 16-bit `mul` and two `cmov`s on x86-64. LLVM also
  lowered its switch so that every digit was first tested as a separator,
  then as a digit, then against `MAX_PARAMS`.
  
  Accumulate in a u32 and clamp once per digit, which preserves the parser's
  u16 saturation behavior. Test for digits before the switch and skip the
  `MAX_PARAMS` check. Sequences with too many parameters are dropped at
  dispatch, so their accumulator is never used.
  
  On x86-64, LLVM now generates 14 instructions and 2 branches per digit
  instead of 23 instructions and 5 branches.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Windows x86-64:
  
  | Input         | Size   | Before (ms)   | After (ms)    | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------- |
  | styled-heavy  | 120x80 | 314.5 ± 4.1   | 308.6 ± 6.9   | 1.02x   |
  | styled-multi  | 120x80 | 375.4 ± 3.3   | 360.1 ± 4.7   | 1.04x   |
  | ASCII         | 120x80 | 49.9 ± 1.5    | 49.7 ± 2.0    | 1.00x   |
  | dense_cells   | 160x50 | 112.8 ± 4.0   | 107.0 ± 3.9   | 1.05x   |
  | DOOM-fire-zig | 160x50 | 190.8 ± 3.8   | 188.2 ± 3.3   | 1.01x   |
  ```
- [`c1f4409`](https://github.com/ghostty-org/ghostty/commit/c1f4409661b0404779d16e09d820427d86815a3e) terminal: speed up UTF-8 error case in SIMD decoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  DecodeUTF8 used to run simdutf's converting pass again after every
  invalid sequence and then, since #15156, decode the valid prefix a
  second time because simdutf's output is undefined on error. Every valid
  run after the first error was decoded twice. After the first error we
  now find the next one with the read-only validator and decode each
  valid run once. Clean input still takes the single fused pass.
  
  This makes the error path cheaper than it was before #15156, with no
  change on valid input.
  
  | Input         | Before #15156 | #15156 | This commit |   Wall ms (before / #15156 / this) |
  | ------------- | ------------: | -----: | ----------: | ---------------------------------: |
  | utf8-inv0     |          4270 |   4270 |        4252 |              316.3 / 316.7 / 317.0 |
  | utf8-inv0.001 |          4292 |   4392 |        4320 |              318.9 / 329.7 / 325.4 |
  | utf8-inv0.01  |          4497 |   4816 |        4502 |              343.5 / 383.2 / 360.8 |
  | utf8-inv0.1   |          6171 |   6602 |        5797 |              473.2 / 570.0 / 518.0 |
  | ascii-inv0.01 |          8123 |   8150 |        8077 |              590.2 / 585.9 / 582.3 |
  | ascii-inv0.1  |         10437 |  10576 |        9925 |              744.9 / 745.5 / 727.1 |
  | random        |         15046 |  15400 |       13241 |           1139.9 / 1189.9 / 1069.6 |
  ```
- [`582f769`](https://github.com/ghostty-org/ghostty/commit/582f769ddf6e6bfbe8ad5839de14702490eb59a6) terminal: speed up UTF-8 error case in SIMD decoding ([#15162](https://github.com/ghostty-org/ghostty/issues/15162)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DecodeUTF8 used to run simdutf's converting pass again after every
  invalid sequence and then, since #15156, decode the valid prefix a
  second time because simdutf's output is undefined on error. Every valid
  run after the first error was decoded twice. After the first error we
  now find the next one with the read-only validator and decode each valid
  run once. Clean input still takes the single fused pass.
  
  This makes the error path cheaper than it was before #15156, with no
  change on valid input.
  
  | Input | Before #15156 | #15156 | This commit | Wall ms (before /
  #15156 / this) |
  | ------------- | ------------: | -----: | ----------: |
  ---------------------------------: |
  | utf8-inv0 | 4270 | 4270 | 4252 | 316.3 / 316.7 / 317.0 |
  | utf8-inv0.001 | 4292 | 4392 | 4320 | 318.9 / 329.7 / 325.4 |
  | utf8-inv0.01 | 4497 | 4816 | 4502 | 343.5 / 383.2 / 360.8 |
  | utf8-inv0.1 | 6171 | 6602 | 5797 | 473.2 / 570.0 / 518.0 |
  | ascii-inv0.01 | 8123 | 8150 | 8077 | 590.2 / 585.9 / 582.3 |
  | ascii-inv0.1 | 10437 | 10576 | 9925 | 744.9 / 745.5 / 727.1 |
  | random | 15046 | 15400 | 13241 | 1139.9 / 1189.9 / 1069.6 |
  ```
- [`8cf026b`](https://github.com/ghostty-org/ghostty/commit/8cf026b1608e6d3b099a05244406a0c4bd49c539) terminal: log stream handler errors out of line ([#15160](https://github.com/ghostty-org/ghostty/issues/15160)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The stream handlers log errors inline in `vt` and `vtPrintAscii`, which
  puts logging and formatting code in the hot functions.
  
  This moves failure handling to a cold helper. On Windows x86-64, this
  reduces the stack allocation of `vtPrintAscii` from 2456 to 296 bytes.
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`2166b44`](https://github.com/ghostty-org/ghostty/commit/2166b446eece5f402809681105b377d8dd602378) terminal: simplify CSI digit parsing and accumulation ([#15161](https://github.com/ghostty-org/ghostty/issues/15161)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `consumeCsiParams` accumulated each digit with saturating u16
  operations, which compiled to a 16-bit `mul` and two `cmov`s on x86-64.
  LLVM also lowered its switch so that every digit was first tested as a
  separator, then as a digit, then against `MAX_PARAMS`.
  
  This accumulates in a u32 and clamps once per digit, which preserves the
  parser's u16 saturation behavior. This also tests for digits before the
  switch and skips the `MAX_PARAMS` check in the digit path. Sequences
  with too many parameters are dropped at dispatch, so their accumulator
  is never used.
  
  On x86-64, LLVM now generates 14 instructions and 2 branches per digit
  instead of 23 instructions and 5 branches.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Windows x86-64:
  
  | Input         | Size   | Before (ms)   | After (ms)    | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------- |
  | styled-heavy  | 120x80 | 314.5 ± 4.1   | 308.6 ± 6.9   | 1.02x   |
  | styled-multi  | 120x80 | 375.4 ± 3.3   | 360.1 ± 4.7   | 1.04x   |
  | ASCII         | 120x80 | 49.9 ± 1.5    | 49.7 ± 2.0    | 1.00x   |
  | dense_cells   | 160x50 | 112.8 ± 4.0   | 107.0 ± 3.9   | 1.05x   |
  | DOOM-fire-zig | 160x50 | 190.8 ± 3.8   | 188.2 ± 3.3   | 1.01x   |
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`7188495`](https://github.com/ghostty-org/ghostty/commit/7188495aaf805d028b26c81aca61c432b2009798) fix(i18n/id_ID): update Bahasa Indonesia translation ([@clavinjune](https://github.com/clavinjune))
- [`e04bf76`](https://github.com/ghostty-org/ghostty/commit/e04bf763c619fefd9712e05af5255a6fdd2ca107) fix(i18n/id_ID): update Bahasa Indonesia translation ([@clavinjune](https://github.com/clavinjune))
- [`411b133`](https://github.com/ghostty-org/ghostty/commit/411b1330f079e33c1df6b9bfc68e2d275f647e8a) fix(i18n/id_ID): update Bahasa Indonesia translation ([@clavinjune](https://github.com/clavinjune))
- [`4133776`](https://github.com/ghostty-org/ghostty/commit/41337762a831730cadc827025f3cc72f0dc0baf8) fix(i18n/id_ID): update Bahasa Indonesia translation ([@clavinjune](https://github.com/clavinjune))
- [`26d98cf`](https://github.com/ghostty-org/ghostty/commit/26d98cf276dd3bec8e117c0af9ab9c11d2ae3a18) Merge branch 'ghostty-org:main' into fix/i18n ([@clavinjune](https://github.com/clavinjune))
- [`b057818`](https://github.com/ghostty-org/ghostty/commit/b057818921aecb4139874018ebe36f07448dac88) Merge branch 'ghostty-org:main' into fix/i18n ([@clavinjune](https://github.com/clavinjune))
- [`0f10e66`](https://github.com/ghostty-org/ghostty/commit/0f10e6698eed3505c780400929d1966b45db111a) simd: decode the valid prefix again when simdutf reports an error ([@jcollie](https://github.com/jcollie))
  ```text
  When convert_utf8_to_utf32_with_errors hits invalid UTF-8, DecodeUTF8
  assumed the output before the error was already decoded and only
  counted how many codepoints that was. simdutf promises nothing about
  the output on error, and its icelake (AVX-512) kernels don't leave the
  valid prefix there, so text before an invalid sequence comes out as
  garbage. Ghostty's vendored simdutf is built without the icelake
  kernels, which hid this, but a build against a system simdutf
  (-fsys=simdutf) on an AVX-512 CPU fails `decode simd matches scalar`
  and decodes terminal output wrongly.
  
  Everything before the error position is valid UTF-8, so convert it
  again with convert_valid_utf8_to_utf32, which costs about what the
  count_utf8 pass it replaces did. The all-valid path is unchanged.
  
  See: https://github.com/ghostty-org/ghostty/discussions/15152
  ```
- [`354d59d`](https://github.com/ghostty-org/ghostty/commit/354d59dcd7b9a84ec068f2efa52e1f55947a9e48) simdutf: build the icelake (AVX-512) kernels again ([@jcollie](https://github.com/jcollie))
  ```text
  The vendored simdutf was built with SIMDUTF_IMPLEMENTATION_ICELAKE=0
  to work around https://github.com/ziglang/zig/issues/20414, where Zig
  0.13 couldn't compile simdutf's AVX-512 code. Zig 0.17 builds it
  for x86_64 Linux, macOS and Windows targets, so drop the workaround
  and let simdutf pick its icelake kernels at runtime on CPUs that have
  them, like a system simdutf already does.
  
  Those kernels don't leave the valid prefix in the output when they hit
  an error, which the previous commit stopped relying on.
  
  Highway's AVX-512 targets stay disabled: Highway 1.2 asks for the
  "evex512" target feature, which clang 22 removed, so they don't
  compile with the current Zig until we update to Highway 1.4. Update
  the comment there to say so.
  ```
- [`cf5519b`](https://github.com/ghostty-org/ghostty/commit/cf5519b22f910ddc7885d2ef62deb94d38d43f22) simdutf: fix AVX512 builds ([#15156](https://github.com/ghostty-org/ghostty/issues/15156)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig 0.13 had problems building for AVX512 so we stopped building the
  vendored simdutf and highway for those targets. If you linked Ghostty to
  a system simdutf that had AVX512 enabled you'd have problems with
  garbled input because the simdutf AVX512 kernels didn't leave the
  buffers in a valid state like other kernels did.
  
  Fixes:  #15155
  
  AI  disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`393a3a7`](https://github.com/ghostty-org/ghostty/commit/393a3a7c7d6a00e34072d3936e0373451408ca6f) i18n: update Bahasa Indonesia translation ([#15117](https://github.com/ghostty-org/ghostty/issues/15117)) ([@trag1c](https://github.com/trag1c))
  ```text
  updating latest commit at
  https://github.com/ghostty-org/ghostty/commit/dce5a9464a25b946cc945ebd99c93441cd7a1e9c
  with Bahasa Indonesia translation
  ```
- [`219e5a4`](https://github.com/ghostty-org/ghostty/commit/219e5a475ce49a13923194eed29ee834683482a4) build(deps): bump softprops/action-gh-release from 3.0.3 to 3.0.4 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.3 to 3.0.4.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/efb35369e0ad2afab669f228072c1b0d510eae64...8a0cd651e5b2365bd640854a3fa5dfc70e4875f3)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.4
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`711702d`](https://github.com/ghostty-org/ghostty/commit/711702d572cfef2897b898d7147050fc6808f6e6) build(deps): bump softprops/action-gh-release from 3.0.3 to 3.0.4 ([#15153](https://github.com/ghostty-org/ghostty/issues/15153)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.3 to 3.0.4.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.4</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>3.0.4</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <h2>3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  <h2>3.0.2</h2>
  <p><code>3.0.2</code> is a patch release focused on release reliability
  and compatibility. It
  reuses existing draft releases when publishing prereleases, supports
  replacing
  release assets on Gitea, hardens streamed asset uploads, and provides
  clearer
  release-creation diagnostics. It also includes TypeScript, coverage, and
  tooling
  maintenance merged since <code>3.0.1</code>.</p>
  <p>This release fixes <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/795">#795</a>,
  <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/438">#438</a>,
  and <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/803">#803</a>.
  The upload transport hardening covers the
  historical failure reported in <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/790">#790</a>,
  although current hosted Node 24 runners did
  not reproduce it naturally. The diagnostics work is related to <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/786">#786</a>
  and does not
  claim a reproducible release-creation fix.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: improve release error reporting and test coverage by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/813">softprops/action-gh-release#813</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: publish existing draft releases as prereleases by <a
  href="https://github.com/godfengliang"><code>@​godfengliang</code></a>
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/801">softprops/action-gh-release#801</a></li>
  <li>fix: upload small checksum assets reliably by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/815">softprops/action-gh-release#815</a></li>
  <li>fix: replace existing release assets on Gitea by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/816">softprops/action-gh-release#816</a></li>
  <li>fix: clarify release creation 404 errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/817">softprops/action-gh-release#817</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): upgrade TypeScript to 7 by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/812">softprops/action-gh-release#812</a></li>
  <li>chore(deps): remove unused TypeScript tooling by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/814">softprops/action-gh-release#814</a></li>
  <li>dependency, Node 24 pin, and CI maintenance merged since
  <code>3.0.1</code></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/8a0cd651e5b2365bd640854a3fa5dfc70e4875f3"><code>8a0cd65</code></a>
  release 3.0.4 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/865">#865</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/ac0115469478f6d234bc639fb400df76407ebac1"><code>ac01154</code></a>
  chore(deps): bump the npm group across 1 directory with 4 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/864">#864</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/ca4c9d538ca27e61dd657936e1633b212b1d7c48"><code>ca4c9d5</code></a>
  chore(deps): bump minimatch and glob (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/862">#862</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/e4a57aec134ea157c36650f6fac99635cae7acf3"><code>e4a57ae</code></a>
  chore(deps): bump undici from 6.29.0 to 6.29.1 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/859">#859</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/ee55a0ef7ddd6c21e04956e5ad9b5c8728309f57"><code>ee55a0e</code></a>
  chore(deps): bump vite from 8.3.2 to 8.3.5 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/855">#855</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/8d42b221d50157ff3763aed11ff814f61a9b183a"><code>8d42b22</code></a>
  chore(deps): bump actions/setup-node (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/853">#853</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/6680cc089e59314c4460b839412c25fb6a71ce3b"><code>6680cc0</code></a>
  chore(deps): bump the npm group with 3 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/851">#851</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/4a050bafc07a1fefdf1754ffad477e371be3b35a"><code>4a050ba</code></a>
  chore(deps): bump source-map-js from 1.2.1 to 1.2.2 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/850">#850</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/b5a645e6d7f681d09866ab86ba7918b222989555"><code>b5a645e</code></a>
  chore(deps): bump the npm group with 4 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/848">#848</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/d99a5de30622195878649ed880754cdff26c7d6e"><code>d99a5de</code></a>
  chore(deps): bump brace-expansion from 5.0.9 to 5.0.12 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/846">#846</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/efb35369e0ad2afab669f228072c1b0d510eae64...8a0cd651e5b2365bd640854a3fa5dfc70e4875f3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.3&new-version=3.0.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## November 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42528435750), [2](https://github.com/ghostty-org/ghostty/actions/runs/42526053671), [3](https://github.com/ghostty-org/ghostty/actions/runs/42507357424), [4](https://github.com/ghostty-org/ghostty/actions/runs/42505532992), [5](https://github.com/ghostty-org/ghostty/actions/runs/42453768003), [6](https://github.com/ghostty-org/ghostty/actions/runs/42448097492)  
Summary: 6 runs • 21 commits • 7 authors

### Changes

- [`86c206b`](https://github.com/ghostty-org/ghostty/commit/86c206bb39c0688080b6781ec158f48d080957da) libghostty-vt: relocatable pkg-config files on Windows, build aarch64-windows-gnu ([@mitchellh](https://github.com/mitchellh))
- [`5237cde`](https://github.com/ghostty-org/ghostty/commit/5237cde0edda3e0d0368efd55e588eddd1af7598) libghostty-vt: check a moved ReleaseFast Windows install tree with a reusable script ([@mitchellh](https://github.com/mitchellh))
- [`1d69295`](https://github.com/ghostty-org/ghostty/commit/1d69295abaff5d96dec2a7f97371f676293e2a63) libghostty-vt: define GHOSTTY_STATIC in the installed static CMake target and pkg-config file ([@mitchellh](https://github.com/mitchellh))
- [`b4cef71`](https://github.com/ghostty-org/ghostty/commit/b4cef71f795dec91b7d4e07a4c72a1c627884948) libghostty-vt: document the prebuilt Windows zips and write the README they ship with ([@mitchellh](https://github.com/mitchellh))
- [`ee16590`](https://github.com/ghostty-org/ghostty/commit/ee16590c411018eb554a8b7c824f2c7975c49fa8) libghostty-vt: build, zip and sign the Windows x64 and Windows on Arm release files ([@mitchellh](https://github.com/mitchellh))
- [`c7db8a6`](https://github.com/ghostty-org/ghostty/commit/c7db8a665fb54acb9b2c24f6d76e175556056561) libghostty-vt: check the Windows release zips on Windows before publishing ([@mitchellh](https://github.com/mitchellh))
- [`c786f94`](https://github.com/ghostty-org/ghostty/commit/c786f941f3b63f04a2c97d4c64cdd63cbdb589c4) libghostty-vt: publish prebuilt Windows zips for x86_64 and aarch64 ([#15151](https://github.com/ghostty-org/ghostty/issues/15151)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR publishes two new zips alongside any libghosty-vt release for
  Windows x86_64 and aarch64.
  
  Each zip contains:
  
  - DLL
  - PDB
  - Import library
  - Static lib
  - Headers
  - CMake package
  - pkg-config files
  - LICENSE, README
  
  Changes needed to make the zips work properly:
  
  - The Windows pkg-config files are now relocatable
  (`prefix=${pcfiledir}/../..`).
  - The installed `ghostty-vt::ghostty-vt-static` target and
  `libghostty-vt-static.pc` now define `GHOSTTY_STATIC`. Without it the
  headers declare every function dllimport and a static link on Windows
  fails.
  
  **AI usage:** Fable researched the ecosystem conventions since I'm not
  totally familiar with Windows and helped propose a plan. I'm not totally
  ignorant on Windows norms so I was able to review it, and look up and
  google things I wasn't sure of myself. Opus implemented all the build
  changes. I wrote the Doxygen docs, README, and commit messages and PR.
  ```
- [`321a32a`](https://github.com/ghostty-org/ghostty/commit/321a32a42393ab12721d2308ffff8957ce6853ad) terminal: fix scrollback not pulled down when growing rows and shrinking cols ([@noib3](https://github.com/noib3))
- [`4f11504`](https://github.com/ghostty-org/ghostty/commit/4f11504fc3cc06406a7b486c97d8c969c0ffb947) build: don't install the themes by default on Windows ([@jcollie](https://github.com/jcollie))
  ```text
  Asking for the iTerm2 themes package downloads and unpacks it whenever
  the build is configured, whichever steps were requested, so even
  `zig build test-lib-vt` fetches it. The current package has theme
  names with a colon in them ("Neon Raincheck: After Hours" and others),
  which aren't valid Windows file names, so the unpack fails on Windows
  and takes the build-libghostty-vt-windows CI job down with it.
  
  There is no Windows app to install themes for, so default
  `-Demit-themes` to false there. `-Demit-themes=true` still asks for
  them.
  ```
- [`32d1c69`](https://github.com/ghostty-org/ghostty/commit/32d1c698bab7fc1ff95fccf7d815d0e0125dde26) build: don't install the themes by default on Windows ([#15149](https://github.com/ghostty-org/ghostty/issues/15149)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Asking for the iTerm2 themes package downloads and unpacks it whenever
  the build is configured, whichever steps were requested, so even `zig
  build test-lib-vt` fetches it. The current package has theme names with
  a colon in them ("Neon Raincheck: After Hours" and others), which aren't
  valid Windows file names, so the unpack fails on Windows and takes the
  build-libghostty-vt-windows CI job down with it.
  
  There is no Windows app to install themes for, so default
  `-Demit-themes` to false there. `-Demit-themes=true` still asks for
  them.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`e0e5728`](https://github.com/ghostty-org/ghostty/commit/e0e57281d737f3ffc5252503d73dff0125c51841) terminal: fix scrollback not pulled down when growing rows and shrinking cols ([#15141](https://github.com/ghostty-org/ghostty/issues/15141)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR fixes an issue where a resize that grows the rows and shrinks
  the columns at the same time pushed the rows it pulled down from
  scrollback right back into it, unlike doing the two resizes one after
  the other.
  
  Found while using Neovim's terminal, where a layout change can resize a
  split across both dimensions at once.
  
  AI disclosure: 🤖 identified the bug, I wrote the fix, 🤖 wrote the
  regression test, I wrote this description.
  ```
- [`eb895f6`](https://github.com/ghostty-org/ghostty/commit/eb895f6128dba382ffeb5fedea97dcd61fcb5979) Update VOUCHED list ([#15146](https://github.com/ghostty-org/ghostty/issues/15146)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15142#discussioncomment-19476906)
  from @jcollie.
  
  Vouch: @neomantra
  ```
- [`e5e9bdb`](https://github.com/ghostty-org/ghostty/commit/e5e9bdb44ebbe9e105033e27474825b010310009) Update VOUCHED list ([#15145](https://github.com/ghostty-org/ghostty/issues/15145)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15144#discussioncomment-19476492)
  from @jcollie.
  
  Vouch: @johnrichardrinehart
  ```
- [`e356223`](https://github.com/ghostty-org/ghostty/commit/e356223d3c1a894aa9cbb479bec30988bcaebb5a) add NSColorExtension test for distance ([@francislata](https://github.com/francislata))
- [`3119f12`](https://github.com/ghostty-org/ghostty/commit/3119f12b6e4fece3a081a0374454dcfd307a75b0) update test case name ([@francislata](https://github.com/francislata))
- [`e035beb`](https://github.com/ghostty-org/ghostty/commit/e035beb9437118b803830a5864ea2f4dd7094354) Add NSColorTests for NSColor+Extension ([#15139](https://github.com/ghostty-org/ghostty/issues/15139)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  # Overview
  This PR adds some tests to the `distance(to:)` extension of
  `NSColor+Extension.swift`.
  
  This increased the coverage from `0.0%` to `35.5%`.
  
  # Details
  In this PR, I only added tests to `distance(to:)` as it is the main
  function exposed within the extension.
  
  I'm adding these tests to further increase the macOS test coverage
  (#7879).
  ```
- [`b543fbe`](https://github.com/ghostty-org/ghostty/commit/b543fbed1a83da7918a7de65ad8ac733c57ceef8) terminal: add render OOM regression test ([@Uzaaft](https://github.com/Uzaaft))
- [`3e29fcd`](https://github.com/ghostty-org/ghostty/commit/3e29fcd628a50757ad24988c721340e56f392485) terminal: retry dirty rows after failed render updates ([@Uzaaft](https://github.com/Uzaaft))
- [`3a69a97`](https://github.com/ghostty-org/ghostty/commit/3a69a97b6070c1789cad760a1bd646620fe3ae01) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`e33e4cf`](https://github.com/ghostty-org/ghostty/commit/e33e4cf83006b541a73074029189e7f9a499fd99) Update iTerm2 colorschemes ([#15140](https://github.com/ghostty-org/ghostty/issues/15140)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261102-150615-3d8a6a1
  ```
- [`59044f5`](https://github.com/ghostty-org/ghostty/commit/59044f5c5ee5764b69cc8153d307507cb1f400f5) terminal: retry dirty rows after failed render updates ([#15127](https://github.com/ghostty-org/ghostty/issues/15127)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  So tl;dr: a failed update marks unfinished work as finished
  
  Test pushed first to prove that this causes a crash before I push the
  patch a patch, that instead leaves failed rows marked as dirty, so the
  next update rebuilds them instead of using incomplete data. But I'm not
  sure of this is *sound* in a terminal.
  ```

## November 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42398288749), [2](https://github.com/ghostty-org/ghostty/actions/runs/42387649303), [3](https://github.com/ghostty-org/ghostty/actions/runs/42384512829), [4](https://github.com/ghostty-org/ghostty/actions/runs/42346179212), [5](https://github.com/ghostty-org/ghostty/actions/runs/42325700870)  
Summary: 5 runs • 12 commits • 4 authors

### Changes

- [`5ed7747`](https://github.com/ghostty-org/ghostty/commit/5ed7747e8db1414ab07ec814ec2c4cd242281396) terminal: enumFromC no longer scans every enum field ([@mitchellh](https://github.com/mitchellh))
- [`1b8b3f5`](https://github.com/ghostty-org/ghostty/commit/1b8b3f55bcc93d2685f7771948516af1222dcc46) terminal: remap pins when the column growth backfill stops early ([@mitchellh](https://github.com/mitchellh))
- [`358818e`](https://github.com/ghostty-org/ghostty/commit/358818ebddb9e4d0bcfb16fb2d3f559cb7c70257) terminfo: use a multi-word description field ([@jparise](https://github.com/jparise))
  ```text
  The last field of a terminfo name line is the entry's description, and
  ours was the single word "Ghostty". ncurses' tic warns about that on
  every compile because older tic versions may treat a description with
  no spaces as another alias:
  
      "<stdin>", line 1, col 31, terminal 'xterm-ghostty': older tic
      versions may treat the description field as an alias
  
  That warning shows up in `+ssh --verbose` and in manual installs.
  
  Use "Ghostty terminal emulator", which matches the description in
  ncurses' own ghostty entry:
  
  https://github.com/ThomasDickey/ncurses-snapshots/blob/26ceb3cbd343/misc/terminfo.src#L8870
  ```
- [`0aa2292`](https://github.com/ghostty-org/ghostty/commit/0aa22921cad37022529a56e064df24a009f01500) terminal: fix dangling pins on column growth resize, faster C enum validation ([#15134](https://github.com/ghostty-org/ghostty/issues/15134)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Two fixes from the libghostty 1.0 upgrade I found in Rex:
  
  - Dangling pins when growing columns without reflow.
  - A performance regression and fix: `enumFromC` no longer scans every
  field.
  
  **AI usage: Opus for tests.**
  ```
- [`27ffca0`](https://github.com/ghostty-org/ghostty/commit/27ffca0dd67177d1f069ea7f910362e5d871613d) terminfo: use a multi-word description field ([#15135](https://github.com/ghostty-org/ghostty/issues/15135)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The last field of a terminfo name line is the entry's description, and
  ours was the single word "Ghostty". ncurses' tic warns about that on
  every compile because older tic versions may treat a description with no
  spaces as another alias:
  
      "<stdin>", line 1, col 31, terminal 'xterm-ghostty': older tic
      versions may treat the description field as an alias
  
  That warning shows up in `+ssh --verbose` and in manual installs.
  
  Use "Ghostty terminal emulator", which matches the description in
  ncurses' own ghostty entry:
  
  
  https://github.com/ThomasDickey/ncurses-snapshots/blob/26ceb3cbd343/misc/terminfo.src#L8870
  ```
- [`3c3f331`](https://github.com/ghostty-org/ghostty/commit/3c3f33121a9be2389584db716248dbf0fa0439a6) cli: run the ssh terminfo install under sh ([@jparise](https://github.com/jparise))
  ```text
  ssh passes the remote command to the user's login shell, and the
  install script assumed POSIX syntax. Under tcsh, nushell, or elvish it
  failed to parse, so the install never succeeded, the host was never
  cached, and every connection retried it and printed a parse error
  before falling back to xterm-256color.
  
  The `command -v tic` check is gone too. It only kept fish from printing
  its own unknown-command error, and fish no longer runs the script.
  
  We also no longer need explicit error codes and can instead rely on `sh
  -c` exiting with the status of the last command.
  ```
- [`8265e74`](https://github.com/ghostty-org/ghostty/commit/8265e74cd3945c56d59aba3917ff01af33ba3e78) cli: run the ssh terminfo install under sh ([#15112](https://github.com/ghostty-org/ghostty/issues/15112)) ([@jcollie](https://github.com/jcollie))
  ```text
  ssh passes the remote command to the user's login shell, and the install
  script assumed POSIX syntax. Under tcsh, nushell, or elvish it failed to
  parse, so the install never succeeded, the host was never cached, and
  every connection retried it and printed a parse error before falling
  back to xterm-256color.
  
  The `command -v tic` check is gone too. It only kept fish from printing
  its own unknown-command error, and fish no longer runs the script.
  
  We also no longer need explicit error codes and can instead rely on `sh
  -c` exiting with the status of the last command.
  ```
- [`ac5374b`](https://github.com/ghostty-org/ghostty/commit/ac5374bd16829d556f7f3636a9a19ff7f506062a) Update VOUCHED list ([#15133](https://github.com/ghostty-org/ghostty/issues/15133)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15132#discussioncomment-19460089)
  from @bo2themax.
  
  Vouch: @Inv1x
  ```
- [`b57d75f`](https://github.com/ghostty-org/ghostty/commit/b57d75f4e2f4e017f52ce2458a91b63922dac1d9) libghostty: doxygen site works better on mobile ([@mitchellh](https://github.com/mitchellh))
  ```text
  Just brute forcing various CSS things to make the site look better on mobile.
  ```
- [`5813c94`](https://github.com/ghostty-org/ghostty/commit/5813c9461d5af78b6307a1254d00b1bc190eaccd) libghostty: doxygen site works better on mobile ([#15129](https://github.com/ghostty-org/ghostty/issues/15129)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Just brute forcing various CSS things to make the site look better on
  mobile.
  ```
- [`ea67530`](https://github.com/ghostty-org/ghostty/commit/ea675302b71a2413b16c77bb12659605bf736be2) libghostty-vt: start 1.1.0-dev, add the ABI baseline and version gate ([@mitchellh](https://github.com/mitchellh))
  ```text
  Housekeeping to move dev to 1.1.0 for libghostty. This also commits the
  ABI golden for future CI runs.
  
  This also fixes an issue where our tests didn't run properly on the 1.0
  tag, and we want it to run for the ABI golden upload.
  ```
- [`5acdbf1`](https://github.com/ghostty-org/ghostty/commit/5acdbf154369928eb228d2263cbe612d165f7569) libghostty-vt: start 1.1.0-dev, add the ABI baseline and version gate ([#15128](https://github.com/ghostty-org/ghostty/issues/15128)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Housekeeping to move dev to 1.1.0 for libghostty. This also commits the
  ABI golden for future CI runs.
  
  This also fixes an issue where our tests didn't run properly on the 1.0
  tag, and we want it to run for the ABI golden upload.
  ```

## November 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42306115040), [2](https://github.com/ghostty-org/ghostty/actions/runs/42286095862), [3](https://github.com/ghostty-org/ghostty/actions/runs/42284650139), [4](https://github.com/ghostty-org/ghostty/actions/runs/42274738908), [5](https://github.com/ghostty-org/ghostty/actions/runs/42265534130), [6](https://github.com/ghostty-org/ghostty/actions/runs/42237235647), [7](https://github.com/ghostty-org/ghostty/actions/runs/42225715062), [8](https://github.com/ghostty-org/ghostty/actions/runs/42201296689), [9](https://github.com/ghostty-org/ghostty/actions/runs/42199593118), [10](https://github.com/ghostty-org/ghostty/actions/runs/42195208227), [11](https://github.com/ghostty-org/ghostty/actions/runs/42162681903)  
Summary: 11 runs • 48 commits • 9 authors

### Changes

- [`0b7f9c1`](https://github.com/ghostty-org/ghostty/commit/0b7f9c156fd9daeb4361c234884c6afc68611566) libghostty-vt: some final C ABI cleanups ([@mitchellh](https://github.com/mitchellh))
  ```text
  Changes to the C API:
  
  - `ghostty_terminal_select_output` takes `const GhosttyGridRef*` rather
    than a struct by value.
  - `GHOSTTY_TERMINAL_DATA_CURSOR_STYLE` is now
    `GHOSTTY_TERMINAL_DATA_CURSOR_SGR_STYLE` with the same value, since
    `GhosttyCursorStyle` means the cursor shape.
  - The allocator vtable functions have named typedefs so the parity test
    can compare their signatures. The ABI is the same, but the Zig side
    moves to `anyopaque` to match the header's `void*`.
  - Render state keys that have no value to report return
    `GHOSTTY_NO_VALUE` rather than `GHOSTTY_INVALID_VALUE`.
  - NULL handles and output pointers no longer crash. Functions that
    return a `GhosttyResult` return `GHOSTTY_INVALID_VALUE`. Functions that
    can't report an error do nothing, or return false, 0, or NULL. The
    headers and the conventions page now document this.
  - `GHOSTTY_TERMINAL_OPT_GLYPH_PROTOCOL` is disabled by default, and a
    NULL value disables it again. Embedders opt in.
  - `ghostty_color_x11_names` returned a garbage pointer without the color
    feature. It now returns an empty table.
  - The Windows DLL exported the two CRT section markers, 211 exports
    against the 209 in `symbols.txt`. They now have hidden visibility.
  ```
- [`e852b90`](https://github.com/ghostty-org/ghostty/commit/e852b903f439e552b9debddd684d89fea1d433b6) libghostty-vt: some final C ABI cleanups ([#15125](https://github.com/ghostty-org/ghostty/issues/15125)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Changes to the C API:
  
  - `ghostty_terminal_select_output` takes `const GhosttyGridRef*` rather
  than a struct by value.
  - `GHOSTTY_TERMINAL_DATA_CURSOR_STYLE` is now
  `GHOSTTY_TERMINAL_DATA_CURSOR_SGR_STYLE` with the same value, since
  `GhosttyCursorStyle` means the cursor shape.
  - The allocator vtable functions have named typedefs so the parity test
  can compare their signatures. The ABI is the same, but the Zig side
  moves to `anyopaque` to match the header's `void*`.
  - Render state keys that have no value to report return
  `GHOSTTY_NO_VALUE` rather than `GHOSTTY_INVALID_VALUE`.
  - NULL handles and output pointers no longer crash. Functions that
  return a `GhosttyResult` return `GHOSTTY_INVALID_VALUE`. Functions that
  can't report an error do nothing, or return false, 0, or NULL. The
  headers and the conventions page now document this.
  - `GHOSTTY_TERMINAL_OPT_GLYPH_PROTOCOL` is disabled by default, and a
  NULL value disables it again. Embedders opt in.
  - `ghostty_color_x11_names` returned a garbage pointer without the color
  feature. It now returns an empty table.
  - The Windows DLL exported the two CRT section markers, 211 exports
  against the 209 in `symbols.txt`. They now have hidden visibility.
  
  **AI usage:** Some of these found by a Fable reviewer that I ran in
  parallel to me hand-reviewing every single header and signature. I wrote
  all the docs and this PR message.
  ```
- [`a859f49`](https://github.com/ghostty-org/ghostty/commit/a859f491075226a883506434aaefb8c552ceba61) libghostty-vt: prepare for 1.0.0 ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prepares libghostty-vt for its first release. The first tag will be
  `vt-1.0.0`. We're skipping 0.1.0 entirely, so it is never released and
  the docs no longer mention it or any pre-1.0 policy.
  
  This doesn't change the C API. The ABI goldens are untouched. The only
  binary differences are the version metadata below.
  ```
- [`0fa3d57`](https://github.com/ghostty-org/ghostty/commit/0fa3d577a5614150ff8e2c152de5fb9d5c6d2dec) libghostty-vt: prepare for 1.0.0 ([#15126](https://github.com/ghostty-org/ghostty/issues/15126)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prepares libghostty-vt for its first release. The first tag will be
  `vt-1.0.0`. We're skipping 0.1.0 entirely, so it is never released and
  the docs no longer mention it or any pre-1.0 policy.
  
  This is mostly a mechanical change of changing where 0.1 is mentioned to
  1.0. I used AI assistance to help me find all the places and also to run
  a swath of verification across multiple operating systems,in parallel to
  me doing the same.
  
  This doesn't change the C API. The ABI goldens are untouched. The only
  binary differences are the version metadata below.
  ```
- [`660a0a2`](https://github.com/ghostty-org/ghostty/commit/660a0a2bb1ed76f95a549601764ba62b36881e64) libghostty: add a test to ensure terminal modes are defined ([@jcollie](https://github.com/jcollie))
  ```text
  Adds a test to make sure that all terminal modes defined in Zig have a
  corresponding definition in `ghostty/vt.h`.
  
  - add `ghostty/vt.h` aliases so that every Zig mode name has a matching
    GHOSTTY_MODE_* macro
  - move the translate-c setup out of build.zig into src/build/c_deps.zig,
    which translates `ghostty.h` and `ghostty/vt.h` once per target and
    optimize mode and imports them as the `ghostty-h` and `ghostty-vt-h`
    modules
  - generalize checkGhosttyHEnum into checkEnum, used by both it and the
    new checkGhosttyVtHMacroExists; the macro check only tests that each
    macro exists, since a mode macro's value is not a plain integer
  - vendor EnumSet and EnumIndexer from the Zig 0.17.0 std library with
    an n^2 eval branch quota in EnumIndexer, since its sort falls back to
    insertion sort on short ranges and the mode table exceeds the n log n
    quota std uses
  ```
- [`9c77332`](https://github.com/ghostty-org/ghostty/commit/9c773327e23b1ef88fd6a1a8abe1323d20054e41) libghostty: translate ghostty/vt.h for the ABI tests through c_deps ([@jcollie](https://github.com/jcollie))
  ```text
  The C ABI tests translated `ghostty/vt.h` themselves in
  `GhosttyZig.initVtCTest`, so the C API test binary ended up with two
  translations of the same header. Have `c_deps` provide the one import,
  `ghostty-vt-h`, to both the mode test and the ABI tests.
  
  - only `ghostty.h` is skipped on wasm and Windows, since it includes
    `<sys/types.h>`; `ghostty/vt.h` needs only compiler-provided headers
    and now translates for every target, linking libc only if the module
    already does
  - translate for the module's own target and optimize mode by default,
    so that layout comparisons are made against the same target
  - include `link_libc` in the cache key
  - drop the wasm and Windows skip from `checkGhosttyVtHMacroExists`
  ```
- [`f80e4d5`](https://github.com/ghostty-org/ghostty/commit/f80e4d5c6bfc8f03a17af4bd1d6f0eeb211332b3) libghostty: rename the mode macros to match the Zig mode names ([@jcollie](https://github.com/jcollie))
  ```text
  Rather than carrying a second spelling of each mode macro as an alias,
  rename the GHOSTTY_MODE_* macros in `ghostty/vt/modes.h` so that each
  one matches the name of the mode in Zig, and drop the aliases. The docs
  and header comments that referred to the old names are updated to
  match.
  ```
- [`f6cb4cf`](https://github.com/ghostty-org/ghostty/commit/f6cb4cf1276c3cb1a027468ddeb1a976a822ccfa) libghostty: add a test to ensure terminal modes are defined ([#12230](https://github.com/ghostty-org/ghostty/issues/12230)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds a test to make sure that all terminal modes defined in Zig have a
  corresponding definition in `ghostty/vt.h`.
  
  AI disclosure: Claude Code was used to make some of the mechanical
  renames/cleanups.
  ```
- [`d03983f`](https://github.com/ghostty-org/ghostty/commit/d03983f02cbffc51b2d661facadab50dc2a209be) terminal: RefCountedSet reuses dead IDs instead of rehashing ([@mitchellh](https://github.com/mitchellh))
  ```text
  Once every ID in a `RefCountedSet` has been handed out, `add` now reuses
  the ID of a dead item (zero references) as long as at least 10% of IDs
  are dead. Previously, `add` returned `NeedsRehash` here and every caller
  responded by cloning the entire page at the same capacity just to
  compact the IDs.
  
  `ghostty-bench +terminal-stream` at 120x80, 8MiB inputs:
  
  | Input           | Scrollback | main (ms)   | set-reuse (ms) | Speedup |
  | --------------- | ---------- | ----------- | -------------- | ------- |
  | links.vt        | 0          | 87.6 ± 1.0  | 65.0 ± 0.4     | 1.35x   |
  | styled-heavy.vt | 0          | 49.2 ± 0.4  | 42.1 ± 0.2     | 1.17x   |
  | styled-mixed.vt | 0          | 87.2 ± 0.3  | 81.6 ± 1.3     | 1.07x   |
  | ascii.vt        | 0          | 9.7 ± 0.1   | 9.7 ± 0.1      | 1.01x   |
  | styled-plain.vt | 0          | 12.4 ± 0.1  | 12.3 ± 0.1     | 1.01x   |
  | osc.vt          | 0          | 157.8 ± 1.3 | 157.5 ± 0.3    | 1.00x   |
  | links.vt        | 10KB       | 38.2 ± 0.5  | 37.7 ± 0.4     | 1.01x   |
  | styled-heavy.vt | 10KB       | 29.8 ± 0.4  | 29.6 ± 0.2     | 1.01x   |
  | styled-mixed.vt | 10KB       | 64.2 ± 0.2  | 64.0 ± 0.2     | 1.00x   |
  | out.txt (2.6GB) | 0          | 4949 ± 7    | 4918 ± 6       | 1.01x   |
  | out.txt (2.6GB) | 50MB       | 5135 ± 7    | 5070 ± 7       | 1.01x   |
  
  Real programs hit this too. I recorded about 25 seconds of each of 17
  programs in a pty and replayed them through `ghostty-bench
  +terminal-stream` at 160x48 with the app's 50MB scrollback. These three
  measurably rehash on main (instructions retired for the whole replay,
  including startup):
  
  | Workload                       | Rehashes (main) | Page copies | Instructions |
  | ------------------------------ | --------------- | ----------- | ------------ |
  | `rg --hyperlink-format` + less | 6               | 12 -> 6     | -14.2%       |
  | chafa playing an animated GIF  | 148             | 150 -> 2    | -10.9%       |
  | `eza --hyperlink -R` + less    | 2               | 8 -> 6      | -3.6%        |
  ```
- [`636c1d7`](https://github.com/ghostty-org/ghostty/commit/636c1d780568db5c5fe299b7105fcf6b4c74c068) terminal: RefCountedSet only reaps dead items it may displace ([@mitchellh](https://github.com/mitchellh))
  ```text
  Only reap a dead item whose PSL is at most the held item's. The bucket
  then never ends up with a shorter PSL than it had, so every probe
  sequence through it stays intact. Otherwise the dead item is probed
  past like any other.
  ```
- [`738d8f7`](https://github.com/ghostty-org/ghostty/commit/738d8f7f5b574b2348e0ba635a0f00a0d51c35fe) terminal: RefCountedSet checks table membership, not a sentinel bucket ([@mitchellh](https://github.com/mitchellh))
- [`38f4a71`](https://github.com/ghostty-org/ghostty/commit/38f4a710e3e6a218342915bf9d29eab10281a702) terminal: RefCountedSet.releaseMultiple asserts n > 0 ([@mitchellh](https://github.com/mitchellh))
- [`31a5299`](https://github.com/ghostty-org/ghostty/commit/31a52992f12710f0382661a481fce46a966a7ea1) terminal: RefCountedSet reclaims the dead ID insert passed over ([@mitchellh](https://github.com/mitchellh))
  ```text
  When `add` reclaims a dead ID, `insert` may still reuse a smaller dead
  ID that it reaps on its probe path. The reclaimed ID then stays dead
  and out of the table, but `free_cursor` had already moved past it, so
  the next reclaims scanned the rest of the set first and only found it
  again after wrapping around.
  
  Point `free_cursor` back at it in that case so it is the next ID
  reclaimed. Harmless before, since it was found eventually, but it is
  the cheapest dead ID to reuse.
  ```
- [`aef8b7b`](https://github.com/ghostty-org/ghostty/commit/aef8b7b38d281784108f1ab1f03d6ecb9c5246d3) terminal: tighten the RefCountedSet dead ID reuse tests ([@mitchellh](https://github.com/mitchellh))
- [`5d3f653`](https://github.com/ghostty-org/ghostty/commit/5d3f653329fc62f04625f1952d88282d93df8b29) terminal: update RefCountedSet docs for dead ID reuse ([@mitchellh](https://github.com/mitchellh))
- [`4d6fb32`](https://github.com/ghostty-org/ghostty/commit/4d6fb32631d20fbd2203be0fdd5ba8109a00519b) libghostty-vt: deploy docs from GHA, move to Vercel, prep release site ([@mitchellh](https://github.com/mitchellh))
  ```text
  This sets up automation so that our libghostty-vt docs go out
  automatically and support a separate tip vs release site.  The build
  happens in GHA so we can remove the Docker builder.
  
  This also moves to Vercel, which we already used for our main web
  domain, so all our web stuff is centralized in one place. I should note
  a bias here because I am a board member of Vercel but that wasn't the
  driving reason and Ghostty has been using Vercel since years before that.
  ```
- [`8b3b025`](https://github.com/ghostty-org/ghostty/commit/8b3b025bdbbeac42fe066d2235af5ae5e6744e44) libghostty-vt: deploy docs from GHA, move to Vercel, prep release site ([#15123](https://github.com/ghostty-org/ghostty/issues/15123)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This sets up automation so that our libghostty-vt docs go out
  automatically and support a separate tip vs release site. The build
  happens in GHA so we can remove the Docker builder.
  
  This also moves to Vercel, which we already used for our main web
  domain, so all our web stuff is centralized in one place. I should note
  a bias here because I am a board member of Vercel but that wasn't the
  driving reason and Ghostty has been using Vercel since years before
  that.
  
  **AI usage:** Opus wrote all the release automation, I reviewed it and
  wrote the commit/PR/etc.
  ```
- [`b5d9c93`](https://github.com/ghostty-org/ghostty/commit/b5d9c93da1b045593a88c846ac8fed0f3835f2f3) terminal: RefCountedSet reuses dead IDs instead of rehashing ([#15121](https://github.com/ghostty-org/ghostty/issues/15121)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Once every ID in a `RefCountedSet` has been handed out, `add` now reuses
  the ID of a dead item in place.
  
  Previously it returned `NeedsRehash`, and every caller responded by
  cloning the entire page at the same capacity, copying every row, cell,
  style, grapheme and string just to free up IDs. This caused quite a lot
  of allocation and throughput churn.
  
  This has a huge impact on alt-screen apps (TUIs) in particular, because
  they don't generally ever allocate new pages and have a fixed size and
  usage pattern (usually) and constantly overwrite styles, links, etc. You
  can see below how this plays out with benchmarks.
  
  `ghostty-bench +terminal-stream` at 120x80, 8 MiB inputs:
  
  | Input | Scrollback | main (ms) | set-reuse (ms) | Speedup |
  | --------------- | ---------- | ----------- | -------------- | -------
  |
  | links.vt | 0 | 90.2 ± 0.7 | 67.3 ± 0.6 | 1.34x |
  | styled-heavy.vt | 0 | 50.7 ± 0.4 | 44.5 ± 0.3 | 1.14x |
  | styled-mixed.vt | 0 | 90.4 ± 1.2 | 83.6 ± 0.3 | 1.08x |
  | ascii.vt | 0 | 10.2 ± 0.1 | 10.2 ± 0.2 | 1.00x |
  | styled-plain.vt | 0 | 13.2 ± 0.3 | 12.9 ± 0.1 | 1.02x |
  | osc.vt | 0 | 161.6 ± 2.0 | 163.3 ± 4.6 | 0.99x |
  | links.vt | 10KB | 39.8 ± 1.1 | 39.5 ± 0.4 | 1.01x |
  | styled-heavy.vt | 10KB | 30.9 ± 0.7 | 30.5 ± 0.2 | 1.01x |
  | styled-mixed.vt | 10KB | 66.5 ± 0.5 | 66.3 ± 0.5 | 1.00x |
  
  I also wanted to know whether real programs hit this, so I recorded
  about 25 seconds of them:
  
  | Workload | Rehashes (main) | Page copies | Instructions |
  | ------------------------------ | --------------- | ----------- |
  ------------ |
  | `rg --hyperlink-format` + less | 6 | 12 -> 6 | -14.2% |
  | chafa playing an animated GIF | 148 | 150 -> 2 | -8.4% |
  | `eza --hyperlink -R` + less | 2 | 8 -> 6 | -3.1% |
  
  And then there are a bunch I tested that didn't move much (but all moved
  towards faster): nvim, helix, btop, htop, tmux.
  
  `NeedsRehash` can now only happen if the living count is wrong. Safe
  builds assert there, and release builds still fall back to the clone. In
  a future PR we can probably remove this entirely.
  
  **AI usage:** I did all the RCS changes, I had Fable adversarially
  review which did pull up a few issues that I verified, I had Opus
  implement the benchmark changes and run them. I wrote this message of
  course.
  ```
- [`3c3a887`](https://github.com/ghostty-org/ghostty/commit/3c3a8873ef0ea7843f1712a40b37c671f565f2a9) doxygen: fix the configuration and keep the build free of warnings ([@mitchellh](https://github.com/mitchellh))
- [`56919d3`](https://github.com/ghostty-org/ghostty/commit/56919d3ffd0981d52110b8d036dc3743b23ef6bb) doxygen: register every C example and rename c-vt to c-vt-osc ([@mitchellh](https://github.com/mitchellh))
- [`f21f400`](https://github.com/ghostty-org/ghostty/commit/f21f40018791bd30fe0ecfc7d104dd556226faf7) doxygen: nest the API reference and describe every topic ([@mitchellh](https://github.com/mitchellh))
- [`5acbc10`](https://github.com/ghostty-org/ghostty/commit/5acbc10ebf84ccb7a9b2d7daf1784f2b3262d74d) doxygen: move the API conventions out of the main page ([@mitchellh](https://github.com/mitchellh))
- [`6f41fba`](https://github.com/ghostty-org/ghostty/commit/6f41fbaad44e8356abfef9881d10ef0d820ecd7d) doxygen: write the Examples page and fix example names and READMEs ([@mitchellh](https://github.com/mitchellh))
- [`3a73ef5`](https://github.com/ghostty-org/ghostty/commit/3a73ef54201efa01760013c8bc6ece70075dfed7) doxygen: move the terminal guides out of the reference pages ([@mitchellh](https://github.com/mitchellh))
- [`2bc37a0`](https://github.com/ghostty-org/ghostty/commit/2bc37a0eea6a2e5da08367e62e0f2b2a2e385938) doxygen: write the main page and Getting Started ([@mitchellh](https://github.com/mitchellh))
- [`7341454`](https://github.com/ghostty-org/ghostty/commit/7341454308f2b8a564a7540ffa6de2d7cd0d6c85) doxygen: move the rendering and image guides out of the reference pages ([@mitchellh](https://github.com/mitchellh))
- [`51bff35`](https://github.com/ghostty-org/ghostty/commit/51bff35a73097f105078f9566604c265b773ee1c) doxygen: move the input, grid, selection, search and snapshot guides out of the reference pages ([@mitchellh](https://github.com/mitchellh))
- [`9a0cb21`](https://github.com/ghostty-org/ghostty/commit/9a0cb21428205711aa4982089109e919704b1aee) doxygen: give every topic page the same short intro ([@mitchellh](https://github.com/mitchellh))
- [`ba66391`](https://github.com/ghostty-org/ghostty/commit/ba66391955118c3bddee80bccb08348f0fe149d9) doxygen: wrap the markdown pages at 80 columns ([@mitchellh](https://github.com/mitchellh))
- [`d2ce23a`](https://github.com/ghostty-org/ghostty/commit/d2ce23a87c9521931851219885e1ac3ab5733fa5) doxgyen: update some docs ([@mitchellh](https://github.com/mitchellh))
- [`2f8d9e1`](https://github.com/ghostty-org/ghostty/commit/2f8d9e1f99b18c80bfebbeb1e44ca647db46dec0) doxygen: update concepts ([@mitchellh](https://github.com/mitchellh))
- [`477bfd2`](https://github.com/ghostty-org/ghostty/commit/477bfd2941c73b8eef96395ee898b0c21f069f18) libghostty-vt: rewritten Doxygen docs ([#15120](https://github.com/ghostty-org/ghostty/issues/15120)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a full rewrite of the libghostty docs.
  
  **AI usage:** I hand-write all the english content, I used Opus to
  handle the build scripts and CI.
  ```
- [`020a0a0`](https://github.com/ghostty-org/ghostty/commit/020a0a0998e084d457cf3d1604fb62de4647525f) terminal: find style runs with one scan in RowBuilder.scan ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `RowBuilder.scan` previously handled each kind of special cell separately,
  each with its own run scan. Rows with frequent style changes paid for failed
  group comparisons of plain cells and styled runs every one or two cells.
  
  Use `Mask.eqlEnd` to find both plain and styled runs. It checks the next
  cell individually before comparing whole groups. Rows with graphemes
  get a separate scan specialization, while the common version is inlined.
  
  Background color cells no longer produce style runs: their color is
  stored in the cell, and `RenderState.Cell.style` is undefined for cells
  with the default style ID. This also removes the need for `Mask.eqlExact`.
  
  `Mask.eql` now ORs the differences together and checks the masked bits
  once to avoid emulated 64-bit lane comparisons on baseline x86-64.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input         | Size   | Mode          | main (ms)     | This PR (ms) | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------------ | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 1314.9 ± 48.0 | 434.9 ± 23.6 | 3.02x   |
  | DOOM-fire-zig | 160x50 | render        | 1622.0 ± 44.2 | 743.4 ± 18.9 | 2.18x   |
  | dense_cells   | 160x50 | render-locked | 1593.7 ± 13.5 | 467.8 ± 7.5  | 3.41x   |
  | dense_cells   | 160x50 | render        | 1969.7 ± 27.4 | 858.4 ± 15.1 | 2.29x   |
  | styled-heavy  | 120x80 | render        | 245.5 ± 5.6   | 211.1 ± 4.5  | 1.16x   |
  | styled-heavy  | 120x80 | render-scroll | 361.4 ± 8.9   | 333.6 ± 9.7  | 1.08x   |
  ```
- [`d1ce0c4`](https://github.com/ghostty-org/ghostty/commit/d1ce0c46573472d6f961d8b04a03868640c4af93) terminal: fix performance regression, apply some fixes ([@mitchellh](https://github.com/mitchellh))
- [`171a4e0`](https://github.com/ghostty-org/ghostty/commit/171a4e0444959e1938084b5db803dd83c16591b6) terminal: find style runs with one scan in RowBuilder.scan ([#15111](https://github.com/ghostty-org/ghostty/issues/15111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `RowBuilder.scan` previously handled each kind of special cell
  separately, each with its own run scan. Rows with frequent style changes
  paid for failed group comparisons of plain cells and styled runs every
  one or two cells.
  
  This finds each run with a new `Mask.eqlEnd`, which returns the index
  where the run ends and checks the next cell on its own before checking
  groups. Rows with graphemes get a separate scan specialization, while
  the common version is inlined.
  
  Background color cells no longer produce style runs: their color is
  stored in the cell, and `RenderState.Cell.style` is already undefined
  for them. This also removes the only use of `Mask.eqlExact`.
  
  `Mask.eql` now ORs the differences and checks the masked bits once,
  which avoids emulated 64-bit lane comparisons on baseline x86-64.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input | Size | Mode | main (ms) | This PR (ms) | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------------
  | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 1314.9 ± 48.0 | 434.9 ± 23.6
  | 3.02x |
  | DOOM-fire-zig | 160x50 | render | 1622.0 ± 44.2 | 743.4 ± 18.9 | 2.18x
  |
  | dense_cells | 160x50 | render-locked | 1593.7 ± 13.5 | 467.8 ± 7.5 |
  3.41x |
  | dense_cells | 160x50 | render | 1969.7 ± 27.4 | 858.4 ± 15.1 | 2.29x |
  | styled-heavy | 120x80 | render | 245.5 ± 5.6 | 211.1 ± 4.5 | 1.16x |
  | styled-heavy | 120x80 | render-scroll | 361.4 ± 8.9 | 333.6 ± 9.7 |
  1.08x |
  | medium_cells | 139x68 | render-locked | 142.2 ± 4.8 | 132.6 ± 4.4 |
  1.07x |
  | medium_cells | 139x68 | render | 149.7 ± 5.5 | 139.3 ± 3.6 | 1.07x |
  | styled-light | 120x80 | render-locked | 149.5 ± 3.8 | 140.3 ± 3.5 |
  1.07x |
  | styled-light | 120x80 | render | 158.8 ± 5.5 | 148.0 ± 4.7 | 1.07x |
  
  AI disclosure: Developed with Claude Code (Opus 5.5) and OpenCode (GPT
  6.1 Sol), including benchmarking and codegen experiments.
  ```
- [`4441aab`](https://github.com/ghostty-org/ghostty/commit/4441aabcafd673314b0667177905726680d9f8ba) terminal/kitty: evict the oldest image by transmission ([@fornwall](https://github.com/fornwall))
  ```text
  Eviction ranked images by generation, which changes whenever an
  animation shows another frame, so a playing animation outlived images
  transmitted after it. Images advanced in the same tick were also ordered
  by hash map iteration. Rank by the transmission stamp instead.
  ```
- [`de202be`](https://github.com/ghostty-org/ghostty/commit/de202be94a418b56136d8075eb4b768672ad9f18) terminal: keep triple-click selection over blank lines ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Dragging a triple-click selection over a blank row clears the
  selection until the pointer reaches another row with content.
  
  Fall back to the untrimmed line at the drag point, matching the
  existing behavior at the click point.
  ```
- [`1fa19fa`](https://github.com/ghostty-org/ghostty/commit/1fa19fa3e9f73e49bd231de4995a1ecfecda7afd) terminal/kitty: evict the oldest image by transmission ([#15103](https://github.com/ghostty-org/ghostty/issues/15103)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  The [Kitty graphics
  protocol](https://sw.kovidgoyal.net/kitty/graphics-protocol/) has a
  [storage
  quota](https://sw.kovidgoyal.net/kitty/graphics-protocol/#image-persistence-and-storage-quotas):
  older images are evicted to make space for newer images.
  
  Image eviction treated an
  [animation](https://sw.kovidgoyal.net/kitty/graphics-protocol/#animation)
  as new again each time it showed another frame, so a playing animation
  outlived images transmitted after it.
  
  #15094 fixed the same problem for image numbers - this PR fixes it for
  eviction.
  
  To reproduce, start with `ghostty --image-storage-limit=12` and run the
  below script:
  
  ```sh
  # Start a green animation:
  printf '\e_Ga=T,q=2,i=1,f=24,s=1,v=1,c=8,r=4;/wAA\e\\'
  printf '\e_Ga=f,q=2,i=1,f=24,s=1,v=1,z=100;AP8A\e\\'
  printf '\e_Ga=a,q=2,i=1,s=3\e\\'
  # Show a blue image:
  printf '\e_Ga=T,q=2,i=2,f=24,s=1,v=1,c=8,r=4;AAD/\e\\'
  # Let the animation advance:
  sleep 1
  # Show a yellow image, going over the quota:
  printf '\e_Ga=T,q=2,i=3,f=24,s=1,v=1,c=8,r=4;//8A\e\\'
  ```
  
  - Before this PR: the newer blue image disappears, leaving the older
  green animation.
  - After this PR: the older green animation disappears, as in Kitty
  (checked using larger images to hit kitty fixed quota).
  
  AI disclosure: Initially created using Opus 5.5 through Claude Code.
  ````
- [`53e5514`](https://github.com/ghostty-org/ghostty/commit/53e55147bbbb0157672dac0228aa7744e881f1fa) terminal: keep triple-click selection over blank lines ([#15113](https://github.com/ghostty-org/ghostty/issues/15113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Dragging a triple-click selection over a blank row currently clears the
  selection until the pointer reaches another row with content.
  
  This falls back to selecting the untrimmed line when the drag point is
  on a blank row, matching the existing behavior at the click point.
  
  To reproduce, run `printf 'alpha beta\n\nthree four\n'`, triple-click
  `alpha`, and drag down over the blank line. The selection should extend
  through it instead of disappearing.
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`9b4a007`](https://github.com/ghostty-org/ghostty/commit/9b4a0076d246cdb36d589be7dd3f14a6079e7d7f) cli: explicitly install terminfo to ~/.terminfo on ssh remote host ([@database64128](https://github.com/database64128))
  ```text
  By default tic installs terminfo into /usr/share/terminfo, which can
  cause file conflicts with the system package manager.
  
  To fix that, explicitly specify the output directory we just created
  to avoid modifying /usr/share/terminfo/.
  
  For #15031
  ```
- [`6283611`](https://github.com/ghostty-org/ghostty/commit/6283611ddf8d6d4a55c323b897428bd83b6ad5cc) cli: verify xterm-ghostty resolves after ssh install ([@jparise](https://github.com/jparise))
  ```text
  Installing to ~/.terminfo doesn't guarantee the entry is usable. ncurses
  skips $HOME/.terminfo for root when built with --disable-root-environ,
  as Arch's package is. Previously, tic installed into the system terminfo
  directory as root, so that case worked by overwriting package-owned
  files. With an explicit output directory, the install would succeed but
  xterm-ghostty wouldn't resolve, and the host would be cached as set up.
  
  Check the entry with infocmp after installing. If it doesn't resolve,
  the install fails and the session falls back to xterm-256color without
  caching the host.
  
  Also drop the mkdir. tic creates its output directory itself.
  
  See #15031, #15061
  ```
- [`2c76f29`](https://github.com/ghostty-org/ghostty/commit/2c76f29972dad21d3f2cc0efde2517a6fa8fed56) cli: explicitly install terminfo to ~/.terminfo on ssh remote host ([#15061](https://github.com/ghostty-org/ghostty/issues/15061)) ([@jparise](https://github.com/jparise))
  ```text
  By default `tic` installs terminfo into `/usr/share/terminfo`, which can
  cause file conflicts with the system package manager.
  
  To fix that, explicitly specify the output directory we just created to
  avoid modifying `/usr/share/terminfo/`.
  
  For #15031
  ```
- [`16f5674`](https://github.com/ghostty-org/ghostty/commit/16f5674dc3eaeee9575d2b729255f2fe0993ece3) Update VOUCHED list ([#15107](https://github.com/ghostty-org/ghostty/issues/15107)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15007#discussioncomment-19437535)
  from @bo2themax.
  
  Vouch: @jin-eden
  ```
- [`db663e0`](https://github.com/ghostty-org/ghostty/commit/db663e0755ef2efcc8dd4ba5c8b7f3f25b5914b0) Update VOUCHED list ([#15106](https://github.com/ghostty-org/ghostty/issues/15106)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15064#discussioncomment-19437280)
  from @bo2themax.
  
  Vouch: @sm010422
  ```
- [`de4bc49`](https://github.com/ghostty-org/ghostty/commit/de4bc494a5d7bb5747bf8cc76b4a31bd033628e2) i18n: updated Latvian translations ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Translations for the command palette's Focus and Untitled labels, new appearance commands and descriptions.
  ```
- [`8a5d14b`](https://github.com/ghostty-org/ghostty/commit/8a5d14bd05f8eab80e00ff24a304092c549c9f9b) i18n: updated Latvian translations ([#15100](https://github.com/ghostty-org/ghostty/issues/15100)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translations for the command palette's Focus and Untitled labels, new
  appearance commands and descriptions.
  ```
- [`6095e27`](https://github.com/ghostty-org/ghostty/commit/6095e277a52fb98286a4660520fa189c51a87ec9) pkg: build simdutf, highway, and wuffs with hidden visibility ([@mitchellh](https://github.com/mitchellh))
  ```text
  When we build them, these are only ever statically linked into our
  binaries. We should not be exporting their symbols ever.
  ```
- [`c445f44`](https://github.com/ghostty-org/ghostty/commit/c445f448a7b0e409e71264ca10b302305a62f696) pkg: build simdutf, highway, and wuffs with hidden visibility ([#15102](https://github.com/ghostty-org/ghostty/issues/15102)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When we build them, these are only ever statically linked into our
  binaries. We should not be exporting their symbols ever.
  ```

