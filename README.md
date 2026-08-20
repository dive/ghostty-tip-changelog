> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 20, 2026 at 15:27 UTC.

## August 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32380496303), [2](https://github.com/ghostty-org/ghostty/actions/runs/32327389360), [3](https://github.com/ghostty-org/ghostty/actions/runs/32324155930), [4](https://github.com/ghostty-org/ghostty/actions/runs/32318148403)  
Summary: 4 runs • 11 commits • 4 authors

### Changes

- [`fd17869`](https://github.com/ghostty-org/ghostty/commit/fd17869d15764a5a1f0f94e3b986e0a15eef0c43) macOS: rework for [#10943](https://github.com/ghostty-org/ghostty/issues/10943) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Keep the background color as it is and apply glass effect on top of it
  ```
- [`6f02d9a`](https://github.com/ghostty-org/ghostty/commit/6f02d9aad6d0fd4263b20e9a895ab4754b2ecc59) font: render glyf directly into output bitmap ([@jparise](https://github.com/jparise))
  ```text
  Glyf rasterization previously let z2d allocate its alpha surface, then
  duplicated the completed pixels into caller-owned storage. Back the z2d
  surface with the final bitmap instead, eliminating one allocation and a
  full bitmap copy for each non-empty glyph.
  ```
- [`9566a1a`](https://github.com/ghostty-org/ghostty/commit/9566a1a87eb04c85f7d9db5b62a138aa7e1a1879) termio: release initial input resources ([@jparise](https://github.com/jparise))
  ```text
  Initial input files remained open and their fully read buffers remained
  allocated after queueWrite copied their contents. Close these files on
  both startup success and failure, free their contents after queueing, and
  borrow raw values already owned by the arena.
  ```
- [`0de91ee`](https://github.com/ghostty-org/ghostty/commit/0de91eee32aa6bc8ac75c4bd868a297daa13a28a) font: render glyf directly into output bitmap ([#13929](https://github.com/ghostty-org/ghostty/issues/13929)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Glyf rasterization previously let z2d allocate its alpha surface, then
  duplicated the completed pixels into caller-owned storage. Back the z2d
  surface with the final bitmap instead, eliminating one allocation and a
  full bitmap copy for each non-empty glyph.
  ```
- [`aea0301`](https://github.com/ghostty-org/ghostty/commit/aea03011d08e2cba529cc8f21d1d5aeba2b447c5) termio: release initial input resources ([#13931](https://github.com/ghostty-org/ghostty/issues/13931)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Initial input files remained open and their fully read buffers remained
  allocated after queueWrite copied their contents. Close these files on
  both startup success and failure, free their contents after queueing,
  and borrow raw values already owned by the arena.
  
  **AI Usage:** This was spotted by GPT 5.6 Sol. I reworked the code a bit
  and understand it all.
  ```
- [`956a687`](https://github.com/ghostty-org/ghostty/commit/956a687d6393c57cf23176e00a86b74f4064441a) macOS: refine liquid glass styles ([#13928](https://github.com/ghostty-org/ghostty/issues/13928)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework for https://github.com/ghostty-org/ghostty/pull/10943;
  
  Keep the background color as it is and apply glass effect on top of it.
  Remove the color modification and keep our implementation relatively
  simple and more straightforward.
  
  This fixes https://github.com/ghostty-org/ghostty/issues/13914 and also
  ofc the linked issue in previous pr.
  
  ### Regular
  
  
  https://github.com/user-attachments/assets/b44e0af1-0a03-4773-8bfa-03ba48804235
  
  
  https://github.com/user-attachments/assets/83ab0ef5-6791-412d-b260-e7c55e7f890c
  
  ### Clear
  
  
  https://github.com/user-attachments/assets/8970b97c-7866-45dd-a122-dc9c8bdc7ec0
  
  
  https://github.com/user-attachments/assets/4105dc8f-f531-4a77-b193-b914c46d3075
  ```
- [`f1948d5`](https://github.com/ghostty-org/ghostty/commit/f1948d50544c36857047c12e46f10a3a1d41160d) terminal: transfer selection text into string maps ([@jparise](https://github.com/jparise))
  ```text
  Selection strings previously duplicated formatted text when callers
  requested a StringMap, even though the regex-link caller immediately
  freed the returned copy.
  
  Add a dedicated selectionStringMap path that transfers the formatter
  output and pin map directly into the returned map. This removes the
  extra allocation and copy while making ownership explicit.
  ```
- [`9ae02a3`](https://github.com/ghostty-org/ghostty/commit/9ae02a326f62bd88f7f5508cf1807c67e7775cb5) terminal: transfer selection text into string maps ([#13923](https://github.com/ghostty-org/ghostty/issues/13923)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Selection strings previously duplicated formatted text when callers
  requested a `StringMap`, even though the regex-link caller immediately
  freed the returned copy.
  
  Add a dedicated `selectionStringMap` path that transfers the formatter
  output and pin map directly into the returned map. This removes the
  extra allocation and copy while making ownership explicit.
  
  **AI Usage:** GTP 5.6 Sol identified and implemented this opportunity. I
  reviewed and understand it all.
  ```
- [`fc5ac17`](https://github.com/ghostty-org/ghostty/commit/fc5ac17a6886c69de93d645d2a7d8e16cb6ebbeb) i18n: complete Dutch (nl) translation for v1.4 ([#13853](https://github.com/ghostty-org/ghostty/issues/13853)) ([@kjvdven](https://github.com/kjvdven))
  ```text
  Fills the 181 untranslated strings in `po/nl.po`, bringing it to
  252/252. Most of them are the command palette actions from
  `src/input/command.zig`; the rest are the new context menu items, global
  keybind notifications, and config editing strings.
  
  **Style.** Ten of the new command palette strings had already been
  translated by previous translators, and those settle the verb form, so
  the rest follows them: imperative for verb+object action titles (`Split
  Left` → `Splits naar links`, `Close Tab` → `Sluit tabblad`), noun
  phrases left as noun phrases (`New Window` → `Nieuw venster`), no title
  case, informal "je". Descriptions are full imperative sentences. Dialog
  headings keep the noun-first infinitive form of the existing `Change
  Terminal Title` → `Titel van de terminal wijzigen`.
  
  A few translation notes:
  
  - `ANSI Sequences` → `ANSI-reeksen` in titles, `ANSI escape sequences` →
  `ANSI-escapereeksen` in descriptions, mirroring the distinction the
  source makes.
  - `Toggle X` titles use the idiomatic `X aan/uit`; their descriptions
  stay imperative (`Schakel … in of uit.`).
  - `surface` is rendered as `terminal` - the Dutch UI has no equivalent
  concept.
  - `scrollback` → `scrollbuffer`.
  
  **No existing translation was modified.** The diff only touches empty
  `msgstr` lines plus `PO-Revision-Date` and `Last-Translator`.
  
  Checked with `msgfmt -c --statistics` (252 translated, no warnings, no
  fuzzy) and `msgcat` (formatting is idempotent, so no rewrap noise for
  the next translator). No `X-Generator` field added.
  
  ---------
  ```
- [`a436a9e`](https://github.com/ghostty-org/ghostty/commit/a436a9edccee8688ec916f4e7ba223532a5183c4) macos: avoid temporary path component allocation ([@jparise](https://github.com/jparise))
  ```text
  The common directory helper previously allocated a temporary slice to
  prepend the base directory before joining path components. Pass the
  three known components directly to std.fs.path.join, leaving only the
  allocation for the returned path.
  ```
- [`9154efc`](https://github.com/ghostty-org/ghostty/commit/9154efcbd3c03bab3f1407c2ece38694fdbcb7ba) macos: avoid temporary path component allocation ([#13921](https://github.com/ghostty-org/ghostty/issues/13921)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The common directory helper previously allocated a temporary slice to
  prepend the base directory before joining path components. Pass the
  three known components directly to std.fs.path.join, leaving only the
  allocation for the returned path.
  ```

## August 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32310030415), [2](https://github.com/ghostty-org/ghostty/actions/runs/32305536881), [3](https://github.com/ghostty-org/ghostty/actions/runs/32298968455), [4](https://github.com/ghostty-org/ghostty/actions/runs/32273834618), [5](https://github.com/ghostty-org/ghostty/actions/runs/32205120526)  
Summary: 5 runs • 45 commits • 7 authors

### Changes

- [`a9f7f6d`](https://github.com/ghostty-org/ghostty/commit/a9f7f6d212a0af39a9597a3ea815140358d1975e) surface: parse text bindings with stack fallback ([@jparise](https://github.com/jparise))
  ```text
  Text binding actions previously allocated a temporary buffer for every
  escaped string. Use a 256-byte stack fallback allocator so typical
  bindings avoid the transient heap allocation while larger values
  continue to use the existing heap-backed behavior.
  ```
- [`8e8d76b`](https://github.com/ghostty-org/ghostty/commit/8e8d76b634f1b791fd693715fc56d728b4967dab) shell-integration: avoid owning temporary commands ([@jparise](https://github.com/jparise))
  ```text
  Some shell setup functions previously converted their stack-backed
  command builders to owned sentinel slices before duplicating them into
  the result arena. Duplicate the builders' written bytes directly
  instead, avoiding unnecessary ownership transfer and sentinel handling.
  ```
- [`49e503f`](https://github.com/ghostty-org/ghostty/commit/49e503fd40401baf3c13903b5941f67dfdcd07db) surface: parse text bindings with stack fallback ([#13918](https://github.com/ghostty-org/ghostty/issues/13918)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Text binding actions previously allocated a temporary buffer for every
  escaped string. Use a 256-byte stack fallback allocator so typical
  bindings avoid the transient heap allocation while larger values
  continue to use the existing heap-backed behavior.
  ```
- [`50d3ac8`](https://github.com/ghostty-org/ghostty/commit/50d3ac8ed6ad1cbca498f7a4388ab14054a5c3e1) shell-integration: avoid owning temporary commands ([#13919](https://github.com/ghostty-org/ghostty/issues/13919)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Some shell setup functions previously converted their stack-backed
  command builders to owned sentinel slices before duplicating them into
  the result arena. Duplicate the builders' written bytes directly
  instead, avoiding unnecessary ownership transfer and sentinel handling.
  ```
- [`f699069`](https://github.com/ghostty-org/ghostty/commit/f6990690f07fdb0a71e46cd809531ca0f5b86f40) Revert "macOS: hide settings menu icon on macOS 27 ([#13664](https://github.com/ghostty-org/ghostty/issues/13664))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 99c483f477dcf3d6523a976772dcac71ab9466d3, reversing
  changes made to 33bdeed1cbc69196c10466d0c9d881c0a7a7ac9c.
  ```
- [`043abc7`](https://github.com/ghostty-org/ghostty/commit/043abc7b6045fa11c08660337a7a2b7a9533205e) macOS: group settings menu in a separate group ([@bo2themax](https://github.com/bo2themax))
- [`5a8921e`](https://github.com/ghostty-org/ghostty/commit/5a8921ecb5bcb0411825722b2b7010db8eb3f56a) surface: keep clipboard content list on stack ([@jparise](https://github.com/jparise))
  ```text
  Use a two element stack-based buffer for the one or two ClipboardContent
  entries rather than the (arena-based) heap allocator.
  ```
- [`4d646ba`](https://github.com/ghostty-org/ghostty/commit/4d646bae0c6dd28c1e49db1b3e04464417f94b41) macOS: group settings menu in a separate group ([#13906](https://github.com/ghostty-org/ghostty/issues/13906)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Reverted https://github.com/ghostty-org/ghostty/pull/13664 with a
  second thought.**
  
  This keeps the consistency with other first-party apps like Terminal,
  Finder, and Music. It seems that most of the first-party apps show the
  standard icons on macOS 27 for "Settings...", "Find", "AutoFill" and
  etc., but in a separate group.
  
  <img width="1060" height="375" alt="image"
  src="https://github.com/user-attachments/assets/d3017865-a443-4c14-ace9-1c6b5acb3f56"
  />
  
  
  I believe this still follows
  [HIG](https://developer.apple.com/design/human-interface-guidelines/menus#Icons).
  ```
- [`a4edca2`](https://github.com/ghostty-org/ghostty/commit/a4edca2a90d6cf89900bb058e71cb6860cec78c5) surface: keep clipboard content list on stack ([#13916](https://github.com/ghostty-org/ghostty/issues/13916)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use a two element stack-based buffer for the one or two ClipboardContent
  entries rather than the (arena-based) heap allocator.
  ```
- [`ece96a1`](https://github.com/ghostty-org/ghostty/commit/ece96a14cf4ff3497505067ec4821a201d2f2b70) i18n: update pt_BR translations ([@guilhermetk](https://github.com/guilhermetk))
- [`8a0a9fa`](https://github.com/ghostty-org/ghostty/commit/8a0a9faf8577c72fa8a287fb72694018a9c80f23) i18n: use "Redefinir" for reset actions in pt_BR ([@guilhermetk](https://github.com/guilhermetk))
  ```text
  The "Reset" menu item and the "Reset Terminal" command palette entry
  were translated as "Reiniciar", which reads as restarting the terminal
  session or process. These actions perform a VT reset that clears
  terminal state without restarting the shell, so "Redefinir" conveys
  the correct meaning and matches the standard pt_BR terminology used
  by other terminal emulators.
  ```
- [`6ab3ef9`](https://github.com/ghostty-org/ghostty/commit/6ab3ef94714f95d8a8f486d645f9056974dcf859) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`123dc0c`](https://github.com/ghostty-org/ghostty/commit/123dc0ccb1e3c7209c94faa9286748bb29a22d52) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`1c34e0d`](https://github.com/ghostty-org/ghostty/commit/1c34e0df8504313223e468020d2415b7e2e5aec7) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`6c29a0a`](https://github.com/ghostty-org/ghostty/commit/6c29a0a28292a75d9c259538193fef994ec6b934) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`d6871cd`](https://github.com/ghostty-org/ghostty/commit/d6871cd924569e5149e18fc6545957e087cd4f7c) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`6fe197d`](https://github.com/ghostty-org/ghostty/commit/6fe197d86ade436f7bbab5d57fdf9893e7eb5e31) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`1225632`](https://github.com/ghostty-org/ghostty/commit/1225632d1c9dc90eb04efd62bd5ec0958a151e27) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`31a10a7`](https://github.com/ghostty-org/ghostty/commit/31a10a7b5172c9233243ca81608cde53a21e705b) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`1b8da6b`](https://github.com/ghostty-org/ghostty/commit/1b8da6b40fd1c67d5d60a02c62b00d86b18ab072) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`58c4796`](https://github.com/ghostty-org/ghostty/commit/58c4796c1c9876995dbc02d91be084df6c2cdea5) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`0149ef5`](https://github.com/ghostty-org/ghostty/commit/0149ef5f72f5aaafd0382fad09f1618c509ffa20) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`17a6627`](https://github.com/ghostty-org/ghostty/commit/17a66279be132cb35b790f6610514ed1a31d6163) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`be892fc`](https://github.com/ghostty-org/ghostty/commit/be892fc6c1aab84b31223ce8a23385e739c59520) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`cdefb68`](https://github.com/ghostty-org/ghostty/commit/cdefb6809a7184f0910861ac57a4ee218e433e03) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`ed13a09`](https://github.com/ghostty-org/ghostty/commit/ed13a09a59dde5ff2695c4a84aad49050c839711) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`e493926`](https://github.com/ghostty-org/ghostty/commit/e49392671390ec9e87f75668608e355122605e27) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`e820ef4`](https://github.com/ghostty-org/ghostty/commit/e820ef48b2b10b7ed44199e24396f1d3b7e456d2) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`03cb485`](https://github.com/ghostty-org/ghostty/commit/03cb485f60d93243bacfdfe51c512c03f1bb9c32) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`3bdbad7`](https://github.com/ghostty-org/ghostty/commit/3bdbad7d8869afb6b95e7997a1a4703e8a71acb3) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`132f154`](https://github.com/ghostty-org/ghostty/commit/132f154e5f419bd719ef77a3c9cf050e7d2f2741) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`bde2047`](https://github.com/ghostty-org/ghostty/commit/bde2047a636dd602a15b034fdefb7b9b61f5b2c2) Apply suggestions from code review ([@guilhermetk](https://github.com/guilhermetk))
- [`d2f08cb`](https://github.com/ghostty-org/ghostty/commit/d2f08cb0b12bf81ac4029a5181bf3dea2ea0f0bd) Apply suggestions from code review ([@guilhermetk](https://github.com/guilhermetk))
- [`ae7080e`](https://github.com/ghostty-org/ghostty/commit/ae7080e6cc00fa7a1107ef57974945b8b18a23e4) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`6562166`](https://github.com/ghostty-org/ghostty/commit/65621664eda30796a5d2fbc04b09e9b01825ef39) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`9581f7d`](https://github.com/ghostty-org/ghostty/commit/9581f7dd456f684d6f41c3b4e58f4621262ff725) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`4302020`](https://github.com/ghostty-org/ghostty/commit/4302020990ad25cfc8294b5fb33b2ca0a4b5310d) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`5a55a34`](https://github.com/ghostty-org/ghostty/commit/5a55a345aa5247d4e67be431f9a920f5fa67399e) Update po/pt_BR.po ([@guilhermetk](https://github.com/guilhermetk))
- [`e8a7097`](https://github.com/ghostty-org/ghostty/commit/e8a7097f65bda1e6bb7a78cee1a67d8f8c9d376f) i18: use "aplicativo" instead of "aplicação" for "application" ([@guilhermetk](https://github.com/guilhermetk))
- [`959c0da`](https://github.com/ghostty-org/ghostty/commit/959c0daeaa1abbe9fd03a0da0601e4cd6e360799) i18n: update revision date ([@guilhermetk](https://github.com/guilhermetk))
- [`3e7230b`](https://github.com/ghostty-org/ghostty/commit/3e7230bf5d0e12d018b850ed3856daa848bfebb7) i18n: update pt_BR translations ([#13819](https://github.com/ghostty-org/ghostty/issues/13819)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update all missing Portuguese/BR translations for 1.4.
  
  Part of https://github.com/ghostty-org/ghostty/issues/13766
  ```
- [`f4f9991`](https://github.com/ghostty-org/ghostty/commit/f4f9991d2c188b7c1f364ed9e44b92dd3356bb2a) chore(vt): expose snapshot api ([@neurosnap](https://github.com/neurosnap))
- [`d9ffbbf`](https://github.com/ghostty-org/ghostty/commit/d9ffbbf17c11f570897a49d4c722130e8698d93b) chore(vt): expose snapshot api ([#13912](https://github.com/ghostty-org/ghostty/issues/13912)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Link:
  https://discord.com/channels/1005603569187160125/1420009803173859449/1539649787748417667
  ```
- [`bed20eb`](https://github.com/ghostty-org/ghostty/commit/bed20eb36453c61c6aff76bdfda0c15235b8e513) terminal: clear tabstop bit on unset instead of toggling ([@fornwall](https://github.com/fornwall))
  ```text
  Tabstops.unset used XOR, so unsetting a column without a tabstop set
  one instead. This made TBC (CSI 0 g) and CTC (CSI 2 W) create a
  tabstop at the cursor column when none existed.
  ```
- [`4c6215b`](https://github.com/ghostty-org/ghostty/commit/4c6215bb8ee186b5c829457a9a9a9c936f2337bf) terminal: clear tabstop bit on unset instead of toggling ([#13900](https://github.com/ghostty-org/ghostty/issues/13900)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make `Tabstops.unset` (backing [Tab Clear
  (TBC)](https://ghostty.org/docs/vt/csi/tbc) with `n=0`) not set a tab
  stop when clearing a column that has no tab stop.
  ```

## August 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32176127114), [2](https://github.com/ghostty-org/ghostty/actions/runs/32172263374), [3](https://github.com/ghostty-org/ghostty/actions/runs/32169188975), [4](https://github.com/ghostty-org/ghostty/actions/runs/32168669864), [5](https://github.com/ghostty-org/ghostty/actions/runs/32160637749), [6](https://github.com/ghostty-org/ghostty/actions/runs/32145015115)  
Summary: 6 runs • 23 commits • 2 authors

### Changes

- [`cfc5a96`](https://github.com/ghostty-org/ghostty/commit/cfc5a96501d72d0c43a73a9ed2f74c6381ba046c) terminal/kitty: validate graphics query image data ([@mitchellh](https://github.com/mitchellh))
  ```text
  Graphics query commands previously initialized their loading state but
  returned success before completing the image load.
  
  This allowed truncated, malformed, or otherwise invalid image data to
  return OK, giving capability probes a false positive.
  
  Complete and validate queried images through the normal load path, then
  discard the result without modifying image storage. Add coverage for
  invalid data and preserving an existing image with the queried ID.
  ```
- [`86d94f1`](https://github.com/ghostty-org/ghostty/commit/86d94f150a2c3a8e83c4dcab004e1a89af07b1c6) terminal/kitty: preserve chunked response identifiers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Chunked image responses used the final command even though only the
  initial chunk carries the image and placement identifiers. Successful
  replies lost image numbers and placement IDs. Final validation errors
  could also be suppressed entirely.
  
  Save the initial response identifiers with the in-progress image and use
  them when the final chunk completes. Continue replacing the response ID
  with the generated image ID after a successful load. Cover successful
  image-number replies and invalid final payloads with unit tests.
  ```
- [`306a169`](https://github.com/ghostty-org/ghostty/commit/306a169033cd945a5bcd8b5c31fdeae218006648) terminal/kitty: preserve data on unmatched delete ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make uppercase Kitty graphics deletes with a nonzero placement ID
  leave the image intact when the named placement does not exist.
  
  Previously, d=I,i=...,p=... could free unreferenced image data after
  matching no placement. A later put then failed with ENOENT, diverging
  from the protocol and Kitty.
  ```
- [`72b6cd7`](https://github.com/ghostty-org/ghostty/commit/72b6cd71247086eaa8f93edcc49d6d689045b715) terminal/kitty: validate graphics query image data ([#13896](https://github.com/ghostty-org/ghostty/issues/13896)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Graphics query commands previously initialized their loading state but
  returned success before completing the image load.
  
  This allowed truncated, malformed, or otherwise invalid image data to
  return OK, giving capability probes a false positive.
  
  Complete and validate queried images through the normal load path, then
  discard the result without modifying image storage. Add coverage for
  invalid data and preserving an existing image with the queried ID.
  ```
- [`fe12e30`](https://github.com/ghostty-org/ghostty/commit/fe12e30b3468b7afb92744f96af33f4ce484f4a9) terminal/kitty: preserve chunked response identifiers ([#13897](https://github.com/ghostty-org/ghostty/issues/13897)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Chunked image responses used the final command even though only the
  initial chunk carries the image and placement identifiers. Successful
  replies lost image numbers and placement IDs. Final validation errors
  could also be suppressed entirely.
  
  Save the initial response identifiers with the in-progress image and use
  them when the final chunk completes. Continue replacing the response ID
  with the generated image ID after a successful load. Cover successful
  image-number replies and invalid final payloads with unit tests.
  ```
- [`7f62fe7`](https://github.com/ghostty-org/ghostty/commit/7f62fe70a288c5d35ebd3097e75c46017950bcc7) terminal/kitty: preserve data on unmatched delete ([#13898](https://github.com/ghostty-org/ghostty/issues/13898)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make uppercase Kitty graphics deletes with a nonzero placement ID leave
  the image intact when the named placement does not exist.
  
  Previously, d=I,i=...,p=... could free unreferenced image data after
  matching no placement. A later put then failed with ENOENT, diverging
  from the protocol and Kitty.
  ```
- [`f8b40a0`](https://github.com/ghostty-org/ghostty/commit/f8b40a02356f5ed945d4c2fa981394776186228b) terminal/kitty: fix various graphics deletion mismatches with spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Limit d=a/A to non-virtual placements that intersect the active screen.
  - Keep unrelated unplaced image data when processing d=A.
  - Make d=R delete matching unused images even when they have no
    placements, and default an omitted x bound to zero.
  - Give ED2 a separate clear path that preserves scrollback references
    while reclaiming every unreferenced image.
  
  References:
  - Spec:
    https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  - Delete reference implementation:
    https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L2114-L2363
  - ED2 reference implementation:
    https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L2919-L2958
  ```
- [`2ced1e5`](https://github.com/ghostty-org/ghostty/commit/2ced1e5c8e55bdc1cd77c7ecada4d0ef1cb28226) terminal/kitty: fix various graphics deletion mismatches with spec ([#13895](https://github.com/ghostty-org/ghostty/issues/13895)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Limit d=a/A to non-virtual placements that intersect the active
  screen.
  - Keep unrelated unplaced image data when processing d=A.
  - Make d=R delete matching unused images even when they have no
  placements, and default an omitted x bound to zero.
  - Give ED2 a separate clear path that preserves scrollback references
  while reclaiming every unreferenced image.
  
  References:
  - Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  - Delete reference implementation:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L2114-L2363
  - ED2 reference implementation:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L2919-L2958
  ```
- [`e5747cf`](https://github.com/ghostty-org/ghostty/commit/e5747cf0b603e4cad0ab6642c44738c9cfb50fa5) terminal/kitty: abort incomplete graphics loads ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, delete left partial bytes alive for the next upload, while
  failed or incomplete retransmissions kept stale placements visible.
  
  Abort incomplete chunked image uploads on delete commands and remove an
  existing image and its placements when retransmission of an explicit ID
  begins.
  ```
- [`55dac8f`](https://github.com/ghostty-org/ghostty/commit/55dac8fc47c239c54540fa30f3bea882d359d07f) terminal/kitty: abort incomplete graphics loads ([#13893](https://github.com/ghostty-org/ghostty/issues/13893)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, delete left partial bytes alive for the next upload, while
  failed or incomplete retransmissions kept stale placements visible.
  
  Abort incomplete chunked image uploads on delete commands and remove an
  existing image and its placements when retransmission of an explicit ID
  begins.
  ```
- [`83145c0`](https://github.com/ghostty-org/ghostty/commit/83145c0a374852b6c1c2b6e7eab94b4db63c10f7) terminal/kitty: reject conflicting image identifiers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reject Kitty graphics commands that specify both an image ID and an
  image number across every protocol action.
  
  These commands previously produced no wire response for transmissions,
  while put and delete actions could proceed using one identifier and
  mutate terminal state.
  
  Retain the original command identifiers, validate them before action
  dispatch, and preserve them in the EINVAL response. Add regression
  coverage for every action, response encoding, quiet suppression, and
  pre-mutation rejection.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal
  ```
- [`52190a5`](https://github.com/ghostty-org/ghostty/commit/52190a5d8da4e21e628bb01f12f32da7b06b3a54) terminal/kitty: intersect source rectangles before sizing ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics placements previously calculated pixel and grid geometry
  from requested source dimensions before intersecting them with the image.
  The renderer clamped explicit dimensions later but treated omitted
  source dimensions as the full image.
  
  This stretched clipped crops into incorrectly sized destinations and
  exposed inconsistent geometry through storage, rendering, and
  libghostty.
  
  Resolve the source rectangle once against the image bounds and reuse it
  for placement sizing, renderer preparation, and the C API. Add
  regression tests for omitted and explicit dimensions and renderer
  geometry.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  Reference: https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1225-L1240
  ```
- [`409e682`](https://github.com/ghostty-org/ghostty/commit/409e682c832198be782071c7b6c182c29227d3aa) terminal/kitty: reject conflicting image identifiers ([#13889](https://github.com/ghostty-org/ghostty/issues/13889)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reject Kitty graphics commands that specify both an image ID and an
  image number across every protocol action.
  
  These commands previously produced no wire response for transmissions,
  while put and delete actions could proceed using one identifier and
  mutate terminal state.
  
  Retain the original command identifiers, validate them before action
  dispatch, and preserve them in the EINVAL response. Add regression
  coverage for every action, response encoding, quiet suppression, and
  pre-mutation rejection.
  
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal
  ```
- [`9848cb1`](https://github.com/ghostty-org/ghostty/commit/9848cb15fae7eb6abfc74d563ff98b24c830900f) terminal/kitty: intersect source rectangles before sizing ([#13890](https://github.com/ghostty-org/ghostty/issues/13890)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics placements previously calculated pixel and grid geometry
  from requested source dimensions before intersecting them with the
  image. The renderer clamped explicit dimensions later but treated
  omitted source dimensions as the full image.
  
  This stretched clipped crops into incorrectly sized destinations and
  exposed inconsistent geometry through storage, rendering, and
  libghostty.
  
  Resolve the source rectangle once against the image bounds and reuse it
  for placement sizing, renderer preparation, and the C API. Add
  regression tests for omitted and explicit dimensions and renderer
  geometry.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  Reference:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1225-L1240
  ```
- [`c5a3c7e`](https://github.com/ghostty-org/ghostty/commit/c5a3c7e2e5b4e39ce59c14cb35c55be971058575) terminal/kitty: constrain placement offsets to cell bounds ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clamp X and Y offsets when a placement is created and normalize them
  again against current cell geometry when sizing and rendering. The
  protocol requires offsets to remain within the first cell and not
  enlarge explicit c/r rectangles:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  
  Previously, explicit placements were sized to the full c/r rectangle
  before the offset was applied. This extended their far edge into
  neighboring cells and let unbounded offsets reach renderer geometry.
  ```
- [`7e5dfa0`](https://github.com/ghostty-org/ghostty/commit/7e5dfa09eb601fedb9bdf5816d02890108ac1f04) terminal/kitty: constrain placement offsets to cell bounds ([#13891](https://github.com/ghostty-org/ghostty/issues/13891)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clamp X and Y offsets when a placement is created and normalize them
  again against current cell geometry when sizing and rendering. The
  protocol requires offsets to remain within the first cell and not
  enlarge explicit c/r rectangles:
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  
  Previously, explicit placements were sized to the full c/r rectangle
  before the offset was applied. This extended their far edge into
  neighboring cells and let unbounded offsets reach renderer geometry.
  ```
- [`abd7706`](https://github.com/ghostty-org/ghostty/commit/abd77067def1653692987588913b83c975ab4893) terminal/kitty: graphics `S` value is exact byte, not max ([@mitchellh](https://github.com/mitchellh))
  ```text
  File transmissions with exactly S bytes or trailing file data previously
  failed because appendRemaining reports StreamTooLong when it reaches its
  limit. This broke the protocol's partial-file transmission path.
  
  Use an exact-length allocation and read when S is nonzero, rejecting
  premature EOF and values above the image limit. Preserve the existing
  bounded read-to-EOF behavior for S=0.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#local-client
  ```
- [`364f8e9`](https://github.com/ghostty-org/ghostty/commit/364f8e9ac1e6dd79233e59fd46435c54e2117caf) terminal/kitty: graphics `S` value is exact byte, not max ([#13892](https://github.com/ghostty-org/ghostty/issues/13892)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  File transmissions with exactly S bytes or trailing file data previously
  failed because appendRemaining reports StreamTooLong when it reaches its
  limit. This broke the protocol's partial-file transmission path.
  
  Use an exact-length allocation and read when S is nonzero, rejecting
  premature EOF and values above the image limit. Preserve the existing
  bounded read-to-EOF behavior for S=0.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#local-client
  ```
- [`afb61e1`](https://github.com/ghostty-org/ghostty/commit/afb61e1b6292f56b863ad0fe61bcdbad47392a5e) terminal/kitty: place cursor after tall images properly ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #13886
  
  This fixes an incompatibility between Ghostty and Kitty 0.47.1+.
  
  Previously, Ghostty handled `C=0` by moving down at most one terminal
  height and then clamping the horizontal destination to the screen. The
  limit protected against an image command requesting billions of rows,
  but it counted ordinary movement to the bottom as well as scrolling.
  
  Kitty defines `C=0` as leaving the cursor after the image and implements
  the movement as rows minus one, plus one row when the image reaches the
  right edge:
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1256-L1260
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L1903-L1915
  
  (Had to view Kitty source to verify what the spec meant)
  
  For example, an eight-row, full-width image in a five-row terminal needs
  four moves to reach the bottom and four more to scroll. The old limit
  allowed only five moves in total, so the next image started four rows
  inside the first one. Clamping the horizontal destination also left the
  cursor at the final column instead of wrapping to column one of the next
  row. Consecutive images could therefore overlap in both directions.
  ```
- [`d4d72f3`](https://github.com/ghostty-org/ghostty/commit/d4d72f3205f7a995fa4578f4b5369937f0b17a18) terminal/kitty: place cursor after tall images properly ([#13887](https://github.com/ghostty-org/ghostty/issues/13887)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #13886
  
  This fixes an incompatibility between Ghostty and Kitty 0.47.1+.
  
  Previously, Ghostty handled `C=0` by moving down at most one terminal
  height and then clamping the horizontal destination to the screen. The
  limit protected against an image command requesting billions of rows,
  but it counted ordinary movement to the bottom as well as scrolling.
  
  Kitty defines `C=0` as leaving the cursor after the image and implements
  the movement as rows minus one, plus one row when the image reaches the
  right edge:
  
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1256-L1260
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L1903-L1915
  
  (Had to view Kitty source to verify what the spec meant)
  
  For example, an eight-row, full-width image in a five-row terminal needs
  four moves to reach the bottom and four more to scroll. The old limit
  allowed only five moves in total, so the next image started four rows
  inside the first one. Clamping the horizontal destination also left the
  cursor at the final column instead of wrapping to column one of the next
  row. Consecutive images could therefore overlap in both directions.
  ```
- [`07af461`](https://github.com/ghostty-org/ghostty/commit/07af4612ba17afe13fcba1de8d8a1258bc666a10) terminal: report size when mode 2048 is enabled ([@elias8](https://github.com/elias8))
- [`5b9a77f`](https://github.com/ghostty-org/ghostty/commit/5b9a77f203865e73de885df743afc73af96fba50) terminal: document mode 2048 size reports ([@elias8](https://github.com/elias8))
- [`0a16db3`](https://github.com/ghostty-org/ghostty/commit/0a16db3c686045fe5ac8a58d3c91dc53d108e662) fix(lib-vt): report size when mode 2048 is enabled ([#13885](https://github.com/ghostty-org/ghostty/issues/13885)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Mode 2048 requires terminals to report the current rows, columns, and
  pixel dimensions [when the mode is
  enabled](https://gist.github.com/rockorager/e695fb2924d36b2bcf1fff4a3704bd83#:~:text=When%20first%20enabled%2C%20the%20terminal%20MUST%20send%20a%20report%20of%20the%20current%20size.),
  then report updated geometry after later resizes. The native termio
  stream already queues the initial report, but the terminal stream only
  reported from `resize`, so libghostty consumers that enabled the mode
  after committing geometry received nothing until another resize.
  
  This makes the generic handler match termio by requesting current
  geometry through the existing size callback and writing the encoded
  report through `write_pty` on every enable.
  ```

## August 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32070024528), [2](https://github.com/ghostty-org/ghostty/actions/runs/32065823102), [3](https://github.com/ghostty-org/ghostty/actions/runs/32056946273), [4](https://github.com/ghostty-org/ghostty/actions/runs/32047937055), [5](https://github.com/ghostty-org/ghostty/actions/runs/32034783819), [6](https://github.com/ghostty-org/ghostty/actions/runs/32007079296), [7](https://github.com/ghostty-org/ghostty/actions/runs/31995485081), [8](https://github.com/ghostty-org/ghostty/actions/runs/31992629892), [9](https://github.com/ghostty-org/ghostty/actions/runs/31984667378)  
Summary: 9 runs • 34 commits • 9 authors

### Changes

- [`9be6c2e`](https://github.com/ghostty-org/ghostty/commit/9be6c2ea2870f409f3e73337f3f5ac74db806ba3) libghostty: option to retain continuations on snapshot decode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a snapshot decoder option that leaves continuation tracking
  enabled on decoded terminals. This lets caller access the continuation
  bytes (if any) that were applied to the terminal.
  
  This lets replay callers export an unfinished parser or UTF-8 sequence
  from the returned terminal.
  
  This defaults to off.
  ```
- [`12967b6`](https://github.com/ghostty-org/ghostty/commit/12967b68f7d46bdbfb2cfffb6768332fb9db68c0) libghostty: option to retain continuations on snapshot decode ([#13878](https://github.com/ghostty-org/ghostty/issues/13878)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a snapshot decoder option that leaves continuation tracking enabled
  on decoded terminals. This lets caller access the continuation bytes (if
  any) that were applied to the terminal.
  
  This lets replay callers export an unfinished parser or UTF-8 sequence
  from the returned terminal.
  
  This defaults to off.
  ```
- [`846d24e`](https://github.com/ghostty-org/ghostty/commit/846d24e12b3bc12c5623cabf311f3e8c13621ea4) libghostty: buffer the writer adapter used by streaming C APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyWriter adapter was unbuffered, so for streaming writers that
  make small writes like the formatter, it produces a crazy amount of callbacks:
  one styled HTML page invoked the callback ~50,000 times in a benchmark lol.
  
  Change WriterAdapter to have an optional buffer (initBuffered) and use
  a 4 KB buffer for all current callers. Also optimize single byte splats
  to use memset.
  
  Results: that same styled HTML example goes from ~50K callbacks to 124.
  And throughput through the C API also improved across every workload
  I tested (styled and unstyled text in every format).
  ```
- [`56e1f3a`](https://github.com/ghostty-org/ghostty/commit/56e1f3a62e26407e8c020ef5881df3e8584be20f) libghostty: buffer the writer adapter used by streaming C APIs ([#13877](https://github.com/ghostty-org/ghostty/issues/13877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyWriter adapter was unbuffered, so for streaming writers that
  make small writes like the formatter, it produces a crazy amount of
  callbacks: one styled HTML page invoked the callback ~50,000 times in a
  benchmark lol. This has a particularly large impact on callers who are
  supplying callbacks through an expensive FFI interface, like Go.
  
  Change WriterAdapter to have an optional buffer (initBuffered) and use a
  4 KB buffer for all current callers. Also optimize single byte splats to
  use memset.
  
  Results: that same styled HTML example goes from ~50K callbacks to 124.
  And throughput through the C API also improved across every workload I
  tested (styled and unstyled text in every format).
  ```
- [`7c4c7ad`](https://github.com/ghostty-org/ghostty/commit/7c4c7adadc8b080ab168ed0af48319185dcbd2ba) pkg/wuffs: use C-only mirror of wuffs ([@jcollie](https://github.com/jcollie))
  ```text
  This prevents us from pulling in test images that trigger some anti-virus
  scanners. It's also smaller since it only has the necessary bits that we need.
  
  This also updates to the latest release: 0.4.0-alpha.10.
  ```
- [`6cadad0`](https://github.com/ghostty-org/ghostty/commit/6cadad06f468745651a6bb53e64d31cc8fae9e24) termio: preserve UTF-8 in desktop notification truncation ([@dolzenko](https://github.com/dolzenko))
- [`ae6d97e`](https://github.com/ghostty-org/ghostty/commit/ae6d97ea71b8ad4bb0d3837cc807d6ae097d4145) termio: avoid rescanning UTF-8 prefixes ([@dolzenko](https://github.com/dolzenko))
- [`53c6fdb`](https://github.com/ghostty-org/ghostty/commit/53c6fdbe7d53eb8c61f7af5e311d04956c4fe283) apprt: own desktop notification truncation ([@dolzenko](https://github.com/dolzenko))
  ```text
  Make the fixed-size desktop notification payload a named Message type and initialize it through a constructor.
  
  Keeping UTF-8 boundary truncation with the payload owns the buffer capacities and sentinel termination at the message boundary, while stream_handler only forwards the title and body.
  ```
- [`5c952ac`](https://github.com/ghostty-org/ghostty/commit/5c952ac977b30f3e4e01417827d4d7745015f50c) macos: simplify command palette sort keys ([@jparise](https://github.com/jparise))
  ```text
  Store the Comparable ObjectIdentifier directly instead of wrapping the
  only sort key type in AnySortKey.
  
  The expected deterministic ordering of equal terminal command titles is
  also now verified by a unit test.
  ```
- [`997a2af`](https://github.com/ghostty-org/ghostty/commit/997a2aff2afce88cdf5fa7a3d5dca047c0d65254) terminal: preserve pending wrap in VT formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, formatting a cursor at the right edge emitted CUP, which
  cleared pending wrap. Replayed output then overwrote the edge cell
  instead of wrapping before the next printable character.
  
  When pending wrap is set, move to and reformat the final cell to restore
  the flag through normal VT behavior. Emit cursor pen state afterward and
  cover replay plus pin-map behavior with a regression test.
  ```
- [`0073976`](https://github.com/ghostty-org/ghostty/commit/00739762316a0ad05c7d412705b5f6111bae3288) terminal: preserve pending wrap in VT formatter ([#13876](https://github.com/ghostty-org/ghostty/issues/13876)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, formatting a cursor at the right edge emitted CUP, which
  cleared pending wrap. Replayed output then overwrote the edge cell
  instead of wrapping before the next printable character.
  
  When pending wrap is set, move to and reformat the final cell to restore
  the flag through normal VT behavior. Emit cursor pen state afterward and
  cover replay plus pin-map behavior with a regression test.
  ```
- [`4816afc`](https://github.com/ghostty-org/ghostty/commit/4816afc74201c4a8170223fb43e7e6fdbaa34a0a) macos: simplify command palette sort keys ([#13872](https://github.com/ghostty-org/ghostty/issues/13872)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Store the Comparable ObjectIdentifier directly instead of wrapping the
  only sort key type in AnySortKey.
  
  The expected deterministic ordering of equal terminal command titles is
  also now verified by a unit test.
  ```
- [`385a378`](https://github.com/ghostty-org/ghostty/commit/385a378fe58425482eb1df8ed614433e06b891de) termio: preserve UTF-8 in desktop notification truncation ([#13811](https://github.com/ghostty-org/ghostty/issues/13811)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - Prevent desktop notification title and body truncation from producing
  invalid UTF-8.
  - Truncate fixed-size buffers to the longest valid UTF-8 prefix.
  - Add regression tests for multibyte characters at the buffer boundary.
  
  Fixes #13795
  
  ## Testing
  
  - Confirmed the original reproducer produces `[Invalid UTF-8]` with the
  installed Ghostty.
  - Confirmed the patched Ghostty displays a valid, truncated
  notification.
  - Added tests covering both notification title and body truncation.
  
  ## AI Usage Disclosure
  
  I used OpenAI Codex to investigate the root cause, implement the fix and
  regression tests, run validation, and help prepare the issue and PR
  descriptions. I reviewed and understand the submitted change.
  ```
- [`159cf6d`](https://github.com/ghostty-org/ghostty/commit/159cf6d7e7fef0f477d400c3f801b9f02dbcfd19) pkg/wuffs: use C-only mirror of wuffs ([#13789](https://github.com/ghostty-org/ghostty/issues/13789)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prevents us from pulling in test images that trigger some
  anti-virus scanners. It's also smaller since it only has the necessary
  bits that we need.
  
  This also updates to the latest release: 0.4.0-alpha.10.
  ```
- [`1eceea9`](https://github.com/ghostty-org/ghostty/commit/1eceea92dac457f95858706f946be7d6b21e5885) i18n: Update ko_KR translations ([@dobbylee](https://github.com/dobbylee))
- [`f430905`](https://github.com/ghostty-org/ghostty/commit/f4309055fbb8cfd74bf0559a054e5eb7ddc361d8) macos: don't put 0x7F as text in key event ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13869
  
  We already checked `< 0x20` but missed `0x7F` which causes similar
  problems.
  ```
- [`6c30dc1`](https://github.com/ghostty-org/ghostty/commit/6c30dc1bfff7e22a9198931411ae862a6bb6277b) i18n: Update ko_KR translations ([#13815](https://github.com/ghostty-org/ghostty/issues/13815)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update all missing Korean translations for 1.4.
  
  Part of #13766
  ```
- [`2349e97`](https://github.com/ghostty-org/ghostty/commit/2349e974b866ae4d9a8c5193a885388ddd4f2b4b) inspector: remove obsolete detachable header helper ([@jparise](https://github.com/jparise))
  ```text
  Remove the unused, callback-based detachable header implementation. It
  supported the previous terminal inspector, which has since been deleted
  (fdbe4343c). The current inspector uses DetachableHeader directly.
  ```
- [`d19f8f7`](https://github.com/ghostty-org/ghostty/commit/d19f8f7f9d3204d37fd1c47f9b51f682238a8423) macos: remove unused hosting window helper ([@jparise](https://github.com/jparise))
  ```text
  Remove the unused SwiftUI environment key intended to expose a hosting
  window. Nothing sets or reads the value.
  ```
- [`c8980b8`](https://github.com/ghostty-org/ghostty/commit/c8980b853b5e822509946c7c62188fe549731376) macos: don't put 0x7F as text in key event ([#13871](https://github.com/ghostty-org/ghostty/issues/13871)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13869
  
  We already checked `< 0x20` but missed `0x7F` which causes similar
  problems.
  ```
- [`924c8a9`](https://github.com/ghostty-org/ghostty/commit/924c8a90ded98fb643def9d7b814efa55e590298) libghostty: C api to stream formatter output through a GhosttyWriter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `ghostty_formatter_format` which uses a streaming GhosttyWriter
  type to write. Update the example to show this.
  ```
- [`0baa0fd`](https://github.com/ghostty-org/ghostty/commit/0baa0fd545365d388922d37370c4da2412aa4ace) inspector: remove obsolete detachable header helper ([#13874](https://github.com/ghostty-org/ghostty/issues/13874)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the unused, callback-based detachable header implementation. It
  supported the previous terminal inspector, which has since been deleted
  (fdbe4343c). The current inspector uses DetachableHeader directly.
  ```
- [`faaf07e`](https://github.com/ghostty-org/ghostty/commit/faaf07e7c001e24e0bd725cc1bb3cb899815d53b) macos: remove unused hosting window helper ([#13873](https://github.com/ghostty-org/ghostty/issues/13873)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the unused SwiftUI environment key intended to expose a hosting
  window. Nothing sets or reads the value.
  ```
- [`ee57b94`](https://github.com/ghostty-org/ghostty/commit/ee57b94170ab5261315cb9345eb67663e8d1908c) libghostty: C api to stream formatter output through a GhosttyWriter ([#13875](https://github.com/ghostty-org/ghostty/issues/13875)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `ghostty_formatter_format` which uses a streaming GhosttyWriter type
  to write. Update the example to show this.
  ```
- [`3924a32`](https://github.com/ghostty-org/ghostty/commit/3924a3255686b2b646d2ee8730ad5528f4542a26) Update VOUCHED list ([#13870](https://github.com/ghostty-org/ghostty/issues/13870)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13838#discussioncomment-18052745)
  from @mitchellh.
  
  Vouch: @basteez
  ```
- [`e2662d7`](https://github.com/ghostty-org/ghostty/commit/e2662d7b63d4aee02f31164c96c180ebed8ddf0b) i18n: translate v1.4 command palette and remaining strings (be) ([@iweuhi2kjrnkw](https://github.com/iweuhi2kjrnkw))
- [`820ed68`](https://github.com/ghostty-org/ghostty/commit/820ed688efa5b914c2779449f260d369caca0b2c) i18n(be): fix translation issues per review ([@iweuhi2kjrnkw](https://github.com/iweuhi2kjrnkw))
  ```text
  - Drop redundant 'было' copula with short-form participles (lines 1767, 1769)
  - Use short predicative form 'недаступна' (line 1780)
  - 'у двух фарматах:' instead of dash-construction (line 156)
  - 'Аднавіць' instead of 'Паўтарыць' for Redo (semantic pair with Undo)
  - Fix 'у' → 'ў' after 'ANSI' (7 places)
  - Align label/description wording for Split Zoom, Read-Only, Float on Top, Secure Input
  - 'усе акны' instead of 'усе вокны' (consistent with 'акно')
  - 'калі яна ёсць' instead of 'даступная' (if present ≠ available)
  - Infinitive 'Дадаць' instead of imperative 'Дадайце'
  ```
- [`b97b17f`](https://github.com/ghostty-org/ghostty/commit/b97b17f06b1ffd694f80edd3df5dd2134a0bcb9e) i18n: translate v1.4 strings (be) ([#13771](https://github.com/ghostty-org/ghostty/issues/13771)) ([@trag1c](https://github.com/trag1c))
  ```text
  Continues the Belarusian (`be`) translation for v1.4 per #13766.
  Translates the remaining 181 strings (mostly the newly-localized command
  palette), bringing `be` to 253/253.
  ```
- [`492c260`](https://github.com/ghostty-org/ghostty/commit/492c26067c9f342f46507ade392cfad2e1400360) libghostty: use custom memory pool for Wasm ([@mitchellh](https://github.com/mitchellh))
  ```text
  A custom memory pool for Wasm that grows by exactly one item size per
  growth and shares the pool across the entire Wasm-module instead of
  per-terminal.
  
  Some background on why `std.heap.MemoryPool` is considered harmful for
  WebAssembly:
  
  First, the std.heap.MemoryPool grows 1.5x at each growth point. The backing
  allocator for that is usually a GPA which is the BrkAllocator for wasm.
  This grows by power-of-two big-allocation slots. If you pair these together
  you get a massive permanent linear memory growth. On non-wasm targets,
  this doesn't matter because these are virtual memory mappings that don't
  cost physical memory, but wasm doesn't work that way.
  
  Second, we were using one pool per terminal. On wasm, this meant that
  we paid for the free list N times. On non-wasm, this makes sense because
  the synchronization overhead has so far been measurable enough under
  load to be prohibitive (although, I'm still skeptical about this and want
  to look into it). On wasm, we build single-threaded modules, so we can use
  a global free list without any extra overhead.
  
  ## Benchmarks
  
  80x24 terminal with 1000-line scrollack processing 16MB of plain ASCII.
  
  | Scenario                        |    Before |     After |
  | ------------------------------- | --------: | --------: |
  | Fresh instance                  |  0.56 MiB |  0.56 MiB |
  | First `terminal_new` (delta)    | +3.44 MiB | +0.88 MiB |
  | One filled terminal (total)     |  4.00 MiB |  1.88 MiB |
  | Each additional filled terminal | +3.00 MiB | +0.44 MiB |
  | 5 filled terminals (total)      | 16.00 MiB |  4.06 MiB |
  
  Throughput numbers are unchanged on wasm and native (to be expected in
  the latter because this is all gated on wasm).
  ```
- [`e9db8d2`](https://github.com/ghostty-org/ghostty/commit/e9db8d2b0b827be035ab75658ea9faf4f0f56d3f) libghostty: use custom memory pool for Wasm, reduce terminal memory by ~75% ([#13865](https://github.com/ghostty-org/ghostty/issues/13865)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A custom memory pool for Wasm that grows by exactly one item size per
  growth and shares the pool across the entire Wasm-module instead of
  per-terminal.
  
  Some background on why `std.heap.MemoryPool` is considered harmful for
  WebAssembly:
  
  First, the std.heap.MemoryPool grows 1.5x at each growth point. The
  backing allocator for that is usually a GPA which is the BrkAllocator
  for wasm. This grows by power-of-two big-allocation slots. If you pair
  these together you get a massive permanent linear memory growth.
  
  On non-wasm targets, the memory growth doesn't matter because these are
  virtual memory mappings that don't cost physical memory, but wasm
  doesn't work that way. Also on native targets, the syscalls to allocate
  memory are very expensive (relatively), so it makes sense to allocate
  large virtual memory chunks and avoid them. Again, wasm doesn't work
  this way.
  
  Second, we were using one pool per terminal. On wasm, this meant that we
  paid for the free list N times. On non-wasm, this makes sense because
  the synchronization overhead has so far been measurable enough under
  load to be prohibitive (although, I'm still skeptical about this and
  want to look into it). On wasm, we build single-threaded modules, so we
  can use a global free list without any extra overhead.
  
  ## Benchmarks
  
  80x24 terminal with 1000-line scrollack processing 16MB of plain ASCII.
  
  | Scenario                        |    Before |     After |
  | ------------------------------- | --------: | --------: |
  | Fresh instance                  |  0.56 MiB |  0.56 MiB |
  | First `terminal_new` (delta)    | +3.44 MiB | +0.88 MiB |
  | One filled terminal (total)     |  4.00 MiB |  1.88 MiB |
  | Each additional filled terminal | +3.00 MiB | +0.44 MiB |
  | 5 filled terminals (total)      | 16.00 MiB |  4.06 MiB |
  
  Throughput numbers are unchanged on wasm and native (to be expected in
  the latter because this is all gated on
  wasm).
  
  Note I'm still very much optimizing the above numbers! This is just my
  first big win.
  
  **AI usage:** None used except to validate and judge.
  ```
- [`5364e51`](https://github.com/ghostty-org/ghostty/commit/5364e5158f171e4d87fdfa43d0fffebc0c3775fa) libghostty: reduce Wasm stack reservation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig default's Wasm stacks to 1MB. Change it to 128 KB instead.
  
  This removes 896 KiB from every Wasm instance's initial linear memory
  reservation. That means that simply _loading_ `ghostty-vt.wasm` is down
  this much.
  
  Through various workload benchmarks of real terminal snapshots,
  artificial worst case full ascii, full styled, full emoji, full mixed,
  etc. workloads, I wasn't able to get a stack to go above 17 KB, so 128 KB
  is VERY generous. Lets start here.
  ```
- [`8d70c5d`](https://github.com/ghostty-org/ghostty/commit/8d70c5dca0346dcba94f8812547ff325e62bc340) libghostty: reduce Wasm stack reservation ([#13864](https://github.com/ghostty-org/ghostty/issues/13864)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig default's Wasm stacks to 1MB. Change it to 128 KB instead.
  
  This removes 896 KiB from every Wasm instance's initial linear memory
  reservation. That means that simply _loading_ `ghostty-vt.wasm` is down
  this much.
  
  Through various workload benchmarks of real terminal snapshots,
  artificial worst case full ascii, full styled, full emoji, full mixed,
  etc. workloads, I wasn't able to get a stack to go above 17 KB, so 128
  KB is VERY generous. Lets start here.
  ```
- [`7a96643`](https://github.com/ghostty-org/ghostty/commit/7a966438fcf5b3b209bb754b67155d34ae93b217) build(deps): bump cachix/install-nix-action from 31.11.0 to 31.11.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.0 to 31.11.1.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/630ae543ea3a38a9a4166f03376c02c50f408342...13d8dd58da0234aa297dedd986986ccb8e7f3e24)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`9a770be`](https://github.com/ghostty-org/ghostty/commit/9a770be61c39757cdb1a0d7670b8265100d3b2a6) build(deps): bump cachix/install-nix-action from 31.11.0 to 31.11.1 ([#13863](https://github.com/ghostty-org/ghostty/issues/13863)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.0 to 31.11.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.1 -&gt; 2.35.2 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/281">cachix/install-nix-action#281</a>
  Fixes a crash (<a
  href="https://redirect.github.com/NixOS/nix/issues/16005"><code>Assertion
  '!awake.empty()' failed</code></a>) that could abort builds.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.0...v31.11.1">https://github.com/cachix/install-nix-action/compare/v31.11.0...v31.11.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/13d8dd58da0234aa297dedd986986ccb8e7f3e24"><code>13d8dd5</code></a>
  fix(ci): skip latest installer on x86_64-darwin</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/875018fe555aee647c21ea81888659240cd8e27b"><code>875018f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/281">#281</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/6624a11f6c07674a3ff71d2431865aecf3587190"><code>6624a11</code></a>
  nix: 2.35.1 -&gt; 2.35.2</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/630ae543ea3a38a9a4166f03376c02c50f408342...13d8dd58da0234aa297dedd986986ccb8e7f3e24">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.0&new-version=31.11.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## August 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31974789508), [2](https://github.com/ghostty-org/ghostty/actions/runs/31971580699), [3](https://github.com/ghostty-org/ghostty/actions/runs/31969954615), [4](https://github.com/ghostty-org/ghostty/actions/runs/31967572084), [5](https://github.com/ghostty-org/ghostty/actions/runs/31952071871), [6](https://github.com/ghostty-org/ghostty/actions/runs/31940439160), [7](https://github.com/ghostty-org/ghostty/actions/runs/31927071035), [8](https://github.com/ghostty-org/ghostty/actions/runs/31921652723)  
Summary: 8 runs • 27 commits • 7 authors

### Changes

- [`bd64703`](https://github.com/ghostty-org/ghostty/commit/bd647035e97da4aadfe1003877ecf64a3a655059) input: don't emit fallback text on key release ([@tsacha](https://github.com/tsacha))
  ```text
  Key events without a kitty entry fall back to writing their UTF-8 text
  directly. On GTK, keys whose unshifted keysym is a dead key or level 5
  latch have no unshifted codepoint and take this path. With event type
  reporting enabled, releases therefore emitted the same text as presses
  and duplicated characters in applications such as Neovim.
  
  Skip the raw text fallback for release events while retaining it for
  presses and repeats. Keep the guard in the shared encoder so release
  events for identified keys still retain the UTF-8 data used to derive
  alternate keys.
  
  Cover releases with and without report-all mode, and verify that repeat
  events continue to emit fallback text.
  ```
- [`29b82dd`](https://github.com/ghostty-org/ghostty/commit/29b82dd80c46de16f5aaa405e51b2148831e2061) config: preserve bytes in hex escapes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13855
  
  Make the config string parser preserve hexadecimal escapes as bytes.
  Previously all escaped values were encoded as Unicode codepoints.
  ```
- [`f8856a7`](https://github.com/ghostty-org/ghostty/commit/f8856a78a291193fbfab081a894d16fc21f4a42e) config: preserve bytes in hex escapes ([#13862](https://github.com/ghostty-org/ghostty/issues/13862)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13855
  
  Make the config string parser preserve hexadecimal escapes as bytes.
  Previously all escaped values were encoded as Unicode codepoints.
  ```
- [`602497e`](https://github.com/ghostty-org/ghostty/commit/602497e9b96c62b05c4c6418538192ad974e4326) input: skip text fallback for kitty key releases ([#13861](https://github.com/ghostty-org/ghostty/issues/13861)) ([@jcollie](https://github.com/jcollie))
  ```text
  Key events without a kitty entry fall back to writing their UTF-8 text
  directly. On GTK, keys whose unshifted keysym is a dead key or level 5
  latch have no unshifted codepoint and take this path. With event type
  reporting enabled, releases therefore emitted the same text as presses
  and duplicated characters in applications such as Neovim.
  
  Skip the raw text fallback for release events while retaining it for
  presses and repeats. Keep the guard in the shared encoder so release
  events for identified keys still retain the UTF-8 data used to derive
  alternate keys.
  
  Cover releases with and without report-all mode, and verify that repeat
  events continue to emit fallback text.
  
    - https://github.com/ghostty-org/ghostty/discussions/12192
    - https://github.com/ghostty-org/ghostty/discussions/12084
    - https://github.com/ghostty-org/ghostty/discussions/12433
    - https://github.com/ghostty-org/ghostty/discussions/13816
  
  ## Testing
  
    - `zig build test-lib-vt -Dtarget=x86_64-linux-gnu`
    - `zig build -Demit-lib-vt -Dtarget=x86_64-linux-gnu`
    - `zig build`
    - Verified the regression test fails without the release guard
  - Manually tested the GTK backend under Wayland/Sway and X11/XWayland,
  with the GTK simple input context and ibus 1.5.34:
      - Ergo-L `!` and `'`
      - Spanish `[`, `{`, `]`, and `}`
  - Presses, repeats, and both modifier-release orders in `nvim --clean`
      - Dead-key composition and cancellation
      - Unicode hexadecimal input
  - Full kitty keyboard mode with `kitty +kitten show_key -m kitty`,
  including composed text
  
  ## AI disclosure
  
  OpenAI Codex assisted with investigating the reports, reviewing the GTK
  and kitty input paths, extending the regression tests, running
  validation, and drafting this description. I reviewed the final code,
  edited this description, manually performed the tests listed above, and
  understand how the change interacts with the input encoder.
  ```
- [`f748b17`](https://github.com/ghostty-org/ghostty/commit/f748b17e27f5ee089494044179dea1c493ce63cc) feat: expand tildes in config theme path to HOME ([@preiter93](https://github.com/preiter93))
  ````text
  When loading a theme from a path that includes a tilde:
  ```
  theme="~/.cache/wal/colors-ghostty"
  ```
  currently fails with the following error:
  ```
  cannot include path separators unless it is an absolute path
  ```
  
  This PR tries to expand the ~ of the path. If there is no ~
  or expansion fails, it falls back to the unexpanded value.
  ````
- [`c121734`](https://github.com/ghostty-org/ghostty/commit/c1217342958b90ed3a25413c1616dfd2dd8cd1bf) move shell expand of theme from theme.zig to config.zig ([@preiter93](https://github.com/preiter93))
- [`37174c7`](https://github.com/ghostty-org/ghostty/commit/37174c73b0600cc3b2d8579fa7a210086ee3bbed) add helper and expand also if light/dark is specified ([@preiter93](https://github.com/preiter93))
- [`68a2008`](https://github.com/ghostty-org/ghostty/commit/68a2008b340959b2a94f27f37ca98257109f6396) fix: format ([@preiter93](https://github.com/preiter93))
- [`7557944`](https://github.com/ghostty-org/ghostty/commit/7557944b4f1fb9eebe451c636227a04e7a4a2704) feat: expand tildes in config theme path to HOME ([#13840](https://github.com/ghostty-org/ghostty/issues/13840)) ([@jcollie](https://github.com/jcollie))
  ````text
  When loading a theme from a path that includes a tilde:
  ```
  theme="~/.cache/wal/colors-ghostty"
  ```
  ghostty currently fails with the following error:
  ```
  cannot include path separators unless it is an absolute path
  ```
  
  This PR tries to expand the ~ of the path. If there is no ~ or expansion
  fails, it falls back to the unexpanded value.
  ````
- [`a8e9b41`](https://github.com/ghostty-org/ghostty/commit/a8e9b413f13cfeec77efd95c3ba9b4750fcbfada) libghostty: simplify Wasm allocation API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace a bunch of type-specific Wasm allocation functions with a generic
  byte allocator and reusable opaque out-parameters for pointers. This
  makes it a lot more ergonomic (relatively) to use the Wasm interface
  and removes a dozen or so exports.
  
  This also updates the `ghostty_type_json` `abi` field with a maximum
  alignment value that host sides can use to keep every allocation aligned
  properly, easily, without hardcoding numbers.
  
  This adds a test to verify this all works as intended and runs in CI.
  ```
- [`3790fb7`](https://github.com/ghostty-org/ghostty/commit/3790fb78fecb3577dee30c40efe1ced3e3f0d9a1) libghostty: simplify Wasm allocation API ([#13860](https://github.com/ghostty-org/ghostty/issues/13860)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace a bunch of type-specific Wasm allocation functions with a
  generic byte allocator and reusable opaque out-parameters for pointers.
  This makes it a lot more ergonomic (relatively) to use the Wasm
  interface and removes a dozen or so exports.
  
  This also updates the `ghostty_type_json` `abi` field with a maximum
  alignment value that host sides can use to keep every allocation aligned
  properly, easily, without hardcoding numbers.
  
  This adds a test to verify this all works as intended and runs in CI.
  ```
- [`7b57c0a`](https://github.com/ghostty-org/ghostty/commit/7b57c0a02942beb3217a751e6d26955e3c3c1d72) Update VOUCHED list ([#13859](https://github.com/ghostty-org/ghostty/issues/13859)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13858#discussioncomment-18043290)
  from @jcollie.
  
  Vouch: @tsacha
  ```
- [`9673a22`](https://github.com/ghostty-org/ghostty/commit/9673a22b01317ac6493240694a2451c8287253d1) libghostty: expand ABI type metadata ([@mitchellh](https://github.com/mitchellh))
  ```text
  The type metadata export only described extern struct layouts, leaving embedders to mirror enum values and tagged union relationships.
  
  Describe every public C type in a versioned manifest with target and build metadata. Keep union field renames alongside their source tagged unions so the manifest uses public C names without changing Zig value layouts.
  ```
- [`c755595`](https://github.com/ghostty-org/ghostty/commit/c75559589e41721ab5a3de8e336d8476f4290535) libghostty: add ABI manifest schema ([@mitchellh](https://github.com/mitchellh))
  ```text
  The ABI manifest previously had no machine-readable grammar or test that
  the public export conformed to it.
  
  Define a Draft 2020-12 schema and add a build check that executes
  ghostty_type_json for native and wasm libraries before validation. Run
  both forms in CI and publish the schema with the generated API docs.
  ```
- [`0e8b7be`](https://github.com/ghostty-org/ghostty/commit/0e8b7bea63ccf8b89d15a82bdaf6a9bb3fc8c43d) vt: expose packed cell layout ([@mitchellh](https://github.com/mitchellh))
  ```text
  GhosttyCell was exposed as a raw integer while its manifest entry was only an alias, forcing bulk-read consumers to duplicate the internal cell bit layout.\n\nAdd reflection helpers for packed structs and tagged unions, and keep the C-facing layout metadata next to Cell itself. Extend the ABI manifest and schema with recursive bit descriptors so every content arm, including palette and RGB backgrounds, can be decoded without hardcoded masks.\n\nDocument manifest-driven cell decoding and test the metadata against Zig reflection and real cell values.
  ```
- [`0ba6250`](https://github.com/ghostty-org/ghostty/commit/0ba6250388641f52135414b38c4259aa682c489b) libghostty: `ghostty_type_json` expanded with more metadata, every enum member, packed layouts, etc. ([#13856](https://github.com/ghostty-org/ghostty/issues/13856)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This PR makes `ghostty_type_json` contain more metadata necessary for
  FFI without access to the C header to produce safe, ABI compliant field
  access.
  
  The existing `ghostty_type_json` didn't expose enough information:
  embedders still had to hardcode enum values, tagged union values, and
  packed bit layouts. For wasm this meant copying offsets and masks from
  Zig internals and hoping they didn't drift. This isn't an ABI I want to
  promise.
  
  This also includes a formal JSON schema included in Doxygen docs and
  used in CI to continuously validate our output structure. I'd like to
  expand in the future comparing to actual C headers too.
  
  ## Examples
  
  ### Named References, Arrays
  
  ```json
  "GhosttyRenderStateColors": {
    "kind": "struct",
    "size": 792,
    "align": 8,
    "fields": {
      "background": {
        "offset": 8,
        "size": 3,
        "type": "GhosttyColorRgb"
      },
      "palette": {
        "offset": 18,
        "size": 768,
        "type": "array",
        "elem": "GhosttyColorRgb",
        "count": 256
      }
    }
  }
  ```
  
  ### Pointers
  
  ```json
  "GhosttyCellsView": {
    "kind": "struct",
    "size": 16,
    "align": 8,
    "fields": {
      "ptr": {
        "offset": 0,
        "size": 8,
        "type": "pointer",
        "elem": "GhosttyCell",
        "const": true,
        "nullable": true
      },
      "len": {
        "offset": 8,
        "size": 8,
        "type": "u64"
      }
    }
  }
  ```
  
  ### Enums
  
  ```json
  "GhosttyStyleColorTag": {
    "kind": "enum",
    "size": 4,
    "align": 4,
    "underlying": "i32",
    "prefix": "GHOSTTY_STYLE_COLOR_",
    "values": {
      "NONE": 0,
      "PALETTE": 1,
      "RGB": 2,
      "TAG_MAX_VALUE": 2147483647
    }
  }
  ```
  
  ### Packed Struct
  
  ```json
  "GhosttyCell": {
    "kind": "packed",
    "size": 8,
    "align": 8,
    "underlying": "u64",
    "bits": {
      "content_tag": {
        "lsb": 0,
        "width": 2,
        "type": "GhosttyCellContentTag"
      },
      "content": {
        "lsb": 2,
        "width": 24,
        "kind": "union",
        "tag": "content_tag",
        "arms": {
          "BG_COLOR_RGB": {
            "kind": "packed",
            "width": 24,
            "bits": {
              "r": {"lsb": 0, "width": 8, "type": "u8"},
              "g": {"lsb": 8, "width": 8, "type": "u8"},
              "b": {"lsb": 16, "width": 8, "type": "u8"}
            }
          }
        }
      }
    }
  }
  ```
  ````
- [`aa25679`](https://github.com/ghostty-org/ghostty/commit/aa25679da8c87b47e9b45410435bded87e283031) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`d7f782d`](https://github.com/ghostty-org/ghostty/commit/d7f782dbcc4471eb697cce0ce888c83787ca38f0) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`7c1d0d4`](https://github.com/ghostty-org/ghostty/commit/7c1d0d414c4bfd976c6ae422f170a4b6249716d5) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
  ```text
  Removed translation for opening config file with default editor.
  ```
- [`06b63c4`](https://github.com/ghostty-org/ghostty/commit/06b63c48594ea04d2a68dd8249250d1477722296) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`26df373`](https://github.com/ghostty-org/ghostty/commit/26df373ec83fb1cebb4fee0a8394144ae984a9b8) i18n: update Hebrew translations for v1.4 ([#13785](https://github.com/ghostty-org/ghostty/issues/13785)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update the Hebrew translations in po/he.po with the 181 new strings for
  v1.4, as requested in issue #13766 :)
  ```
- [`b4079f0`](https://github.com/ghostty-org/ghostty/commit/b4079f00c8946207e4db8571e3209f2de7ac4a27) libghostty: add render state structured cursor read ([@mitchellh](https://github.com/mitchellh))
  ```text
  A normal renderer would have to call `ghostty_render_state_get`
  _eight times_ to reconstruct the cursor. In languages where FFI is
  expensive (Go, wasm, etc.), this showed up in profiles of every frame.
  
  Add a sized cursor snapshot and expose it. Also expose the existing color
  snapshot through ghostty_render_state_get and remove the older
  dedicated color getter.
  ```
- [`0d37f2d`](https://github.com/ghostty-org/ghostty/commit/0d37f2d34dabd6bc6f7cf094e0d6466186b8c783) libghostty: add dedicated dirty row iteration + clear functions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add render state C APIs for iterating only rows that require a redraw
  and for marking a completed frame clean in one call.
  
  A one-row update in a 24-row viewport reduces dirty-row discovery from
  50 calls to two, while cleanup becomes one call instead of O(N) of rows.
  
  This lower call count is massive for environments where FFI is expensive
  (Go, wasm).
  
  The dirty next API outputs the viewport y because it jumps, unlike the
  normal sequential next where its trivial for a caller to keep track.
  ```
- [`16c833c`](https://github.com/ghostty-org/ghostty/commit/16c833c5f1ffa9511909199ef1fab389493be1ef) libghostty: add render state structured cursor read ([#13851](https://github.com/ghostty-org/ghostty/issues/13851)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A normal renderer would have to call `ghostty_render_state_get` _eight
  times_ to reconstruct the cursor. In languages where FFI is expensive
  (Go, wasm, etc.), this showed up in profiles of every frame.
  
  Add a sized cursor snapshot and expose it. Also expose the existing
  color snapshot through ghostty_render_state_get and remove the older
  dedicated color getter.
  
  Found during my normal Go/wasm adventures.
  ```
- [`ad6e72d`](https://github.com/ghostty-org/ghostty/commit/ad6e72ddc4e9e259c9b70bff6e2b389e0ce91949) libghostty: add dedicated dirty row iteration + clear functions ([#13852](https://github.com/ghostty-org/ghostty/issues/13852)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add render state C APIs for iterating only rows that require a redraw
  and for marking a completed frame clean in one call.
  
  A one-row update in a 24-row viewport reduces dirty-row discovery from
  50 calls to two, while cleanup becomes one call instead of O(N) of rows.
  
  This lower call count is massive for environments where FFI is expensive
  (Go, wasm).
  
  The dirty next API outputs the viewport y because it jumps, unlike the
  normal sequential next where its trivial for a caller to keep track.
  ```
- [`f2897f3`](https://github.com/ghostty-org/ghostty/commit/f2897f31dec839352302369b3cb8009c4cec180b) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`02436fd`](https://github.com/ghostty-org/ghostty/commit/02436fd4eb0fca179f6d58717e9bc7a0ce106272) Update iTerm2 colorschemes ([#13850](https://github.com/ghostty-org/ghostty/issues/13850)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260810-152212-0173c3c
  ```

## August 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31910656085), [2](https://github.com/ghostty-org/ghostty/actions/runs/31894663124), [3](https://github.com/ghostty-org/ghostty/actions/runs/31890031839), [4](https://github.com/ghostty-org/ghostty/actions/runs/31876969328), [5](https://github.com/ghostty-org/ghostty/actions/runs/31868500752), [6](https://github.com/ghostty-org/ghostty/actions/runs/31865684095), [7](https://github.com/ghostty-org/ghostty/actions/runs/31864664855), [8](https://github.com/ghostty-org/ghostty/actions/runs/31862777169)  
Summary: 8 runs • 30 commits • 6 authors

### Changes

- [`ecbeb60`](https://github.com/ghostty-org/ghostty/commit/ecbeb60ca5327186301900ccef208143ff46ef22) macos: send all insertText commits as key events ([@sghng](https://github.com/sghng))
  ```text
  Previously, insertText commits without marked text were delivered via
  sendText, which applies paste semantics and wraps the text in bracketed
  paste when the program enables it. macOS dictation and other input
  methods often commit without marked text, so programs treated dictated
  text as a paste and applied paste-specific handling.
  
  insertText is only invoked by input methods (IME, dictation, emoji
  picker, character viewer); real paste operations use a separate path.
  Send every non-empty commit through the key event path so programs
  interpret input method text as typed input. Typing is unaffected (the
  accumulator path returns earlier) and Cmd+V pastes are unaffected.
  
  The helper is renamed from committedPreeditTextAction to
  committedTextAction since it no longer only handles preedit commits.
  ```
- [`fff9f62`](https://github.com/ghostty-org/ghostty/commit/fff9f62f38cfef56ada5239ea22555b35c1e063c) cli: always install embedded SSH terminfo ([@jparise](https://github.com/jparise))
  ```text
  Remove the remote infocmp short-circuit from +ssh setup. The command
  already sends Ghostty's embedded terminfo source to tic, so accepting
  any existing entry leaves the payload unused and can preserve stale
  data.
  ```
- [`69b9abf`](https://github.com/ghostty-org/ghostty/commit/69b9abf09ebad2b11a6850a28271676f6bfeb108) cli: version SSH terminfo cache entries ([@jparise](https://github.com/jparise))
  ```text
  Derive a version from the encoded Ghostty terminfo and require callers
  to pass it explicitly when reading or writing the SSH cache. Cache
  entries created for older or different payloads no longer suppress a
  required installation.
  ```
- [`36d8e3f`](https://github.com/ghostty-org/ghostty/commit/36d8e3f77779939a4413ddcd72c05ab08aeae57d) terminal/snapshot: slicing-by-16 software CRC32C ([@mitchellh](https://github.com/mitchellh))
  ```text
  The software CRC32C fallback (WebAssembly and any other target without a
  dedicated instruction) was the std byte-at-a-time table walk, which
  profiled at ~65% of snapshot encode and ~70% of decode self-time in V8.
  Replace it with slicing-by-16: sixteen bytes fold per iteration through
  comptime per-position tables, so the serial dependency advances one block
  at a time instead of one byte.
  
  The hardware backends (aarch64 CRC, x86_64 SSE4.2) are unchanged, so
  native is expected to be unaffected; its deltas below are run-to-run
  noise.
  
  Benchmarks: wasm is V8 (node 25), ReleaseFast + wasm-opt -O3, 80x24
  terminal, 2 MiB VT corpus per workload, complete snapshot including
  scrollback, best-of-5. Native is aarch64 macOS, hyperfine mean,
  ghostty-bench +terminal-snapshot --loops=20. "base" is the parent commit.
  
  | wasm      | encode base | encode   | decode base | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     7.07 ms |  3.43 ms |     6.45 ms |  2.81 ms |
  | styled    |    10.54 ms |  3.14 ms |    14.37 ms |  7.12 ms |
  | truecolor |    15.23 ms |  5.33 ms |    21.76 ms | 12.11 ms |
  | cjk       |    25.41 ms |  5.95 ms |    30.83 ms | 12.04 ms |
  | grapheme  |    27.67 ms | 14.18 ms |    27.00 ms | 13.16 ms |
  
  | native | mode   | base    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 40.6 ms | 41.7 ms |
  | ascii  | decode | 51.2 ms | 53.2 ms |
  | utf8   | encode | 45.2 ms | 47.2 ms |
  | utf8   | decode | 59.8 ms | 61.6 ms |
  ```
- [`c1a61fd`](https://github.com/ghostty-org/ghostty/commit/c1a61fddda00e907c7e66bd3609d6c558cccd26d) terminal/snapshot: borrow fully buffered record payloads ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the record source already has the complete payload buffered — always
  the case for in-memory snapshots such as ghostty_snapshot_decoder_new_buf
  — the record reader now borrows the payload straight out of the source
  buffer instead of streaming it through the limited and hashing reader
  adapters. Payload decoders parse a fixed reader over the borrowed bytes,
  `finish` validates the CRC with a single bulk update, and the source
  advances only after validation.
  
  The page decoder takes a matching fast path: a fully buffered payload is
  parsed in place, skipping the staging allocation and copy it previously
  made per PAGE record. Streaming sources are unchanged.
  
  This is a modest win on its own; it is also the foundation for later
  commits whose buffered fast paths rely on the payload being contiguous.
  
  Benchmarks (see the first commit in this series for methodology; "prev"
  is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     3.43 ms |  3.50 ms |     2.81 ms |  2.68 ms |
  | styled    |     3.14 ms |  3.15 ms |     7.12 ms |  7.04 ms |
  | truecolor |     5.33 ms |  5.27 ms |    12.11 ms | 12.04 ms |
  | cjk       |     5.95 ms |  5.92 ms |    12.04 ms | 11.89 ms |
  | grapheme  |    14.18 ms | 14.33 ms |    13.16 ms | 13.14 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 41.7 ms | 41.8 ms |
  | ascii  | decode | 53.2 ms | 52.4 ms |
  | utf8   | encode | 47.2 ms | 47.4 ms |
  | utf8   | decode | 61.6 ms | 61.2 ms |
  ```
- [`973f619`](https://github.com/ghostty-org/ghostty/commit/973f619a2371c50fffb2062bd59a0c5134c783b1) terminal/snapshot: vectorize grid row encoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Row encoding previously made two scalar passes over every row (a backward
  scan for the encoded cell count and a validation pass accumulating the
  width-selection OR), then wrote a 3-byte header and per-width chunked
  cells through separate writer calls.
  
  Three changes, all bulk-codec only with the portable path unchanged:
  
    - scanRow computes the count and word-OR in @Vector(4, u64) strides.
      Trailing default cells are all-zero words, so the OR over the whole
      row equals the OR over the encoded prefix.
    - The per-cell wide-pair validation loop is skipped entirely when the
      OR carries no wide bits, which is every row of plain text.
    - Rows are emitted with a single reservation in the destination's spare
      buffer capacity (header plus cells, no writer calls), using explicit
      i8x16.shuffle truncation for the 1/2/4-byte cell widths. Zig 0.16
      disables loop auto-vectorization, so the previous "vectorizable"
      truncating loop was actually scalar. Destinations without buffered
      capacity (counting writers, a still-growing scratch) fall through to
      the streaming path.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     3.50 ms |  2.09 ms |     2.68 ms |  2.67 ms |
  | styled    |     3.15 ms |  2.23 ms |     7.04 ms |  7.00 ms |
  | truecolor |     5.27 ms |  4.95 ms |    12.04 ms | 11.85 ms |
  | cjk       |     5.92 ms |  6.03 ms |    11.89 ms | 11.67 ms |
  | grapheme  |    14.33 ms | 13.08 ms |    13.14 ms | 13.28 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 41.8 ms | 24.5 ms |
  | ascii  | decode | 52.4 ms | 53.4 ms |
  | utf8   | encode | 47.4 ms | 47.6 ms |
  | utf8   | decode | 61.2 ms | 60.9 ms |
  ```
- [`593762c`](https://github.com/ghostty-org/ghostty/commit/593762cfa11afdd3eaefc9e0bdd9d979d85ab39f) terminal/snapshot: batch grapheme suffix codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Grapheme suffix encoding made two full passes over the grid (a counting
  pass, then an emit pass) and issued three writer calls per entry plus one
  per codepoint. Every grapheme cell owns exactly one entry in the page's
  grapheme map, so the section count now comes straight from
  page.graphemeCount() with no counting pass, and entries are batched
  through a 4 KB buffer with one writer call per flush. The per-entry size
  check moved into the emit loop; an error still cancels the whole record
  before any of it is emitted, so error behavior is unchanged.
  
  Decoding similarly parsed entry headers and codepoints with one reader
  call per integer. Fully buffered payloads (the common case after the
  borrowed-payload commit) now parse entry headers and codepoint runs
  directly from the buffered bytes, and entries whose target cell cannot
  carry a suffix discard their codepoints in bulk.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.09 ms |  2.07 ms |     2.67 ms |  2.69 ms |
  | styled    |     2.23 ms |  2.29 ms |     7.00 ms |  7.06 ms |
  | truecolor |     4.95 ms |  4.91 ms |    11.85 ms | 11.99 ms |
  | cjk       |     6.03 ms |  6.14 ms |    11.67 ms | 11.83 ms |
  | grapheme  |    13.08 ms |  8.26 ms |    13.28 ms | 11.18 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.5 ms | 24.3 ms |
  | ascii  | decode | 53.4 ms | 50.9 ms |
  | utf8   | encode | 47.6 ms | 41.2 ms |
  | utf8   | decode | 60.9 ms | 59.5 ms |
  ```
- [`2aaad3c`](https://github.com/ghostty-org/ghostty/commit/2aaad3ca99a27d36eff57d6e59e2044005ef2ba4) terminal/snapshot: vectorize grid cell decoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoding one- and two-byte cells widened them to their 8-byte words one
  scalar store at a time. The bulk codec now widens sixteen transported
  bytes per step with byte shuffles against a zero vector, degrading
  width-two surrogate lanes to U+FFFD with a vector select, exactly
  matching the scalar path. Short row tails reprocess the final full
  window with overlapping stores that rewrite identical bytes.
  
  This is a native win: the shuffles lower to NEON and take ascii decode
  from 38.9 ms to 34.0 ms (measured by toggling this path at the tip of
  this series). On wasm, V8 runs the scalar fallback at the same speed as
  the shuffle version — the loop is store-bound either way — so the wasm
  deltas below are flat.
  
  Row decoding also drops per-field packed-struct read-modify-writes in
  favor of one load and one store per row header, and rows that are fully
  default (zero header byte, zero encoded cells) skip all work: decoded
  pages start zeroed, which is exactly the default row and cell state.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.07 ms |  2.18 ms |     2.69 ms |  2.68 ms |
  | styled    |     2.29 ms |  2.28 ms |     7.06 ms |  6.93 ms |
  | truecolor |     4.91 ms |  4.93 ms |    11.99 ms | 11.91 ms |
  | cjk       |     6.14 ms |  6.11 ms |    11.83 ms | 11.72 ms |
  | grapheme  |     8.26 ms |  8.28 ms |    11.18 ms | 11.38 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.3 ms | 24.3 ms |
  | ascii  | decode | 50.9 ms | 46.7 ms |
  | utf8   | encode | 41.2 ms | 41.0 ms |
  | utf8   | decode | 59.5 ms | 59.5 ms |
  ```
- [`7c1014e`](https://github.com/ghostty-org/ghostty/commit/7c1014ef662cd4e9b968b5bac6ca062fa17a3b56) terminal/snapshot: resolve wide pairs in a per-row pass ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cell decoding ran wide-pair normalization inline for every decoded cell:
  two neighbor loads and a switch per cell, even though the overwhelming
  majority of rows contain no wide cells at all. Normalization is defined
  against already-stored predecessors, so running it as an ordered pass
  over the stored row afterward is exactly equivalent to interleaving it.
  
  The word-cell decoders now accumulate the bitwise OR of the row's wire
  words as they apply cells, and the pass is gated on it: rows without
  wide bits are already normalized (every cell narrow), and width-four and
  narrower transports cannot encode wide bits at all, so their rows skip
  the check at comptime. That removes the per-cell neighbor traffic from
  all styled text, which decodes through the four-byte width.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.18 ms |  2.06 ms |     2.68 ms |  2.70 ms |
  | styled    |     2.28 ms |  2.41 ms |     6.93 ms |  6.56 ms |
  | truecolor |     4.93 ms |  5.02 ms |    11.91 ms | 11.86 ms |
  | cjk       |     6.11 ms |  6.03 ms |    11.72 ms | 11.60 ms |
  | grapheme  |     8.28 ms |  8.36 ms |    11.38 ms | 11.39 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.3 ms | 25.6 ms |
  | ascii  | decode | 46.7 ms | 48.1 ms |
  | utf8   | encode | 41.0 ms | 41.7 ms |
  | utf8   | decode | 59.5 ms | 58.5 ms |
  ```
- [`47a5182`](https://github.com/ghostty-org/ghostty/commit/47a5182621e324f3351683ca2cc422562b3ff792) terminal/snapshot: skip remap tables for pages without styles ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoding a page allocated and zeroed two full remap tables (a 128 KB
  entries array plus an 8 KB seen bitmap each for styles and hyperlinks)
  even when the page declared no table entries at all, which is every page
  of plain scrollback. Empty tables now use a shared `.empty` remap that
  allocates nothing; `get` reads it as all-unmapped through a length check.
  Pages that do declare entries are unchanged.
  
  (Leaving the entries array unzeroed behind a seen-bitmap-gated `get` was
  also tried and measured no better than the plain memset, so the table
  keeps its simple zero-means-unmapped representation.)
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.06 ms |  2.13 ms |     2.70 ms |  2.54 ms |
  | styled    |     2.41 ms |  2.29 ms |     6.56 ms |  6.75 ms |
  | truecolor |     5.02 ms |  4.95 ms |    11.86 ms | 12.05 ms |
  | cjk       |     6.03 ms |  6.23 ms |    11.60 ms | 11.39 ms |
  | grapheme  |     8.36 ms |  8.72 ms |    11.39 ms | 11.27 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 25.6 ms | 24.4 ms |
  | ascii  | decode | 48.1 ms | 45.1 ms |
  | utf8   | encode | 41.7 ms | 41.9 ms |
  | utf8   | decode | 58.5 ms | 58.6 ms |
  ```
- [`1359973`](https://github.com/ghostty-org/ghostty/commit/1359973aefb37a9beaa2ec3e8f79df78290ea6f5) terminal/snapshot: single-pass style entry codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Style entries went through roughly five writer or reader vtable calls
  each: encode wrote three 4-byte colors and two u16s separately, and
  decode read 16 bytes into a stack buffer only to re-parse it through a
  nested fixed reader, one small read per field. Style-heavy pages carry
  hundreds of entries per page, so encode now assembles each entry in a
  16-byte buffer with a single write, and decode parses the fixed-size
  entry directly from a byte array. Entries additionally parse straight
  from the buffered payload (ID and value together) when it is contiguous.
  
  Inserting a decoded style also hashed twice: an explicit `lookup` before
  `add`, even though `add` already returns the existing entry for repeated
  values. Insert with `add` alone, taking one reference per accepted table
  entry, and surrender those references through the encoded-ID remap after
  grid decoding, the same scheme hyperlink entries already use. Refcount
  outcomes are identical: each distinct style nets its cell references.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.13 ms |  2.12 ms |     2.54 ms |  2.59 ms |
  | styled    |     2.29 ms |  2.23 ms |     6.75 ms |  6.43 ms |
  | truecolor |     4.95 ms |  3.44 ms |    12.05 ms |  8.35 ms |
  | cjk       |     6.23 ms |  5.99 ms |    11.39 ms | 11.39 ms |
  | grapheme  |     8.72 ms |  8.33 ms |    11.27 ms | 10.89 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.4 ms | 24.7 ms |
  | ascii  | decode | 45.1 ms | 47.5 ms |
  | utf8   | encode | 41.9 ms | 41.9 ms |
  | utf8   | decode | 58.6 ms | 58.8 ms |
  ```
- [`eb09bf8`](https://github.com/ghostty-org/ghostty/commit/eb09bf82918de51f22b805dc705ed67b2968b984) terminal/snapshot: interleave software CRC32C streams ([@mitchellh](https://github.com/mitchellh))
  ```text
  Slicing tables removed the byte-at-a-time dependency chain, but each
  16-byte fold still depends serially on the previous one, leaving the
  software CRC latency-bound at roughly 2.5-3 GB/s in V8 while snapshot
  payloads run through it once per direction. wasm has no carry-less
  multiply, so wider tables are the only classic escape — and measuring
  slicing-by-32 against interleaving showed the extra 16 KB of tables buys
  nothing once the chain is hidden.
  
  Instead, inputs of 4 KiB and up split into thirds processed as three
  independent fold chains in one loop, then merge with the GF(2) zero-shift
  operator: crc(A ++ B, s) = crc(B, 0) XOR zeroShift(crc(A, s), |B|). The
  shift matrices are comptime, storing only even powers of two (an odd
  power applies the preceding matrix twice), 4 KB total. Software CRC
  throughput roughly doubles; hardware backends are untouched, so native
  is unaffected (tables below are noise).
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.12 ms |  1.73 ms |     2.59 ms |  2.17 ms |
  | styled    |     2.23 ms |  1.47 ms |     6.43 ms |  5.38 ms |
  | truecolor |     3.44 ms |  2.30 ms |     8.35 ms |  7.17 ms |
  | cjk       |     5.99 ms |  3.89 ms |    11.39 ms |  9.50 ms |
  | grapheme  |     8.33 ms |  6.94 ms |    10.89 ms |  9.24 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.7 ms | 24.8 ms |
  | ascii  | decode | 47.5 ms | 49.2 ms |
  | utf8   | encode | 41.9 ms | 42.4 ms |
  | utf8   | decode | 58.8 ms | 59.5 ms |
  ```
- [`433b16b`](https://github.com/ghostty-org/ghostty/commit/433b16bcb1226a5d840318f88a1fb59e089b0649) terminal/apc: limit glyf decode allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocations made while decoding registered glyf
  outlines to 64 KB.
  
  Carefully crafted glyf outlines could expand into ~768KB of memory per
  glossary entry, which adds up to hundreds of MB per terminal surface.
  Across many terminals this could cause issues.
  
  The 64KB number was chosen by inspecting every glyph across Apple
  symbols and Noto emoji and the largest single glyph found was 40KB. So,
  64KB is generous while limiting each terminal to ~68MB of RAM for max
  glyph glossaries.
  ```
- [`746a11c`](https://github.com/ghostty-org/ghostty/commit/746a11c721a1cf31d2691008340c719bb0a84b03) libghostty: much faster terminal snapshot encode and decode for wasm ([#13848](https://github.com/ghostty-org/ghostty/issues/13848)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Snapshot encode is now 4-7x faster, decode is 3x faster for wasm builds.
  
  Snapshot decode is particularly important for wasm builds because
  libghostty is mainly used on web as a terminal _viewer_ and snapshots
  are the best, most efficient way to ship down full terminal state.
  
  The biggest change here is a totally custom software CRC32
  implementation, which accounted for ~70% of total decode time. Native
  builds on aarch64/x86_64 use dedicated hardware instructions that wasm
  doesn't have. We've written a custom CRC32 impl (verified against Zig
  stdlib through randomized unit tests) that goes from 0.3 GB/s to 5 GB/s
  throughput in V8.
  
  ## Benchmarks
  
  Wasm on V8:
  
  | Workload | Encode Before | Encode After | Speedup | Decode Before |
  Decode After | Speedup |
  |---|---|---|---|---|---|---|
  | ascii | 290 MB/s | 1182 MB/s | 4.1x | 318 MB/s | 946 MB/s | 3.0x |
  | styled (sgr16) | 387 MB/s | 2771 MB/s | 7.2x | 284 MB/s | 758 MB/s |
  2.7x |
  | sgr-truecolor | 361 MB/s | 2382 MB/s | 6.6x | 252 MB/s | 766 MB/s |
  3.0x |
  | cjk | 411 MB/s | 2686 MB/s | 6.5x | 339 MB/s | 1100 MB/s | 3.2x |
  | grapheme | 280 MB/s | 1117 MB/s | 4.0x | 287 MB/s | 839 MB/s | 2.9x |
  
  Native on aarch64:
  
  | Corpus | Mode | Before | After |
  |---|---|---|---|
  | ascii | encode | 40.6 ms | 24.8 ms |
  | ascii | decode | 51.2 ms | 49.2 ms |
  | utf8 | encode | 45.2 ms | 42.4 ms |
  | utf8 | decode | 59.8 ms | 59.5 ms |
  
  **AI usage:** Fable did everything here except write this PR and the
  comments. It also wrote the commit messages in this case. I reviewed
  everything.
  ```
- [`e524df6`](https://github.com/ghostty-org/ghostty/commit/e524df6c829ec11eccc88d1a01e1a7a0416d5454) terminal/apc: limit glyf decode allocations ([#13849](https://github.com/ghostty-org/ghostty/issues/13849)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocations made while decoding registered glyf
  outlines to 64 KB.
  
  Carefully crafted glyf outlines could expand into ~768KB of memory per
  glossary entry, which adds up to hundreds of MB per terminal surface.
  Across many terminals this could cause issues.
  
  The 64KB number was chosen by inspecting every glyph across Apple
  symbols and Noto emoji and the largest single glyph found was 40KB. So,
  64KB is generous while limiting each terminal to ~68MB of RAM for max
  glyph glossaries.
  
  AI was used only to write initial tests, I rewrote em.
  ```
- [`cbe8a0e`](https://github.com/ghostty-org/ghostty/commit/cbe8a0ed4eb27e1530bc8132e52a6c45c135332c) cli: keep cached SSH terminfo installs current ([#13844](https://github.com/ghostty-org/ghostty/issues/13844)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On a local cache miss, always send our embedded terminfo source to the
  remote `tic` instead of accepting any existing entry reported by
  `infocmp`.
  
  We also version cache entries using a content-derived hash of our
  embedded terminfo. Non-matching entries produce a cache miss and trigger
  (re)installation.
  ```
- [`9009122`](https://github.com/ghostty-org/ghostty/commit/9009122953f59d4900143aad587202a70c2136f4) macos: send all `insertText` commits as key events ([#13817](https://github.com/ghostty-org/ghostty/issues/13817)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Partially addresses #13796. Extends #13222.
  
  Previously, `insertText` commits without marked text were delivered via
  `sendText`, which applies paste semantics and wraps the text in
  bracketed
  paste when the program enables it. macOS dictation and other input
  methods often commit without marked text, so programs treated dictated
  text as a paste: opencode collapsed it into a `"[Pasted ~N lines]"` chip
  and Neovim applied paste-mode handling.
  
  `insertText` is only invoked by input methods (IME, dictation, emoji
  picker, character viewer); real paste operations use a separate path.
  Every non-empty commit is now sent as a key event — the same path
  already used for preedit commits since #13222 — so input method text
  always arrives as typed input.
  
  Typing is unaffected (the accumulator path returns earlier) and Cmd+V
  pastes are unaffected. `committedPreeditTextAction` is renamed to
  `committedTextAction` since it no longer only handles preedit commits.
  
  Testing:
  
  - 311 macOS unit tests pass.
  - Manually verified on macOS 26: dictation into Opencode and Neovim
    arrives inline with no paste handling; emoji picker inserts inline;
    Chinese IME composition unchanged; dictation in Neovim normal mode now
    behaves as keystrokes, matching Terminal.app.
  
  Notes:
  
  - Dictated "new line" now matches Terminal.app behavior (no newline
    with typed-text semantics). The previous behavior came from the paste
    path preserving the newline; a follow-up could deliver it as an
    Enter keypress if desired.
  
  AI usage: drafted with OMO + OpenCode + DeepSeek V4 Pro assistance;
  reviewed, edited, and manually tested by the author.
  ```
- [`cecf816`](https://github.com/ghostty-org/ghostty/commit/cecf81678e47f967b0354acada67e69d229f436b) Update VOUCHED list ([#13843](https://github.com/ghostty-org/ghostty/issues/13843)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13841#discussioncomment-18031969)
  from @jcollie.
  
  Vouch: @preiter93
  ```
- [`946422d`](https://github.com/ghostty-org/ghostty/commit/946422dbc5832bb1d8e3298e339c89577da86bca) terminal: replace std.fmt.parseFloat with custom fraction parsing ([@mitchellh](https://github.com/mitchellh))
  ```text
  We have exactly two callers of `parseFloat` and they both have very
  limited expect input shapes: values 0-1, simple decimals. parseFloat
  brings in ~26KB of binary size, so replace it with a custom parser for
  our exact shape.
  ```
- [`e3939d0`](https://github.com/ghostty-org/ghostty/commit/e3939d0f6224f2d9d16d030e7c1c04f082b0f39e) terminal: replace std.fmt.parseFloat with custom fraction parsing ([#13839](https://github.com/ghostty-org/ghostty/issues/13839)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We have exactly two callers of `parseFloat` and they both have very
  limited expect input shapes: values 0-1, simple decimals. parseFloat
  brings in ~26KB of binary size, so replace it with a custom parser for
  our exact shape.
  ```
- [`1d9fcdc`](https://github.com/ghostty-org/ghostty/commit/1d9fcdc151aedc72db1678e6e1df3425ed94939b) i18n: complete Kazakh (kk) translation for v1.4 ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
  ```text
  Translates the 180 remaining strings, mainly command palette entries
  introduced for v1.4 localization.
  ```
- [`034f584`](https://github.com/ghostty-org/ghostty/commit/034f5843f21b7a3c9924d5e42ee34ee784699763) fix: apply kk translation review feedback ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
- [`b5aa8e7`](https://github.com/ghostty-org/ghostty/commit/b5aa8e7a071f53dec2c203fc521e147ce6e8cce0) i18n: complete Kazakh (kk) translation for v1.4 ([#13778](https://github.com/ghostty-org/ghostty/issues/13778)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translates the 180 remaining strings, mainly command palette entries
  introduced for v1.4 localization.
  ```
- [`1fdbb8c`](https://github.com/ghostty-org/ghostty/commit/1fdbb8c912231bdbe039614a70f10772a3e50d23) libghostty: -Dvt-features to compile out unused features ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a `-Dvt-features` build option for libghostty-vt that
  compiles out optional feature areas, primarily so size-conscious
  embedders (e.g. wasm) can significantly trim the binary.
  
  The flag is similar to `-Dcpu`, `+feature` or `feature` to enable it,
  `-feature` to disable, magic word `all` to turn all features on or off.
  Example: `-Dvt-features=-all,+render-state` builds only the render
  state API.
  
  ### Sizes
  
  | Build | Bytes | Brotli |
  |---|---|---|
  | default (all features) | 876,500 | 218,309 |
  | web interactive (`-all,+render-state,+input-encode,+selection,+color,+grid-introspection`) | 661,119 | 168,994 |
  | read-only viewer (`-all,+render-state`) | 537,441 | 132,858 |
  | bare VT core (`-all`) | 515,422 | 125,756 |
  | xterm.js browser bundle (incl. renderers) | 488,663 | 99,311 |
  | @xterm/headless | 182,672 | 39,651 |
  
  Note: xterm versions are stable as of this commit.
  ```
- [`794515b`](https://github.com/ghostty-org/ghostty/commit/794515ba60a8c6d537b5f3a427374b23b2673492) libghostty: -Dvt-features to compile out unused features ([#13834](https://github.com/ghostty-org/ghostty/issues/13834)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a `-Dvt-features` build option for libghostty-vt that
  compiles out optional feature areas, primarily so size-conscious
  embedders (e.g. wasm) can significantly trim the binary.
  
  The flag is similar to `-Dcpu`, `+feature` or `feature` to enable it,
  `-feature` to disable, magic word `all` to turn all features on or off.
  Example: `-Dvt-features=-all,+render-state` builds only the render state
  API.
  
  Added CI to verify the lib and tests _compile_ (we don't run it) for
  each individual feature.
  
  ### Sizes
  
  wasm32, ReleaseFast:
  
  | Build | Bytes | Brotli |
  |---|---|---|
  | default (all features) | 876,500 | 218,309 |
  | web interactive
  (`-all,+render-state,+input-encode,+selection,+color,+grid-introspection`)
  | 661,119 | 168,994 |
  | read-only viewer (`-all,+render-state`) | 537,441 | 132,858 |
  | bare VT core (`-all`) | 515,422 | 125,756 |
  | xterm.js browser bundle (incl. renderers) | 488,663 | 99,311 |
  | @xterm/headless | 182,672 | 39,651 |
  
  Note: xterm versions are stable as of this commit.
  
  ### C Header Note
  
  I didn't do a `vt/features.h` style header that has macros to guard
  symbols for the various features. This is something we should do in the
  future. The way it is now, the C header always declares everything, and
  its not a problem unless an unavailable function is referenced at link
  time.
  ```
- [`348f714`](https://github.com/ghostty-org/ghostty/commit/348f714ff97a4b323ee2ce195bb16387ba6a1dbe) Update VOUCHED list ([#13833](https://github.com/ghostty-org/ghostty/issues/13833)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13831#discussioncomment-18025282)
  from @jcollie.
  
  Vouch: @DiegoArmstrong
  ```
- [`d61920d`](https://github.com/ghostty-org/ghostty/commit/d61920d80e0e6d2c2a058c96d1b916c7300ddab5) lib-vt: disable logging in wasm release builds ([@mitchellh](https://github.com/mitchellh))
- [`51a4311`](https://github.com/ghostty-org/ghostty/commit/51a4311ef18b0971c112967cf24a538a2c71ea36) terminal: clean up overzealous inlining ([@mitchellh](https://github.com/mitchellh))
- [`0e0893a`](https://github.com/ghostty-org/ghostty/commit/0e0893adff219b80f8837f685bfd54f643036fc6) libghostty: attacking wasm binary size ([#13830](https://github.com/ghostty-org/ghostty/issues/13830)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This should release our ReleaseFast bundle from 1.1MB to ~800KB.
  
  The major win is disabling logging in ReleaseFast wasm builds (~200KB).
  
  The next is removing aggressive inlining in paths that don't make sense
  for performance. Verified with benchmarks on native to not affect
  anything really.
  
  The third was really dumb: `var buf: [4096]u32 = @splat(c)` in LLVM
  releasefast for wasm was lowering to 4096 separate `i32.store`...
  like... 30KB of code. Replacing this with a for loop reduced by 30KB and
  made REP (a rare sequence) 11x faster lol.
  ```
- [`e84dd30`](https://github.com/ghostty-org/ghostty/commit/e84dd3015543d695e51993e02a01283cfdab2439) Update VOUCHED list ([#13829](https://github.com/ghostty-org/ghostty/issues/13829)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13828#discussioncomment-18024891)
  from @jcollie.
  
  Vouch: @diego-moment
  ```

## August 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31844397329), [2](https://github.com/ghostty-org/ghostty/actions/runs/31839586303), [3](https://github.com/ghostty-org/ghostty/actions/runs/31833203809), [4](https://github.com/ghostty-org/ghostty/actions/runs/31827610332), [5](https://github.com/ghostty-org/ghostty/actions/runs/31820574489), [6](https://github.com/ghostty-org/ghostty/actions/runs/31817549169), [7](https://github.com/ghostty-org/ghostty/actions/runs/31807124981), [8](https://github.com/ghostty-org/ghostty/actions/runs/31806196926), [9](https://github.com/ghostty-org/ghostty/actions/runs/31799751847), [10](https://github.com/ghostty-org/ghostty/actions/runs/31775512293), [11](https://github.com/ghostty-org/ghostty/actions/runs/31768389423), [12](https://github.com/ghostty-org/ghostty/actions/runs/31764190608)  
Summary: 12 runs • 28 commits • 11 authors

### Changes

- [`88ed6be`](https://github.com/ghostty-org/ghostty/commit/88ed6bebf4abfa8deb1b0cdd73dde4b07c7e0a3e) libghostty: much faster wide-character reflow on resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  Resizing a terminal whose buffer is heavy with wide characters (CJK,
  emoji) is now 3-5x faster on the reflow path.
  
  This was relatively simple work. We already have a bulk fast path for
  same-style cells. We previously omitted ANY wide characters from this.
  We relaxed this by making it work with complete wide pairs (wide followed
  by spacer tail).
  
  ### Benchmarks
  
  Resize dance (13 column resizes, 80 -> 40 -> 132 and back and forth again)
  over a ~2,000-row scrollback buffer.
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | cjk | 0.938 | 0.296 | 3.2x |
  | emoji | 0.875 | 0.191 | 4.6x |
  | mixed build-log | 0.306 | 0.155 | 2.0x |
  | grapheme | 2.449 | 1.831 | 1.3x |
  | ascii-short | 0.115 | 0.117 | 1.0x |
  | ascii-long | 0.109 | 0.112 | 1.0x |
  | latin | 0.093 | 0.095 | 1.0x |
  | sgr-truecolor | 0.939 | 0.965 | 1.0x |
  
  **AI usage:** Profiled, implemented, benchmarked, and written by Fable.
  Plan validated by me before doing it, I wrote all the
  comments/commits/blah.
  ```
- [`d760ee9`](https://github.com/ghostty-org/ghostty/commit/d760ee96e54657416eb427b793c7e839f003df7d) terminal: much faster wide-character reflow on resize ([#13827](https://github.com/ghostty-org/ghostty/issues/13827)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Resizing a terminal whose buffer is heavy with wide characters (CJK,
  emoji) is now 3-5x faster on the reflow path.
  
  This was relatively simple work. We already have a bulk fast path for
  same-style cells. We previously omitted ANY wide characters from this.
  We relaxed this by making it work with complete wide pairs (wide
  followed by spacer tail).
  
  ### Benchmarks
  
  Resize dance (13 column resizes, 80 -> 40 -> 132 and back and forth
  again) over a ~2,000-row scrollback buffer.
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | cjk | 0.938 | 0.296 | 3.2x |
  | emoji | 0.875 | 0.191 | 4.6x |
  | mixed build-log | 0.306 | 0.155 | 2.0x |
  | grapheme | 2.449 | 1.831 | 1.3x |
  | ascii-short | 0.115 | 0.117 | 1.0x |
  | ascii-long | 0.109 | 0.112 | 1.0x |
  | latin | 0.093 | 0.095 | 1.0x |
  | sgr-truecolor | 0.939 | 0.965 | 1.0x |
  
  **AI usage:** Profiled, implemented, benchmarked, and written by Fable.
  Plan validated by me before doing it, I wrote all the
  comments/commits/blah.
  ```
- [`3d9b2b4`](https://github.com/ghostty-org/ghostty/commit/3d9b2b483cd807c05e72e2827559572c38bcbe66) libghostty: much faster grapheme-heavy IO throughput ([@mitchellh](https://github.com/mitchellh))
  ```text
  Processing grapheme-heavy input (ZWJ sequences, emoji modifiers, flags,
  combining marks) through is now almost 3x faster.
  
  ### Primary Change: PageList Capacity Projection
  
  This workload was heavily bound by `PageList.increaseCapacity` because
  pathological cases of single-dimensional growth cause repeated page
  capacity doublings which get increasingly expensive because each time we
  do a full allocation + clone.
  
  So the major change is that for grapheme bytes in particular, when we
  reach a capacity limit, we take the current usage for the current set of
  rows and project it out to the remaining capacity of rows. Basically, we
  assume that a similar workload will continue. So rather than doubling,
  we're _guessing_ how much you're going to need.
  
  In the real world, I'm not really sure if this matters at all. There are
  no regressions on any regular corpus streams (asciinema, wikipedia dumps, etc.).
  
  ### Other Changes
  
  There are some other changes here, all found on the path to improving
  grapheme IO throughput:
  
  * The bitmap allocator now maintains `search_start` hint we update on
    every allocation so that future free-scans are much faster. This is
    the lowest possible place we don't have a full bitmap.
  
  * For wasm32, we use an alternate hashing structure for small keys
    since Wyhash's 64bit * 64bit multiplication is very very slow because
    wasm has no widening instruction.
  
  * Terminal `printSlice` now checks the fast path compatibility once up front
    rather than on every fast-path attempt.
  
  ### Benchmarks
  
  Data: ZWJ family/profession sequences, skin-tone modifiers,
  flags, and combining marks streamed in 64 KiB chunks into an 80x24
  terminal, default modes.
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | wasm, V8, 16 MiB stream | 52 MB/s | 151 MB/s | 2.9x |
  | native, terminal-stream, 64 MiB | 894 ms | 305 ms | 2.9x |
  
  Sorry the native stuff is in ms, that's how our native `ghostty-bench`
  does things versus the custom little V8 harness.
  
  **AI usage:** Developed alongside Fable: profiling, implementation, and
  benchmarks. All human language messages written myself. Validated myself.
  ```
- [`6b22215`](https://github.com/ghostty-org/ghostty/commit/6b22215c5d46019f94b658f7665941f951d0de1e) libghostty: much faster grapheme-heavy IO throughput ([#13826](https://github.com/ghostty-org/ghostty/issues/13826)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Processing grapheme-heavy input (ZWJ sequences, emoji modifiers, flags,
  combining marks) through is now almost 3x faster.
  
  ### Primary Change: PageList Capacity Projection
  
  This workload was heavily bound by `PageList.increaseCapacity` because
  pathological cases of single-dimensional growth cause repeated page
  capacity doublings which get increasingly expensive because each time we
  do a full allocation + clone.
  
  So the major change is that for grapheme bytes in particular, when we
  reach a capacity limit, we take the current usage for the current set of
  rows and project it out to the remaining capacity of rows. Basically, we
  assume that a similar workload will continue. So rather than doubling,
  we're _guessing_ how much you're going to need.
  
  In the real world, I'm not really sure if this matters at all. There are
  no regressions on any regular corpus streams (asciinema, wikipedia
  dumps, etc.).
  
  ### Other Changes
  
  There are some other changes here, all found on the path to improving
  grapheme IO throughput:
  
  * The bitmap allocator now maintains `search_start` hint we update on
  every allocation so that future free-scans are much faster. This is the
  lowest possible place we don't have a full bitmap.
  
  * For wasm32, we use an alternate hashing structure for small keys since
  Wyhash's 64bit * 64bit multiplication is very very slow because wasm has
  no widening instruction.
  
  * Terminal `printSlice` now checks the fast path compatibility once up
  front rather than on every fast-path attempt.
  
  ### Benchmarks
  
  Data: ZWJ family/profession sequences, skin-tone modifiers, flags, and
  combining marks streamed in 64 KiB chunks into an 80x24 terminal,
  default modes.
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | wasm, V8, 16 MiB stream | 52 MB/s | 151 MB/s | 2.9x |
  | native, terminal-stream, 64 MiB | 894 ms | 305 ms | 2.9x |
  
  Sorry the native stuff is in ms, that's how our native `ghostty-bench`
  does things versus the custom little V8 harness.
  
  **AI usage:** Developed alongside Fable: profiling, implementation, and
  benchmarks. All human language messages written myself. Validated
  myself.
  ```
- [`74a233b`](https://github.com/ghostty-org/ghostty/commit/74a233b5439c6721cee8ae1f453c308e02ca9d74) libghostty: faster render state reads and updates on wasm targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the `ghostty_render_state_*` C API significantly faster on
  wasm32-freestanding, measured in V8 via Node for Chrome. Also verified
  in `jsc` for Safari.
  
  The major change is a new bulk row read API that makes full-screen cell reads
  roughly 10x faster for wasm embedders. This should help any embedder with
  high FFI overhead, such as Go, Python, etc. too.
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions (two of the changes are native wins as well).
  
  ## Changes
  
  * color: the "vectorized" palette conversion loop was silently
    scalarized by LLVM into per-byte ops because it loaded/stored through
    array-typed pointers. Zig 0.16 disables the LLVM loop vectorizer, so
    manually vectorized loops must go through vector-typed pointers.
  * C styles: major optimizations to converting Zig styles to C styles.
    This is a heavy operation for render state.
  * render: `endUpdate`'s style-run fill (`@memset` with a struct value)
    re-loaded its source every iteration and stored field by field. Now
    manually vectorized.
  * render: new `GHOSTTY_RENDER_STATE_ROW_DATA_CELLS_RAW` returns a
    borrowed `GhosttyCellsView` of the current row's raw cell values, valid
    until the next update. One call per row instead of 3-6 calls per cell.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | colors_get | 114 ns | 35 ns | 3.3x |
  | style get, per styled cell | 7.8 ns | 6.7 ns | 1.2x |
  | raw+style read, per cell | 8.6 ns | 7.7 ns | 1.1x |
  | full-screen text read, per cell | 7.5 ns | 0.7 ns | 10.7x |
  | full-screen text+style read, per cell | 8.6 ns | 1.7 ns | 5.1x |
  | render state update, styled full frame | 3.4 us | 2.6 us | 1.3x |
  
  **AI usage:** Fable did the implementation and benchmarking and drafted
  this message. Comments were partially rewritten by me.
  ```
- [`16833f5`](https://github.com/ghostty-org/ghostty/commit/16833f5e5f58589c3d6ba876a73eb0c5f550231d) libghostty: faster render state reads and updates on wasm targets ([#13825](https://github.com/ghostty-org/ghostty/issues/13825)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the `ghostty_render_state_*` C API significantly faster on
  wasm32-freestanding, measured in V8 via Node for Chrome. Also verified
  in `jsc` for Safari.
  
  The major change is a new bulk row read API that makes full-screen cell
  reads roughly 10x faster for wasm embedders. This should help any
  embedder with high FFI overhead, such as Go, Python, etc. too.
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions (two of the changes are native wins as well).
  
  ## Changes
  
  * color: the "vectorized" palette conversion loop was silently
  scalarized by LLVM into per-byte ops because it loaded/stored through
  array-typed pointers. Zig 0.16 disables the LLVM loop vectorizer, so
  manually vectorized loops must go through vector-typed pointers.
  * C styles: major optimizations to converting Zig styles to C styles.
  This is a heavy operation for render state.
  * render: `endUpdate`'s style-run fill (`@memset` with a struct value)
  re-loaded its source every iteration and stored field by field. Now
  manually vectorized.
  * render: new `GHOSTTY_RENDER_STATE_ROW_DATA_CELLS_RAW` returns a
  borrowed `GhosttyCellsView` of the current row's raw cell values, valid
  until the next update. One call per row instead of 3-6 calls per cell.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | colors_get | 114 ns | 35 ns | 3.3x |
  | style get, per styled cell | 7.8 ns | 6.7 ns | 1.2x |
  | raw+style read, per cell | 8.6 ns | 7.7 ns | 1.1x |
   | full-screen text read, per cell | 7.5 ns | 0.7 ns | 10.7x |
   | full-screen text+style read, per cell | 8.6 ns | 1.7 ns | 5.1x |
  | render state update, styled full frame | 3.4 us | 2.6 us | 1.3x |
  
  **AI usage:** Fable did the implementation and benchmarking and drafted
  this message. Comments were partially rewritten by me.
  ```
- [`87f69a1`](https://github.com/ghostty-org/ghostty/commit/87f69a12ee28445cd95e39060fd626ccfc27b5e0) libghostty: much faster vt_write on wasm targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes `ghostty_terminal_vt_write` on wasm32-freestanding anywhere
  from 1.4x to 13x faster depending on the input, measured in V8 via Node
  for Chrome as well as `jsc` for Safari.
  
  ## Changes
  
  * stream: the batched parse path (bulk UTF-8 decode, print_slice runs)
    is used even when `build_options.simd` is false. The per-byte loop
    is now debug-only.
  * simd/vt: the scalar `utf8DecodeUntilControlSeq` gets a vectorized
    ASCII bulk path that is compatible with wasm simd128.
  * style: on wasm, `Style.eql` compares canonical `PackedStyle` forms
    which is faster by like 11%. On native its slower so we only do this
    for wasm.
  * build: wasm targets now default to the `simd128` CPU feature since
    every browser engine has supported it for years. Opt out with
    `-Dcpu=generic`.
  * PACKAGING.md documents the wasm build, including `wasm-opt` notes.
  
  ## Benchmarks
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | ascii | 85 MB/s | 1070 MB/s | 12.5x |
  | ascii-wrap | 84 MB/s | 1103 MB/s | 13.1x |
  | clear-redraw | 85 MB/s | 913 MB/s | 10.7x |
  | scroll | 79 MB/s | 304 MB/s | 3.8x |
  | cursor | 120 MB/s | 255 MB/s | 2.1x |
  | utf8 | 99 MB/s | 169 MB/s | 1.7x |
  | sgr16 | 81 MB/s | 133 MB/s | 1.6x |
  | sgr-truecolor | 62 MB/s | 88 MB/s | 1.4x |
  
  End result: wasm at roughly 50-85% of the native ReleaseFast+SIMD build
  on the same workloads. Plain ASCII was at 6% of native before.
  
  **AI usage:** Lots of Fable help. As always, the human language stuff
  like this commit and comments were rewritten by me.
  ```
- [`2f72b04`](https://github.com/ghostty-org/ghostty/commit/2f72b041f65932867baef177e8f3be9c92b0f2ed) libghostty: much faster vt_write on wasm targets ([#13821](https://github.com/ghostty-org/ghostty/issues/13821)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes `ghostty_terminal_vt_write` on wasm32-freestanding anywhere
  from 1.4x to 13x faster depending on the input, measured in V8 via Node
  for Chrome as well as `jsc` for Safari.
  
  This changes the default Wasm build to default to enabling the `simd128`
  CPU feature because baseline doesn't have that and every major browser
  has supported it for years. This results in massive performance
  improvements (like, 50%+ on all streams).
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions.
  
  ## Changes
  
  * stream: the batched parse path (bulk UTF-8 decode, print_slice runs)
  is used even when `build_options.simd` is false. The per-byte loop is
  now debug-only.
  * simd/vt: the scalar `utf8DecodeUntilControlSeq` gets a vectorized
  ASCII bulk path that is compatible with wasm simd128.
  * style: on wasm, `Style.eql` compares canonical `PackedStyle` forms
  which is faster by like 11%. On native its slower so we only do this for
  wasm.
  * build: wasm targets now default to the `simd128` CPU feature since
  every browser engine has supported it for years. Opt out with
  `-Dcpu=generic`.
  * PACKAGING.md documents the wasm build, including `wasm-opt` notes.
  
  ## Benchmarks
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | ascii | 85 MB/s | 1070 MB/s | 12.5x |
  | ascii-wrap | 84 MB/s | 1103 MB/s | 13.1x |
  | clear-redraw | 85 MB/s | 913 MB/s | 10.7x |
  | scroll | 79 MB/s | 304 MB/s | 3.8x |
  | cursor | 120 MB/s | 255 MB/s | 2.1x |
  | utf8 | 99 MB/s | 169 MB/s | 1.7x |
  | sgr16 | 81 MB/s | 133 MB/s | 1.6x |
  | sgr-truecolor | 62 MB/s | 88 MB/s | 1.4x |
  
  End result: wasm at roughly 50-85% of the native ReleaseFast+SIMD build
  on the same workloads. Plain ASCII was at 6% of native before.
  
  **AI usage:** Lots of Fable help. As always, the human language stuff
  like this commit and comments were rewritten by me.
  ```
- [`29a70bc`](https://github.com/ghostty-org/ghostty/commit/29a70bc3674e7a95c47a54f9660833a86c87f3b5) ci: publish wasm tip artifacts ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds and publishes `ghostty-vt.wasm` binaries into our tip
  GitHub releases. These are built with the proper optimization, `simd128`
  CPU feature set, and run through `wasm-opt`.
  
  This allows wasm consumers to use libghostty without a Zig toolkit.
  
  Published two: `ghostty-vt.wasm` and `ghostty-vt-small.wasm`. The latter
  is ReleaseSmall, but is 10 to 20% slower. Users choice.
  ```
- [`8f485a7`](https://github.com/ghostty-org/ghostty/commit/8f485a7f478fc497ec02d60f274a33af542f1819) ci: publish wasm tip artifacts ([#13822](https://github.com/ghostty-org/ghostty/issues/13822)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds and publishes `ghostty-vt.wasm` binaries into our tip GitHub
  releases. These are built with the proper optimization, `simd128` CPU
  feature set, and run through `wasm-opt`.
  
  This allows wasm consumers to use libghostty without a Zig toolkit.
  
  Published two: `ghostty-vt.wasm` and `ghostty-vt-small.wasm`. The latter
  is ReleaseSmall, but is 10 to 20% slower. Users choice.
  ```
- [`e305665`](https://github.com/ghostty-org/ghostty/commit/e3056658d05bdd54db9fd37a02c196bfe81cfe39) libghostty: faster render state updates and C API reads ([@mitchellh](https://github.com/mitchellh))
  ```text
  This improves the performance of render state plus C API reads. I
  specifically benchmarked the C API call and found a lot of overhead in
  the C API layer which this cleans up. The impact of these changes will be
  less visible to Zig consumers but moderately improve there.
  
  All benchmark numbers below are via the C API.
  
  Highlights:
  
  - full rebuilds are **1.71x faster (11.4µs to 6.6µs per 120x80 frame)**
  - single-dirty-row updates (e.g. the TUI/prompt steady state) are *1.44x
    faster**
  - full-frame reads through the C API are **1.2x to 1.8x faster**
  
  ## Changes
  
  * endUpdate skips unchanged style runs.
  * `GRAPHEMES_UTF8` getter gets a fast path for single ASCII codepoints (the
    overwhelming majority of cells).
  * The bg/fg color getters no longer copy the full 28-byte style. Instead,
     they switch directly on the one color field they need.
  * The `get_multi` variants validate the handle and position once per batch
    instead of per key.
  * Iterator positions are sentinel values instead of Zig optionals. The
    optional tagging overhead was showing up in benchmarks.
  * `colors_get` reads through a pointer instead of copying the ~1KB colors
    struct to the stack per call.
  * The palette conversion is vectorized. The 4-byte padded RGB to 3-byte
    was not being auto-vectorized. Explicitly vectorize it. Something like
    a 4x speedup on NEON.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | update (forced full rebuild) | 11.4 µs/frame | 6.6 µs/frame | 1.71x |
  | update (single dirty row) | 143 ns | 99 ns | 1.44x |
  | read cell style/bg/fg/selected | 10.3 ns/cell | 8.8 ns/cell | 1.17x |
  | read cell via get_multi | 9.6 ns/cell | 6.9 ns/cell | 1.40x |
  | read cell UTF-8 text | 4.9 ns/cell | 2.7 ns/cell | 1.78x |
  | colors_get + palette | 213 ns/call | 45 ns/call | 4.58x |
  
  Clean updates (no terminal changes) and the raw cell read paths
  are unchanged.
  
  **AI usage:** Driven by Fable primarily, reviewed everything and rewrote
  all human-language (comments) since Fable in particular does really bad
  at that. This commit message too.
  ```
- [`53be7d0`](https://github.com/ghostty-org/ghostty/commit/53be7d0353640351e2d6a06725779f21a3ebe481) libghostty: faster render state updates and C API reads ([#13818](https://github.com/ghostty-org/ghostty/issues/13818)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This improves the performance of render state plus C API reads. I
  specifically benchmarked the C API call and found a lot of overhead in
  the C API layer which this cleans up. The impact of these changes will
  be less visible to Zig consumers but moderately improve there.
  
  All benchmark numbers below are via the C API.
  
  Highlights:
  
  - full rebuilds are **1.71x faster (11.4µs to 6.6µs per 120x80 frame)**
  - single-dirty-row updates (e.g. the TUI/prompt steady state) are
  **1.44x faster**
  - full-frame reads through the C API are **1.2x to 1.8x faster**
  
  ## Changes
  
  * endUpdate skips unchanged style runs.
  * `GRAPHEMES_UTF8` getter gets a fast path for single ASCII codepoints
  (the overwhelming majority of cells).
  * The bg/fg color getters no longer copy the full 28-byte style.
  Instead, they switch directly on the one color field they need.
  * The `get_multi` variants validate the handle and position once per
  batch instead of per key.
  * Iterator positions are sentinel values instead of Zig optionals. The
  optional tagging overhead was showing up in benchmarks.
  * `colors_get` reads through a pointer instead of copying the ~1KB
  colors struct to the stack per call.
  * The palette conversion is vectorized. The 4-byte padded RGB to 3-byte
  was not being auto-vectorized. Explicitly vectorize it. Something like a
  4x speedup on NEON.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | update (forced full rebuild) | 11.4 µs/frame | 6.6 µs/frame | 1.71x |
  | update (single dirty row) | 143 ns | 99 ns | 1.44x |
  | read cell style/bg/fg/selected | 10.3 ns/cell | 8.8 ns/cell | 1.17x |
  | read cell via get_multi | 9.6 ns/cell | 6.9 ns/cell | 1.40x |
  |read cell UTF-8 text | 4.9 ns/cell | 2.7 ns/cell | 1.78x |
  | colors_get + palette | 213 ns/call | 45 ns/call | 4.58x |
  
  Clean updates (no terminal changes) and the raw cell read paths are
  unchanged.
  
  **AI usage:** Driven by Fable primarily, reviewed everything and rewrote
  all human-language (comments) since Fable in particular does really bad
  at that. This commit message too.
  ```
- [`cde7f93`](https://github.com/ghostty-org/ghostty/commit/cde7f93435eb40dfbc306e338c43418e8322220e) renderer: simplify cell row storage ([@jparise](https://github.com/jparise))
  ```text
  Cell contents used our ArrayListCollection container to manage per-row
  foreground lists. This was the only place ArrayListCollection was used.
  
  We now own the row list slice directly, initialize cursor capacity to
  exactly one cell, and reallocate the contiguous background buffer in
  place when possible. Foreground rows still use exact sizes so resizes
  (which are infrequent) do not retain the high-water mark.
  ```
- [`4a174e1`](https://github.com/ghostty-org/ghostty/commit/4a174e1c89a93853d18e47fd7553801633ba8746) renderer: simplify cell row storage ([#13599](https://github.com/ghostty-org/ghostty/issues/13599)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cell contents used our ArrayListCollection container to manage per-row
  foreground lists. This was the only place ArrayListCollection was used.
  
  We now own the row list slice directly, initialize cursor capacity to
  exactly one cell, and reallocate the contiguous background buffer in
  place when possible. Foreground rows still use exact sizes so resizes
  (which are infrequent) do not retain the high-water mark.
  ```
- [`250a36f`](https://github.com/ghostty-org/ghostty/commit/250a36fe6f55de3d2a910deb420f35b0cf6dc350) i18n: Update es_ES translations ([@alosarjos](https://github.com/alosarjos))
  ```text
  Update the translations for the next 1.4 release
  ```
- [`f2022fe`](https://github.com/ghostty-org/ghostty/commit/f2022fe88d57f1b93913de1087ec4f3e459ef3b7) macOS: avoid holding SurfaceView when sending notifications ([@bo2themax](https://github.com/bo2themax))
- [`375ce78`](https://github.com/ghostty-org/ghostty/commit/375ce787466f7bd666f5d8b2e32182ade296dcf3) i18n: Update Norwegian translations ([@Uzaaft](https://github.com/Uzaaft))
- [`6584450`](https://github.com/ghostty-org/ghostty/commit/6584450279ae3ccd20c889c091a73b3a52d5ce09) i18n: Update Norwegian translations ([#13781](https://github.com/ghostty-org/ghostty/issues/13781)) ([@trag1c](https://github.com/trag1c))
- [`1ff3deb`](https://github.com/ghostty-org/ghostty/commit/1ff3deb1bbbf960e69edf49eb7b34fa227080b8d) i18n: Update es_ES translations ([#13800](https://github.com/ghostty-org/ghostty/issues/13800)) ([@00-kat](https://github.com/00-kat))
  ```text
  Update the translations for the next 1.4 release
  ```
- [`562f21a`](https://github.com/ghostty-org/ghostty/commit/562f21a6e72ce1710ca859b25b1562f7f7b0f76a) macOS: avoid holding SurfaceView when sending notifications ([#13810](https://github.com/ghostty-org/ghostty/issues/13810)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We shouldn't hold a closing surface view when sending notifications and
  waiting to dismiss that notification. This happens rarely, but it's the
  right thing to do.
  
  ### AI Disclosure
  Found by Claude when judging other branches, I applied the changes
  myself.
  
  > Forgot that after force pushing, you can't reopen #13787 🫪, linking it
  here for the review history.
  ```
- [`f81dcad`](https://github.com/ghostty-org/ghostty/commit/f81dcadc82ea2afdcf2dc92929037701122f05b5) Update VOUCHED list ([#13814](https://github.com/ghostty-org/ghostty/issues/13814)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13812#discussioncomment-18018163)
  from @mitchellh.
  
  Vouch: @elitex45
  ```
- [`987ee52`](https://github.com/ghostty-org/ghostty/commit/987ee52751a7d87a7bee996cd2e249a01be2571b) Update and (hopefully) complete Hungarian translations in hu.po ([@balazs-szucs](https://github.com/balazs-szucs))
- [`fa392ba`](https://github.com/ghostty-org/ghostty/commit/fa392baf28c7343ea8f7b005fe2a3299116ee79b) i18n: add missing Hungarian translations ([#13799](https://github.com/ghostty-org/ghostty/issues/13799)) ([@00-kat](https://github.com/00-kat))
  ```text
  Part of: #13766
  ```
- [`93e7e7e`](https://github.com/ghostty-org/ghostty/commit/93e7e7e9933a339032a0499043e0f0c6d7218a7a) po/zh_CN: add missing translations ([@pluiedev](https://github.com/pluiedev))
  ```text
  Frankly the number of command palette entries is a bit ridiculous,
  but such is life
  ```
- [`485864c`](https://github.com/ghostty-org/ghostty/commit/485864cd609ebc7c0350aacbf0ef8c8a0a767c86) po/zh_CN: add missing translations ([#13608](https://github.com/ghostty-org/ghostty/issues/13608)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Frankly the number of command palette entries is a bit ridiculous, but
  such is life
  ```
- [`89a26a3`](https://github.com/ghostty-org/ghostty/commit/89a26a39eb01a7cf34a64f9329da8304bebd4d8e) Update VOUCHED list ([#13808](https://github.com/ghostty-org/ghostty/issues/13808)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12664#discussioncomment-18012616)
  from @pluiedev.
  
  Vouch: @Zlitus
  ```
- [`365e0bd`](https://github.com/ghostty-org/ghostty/commit/365e0bd0083f3d51a7b7242ad8c5a025c7848c75) i18n: Updating `es_AR` for 1.4 ([#13784](https://github.com/ghostty-org/ghostty/issues/13784)) ([@alanmoyano](https://github.com/alanmoyano))
  ```text
  This PR also updates old translations to keep better consistency.
  
  AI Disclaimer: I translated manually all strings and then used an agent
  to review consistency and legibility and applied many suggestions.
  ```
- [`710b872`](https://github.com/ghostty-org/ghostty/commit/710b8723905533d623c5e64ba0c5e6662fe79713) Update VOUCHED list ([#13805](https://github.com/ghostty-org/ghostty/issues/13805)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13804#discussioncomment-18010199)
  from @jcollie.
  
  Vouch: @pssalman
  ```

