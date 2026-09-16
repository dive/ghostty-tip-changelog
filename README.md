> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 16, 2026 at 23:29 UTC.

## September 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35115987294)  
Summary: 1 runs • 7 commits • 4 authors

### Changes

- [`fe9cf6a`](https://github.com/ghostty-org/ghostty/commit/fe9cf6a26691fb7dbfc260eb169a801ca4b9790f) build: fully transition away from cImport/addTranslateC ([@vancluever](https://github.com/vancluever))
  ```text
  This migrates all remaining uses of cImport (and addTranslateC for good
  measure) to using translate-c for C translation, ensuring that we are
  ready for when cImport is removed from the language, and also that all
  sources of C translation are using the same snapshot of the external
  package (when can then be updated when we need to fix something).
  
  A couple of notes:
  
  * A few options have been added to support the new translations, namely
    the ability to link libraries (passed through to linkLibrary on the
    Translator side) and whether or not to initialize default values
    (looks like cImport did this without a way to control it, but
    translate-c does not do it by default).
  
  * Using the new library linking option actually simplifies the process
    of translating a number of the C packages as we have been shipping the
    necessary headers for these packages already with the applicable
    libraries. For some of the more complex translation processes though,
    we still include the appropriate directories directly.
  ```
- [`4dfa44e`](https://github.com/ghostty-org/ghostty/commit/4dfa44ecd95a9e6c72188484c2a2871298800e8a) bash: use passed exit status in precmd ([@jparise](https://github.com/jparise))
  ```text
  The Bash 4.4+ prompt hook saves the command status before doing its own
  work and passes it to __ghostty_precmd. The function ignored that
  argument and instead read the hook invocation status, causing command
  end markers to report zero.
  
  Use the explicit argument when present while retaining the current
  status fallback required by the older bash-preexec path.
  
  See #14247
  ```
- [`ed7f046`](https://github.com/ghostty-org/ghostty/commit/ed7f046ee4dee89e5e8bbbecbc67ee14ac1f10d1) bash: recognize attributed prompt command arrays ([@jparise](https://github.com/jparise))
  ```text
  Bash includes additional variable attributes in declare output, so an
  exported indexed array is reported with an -ax prefix instead of -a.
  Match the indexed-array prefix without requiring a following space so
  these values continue through the array-preserving path.
  ```
- [`591ccac`](https://github.com/ghostty-org/ghostty/commit/591ccacbdfa59945cb4f5b015390d0b8d416a7f0) bash: preserve exit status across prompt commands ([@jparise](https://github.com/jparise))
  ```text
  Existing scalar PROMPT_COMMAND entries can overwrite the last command's
  status before Ghostty's appended hook runs. Capture and restore the
  status before those commands, then consume the saved value in the final
  hook.
  
  Keep array hooks as independent entries because Bash 5.1 and newer
  restore the original status for each entry. Preserve the existing
  PROMPT_COMMAND type and safely handle inherited prompt commands where
  Ghostty's function definitions are absent.
  
  This retains the fast Bash 4.4+ PS0 integration rather than using
  bash-preexec's DEBUG trap.
  
  See #14247
  ```
- [`8482d54`](https://github.com/ghostty-org/ghostty/commit/8482d5454e0eee8329cadf2711be78c40298b6ec) bash: fix OSC 133;D status always zero ([#14250](https://github.com/ghostty-org/ghostty/issues/14250)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Bash 4.4+ prompt hook saves the command status before doing its own
  work and passes it to __ghostty_precmd. The function ignored that
  argument and instead read the hook invocation status, causing command
  end markers to report zero.
  
  Also, existing scalar PROMPT_COMMAND entries can overwrite the last
  command's status before Ghostty's appended hook runs. Capture and
  restore the status before those commands, then consume the saved value
  in the final hook.
  
  Fixes #14247
  ```
- [`8fff9d6`](https://github.com/ghostty-org/ghostty/commit/8fff9d6e98ccb37930629429dafdb02ff97faaea) build: fully transition away from cImport/addTranslateC ([#14246](https://github.com/ghostty-org/ghostty/issues/14246)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This migrates all remaining uses of `cImport` (and `addTranslateC` for
  good measure) to using translate-c for C translation, ensuring that we
  are ready for when `cImport` is removed from the language, and also that
  all sources of C translation are using the same snapshot of the external
  package (when can then be updated when we need to fix something).
  
  A couple of notes:
  
  * A few options have been added to support the new translations, namely
  the ability to link libraries (passed through to `linkLibrary` on the
  Translator side) and whether or not to initialize default values (looks
  like `cImport` did this without a way to control it, but translate-c
  does not do it by default).
  
  * Using the new library linking option actually simplifies the process
  of translating a number of the C packages as we have been shipping the
  necessary headers for these packages already with the applicable
  libraries. For some of the more complex translation processes though, we
  still include the appropriate directories directly.
  ```
- [`f9a3f24`](https://github.com/ghostty-org/ghostty/commit/f9a3f24a56bf05f70894e1a084809d4fffadf420) Update VOUCHED list ([#14256](https://github.com/ghostty-org/ghostty/issues/14256)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14249#discussioncomment-18467661)
  from @mitchellh.
  
  Vouch: @MisterTea
  ```

## September 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34933551563)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`d4c88d8`](https://github.com/ghostty-org/ghostty/commit/d4c88d8069912b653d707191388ca98e24751f12) Update VOUCHED list ([#14241](https://github.com/ghostty-org/ghostty/issues/14241)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14240#discussioncomment-18444371)
  from @jcollie.
  
  Vouch: @JuaniRaggio
  ```

## September 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34895432872), [2](https://github.com/ghostty-org/ghostty/actions/runs/34891901089), [3](https://github.com/ghostty-org/ghostty/actions/runs/34849215429), [4](https://github.com/ghostty-org/ghostty/actions/runs/34791379020)  
Summary: 4 runs • 83 commits • 13 authors

### Changes

- [`4c7496c`](https://github.com/ghostty-org/ghostty/commit/4c7496c03541a62b9721da772e786bfe99e02849) i18n: update Lithuanian translation for v1.4 ([@tdslot](https://github.com/tdslot))
  ```text
  Translate all 181 missing strings, including the command palette entries.
  
  AI-assisted with Pi using OpenAI Codex (gpt-5.6-sol) to draft the translations and run gettext checks. I manually reviewed all translations. msgfmt and msgcmp checks pass.
  
  Related to #13766
  ```
- [`3e08654`](https://github.com/ghostty-org/ghostty/commit/3e08654225115eabd693d16f2f70135257a6a872) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`167ed57`](https://github.com/ghostty-org/ghostty/commit/167ed5788f804160c1a9c282b838a08639a50ec7) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`bd42267`](https://github.com/ghostty-org/ghostty/commit/bd4226741b7351a88303db269fb23610b663bef4) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`f8304c0`](https://github.com/ghostty-org/ghostty/commit/f8304c01f7c50a27b7047fce988826fca151cb51) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`e9693a4`](https://github.com/ghostty-org/ghostty/commit/e9693a4a2f5fe9083815eee117d8ace67be3ad5d) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`0f03d15`](https://github.com/ghostty-org/ghostty/commit/0f03d156c0e146c0645b501dd1aa0aed31681932) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`b3f4dbb`](https://github.com/ghostty-org/ghostty/commit/b3f4dbb37fb92170d7c31352704a7d0d1239cd2e) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`57b3122`](https://github.com/ghostty-org/ghostty/commit/57b312293d32d9d707a95759908468e5638f324b) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`dc2d6f1`](https://github.com/ghostty-org/ghostty/commit/dc2d6f1b3ad796ee511d7e69ceababfe5efe9941) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`eba2ec9`](https://github.com/ghostty-org/ghostty/commit/eba2ec988dbd4063f1072d310f87706dec5d2ca5) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`1779cab`](https://github.com/ghostty-org/ghostty/commit/1779cabf425421e3ec30c0e1463163107d85e1c4) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`58dd6d7`](https://github.com/ghostty-org/ghostty/commit/58dd6d777a77e5f49398a085610ee9c80cbb714a) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`a44c474`](https://github.com/ghostty-org/ghostty/commit/a44c47477ea49d5719d9eee488670fff8444ca4f) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`4df91b3`](https://github.com/ghostty-org/ghostty/commit/4df91b3fc7292c5929f7d834e90dfc29c5eb00e2) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`ab26bb4`](https://github.com/ghostty-org/ghostty/commit/ab26bb4b2ae5a2139fd41740c5fe531f088ade9e) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`7d355b8`](https://github.com/ghostty-org/ghostty/commit/7d355b8a0b09f9175ead9c61083e646ff23c19cf) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`d405da4`](https://github.com/ghostty-org/ghostty/commit/d405da4452dd5377232e44a1156ae46f7f89c4e0) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`6633869`](https://github.com/ghostty-org/ghostty/commit/6633869d8b44f527f3a9920963f263147840d52e) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`18d323d`](https://github.com/ghostty-org/ghostty/commit/18d323d24c19780fb041c1ba70dde4a439faa536) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`7a82211`](https://github.com/ghostty-org/ghostty/commit/7a8221113f761cc38e96e15e0da48eb687a3d3e6) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`7d6c090`](https://github.com/ghostty-org/ghostty/commit/7d6c090a7d3c1238fa5397bfafe0a4ca37caaddf) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`56b739c`](https://github.com/ghostty-org/ghostty/commit/56b739cc3188f53aa5ebd4e0021691831c2084bc) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`85508ca`](https://github.com/ghostty-org/ghostty/commit/85508ca2c9568b8204f37e1cb78344f0673ec9ad) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`05dd3c5`](https://github.com/ghostty-org/ghostty/commit/05dd3c53a7ed47d387d22db4a1e36fc172d6f06b) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`159be4d`](https://github.com/ghostty-org/ghostty/commit/159be4d3c2186377884f77794a8d0aa874954d0b) Update po/lt.po ([@tdslot](https://github.com/tdslot))
  ```text
  Here translate correction isn't exact, but probably depend of context. In English version there is no word "exact".
  ```
- [`6f6da70`](https://github.com/ghostty-org/ghostty/commit/6f6da700ede0289ecb534a726b0b13c584a23f8e) Merge branch 'ghostty-org:main' into i18n-update-translation-lt-for-v1.4 ([@tdslot](https://github.com/tdslot))
- [`ff5b87e`](https://github.com/ghostty-org/ghostty/commit/ff5b87e4dbef56cd6b54174520ed151b88c47368) i18n: re-apply remaining lt.po review suggestions ([@tdslot](https://github.com/tdslot))
  ```text
  Eleven review suggestions from the PR were accepted but never made it
  into the pushed commit. Re-apply them and rewrap the affected entries to
  the canonical 79-column gettext width.
  
  Claude-Session: https://claude.ai/code/session_019aW9GqQj7USLWhmzNhuE34
  ```
- [`607d59b`](https://github.com/ghostty-org/ghostty/commit/607d59b0e8ef46da6e6e6e490ef8e82f961ffb25) i18n: fix Lithuanian grammar and terminology consistency in lt.po ([@tdslot](https://github.com/tdslot))
  ```text
  The wording follows the consultation bank of the VLKK (State Commission
  of the Lithuanian Language) rather than personal preference; the
  relevant entries are cited per change.
  
  - "padalinti" -> "padalyti" (9 strings). VLKK treats "dalyti" and
    "dalinti" as equal variants of the norm, prefixed derivatives
    explicitly included ("padalyti ir padalinti"), but advises picking one
    per text: "Viename tekste patartina pasirinkti vieną kurį variantą ir
    nuosekliai jį vartoti. Nereikėtų kaitalioti ir iš veiksmažodžio dalyti
    ir jo formų padarytų įsigalėjusių terminų."
    https://vlkk.lt/konsultacijos/4607-dalyti-dalinti
    The file was mixing them: the verb was "padalinti" while the noun
    everywhere was "padalijimas", which is formed from "dalyti". Unified
    on the "dalyti" line, since the established noun already commits the
    file to it, and it is also the primary variant in "Kalbos patarimai"
    (Vilnius, 2002, p. 69).
  
  - "atstatyti" -> "atkurti" / "nustatyti iš naujo" (7 strings). VLKK:
    "Veiksmažodis atstatyti reikšme 'grąžinti kokį dalyką į buvusią
    (nesusijusią su stovėjimu) padėtį' [...] vertinamas kaip verstinis ir
    vengtinas vartoti. Vartotini junginiai su veiksmažodžiais grąžinti,
    atkurti ar pan."
    https://vlkk.lt/konsultacijos/12800-atstatyti
    https://vlkk.lt/konsultacijos/235-atstatyti
    Restoring a default font or window size is exactly that sense, so
    "Reset Font Size" / "Reset Window Size" are now "Atkurti...". The file
    already used "atkurti" in "Išdidinti arba atkurti langą". Plain
    "Reset" and "Reset Terminal" re-initialise rather than restore a
    previous value, so those became "Nustatyti (terminalą) iš naujo".
  
  - "selection" is now consistently "pažymėtas tekstas" / "pažymėjimas"
    (26 strings). It had been split between that and "pasirinkimas",
    which means "a choice" -- the sense the file already uses it in for
    "Remember choice for this split".
  
  - "Toggle Fullscreen" now uses the same "Įjungti arba išjungti" pattern
    as the other on/off toggles.
  
  - "Equalize Splits" is plural, agreeing with its own description.
  
  - Unify the HTML "paste path" description with its plain/ANSI siblings,
    and minor wording fixes to the tagline and the $EDITOR description.
  
  Claude-Session: https://claude.ai/code/session_019aW9GqQj7USLWhmzNhuE34
  ```
- [`661e1e7`](https://github.com/ghostty-org/ghostty/commit/661e1e77f445057312666a74d9f5002e82f81764) i18n: update Lithuanian translation for v1.4 ([#13777](https://github.com/ghostty-org/ghostty/issues/13777)) ([@trag1c](https://github.com/trag1c))
  ```text
  Updates the Lithuanian translation for v1.4 and fills all 181 missing
  strings, including the command palette entries.
  
  Related to #13766.
  
  Validation:
  - Manually reviewed all translated strings
  - `msgfmt --check --check-compatibility --check-accelerators` passes
  - `msgcmp` against the translation template passes
  
  AI usage: I used Pi with OpenAI Codex (gpt-5.6-sol) to draft the
  translations and run gettext checks. I manually reviewed all
  translations before submitting.
  ```
- [`6542288`](https://github.com/ghostty-org/ghostty/commit/65422886645f0df601894b9571cb23f583f68caf) Start Italian translation for 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`c488a41`](https://github.com/ghostty-org/ghostty/commit/c488a41b0673ec45e2dab28d0c8b6072b7da709f) nix: add libglvnd to devShell for EGL ([@pluiedev](https://github.com/pluiedev))
- [`fa2ec3a`](https://github.com/ghostty-org/ghostty/commit/fa2ec3a6a890c0d4e4d550564a8e37dc83d047ef) pkg/opengl: add EGL headers and bindings ([@pluiedev](https://github.com/pluiedev))
  ```text
  We need this for exporting DMABUFs and creating our own GL context
  independent of GTK.
  ```
- [`7581009`](https://github.com/ghostty-org/ghostty/commit/75810091686f5ee28d37550c4a7bb07eedaa51da) build: link against libEGL ([@pluiedev](https://github.com/pluiedev))
- [`2f0b653`](https://github.com/ghostty-org/ghostty/commit/2f0b65346918047518e7b32f9bbfa1240c15b62e) gtk,opengl: free us from the clutches of GtkGLArea ([@pluiedev](https://github.com/pluiedev))
  ```text
  GtkGLArea had numerous downsides that forced us to invent unsightly hacks
  in our renderer to work around them, most chiefly the fact that it holds
  its own GdkGLContext on the main thread (GL contexts are not at all
  thread-safe), forcing us to keep our GL calls on the main thread.
  It also does not interact well with triple-buffering and initialization
  is forced to be this sort of deferred song-and-dance since we need to
  wait for the GLArea to initialize its GL context before we can initialize
  the renderer, the core surface, and then most things in the GTK surface.
  
  We instead invent our own custom widget named RenderSurface that takes
  simple DMABUFs and displays them. The task of obtaining a GL context
  falls to manual EGL bindings, since we also need EGL to export OpenGL
  textures into DMABUFs. We keep the EGL context solely on the render
  thread meaning that the main thread never concerns itself with rendering
  except when being notified that the renderer has pushed a new frame.
  
  What makes this extra significant is that now the entire GTK apprt no
  longer depends on OpenGL in any way, shape or form. As long as it is
  being fed DMABUFs, it can render from whichever graphics API you want.
  This means we can add more backends based on OpenGL ES or more likely
  Vulkan rather painlessly in the future.
  
  **AI disclosure**: I came up with the idea and let Pi implement most of
  the nitty-gritty details around EGL, as well as replumbing the renderer
  and cleaning up all the GTK-specific workarounds there. I then carefully
  vetted every line of code and spent roughly as much time reviewing as
  coding. Most of the documentation and all commit messages are in my
  own words.
  ```
- [`380778e`](https://github.com/ghostty-org/ghostty/commit/380778e3ca8bd4083c76ce721f28417e0eacf396) ci: drop libghostty-internal builds on Windows ([@pluiedev](https://github.com/pluiedev))
  ```text
  libghostty-internal isn't really supposed to be used in Windows anyway,
  so why bother testing it?
  ```
- [`a5f604d`](https://github.com/ghostty-org/ghostty/commit/a5f604da718f600088504a37083ae1d160121af0) renderer: make LatestFrame methods no-ops when ExportedFrame is void ([@pluiedev](https://github.com/pluiedev))
- [`4c89835`](https://github.com/ghostty-org/ghostty/commit/4c8983586c4fcdeb0a13bc36a1820e5617c3877f) gtk: initialize core surface on first resize ([@pluiedev](https://github.com/pluiedev))
  ```text
  Now that our core surface does not depend on any GTK-sided OpenGL
  initialization, we can initialize it a lot earlier than before, during
  the first resize event right after GTK allocates the size for the widget.
  ```
- [`b87af86`](https://github.com/ghostty-org/ghostty/commit/b87af8646f71de1398e665c361fe659b0707a72e) pkg/opengl: replace cImport with translate-c ([@pluiedev](https://github.com/pluiedev))
  ```text
  General Zig 0.16+ futureproofing
  ```
- [`adf1614`](https://github.com/ghostty-org/ghostty/commit/adf161473d983986f48c9650152f707bd285d931) pkg/opengl: polish API ([@pluiedev](https://github.com/pluiedev))
- [`45aa963`](https://github.com/ghostty-org/ghostty/commit/45aa963d6b634f8d3e4e9a9ecdd272bf8ad751dd) opengl: delay opengl flush ([@pluiedev](https://github.com/pluiedev))
  ```text
  See https://github.com/ghostty-org/ghostty/pull/14052#issuecomment-5521325497
  ```
- [`ce5d51f`](https://github.com/ghostty-org/ghostty/commit/ce5d51f46f97e5321267abab488ff5d0fdabb2f6) gtk/render_surface: report dmabuf build errors ([@pluiedev](https://github.com/pluiedev))
- [`202fa8e`](https://github.com/ghostty-org/ghostty/commit/202fa8e39007ccbcc267173f1217422d1ac72736) gtk: do not disable OpenGL ES and Vulkan ([@pluiedev](https://github.com/pluiedev))
  ```text
  Apparently either OpenGL ES or Vulkan is required to present our DMABUFs
  for jcollie
  ```
- [`5728672`](https://github.com/ghostty-org/ghostty/commit/57286723d0529dbe10890b84e05baa682f7e9d56) nix: update zon2nix to 0.7.0 ([@jcollie](https://github.com/jcollie))
  ```text
  1. Speeds up runs by ~3x for projects with a large number of
  dependencies by downloading in parallel (~55s → 16s on my workstation).
  
  2. Adds some workarounds for Zig 0.16's package management. The changes
  don't affect Ghostty itself, but do affect downstream projects that
  embed libghostty-vt and want to create Nix packages of their own.
  ```
- [`f5efbae`](https://github.com/ghostty-org/ghostty/commit/f5efbaee5f3bec4de688ba188b51f5bd5b5059a3) nix: use hardlinks ([@jcollie](https://github.com/jcollie))
  ```text
  Zig doesn't like symlinks in some situations.
  ```
- [`13a21fc`](https://github.com/ghostty-org/ghostty/commit/13a21fc047d26827ee324268de427f0862289ab6) nix: use --reflink=auto instead of --link ([@jcollie](https://github.com/jcollie))
  ```text
  Another Zig build system quirk worked around.
  ```
- [`d08ebcc`](https://github.com/ghostty-org/ghostty/commit/d08ebcc867285a3c320144a6d10517b4c40d0790) Keep working on italian translation on 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`69f42c1`](https://github.com/ghostty-org/ghostty/commit/69f42c1a30593bdeb7588c8e66586f8bb9e2ca06) Use 'riquadro' instead of 'divisione' for 'Split' ([@Misairuzame](https://github.com/Misairuzame))
- [`d00a498`](https://github.com/ghostty-org/ghostty/commit/d00a498274f321b8808ba89d63c4e23d93a7d8e0) opengl: flip Y axis during framebuffer blit ([@pluiedev](https://github.com/pluiedev))
- [`4dac203`](https://github.com/ghostty-org/ghostty/commit/4dac203c3f6da1c3ec884e71b1cdc6a428b7a8e5) Finish italian translation for 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`74e47a7`](https://github.com/ghostty-org/ghostty/commit/74e47a706f95f7fabaa4ea7c7a0cf25ffae21bd2) macOS: fix title bar clipping custom font ([@bo2themax](https://github.com/bo2themax))
  ```text
  The #9168 fix is no longer needed, since the frame is now higher than the actual glyph.
  ```
- [`ef7edc4`](https://github.com/ghostty-org/ghostty/commit/ef7edc4a24cf3ef0d6862276602e09f7b4b11b40) gtk/build: speed up repeated builds by letting the Zig build cache work ([@jcollie](https://github.com/jcollie))
  ```text
  Repeated builds were penalized for three reasons:
  
  1. The gresource XML embedded the absolute cache paths of the compiled
  .ui files. It now uses relative paths, resolved against a `--sourcedir`
  passed to glib-compile-resources.
  
  2. Blueprints were compiled through a small Zig wrapper, and a Run step
  hashes the bytes of the executable it runs. A Zig binary does not relink
  to the same bytes, so after a branch switch that touched the wrapper
  every .ui moved, the gresource compiler re-ran and the whole app
  recompiled for identical output. blueprint-compiler is now run directly
  and the wrapper is reduced to a single version check whose output
  nothing reads.
  
  3. The gresource pipeline was built once per artifact. It is now
  memoized on the *std.Build.
  
  Cold builds and builds after real blueprint changes are unaffected. A
  build after the wrapper relinks goes from ~43s to ~7s on my system.
  
  AI disclosure: Claude Opus 5 was used to pinpoint the source of the
  cache poisoning and to prepare a patch. Claude Fable 5.1 measured it,
  traced the remaining churn to the wrapper's relinks, and replaced a
  custom build step with stock ones. The commit message is human-written
  based on the author's understanding of the changes.
  
  Claude-Session: https://claude.ai/code/session_01RsfB3eoSTLfnKa6zi25teN
  ```
- [`55c3e8c`](https://github.com/ghostty-org/ghostty/commit/55c3e8cc0da32921aded5bda5f4de70e69bc0888) First review feedback ([@Misairuzame](https://github.com/Misairuzame))
- [`5beb94c`](https://github.com/ghostty-org/ghostty/commit/5beb94c1620e5f9e880db002d84b95f84cbf25de) renderer: apply font-thicken to IME preedit text ([@helium777](https://github.com/helium777))
  ```text
  IME preedit text was rendered with unthickened glyphs because
  addPreeditCell omitted font_thicken options when calling
  renderCodepoint, leaving them at their default false values.
  
  Fixes #13758
  ```
- [`45058d7`](https://github.com/ghostty-org/ghostty/commit/45058d768991e49d74dd699e012fb0610bc8ae6f) Review feedback ([@Misairuzame](https://github.com/Misairuzame))
- [`962a060`](https://github.com/ghostty-org/ghostty/commit/962a060c86ec518baaf3f54ea51337e8259803ff) macOS: fix title bar clipping custom font ([#14217](https://github.com/ghostty-org/ghostty/issues/14217)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/issues/14135.
  
  <img width="1398" height="652" alt="image"
  src="https://github.com/user-attachments/assets/6901a05e-9d23-4e25-89a7-c16c1694a0f9"
  />
  
  
  > The #9168 fix is no longer needed, since the frame is now higher than
  the actual glyph.
  
  The frame change observation only affects those who have a custom window
  title font set in their config. I asked Claude to run some main thread
  benchmarking compared to `main`; it will gain some delays for rapid
  title changes and window resizing. The additional cost is brought by the
  frequent frame updates which are done by AppKit. But that's necessary
  for updating the title to the correct style.
  
  > I tried to do some diffing and removing duplicates, but it will add
  too many changes too, and I didn't think it's worth doing so.
  
  The amount looks ok to me.
  
  ### `window-title-font-family = PT Mono`
  
  | Phase | Metric | base | branch | Δ | ratio |
  |---|---|---:|---:|---:|---:|
  | Idle, 3 s | main-thread CPU | 2.8 ms | 2.8 ms | -0.0 | 1.00 |
  |  | process CPU | 11.3 ms | 11.2 ms | -0.1 | 0.99 |
  | Paced title updates, 150 × 100 ms | main-thread CPU | 878.5 ms |
  **946.7 ms** | **+68.3** | **1.08** |
  |  | process CPU | 1219.9 ms | 1335.0 ms | +115.1 | 1.09 |
  |  | wall | 17.24 s | 17.34 s | +0.1 | 1.01 |
  | Title burst, 5000 back-to-back | main-thread CPU | 180.7 ms | 181.4 ms
  | +0.7 | 1.00 |
  |  | process CPU | 254.2 ms | 254.8 ms | +0.6 | 1.00 |
  |  | wall | 2.31 s | 2.32 s | +0.0 | 1.00 |
  | `toggle_maximize` × 16 (animated resize) | main-thread CPU | 1947.8 ms
  | **2178.0 ms** | **+230.2** | **1.12** |
  |  | process CPU | 4166.8 ms | 4403.2 ms | +236.4 | 1.06 |
  |  | wall | 16.68 s | 16.72 s | +0.0 | 1.00 |
  | Native fullscreen enter/exit × 2 | main-thread CPU | 196.8 ms | 195.9
  ms | -0.9 | 1.00 |
  |  | process CPU | 360.8 ms | 361.5 ms | +0.7 | 1.00 |
  |  | wall | 8.47 s | 8.47 s | +0.0 | 1.00 |
  
  ### AI Disclosure
  
  Asked Claude to generate the harness to run the benchmark and review my
  changes. I did the changes myself.
  ```
- [`1ab2501`](https://github.com/ghostty-org/ghostty/commit/1ab2501e79b7f1b204896a1009cd6566c93f4e46) gtk/build: speed up repeated builds by letting the Zig build cache work ([#14212](https://github.com/ghostty-org/ghostty/issues/14212)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Repeated builds were penalized for three reasons:
  
  1. The gresource XML embedded the absolute cache paths of the compiled
  .ui files. It now uses relative paths, resolved against a `--sourcedir`
  passed to glib-compile-resources.
  
  2. Blueprints were compiled through a small Zig wrapper, and a Run step
  hashes the bytes of the executable it runs. A Zig binary does not relink
  to the same bytes, so after a branch switch that touched the wrapper
  every .ui moved, the gresource compiler re-ran and the whole app
  recompiled for identical output. blueprint-compiler is now run directly
  and the wrapper is reduced to a single version check whose output
  nothing reads.
  
  3. The gresource pipeline was built once per artifact. It is now
  memoized on the *std.Build.
  
  Cold builds and builds after real blueprint changes are unaffected. A
  build after the wrapper relinks goes from ~43s to ~7s on my system.
  
  AI disclosure: Claude Opus 5 was used to pinpoint the source of the
  cache poisoning and to prepare a patch. Claude Fable 5.1 measured it,
  traced the remaining churn to the wrapper's relinks, and replaced a
  custom build step with stock ones. The commit message is human-written
  based on the author's understanding of the changes.
  ```
- [`d30379c`](https://github.com/ghostty-org/ghostty/commit/d30379c5b9e3dad0963a0c6881896b9b38963801) nix: update zon2nix to 0.7.0 ([#14192](https://github.com/ghostty-org/ghostty/issues/14192)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  1. Speeds up runs by ~3x for projects with a large number of
  dependencies by downloading in parallel (~55s → 16s on my workstation).
  
  2. Adds some workarounds for Zig 0.16's package management. The changes
  don't affect Ghostty itself, but do affect downstream projects that
  embed libghostty-vt and want to create Nix packages of their own.
  
  AI disclosure: Claude was used to diagnose CI failures and suggest
  fixes.
  ```
- [`49b95d8`](https://github.com/ghostty-org/ghostty/commit/49b95d846621469ebc5950fd005fa57bcc160d85) gtk,opengl: free us from the clutches of GtkGLArea ([#14052](https://github.com/ghostty-org/ghostty/issues/14052)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  GtkGLArea had numerous downsides that forced us to invent unsightly
  hacks in our renderer to work around them, most chiefly the fact that it
  holds its own GdkGLContext on the main thread (GL contexts are not at
  all thread-safe), forcing us to keep our GL calls on the main thread. It
  also does not interact well with triple-buffering and initialization is
  forced to be this sort of deferred song-and-dance since we need to wait
  for the GLArea to initialize its GL context before we can initialize the
  renderer, the core surface, and then most things in the GTK surface.
  
  We instead invent our own custom widget named RenderSurface that takes
  simple DMABUFs and displays them. The task of obtaining a GL context
  falls to manual EGL bindings, since we also need EGL to export OpenGL
  textures into DMABUFs. We keep the EGL context solely on the render
  thread meaning that the main thread never concerns itself with rendering
  except when being notified that the renderer has pushed a new frame.
  
  What makes this extra significant is that now the entire GTK apprt no
  longer depends on OpenGL in any way, shape or form. As long as it is
  being fed DMABUFs, it can render from whichever graphics API you want.
  This means we can add more backends based on OpenGL ES or more likely
  Vulkan rather painlessly in the future.
  
  **AI disclosure**: I came up with the idea and let Pi implement most of
  the nitty-gritty details around EGL, as well as replumbing the renderer
  and cleaning up all the GTK-specific workarounds there. I then carefully
  vetted every line of code and spent roughly as much time reviewing as
  coding. Most of the documentation and all commit messages are in my own
  words.
  ```
- [`b38394a`](https://github.com/ghostty-org/ghostty/commit/b38394ae3407a4c4c27102517c03384bec89a560) i18n: it_IT translations for 1.4 ([#13996](https://github.com/ghostty-org/ghostty/issues/13996)) ([@00-kat](https://github.com/00-kat))
- [`6ab34ca`](https://github.com/ghostty-org/ghostty/commit/6ab34cad2d1a91a6282c088e448256248aadda0c) gtk: remove unused blueprint using statement ([@tristan957](https://github.com/tristan957))
- [`9dc0d97`](https://github.com/ghostty-org/ghostty/commit/9dc0d974e62d4a98f55680a58fa574949f4bf134) terminal: answer ANSI DECRQM queries ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14225
  
  Handle the ANSI form of DECRQM (`CSI Ps $ p`), as specified by the
  VT510 reference [1] and xterm [2]. Previously, only the DEC private
  form reached the mode query handler.
  
  [1] https://vt100.net/docs/vt510-rm/DECRQM.html
  [2] https://invisible-island.net/xterm/ctlseqs/ctlseqs.txt
  ```
- [`ec98864`](https://github.com/ghostty-org/ghostty/commit/ec98864737dbf1ccbb6c44b7f72096479b847565) gtk: remove unused blueprint using statement ([#14235](https://github.com/ghostty-org/ghostty/issues/14235)) ([@mitchellh](https://github.com/mitchellh))
- [`3beb6d7`](https://github.com/ghostty-org/ghostty/commit/3beb6d717ac305e6a3c7b152103a6f7e81d8e3cf) terminal: decrqm don't truncate 16-bit mode requests ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQM requests can use a full 16-bit number but we truncated to 15-bits
  for the reply (cause thats all we know about). Preserve, the full
  16-bits for requests so we give the proper response.
  ```
- [`88abb77`](https://github.com/ghostty-org/ghostty/commit/88abb77b17ba0028d41d6731a1521f318d31f777) renderer: apply font-thicken to IME preedit text ([#14230](https://github.com/ghostty-org/ghostty/issues/14230)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Fixes #13758
  
  ### Problem
  
  With `font-thicken = true` on macOS, IME preedit (composing) text
  renders noticeably thinner than committed text.
  
  ### Cause & Fix
  Committed and preedit text diverge in `src/renderer/generic.zig`:
  
  ```text
  Committed: Shaper -> addGlyph -> renderGlyph(..., { .thicken = config.font_thicken, ... })
  Preedit: State -> addPreeditCell -> renderCodepoint(..., { .grid_metrics })
  ```
  
  Fix: Pass `self.config.font_thicken` and
  `self.config.font_thicken_strength` in `addPreeditCell`.
  
  ### Testing
  
  - Verified on macOS with `font-thicken = true`.
  - Verified with `zig fmt --check`.
  
  ### AI Disclosure
  
  AI (gemini-3.8-flash) assisted in tracing the call path; manually
  verified and tested.
  ````
- [`1f225eb`](https://github.com/ghostty-org/ghostty/commit/1f225ebb5894189aa9e12cf3a371f787e574c5f4) terminal: answer ANSI DECRQM queries ([#14236](https://github.com/ghostty-org/ghostty/issues/14236)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14225
  
  Handle the ANSI form of DECRQM (`CSI Ps $ p`), as specified by the VT510
  reference [1] and xterm [2]. Previously, only the DEC private form
  reached the mode query handler.
  
  [1] https://vt100.net/docs/vt510-rm/DECRQM.html
  [2] https://invisible-island.net/xterm/ctlseqs/ctlseqs.txt
  ```
- [`148681e`](https://github.com/ghostty-org/ghostty/commit/148681e0aab45ea84386a7839a26db3e5015cfcd) terminal: decrqm don't truncate 16-bit mode requests ([#14237](https://github.com/ghostty-org/ghostty/issues/14237)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQM requests can use a full 16-bit number but we truncated to 15-bits
  for the reply (cause thats all we know about). Preserve, the full
  16-bits for requests so we give the proper response.
  ```
- [`ba8690c`](https://github.com/ghostty-org/ghostty/commit/ba8690c42088c4dbaaf51e983a31f424a1610b01) i18n(de): Typo fix ([@derVedro](https://github.com/derVedro))
- [`8b5678b`](https://github.com/ghostty-org/ghostty/commit/8b5678bd16df3f3ff0b58d533812c2e04e9dfb5a) i18n(de): German translation improvements ([@derVedro](https://github.com/derVedro))
- [`1266c0a`](https://github.com/ghostty-org/ghostty/commit/1266c0a32aca8faff43881f30176f56dd498c0d0) i18n: update `de_DE` translations ([@rpfaeffle](https://github.com/rpfaeffle))
- [`b32b2f8`](https://github.com/ghostty-org/ghostty/commit/b32b2f87ae478fa195a1e44737648f46ba95d51f) i18n(de): Typo fix ([@derVedro](https://github.com/derVedro))
- [`fee8cb5`](https://github.com/ghostty-org/ghostty/commit/fee8cb523709d89c986421cee844ee53137c2793) i18n(de): Wording plain text ([@derVedro](https://github.com/derVedro))
- [`4cc8fa3`](https://github.com/ghostty-org/ghostty/commit/4cc8fa3359fe3368859b7e226cc28ba93d78d3d1) i18n(de): Fix accidental deletion ([@derVedro](https://github.com/derVedro))
- [`9c4a5a8`](https://github.com/ghostty-org/ghostty/commit/9c4a5a8998bd5fb5f139dce35b7da84b287ca0ae) i18n(de): German translation improvements ([@derVedro](https://github.com/derVedro))
- [`3879bff`](https://github.com/ghostty-org/ghostty/commit/3879bff33d279990539e563d5e40e0368f515665) i18n(de): Wording plain text ([@derVedro](https://github.com/derVedro))
- [`1aaca23`](https://github.com/ghostty-org/ghostty/commit/1aaca23e35f0fac52120d9c4be7a8300b7b5734d) i18n(de): Fix accidental deletion ([@derVedro](https://github.com/derVedro))
- [`5e61670`](https://github.com/ghostty-org/ghostty/commit/5e6167072624f672ac21c3cfc0eef83bb95bec88) i18n(de): update German translation ([@derVedro](https://github.com/derVedro))
- [`e3849b7`](https://github.com/ghostty-org/ghostty/commit/e3849b7a674f5c681ec7d22050f5c4aa26bf83a7) i18n(de): update German translation ([@derVedro](https://github.com/derVedro))
- [`05fcdcc`](https://github.com/ghostty-org/ghostty/commit/05fcdccfedae9d7d3fd5c640ac448fa72f58e696) Merge branch 'i18n/de_DE' into german-supplements ([@derVedro](https://github.com/derVedro))
- [`5833977`](https://github.com/ghostty-org/ghostty/commit/583397756d56b0e2bf8050cd67371389c695a53b) i18n(de): additional improvements ([@rpfaeffle](https://github.com/rpfaeffle))
- [`50f757d`](https://github.com/ghostty-org/ghostty/commit/50f757dc84c1179fe55ee396fb00268ae8dab0b9) i18n(de): adjust floating state description ([@rpfaeffle](https://github.com/rpfaeffle))
- [`d5eba8d`](https://github.com/ghostty-org/ghostty/commit/d5eba8d169545cc29d5ee9796ba37ff29759f4db) i18n: update `de_DE` translations ([#13846](https://github.com/ghostty-org/ghostty/issues/13846)) ([@00-kat](https://github.com/00-kat))
  ```text
  Part of #13766.
  ```
- [`0c2a290`](https://github.com/ghostty-org/ghostty/commit/0c2a290d3a3e2a599be3a43435d778a5896667ee) Sync CODEOWNERS vouch list ([#14229](https://github.com/ghostty-org/ghostty/issues/14229)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @ibaios
  ```

## September 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34768241847), [2](https://github.com/ghostty-org/ghostty/actions/runs/34754840764), [3](https://github.com/ghostty-org/ghostty/actions/runs/34737770142)  
Summary: 3 runs • 5 commits • 4 authors

### Changes

- [`1a8f331`](https://github.com/ghostty-org/ghostty/commit/1a8f331f16b36717f457306753352f260c2ccdb5) macOS: implement move_tab_to_new_window ([@pedronaugusto](https://github.com/pedronaugusto))
  ```text
  The action and its keybind exist, and GTK implements them, but macOS had no
  handler so the binding did nothing there. AppKit already has the command for
  window tabs, so this forwards to it.
  
  A window that isn't in a tab group, or is alone in one, is already a window of
  its own, so there is nothing to move and the action reports it did nothing.
  
  Implements the remaining macOS half of #2630.
  ```
- [`7aab0a0`](https://github.com/ghostty-org/ghostty/commit/7aab0a0392369613472bd5dcfd66bef58e78c3ec) macOS: implement move_tab_to_new_window ([#14216](https://github.com/ghostty-org/ghostty/issues/14216)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Closes #2630 for macOS. #13621 added the `move_tab_to_new_window` action
  and the GTK side; this does the same on macOS with AppKit.
  
  With native tabs a tab is already a window, so the action forwards to
  AppKit's own `moveTabToNewWindow:`. It's a no-op when the window is
  alone in its tab group, same as the Window menu item. The "only
  implemented on Linux" note comes off the doc comment in `Binding.zig`.
  Tested on macOS 26, from a keybind and from the command palette. I have
  no macOS 13-15 machine.
  
  Full disclosure, written with Claude Code, I directed it, read every
  line, and tested the result.
  ```
- [`09a2724`](https://github.com/ghostty-org/ghostty/commit/09a2724c23fd13f7cd24c093c568a4b6792a66a2) Update VOUCHED list ([#14223](https://github.com/ghostty-org/ghostty/issues/14223)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14221#discussioncomment-18420862)
  from @jcollie.
  
  Vouch: @helium777
  ```
- [`6a64b1c`](https://github.com/ghostty-org/ghostty/commit/6a64b1c86a969bfd6e3a51f1a5c757f980657a3b) po/zh_CN: add missing translations ([@bo2themax](https://github.com/bo2themax))
- [`5252b19`](https://github.com/ghostty-org/ghostty/commit/5252b193cfd52b4bcd868135e21e4563f2f326ec) po/zh_CN: add missing translations ([#14218](https://github.com/ghostty-org/ghostty/issues/14218)) ([@pluiedev](https://github.com/pluiedev))

## September 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34701118130), [2](https://github.com/ghostty-org/ghostty/actions/runs/34674371812)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`9bbb9b2`](https://github.com/ghostty-org/ghostty/commit/9bbb9b24680358c939846b79a519ce10f7638d1f) Update VOUCHED list ([#14215](https://github.com/ghostty-org/ghostty/issues/14215)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14166#discussioncomment-18413557)
  from @jcollie.
  
  Vouch: @pedronaugusto
  ```
- [`c0c5473`](https://github.com/ghostty-org/ghostty/commit/c0c5473daf5b0ebc78ce0c8d1854f6221574ab3c) build: refactoring our use of translate-c ([@vancluever](https://github.com/vancluever))
  ```text
  This commit refactors our use of translate-c, in preparation for larger
  removal of cImport and better co-ordination between building of C
  dependencies and translation of headers.
  
  The major update is the creation of an internal helper package that
  wraps our use of the external translate-c library. This allows us to not
  only have better shorthand and a data-driven, declarative approach to C
  translation (versus the otherwise more imperative approach), it also
  funnels the external dependency into a single package instead of
  spreading it out among what will be an increasingly larger amount of
  places as dependencies in "pkg/" get updated.
  
  It also includes some refactors, namely to the harfbuzz package, which
  has had its individual settings refactored into helpers to allow for the
  settings to be better shared between translation and the build of the
  c-based static library.
  
  Wuffs has also had a bit of a refactor too so that we don't generate a
  file with all of the macro defines in it - we just send these in as "-D"
  flags now.
  ```
- [`e2e53f8`](https://github.com/ghostty-org/ghostty/commit/e2e53f861482e080bf45054ba49ef471f9849937) build: refactoring our use of translate-c ([#14203](https://github.com/ghostty-org/ghostty/issues/14203)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This commit refactors our use of translate-c, in preparation for larger
  removal of `cImport` and better co-ordination between building of C
  dependencies and translation of headers.
  
  The major update is the creation of an internal helper package that
  wraps our use of the external translate-c library. This allows us to not
  only have better shorthand and a data-driven, declarative approach to C
  translation (versus the otherwise more imperative approach), it also
  funnels the external dependency into a single package instead of
  spreading it out among what will be an increasingly larger amount of
  places as dependencies in `pkg/` get updated.
  
  It also includes some refactors, namely to the harfbuzz package, which
  has had its individual settings refactored into helpers to allow for the
  settings to be better shared between translation and the build of the
  c-based static library.
  
  Wuffs has also had a bit of a refactor too so that we don't generate a
  file with all of the macro defines in it - we just send these in as `-D`
  flags now.
  ```

## September 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34467384606), [2](https://github.com/ghostty-org/ghostty/actions/runs/34461061903), [3](https://github.com/ghostty-org/ghostty/actions/runs/34447229683)  
Summary: 3 runs • 210 commits • 27 authors

### Changes

- [`53ae1dd`](https://github.com/ghostty-org/ghostty/commit/53ae1dd8bc318fcd139b1a51216a9355a642bd91) update translation ([@anhthang](https://github.com/anhthang))
- [`d13d439`](https://github.com/ghostty-org/ghostty/commit/d13d4399557dbbd81dc462aa1a314d5dba531db8) update ([@anhthang](https://github.com/anhthang))
- [`44f2a44`](https://github.com/ghostty-org/ghostty/commit/44f2a44df7e8c4a0c6df3f7d872ef3d7ead88e51) i18n: update `vi` translation for 1.4 ([#13783](https://github.com/ghostty-org/ghostty/issues/13783)) ([@00-kat](https://github.com/00-kat))
- [`8a3dbc8`](https://github.com/ghostty-org/ghostty/commit/8a3dbc8ce6f450f810e3b05be72690c103e1827b) i18n(hr): spiffy up the translation ([@neoto](https://github.com/neoto))
  ```text
  Adds some linguistic polish mentioned in [my
  review](https://github.com/ghostty-org/ghostty/pull/14019#pullrequestreview-5146552587)
  and throughout the comments.
  
  Contributes to #13766
  ```
- [`6d8f8b9`](https://github.com/ghostty-org/ghostty/commit/6d8f8b9aa739e84a7cbaab2880dfdb5601e1c42e) chore: make event reporting explicit ([@neoto](https://github.com/neoto))
- [`ea624f5`](https://github.com/ghostty-org/ghostty/commit/ea624f5a8cdab0ca353be76a7b5416b76fd58ce2) i18n(hr): spiffy up the translation ([#14194](https://github.com/ghostty-org/ghostty/issues/14194)) ([@trag1c](https://github.com/trag1c))
  ```text
  Adds some linguistic polish mentioned in [my
  
  review](https://github.com/ghostty-org/ghostty/pull/14019#pullrequestreview-5146552587)
  and throughout the comments.
  
  Contributes to #13766
  
  CC: @Filip7 @kristina8888
  ```
- [`4bb135e`](https://github.com/ghostty-org/ghostty/commit/4bb135e2de19b2ce8bddec77ba964ddaebbadc1e) i18n(ru): start updating Russian translation ([@derVedro](https://github.com/derVedro))
- [`1dd31f9`](https://github.com/ghostty-org/ghostty/commit/1dd31f9e9458ac1bf44860d55021f9d54e53c646) i18n(ru): work in progress on Russian translation ([@derVedro](https://github.com/derVedro))
- [`0525c18`](https://github.com/ghostty-org/ghostty/commit/0525c18f60ade456a484d9dc26e751d3c1b3993d) i18n: adjust and extend Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`c50288c`](https://github.com/ghostty-org/ghostty/commit/c50288c35fd147482dbd7e30cfcc414c7612c7dd) i18n: address comments for Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`2a51bdf`](https://github.com/ghostty-org/ghostty/commit/2a51bdf1266df638e9ba49ad5cfad6ee7c780ca3) i18n: return Ghostty to Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`1026a00`](https://github.com/ghostty-org/ghostty/commit/1026a00c19b3cbf254c0b85dced92ab8e63d77bf) i18n: adjust Ukrainian translations ([@chernetskyi](https://github.com/chernetskyi))
- [`d23af9e`](https://github.com/ghostty-org/ghostty/commit/d23af9e397dfe06760ce2ad8f54fb178e7d82e62) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`80b8e49`](https://github.com/ghostty-org/ghostty/commit/80b8e4957625195e85727a6c28200f3bf6c54941) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`5546750`](https://github.com/ghostty-org/ghostty/commit/5546750a75cf44f881c43f44204aa6a9012ab296) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`1510d2b`](https://github.com/ghostty-org/ghostty/commit/1510d2b42a284c183e1fd71749290c220e23ce3d) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`b5817a3`](https://github.com/ghostty-org/ghostty/commit/b5817a35a493eb68dbe3737802384792c561ef06) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`f6244f7`](https://github.com/ghostty-org/ghostty/commit/f6244f7d7f2d555382192e701cd6bc33859b64b6) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`320ba75`](https://github.com/ghostty-org/ghostty/commit/320ba75dc925096bc9b31d4de756b2779380dcd3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`1054be4`](https://github.com/ghostty-org/ghostty/commit/1054be4b6ff66c63f4f703c38d06a547c12d79ba) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`6758251`](https://github.com/ghostty-org/ghostty/commit/675825163b3aa975fe66f577e99b75982b15d45b) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`3f87b2e`](https://github.com/ghostty-org/ghostty/commit/3f87b2e5817429fd123af2c980cf6798017b75a1) i18n(ru): second part of Russian translation ([@derVedro](https://github.com/derVedro))
- [`32159b6`](https://github.com/ghostty-org/ghostty/commit/32159b6fe6714a8401d5ad21ce8487ac0266afd8) i18n(ru): small fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`768bc2e`](https://github.com/ghostty-org/ghostty/commit/768bc2ed475ede520dbe0695184a9e2c4aec9128) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`4c696b9`](https://github.com/ghostty-org/ghostty/commit/4c696b90c5c2db61fd0929f102e9701bbcdfb809) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`0a396b4`](https://github.com/ghostty-org/ghostty/commit/0a396b43dccee62e61e2f17643262b800fd7699b) i18n(ru): context menu fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`ba35746`](https://github.com/ghostty-org/ghostty/commit/ba35746377788b8953a895559a91c6e1733c18da) i18n(ru): improve Russian translation ([@derVedro](https://github.com/derVedro))
- [`6244458`](https://github.com/ghostty-org/ghostty/commit/6244458a11f7c83c9c8774d2f5d27aba027c00fc) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`84dff76`](https://github.com/ghostty-org/ghostty/commit/84dff76b1383f0535657902b64cb614a34bd48e8) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`915977a`](https://github.com/ghostty-org/ghostty/commit/915977a484da9d9b93b3a30ac80ff068c5c3c6a8) i18n(ru): equalize splits ([@derVedro](https://github.com/derVedro))
- [`278b4e2`](https://github.com/ghostty-org/ghostty/commit/278b4e2fc7aab0c5073afdfe2570f27a5a4b9142) i18n(ru): refine Russian translation ([@derVedro](https://github.com/derVedro))
- [`572fd58`](https://github.com/ghostty-org/ghostty/commit/572fd5837728da2363168f035743597767b5b237) macOS: use the same default BellFeatures as config ([@bo2themax](https://github.com/bo2themax))
- [`4f4589f`](https://github.com/ghostty-org/ghostty/commit/4f4589f31f2ca196fc88731dfcdc77e1cbde9852) macOS: use the same default BellFeatures as config ([#14049](https://github.com/ghostty-org/ghostty/issues/14049)) ([@mitchellh](https://github.com/mitchellh))
- [`2de1596`](https://github.com/ghostty-org/ghostty/commit/2de15961157343ff7dbeacc1281df97a3af6c624) macos: normalize action working directory paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #14048
  
  Directory URLs no longer export a trailing slash through PWD, which
  keeps zsh's %1~ prompt expansion from resolving to an empty string.
  
  A shared URL helper removes trailing separators while preserving the
  filesystem root and percent-decoding behavior. Tests cover normal,
  repeated, encoded, and root paths.
  ```
- [`07abbd1`](https://github.com/ghostty-org/ghostty/commit/07abbd1e7ee1f98d40cffacf537577e0bcb3522b) Update macos/Sources/Helpers/Extensions/URL+Extension.swift ([@mitchellh](https://github.com/mitchellh))
- [`1c3a4a8`](https://github.com/ghostty-org/ghostty/commit/1c3a4a8314669a97177e4b39cd5d6451f4c257f3) Update macos/Sources/Helpers/Extensions/URL+Extension.swift ([@mitchellh](https://github.com/mitchellh))
- [`fac595c`](https://github.com/ghostty-org/ghostty/commit/fac595c741aaec126d1cf0085dacfa63019a02c4) macos: normalize action working directory paths ([#14051](https://github.com/ghostty-org/ghostty/issues/14051)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #14048
  
  Directory URLs no longer export a trailing slash through PWD, which
  keeps zsh's %1~ prompt expansion from resolving to an empty string.
  
  A shared URL helper removes trailing separators while preserving the
  filesystem root and percent-decoding behavior. Tests cover normal,
  repeated, encoded, and root paths.
  ```
- [`5aeb693`](https://github.com/ghostty-org/ghostty/commit/5aeb693b7727b0dc6fcc9193bc1d2453af3bcb9a) i18n: Russian translation for 1.4 ([#13809](https://github.com/ghostty-org/ghostty/issues/13809)) ([@trag1c](https://github.com/trag1c))
- [`9af9348`](https://github.com/ghostty-org/ghostty/commit/9af934813a32262ab525673840ccd76ed7df2f52) Merge from upstream ([@mohshami](https://github.com/mohshami))
- [`eb722cb`](https://github.com/ghostty-org/ghostty/commit/eb722cb26dfe3fb5dc481181ae463940492cd742) terminal: mark the previous row dirty when clearing its spacer head ([@fornwall](https://github.com/fornwall))
  ```text
  Erasing a wrapped wide character at the start of a row (ECH or DCH)
  also clears the spacer head it left at the end of the previous row,
  but that row was never marked dirty. With both rows visible, an
  incremental render kept the stale spacer head on screen until
  something unrelated redrew that row.
  
  The clearing happens in the row-start branch of splitCellBoundary.
  clearCells doesn't do dirty tracking, and both callers only mark
  the cursor row, so mark the previous row at the point it's mutated.
  
  The added dirty assertions fail without the fix.
  ```
- [`76e568b`](https://github.com/ghostty-org/ghostty/commit/76e568b475fe88f5506be33ad1a684f3c1eae85e) terminal: mark the previous row dirty when clearing its spacer head ([#14054](https://github.com/ghostty-org/ghostty/issues/14054)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erasing a wrapped wide character at the start of a row (`ECH` or `DCH`)
  also clears the spacer head it left at the end of the previous row, but
  that row was never marked dirty. With both rows visible, an incremental
  render kept the stale spacer head on screen until something unrelated
  redrew that row.
  
  The clearing happens in the row-start branch of `splitCellBoundary`.
  `clearCells` doesn't do dirty tracking, and both callers only mark the
  cursor row, so mark the previous row at the point it's mutated.
  
  The added dirty assertions fail without the fix.
  
  ## AI Disclaimer
  Claude did the heavy lifting - identifying the root cause, generating
  code and description. I reviewed and iterated on it to move around and
  tweak tests, comments and reduce verboseness. Verified the end user
  visible behaviour improvement with a script that coloured the wide
  character, which made the stale rendering visible until a switch to the
  alt screen and back cleared it it.
  ```
- [`58f43d5`](https://github.com/ghostty-org/ghostty/commit/58f43d56289d234271e1e829712e2f043c88278f) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`777929a`](https://github.com/ghostty-org/ghostty/commit/777929a8fe603574474f6e1c9c0a35c08af1a2d9) macOS: review windows when closing multiple tabs ([@bo2themax](https://github.com/bo2themax))
- [`4540d49`](https://github.com/ghostty-org/ghostty/commit/4540d499ae463ad7b90f28f6f852f64f844c160f) macOS: review windows when closing multiple tabs ([#14062](https://github.com/ghostty-org/ghostty/issues/14062)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We can also make close undoable when quitting, i'll add it as a follow
  up pr.
  
  <img width="573" height="450" alt="Xnip2026-08-28_19-25-02"
  src="https://github.com/user-attachments/assets/3b4f34f4-9ee6-4180-beb7-f90e98c8aa40"
  />
  ```
- [`c8c4526`](https://github.com/ghostty-org/ghostty/commit/c8c4526e43e6f832ab5d88759cde98a7b2129886) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`300a0df`](https://github.com/ghostty-org/ghostty/commit/300a0dfcb6a6081ea2ead620445965d036f2ae74) Add the Serbian and Serbian Latin translations ([@kostich](https://github.com/kostich))
- [`74e0bfd`](https://github.com/ghostty-org/ghostty/commit/74e0bfdf24dc02d9cc43d5e9356b7887467abe21) Register code ownership ([@kostich](https://github.com/kostich))
- [`7aa4767`](https://github.com/ghostty-org/ghostty/commit/7aa47671482a29875664f112dd503235d8c421ff) Add new translations to locales file ([@kostich](https://github.com/kostich))
- [`635abb7`](https://github.com/ghostty-org/ghostty/commit/635abb7ee81c8f3f4969255d24e0c24bb47f56cc) Update po/sr.po ([@kostich](https://github.com/kostich))
- [`6cd684d`](https://github.com/ghostty-org/ghostty/commit/6cd684d5d3b2a83c9966b6c5ba239d36fbd937a9) gtk: fix stale pointers to property bindings ([@dkinzler](https://github.com/dkinzler))
  ```text
  Previously, the property binding created in `Surface.bindIsSplit` would
  get freed automatically when the source object (the SplitTree widget)
  got finalized. A subsequent call to `bindIsSplit` could then cause a
  crash by using the stale pointer to the binding. This bug could e.g. be
  triggered by dragging the surface from a single-surface tab to another
  tab.
  
  We now create an extra reference to the binding object so that Surface
  essentially owns the binding and is responsible for freeing it.
  
  Updated the binding in `SurfaceScrolledWindow` to use the same pattern.
  That one was probably fine, because the binding is only created once,
  but let's be safe.
  ```
- [`e8ba5d2`](https://github.com/ghostty-org/ghostty/commit/e8ba5d2c2749e3ac85a280a6f854d9cf3e1646cc) Standardize how config/setting/preference is translated ([@kostich](https://github.com/kostich))
- [`1ae448c`](https://github.com/ghostty-org/ghostty/commit/1ae448c23b42a14b209f50e2b2de4415bfed37c9) Fix translation of sequences ([@kostich](https://github.com/kostich))
- [`2a0371b`](https://github.com/ghostty-org/ghostty/commit/2a0371b28f2077b5553a72d8f1cb5ff878634855) Apply batched suggestions from code review ([@kostich](https://github.com/kostich))
- [`17a2474`](https://github.com/ghostty-org/ghostty/commit/17a24746c4785c24bb3ff6f6758cdccf4bcb38c1) Use the correct accusative form for inanimata ([@kostich](https://github.com/kostich))
- [`e3969ab`](https://github.com/ghostty-org/ghostty/commit/e3969ab494e62bf5a66270e6bae56665faf8fce3) Align translations for current and to left/right ([@kostich](https://github.com/kostich))
- [`84c8e7d`](https://github.com/ghostty-org/ghostty/commit/84c8e7d829ce67f7c079e40cff646e0784986e9b) Align translation for Focus ([@kostich](https://github.com/kostich))
- [`97f57ed`](https://github.com/ghostty-org/ghostty/commit/97f57edccc10cb5ccef34d9d4c94276748bbd953) renderer: vsync unfocused surfaces while dirty ([@j-c-m](https://github.com/j-c-m))
  ```text
  6ae1784f4
  
  Unfocused surfaces stopped the CVDisplayLink and encoded a GPU
  frame on every PTY wakeup. A burst of close writes became that many
  Metal submits instead of one vsync.
  
  Keep the link running while the surface is visible and dirty or
  animating, whether or not it is focused. Idle surfaces still park.
  Focus continues to gate cursor blink, custom-shader animation, and
  QoS.
  ```
- [`caf48a4`](https://github.com/ghostty-org/ghostty/commit/caf48a41ee5c3861c786270d64bac950f2513012) main: fix inverted allow_stack_tracing condition ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.16.0 update dropped the negation from the std default
  (!strip_debug_info), disabling stack traces in every unstripped build.
  
  AI disclosure: Claude Fable was used to diagnose the problem and find the
  fix. Commit message was written by me.
  
  Claude-Session: https://claude.ai/code/session_01QfzQME46DQXwMWa43bQaa3
  ```
- [`069497e`](https://github.com/ghostty-org/ghostty/commit/069497e0ca7d02c073d69e80003c1e0f0b067ee6) gtk: fix stale pointers to property bindings ([#14065](https://github.com/ghostty-org/ghostty/issues/14065)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14037 where dragging the surface from a tab with just a single
  surface to another tab causes a crash.
  
  The cause of the crash is a stale pointer to the property binding
  created in `Surface.bindIsSplit`. When the surface is moved,
  `SplitTree.moveSplit` first updates the two split tree data structures
  of the source/target tab and then calls `bindIsSplit` to bind the
  `is-split` property of the moved surface to the `SplitTree` widget in
  the target tab. When `bindIsSplit` is called, the `SplitTree` widget in
  the source tab has already been destroyed (because the source tab is now
  empty) which causes the old binding to be freed automatically and the
  pointer `Surface.is_split_binding` becomes stale. `bindIsSplit` then
  tries to run `is_split_binding.unbind()` which causes the crash.
  
  When you create a binding with `bindProperty`, the binding itself owns
  the initially created reference and it gets freed when the source or
  target object of the binding is finalized. To prevent this, we now
  create an extra reference to the binding object so that the Surface
  widget owns it and is responsible for freeing it. The binding can still
  get severed automatically, but the binding object itself will not be
  destroyed. This is the solution mentioned in the [GObject
  docs](https://docs.gtk.org/gobject/method.Object.bind_property.html).
  Alternatively, using a WeakRef for the pointer would have also worked.
  
  Updated the binding in `SurfaceScrolledWindow` to use the same pattern.
  That one was probably fine, because the binding should only be created
  once, but it doesn't hurt to be safe.
  
  I reproduced the crash on KDE, on Hyprland I just got a glib critical
  error message about the invalid pointer. That probably has to do with
  what exactly happens to the freed memory, or maybe differing versions.
  
  #### AI Disclosure
  
  Code and comments were written by myself, used GPT5.6 in researching
  gobject binding lifecycles.
  ```
- [`3baff3a`](https://github.com/ghostty-org/ghostty/commit/3baff3a069cb64a9d3739c2ff25423524b3b80ee) main: fix inverted allow_stack_tracing condition ([#14069](https://github.com/ghostty-org/ghostty/issues/14069)) ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.16.0 update dropped the negation from the std default
  (!strip_debug_info), disabling stack traces in every unstripped build.
  
  AI disclosure: Claude Fable was used to diagnose the problem and find
  the fix. Commit message was written by me.
  
  
  Claude-Session: https://claude.ai/code/session_01QfzQME46DQXwMWa43bQaa3
  ```
- [`166d2fe`](https://github.com/ghostty-org/ghostty/commit/166d2fe34d65bd1fa393fd8a213c57bc6119dfb9) build: update Sparkle to 2.9.4 ([@Svector-anu](https://github.com/Svector-anu))
- [`7b47213`](https://github.com/ghostty-org/ghostty/commit/7b47213f94058c3715205ce8fa73f7ae581a652c) Update VOUCHED list ([#14074](https://github.com/ghostty-org/ghostty/issues/14074)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14072#issuecomment-5463405035)
  from @bo2themax.
  
  Vouch: @Svector-anu
  ```
- [`a542359`](https://github.com/ghostty-org/ghostty/commit/a5423592cde24222c0d1719f780c54434b5b5d34) libghostty: use caller allocation on native freestanding ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Native freestanding targets have neither an OS page allocator nor a usable default SMP allocator. Use the allocator supplied through libghostty for terminal page storage and make a missing C allocator fail with out-of-memory instead of instantiating hosted allocation machinery. Document that native freestanding C callers must supply an allocator for allocating operations.
  ```
- [`3376153`](https://github.com/ghostty-org/ghostty/commit/3376153a44e5269b9aee5e6d2524954c171e717b) build: support native freestanding libghostty-vt ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Native freestanding targets cannot emit shared libraries and do not provide an OS page size, stack unwinder, hosted SIMD dependencies, or filesystem-backed Kitty graphics. Build only the static artifact for those targets, define the minimum alignment used for terminal pages, disable hosted-only defaults, and install the public headers with the archive.
  ```
- [`094d175`](https://github.com/ghostty-org/ghostty/commit/094d175efa506f87c296fd8a51371c68eea191b9) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`0a76c31`](https://github.com/ghostty-org/ghostty/commit/0a76c311527a20727764e3281eb4efa8c350058a) Update iTerm2 colorschemes ([#14077](https://github.com/ghostty-org/ghostty/issues/14077)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260824-153547-75c93ee
  ```
- [`98cd670`](https://github.com/ghostty-org/ghostty/commit/98cd670c0c2ccdd3f22c40c65a3306e933643ada) Update VOUCHED list ([#14079](https://github.com/ghostty-org/ghostty/issues/14079)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14078#discussioncomment-18203195)
  from @jcollie.
  
  Vouch: @and-rs
  ```
- [`81d28be`](https://github.com/ghostty-org/ghostty/commit/81d28beaa2e3c507299d0c1a5271c2af718212e3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`090fca4`](https://github.com/ghostty-org/ghostty/commit/090fca451d2c63bc2a5ccec23ea54cedce62c6a6) terminal/kitty: validate POSIX shared memory names ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update shared memory name validation according to the new spec:
  
  https://github.com/kovidgoyal/kitty/commit/22042970cf3a4668d02a1a7bcccca778ec864c21
  ```
- [`7035647`](https://github.com/ghostty-org/ghostty/commit/70356472faa9768eb37577430602fa30495eca81) build: update Sparkle to 2.9.4 ([#14072](https://github.com/ghostty-org/ghostty/issues/14072)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update the macOS Sparkle dependency from 2.9.0 to 2.9.4.
  
  This keeps the Swift package resolution and all tag/tip release workflow
  downloads aligned on the same version. Sparkle 2.9.2 included fixes for
  GHSA-g3hp-f6mg-559v and GHSA-hg88-v3cw-3qrh; 2.9.4 is the current stable
  release.
  
  Validation:
  - verified the 2.9.4 release contains
  `Sparkle-for-Swift-Package-Manager.zip`
  - verified the lockfile revision matches the 2.9.4 tag
  - `jq empty` on `Package.resolved`
  - `git diff --check`
  
  I could not run Xcode package resolution locally because the active
  developer directory is Command Line Tools rather than a full Xcode
  installation.
  ```
- [`5f54958`](https://github.com/ghostty-org/ghostty/commit/5f5495826c7ad143c113c25f40cf2ef39d55e459) terminal: fix living item over-count in RefCountedSet.addWithId ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of `addWithIdContext`
  incremented `living` unconditionally even if `upsert` resolved the value
  to an item that was already alive under a different ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style memory
  to be over-provisioned.
  ```
- [`ec7929c`](https://github.com/ghostty-org/ghostty/commit/ec7929c9c2fffb1c46096f94cc9bdd6d57c85b72) terminal/kitty: validate POSIX shared memory names ([#14080](https://github.com/ghostty-org/ghostty/issues/14080)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update shared memory name validation according to the new spec:
  
  
  https://github.com/kovidgoyal/kitty/commit/22042970cf3a4668d02a1a7bcccca778ec864c21
  ```
- [`83c5671`](https://github.com/ghostty-org/ghostty/commit/83c56715773d2b5f0e8b1d5bee68424514bb43e3) renderer: vsync unfocused surfaces while dirty ([#14068](https://github.com/ghostty-org/ghostty/issues/14068)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A follow on for #14035, we can now fix a long standing
  effiency/performance bug now that we park the display link while idle.
  This actually could cause "animated" un-focused windows to use more GPU
  than their focused counterparts. (AI Agent interfaces seem to love
  animation).
  
  6ae1784f4
  
  Unfocused surfaces stopped the CVDisplayLink and encoded a GPU frame on
  every PTY wakeup. A burst of close writes became that many Metal submits
  instead of one vsync.
  
  Keep the link running while the surface is visible and dirty or
  animating, whether or not it is focused. Idle surfaces still park.
  ```
- [`c181983`](https://github.com/ghostty-org/ghostty/commit/c181983253129f2803891a2d801951244ae5313c) build: update Sparkle to 2.9.6 and pin SPM ([@bo2themax](https://github.com/bo2themax))
- [`6d850fe`](https://github.com/ghostty-org/ghostty/commit/6d850fef7780f3461ee526eba16077ea9d7df8a6) Update VOUCHED list ([#14084](https://github.com/ghostty-org/ghostty/issues/14084)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14083#discussioncomment-18204946)
  from @jcollie.
  
  Vouch: @mgsloan
  ```
- [`3e2c0fa`](https://github.com/ghostty-org/ghostty/commit/3e2c0fa2db39215ee3b8098181baca7feb04ec27) gtk: do not warn when gtk-xft-dpi is -1 ([@mgsloan](https://github.com/mgsloan))
  ````text
  Before this change, ghostty frequently logs the following warning, even though a `gtk-xft-dpi` value of `-1` is valid and indicates default scaling.
  
  ```
  warning(gtk_ghostty_surface): gtk-xft-dpi has invalid value (-1), using default
  ```
  
  From [the gtk docs](https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html):
  
  > The font resolution, in 1024 * dots/inch.
  >
  > -1 to use the default value.
  ````
- [`860cfb1`](https://github.com/ghostty-org/ghostty/commit/860cfb1d7958d0c5af09ff23488cfa6ea6665b46) Address review feedback ([@mgsloan](https://github.com/mgsloan))
- [`8af6897`](https://github.com/ghostty-org/ghostty/commit/8af6897c0afc63037a8a3efee4162a380e3a4572) gtk: do not warn when gtk-xft-dpi is -1 ([#14085](https://github.com/ghostty-org/ghostty/issues/14085)) ([@jcollie](https://github.com/jcollie))
  ````text
  Before this change, ghostty frequently logs the following warning, even
  though a `gtk-xft-dpi` value of `-1` is valid and indicates default
  scaling.
  
  ```
  warning(gtk_ghostty_surface): gtk-xft-dpi has invalid value (-1), using default
  ```
  
  From [the gtk
  docs](https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html):
  
  > The font resolution, in 1024 * dots/inch.
  >
  > -1 to use the default value.
  ````
- [`807a51e`](https://github.com/ghostty-org/ghostty/commit/807a51e3e238b7ae81fdcb03f93e2e3e7d990716) updated localization file (andrejd-magix)
- [`36015c9`](https://github.com/ghostty-org/ghostty/commit/36015c99d06d671ba961c83b74d01d7ef45dc8d3) updated revision date (andrejd-magix)
- [`ee10453`](https://github.com/ghostty-org/ghostty/commit/ee10453a26dfc8ec5d7b612f5e4a5763da7cfa82) fix unclosed quote (andrejd-magix)
- [`abac4c2`](https://github.com/ghostty-org/ghostty/commit/abac4c2cb8122540d99f30645581918022a31fc8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`10b7158`](https://github.com/ghostty-org/ghostty/commit/10b7158e8cd57f21f7327c73a6b2cdb2f498fdae) ci: cross-compile freestanding libghostty-vt ([@Uzaaft](https://github.com/Uzaaft))
- [`7fd93e0`](https://github.com/ghostty-org/ghostty/commit/7fd93e09ca6cbca7c4c4c0dbf2817ca49a82a2a4) build: update Sparkle to 2.9.6 and pin SPM ([#14082](https://github.com/ghostty-org/ghostty/issues/14082)) ([@mitchellh](https://github.com/mitchellh))
- [`0dc2032`](https://github.com/ghostty-org/ghostty/commit/0dc2032e6ab5f197f1d93f8eb1f1735a2b5091e1) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`ec3e384`](https://github.com/ghostty-org/ghostty/commit/ec3e384d2d7d86206fc3c71aa23a76b7bdb5eae9) Sync CODEOWNERS vouch list ([#14090](https://github.com/ghostty-org/ghostty/issues/14090)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @jakeriksen
  - @Kleshzz
  ```
- [`e8aa098`](https://github.com/ghostty-org/ghostty/commit/e8aa098674a42e2b4ed1b8c42f4224564ad9fc1e) Update VOUCHED list ([#14092](https://github.com/ghostty-org/ghostty/issues/14092)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14091#discussioncomment-18212381)
  from @pluiedev.
  
  Denounce: @thomas-trijindev
  ```
- [`0254a7f`](https://github.com/ghostty-org/ghostty/commit/0254a7f06f8b955f9107090581b22ad14f010fe8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`dfccdb2`](https://github.com/ghostty-org/ghostty/commit/dfccdb2d4dfdfa9da14664ae06f56f3db923d1e2) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600) ([@mohshami](https://github.com/mohshami))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Run zig fmt
  
  Move true/false options for copy-on-select to the compatibility handler
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/Surface.zig
  
  
  Update src/Surface.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/Surface.zig
  
  
  Update src/Surface.zig
  
  
  Reorder switch items
  
  Apply comment from kat
  
  Remove redundent code
  ```
- [`e80ce2e`](https://github.com/ghostty-org/ghostty/commit/e80ce2ed4cc603c0b52f9cb344f39c64048478e0) Fix build error ([@mohshami](https://github.com/mohshami))
- [`d4d8f62`](https://github.com/ghostty-org/ghostty/commit/d4d8f62262cb1a974a7d2470d5f79f811fab15e4) i18n: adjust and extend Ukrainian translation ([#13854](https://github.com/ghostty-org/ghostty/issues/13854)) ([@trag1c](https://github.com/trag1c))
- [`59141ad`](https://github.com/ghostty-org/ghostty/commit/59141ad21d7e86e48eec8ab8cbfe0095cb814303) add eu translation ([@erral](https://github.com/erral))
- [`fc7bfa6`](https://github.com/ghostty-org/ghostty/commit/fc7bfa60b4b5b40183387e52b782612f417812f3) ci: move freestanding build into test workflow ([@Uzaaft](https://github.com/Uzaaft))
- [`028af92`](https://github.com/ghostty-org/ghostty/commit/028af92ce3876ce1627163ce777f516b8218b410) terminal: clarify page allocator fallback ([@Uzaaft](https://github.com/Uzaaft))
- [`f6113ea`](https://github.com/ghostty-org/ghostty/commit/f6113ea2f5da697351ffe9dd91653427c4d27f90) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600), more flexible copy-on-select and middle-click-action ([#12604](https://github.com/ghostty-org/ghostty/issues/12604)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Note: No AI was used, Even though I don't know Zig, I looked at the code
  and the modifications seemed easy enough
  
  Closes #12600
  ```
- [`c290639`](https://github.com/ghostty-org/ghostty/commit/c2906398be63f7eed567eee294ec09f291844b95) terminal: fix living item over-count in RefCountedSet.addWithId ([#14081](https://github.com/ghostty-org/ghostty/issues/14081)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of
  `addWithIdContext` incremented `living` unconditionally even if `upsert`
  resolved the value to an item that was already alive under a different
  ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style
  memory to be over-provisioned.
  
  cc @qwerasd205 since its ref counted set, but I did this work manually
  ❤️
  ```
- [`e8709b1`](https://github.com/ghostty-org/ghostty/commit/e8709b1f9ee1a1275c8ca2b3c22f40a4e4663137) Merge remote-tracking branch 'upstream/main' into add-serbian-translation ([@kostich](https://github.com/kostich))
- [`90f7759`](https://github.com/ghostty-org/ghostty/commit/90f775976328cd90b8cf12637b776f0689f2f4f8) Fix HTML/URL acronyms as agreed ([@kostich](https://github.com/kostich))
- [`8bf7e51`](https://github.com/ghostty-org/ghostty/commit/8bf7e517f0571c605a206aae00977c2e8e0cc7ce) Regenerate sr@latin.po from sr.po ([@kostich](https://github.com/kostich))
- [`5e02d00`](https://github.com/ghostty-org/ghostty/commit/5e02d0014de36ab776ac947e60ae5641c9674ca4) ci: require freestanding libghostty-vt builds ([@Uzaaft](https://github.com/Uzaaft))
- [`458f079`](https://github.com/ghostty-org/ghostty/commit/458f079f176632bf98d503bef1726472be505f07) Use the informal form ([@kostich](https://github.com/kostich))
- [`2c854a1`](https://github.com/ghostty-org/ghostty/commit/2c854a1aa42c96ec484f136fdd38d060bd6a7683) freestanding support ([#14076](https://github.com/ghostty-org/ghostty/issues/14076)) ([@mitchellh](https://github.com/mitchellh))
- [`149c9f5`](https://github.com/ghostty-org/ghostty/commit/149c9f562af3933493eb7dd275259eee9ce26f79) terminal: extract whole-terminal search orchestration from the search thread ([@mitchellh](https://github.com/mitchellh))
- [`32601cd`](https://github.com/ghostty-org/ghostty/commit/32601cd79a23618d0e64fd0c73bfd47e713be1ef) terminal/c: add search wrapper implementing the whole-terminal search API ([@mitchellh](https://github.com/mitchellh))
- [`cdef14a`](https://github.com/ghostty-org/ghostty/commit/cdef14a1fddd223b63fec60a8f59832a7e2a4db9) Remove X-Generator from the sr.po file ([@kostich](https://github.com/kostich))
- [`f0c918f`](https://github.com/ghostty-org/ghostty/commit/f0c918fc4b72c6c7e746db68f753d102a02bb206) terminal/c: allow freeing a search and its terminal in any order ([@mitchellh](https://github.com/mitchellh))
- [`f920291`](https://github.com/ghostty-org/ghostty/commit/f9202919f71951e7b5af2837afc30f181ad2168c) libghostty: add ghostty_search_* terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`674abd8`](https://github.com/ghostty-org/ghostty/commit/674abd8a1940c928d3a0fb0ca27d6ed6dfc5e3c0) example: add c-vt-search demonstrating the terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`76d9fce`](https://github.com/ghostty-org/ghostty/commit/76d9fcefef592617360577c9208490dc44d04a65) libghostty: set the search needle via ghostty_search_set, drop GhosttySearchOptions ([@mitchellh](https://github.com/mitchellh))
- [`4b51f52`](https://github.com/ghostty-org/ghostty/commit/4b51f521d4080f1bbdb113180f1b109404b6ad7f) libghostty: add terminal search API ([#14097](https://github.com/ghostty-org/ghostty/issues/14097)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This exposes the terminal search API through libghostty C and Zig APIs.
  
  This was previously available through the Zig APIs but forced our
  threading model. I've now extracted the full terminal search state to a
  new `terminal.search.TerminalSearch` structure so threading isn't
  forced. The C API is completely new.
  
  ## Example (C)
  
  ```c
  GhosttySearch search;
  ghostty_search_new(NULL, &search, terminal);
  
  GhosttyString needle = { (const uint8_t *)"error", 5 };
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_NEEDLE, &needle);
  ghostty_search_run(search);
  
  // Find bar chrome: "k of n"
  size_t total, idx;
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_TOTAL_MATCHES, &total);
  
  // Enter: select the next match (wraps, scrolls the viewport if needed)
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_SELECT_NEXT, NULL);
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_SELECTED_INDEX, &idx);
  
  ghostty_search_free(search);
  ```
  ````
- [`8168115`](https://github.com/ghostty-org/ghostty/commit/81681158b1f04b9900c3e58ba6db790384f5b6f5) Add Serbian translation ([#13842](https://github.com/ghostty-org/ghostty/issues/13842)) ([@00-kat](https://github.com/00-kat))
  ```text
  ## Summary
  - Adds Serbian translations for both Cyrillic (`sr`) and Latin
  (`sr@latin`) scripts, registered in `src/os/i18n_locales.zig` and
  `CODEOWNERS`.
  - `po/sr@latin.po` is generated from `po/sr.po` with `msgfilter
  recode-sr-latin` and should not be translated by hand.
  - Replaces the closed #13030; strings are rebased onto current `main`.
  
  Cc @slowdub for a review.
  
  EDIT: AI disclosure: I used Cursor (Grok 4.6) for mechanical repo work
  only, not for writing the Serbian translations. The agent fetched
  ghostty-org/ghostty, branched from current main, ran msgmerge on
  po/sr.po against the template, generated po/sr@latin.po with msgfilter
  recode-sr-latin, registered sr / sr@latin in src/os/i18n_locales.zig and
  CODEOWNERS, rebased my three commits onto later main, pushed the branch,
  and opened this PR (I had intended to open the PR myself, s***** thing
  ignored my instructions). I translated and reviewed sr.po and the Latin
  file is a recode of that catalog, not a separate translation since
  Serbian Cyrillic can be perfectly transcoded to the Latin script via
  [recode-sr-latin](https://linux.die.net/man/1/recode-sr-latin).
  ```
- [`38c984e`](https://github.com/ghostty-org/ghostty/commit/38c984e6760f59a634b6538f5e8669ec829019f1) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.2 to 3.0.3.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`20abdb5`](https://github.com/ghostty-org/ghostty/commit/20abdb50a6216c450d6d4d010c41c7edf5ab15b2) Update VOUCHED list ([#14101](https://github.com/ghostty-org/ghostty/issues/14101)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14100#discussioncomment-18229353)
  from @jcollie.
  
  Vouch: @jzillmann
  ```
- [`d4a5ff5`](https://github.com/ghostty-org/ghostty/commit/d4a5ff58b6bc4a1fcc79a69f5cff94a678d97f42) macOS: fix window cascading ([@bo2themax](https://github.com/bo2themax))
- [`d2e2488`](https://github.com/ghostty-org/ghostty/commit/d2e2488ef7539124122d346399a5e5cca152f259) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([#14098](https://github.com/ghostty-org/ghostty/issues/14098)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.2 to 3.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.3</h2>
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
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
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
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/efb35369e0ad2afab669f228072c1b0d510eae64"><code>efb3536</code></a>
  release 3.0.3 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/840">#840</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/6441963a7597ab67f36fea0287a7ae58a9bfd8fe"><code>6441963</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/839">#839</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/e5ee6bc58a36b838b92fc1217f2e4b414b5abcc8"><code>e5ee6bc</code></a>
  chore(deps): bump esbuild from 0.28.1 to 0.28.2 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/837">#837</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/d1e66170d32c9ec7bbcb7fae044d3d686ce304d3"><code>d1e6617</code></a>
  chore(deps): bump undici from 6.27.0 to 6.28.0 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/831">#831</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/64037519ba20f54c01bc1dc90342c929aac5a2fa"><code>6403751</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/835">#835</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/7c7184b6876126a5df15adc5b679dc450a393725"><code>7c7184b</code></a>
  chore(deps): bump postcss from 8.5.19 to 8.5.25 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/833">#833</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/0f3f0d2943676d58f9698b3ab590c2056023d77d"><code>0f3f0d2</code></a>
  chore(deps): bump brace-expansion from 5.0.8 to 5.0.9 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/832">#832</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/77fb938f2f95e717ce6705d2909af527263360a0"><code>77fb938</code></a>
  chore(deps): bump prettier from 3.9.5 to 3.9.6 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/830">#830</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/5a6f51711ce2ba103b78f5e9550f810679f11e0e"><code>5a6f517</code></a>
  chore(deps): bump brace-expansion from 5.0.7 to 5.0.8 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/828">#828</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/a3c91c98f80000f5b06c7fc0327c54f51c6ab7d8"><code>a3c91c9</code></a>
  chore(deps): bump the github-actions group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/825">#825</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.2&new-version=3.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`b7a680b`](https://github.com/ghostty-org/ghostty/commit/b7a680bc40b76cf7ed6b21044ac3f291ea0056be) macOS: fix window cascading ([#14106](https://github.com/ghostty-org/ghostty/issues/14106)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression from https://github.com/ghostty-org/ghostty/pull/13722
  ```
- [`451e224`](https://github.com/ghostty-org/ghostty/commit/451e224c64ddd0a9d9e9df045cdfb27c38fa8ff2) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([@bo2themax](https://github.com/bo2themax))
- [`3c1ef5b`](https://github.com/ghostty-org/ghostty/commit/3c1ef5b32fc5ea6b93d28493fabf193f595139cf) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([#14111](https://github.com/ghostty-org/ghostty/issues/14111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I don't know what happened to me, but I didn't notice that I should
  delete this🫪
  ```
- [`501e7b5`](https://github.com/ghostty-org/ghostty/commit/501e7b5c1cf04162305c56e85204d2b1ac9427fb) pkg/fontconfig: update to 2.18.3 ([@vancluever](https://github.com/vancluever))
  ```text
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`2ba7576`](https://github.com/ghostty-org/ghostty/commit/2ba75764f6002baab9cb439dfff7ec37ac7704e8) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions) from 6.7 to 6.8.
  - [Release notes](https://github.com/flatpak/flatpak-github-actions/releases)
  - [Commits](https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3)
  
  ---
  updated-dependencies:
  - dependency-name: flatpak/flatpak-github-actions/flatpak-builder
    dependency-version: '6.8'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7358067`](https://github.com/ghostty-org/ghostty/commit/7358067d1a014e0dc36545046f2df41255f2ea26) build(deps): bump cachix/cachix-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Changelog](https://github.com/cachix/cachix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: 38b082610b782e7e93e209c35fd730d399dee866
    dependency-type: direct:production
  ...
  ```
- [`310797d`](https://github.com/ghostty-org/ghostty/commit/310797df1d912bccd63ef624395a2458e99f6cf7) macOS: fix cascading without affecting other new-window behaviours ([@bo2themax](https://github.com/bo2themax))
- [`a8b0855`](https://github.com/ghostty-org/ghostty/commit/a8b0855b630022db2933f402d9c964a111c8751c) macOS: fix cascading for HiddenTitlebarTerminalWindow ([@bo2themax](https://github.com/bo2themax))
- [`58aa59d`](https://github.com/ghostty-org/ghostty/commit/58aa59d0e176b57d27e685dee86d3e9b7e165ef9) Update po/eu.po ([@erral](https://github.com/erral))
- [`6a51526`](https://github.com/ghostty-org/ghostty/commit/6a5152651c8744bf5058d49ee45fdb6aee63d570) Update po/eu.po ([@erral](https://github.com/erral))
- [`4c731b5`](https://github.com/ghostty-org/ghostty/commit/4c731b5d89708ae742d4809ef1ce6a81c5c551da) Update po/eu.po ([@erral](https://github.com/erral))
- [`4ffec4b`](https://github.com/ghostty-org/ghostty/commit/4ffec4bda7ed603be297564a7b23c1d21707106e) Update po/eu.po ([@erral](https://github.com/erral))
- [`f407316`](https://github.com/ghostty-org/ghostty/commit/f407316c84a313a7f9694a2d6f3e1acabc19a416) Update po/eu.po ([@erral](https://github.com/erral))
  ```text
  applying but both eskuma and eskuina are OK.
  ```
- [`63039a6`](https://github.com/ghostty-org/ghostty/commit/63039a688e765c448ca7cc80b77d83d2177e6f51) update ([@erral](https://github.com/erral))
- [`f184d3c`](https://github.com/ghostty-org/ghostty/commit/f184d3ceb5eaee08f92f6302ac2a499bcd7dc015) update ([@erral](https://github.com/erral))
- [`4da902b`](https://github.com/ghostty-org/ghostty/commit/4da902b3c9929333f7cf78147ec714f34d5619c0) update ([@erral](https://github.com/erral))
- [`9801423`](https://github.com/ghostty-org/ghostty/commit/9801423d01e0e883c32f95a210afd98919520562) update ([@erral](https://github.com/erral))
- [`5d6615f`](https://github.com/ghostty-org/ghostty/commit/5d6615fc43ce5bc7ba9981e0c925d4e3d9dfb0d7) bash: upgrade to bash-preexec 0.7.0 ([@jparise](https://github.com/jparise))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use
  the preexec command argument, which is no longer true because we use it
  for the window title. The comment now explains the current reasoning:
  our bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  ```
- [`7520175`](https://github.com/ghostty-org/ghostty/commit/75201750213200fba1537cf724fac5ba3dec4318) more fixes ([@erral](https://github.com/erral))
- [`aafacb1`](https://github.com/ghostty-org/ghostty/commit/aafacb1cb940e3599cb4ec2c4f9cb975532a12a4) macOS: fix flickering when creating new tab with glass style ([@bo2themax](https://github.com/bo2themax))
- [`fec89f2`](https://github.com/ghostty-org/ghostty/commit/fec89f2541e412b1a2556e56742c7612118f1b72) macOS: fix flickering when creating new tab with glass style ([#14121](https://github.com/ghostty-org/ghostty/issues/14121)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A regression from #13985.
  
  
  https://github.com/user-attachments/assets/cc7d76d7-7d86-4566-921c-a6531ce4087d
  
  
  
  
  ### AI Disclosure
  
  Used Claude to investigate, I reviewed and tested.
  ```
- [`0c1909d`](https://github.com/ghostty-org/ghostty/commit/0c1909d09a0db148913b79c684db1cef58e214ee) bash: upgrade to bash-preexec 0.7.0 ([#14120](https://github.com/ghostty-org/ghostty/issues/14120)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use the
  preexec command argument, which is no longer true because we use it for
  the window title. The comment now explains the current reasoning: our
  bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  
  *AI Usage:* I asked Fable 5.1 to run a verification pass after my manual
  upgrade, and it confirmed the expected behavior.
  ```
- [`084316a`](https://github.com/ghostty-org/ghostty/commit/084316aa825a210dedc9c2fce07772cf36ade3cb) macOS: fix cascading without affecting other new-window behaviours ([#14118](https://github.com/ghostty-org/ghostty/issues/14118)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found another regression when investigating #14107 after the last fix.
  This regression appears on macOS 15 and 26 as well: **New window by
  Shortcuts.app or service menu while a window is visible would create a
  tab**.
  
  It appears that for `new-window` triggered by Shortcuts/Service, a small
  delay is needed to avoid automatic tabbing. It's either removing
  `NSWindow.userTabbingPreference == .always` completely or adding another
  "delay" for cascading. The latter should be better.
  
  Also fixes another cascading for `macos-titlebar-style = hidden`
  previously missed.
  ```
- [`41004c6`](https://github.com/ghostty-org/ghostty/commit/41004c6e2204494a2cbc0b4b78dd3b9c671d7488) build(deps): bump cachix/cachix-action from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866 ([#14116](https://github.com/ghostty-org/ghostty/issues/14116)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 5f2d7c5294214f71b873db4b969586b980625e71 to
  38b082610b782e7e93e209c35fd730d399dee866.
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/blob/master/RELEASE.md">cachix/cachix-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Release</h1>
  <ol>
  <li>
  <p>Create and push a new tag:</p>
  <pre lang="console"><code>git tag v17
  git push origin v17
  </code></pre>
  </li>
  <li>
  <p>Wait for CI to pass.</p>
  </li>
  <li>
  <p><a href="https://github.com/cachix/cachix-action/releases/new">Create
  a release</a> for the new tag.</p>
  </li>
  <li>
  <p>Move the major version tag to the latest release:</p>
  <pre lang="console"><code>git tag -fa v17
  git push origin v17 --force
  </code></pre>
  </li>
  </ol>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/38b082610b782e7e93e209c35fd730d399dee866"><code>38b0826</code></a>
  dev: cleanup tests and dev files</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/0fe030c2864be690428363af3bc7016b7b1925d8"><code>0fe030c</code></a>
  dist</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/792dafcfd01b48d3df8424b641db396602252fc3"><code>792dafc</code></a>
  deps: bump dependencies</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/b690244fb5c76a5486c33b0fbbc6fd55c857d1fe"><code>b690244</code></a>
  ci: improve Nix compatibility test coverage</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/f495f3ffa2f3810a92e5cc0abc2c5d6a2a07ec82"><code>f495f3f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/217">#217</a>
  from cachix/dependabot/github_actions/actions/checkout-7</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/9ee3c77d45d24a8b7557d22cbba3454f2a4f8a7b"><code>9ee3c77</code></a>
  chore(deps): bump actions/checkout from 6 to 7</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
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
- [`dd167cc`](https://github.com/ghostty-org/ghostty/commit/dd167cc464f8f8b30cc561fb07e09e9fb2986c14) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder from 6.7 to 6.8 ([#14115](https://github.com/ghostty-org/ghostty/issues/14115)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions)
  from 6.7 to 6.8.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/flatpak/flatpak-github-actions/releases">flatpak/flatpak-github-actions/flatpak-builder's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.8</h2>
  <ul>
  <li>Add saveCache flag</li>
  <li>Add ability to override artifact name</li>
  <li>Add buildDebugBundle flag</li>
  <li>Update tests, documentation and dependencies</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/79327416609af08178ad73b352877e51450790b3"><code>7932741</code></a>
  Update all dependencies and regenerate dist</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/09e3d61868ecd92a1c5b298a31bcc4bae17ae217"><code>09e3d61</code></a>
  readme: Don't specify setting cache key to github.sha (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/261">#261</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/23e622281a14ba5350ce2ab1ae700ac7d08cc841"><code>23e6222</code></a>
  Update runtime versions and docker images to latest</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a3ab43f58191aa8dc105e572c0a62eaac0a7555a"><code>a3ab43f</code></a>
  flatpak-builder: Add saveCache flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/8e357b1556f526e3642244bdf1a6d585be36de54"><code>8e357b1</code></a>
  ci: Remove unnecessary 'needs' from debug bundle job</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/26e19caa3a954b1d36898a0e239a67d8e856f99c"><code>26e19ca</code></a>
  ci: Add test for artifact-name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/06d246b4d5459d93c166243236f8a086d5578746"><code>06d246b</code></a>
  flatpak-builder: Add ability to override artifact name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a2622647717d8185d0f8cf01bb1ea2341e357ae0"><code>a262264</code></a>
  ci: Add job that uses build-debug-bundle</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/f7362292df659c06960a8c0dc309ab5990454a29"><code>f736229</code></a>
  flatpak-builder: Add buildDebugBundle flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/3b10954431df173eb3b564bb9adfddf3842ff91c"><code>3b10954</code></a>
  ci: Update actions to versions using Node 24</li>
  <li>See full diff in <a
  href="https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=flatpak/flatpak-github-actions/flatpak-builder&package-manager=github_actions&previous-version=6.7&new-version=6.8)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`06178ee`](https://github.com/ghostty-org/ghostty/commit/06178eeaad7648216a0da5eb73537e9dba2266cb) terminal/search: resume a complete search when history is prepended ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`b0481f5`](https://github.com/ghostty-org/ghostty/commit/b0481f5aa76a97e652bb842937ae4fa0eda68f3c) terminal/search: resume a complete search when history is prepended ([#14123](https://github.com/ghostty-org/ghostty/issues/14123)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`3b8141f`](https://github.com/ghostty-org/ghostty/commit/3b8141fbd8e2f5770809d3df2fe0077849866dde) os/open: consume the newline when draining opener stderr ([@jzillmann](https://github.com/jzillmann))
  ```text
  takeDelimiterExclusive never consumes the delimiter: it tosses only the
  exclusive length, so the '\n' stays buffered. Once the spawned opener
  writes a single line to stderr, every subsequent call returns an empty
  slice without advancing the stream, and openThread's loop spins forever
  - one pinned core per affected open(), logging empty
  "open stderr=" warnings at tens of thousands of messages per second for
  the lifetime of the process. The thread also never reaches exe.wait(),
  so the child is never reaped.
  
  Read inclusively instead (which does consume the delimiter) and trim
  the '\n' for logging.
  
  Repro: open a link whose handler writes to stderr, e.g. an OSC 8 link
  with an unknown scheme; watch a core disappear and the unified log
  flood with "os-open: open stderr=".
  
  See discussion #14100.
  ```
- [`372d691`](https://github.com/ghostty-org/ghostty/commit/372d6914b8615610e290f8e8446d75cf4b53efeb) i18n: complete eu translation ([#14095](https://github.com/ghostty-org/ghostty/issues/14095)) ([@trag1c](https://github.com/trag1c))
- [`e212b73`](https://github.com/ghostty-org/ghostty/commit/e212b73cdaf381f2d57edc11307b06c1f520df4b) Update mk localization for v1.4 ([#14088](https://github.com/ghostty-org/ghostty/issues/14088)) ([@trag1c](https://github.com/trag1c))
  ```text
  Addressing #13766 for mk.
  ```
- [`349f026`](https://github.com/ghostty-org/ghostty/commit/349f026087d948f8f898dca3231ff91438f83ab8) os/open: consume the newline when draining opener stderr ([#14125](https://github.com/ghostty-org/ghostty/issues/14125)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the runaway-thread bug reported in #14100 (vouched there).
  
  `openThread` drains the spawned opener's stderr with
  `takeDelimiterExclusive('\n')`. That function tosses only the exclusive
  length, so the `'\n'` is never consumed. Once the child writes one line
  to stderr, every subsequent call returns an empty slice without
  advancing the stream: the `while (true)` loop spins forever — one pinned
  core per affected `open()`, logging empty `os-open: open stderr=`
  warnings at tens of thousands of messages per second for the lifetime of
  the process — and `exe.wait()` is never reached, so the child is never
  reaped.
  
  This change reads inclusively (`takeDelimiterInclusive`, which does
  consume the delimiter) and trims the `'\n'` for logging.
  
  Observed in the wild embedding libghostty on macOS: several days of
  uptime accumulated six leaked opener threads at ~70% of a core each
  (~4.4 cores), from six link clicks whose `/usr/bin/open` wrote to
  stderr. After the fix, the same workload shows zero `os-open` log
  traffic and no leaked threads.
  
  Repro without the fix: open a link whose handler writes to stderr (e.g.
  an OSC 8 link with an unknown scheme), then watch a core pin and `log
  stream --predicate 'subsystem == "com.mitchellh.ghostty"'` flood.
  
  **AI disclosure** (per `AI_POLICY.md`): the bug was diagnosed and this
  patch drafted with Claude Code (thread sampling, log analysis, and
  reading the Zig 0.16 `std.Io.Reader` source to confirm
  `takeDelimiterExclusive`/`takeDelimiterInclusive` toss semantics). I
  reviewed the analysis and the change, understand both, and verified the
  fix in a production build of the embedding app.
  ```
- [`5dfb672`](https://github.com/ghostty-org/ghostty/commit/5dfb672986b57b6246d0c5d2c3c9a8fd3d138543) surface: restore mouse_shape when modifier overrides end ([@j-c-m](https://github.com/j-c-m))
  ```text
  hard-coded .default & .text overrode a previously set OSC22 pointer
  shape, this was a regression introduced in 6e8ed4e8b.
  ```
- [`6674aa3`](https://github.com/ghostty-org/ghostty/commit/6674aa3ba88e4e316af4106746e4b2091868df79) surface: update keyToMouseShape tests to expect mouse_shape ([@j-c-m](https://github.com/j-c-m))
  ```text
  Update the tests to expect the mouse_shape back, not the hardcoded
  .default or .text
  ```
- [`3a766cc`](https://github.com/ghostty-org/ghostty/commit/3a766ccf501c669298e5b648a47d217e99bff618) surface: show .text (i-beam) while shift is held without mouse tracking ([@j-c-m](https://github.com/j-c-m))
  ```text
  I think this is the expected behavoir when a custom OSC22 pointer is set. Once
  shift is released it will return to mouse_shape (whatever the pointer
  was before shit held).
  ```
- [`0fb6d29`](https://github.com/ghostty-org/ghostty/commit/0fb6d29404aab9c54c6fbce3cebd630960938117) SurfaceMouse: simplify keyToMouseShape ([@vancluever](https://github.com/vancluever))
  ```text
  keyToMouseShape was initially designed with more of a transition table
  model in mind to handle key presses/overrides based on very specific
  cursor states. This never materialized, so I think it's safe to just
  simply the process of handling overrides and/or passing along the
  current cursor state from the terminal in the event of key presses.
  
  Also removed a test that is essentially a duplicate of one before it now
  (returning current surface shape in the event of no overrides).
  ```
- [`6000034`](https://github.com/ghostty-org/ghostty/commit/600003455a9b6e7cf06b3127a490d6ab3c1b05df) surface: restore application mouse shape after modifier overrides ([#14128](https://github.com/ghostty-org/ghostty/issues/14128)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a regression of 9a6469743 introduced in 6e8ed4e8b.
  
  With this fix the mouse pointer will be restored to the previous (which
  could have be set to something else via OSC22), not a hardcoded .text or
  .default.
  
  It also will change the cursor to a text selection if shift is held even
  without mouse tracking, I think this is the expected behavior when a
  cursor is set via OSC22. (Kitty additionaly, once you start selecting
  changes to text (I-beam), this would be a follow-up if we desire to
  behave like kitty with OSC22 pointers).
  ```
- [`e01e75b`](https://github.com/ghostty-org/ghostty/commit/e01e75bbb228cfbb5fc08cdd53316928761c020b) terminal: don't touch me! keep the page pool free list unobtrusive ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with
  a custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for
  its items which causes every item to be touched, which forces a full
  page-in of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free
  list entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed,
  but not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`31bdcd5`](https://github.com/ghostty-org/ghostty/commit/31bdcd5a79639bbac97c1a94e0f41d0f5ff84ca2) terminal: don't touch me! keep the page pool free list unobtrusive ([#14130](https://github.com/ghostty-org/ghostty/issues/14130)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with a
  custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for its
  items which causes every item to be touched, which forces a full page-in
  of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free list
  entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed, but
  not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`e347482`](https://github.com/ghostty-org/ghostty/commit/e347482fba62fd905fab2d4c8ec6a8c6f3664385) macOS: fix find previous action when search is focused ([@bo2themax](https://github.com/bo2themax))
- [`e8936b8`](https://github.com/ghostty-org/ghostty/commit/e8936b8969e78e07d9a8bf2b6a22ce59a38f5dfb) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Didn't respect the comment above before when reverting and testing hidden title 🫪
  ```
- [`3cca3e0`](https://github.com/ghostty-org/ghostty/commit/3cca3e0b956f07e008a4c66bb5f1a8ce266259a3) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([#14132](https://github.com/ghostty-org/ghostty/issues/14132)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Didn't respect the comment above. Sorry for the back&forth changes 🫪
  ```
- [`09ff85b`](https://github.com/ghostty-org/ghostty/commit/09ff85b2ac7b4204bbc48b5c7010adf0bdfb36d8) macOS: fix find previous action when search is focused ([#14131](https://github.com/ghostty-org/ghostty/issues/14131)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Typo found by @lrytz.
  ```
- [`ffe015e`](https://github.com/ghostty-org/ghostty/commit/ffe015ee55d1ab39cbf1525823ff18092433eab9) terminal: bitmap allocator marks free chunks with zero bits ([@mitchellh](https://github.com/mitchellh))
- [`c0a4f80`](https://github.com/ghostty-org/ghostty/commit/c0a4f80d80d75f7d3250d12554501fd7197e9bb0) terminal: hash map and ref counted set can initialize from zeroed memory ([@mitchellh](https://github.com/mitchellh))
- [`6112935`](https://github.com/ghostty-org/ghostty/commit/6112935a2fe9b7f5fd6c7595225c53406bee3bb1) terminal: hash map keeps its capacity and entry pointers in the struct ([@mitchellh](https://github.com/mitchellh))
- [`d2ff6d7`](https://github.com/ghostty-org/ghostty/commit/d2ff6d77a05d9e9b247684fad6bcb7979d0b2aca) terminal: pages initialize from zeroed memory and cache-line align their cells ([@mitchellh](https://github.com/mitchellh))
- [`07bccf7`](https://github.com/ghostty-org/ghostty/commit/07bccf7a311acdfa6afc77f2016160d49b1f1982) terminal: make all page data structures treat zero as empty to avoid eagerly paging in mmap pages ([#14137](https://github.com/ghostty-org/ghostty/issues/14137)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates all our page data structures so that the `0` value
  (literally `@memset(0)`) means empty. This way, when we initialize a new
  page via mmap (OS-guaranteed zeroed), we don't need to write to it, and
  don't trigger the kernel to physically map the memory.
  
  From Ghostty 1.3.1, our empty terminal physical memory usage goes from
  128 KB to 48 KB (#14130) to 16 KB (this PR). And even with an empty
  prompt written on my machine, it holds at 16KB, only increasing to two
  pages (32 KB) with 24 rows written.
  
  Here are some measurements.
  
  | Per terminal | Before (macOS) | After (macOS) | Before (Linux) | After
  (Linux) |
  
  |-------------------------------------------------------|----------------|---------------|----------------|---------------|
  | Page-list memory dirty, fresh | 48 KiB | 16 KiB | 24 KiB | 8 KiB |
  | Page-list memory dirty, 24 visible rows written | 64 KiB | 32 KiB | 36
  KiB | 20 KiB |
  
  Note macOS uses 16KB pages and Linux generally uses 4 KB pages.
  
  I ran `ghostty-bench +terminal-stream` main vs this branch and with
  every normal workload the results are within noise (sometimes faster
  sometimes slower).
  
  **AI usage:** It was used as a judge/validator. The actual changes were
  me, commit messages and PR messages all me.
  ```
- [`efa3c66`](https://github.com/ghostty-org/ghostty/commit/efa3c66ed16ea9251d5b2a74b606aabc248d2c00) terminal: PageList nodes are pooled individually from the gpa instead of an arena ([@mitchellh](https://github.com/mitchellh))
- [`35a6fb7`](https://github.com/ghostty-org/ghostty/commit/35a6fb747f5d60ee6d92a7f5667474914a47cf21) terminal: PageList preheats only the viewport and cursor pins ([@mitchellh](https://github.com/mitchellh))
- [`105d0a5`](https://github.com/ghostty-org/ghostty/commit/105d0a5453654f15cbe9e902df9e72ed62fa5474) terminal: C terminal wrapper allocates the kitty temp dir path only when it is set ([@mitchellh](https://github.com/mitchellh))
- [`d1cd56a`](https://github.com/ghostty-org/ghostty/commit/d1cd56a56c4244d9d9fadae028cbffc23a1d3d1a) terminal: dynamic palette shares the built-in default instead of copying it per terminal ([@mitchellh](https://github.com/mitchellh))
- [`c81f0b2`](https://github.com/ghostty-org/ghostty/commit/c81f0b26871c7fbbe2fc35549fdad1f64ed29094) terminal: cut the fixed heap cost of a new terminal nearly in half ([#14138](https://github.com/ghostty-org/ghostty/issues/14138)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This focuses explicitly on the non-mmap allocations for a
  `ghostty_terminal_new` result. The result is that we lower this portion
  of the memory by almost half. The total benefit is smaller since 70% of
  a terminal is mmap'd allocations, but this still yields an absolute ~5KB
  savings on macOS on every new terminal (not just empty, but also with a
  normal prompt and so on).
  
  Four changes to make it happy, broken down into individual commits.
  Nothing crazy:
  
  - **Page list nodes are pooled individually.** The node pool was a
  `std.heap.MemoryPool`, which sits on an arena that preheats and grows
  1.5x, so we paid for wasted space. Nodes now come from `UntouchedPool`
  (the same pool as page buffers) with a preheat of one, so the cost is
  exactlyone node (well, exactly one bucket element size in whatever
  allocator).
  - **Pin pool and tracked pin set are sized for two pins.** Every screen
  tracks exactly a viewport pin and a cursor pin at creation, but we
  preheated eight pins and let the tracked pin map grow to 17 slots on the
  first insert via doubling.
  - **The kitty temp dir path is allocated only when set.** The C wrapper
  embedded a 1 KiB `max_path_bytes` buffer that only embedders that set
  `kitty_image_medium_temp_file` ever wrote to.
  - **The default palette is shared instead of copied.** `DynamicPalette`
  carried two full 1 KiB palettes, `current` and `original`, and
  `original` was almost always the built-in default. It is now a pointer
  to the shared built-in default, or to an allocator-owned copy when a
  custom default is set. This introduces a new OOM path but we gracefully
  handle it by either ignoring or resetting.
  
  Memory measurements:
  
  | Per terminal                                | Before   | After    |
  |---------------------------------------------|----------|----------|
  | phys_footprint delta, fresh                 | 30,066 B | 25,069 B |
  | phys_footprint delta, styled prompt written | 47,023 B | 41,944 B |
  | malloc zone bytes dirtied, fresh            | 12,698 B | 7,782 B  |
  | malloc blocks live after `terminal_new`     | 11,904 B | 6,688 B  |
  | malloc blocks live after the prompt         | 12,320 B | 7,104 B  |
  
  I ran `ghostty-bench +terminal-stream` on a 500 MB ascii corpus, main vs
  this branch interleaved, and there is no noticeable change.
  
  **AI usage:** Fable did validation of the work, I did the
  implementations, commit messages, and PR notes.
  ```
- [`4406cea`](https://github.com/ghostty-org/ghostty/commit/4406cea3e9fde88876551cedfef10d3b245b75b6) input: encode ctrl keys with modifyOtherKeys 2 ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still encoded
  as C0 bytes. This is wrong. I'm going to do a more in depth audit if
  possible with every possible key combination against xterm to see where
  we diverge but this fixes this for now without regressing any tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```
- [`1f5bb57`](https://github.com/ghostty-org/ghostty/commit/1f5bb5769fbb5e717546073d33d3985604a315b2) input: encode ctrl keys with modifyOtherKeys 2 ([#14144](https://github.com/ghostty-org/ghostty/issues/14144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still
  encoded as C0 bytes. This is wrong. I'm going to do a more in depth
  audit if possible with every possible key combination against xterm to
  see where we diverge but this fixes this for now without regressing any
  tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```
- [`636a2f3`](https://github.com/ghostty-org/ghostty/commit/636a2f35b4a37fbb1b58dd801ae14513d355e95e) input: preserve numeric keypad output with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`e7bdda9`](https://github.com/ghostty-org/ghostty/commit/e7bdda9918a87f74178e15132c2894e29a8bf271) input: encode F13 through F25 ([@mitchellh](https://github.com/mitchellh))
- [`37e3cdd`](https://github.com/ghostty-org/ghostty/commit/37e3cdd2d281feb2bb403600974289406f891461) input: encode alt+escape with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`cc3fd8a`](https://github.com/ghostty-org/ghostty/commit/cc3fd8a773300371e2d1f41265128a7bf10adfa2) input: encode help and context menu keys ([@mitchellh](https://github.com/mitchellh))
- [`b97654f`](https://github.com/ghostty-org/ghostty/commit/b97654fe76a8badbbb0c51c0c0e2156fd12f0731) input: improve xterm modifyOtherKeys 2 compatibility ([#14145](https://github.com/ghostty-org/ghostty/issues/14145)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #14144
  
  I wrote a harness that created all possible US-layout keyboard input
  combinations with xterm patch 411 and Ghostty main and compared their
  full encoding sequence. There are various miscompatibilities on purpose
  but these were definitely bugs I wanted to address first.
  
  - Normal-mode numeric keypad keys now preserve their numeric output
  instead of falling through to generic MOK2 encoding. Application keypad
  behavior is unchanged.
  - F13 through F25 now emit their xterm-compatible function-key
  sequences, including modifier parameters.
  - Help and Context Menu now emit editing-key codes 28 and 29.
  - Alt+Escape now emits `CSI 27;3;27~` under MOK2 while retaining the
  traditional `ESC ESC` encoding otherwise.
  
  After these changes, 2,081 of 2,096 cases match xterm exactly. The
  remaining 15 differences are intentional.
  ```
- [`587e08f`](https://github.com/ghostty-org/ghostty/commit/587e08f3f70d29c7bc196e2cd919bd4b11f9b5bb) input: encode non-ASCII alt prefixes as UTF-8 ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to
  the UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without changing
  MOK2. The cases I'm talking about are in my comparison harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`492300c`](https://github.com/ghostty-org/ghostty/commit/492300cad104195411d12217dd22f1cd05f31376) input: encode non-ASCII alt prefixes as UTF-8 ([#14146](https://github.com/ghostty-org/ghostty/issues/14146)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to the
  UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without
  changing MOK2. The cases I'm talking about are in my comparison
  harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`11d1cc4`](https://github.com/ghostty-org/ghostty/commit/11d1cc4fc8decc84048bde1b746f3a013493e36f) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`5909690`](https://github.com/ghostty-org/ghostty/commit/5909690de1d942c8b846dfd51c8a26e510436ade) config: rebuild RepeatableCommand's C mirror on clone ([@i999rri](https://github.com/i999rri))
  ```text
  Cloning value_c copied Command.C structs whose string pointers
  still referenced the source config's memory; once the source was
  freed, an embedded host reading the command list after a config
  replace (ghostty_config_clone + ghostty_config_free of the old
  one) hit use-after-free, caught by ASan. Rebuild the mirror from
  the cloned commands with the same cval path parseCLI uses, and add
  a regression test asserting the clone's C strings do not alias the
  source's.
  ```
- [`955d902`](https://github.com/ghostty-org/ghostty/commit/955d902fa6abb3aaf71cac60d6b81bd83fa7fc69) pkg/fontconfig: update to 2.18.3 ([#14113](https://github.com/ghostty-org/ghostty/issues/14113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #14071 (just additional review and local re-generation/re-org
  of needed headers).
  
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`f426f6f`](https://github.com/ghostty-org/ghostty/commit/f426f6f181ba95f45d33f683fb754b6359d9e04f) Update iTerm2 colorschemes ([#14159](https://github.com/ghostty-org/ghostty/issues/14159)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260831-151010-752a9c0
  ```
- [`97f2ddb`](https://github.com/ghostty-org/ghostty/commit/97f2ddb06e43ed73948385944cd1b0c19c282807) Sync CODEOWNERS vouch list ([#14163](https://github.com/ghostty-org/ghostty/issues/14163)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @slowdub
  ```
- [`258c057`](https://github.com/ghostty-org/ghostty/commit/258c057c0ac7d23b8a908fc1f4c5636670ccdcd1) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action) from 1.4 to 1.5.
  - [Release notes](https://github.com/ryand56/r2-upload-action/releases)
  - [Commits](https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317)
  
  ---
  updated-dependencies:
  - dependency-name: ryand56/r2-upload-action
    dependency-version: '1.5'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e9283ba`](https://github.com/ghostty-org/ghostty/commit/e9283ba872bfb2135dbaadea68d08980dbae5f88) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts) from 1.4.0 to 1.8.0.
  - [Release notes](https://github.com/c-hive/gha-remove-artifacts/releases)
  - [Commits](https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61)
  
  ---
  updated-dependencies:
  - dependency-name: c-hive/gha-remove-artifacts
    dependency-version: 1.8.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`2b3b893`](https://github.com/ghostty-org/ghostty/commit/2b3b893919e0bee74b567598e741a735777c9687) deps: update translate-c backport ([@vancluever](https://github.com/vancluever))
- [`82938b6`](https://github.com/ghostty-org/ghostty/commit/82938b633ba646db38591d969c3c526332bd7e65) deps: update translate-c backport ([#14126](https://github.com/ghostty-org/ghostty/issues/14126)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is just a monthly refresh, things have been pretty quiet on both
  the Aro and translate-c sides.
  
  https://github.com/vancluever/arocc/compare/ecbc5c7...f97cdfc
  
  https://codeberg.org/vancluever/translate-c/compare/05e7b9dd87...4e879eb8ab
  ```
- [`ccaf7c7`](https://github.com/ghostty-org/ghostty/commit/ccaf7c776144cb5200fa0de605159cb90788a286) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([#14164](https://github.com/ghostty-org/ghostty/issues/14164)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action)
  from 1.4 to 1.5.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/ryand56/r2-upload-action/releases">ryand56/r2-upload-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.9.0
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/524">ryand56/r2-upload-action#524</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.686.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/526">ryand56/r2-upload-action#526</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.687.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/527">ryand56/r2-upload-action#527</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.688.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/528">ryand56/r2-upload-action#528</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.689.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/529">ryand56/r2-upload-action#529</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.691.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/530">ryand56/r2-upload-action#530</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v16 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/531">ryand56/r2-upload-action#531</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/532">ryand56/r2-upload-action#532</a></li>
  <li>chore(deps): update dependency <code>@​vercel/ncc</code> to v0.38.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/534">ryand56/r2-upload-action#534</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/533">ryand56/r2-upload-action#533</a></li>
  <li>chore(deps): update dependency typescript to v5.7.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/537">ryand56/r2-upload-action#537</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.700.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/536">ryand56/r2-upload-action#536</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.701.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/538">ryand56/r2-upload-action#538</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.703.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/539">ryand56/r2-upload-action#539</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.1
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/535">ryand56/r2-upload-action#535</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/540">ryand56/r2-upload-action#540</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/541">ryand56/r2-upload-action#541</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.705.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/542">ryand56/r2-upload-action#542</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.709.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/543">ryand56/r2-upload-action#543</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.2
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/544">ryand56/r2-upload-action#544</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.712.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/545">ryand56/r2-upload-action#545</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.713.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/546">ryand56/r2-upload-action#546</a></li>
  <li>fix(deps): update dependency mime to v4.0.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/548">ryand56/r2-upload-action#548</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.715.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/547">ryand56/r2-upload-action#547</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.717.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/549">ryand56/r2-upload-action#549</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/550">ryand56/r2-upload-action#550</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.5
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/551">ryand56/r2-upload-action#551</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.722.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/552">ryand56/r2-upload-action#552</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.723.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/553">ryand56/r2-upload-action#553</a></li>
  <li>chore(deps): update dependency typescript to v5.7.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/554">ryand56/r2-upload-action#554</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.726.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/555">ryand56/r2-upload-action#555</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.6
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/556">ryand56/r2-upload-action#556</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.731.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/557">ryand56/r2-upload-action#557</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.7
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/558">ryand56/r2-upload-action#558</a></li>
  <li>chore(deps): update determinatesystems/magic-nix-cache-action action
  to v9 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/560">ryand56/r2-upload-action#560</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.10.10 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/561">ryand56/r2-upload-action#561</a></li>
  <li>chore(deps): update dependency typescript to v5.8.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/564">ryand56/r2-upload-action#564</a></li>
  <li>ci(test-nix): replace magic nix cache with flakehub cache by <a
  href="https://github.com/ryand56"><code>@​ryand56</code></a> in <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/567">ryand56/r2-upload-action#567</a></li>
  <li>chore(deps): update dependency typescript to v5.8.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/566">ryand56/r2-upload-action#566</a></li>
  <li>fix(deps): update dependency mime to v4.0.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/565">ryand56/r2-upload-action#565</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v17 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/569">ryand56/r2-upload-action#569</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.810.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/559">ryand56/r2-upload-action#559</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.19 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/572">ryand56/r2-upload-action#572</a></li>
  <li>chore(deps): update stefanzweifel/git-auto-commit-action action to
  v6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/576">ryand56/r2-upload-action#576</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.832.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/571">ryand56/r2-upload-action#571</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.33 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/573">ryand56/r2-upload-action#573</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.837.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/577">ryand56/r2-upload-action#577</a></li>
  <li>chore(deps): update dependency dotenv to v16.6.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/578">ryand56/r2-upload-action#578</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317"><code>33ebb7a</code></a>
  chore: update to nodejs 24</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/61474c8f6a21b0dd8fc877a0b93c2c2078c88f60"><code>61474c8</code></a>
  chore: update mappings [skip ci]</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/7d9e7c27f8702296342da8daf84e76b24e43622d"><code>7d9e7c2</code></a>
  chore(deps): update typescript to v6</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/6e86c77f4ab91d5b532f6156c15509ef35fd905a"><code>6e86c77</code></a>
  fix(renovate): increase minimumReleaseAge and add packageRules for
  ts</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/fd3d3d4ccdcea99f8e7cc84bbb0a468147e9235e"><code>fd3d3d4</code></a>
  chore(deps): update dependency jest to v30.5.1</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/0b5990b910991eb1c068df9f99384b66e0b49e41"><code>0b5990b</code></a>
  chore(deps): update dependency github-action-ts-run-api to v3.1.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/4196309eee620f2cd556648b16b4b45fd959cee9"><code>4196309</code></a>
  chore(deps): update dependency dotenv to v17.4.2</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/d62fd1388703f08312d5f62fdef74f4b363a2802"><code>d62fd13</code></a>
  chore(deps): update dependency <code>@​vercel/ncc</code> to ^0.45.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/5124bb99384f12af4f3947f0c6a8f6509d580079"><code>5124bb9</code></a>
  chore(deps): update dependency ts-jest to v29.4.12</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/820995a4f185d5c18d4c60e6e371494e3046b336"><code>820995a</code></a>
  chore(deps): update dependency <code>@​actions/core</code> to
  v3.0.1</li>
  <li>Additional commits viewable in <a
  href="https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=ryand56/r2-upload-action&package-manager=github_actions&previous-version=1.4&new-version=1.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`da9e216`](https://github.com/ghostty-org/ghostty/commit/da9e21602f918d47a46399c458937eff7c7a74ac) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([#14165](https://github.com/ghostty-org/ghostty/issues/14165)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts)
  from 1.4.0 to 1.8.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/c-hive/gha-remove-artifacts/releases">c-hive/gha-remove-artifacts's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.8.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>skip-recent-commits</code> input keeps every artifact of
  the N most recent commits, regardless of how many artifacts each commit
  produced. Applied before <code>skip-recent</code>, so the two can be
  combined. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/28">#28</a></li>
  <li><code>GITHUB_TOKEN</code> can now be set on both <code>env:</code>
  and <code>with:</code> (for example when it is exported for all steps)
  without the action failing. The input takes precedence. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/48">#48</a></li>
  </ul>
  <h2>v1.7.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>dry-run</code> input: logs which artifacts would be
  removed without deleting anything.</li>
  <li>Stricter input validation. <code>age</code> now rejects fractional
  amounts and units that are not durations (for example <code>30 D</code>,
  which moment silently treated as zero); <code>skip-recent</code> and
  <code>max-retries</code> must be non-negative integers. Previously such
  values could make every artifact eligible for deletion.</li>
  <li>Artifacts without commit information are reported separately from
  tagged ones when <code>skip-tags</code> is on.</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>Rewritten in TypeScript under <code>src/</code>, bundled with
  esbuild</li>
  <li>Unit tests for input parsing and the cleanup plan, plus end-to-end
  tests against a mock GitHub API covering deletion, rate limit retries
  and failure handling</li>
  <li>CI split into lint, typecheck, test, build and run jobs</li>
  <li>Dropped dependencies: yn, dotenv-safe, cross-env,
  eslint-plugin-import</li>
  </ul>
  <h2>v1.6.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>Artifacts are now listed repo-wide instead of per workflow run. This
  cuts API requests by roughly two orders of magnitude and removes the
  hardcoded 90-day window, so artifacts on repositories with longer
  retention are now cleaned up too. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/62">#62</a></li>
  <li>A failed deletion no longer aborts the run: remaining artifacts are
  still processed and the action fails at the end with a count.</li>
  <li>With <code>skip-tags</code>, artifacts without commit information
  are kept rather than deleted.</li>
  <li>The log ends with a summary of removed and skipped artifacts. Fixes
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/21">#21</a></li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>CI checks that <code>dist/</code> matches the source instead of
  auto-committing it</li>
  <li>Removed CodeQL workflow, pre-commit hooks and
  eslint-plugin-import</li>
  <li>Dependency purposes documented in <code>package.json</code></li>
  </ul>
  <h2>v1.5.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>max-retries</code> input caps how often a rate-limited
  request is retried before the action fails. <strong>Default: 5.</strong>
  Previously requests were retried indefinitely; set a larger value to
  keep the old behaviour. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/36">#36</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/49">#49</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/51">#51</a></li>
  <li>Action runtime updated to Node 24 (<a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/63">#63</a>)</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>All dependencies upgraded (<code>@actions/core</code> 3,
  <code>@octokit/action</code> 8, <code>@octokit/plugin-throttling</code>
  11, moment 2.30). <code>pnpm audit</code> reports no known
  vulnerabilities.</li>
  <li>Source converted to ESM, bundled with <code>@vercel/ncc</code></li>
  <li>Tooling: pnpm, ESLint 10, Prettier 3, CI on Node 24</li>
  <li>Docs: <code>action.yml</code> description, updated retention docs
  link</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/62c2fbea931baa7dd4a6b73ea5a799984a818f61"><code>62c2fbe</code></a>
  Bump version to 1.8.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/449a616233a48dbdd28ba5e08f4c2fb62913afa8"><code>449a616</code></a>
  Add skip-recent-commits input and accept GITHUB_TOKEN from env and
  input</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/4bff15786ba0b91dd8ed7c32459eb72441ac1b6c"><code>4bff157</code></a>
  Bump version to 1.7.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/a52e55eb4fd2dd1ce50f4e125d7e5855873bb38a"><code>a52e55e</code></a>
  Add end-to-end tests against a mock GitHub API</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/03f14e2351077f8bc463a7887eba3d4c062347b1"><code>03f14e2</code></a>
  Simplify config parsing, logging and tsconfig</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/04de7b0694b817261c05361cebc55090c8be4fb8"><code>04de7b0</code></a>
  Address review findings on the TypeScript rewrite</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/8b74b1b6fcb2881415de6d93701d4f4de6b170b1"><code>8b74b1b</code></a>
  Rewrite in TypeScript, add tests, merge CI workflows</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/73aaf4a5bf7a8fc25eca958284e770e44493029a"><code>73aaf4a</code></a>
  Bump version to 1.6.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/c4da97c8ee1e02b19ba57ae62c3fafd4b618e06d"><code>c4da97c</code></a>
  Ignore CLAUDE.local.md</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/614c11c542a610a4eec69c8e2faa27904004155f"><code>614c11c</code></a>
  Describe each dependency in package.json</li>
  <li>Additional commits viewable in <a
  href="https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=c-hive/gha-remove-artifacts&package-manager=github_actions&previous-version=1.4.0&new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`72cf508`](https://github.com/ghostty-org/ghostty/commit/72cf508551cb1c559c9ca32330e9647399031ebb) renderer: never stop the display link while holding the draw mutex ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes
  the same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`623106c`](https://github.com/ghostty-org/ghostty/commit/623106cc4ea9ad5b8cc070e5e5c5260eb6eeaa7b) config: rebuild RepeatableCommand's C mirror on clone ([#14170](https://github.com/ghostty-org/ghostty/issues/14170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Why
  
  `RepeatableCommand.clone` copies `value_c` shallowly: the cloned
  `Command.C` structs keep string pointers into the *source* config's
  memory, so the clone only stays valid as long as its source lives. Every
  other field of a config clone is a deep copy — this is the one spot
  where the clone silently borrows.
  
  The macOS app never notices because of how it rotates configs: its
  clone's source is the core-owned live config, and both are replaced
  together on the next reload, so a clone never outlives its source. An
  embedder that clones a config and then frees the source — a legal
  sequence, e.g. promoting the clone to be the new active config — reads
  freed memory the next time it fetches `command-palette-entry` through
  the C API. Caught by AddressSanitizer.
  
  History: the shallow copy is as old as the C exposure itself.
  `dbe6035da` introduced `RepeatableCommand` with a correct deep `clone`
  (zig-side `value` only); `017021787` added the `value_c` mirror for
  `ghostty_config_get`, maintaining it carefully in `init`/`parseCLI` but
  extending `clone` with only the mechanical `ArrayList.clone` — the
  struct array copies, the string ownership doesn't. Nothing in-tree
  exercises clone-then-free-source, so it stayed latent.
  
  ## What
  
  Rebuild the C mirror from the cloned commands using the same
  `Command.cval` path `parseCLI` uses, so the clone's C strings live in
  the clone's own allocation. A regression test asserts the clone's C
  strings do not alias the source's while staying equal in content.
  
  ## AI disclosure
  
  Developed with AI assistance (Claude Code). The bug was found by
  AddressSanitizer while testing the Windows embedding host; the
  root-cause analysis, the fix, and the regression test were produced in
  an AI-assisted session, then reviewed and verified by the submitter
  (ASan clean after the fix, `RepeatableCommand` tests passing).
  ```
- [`82232ec`](https://github.com/ghostty-org/ghostty/commit/82232ecde55405559dec29c5466cb9e39938cb41) renderer: never stop the display link while holding the draw mutex ([#14171](https://github.com/ghostty-org/ghostty/issues/14171)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes the
  same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`dd2edd7`](https://github.com/ghostty-org/ghostty/commit/dd2edd760da6b90b01ef88f75e1bea8a71b31e3f) libvt: return safe pointers for empty output ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```
- [`b0c421f`](https://github.com/ghostty-org/ghostty/commit/b0c421fcd2e290629d4285c181b52fe2f2095f06) libghostty: return safe pointers for empty output ([#14177](https://github.com/ghostty-org/ghostty/issues/14177)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```
- [`1ff027c`](https://github.com/ghostty-org/ghostty/commit/1ff027c3322864c3c28e701496c8e9d5c14cd4ee) i18n(hr): started updating hr translation ([@Filip7](https://github.com/Filip7))
  ```text
  Related issue #13766
  ```
- [`437dce2`](https://github.com/ghostty-org/ghostty/commit/437dce21bc4853b89af56daa88a5fd5af2911d75) Update hr.po ([@kristina8888](https://github.com/kristina8888))
  ```text
  added new translations for croatian language
  ```
- [`edf3aa0`](https://github.com/ghostty-org/ghostty/commit/edf3aa01bb4d4ce2544f58213eb98c0b90c99911) i18n(hr): added more translations and fixes ([@Filip7](https://github.com/Filip7))
- [`c01c683`](https://github.com/ghostty-org/ghostty/commit/c01c683eb0564b741de6f535e95c3ffc43aff59b) i18n(hr): "toggle" string translations ([@Filip7](https://github.com/Filip7))
  ```text
  i18n(hr): add missing translations and correct some others
  ```
- [`d1ed60d`](https://github.com/ghostty-org/ghostty/commit/d1ed60d569292c249ddfba42a91d452865c34762) Update hr.po ([@kristina8888](https://github.com/kristina8888))
- [`68852fc`](https://github.com/ghostty-org/ghostty/commit/68852fc008e0d14391fb284d3bbfb2276efd4033) i18n(hr): unify translation ([@Filip7](https://github.com/Filip7))
  ```text
  Use "zaslon" instead of "ekran"
  ```
- [`4480625`](https://github.com/ghostty-org/ghostty/commit/448062571c5edf010b7490d06869b88b5ebf8f80) i18n: Started updating hr translation ([#14019](https://github.com/ghostty-org/ghostty/issues/14019)) ([@trag1c](https://github.com/trag1c))
  ```text
  Related issue #13766
  ```
- [`0b54463`](https://github.com/ghostty-org/ghostty/commit/0b54463649eee14c0628cc7ab95065f8a299e73c) terminal/kitty: reject unsafe Windows paths for image file mediums ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty graphics file and temporary file mediums open a
  client-supplied path and the Kitty specification only specifies the
  blocklist for Unix-style machines.
  
  Windows has various unsafe paths as well that we should very obviously
  block. This diverges from the Kitty specification for now (I plan
  on reporting this upstream and asking for feedback) but I think its the
  right move for security.
  
  Windows dangerous namespaces:
  
    - A UNC path (`\\server\share\x`, also `//server/share/x`) makes the
      process resolve the host and authenticate to it over SMB.
    - The device namespaces (`\\.\`, `\\?\`, `\??\`) reach raw volumes and
      named pipes, where the open connects to something or blocks.
    - Reserved DOS device names (CON, NUL, COM1, ...) resolve to devices
      from inside any directory.
  
  These are now blocked.
  
  This commit also heap allocates the path buffer because max path on
  windows is around 100KB. :)
  ```
- [`7adbb51`](https://github.com/ghostty-org/ghostty/commit/7adbb5160d24bde9a65b5999d1ccd6ea4ec053b5) build/libghostty-vt: export uucode so that it can be re-used ([@jcollie](https://github.com/jcollie))
- [`cf4de79`](https://github.com/ghostty-org/ghostty/commit/cf4de795be50ec5bfe6675803a3371d4055f2beb) kitty: reject unsafe Windows paths for image file mediums ([#14189](https://github.com/ghostty-org/ghostty/issues/14189)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty graphics file and temporary file mediums open a
  client-supplied path and the Kitty specification only specifies the
  blocklist for Unix-style machines.
  
  Windows has various unsafe paths as well that we should very obviously
  block. This diverges from the Kitty specification for now (I plan on
  reporting this upstream and asking for feedback) but I think its the
  right move for security.
  
  Windows dangerous namespaces:
  
  - A UNC path (`\\server\share\x`, also `//server/share/x`) makes the
  process resolve the host and authenticate to it over SMB.
  - The device namespaces (`\\.\`, `\\?\`, `\??\`) reach raw volumes and
  named pipes, where the open connects to something or blocks.
  - Reserved DOS device names (CON, NUL, COM1, ...) resolve to devices
  from inside any directory.
  
  These are now blocked.
  
  This commit also heap allocates the path buffer because max path on
  windows is around 100KB. :)\
  
  **AI usage:** Fable and Astra both helped with validation, edge cases.
  ```
- [`60b4306`](https://github.com/ghostty-org/ghostty/commit/60b43068c5fc74c2117877b8ac4ecf9321bb8f24) terminal: reclaim pooled and compressed page memory on Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds memory decommit/recommit support to Windows via
  DiscardVirtualMemory. This allows unused page memory to be reclaimed
  the same way it is already today on Linux and macOS.
  
  DiscardVirtualMemory releases the physical pages behind a committed
  range but leaves it committed, so a later access finds a zero page or
  the old contents rather than faulting, and nothing has to be committed
  again before reuse. That keeps recommit a no-op and, more importantly,
  keeps restoring a compressed page infallible.
  
  Windows has an alternative `VirtualFree(MEM_DECOMMIT)` followed by
  `VirtualAlloc(MEM_COMMIT)` which releases the commit charge as well, but
  Windows has no overcommit, so the commit can be refused on restore and our
  restore path doesn't support OOM.
  
  https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory
  ```
- [`7644e6d`](https://github.com/ghostty-org/ghostty/commit/7644e6d627ede8042db16d264ed3d118d8832923) build/linghostty-vt: fix libvaxis access to uucode tables ([@jcollie](https://github.com/jcollie))
- [`95cfbbb`](https://github.com/ghostty-org/ghostty/commit/95cfbbb055c659f57da3650cfb733dbb5072f6a5) terminal: reclaim pooled and compressed page memory on Windows ([#14190](https://github.com/ghostty-org/ghostty/issues/14190)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds memory decommit/recommit support to Windows via
  DiscardVirtualMemory. This allows unused page memory to be reclaimed the
  same way it is already today on Linux and macOS.
  
  DiscardVirtualMemory releases the physical pages behind a committed
  range but leaves it committed, so a later access finds a zero page or
  the old contents rather than faulting, and nothing has to be committed
  again before reuse. That keeps recommit a no-op and, more importantly,
  keeps restoring a compressed page infallible.
  
  Windows has an alternative `VirtualFree(MEM_DECOMMIT)` followed by
  `VirtualAlloc(MEM_COMMIT)` which releases the commit charge as well, but
  Windows has no overcommit, so the commit can be refused on restore and
  our restore path doesn't support OOM.
  
  
  https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory
  ```
- [`4a70ee4`](https://github.com/ghostty-org/ghostty/commit/4a70ee4718ba0967bcfd72f43adb715bf65a860d) build/libghostty-vt: fixed to the build system for programs that embed libghostty-vt and libvaxis ([#14191](https://github.com/ghostty-org/ghostty/issues/14191)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Two small patches that don't directly affect Ghostty, but do affect
  programs that embed `libghostty-vt` and `libvaxis`, or
  any other combination that also uses `uucode`.
  
  AI disclosure: these bugs were discovered/fixed by Claude, but I've
  rewritten parts of the patches and the comments.
  
  CC @rockorager
  ```
- [`f6cb831`](https://github.com/ghostty-org/ghostty/commit/f6cb8312b38088e4038296ecc5dde3f23c83fd94) tinyio: implement a Windows version and use it in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements TinyIO for Windows which is used to save binary and runtime
  costs. As a reminder, binary costs are saved because `std.Io` uses a
  vtable so compilers can't prune any unused functions, so you pay for the
  full cost. We can noop unused functions to save. Runtime is saved
  because there is less state to carry for unused functionality like
  concurrency primitives.
  
  The impl itself is mostly taken from Zig directly. I ran tests on
  Windows (arm64) and verified everything works as expected so far!
  
  Binary size measurements before/after:
  
    | Mode         | Io owner        | ghostty-vt.dll | vs. Threaded |
    |--------------|-----------------|---------------:|-------------:|
    | ReleaseFast  | std.Io.Threaded |      2,209,280 |              |
    | ReleaseFast  | std.Io.failing  |      1,815,552 |     -393,728 |
    | ReleaseFast  | TinyIo          |      1,826,816 |     -382,464 |
    | ReleaseSmall | std.Io.Threaded |      1,541,632 |              |
    | ReleaseSmall | std.Io.failing  |      1,190,912 |     -350,720 |
    | ReleaseSmall | TinyIo          |      1,199,616 |     -342,016 |
  
  The runtime savings are relatively small, but 1KB per terminal ain't nothing:
  
    | Io owner        | Private, +100 terminals | Private, startup |
    |-----------------|------------------------:|-----------------:|
    | std.Io.Threaded |            +161,845,248 |          782,336 |
    | TinyIo          |            +161,742,848 |          729,088 |
  ```
- [`fde3449`](https://github.com/ghostty-org/ghostty/commit/fde3449b348d8e36c0d52fd39bb33ea66744b958) tinyio: implement a Windows version and use it in the C API ([#14193](https://github.com/ghostty-org/ghostty/issues/14193)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements TinyIO for Windows which is used to save binary and runtime
  costs. As a reminder, binary costs are saved because `std.Io` uses a
  vtable so compilers can't prune any unused functions, so you pay for the
  full cost. We can noop unused functions to save. Runtime is saved
  because there is less state to carry for unused functionality like
  concurrency primitives.
  
  The impl itself is mostly taken from Zig directly. I ran tests on
  Windows (arm64) and verified everything works as expected so far!
  
  Binary size measurements before/after:
  
    | Mode         | Io owner        | ghostty-vt.dll | vs. Threaded |
    |--------------|-----------------|---------------:|-------------:|
    | ReleaseFast  | std.Io.Threaded |      2,209,280 |              |
    | ReleaseFast  | TinyIo          |      1,826,816 |     -382,464 |
    | ReleaseSmall | std.Io.Threaded |      1,541,632 |              |
    | ReleaseSmall | TinyIo          |      1,199,616 |     -342,016 |
  
  The runtime savings are relatively small, but 1KB per terminal ain't
  nothing:
  
    | Io owner        | Private, +100 terminals | Private, startup |
    |-----------------|------------------------:|-----------------:|
    | std.Io.Threaded |            +161,845,248 |          782,336 |
    | TinyIo          |            +161,742,848 |          729,088 |
  ```
- [`8c17235`](https://github.com/ghostty-org/ghostty/commit/8c17235f8d1447ae3b5109d1c3a7d1256a9b2de4) Update VOUCHED list ([#14195](https://github.com/ghostty-org/ghostty/issues/14195)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14194#issuecomment-5608205535)
  from @trag1c.
  
  Vouch: @neoto
  ```
- [`466439b`](https://github.com/ghostty-org/ghostty/commit/466439bdfc868da880d7abefbe698df35d05f9aa) Update VOUCHED list ([#14205](https://github.com/ghostty-org/ghostty/issues/14205)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14179#discussioncomment-18381789)
  from @jcollie.
  
  Vouch: @korikhin
  ```

