> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 10, 2026 at 03:59 UTC.

## October 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37960020956), [2](https://github.com/ghostty-org/ghostty/actions/runs/37902855280), [3](https://github.com/ghostty-org/ghostty/actions/runs/37884767144)  
Summary: 3 runs • 6 commits • 4 authors

### Changes

- [`7f1219f`](https://github.com/ghostty-org/ghostty/commit/7f1219fd701449fa3e5de33b9ba9ce85f008ac33) cli/list-themes: add ctrl-d/u paging ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  Ctrl-D and Ctrl-U move down and up 20 themes, like PgDn and PgUp.
  This helps keyboards without page keys and matches the less/vi-style
  keys that already exist (g/G).
  ```
- [`246f702`](https://github.com/ghostty-org/ghostty/commit/246f702876b924a1cb7cade1e99274d1470302fc) cli/list-themes: add ctrl-d/u paging ([#14607](https://github.com/ghostty-org/ghostty/issues/14607)) ([@jcollie](https://github.com/jcollie))
  ```text
  discussion #14604
  
  ## Ctrl-D and Ctrl-U paging
  
  `Ctrl-D` and `Ctrl-U` move down and up 20 themes. `PgDn` and `PgUp`
  already do this. `g` and `G` already exist (#13376), so vim-like paging
  fits. It also helps users who have no `PgUp` or `PgDn` key.
  ```
- [`9d479dc`](https://github.com/ghostty-org/ghostty/commit/9d479dcb1664e8dc3c66c7302ce596dc56b36d6d) Update VOUCHED list ([#14614](https://github.com/ghostty-org/ghostty/issues/14614)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14582#discussioncomment-18831499)
  from @pluiedev.
  
  Denounce: @Martzcode
  ```
- [`f473f31`](https://github.com/ghostty-org/ghostty/commit/f473f310979da7002f3c2793f39cfbeef475bb88) terminal: support DECSTR ([@jcollie](https://github.com/jcollie))
  ```text
  Programs and test suites use DECSTR (CSI ! p) to undo the modes, margins,
  and pen they may have left behind without clearing the screen. It was
  ignored, so that state leaked into whatever ran next.
  ```
- [`5169c47`](https://github.com/ghostty-org/ghostty/commit/5169c473aa996a9eff29307daad6a01501c5c245) terminal: documentation for DECSTR ([@korikhin](https://github.com/korikhin))
- [`b115e45`](https://github.com/ghostty-org/ghostty/commit/b115e456749e2820a14d3942a63159ff8d46d925) terminal: support DECSTR ([#14538](https://github.com/ghostty-org/ghostty/issues/14538)) ([@jcollie](https://github.com/jcollie))
  ```text
  Programs and test suites use DECSTR (CSI ! p) to undo the modes,
  margins, and pen they may have left behind without clearing the screen.
  It was ignored, so that state leaked into whatever ran next.
  ```

## October 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37856874364), [2](https://github.com/ghostty-org/ghostty/actions/runs/37844704694), [3](https://github.com/ghostty-org/ghostty/actions/runs/37805457756), [4](https://github.com/ghostty-org/ghostty/actions/runs/37794266921), [5](https://github.com/ghostty-org/ghostty/actions/runs/37790076764), [6](https://github.com/ghostty-org/ghostty/actions/runs/37789831587), [7](https://github.com/ghostty-org/ghostty/actions/runs/37742721150)  
Summary: 7 runs • 12 commits • 7 authors

### Changes

- [`54ba7b1`](https://github.com/ghostty-org/ghostty/commit/54ba7b1dd98dfaf14ee82ae7cbf435e867986da9) cli/list-themes: fix keypad page down binding ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  The move-down-by-20 binding listed kp_down instead of kp_page_down.
  Pressing keypad down matched both this binding and the move-down-by-1
  binding, so it moved 21 themes. The move-up-by-20 binding already uses
  kp_page_up.
  ```
- [`c770410`](https://github.com/ghostty-org/ghostty/commit/c770410dbb57909ff4f6921a6497688a957f85db) cli/list-themes: fix keypad page down binding ([#14605](https://github.com/ghostty-org/ghostty/issues/14605)) ([@jcollie](https://github.com/jcollie))
  ````text
  discussion #14604
  
  ## small bug fix
  
  In the "move down 20" binding, `vaxis.Key.kp_down` should be
  `vaxis.Key.kp_page_down`. A `kp_down` press matches both `if` statements
  and moves down 21 rows. I cannot test this because I use macOS and have
  no keypad.
  
  ```zig
  // move down
  if (key.matchesAny(&.{ 'j', '+', vaxis.Key.down, vaxis.Key.kp_down, vaxis.Key.kp_add }, .{}))
      self.down(1);
  if (key.matchesAny(&.{ vaxis.Key.page_down, vaxis.Key.kp_down }, .{}))
      self.down(20);
  
  // move up (no issue, it uses kp_page_up)
  if (key.matchesAny(&.{ 'k', '-', vaxis.Key.up, vaxis.Key.kp_up, vaxis.Key.kp_subtract }, .{}))
      self.up(1);
  if (key.matchesAny(&.{ vaxis.Key.page_up, vaxis.Key.kp_page_up }, .{}))
      self.up(20);
  ```
  ````
- [`55424c1`](https://github.com/ghostty-org/ghostty/commit/55424c1ccb34bff8f5534b5bc918ea859b3a9278) i18n: use "konfiguration" consistently in Danish (da) translation ([@kgni](https://github.com/kgni))
- [`e2ced6b`](https://github.com/ghostty-org/ghostty/commit/e2ced6b710427ea69dc6795bf00a787c81554452) i18n: update Danish (da) PO-Revision-Date ([@kgni](https://github.com/kgni))
- [`ce63fcb`](https://github.com/ghostty-org/ghostty/commit/ce63fcba60abb7e11e6435fae32855c20ef3c9cf) I18n/da konfiguration ([#14594](https://github.com/ghostty-org/ghostty/issues/14594)) ([@trag1c](https://github.com/trag1c))
  ````text
  ## Summary
  
  Small follow up to #14586  based on a suggestion from @Fjodor42.
  Two strings used "konfigurering" while the rest of the file uses
  "konfiguration".
  
  ```diff
   msgid "Open Configuration in OS Editor"
  -msgstr "Åbn konfigurering i styresystemets redigeringsprogram"
  +msgstr "Åbn konfiguration i styresystemets redigeringsprogram"
  
   msgid "Open Configuration in New Window"
  -msgstr "Åbn konfigurering i nyt vindue"
  +msgstr "Åbn konfiguration i nyt vindue"
  ```
  
  Also bumped `PO-Revision-Date`.
  ````
- [`23c7a3e`](https://github.com/ghostty-org/ghostty/commit/23c7a3e5a68aefee51b30a780e706771f80b5f97) formatter: write the cursor position relative to the margins in origin mode ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output from TerminalFormatter restores origin mode (DECOM) with the
  other modes and the scrolling region after the contents, then writes
  the cursor position with CUP. In origin mode CUP counts from the
  top-left of the scrolling region, but the position was written from the
  top-left of the screen, so replaying the output put the cursor that far
  down and to the right whenever a program had set margins and origin
  mode.
  
  When the output restores both origin mode and the scrolling region,
  the cursor position (and the cell reprinted to restore a pending wrap)
  is now written relative to the region's top-left. Without either, the
  replaying terminal counts from the screen's top-left, as before.
  ```
- [`7ec9e26`](https://github.com/ghostty-org/ghostty/commit/7ec9e26a29399b30ef78f06985fc75045b3cecb6) formatter: write the cursor position relative to the margins in origin mode ([#14588](https://github.com/ghostty-org/ghostty/issues/14588)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  When a program sets a scrolling region and origin mode (DECOM), the VT
  output from `TerminalFormatter` restores the cursor to the wrong place.
  The formatter restores origin mode and the scrolling region (along with
  the other modes) after the contents, then writes the cursor position
  with CUP. In origin mode, CUP counts from the top-left of the screen, so
  the replayed cursor lands too far down (and right with DECSLRM), by the
  size of the margins.
  
  ### Reproduce
  
  Format a terminal with a scrolling region on rows 5-20, with origin mode
  on and the cursor at row 7, column 7, then play the output back and
  print an `X` at the cursor. I made an agent write a small C program with
  `ghostty_formatter_terminal_new` (modes, scrolling region, and cursor
  extras on) against libghostty-vt built from `main` and from this branch:
  
  <img width="764" height="602" alt="formatter-side-by-side"
  src="https://github.com/user-attachments/assets/787943b4-3763-4bbc-8eb8-1924600063e1"
  />
  
  
  The only difference in the output is the cursor position:
  
  ```
  main:  …row 24\e[5;20r\e[7;7H\e[0m   → row 11 in origin mode
  fixed: …row 24\e[5;20r\e[3;7H\e[0m   → row 7
  ```
  
  **The Fix:** When the output restores both origin mode and the scrolling
  region, the cursor position is now rewritten relative to the region's
  top-left. Without either, the replaying terminal counts from the
  screen's top-left, as before. Setting origin mode moves the cursor home,
  so you must write the position relative to the margins after it, and no
  mode ordering avoids this.
  
  ### Performance
  
  The fix runs once per format, not per cell. I've used the benchmark I
  contributed in https://github.com/ghostty-org/ghostty/pull/14581 to run
  `ghostty-bench +terminal-formatter` with `TerminalFormatter` and every
  extra, ReleaseFast on my MacBook Pro M1 Max, median of 60 hyperfine
  runs:
  
  | **Input** | **main** | **this PR** |
  | --- | --- | --- |
  |  80×24 screen in origin mode, 100,000 formats | 1005.4 ms | 999.4 ms |
  | ghostty-gen +styled --seed=42, 640 KB, 20 formats | 47.4 ms | 47.3 ms
  |
  
  AI disclosure: Written with help from Claude Code using Opus 5.5. I
  reviewed, tested and ran the benchmarks myself.
  ````
- [`bad5854`](https://github.com/ghostty-org/ghostty/commit/bad5854f358332f3168b35c5052f41b45a2671b3) Update VOUCHED list ([#14603](https://github.com/ghostty-org/ghostty/issues/14603)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14595#issuecomment-6062284415)
  from @mitchellh.
  
  Vouch: @Huge
  ```
- [`0f171f6`](https://github.com/ghostty-org/ghostty/commit/0f171f650a1cbbd6df4a2573b6b0c7de57cc6d90) Update VOUCHED list ([#14600](https://github.com/ghostty-org/ghostty/issues/14600)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14597#issuecomment-6061673855)
  from @pluiedev.
  
  Denounce: @riskirills66
  ```
- [`7551c5b`](https://github.com/ghostty-org/ghostty/commit/7551c5bad4211ebf3cf20647f5b735f2dc14b1f6) Update VOUCHED list ([#14599](https://github.com/ghostty-org/ghostty/issues/14599)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14598#issuecomment-6061636878)
  from @trag1c.
  
  Vouch: @Rayzerrek
  ```
- [`7b60f9b`](https://github.com/ghostty-org/ghostty/commit/7b60f9bf5f057394038f81653eaa7cc5a55bb5df) i18n: improve Danish (da) translation ([@kgni](https://github.com/kgni))
- [`8f0dd37`](https://github.com/ghostty-org/ghostty/commit/8f0dd3709050b1026f6324368805033197d8b4a5) i18n: improve Danish (da) translation ([#14586](https://github.com/ghostty-org/ghostty/issues/14586)) ([@trag1c](https://github.com/trag1c))
  ````text
  Hi!
  
  I'm a native Danish speaker and went through the Danish translation. I
  hope it's okay that I open this.
  
  My background: Got 0 errors in all of my spelling tests from 4th to 6th
  grade
  
  Happy to adjust or drop anything the da_DK maintainers disagree with.
  
  I followed the Danish GNOME translations for some of these - e.g.
  "Afslut" instead of "Luk ned"
  
  ## Summary
  
  Review pass of `po/da.po` with grammar fixes and small consistency
  changes. No new strings; still `252/252` translated.
  
  ```diff
  - Åben i Ghostty / Åben et nyt vindue. / …og åben den.
  + Åbn i Ghostty / Åbn et nyt vindue. / …og åbn den.        (imperative of "åbne", ~20 strings)
  - Kopiér det valgte tekst …
  + Kopiér den valgte tekst …                                 ("tekst" is common gender)
  - Slå sikker input til/fra
  + Slå sikkert input til/fra                                 ("input" is neuter / intetkøn)
  - Hvis ingen terminaltitel er angivet, vil dette have ingen effekt.
  + Hvis ingen terminaltitel er angivet, har dette ingen effekt.
  - Luk ned / Luk ned for Ghostty?
  + Afslut / Afslut Ghostty?                                  (matches GNOME)
  - Eksekver en kommando… / …vil blive eksekveret.
  + Kør en kommando… / …vil blive kørt.
  - Venligst gennemse fejlene nedenfor, og derefter enten genindlæs …
  + Gennemgå fejlene nedenfor, og genindlæs derefter …
  - Tjek efter opdateringer
  + Søg efter opdateringer
  - Dialog for at skifte titlen på den nuværende terminal.
  + Angiv en ny titel for den nuværende terminal.
  - Kopiér valg som HTML …
  + Kopiér markering som HTML …                               (matches "markering" elsewhere)
  ```
  
  Smaller consistency fixes:
  - `Dette medfører en nedsat ydeevne.` → `Ydeevnen vil være nedsat.`
  - `Slå vis altid øverst til/fra` → `Slå 'altid øverst' til/fra`
  - "Kopiér skærm/markering … til midlertidig fil" titles now use the same
  wording
  - Comma before "og" in all temp-file descriptions
  
  I used Claude Code to help review the initial translation; I went
  through and chose every change myself.
  ````

## October 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37630750011), [2](https://github.com/ghostty-org/ghostty/actions/runs/37569761740), [3](https://github.com/ghostty-org/ghostty/actions/runs/37551559977)  
Summary: 3 runs • 4 commits • 3 authors

### Changes

- [`a60e9e2`](https://github.com/ghostty-org/ghostty/commit/a60e9e2a57f73e1eef2bd1cf2995a467f69e7fb0) Update VOUCHED list ([#14585](https://github.com/ghostty-org/ghostty/issues/14585)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14584#discussioncomment-18795569)
  from @jcollie.
  
  Vouch: @kgni
  ```
- [`c706451`](https://github.com/ghostty-org/ghostty/commit/c706451fe8bf1a55750c3262ed323df99d717a24) terminal: apply a single shift to exactly one printed character ([@robmorgan](https://github.com/robmorgan))
  ```text
  A single shift (SS2/SS3) applies to the next character received. Only
  printCell used it up, so a combining mark or VS16, which attaches to
  the previous cell without going through printCell, left the shift in
  place for the character after it.
  
  DEC STD 070 (3.8.3.2) says that if the character after a single shift
  is not a graphic character in its range, the shift is ignored and the
  character is processed as if the shift had not been received. ISO 2022
  (8.4) likewise applies it to the immediately following character
  only. print now takes the charset, and clears the single shift, once
  for each codepoint, so a combining mark or VS16 cancels the shift and
  prints unmapped. xterm does the same (WriteNow in charproc.c).
  
  printCell maps its character with that charset and writes it with the
  new writeCell, which writes a cell as it is. Spacers and blanks use
  writeCell, and so does the grapheme path that moves a character VS16
  widened to the next row. That path printed the stored, already mapped
  character through the charset again, so a '#' became a '£' if the
  British set was selected in between.
  ```
- [`b699ea7`](https://github.com/ghostty-org/ghostty/commit/b699ea79f4b881421b4b3055abc16a0957d76beb) terminal: apply a single shift to exactly one printed character ([#14576](https://github.com/ghostty-org/ghostty/issues/14576)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With a single shift (SS2/SS3) pending, a combining mark or VS16 did not
  use it up because only `printCell` cleared the shift and those
  characters attach to the previous cell without going through it. The
  shift then applied to the next character instead. So in `x` + SS2 + VS16
  + `#` with the British set in G2, the `#` became a `£`.
  
  ### Reproduce
  
  Run these in a current build:
  ```sh
  printf 'x\e*0\eN\u0301a\e*B\n'              # combining mark: prints x́▒, should be x́a
  printf 'x\e*A\eN\uFE0F#\e*B\n'              # VS16: prints x£, should be x#
  printf '\e[%dG#\e(A\uFE0F\e(B\n' $COLUMNS   # expect a wide # at the start of the next line
  ```
  
  **Old**
  <img width="656" height="297" alt="image"
  src="https://github.com/user-attachments/assets/7a20c734-71fd-422f-8394-106e6234d538"
  />
  
  **Fixed**
  <img width="434" height="295" alt="image"
  src="https://github.com/user-attachments/assets/1401e986-3fde-479c-aa5c-e7546861ed97"
  />
  
  DEC STD 070 (3.8.3.2) says that if the character after a single shift is
  not a graphic character in its range, the shift is ignored and the
  character is processed as if the shift had not been received. ISO 2022
  (8.4) likewise applies it to the immediately following character only.
  `print` now takes the charset, and clears the single shift, once for
  each codepoint, so a combining mark or VS16 cancels the shift and prints
  unmapped. xterm does the same (WriteNow in `charproc.c`).
  
  `printCell` maps its character with that charset and writes it with the
  new `writeCell`, which writes a cell as it is. Spacers and blanks use
  `writeCell`, and so does the grapheme path that moves a character VS16
  widened to the next row. That path printed the stored, already mapped
  character through the charset again, so a '#' became a '£' if the
  British set was selected in between (e.g: before VS16).
  
  ### Performance
  I ran `ghostty-bench +terminal-stream` with hyperfine against `main`
  (ReleaseFast, M1 Max, the same 100 MB inputs for both). ASCII, styled
  and DEC line-drawing input show no change, since they go through
  `printSlice` and never reach this code. Random UTF-8, which falls back
  to `print` for most codepoints, is about 1% slower, within this
  machine's run-to-run noise.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`34f3900`](https://github.com/ghostty-org/ghostty/commit/34f39002c6e3974b54e6a6d400bd83777c5ea558) Update VOUCHED list ([#14573](https://github.com/ghostty-org/ghostty/issues/14573)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14323#discussioncomment-18786373)
  from @jcollie.
  
  Vouch: @ekusiadadus
  ```

## October 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37542529824), [2](https://github.com/ghostty-org/ghostty/actions/runs/37515317220), [3](https://github.com/ghostty-org/ghostty/actions/runs/37510349661), [4](https://github.com/ghostty-org/ghostty/actions/runs/37392894640)  
Summary: 4 runs • 8 commits • 4 authors

### Changes

- [`bae2c3c`](https://github.com/ghostty-org/ghostty/commit/bae2c3cdbf73f2ac33a67e4b0b7811165f0f62d4) libghostty-vt: program status protocol (OSC 7501) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for OSC 7501, the program status protocol. A program
  uses it to tell the terminal what it is doing (idle, working, done,
  blocked on the user, or failed) and why.
  
  The terminal doesn't keep records itself, the same as OSC 9;4. The
  embedder keeps one record per id and applies the spec's lifetime rules.
  A full reset reports a clear of every record. The terminal only answers
  the support query (`OSC 7501 ; ?`) while the effect is set, so programs
  don't send reports that nothing reads. The Ghostty app ignores these
  reports for now.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
    https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`a4aacd9`](https://github.com/ghostty-org/ghostty/commit/a4aacd918ba9e79929ff608034c60a4341773ef0) libghostty-vt: program status protocol (OSC 7501) ([#14560](https://github.com/ghostty-org/ghostty/issues/14560)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for OSC 7501, the program status protocol. A program
  uses it to tell the terminal what it is doing (idle, working, done,
  blocked on the user, or failed) and why.
  
  OSC7501 is the first net-new terminal specification to be pioneered by
  the Ghostty project. In full transparency, this work was motivated by my
  work on Superlogical, but the specification was carefully written in a
  way that doesn't bias towards that use case. The specification is
  broadly useful across a wide variety of applications. I also distributed
  the specification with a diverse group of application and terminal
  developers to solicit feedback.
  
  The terminal doesn't keep records itself, the same as OSC 9;4. The
  embedder keeps one record per id and applies the spec's lifetime rules.
  A full reset reports a clear of every record. The terminal only answers
  the support query (`OSC 7501 ; ?`) while the effect is set, so programs
  don't send reports that nothing reads. The Ghostty app ignores these
  reports for now.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
  https://gist.github.com/mitchellh/7acae3abd8355c1c00287d67e96c913a
  ```
- [`13b5ab2`](https://github.com/ghostty-org/ghostty/commit/13b5ab2041fe866e9b448697cd8485b115c32ba2) terminal: stop line selection at prompt boundaries across blank cells ([@fornwall](https://github.com/fornwall))
  ```text
  Selecting a span of blank cells or whitespace between OSC 133 semantic
  boundaries could pull in neighboring prompt text and reverse the
  selection endpoints.
  
  The whitespace trims iterate with a `CellIterator` bounded by the end
  pin, but the iterator bounds only the row, so the trim ran past the end
  column into the next prompt.
  ```
- [`6220a36`](https://github.com/ghostty-org/ghostty/commit/6220a36172ec4558b308b317ac9a7b1e0960cb50) terminal: print codepoints above 0xFF unmapped in a charset, as xterm ([@robmorgan](https://github.com/robmorgan))
  ```text
  With a charset other than UTF-8 or ASCII designated (the DEC
  line-drawing set, say), printCell mapped every codepoint above 0xFF to
  a space. An emoji printed in that state became a blank, and since its
  width still came from the original codepoint, a two-column one, so the
  rest of the row shifted too.
  
  A designated set only applies to the range it is invoked into: G0 is
  invoked into GL (0x21-0x7E), so codepoints outside it pass through
  unchanged (DEC STD 070, following ISO 2022; xterm does the same). The
  charset tables already only remap codepoints in GL, so printCell now
  prints anything above 0xFF as is instead of replacing it with a space.
  ```
- [`4611e04`](https://github.com/ghostty-org/ghostty/commit/4611e04ff63c50f71b3e951c4015cfae416cb40d) terminal: print codepoints above 0xFF unmapped in a charset, as xterm ([#14554](https://github.com/ghostty-org/ghostty/issues/14554)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With a charset other than UTF-8 or ASCII designated (e.g. the DEC
  line-drawing set), `printCell` mapped every codepoint above `0xFF` to a
  space. An emoji printed in that state became a blank, and since its
  width still came from the original codepoint (a two-column one), so the
  rest of the row shifted too.
  
  A designated set only applies to the range it is invoked into: G0 is
  invoked into GL (`0x21`–`0x7E`), so codepoints outside it should pass
  through unchanged (DEC STD 070, following ISO 2022 - I checked and xterm
  behaves the same way). Ghostty's charset tables already only remap
  codepoints in GL, so `printCell` now prints anything above `0xFF` as is
  instead of replacing it with a space.
  
  To reproduce, run this inside a current build:
  ```sh
  printf '\e(0`\U0001F600a\e(B\n'
  ```
  
  **Old**
  <img width="585" height="82" alt="image"
  src="https://github.com/user-attachments/assets/4df6c46f-eaf1-459a-b7c2-2e175bbca6ed"
  />
  
  **New**
  <img width="323" height="58" alt="image"
  src="https://github.com/user-attachments/assets/d618502b-e44f-4243-b4b4-8c76e079b88d"
  />
  
  AI disclosure: Created with help from Claude Code using Opus 5.5.
  Iterated on, manually tested, and reviewed by me.
  ````
- [`ca2356f`](https://github.com/ghostty-org/ghostty/commit/ca2356fa05bedefacfc30a71d93ee899aaedb998) terminal: stop line selection at prompt boundaries across blank cells ([#14553](https://github.com/ghostty-org/ghostty/issues/14553)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Selecting a span of blank cells or whitespace between [OSC 133 semantic
  boundaries](https://gitlab.freedesktop.org/Per_Bothner/specifications/-/blob/master/proposals/semantic-prompts.md)
  could pull in neighboring prompt text and reverse the selection
  endpoints. The whitespace trims iterate with a `CellIterator` bounded by
  the end pin, but the iterator bounds only the row, so the trim ran past
  the end column into the next prompt.
  
  To reproduce: Run this script and triple-click either blank cell between
  `x` and `m` on the first row. Before the fix, the selection reaches into
  the neighboring prompt text; after the fix, nothing is selected (like
  triple-clicking a blank row).
  
  ```sh
  #!/bin/sh
  # On exit:
  # \033]133;C\007  Switch back to command-output mode (OSC 133;C).
  # \033[?1049l     Leave the alternate screen and restore the original screen.
  trap 'printf "\033]133;C\007\033[?1049l"' 0
  
  # \033[?1049h     Enter the alternate screen, preserving the original screen.
  # \033]133;C\007  Mark subsequent text as command output (OSC 133;C).
  # \033[2J        Clear the visible screen, leaving unwritten output cells.
  # \033[H         Move the cursor to the top-left corner.
  printf '\033[?1049h\033]133;C\007\033[2J\033[H'
  
  # \033]133;A\007  Mark the start of a prompt (OSC 133;A).
  # x              Print a prompt cell in column 1.
  # \033[2C        Move right two columns, leaving two unwritten output cells.
  # m              Print another prompt cell in column 4.
  # \033]133;C\007  Switch back to command-output mode (OSC 133;C).
  printf '\033]133;A\007x\033[2Cm\033]133;C\007'
  
  # Wait for Enter while you test selection; the exit trap restores the screen.
  read -r _
  ```
  
  AI disclosure: Initially created with the help of gpt-6 astra in codex.
  Iterated on, reviewed and tested by me.
  ````
- [`2febd01`](https://github.com/ghostty-org/ghostty/commit/2febd0116dab28df8beb00e4a3453022fe8f3c16) Update VOUCHED list ([#14566](https://github.com/ghostty-org/ghostty/issues/14566)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14563#discussioncomment-18782495)
  from @jcollie.
  
  Vouch: @magnussp
  ```
- [`c3203ea`](https://github.com/ghostty-org/ghostty/commit/c3203ea4b169a18eb2ccfe92847e426d8afea858) Update VOUCHED list ([#14550](https://github.com/ghostty-org/ghostty/issues/14550)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14549#discussioncomment-18767762)
  from @jcollie.
  
  Vouch: @robmorgan
  ```

## October 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37273745638), [2](https://github.com/ghostty-org/ghostty/actions/runs/37265526133)  
Summary: 2 runs • 4 commits • 4 authors

### Changes

- [`140feb8`](https://github.com/ghostty-org/ghostty/commit/140feb86ae4594472607859b75167889de0c13da) renderer: always release shaders when the render thread exits (Anonymous)
  ```text
  Since #14052, shaders are only freed by releaseGpuResources while the
  display is unrealized, and only the GTK apprt unrealizes. The macOS
  apprt never does, so each closed surface leaked its five render
  pipelines and shader library.
  
  threadExit now marks the display unrealized before releasing GPU
  resources. This frees the shaders and stops any later draw from
  rebuilding resources after the render thread is gone.
  ```
- [`35a81a9`](https://github.com/ghostty-org/ghostty/commit/35a81a980bb9fce09a1ea762a68b55f8eb3477ed) renderer: always release shaders  ([#14542](https://github.com/ghostty-org/ghostty/issues/14542)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  shaders are only fread by releaseGpuResources while the display is
  unrealized and only the gtk apprt unrealizes. The mac apprt never does
  automatically so each closed surface leaked its five render pipelines
  and shader library. Updated so threadExit now marks the display
  unrealized before releasing GPU resources.
  ```
- [`157c44f`](https://github.com/ghostty-org/ghostty/commit/157c44f643c9209e31bb92f4c2c4bcec9c6d23d5) input: UTF-8 encode the button in 1005 mouse reports ([@fornwall](https://github.com/fornwall))
  ```text
  In UTF-8 mouse mode (DECSET 1005) the button value was written as a
  single raw byte. xterm encodes it as UTF-8 like the coordinates, so
  values from 128 (buttons 8 and 9) take two bytes. The raw byte made
  the report invalid UTF-8.
  ```
- [`b094a6b`](https://github.com/ghostty-org/ghostty/commit/b094a6ba31825aec1b2beaae54686b4a31f98a8a) input: UTF-8 encode the button in 1005 mouse reports ([#14532](https://github.com/ghostty-org/ghostty/issues/14532)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix UTF-8 mouse reporting (DECSET 1005) to UTF-8 encode the button
  value, as required by [xterm’s
  specification](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h3-Extended-coordinates).
  
  Previously, buttons 8 and 9 (back/forward) produced a raw byte of `0xA0`
  or `0xA1`, making the report invalid UTF-8. For example, pressing button
  8 at column 1, row 1 produced:
  
  - Before: `b'\x1b[M\xa0!!'`
  - After: `b'\x1b[M\xc2\xa0!!'`
  
  AI disclosure: Initially created with claude code using opus 5.5.
  Iterated on, reviewed and tested manually by me.
  ```

## October 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37206958649), [2](https://github.com/ghostty-org/ghostty/actions/runs/37206425565), [3](https://github.com/ghostty-org/ghostty/actions/runs/37167192678)  
Summary: 3 runs • 23 commits • 5 authors

### Changes

- [`e6db5b6`](https://github.com/ghostty-org/ghostty/commit/e6db5b633a9ae820fea1620af52dbf87cc7e430c) terminal: fix crash after shrinking columns splits a wide char ([@fornwall](https://github.com/fornwall))
  ```text
  Narrowing without reflow cleared only the cells past the new width, so a
  wide char whose spacer tail was cut kept its head in the new last column.
  Every operation pairing a head with the cell after it then reached past
  the row end: insertBlanks and eraseLine(.left) panic in Screen.clearCells,
  and rowWillBeShifted writes cells[cols].
  
  Clear the orphaned head along with the cut columns.
  ```
- [`5dc28bb`](https://github.com/ghostty-org/ghostty/commit/5dc28bb8eebaf57a6c793a406bfea8c632d4fa94) terminal: fix crash after shrinking columns splits a wide char ([#14509](https://github.com/ghostty-org/ghostty/issues/14509)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Narrowing the terminal without reflow (wraparound off, or the alternate
  screen) can cut a wide char in half, leaving its head in the last column
  with no spacer tail.
  
  Later edits on that row (e.g.
  [ICH](https://ghostty.org/docs/vt/csi/ich)) then clear the missing tail
  too, reaching one cell past the row end, which leads to a bounds
  assertion failure in safe builds or an out-of-bounds write otherwise.
  
  To reproduce, run the below script inside a safe build:
  
  ```sh
  #!/bin/sh
  printf '\e[?40h\e[?3h'       # allow DECCOLM, switch to 132 columns
  printf '\e[?47h\e[1;80H一'   # alternate screen: wide char in columns 80-81
  printf '\e[?47l\e[?3l'       # back to 80 columns (alternate screen shrinks without reflow)
  printf '\e[?47h\e[1;80H\e[@' # alternate screen: insert a blank at the last column
  printf '\e[2;1Hsurvived\n'
  ```
  
  - Before: Triggers assertion in `Screen.clearCells`.
  - After: Prints `survived`, column 80 is blank.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ````
- [`9272a2f`](https://github.com/ghostty-org/ghostty/commit/9272a2f7c24a9282541dba8a3b361ae98bde81bc) terminal: support DECRQCRA and XTCHECKSUM ([@jcollie](https://github.com/jcollie))
  ```text
  Programs such as terminal test suites use DECRQCRA to check what is on
  the screen. Since it also lets any program read the screen back, it is
  off unless vt-xt-checksum-report is set.
  ```
- [`00a19db`](https://github.com/ghostty-org/ghostty/commit/00a19db51aeee5253c83fecc5b647c0358573b5f) config: add vt-xt-checksum-extension ([@jcollie](https://github.com/jcollie))
  ```text
  RIS resets the DECRQCRA checksum calculation, so a program like
  esctest that needs xterm's other calculations had no way to keep it.
  This is the equivalent of xterm's checksumExtension resource.
  ```
- [`7e2d179`](https://github.com/ghostty-org/ghostty/commit/7e2d1793da7f3e1d00b27abe5fe03bb04a0fb474) lib-vt: add GHOSTTY_TERMINAL_OPT_XT_CHECKSUM_EXTENSION ([@jcollie](https://github.com/jcollie))
  ```text
  Embedders had no way to choose the DECRQCRA checksum calculation that
  survives RIS, which vt-xt-checksum-extension gives the app.
  ```
- [`25b04b4`](https://github.com/ghostty-org/ghostty/commit/25b04b410463b97dbc91ec4d24da500a66f4b962) lib-vt: export xt_checksum and device_attributes ([@jcollie](https://github.com/jcollie))
  ```text
  Zig users couldn't name the types needed to set a default checksum or
  answer device attribute queries.
  ```
- [`edcaf66`](https://github.com/ghostty-org/ghostty/commit/edcaf66707f1164030872c0d7a463035af9fc29a) test/esctest: enable DECRQCRA ([@jcollie](https://github.com/jcollie))
  ```text
  esctest reads the screen back with DECRQCRA, so every test that checks
  screen contents failed while the runner left it off.
  ```
- [`cc02767`](https://github.com/ghostty-org/ghostty/commit/cc02767783543f53420c0adf139b5fe6b2471a78) terminal: link to xterm's checksum implementation ([@jcollie](https://github.com/jcollie))
  ```text
  The checksum is modeled on xterm's, so point at its source for comparison.
  ```
- [`5f0d4fe`](https://github.com/ghostty-org/ghostty/commit/5f0d4febc3ac8686ac911aa4a209a4e3d8a48131) terminal: use a rectangle selection for DECRQCRA ([@jcollie](https://github.com/jcollie))
  ```text
  The checksum had its own rectangle type and row walk, duplicating what
  Selection and the pin iterators already provide.
  ```
- [`b2f557c`](https://github.com/ghostty-org/ghostty/commit/b2f557c6c142a5787774c59dd8cb88a58fabc5d0) terminal: inline the checksum test helper ([@jcollie](https://github.com/jcollie))
  ```text
  Each test now shows the selection and flags it checks directly.
  ```
- [`01b9f49`](https://github.com/ghostty-org/ghostty/commit/01b9f4958d9d952cdbbe2473c31dfc7695d3c421) terminal: link to xterm's checksumExtension source ([@jcollie](https://github.com/jcollie))
  ```text
  xterm's documentation for these bits disagrees with its code, so
  point at both to show which one the flags follow.
  ```
- [`e8b858c`](https://github.com/ghostty-org/ghostty/commit/e8b858cc66971aa55376866b149fe304e958fc3b) terminal/tmux: don't count unstored bytes against max_bytes ([@jcollie](https://github.com/jcollie))
  ```text
  A line that filled the control mode buffer exactly couldn't be
  terminated: the newline ending a notification or block, and the '%'
  starting the next notification, were rejected as exceeding the limit
  even though none of them are stored. The parser then broke and dropped
  all further control mode output.
  
  Fixes #11935
  ```
- [`e55c687`](https://github.com/ghostty-org/ghostty/commit/e55c687a4bdf46a4a7a9f51f040798fc11e62154) input: encode ctrl+alt+shift+backspace in legacy mode ([@fornwall](https://github.com/fornwall))
  ```text
  The legacy backspace table, taken from foot's keymap.h, was missing
  foot's Shift+Alt+Ctrl row. The chord fell through to the unmodified
  entry and sent a bare DEL (BS under DECBKM), dropping both the Alt
  prefix and Ctrl. Send ESC BS like Alt+Ctrl and Shift+Alt+Ctrl+Super.
  ```
- [`82ae67b`](https://github.com/ghostty-org/ghostty/commit/82ae67b9f41a009b131f4e336895cb2cce299dfd) libghostty: document allocator alignment as a bit count ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The alloc callback's alignment was documented as a power of two between
  1 and 16, but every vtable call passes @intFromEnum of a
  std.mem.Alignment: the number of low address bits that must be zero,
  not a byte count. An allocator written to the header would align a
  16-byte request to 4 bytes. The range was also wrong: snapshot export
  asks the terminal's allocator for page-aligned memory through
  pagePreservingState.
  
  Document the encoding the implementation already uses, with examples.
  ```
- [`406f2e5`](https://github.com/ghostty-org/ghostty/commit/406f2e54401978ad0bbf312b465554465b901f4e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`ac2ae69`](https://github.com/ghostty-org/ghostty/commit/ac2ae69e08690a6da4e92d61728da4513674bd4b) Update iTerm2 colorschemes ([#14527](https://github.com/ghostty-org/ghostty/issues/14527)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260928-151043-99d9701
  ```
- [`3425025`](https://github.com/ghostty-org/ghostty/commit/3425025e585a3403340d4dc6d65132f42e05e605) libghostty: document allocator alignment as log2 ([#14515](https://github.com/ghostty-org/ghostty/issues/14515)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The header says alignment is a power of two from 1 to 16:
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/include/ghostty/vt/allocator.h#L113-L114
  
  It's actually the log2, since we pass @intFromEnum of a
  std.mem.Alignment, which stores the exponent (@"16" = 4):
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/lib/allocator.zig#L99
  https://ziglang.org/documentation/0.16.0/std/#std.mem.Alignment
  
  So a C allocator written to the header aligns a 16-byte request to 4
  bytes.
  
  The 1–16 range is wrong too. Snapshot export asks the terminal's
  allocator for page-aligned memory:
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/terminal/snapshot/history.zig#L182
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/terminal/PageList.zig#L175-L178
  
  cc @pluiedev cuz i ruberducked the doc change with her.
  ```
- [`eee709f`](https://github.com/ghostty-org/ghostty/commit/eee709f5d3f1030cde981233ec75bfa940cd843f) input: encode ctrl+alt+shift+backspace in legacy mode ([#14508](https://github.com/ghostty-org/ghostty/issues/14508)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  In legacy key encoding, `Ctrl+Alt+Shift+Backspace` sent a bare DEL
  (`0x7f`), the same as plain Backspace.
  
  The backspace table in `function_keys.zig`, which [its header
  says](https://github.com/ghostty-org/ghostty/blob/33da6848d63b3bba2b4f31ab1531d618f2795192/src/input/function_keys.zig#L6-L7)
  is mostly based on foot's `keymap.h`, was missing [foot's Shift+Alt+Ctrl
  row](https://codeberg.org/dnkl/foot/src/commit/cb2771788998f6a6288e2de8273c55a8214551e0/keymap.h#L109).
  With this change it sends `ESC BS` (`\x1b\x08`), matching xterm.
  
  To reproduce, run:
  
  ```sh
  python3 -c 'import os,tty,termios;a=termios.tcgetattr(0);tty.setraw(0);b=os.read(0,16);termios.tcsetattr(0,termios.TCSADRAIN,a);print(repr(b))'
  ```
  
  Then press **Ctrl+Alt+Shift+Backspace** (Option for Alt on macOS).
  
  | | Output |
  |---|---|
  | Before | `b'\x7f'` |
  | After | `b'\x1b\x08'` |
  
  For comparison, Ctrl+Alt+Backspace prints `b'\x1b\x08'` both before and
  after.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ````
- [`2fb0c9c`](https://github.com/ghostty-org/ghostty/commit/2fb0c9cacb3fc75dbc8aedee9b7ed4321f091d33) terminal/tmux: don't count unstored bytes against max_bytes ([#14503](https://github.com/ghostty-org/ghostty/issues/14503)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A line that filled the control mode buffer exactly couldn't be
  terminated: the newline ending a notification or block, and the '%'
  starting the next notification, were rejected as exceeding the limit
  even though none of them are stored. The parser then broke and dropped
  all further control mode output.
  
  Fixes #11935
  
  AI disclosure: Claude Code assisted in the development of this PR.
  ```
- [`04d685c`](https://github.com/ghostty-org/ghostty/commit/04d685c6aa54b27a11fd547a9ac62cd97fdd5ee6) terminal: add suport for DECRQCRA and XTCHECKSUM ([#14483](https://github.com/ghostty-org/ghostty/issues/14483)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQCRA and XTCHECKSUM are used to inspect cells on the running
  terminal. They are mainly useful in conformance tests that verify that
  other control sequences are doing the right thing. Since these control
  sequences could be used to read the entire contents of the screen, they
  are disabled by default (see the `vt-checksum-report` config).
  
  Enabling these fix many of the failing `esctest2` tests.
  
  AI disclosure: Claude Code was used to develop this PR but I have
  thoroughly reviewed the code.
  ```
- [`aca9bf0`](https://github.com/ghostty-org/ghostty/commit/aca9bf031821c1b9dedfec24e93fb609468a274f) libghostty-vt: zero the decode_png output before the callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  For C embedders this was harmless but for embedders in garbage-collected
  languages like Go it isn't because it has a pointer field and in Go,
  storing a pointer into C memory requires that memory to be initialized first,
  because the collector also looks at the value being overwritten. If the
  leftover stack bytes happened to look like a Go heap address, the process
  would abort.
  
  And surprise surprise, around 1 in ~24,000 test runs on my Mac Studio at
  home was able to trigger this in my Go bindings.
  
  References:
  
  - cgo, "Passing pointers": C memory must be initialized before Go code
    stores a pointer into it.
    https://pkg.go.dev/cmd/cgo#hdr-Passing_pointers
  ```
- [`0e0ff28`](https://github.com/ghostty-org/ghostty/commit/0e0ff282f72c92d930d41f4703547d3bc9618ba2) libghostty-vt: zero the decode_png output before the callback ([#14530](https://github.com/ghostty-org/ghostty/issues/14530)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For C embedders this was harmless but for embedders in garbage-collected
  languages like Go it isn't because it has a pointer field and in Go,
  storing a pointer into C memory requires that memory to be initialized
  first, because the collector also looks at the value being overwritten.
  If the leftover stack bytes happened to look like a Go heap address, the
  process would abort.
  
  And surprise surprise, around 1 in ~24,000 test runs on my Mac Studio at
  home was able to trigger this in my Go bindings.
  
  References:
  
  - cgo, "Passing pointers": C memory must be initialized before Go code
  stores a pointer into it.
  https://pkg.go.dev/cmd/cgo#hdr-Passing_pointers
  ```
- [`f96c971`](https://github.com/ghostty-org/ghostty/commit/f96c9711b9f72ecf75e0fd50f3434529b4dea5b6) Update VOUCHED list ([#14528](https://github.com/ghostty-org/ghostty/issues/14528)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12713#discussioncomment-18737824)
  from @jcollie.
  
  Vouch: @maddythewisp
  ```

