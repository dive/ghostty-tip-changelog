> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 17, 2026 at 23:20 UTC.

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

