> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 31, 2026 at 20:35 UTC.

## August 31, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33421529945), [2](https://github.com/ghostty-org/ghostty/actions/runs/33398446520), [3](https://github.com/ghostty-org/ghostty/actions/runs/33352467854), [4](https://github.com/ghostty-org/ghostty/actions/runs/33343337803)  
Summary: 4 runs • 30 commits • 5 authors

### Changes

- [`d23af9e`](https://github.com/ghostty-org/ghostty/commit/d23af9e397dfe06760ce2ad8f54fb178e7d82e62) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`80b8e49`](https://github.com/ghostty-org/ghostty/commit/80b8e4957625195e85727a6c28200f3bf6c54941) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`5546750`](https://github.com/ghostty-org/ghostty/commit/5546750a75cf44f881c43f44204aa6a9012ab296) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`1510d2b`](https://github.com/ghostty-org/ghostty/commit/1510d2b42a284c183e1fd71749290c220e23ce3d) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`b5817a3`](https://github.com/ghostty-org/ghostty/commit/b5817a35a493eb68dbe3737802384792c561ef06) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`f6244f7`](https://github.com/ghostty-org/ghostty/commit/f6244f7d7f2d555382192e701cd6bc33859b64b6) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`320ba75`](https://github.com/ghostty-org/ghostty/commit/320ba75dc925096bc9b31d4de756b2779380dcd3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`1054be4`](https://github.com/ghostty-org/ghostty/commit/1054be4b6ff66c63f4f703c38d06a547c12d79ba) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`6758251`](https://github.com/ghostty-org/ghostty/commit/675825163b3aa975fe66f577e99b75982b15d45b) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`768bc2e`](https://github.com/ghostty-org/ghostty/commit/768bc2ed475ede520dbe0695184a9e2c4aec9128) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`4c696b9`](https://github.com/ghostty-org/ghostty/commit/4c696b90c5c2db61fd0929f102e9701bbcdfb809) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`9af9348`](https://github.com/ghostty-org/ghostty/commit/9af934813a32262ab525673840ccd76ed7df2f52) Merge from upstream ([@mohshami](https://github.com/mohshami))
- [`58f43d5`](https://github.com/ghostty-org/ghostty/commit/58f43d56289d234271e1e829712e2f043c88278f) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`c8c4526`](https://github.com/ghostty-org/ghostty/commit/c8c4526e43e6f832ab5d88759cde98a7b2129886) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`81d28be`](https://github.com/ghostty-org/ghostty/commit/81d28beaa2e3c507299d0c1a5271c2af718212e3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
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
- [`abac4c2`](https://github.com/ghostty-org/ghostty/commit/abac4c2cb8122540d99f30645581918022a31fc8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`0dc2032`](https://github.com/ghostty-org/ghostty/commit/0dc2032e6ab5f197f1d93f8eb1f1735a2b5091e1) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
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
- [`0525c18`](https://github.com/ghostty-org/ghostty/commit/0525c18f60ade456a484d9dc26e751d3c1b3993d) i18n: adjust and extend Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`c50288c`](https://github.com/ghostty-org/ghostty/commit/c50288c35fd147482dbd7e30cfcc414c7612c7dd) i18n: address comments for Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`2a51bdf`](https://github.com/ghostty-org/ghostty/commit/2a51bdf1266df638e9ba49ad5cfad6ee7c780ca3) i18n: return Ghostty to Ukrainian translation ([@chernetskyi](https://github.com/chernetskyi))
- [`1026a00`](https://github.com/ghostty-org/ghostty/commit/1026a00c19b3cbf254c0b85dced92ab8e63d77bf) i18n: adjust Ukrainian translations ([@chernetskyi](https://github.com/chernetskyi))
- [`d4d8f62`](https://github.com/ghostty-org/ghostty/commit/d4d8f62262cb1a974a7d2470d5f79f811fab15e4) i18n: adjust and extend Ukrainian translation ([#13854](https://github.com/ghostty-org/ghostty/issues/13854)) ([@trag1c](https://github.com/trag1c))
- [`e8aa098`](https://github.com/ghostty-org/ghostty/commit/e8aa098674a42e2b4ed1b8c42f4224564ad9fc1e) Update VOUCHED list ([#14092](https://github.com/ghostty-org/ghostty/issues/14092)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14091#discussioncomment-18212381)
  from @pluiedev.
  
  Denounce: @thomas-trijindev
  ```
- [`ec3e384`](https://github.com/ghostty-org/ghostty/commit/ec3e384d2d7d86206fc3c71aa23a76b7bdb5eae9) Sync CODEOWNERS vouch list ([#14090](https://github.com/ghostty-org/ghostty/issues/14090)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @jakeriksen
  - @Kleshzz
  ```

## August 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33336500501), [2](https://github.com/ghostty-org/ghostty/actions/runs/33304806060), [3](https://github.com/ghostty-org/ghostty/actions/runs/33301014311), [4](https://github.com/ghostty-org/ghostty/actions/runs/33290237904), [5](https://github.com/ghostty-org/ghostty/actions/runs/33288542884), [6](https://github.com/ghostty-org/ghostty/actions/runs/33286306984)  
Summary: 6 runs • 15 commits • 7 authors

### Changes

- [`c181983`](https://github.com/ghostty-org/ghostty/commit/c181983253129f2803891a2d801951244ae5313c) build: update Sparkle to 2.9.6 and pin SPM ([@bo2themax](https://github.com/bo2themax))
- [`7fd93e0`](https://github.com/ghostty-org/ghostty/commit/7fd93e09ca6cbca7c4c4c0dbf2817ca49a82a2a4) build: update Sparkle to 2.9.6 and pin SPM ([#14082](https://github.com/ghostty-org/ghostty/issues/14082)) ([@mitchellh](https://github.com/mitchellh))
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
- [`6d850fe`](https://github.com/ghostty-org/ghostty/commit/6d850fef7780f3461ee526eba16077ea9d7df8a6) Update VOUCHED list ([#14084](https://github.com/ghostty-org/ghostty/issues/14084)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14083#discussioncomment-18204946)
  from @jcollie.
  
  Vouch: @mgsloan
  ```
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
- [`166d2fe`](https://github.com/ghostty-org/ghostty/commit/166d2fe34d65bd1fa393fd8a213c57bc6119dfb9) build: update Sparkle to 2.9.4 ([@Svector-anu](https://github.com/Svector-anu))
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
- [`98cd670`](https://github.com/ghostty-org/ghostty/commit/98cd670c0c2ccdd3f22c40c65a3306e933643ada) Update VOUCHED list ([#14079](https://github.com/ghostty-org/ghostty/issues/14079)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14078#discussioncomment-18203195)
  from @jcollie.
  
  Vouch: @and-rs
  ```
- [`094d175`](https://github.com/ghostty-org/ghostty/commit/094d175efa506f87c296fd8a51371c68eea191b9) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`0a76c31`](https://github.com/ghostty-org/ghostty/commit/0a76c311527a20727764e3281eb4efa8c350058a) Update iTerm2 colorschemes ([#14077](https://github.com/ghostty-org/ghostty/issues/14077)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260824-153547-75c93ee
  ```

## August 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33261764252), [2](https://github.com/ghostty-org/ghostty/actions/runs/33259592247)  
Summary: 2 runs • 5 commits • 3 authors

### Changes

- [`7b47213`](https://github.com/ghostty-org/ghostty/commit/7b47213f94058c3715205ce8fa73f7ae581a652c) Update VOUCHED list ([#14074](https://github.com/ghostty-org/ghostty/issues/14074)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14072#issuecomment-5463405035)
  from @bo2themax.
  
  Vouch: @Svector-anu
  ```
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

## August 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33201228282), [2](https://github.com/ghostty-org/ghostty/actions/runs/33140987507)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`777929a`](https://github.com/ghostty-org/ghostty/commit/777929a8fe603574474f6e1c9c0a35c08af1a2d9) macOS: review windows when closing multiple tabs ([@bo2themax](https://github.com/bo2themax))
- [`4540d49`](https://github.com/ghostty-org/ghostty/commit/4540d499ae463ad7b90f28f6f852f64f844c160f) macOS: review windows when closing multiple tabs ([#14062](https://github.com/ghostty-org/ghostty/issues/14062)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We can also make close undoable when quitting, i'll add it as a follow
  up pr.
  
  <img width="573" height="450" alt="Xnip2026-08-28_19-25-02"
  src="https://github.com/user-attachments/assets/3b4f34f4-9ee6-4180-beb7-f90e98c8aa40"
  />
  ```
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

## August 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33124382421), [2](https://github.com/ghostty-org/ghostty/actions/runs/33121250277), [3](https://github.com/ghostty-org/ghostty/actions/runs/33114064367), [4](https://github.com/ghostty-org/ghostty/actions/runs/33096957391), [5](https://github.com/ghostty-org/ghostty/actions/runs/33036403965), [6](https://github.com/ghostty-org/ghostty/actions/runs/33034019716)  
Summary: 6 runs • 25 commits • 7 authors

### Changes

- [`4bb135e`](https://github.com/ghostty-org/ghostty/commit/4bb135e2de19b2ce8bddec77ba964ddaebbadc1e) i18n(ru): start updating Russian translation ([@derVedro](https://github.com/derVedro))
- [`1dd31f9`](https://github.com/ghostty-org/ghostty/commit/1dd31f9e9458ac1bf44860d55021f9d54e53c646) i18n(ru): work in progress on Russian translation ([@derVedro](https://github.com/derVedro))
- [`3f87b2e`](https://github.com/ghostty-org/ghostty/commit/3f87b2e5817429fd123af2c980cf6798017b75a1) i18n(ru): second part of Russian translation ([@derVedro](https://github.com/derVedro))
- [`32159b6`](https://github.com/ghostty-org/ghostty/commit/32159b6fe6714a8401d5ad21ce8487ac0266afd8) i18n(ru): small fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`0a396b4`](https://github.com/ghostty-org/ghostty/commit/0a396b43dccee62e61e2f17643262b800fd7699b) i18n(ru): context menu fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`ba35746`](https://github.com/ghostty-org/ghostty/commit/ba35746377788b8953a895559a91c6e1733c18da) i18n(ru): improve Russian translation ([@derVedro](https://github.com/derVedro))
- [`6244458`](https://github.com/ghostty-org/ghostty/commit/6244458a11f7c83c9c8774d2f5d27aba027c00fc) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`84dff76`](https://github.com/ghostty-org/ghostty/commit/84dff76b1383f0535657902b64cb614a34bd48e8) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`915977a`](https://github.com/ghostty-org/ghostty/commit/915977a484da9d9b93b3a30ac80ff068c5c3c6a8) i18n(ru): equalize splits ([@derVedro](https://github.com/derVedro))
- [`278b4e2`](https://github.com/ghostty-org/ghostty/commit/278b4e2fc7aab0c5073afdfe2570f27a5a4b9142) i18n(ru): refine Russian translation ([@derVedro](https://github.com/derVedro))
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
- [`572fd58`](https://github.com/ghostty-org/ghostty/commit/572fd5837728da2363168f035743597767b5b237) macOS: use the same default BellFeatures as config ([@bo2themax](https://github.com/bo2themax))
- [`4f4589f`](https://github.com/ghostty-org/ghostty/commit/4f4589f31f2ca196fc88731dfcdc77e1cbde9852) macOS: use the same default BellFeatures as config ([#14049](https://github.com/ghostty-org/ghostty/issues/14049)) ([@mitchellh](https://github.com/mitchellh))
- [`28b5bf9`](https://github.com/ghostty-org/ghostty/commit/28b5bf905986f9e795466b7995640d80c44c16bc) font: update embedded Noto emoji fonts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14046
  
  Update Noto Color Emoji from v2.034 to v2.051 and Noto Emoji
  Regular from v1.002 to v3.005.
  
  The old assets predate Unicode 15.0 and decompose newer ZWJ sequences
  into separate glyphs. This causes sequences such as the Emoji 15.1
  head-shaking faces to overlap neighboring terminal cells. The new
  assets provide the missing sequence glyphs through Unicode 17.0.
  
  New supported glyphs too:
  
  | Codepoint | Glyph | Name |
  |-----------|-------|------|
  | U+1F6D8 | 🛘 | LANDSLIDE |
  | U+1F6DC | 🛜 | WIRELESS |
  | U+1FA75 | 🩵 | LIGHT BLUE HEART |
  | U+1FA76 | 🩶 | GREY HEART |
  | U+1FA77 | 🩷 | PINK HEART |
  | U+1FA87 | 🪇 | MARACAS |
  | U+1FA88 | 🪈 | FLUTE |
  | U+1FA89 | 🪉 | HARP |
  | U+1FA8A | 🪊 | TROMBONE |
  | U+1FA8E | 🪎 | TREASURE CHEST |
  | U+1FA8F | 🪏 | SHOVEL |
  | U+1FAAD | 🪭 | FOLDING HAND FAN |
  | U+1FAAE | 🪮 | HAIR PICK |
  | U+1FAAF | 🪯 | KHANDA |
  | U+1FABB | 🪻 | HYACINTH |
  | U+1FABC | 🪼 | JELLYFISH |
  | U+1FABD | 🪽 | WING |
  | U+1FABE | 🪾 | LEAFLESS TREE |
  | U+1FABF | 🪿 | GOOSE |
  | U+1FAC6 | 🫆 | FINGERPRINT |
  | U+1FAC8 | 🫈 | HAIRY CREATURE |
  | U+1FACD | 🫍 | ORCA |
  | U+1FACE | 🫎 | MOOSE |
  | U+1FACF | 🫏 | DONKEY |
  | U+1FADA | 🫚 | GINGER ROOT |
  | U+1FADB | 🫛 | PEA POD |
  | U+1FADC | 🫜 | ROOT VEGETABLE |
  | U+1FADF | 🫟 | SPLATTER |
  | U+1FAE8 | 🫨 | SHAKING FACE |
  | U+1FAE9 | 🫩 | FACE WITH BAGS UNDER EYES |
  | U+1FAEA | 🫪 | DISTORTED FACE |
  | U+1FAEF | 🫯 | FIGHT CLOUD |
  | U+1FAF7 | 🫷 | LEFTWARDS PUSHING HAND |
  | U+1FAF8 | 🫸 | RIGHTWARDS PUSHING HAND |
  ```
- [`890aa63`](https://github.com/ghostty-org/ghostty/commit/890aa63dbbd586c6687a60b3736109203649d8dc) font: update embedded Noto emoji fonts ([#14047](https://github.com/ghostty-org/ghostty/issues/14047)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14046
  
  Update Noto Color Emoji from v2.034 to v2.051 and Noto Emoji Regular
  from v1.002 to v3.005.
  
  The old assets predate Unicode 15.0 and decompose newer ZWJ sequences
  into separate glyphs. This causes sequences such as the Emoji 15.1
  head-shaking faces to overlap neighboring terminal cells. The new assets
  provide the missing sequence glyphs through Unicode 17.0.
  
  New supported glyphs too:
  
  | Codepoint | Glyph | Name |
  |-----------|-------|------|
  | U+1F6D8 | 🛘 | LANDSLIDE |
  | U+1F6DC | 🛜 | WIRELESS |
  | U+1FA75 | 🩵 | LIGHT BLUE HEART |
  | U+1FA76 | 🩶 | GREY HEART |
  | U+1FA77 | 🩷 | PINK HEART |
  | U+1FA87 | 🪇 | MARACAS |
  | U+1FA88 | 🪈 | FLUTE |
  | U+1FA89 | 🪉 | HARP |
  | U+1FA8A | 🪊 | TROMBONE |
  | U+1FA8E | 🪎 | TREASURE CHEST |
  | U+1FA8F | 🪏 | SHOVEL |
  | U+1FAAD | 🪭 | FOLDING HAND FAN |
  | U+1FAAE | 🪮 | HAIR PICK |
  | U+1FAAF | 🪯 | KHANDA |
  | U+1FABB | 🪻 | HYACINTH |
  | U+1FABC | 🪼 | JELLYFISH |
  | U+1FABD | 🪽 | WING |
  | U+1FABE | 🪾 | LEAFLESS TREE |
  | U+1FABF | 🪿 | GOOSE |
  | U+1FAC6 | 🫆 | FINGERPRINT |
  | U+1FAC8 | 🫈 | HAIRY CREATURE |
  | U+1FACD | 🫍 | ORCA |
  | U+1FACE | 🫎 | MOOSE |
  | U+1FACF | 🫏 | DONKEY |
  | U+1FADA | 🫚 | GINGER ROOT |
  | U+1FADB | 🫛 | PEA POD |
  | U+1FADC | 🫜 | ROOT VEGETABLE |
  | U+1FADF | 🫟 | SPLATTER |
  | U+1FAE8 | 🫨 | SHAKING FACE |
  | U+1FAE9 | 🫩 | FACE WITH BAGS UNDER EYES |
  | U+1FAEA | 🫪 | DISTORTED FACE |
  | U+1FAEF | 🫯 | FIGHT CLOUD |
  | U+1FAF7 | 🫷 | LEFTWARDS PUSHING HAND |
  | U+1FAF8 | 🫸 | RIGHTWARDS PUSHING HAND |
  ```
- [`6229d4e`](https://github.com/ghostty-org/ghostty/commit/6229d4eb62f9e2483b3ea00c11fcde70590d2d84) macOS: fix AppleScript send key for non-control keys ([@bo2themax](https://github.com/bo2themax))
- [`e9ad4b1`](https://github.com/ghostty-org/ghostty/commit/e9ad4b1d631ec91c8cad401700fee1754612ef33) macOS: fix non control keys are not working for AppleScript ([#13205](https://github.com/ghostty-org/ghostty/issues/13205)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `send key` only works for control keys like `enter` currently; this adds
  (fixes) the support for other keys listed as available. Found by
  @paaloeye in #13180
  
  The core of this fix is relying on `UCKeyTranslate` to get the
  corresponding character and code point from a key code using
  `KeyboardLayout.character(for:modifiers:)`.
  
  ScriptKeyEventCommand now respects `macos-option-as-alt`, and attach
  `text`, `unshifted_codepoint` and `consumed_mods` under the same
  condition as a manual input events like in `performKeyEquivalent` and
  `localEventKeyDown`.
  
  ## AI Disclosure
  
  Claude did the heavy lifting, I reviewed and rephrased some of the
  comments it generated. And ofc reviewed and tested myself.
  ```
- [`ee8095d`](https://github.com/ghostty-org/ghostty/commit/ee8095d37d9813669688cf2f666756e607b84713) terminal/snapshot: use stack fallback for record scratch ([@jparise](https://github.com/jparise))
  ```text
  Use a bounded 512-byte stack fallback for complete-snapshot record
  scratch. Small records avoid heap growth while larger records continue
  through the heap allocator.
  ```
- [`f2d5758`](https://github.com/ghostty-org/ghostty/commit/f2d5758f6305867dc36b36293c6165d8152b853e) terminal/snapshot: use stack fallback for record scratch ([#14018](https://github.com/ghostty-org/ghostty/issues/14018)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use a bounded 512-byte stack fallback for complete-snapshot record
  scratch. Small records avoid heap growth while larger records continue
  through the heap allocator.
  
  This usually means 2 fewer allocations per encode, resulting in a small
  performance improvement in a local benchmark:
  
  | Workload | `main` median | Branch median | Change |
  |---|---:|---:|---:|
  | Empty, 50k encodes | 135.06 ms | 130.76 ms | **3.2% faster** |
  | 1 MiB ASCII, 500 encodes | 280.75 ms | 281.25 ms | **0.2% slower**,
  within noise |
  | 1 MiB styled, 200 encodes | 1,023.02 ms | 996.32 ms | **2.6% faster**
  |
  ```
- [`522ebdd`](https://github.com/ghostty-org/ghostty/commit/522ebdd0a313ef366d3567694e3588b780fae8ee) build(deps): bump hustcer/milestone-action from 3.1 to 3.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [hustcer/milestone-action](https://github.com/hustcer/milestone-action) from 3.1 to 3.2.
  - [Release notes](https://github.com/hustcer/milestone-action/releases)
  - [Changelog](https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/hustcer/milestone-action/compare/ebed8d5daafd855a600d7e665c1b130f06d24130...2f38355153344ccaaa44b5b5fcff9f604dff1b45)
  
  ---
  updated-dependencies:
  - dependency-name: hustcer/milestone-action
    dependency-version: '3.2'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`f349d10`](https://github.com/ghostty-org/ghostty/commit/f349d108431007dac0d908af33301e3cc460b2f3) build(deps): bump hustcer/milestone-action from 3.1 to 3.2 ([#14040](https://github.com/ghostty-org/ghostty/issues/14040)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [hustcer/milestone-action](https://github.com/hustcer/milestone-action)
  from 3.1 to 3.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/releases">hustcer/milestone-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.2</h2>
  <h2>[3.2] - 2026-08-25</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li>Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li>Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li>Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li>Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li>Upgrade Nu to 0.115.1</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md">hustcer/milestone-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.2] - 2026-08-25</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li>Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li>Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li>Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li>Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li>Upgrade Nu to 0.115.1</li>
  </ul>
  <h2>[3.1] - 2026-01-23</h2>
  <h3>Documentation</h3>
  <ul>
  <li>Update milestone-action version in README (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/162">#162</a>)</li>
  </ul>
  <h3>Features</h3>
  <ul>
  <li>Break before sleep when milestone found</li>
  </ul>
  <h3>Miscellaneous Tasks</h3>
  <ul>
  <li>Update README.md (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/166">#166</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Update Nu to 0.109.1</li>
  <li>Update Nushell to 0.110.0 (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/167">#167</a>)</li>
  <li>Upgrade hustcer/setup-nu to v3.22</li>
  </ul>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.0] - 2025-10-26</h2>
  <p>This release introduces changes that may impact some users. If the
  action fails due to insufficient permissions, please add the
  <code>issues: write</code> and <code>pull-requests: write</code>
  permissions to your workflow. Additionally, the API for binding
  milestones has been modified. Due to these changes, the major version
  has been incremented to 3.</p>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Try to fix GitHub Projects (classic) deprecation warning by using
  REST API instead of GraphQL (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/157">#157</a>)</li>
  <li>Fix &quot;Resource not accessible by integration&quot; error for
  issue milestone binding by adding <code>issues: write</code>
  permission</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/2f38355153344ccaaa44b5b5fcff9f604dff1b45"><code>2f38355</code></a>
  Bump to v3.2</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/90d61222172fcab928f4097d7ac0f9b777f8c6a6"><code>90d6122</code></a>
  deps: Upgrade Nu to 0.115.1</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/e587063f374a27424be13284709902ef21d0e7e2"><code>e587063</code></a>
  fix: Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/cc2b756fd4aa0c6296b7268f41108dc88bfb8228"><code>cc2b756</code></a>
  fix: Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/f8cedae0c15efb735341ecea49835c86190dee13"><code>f8cedae</code></a>
  fix: Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/b57a2e26d7ae416cd8f283c8ddcf0022639b0a99"><code>b57a2e2</code></a>
  fix: Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/3ba8f40c9539a0d3b5ac92732bd3a26f3a9e80df"><code>3ba8f40</code></a>
  fix: Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/1e6a3fcc554f6c07ada4feabb0b1935aa60243d3"><code>1e6a3fc</code></a>
  deps: Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/913159549289b377b4d0c9c830101da8d4c82387"><code>9131595</code></a>
  deps: Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>See full diff in <a
  href="https://github.com/hustcer/milestone-action/compare/ebed8d5daafd855a600d7e665c1b130f06d24130...2f38355153344ccaaa44b5b5fcff9f604dff1b45">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=hustcer/milestone-action&package-manager=github_actions&previous-version=3.1&new-version=3.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## August 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33015847463), [2](https://github.com/ghostty-org/ghostty/actions/runs/33003643945), [3](https://github.com/ghostty-org/ghostty/actions/runs/32980266736), [4](https://github.com/ghostty-org/ghostty/actions/runs/32953632696), [5](https://github.com/ghostty-org/ghostty/actions/runs/32932472332), [6](https://github.com/ghostty-org/ghostty/actions/runs/32929311994)  
Summary: 6 runs • 15 commits • 4 authors

### Changes

- [`b6ac6e1`](https://github.com/ghostty-org/ghostty/commit/b6ac6e1d479f29fb8194f86ec24b72901aa94c21) Revert "macOS: use same ResetZoomAccessoryView ([#14028](https://github.com/ghostty-org/ghostty/issues/14028))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 15ff186f65ca0bdbd1fa397ab03908d59de16463, reversing
  changes made to 1abd53ee537a93bb33107a415fe4f4131bcf0f5b.
  ```
- [`0a9f47c`](https://github.com/ghostty-org/ghostty/commit/0a9f47cae0bc3cb653ea52fbd4e1d632b79dd91a) macOS: update note about tab accessory view ([@bo2themax](https://github.com/bo2themax))
- [`b69f612`](https://github.com/ghostty-org/ghostty/commit/b69f612672f4e31e20dec2ee2684d295aec149f1) macOS: update note about tab accessory view ([#14038](https://github.com/ghostty-org/ghostty/issues/14038)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reverts: #14028
  ```
- [`6688aa0`](https://github.com/ghostty-org/ghostty/commit/6688aa072f87dcb169fa1a49dcf5eadc9ed87956) renderer: park DisplayLink while idle ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14033
  
  Pause the CVDisplayLink when there isn't any real work to do.
  
  Start the link after updateFrame rebuilds cells, keep it running while
  cell changes or animations remain pending, and resync it from the
  no-redraw path to sleep it again.
  
  I also did some benchmark to measure the cost of starting/stopping the
  display link since this includes a lot more of that and I found that
  a continuously running link used 29 to 35 us of CPU per callback, while
  starting and stopping it for every frame used 103 to 121 us. So, in some
  pathological case this can be worse, but its still microseconds, and in
  the normal case this helps Ghostty sleep a lot more.
  ```
- [`d9840f3`](https://github.com/ghostty-org/ghostty/commit/d9840f3c8fc230c7768ae760c412974e9fc923bb) renderer: park DisplayLink while idle ([#14035](https://github.com/ghostty-org/ghostty/issues/14035)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14033
  
  Pause the CVDisplayLink when there isn't any real work to do.
  
  Start the link after updateFrame rebuilds cells, keep it running while
  cell changes or animations remain pending, and resync it from the
  no-redraw path to sleep it again.
  
  I also did some benchmark to measure the cost of starting/stopping the
  display link since this includes a lot more of that and I found that a
  continuously running link used 29 to 35 us of CPU per callback, while
  starting and stopping it for every frame used 103 to 121 us. So, in some
  pathological case this can be worse, but its still microseconds, and in
  the normal case this helps Ghostty sleep a lot more.
  ```
- [`851751a`](https://github.com/ghostty-org/ghostty/commit/851751a1167a05d83f08c010a7b1e92f435f783f) macOS: clean up deprecated toolbar button ([@bo2themax](https://github.com/bo2themax))
- [`7a15898`](https://github.com/ghostty-org/ghostty/commit/7a15898bc813558a25c4beffd7391dad14cbb20c) macOS: use same ResetZoomAccessoryView ([@bo2themax](https://github.com/bo2themax))
- [`1abd53e`](https://github.com/ghostty-org/ghostty/commit/1abd53ee537a93bb33107a415fe4f4131bcf0f5b) macOS: clean up deprecated toolbar button ([#14027](https://github.com/ghostty-org/ghostty/issues/14027)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This button is a leftover from cf6017e777cda0e0c131b616f408c9a81644b5d7,
  we're now using tab's and titlebar's accessory view to display unzoom
  buttons, no need to keep them.
  ```
- [`15ff186`](https://github.com/ghostty-org/ghostty/commit/15ff186f65ca0bdbd1fa397ab03908d59de16463) macOS: use same ResetZoomAccessoryView ([#14028](https://github.com/ghostty-org/ghostty/issues/14028)) ([@mitchellh](https://github.com/mitchellh))
- [`73e53ce`](https://github.com/ghostty-org/ghostty/commit/73e53ceeac4d81b59d228db32de933d8114d42cd) i18n: update fr_FR translations ([@flou](https://github.com/flou))
- [`5f5b988`](https://github.com/ghostty-org/ghostty/commit/5f5b988c5236facfe8d2439203d9ee9d5b636cf8) i18n: update fr_FR translations ([#13971](https://github.com/ghostty-org/ghostty/issues/13971)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update missing french translations for Ghostty 1.4
  (https://github.com/ghostty-org/ghostty/issues/13766)
  ```
- [`40a40f8`](https://github.com/ghostty-org/ghostty/commit/40a40f848dfca8c5edbc0098dd828aec03ae8e64) terminal: ignore UTF-8-decoded C1 controls in the ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Drop UTF-8 decoded C1 controls entirely. This matches xterm's default
  behavior which is our standard policy (but note it diverges from libvte
  which executes them). There isn't really any standard I could find
  around this.
  
  The ground state UTF-8 fast paths (both the scalar decoder and the
  batched SIMD path) previously treated decoded codepoints C1 control
  codepoints as normal UTF-8 text and routed them to print.
  ```
- [`88f57ee`](https://github.com/ghostty-org/ghostty/commit/88f57ee66eeaad4da77b414b245f7b6693348985) terminal: ignore UTF-8-decoded C1 controls in the ground state ([#14023](https://github.com/ghostty-org/ghostty/issues/14023)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Drop UTF-8 decoded C1 controls entirely. This matches xterm's default
  behavior which is our standard policy (but note it diverges from libvte
  which executes them). There isn't really any standard I could find
  around this.
  
  The ground state UTF-8 fast paths (both the scalar decoder and the
  batched SIMD path) previously treated decoded codepoints C1 control
  codepoints as normal UTF-8 text and routed them to print.
  ```
- [`0f35043`](https://github.com/ghostty-org/ghostty/commit/0f35043c9ac588811f22c732ac5392850f22381e) terminal: execute C0 controls 0x10-0x1F in the ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14021
  
  The ground state UTF-8 fast paths only classified 0x00-0x0F plus 0x1B (escape)
  as C0 controls. The remaining C0 bytes (0x10-0x1A, 0x1C-0x1F) were decoded
  as ordinary codepoints and routed to print as if they were text.
  
  This resulted in incorrect grids but also very weird font fallback, e.g.
  U+0014 would find CJK fonts.
  
  This commit fixes this by routing every ground state C0 byte except ESC to
  execute as it should be.
  ```
- [`6dcf68f`](https://github.com/ghostty-org/ghostty/commit/6dcf68fc0b12e8caebbfc43770d66edac124b4f8) terminal: execute C0 controls 0x10-0x1F in the ground state ([#14022](https://github.com/ghostty-org/ghostty/issues/14022)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14021
  
  The ground state UTF-8 fast paths only classified 0x00-0x0F plus 0x1B
  (escape) as C0 controls. The remaining C0 bytes (0x10-0x1A, 0x1C-0x1F)
  were decoded as ordinary codepoints and routed to print as if they were
  text.
  
  This resulted in incorrect grids but also very weird font fallback, e.g.
  U+0014 would find CJK fonts.
  
  This commit fixes this by routing every ground state C0 byte except ESC
  to execute as it should be.
  ```

## August 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32885561859), [2](https://github.com/ghostty-org/ghostty/actions/runs/32868574536), [3](https://github.com/ghostty-org/ghostty/actions/runs/32863067913), [4](https://github.com/ghostty-org/ghostty/actions/runs/32861518453), [5](https://github.com/ghostty-org/ghostty/actions/runs/32852280188), [6](https://github.com/ghostty-org/ghostty/actions/runs/32811372816)  
Summary: 6 runs • 25 commits • 5 authors

### Changes

- [`c4e1697`](https://github.com/ghostty-org/ghostty/commit/c4e16970a803b170e352432424f44192cb59f3ac) renderer: release GPU resources for hidden surfaces (macOS) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ref #12034
  
  This commit releases many GPU resources when a surface becomes invisible and
  rebuilds it on the next draw. I don't say "all" because there are still
  some things we can improve on (Kitty images).
  
  We previously held onto all GPU resources for the lifetime of the surface
  regardless of its visibility state. This is 3x (for triple-buffering):
  screen render targets, uniform/cell/custom shader buffers, font textures,
  and more.
  
  Measured on macOS (Metal):
  
  | Measurement (1 visible + 20 hidden tabs)    | Before    | After   |
  |---------------------------------------------|-----------|---------|
  | Tracked GPU allocations (steady state)      | 384.6 MiB | 18.3 MiB |
  | `MTLDevice.currentAllocatedSize`            | 393.3 MiB | 19.7 MiB |
  | `footprint` IOSurface (dirty)               | 309 MB    | 15 MB   |
  | Swap chain rebuild on unhide (42 switches)  | n/a       | avg 0.43 ms, max 0.55 ms |
  
  As you can see, importantly, swap chain rebuild is fast: 0.43ms average.
  That means that the rebuild is imperceptible and happens well within
  a frame draw time.
  
  This is macOS only, but most of the work was in the generic renderer.
  GTK only needs to call `releaseGpuResources` when it becomes invisible
  to get the same benefits. I didn't have my VM handy to test this yet so
  I didn't include it.
  ```
- [`683d8db`](https://github.com/ghostty-org/ghostty/commit/683d8db643b95cf229bfb5fe9fab9ae677920343) renderer: release GPU resources for hidden surfaces (macOS) ([#14017](https://github.com/ghostty-org/ghostty/issues/14017)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ref #12034
  
  This commit releases many GPU resources when a surface becomes invisible
  and rebuilds it on the next draw. I don't say "all" because there are
  still some things we can improve on (Kitty images).
  
  We previously held onto all GPU resources for the lifetime of the
  surface regardless of its visibility state. This is 3x (for
  triple-buffering): screen render targets, uniform/cell/custom shader
  buffers, font textures, and more.
  
  Measured on macOS (Metal):
  
  | Measurement (1 visible + 20 hidden tabs)    | Before    | After   |
  |---------------------------------------------|-----------|---------|
  | Tracked GPU allocations (steady state)      | 384.6 MiB | 18.3 MiB |
  | `MTLDevice.currentAllocatedSize`            | 393.3 MiB | 19.7 MiB |
  | `footprint` IOSurface (dirty)               | 309 MB    | 15 MB   |
  | Swap chain rebuild on unhide (42 tab switches) | n/a | avg 0.43 ms,
  max 0.55 ms |
  
  As you can see, importantly, swap chain rebuild is fast: 0.43ms average.
  That means that the rebuild is imperceptible and happens well within a
  frame draw time.
  
  This is macOS only, but most of the work was in the generic renderer.
  GTK only needs to call `releaseGpuResources` when it becomes invisible
  to get the same benefits. I didn't have my VM handy to test this yet so
  I didn't include it.
  ```
- [`48a9e29`](https://github.com/ghostty-org/ghostty/commit/48a9e29f79e918d4f73a13c1ce27646d029811e4) nix: update nixpkgs-unstable ([@jcollie](https://github.com/jcollie))
  ```text
  Update nixpkgs-unstable to pick up fontconfig 2.18. Currently we are linking against 2.17 and you get errors
  like this on standard error when using config files meant for fontconfig 2.18:
  
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 20: invalid constant used :
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 23: invalid constant used : monospace
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 42: invalid attribute 'xsi:nil'
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 43: invalid constant used :
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 46: invalid constant used : sans-serif
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 68: invalid attribute 'xsi:nil'
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 69: invalid constant used :
  
  This also removes an override for libfyaml on Darwin that was merged upstream into nixpkgs.
  ```
- [`d9857ea`](https://github.com/ghostty-org/ghostty/commit/d9857eabae06baebc9685121bfe78c49090643af) cli: update list-themes preview sample to valid Zig 0.16 syntax ([@tacheraSasi](https://github.com/tacheraSasi))
- [`bc2f7d7`](https://github.com/ghostty-org/ghostty/commit/bc2f7d7d2fa589a3abf9e4f6696e0a7f7c204e4f) terminal: update Kitty clipboard base64 handling to spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty clipboard protocol now specifies base64 handling:
  All OSC 5522 payloads and the base64 metadata values (mime, name, pw)
  use strict RFC 4648 with the standard alphabet. Characters outside
  the alphabet (including whitespace) and incorrect padding must be
  rejected, never silently skipped.
  
  For wdata payloads for one MIME type, the base64 stream can be split
  at arbitrary packet boundaries and only the concatenation must be
  correctly padded.
  
  Simdutf has a strict mode for base64 so we got this for free.
  Benchmarks to be safe:
  
  | Decoder                       | Time  | Throughput |
  |-------------------------------|-------|------------|
  | permissive (previous)         | 99ms  | 10.8 GB/s  |
  | strict                        | 97ms  | 11.1 GB/s  |
  | strict, streaming 4KiB chunks | 102ms | 10.5 GB/s  |
  | strict w/ separate scan pass  | 143ms | 7.5 GB/s   |
  | std.base64 scalar             | 234ms | 4.6 GB/s   |
  
  Spec changes upstream:
  https://github.com/kovidgoyal/kitty/commit/479872838f7536ab87b8133471eb49d06804951b
  https://sw.kovidgoyal.net/kitty/clipboard/#encoding-of-payloads
  ```
- [`82ccf12`](https://github.com/ghostty-org/ghostty/commit/82ccf12ca22131d2c845387806b6a924f86abe5f) nix: update nixpkgs-unstable ([#13678](https://github.com/ghostty-org/ghostty/issues/13678)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update nixpkgs-unstable to pick up fontconfig 2.18. Currently we are
  linking against 2.17 and you get errors like this on standard error when
  using config files meant for fontconfig 2.18:
  
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 20:
  invalid constant used :
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 23:
  invalid constant used : monospace
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 42:
  invalid attribute 'xsi:nil'
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 43:
  invalid constant used :
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 46:
  invalid constant used : sans-serif
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 68:
  invalid attribute 'xsi:nil'
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 69:
  invalid constant used :
  ```
- [`557253d`](https://github.com/ghostty-org/ghostty/commit/557253d8f64f8b08da33f5a7f3cb33a75960b09d) terminal: update Kitty clipboard base64 handling to spec ([#14015](https://github.com/ghostty-org/ghostty/issues/14015)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty clipboard protocol now specifies base64 handling: All OSC 5522
  payloads and the base64 metadata values (mime, name, pw) use strict RFC
  4648 with the standard alphabet. Characters outside the alphabet
  (including whitespace) and incorrect padding must be rejected, never
  silently skipped.
  
  For wdata payloads for one MIME type, the base64 stream can be split at
  arbitrary packet boundaries and only the concatenation must be correctly
  padded.
  
  Simdutf has a strict mode for base64 so we got this for free. Benchmarks
  to be safe:
  
  | Decoder                       | Time  | Throughput |
  |-------------------------------|-------|------------|
  | permissive (previous)         | 99ms  | 10.8 GB/s  |
  | strict                        | 97ms  | 11.1 GB/s  |
  | strict, streaming 4KiB chunks | 102ms | 10.5 GB/s  |
  | strict w/ separate scan pass  | 143ms | 7.5 GB/s   |
  | std.base64 scalar             | 234ms | 4.6 GB/s   |
  
  Spec changes upstream:
  
  https://github.com/kovidgoyal/kitty/commit/479872838f7536ab87b8133471eb49d06804951b
  https://sw.kovidgoyal.net/kitty/clipboard/#encoding-of-payloads
  ```
- [`4e817e7`](https://github.com/ghostty-org/ghostty/commit/4e817e79a1d7e3fe7393297e3c8f1269abb6523a) terminal: treat high bytes in DCS strings as payload data ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #11216
  
  The dcs_passthrough state only forwarded bytes 0x00-0x7E to the DCS
  handler. Bytes 0x80-0x9F hit the "anywhere" C1 transitions and exited
  the string, while 0xA0-0xFF fell through to the default transition and
  were silently dropped. **This breaks any DCS payload carrying UTF-8. **
  
  A continuation byte in the C1 range terminates or corrupts the string:
  "Ü" is 0xC3 0x9C, so the 0xC3 is dropped and the 0x9C acts as 8-bit ST,
  ending the DCS mid-character.
  
  Also, a payload byte such as 0x9B (second byte of "Û") transitions to
  csi_entry, so the remainder of the payload executes as a live control sequence.
  This is a prerequisite for tmux control mode (#1935), whose %output
  notifications carry raw UTF-8 pane content.
  
  Fix this in the parse table only: override 0x80-0xFF in
  dcs_passthrough to put and in dcs_ignore to ignore, exactly how
  osc_string already claims 0x20-0xFF (including 0x9C) as data. This
  deviates from the vt100.net state machine
  (https://vt100.net/emu/dec_ansi_parser) deliberately and includes
  0x9C: a raw 0x9C is indistinguishable from a UTF-8 continuation byte,
  and we don't honor 8-bit C1 controls in the ground state either.
  ```
- [`b260da2`](https://github.com/ghostty-org/ghostty/commit/b260da24f8f10bebc92539eef640dbfd26c5a854) cli: update list-themes preview sample to valid Zig 0.16 syntax ([#14012](https://github.com/ghostty-org/ghostty/issues/14012)) ([@jcollie](https://github.com/jcollie))
  ````text
  The demo code shown in the `+list-themes` theme preview was stale from
  before the Zig 0.16 migration (context: #12228). It referenced
  `std.Io.getStdOut().writer()`, which never existed in any Zig release,
  and `pub fn main() !void`. This rewrites the rendered sample to valid
  Zig 0.16 idioms:
  
  ```zig
  const std = @import("std");
  
  pub fn main(init: std.process.Init) !void {
      var buf: [1024]u8 = undefined;
      var stdout = std.Io.File.stdout().writer(init.io, &buf);
      const w = &stdout.interface;
  
      var i: usize = 1;
      while (i <= 16) : (i += 1) {
          if (i % 15 == 0) {
              try w.writeAll("ZiggZagg\n");
          } else if (i % 3 == 0) {
              try w.writeAll("Zigg\n");
          } else if (i % 5 == 0) {
              try w.writeAll("Zagg\n");
          } else {
              try w.print("{d}\n", .{i});
          }
      }
      try w.flush();
  }
  ```
  
  The gutter line numbers, row offsets, and child window height were
  renumbered to match, and the zig version shown in the demo prompt line
  was updated from v0.13.0 to v0.16.0.
  ````
- [`9c3ec93`](https://github.com/ghostty-org/ghostty/commit/9c3ec931d64561a8407dde7ac984ce156ae91539) terminal: treat high bytes in DCS strings as payload data ([#14016](https://github.com/ghostty-org/ghostty/issues/14016)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #11216
  
  The dcs_passthrough state only forwarded bytes 0x00-0x7E to the DCS
  handler. Bytes 0x80-0x9F hit the "anywhere" C1 transitions and exited
  the string, while 0xA0-0xFF fell through to the default transition and
  were silently dropped. **This breaks any DCS payload carrying UTF-8. **
  
  A continuation byte in the C1 range terminates or corrupts the string:
  "Ü" is 0xC3 0x9C, so the 0xC3 is dropped and the 0x9C acts as 8-bit ST,
  ending the DCS mid-character.
  
  Also, a payload byte such as 0x9B (second byte of "Û") transitions to
  csi_entry, so the remainder of the payload executes as a live control
  sequence. This is a prerequisite for tmux control mode (#1935), whose
  %output notifications carry raw UTF-8 pane content.
  
  Fix this in the parse table only: override 0x80-0xFF in dcs_passthrough
  to put and in dcs_ignore to ignore, exactly how osc_string already
  claims 0x20-0xFF (including 0x9C) as data. This deviates from the
  vt100.net state machine
  (https://vt100.net/emu/dec_ansi_parser) deliberately and includes 0x9C:
  a raw 0x9C is indistinguishable from a UTF-8 continuation byte, and we
  don't honor 8-bit C1 controls in the ground state either.
  ```
- [`bb00a5c`](https://github.com/ghostty-org/ghostty/commit/bb00a5c988245a10f7d96dfdadcbfbd03f977dc4) Update VOUCHED list ([#14013](https://github.com/ghostty-org/ghostty/issues/14013)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14012#issuecomment-5412366760)
  from @jcollie.
  
  Vouch: @tacheraSasi
  ```
- [`8c5bc3d`](https://github.com/ghostty-org/ghostty/commit/8c5bc3d29f17ebc42b81d4b61ec1fe86886332d4) terminal: optimize OSC string reading with SIMD ([@mitchellh](https://github.com/mitchellh))
  ```text
  We now have large OSCs (e.g. Kitty clipboard protocol) on the order
  of megabytes. OSC was still byte-at-a-time. This adds a vector-optimized
  plus bulk storing path to OSC, similar to APC.
  
  Throughput measured with the terminal-stream benchmark:
  
  | Corpus                   | Before | After | Speedup |
  |--------------------------|--------|-------|---------|
  | OSC 52, 1MiB payloads    | 446ms  | 14ms  | 32x     |
  | OSC 5522, 1MiB payloads  | 446ms  | 15ms  | 30x     |
  | OSC 5522, 64KiB payloads | 448ms  | 14ms  | 32x     |
  | OSC 5522, 4KiB payloads  | 448ms  | 16ms  | 29x     |
  | Tiny titles (~24B each)  | 450ms  | 73ms  | 6.2x    |
  | Mixed OSCs (16MiB)       | 595ms  | 531ms | 1.13x   |
  
  Used Fable to help validate this with a barrage of differential tests.
  The actual implementation was AI-written but was guided to basically
  mimic the APC path and then I hand verified everything too.
  ```
- [`8144ef4`](https://github.com/ghostty-org/ghostty/commit/8144ef4e73e70a4e9942fceb319819005f07fd37) terminal: optimize OSC string reading with SIMD ([#14011](https://github.com/ghostty-org/ghostty/issues/14011)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We now have large OSCs (e.g. Kitty clipboard protocol) on the order of
  megabytes. OSC was still byte-at-a-time. This adds a vector-optimized
  plus bulk storing path to OSC, similar to APC.
  
  Throughput measured with the terminal-stream benchmark:
  
  | Corpus                   | Before | After | Speedup |
  |--------------------------|--------|-------|---------|
  | OSC 52, 1MiB payloads    | 446ms  | 14ms  | 32x     |
  | OSC 5522, 1MiB payloads  | 446ms  | 15ms  | 30x     |
  | OSC 5522, 64KiB payloads | 448ms  | 14ms  | 32x     |
  | OSC 5522, 4KiB payloads  | 448ms  | 16ms  | 29x     |
  | Tiny titles (~24B each)  | 450ms  | 73ms  | 6.2x    |
  | Mixed OSCs (16MiB)       | 595ms  | 531ms | 1.13x   |
  
  Used Fable to help validate this with a barrage of differential tests.
  The actual implementation was AI-written but was guided to basically
  mimic the APC path and then I hand verified everything too.
  ```
- [`a2212a5`](https://github.com/ghostty-org/ghostty/commit/a2212a5b1229d580ceb25d67cf3353b679eddf3b) macos: replace legacy aspectRatio with scaledToFit in clipboard preview ([@bo2themax](https://github.com/bo2themax))
- [`d7f5ba3`](https://github.com/ghostty-org/ghostty/commit/d7f5ba3b4f4745660dbb5ada6fde6f841aba07af) macOS: add test cases for ScriptKeyEventCommand ([@bo2themax](https://github.com/bo2themax))
- [`f1b9efe`](https://github.com/ghostty-org/ghostty/commit/f1b9efed802650ffaccc0b53da026314909bae53) macOS: update default behaviour of KeyboardLayout.character(for:modifiers:) ([@bo2themax](https://github.com/bo2themax))
- [`719def7`](https://github.com/ghostty-org/ghostty/commit/719def70f3df246695881f571f0edde28b95f0a3) macOS: update default behaviour of KeyboardLayout.character(for:modifiers:) ([#14009](https://github.com/ghostty-org/ghostty/issues/14009)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up for #13888, and prepare for #13205.
  
  The comments are copied from the history commit.
  
  ## AI Disclosure
  
  The tests are updated by Claude, I cherrypicked them.
  ```
- [`1c73935`](https://github.com/ghostty-org/ghostty/commit/1c739350c31a8340fdbf56cd7e703f860f69bed4) macOS: add test cases for ScriptKeyEventCommand ([#14008](https://github.com/ghostty-org/ghostty/issues/14008)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Partial changes for #13205, known issues are marked as warnings.
  
  ### AI Disclosure
  
  Claude generated these tests from linked pr, I cherrypicked and reviewed
  myself.
  ```
- [`6d2b436`](https://github.com/ghostty-org/ghostty/commit/6d2b43652950b417431145147dd445d32e04119c) macos: replace legacy aspectRatio with scaledToFit in clipboard preview ([#14006](https://github.com/ghostty-org/ghostty/issues/14006)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the swiftlint legacy_swiftui_aspect_ratio violation.
  
  ### AI Disclosure
  
  By Claude, but it's really simple.
  ```
- [`b31fbc8`](https://github.com/ghostty-org/ghostty/commit/b31fbc846474bf6082f1a3f13290e17f2d984a25) terminal: fully reset row metadata when recycling row storage ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13940
  
  Various operations like scroll, line insert, erase, etc. operations
  would clear cells but remain row metadata such as wrap flags and
  semantic prompt state.
  
  When we had fast paths in `grow` and other places like resize
  we would adopt that without knowing it because we didn't properly clear.
  
  Fix this by properly clearing row metadata too at the points where we
  erase a row that might be reused.
  
  Benchmarked with terminal-stream workloads for each affected path.
  The added cost is 2-4 instructions per recycled row next to the existing
  full-row cell clear. There was no measurable wall-clock change on any
  workload.
  
  AI helped run the benchmarks for me and analyze for missing places (it found
  some!) but otherwise this was hand-designed.
  ```
- [`046a45a`](https://github.com/ghostty-org/ghostty/commit/046a45a5fcacf427573b81de6e03de37fe01bb16) terminal: fully reset row metadata when recycling row storage ([#14010](https://github.com/ghostty-org/ghostty/issues/14010)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13940
  
  Various operations like scroll, line insert, erase, etc. operations
  would clear cells but remain row metadata such as wrap flags and
  semantic prompt state.
  
  When we had fast paths in `grow` and other places like resize we would
  adopt that without knowing it because we didn't properly clear.
  
  Fix this by properly clearing row metadata too at the points where we
  erase a row that might be reused.
  
  Benchmarked with terminal-stream workloads for each affected path. The
  added cost is 2-4 instructions per recycled row next to the existing
  full-row cell clear. There was no measurable wall-clock change on any
  workload.
  
  AI helped run the benchmarks for me and analyze for missing places (it
  found some!) but otherwise this was hand-designed.
  ```
- [`70f0065`](https://github.com/ghostty-org/ghostty/commit/70f0065759428c0594c7c5befcb20104ff7ab615) terminal: reject oversized Kitty clipboard writes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update OSC 5522 writes to reject every transaction that exceeds the
  configured decoded-data limit. The previous behavior truncated text
  while rejecting only non-text data.
  
  Programs now receive EFBIG as soon as a write crosses the limit. The
  clipboard remains untouched, and remaining write packets are ignored
  until a new transaction begins. Raise the default to the protocol
  minimum of 64 MiB.
  
  This applies the latest spec change:
  https://github.com/kovidgoyal/kitty/commit/32ea1041921607836e37815e0ab3692264a6cc81
  ```
- [`e8d8945`](https://github.com/ghostty-org/ghostty/commit/e8d8945b536189366e227b157aa0b8202b94890a) terminal: update Kitty clipboard text input validation to spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate decoded OSC 5522 metadata, read MIME lists, and alias
  lists as UTF-8. Treat an alias without a target MIME type as an
  invalid write packet.
  
  Malformed write packets now return EINVAL and terminate the in-flight
  transaction instead of leaving it active. Malformed reads are dropped
  without disturbing an active write.
  
  Latest changes upstream to spec:
  https://github.com/kovidgoyal/kitty/commit/458421af4656a8f90beca7d95e4c1ff7093cf269
  ```
- [`4888c0a`](https://github.com/ghostty-org/ghostty/commit/4888c0a02c2e36b5146900195e344a8ac307660f) terminal: reject oversized Kitty clipboard writes ([#14004](https://github.com/ghostty-org/ghostty/issues/14004)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update OSC 5522 writes to reject every transaction that exceeds the
  configured decoded-data limit. The previous behavior truncated text
  while rejecting only non-text data.
  
  Programs now receive EFBIG as soon as a write crosses the limit. The
  clipboard remains untouched, and remaining write packets are ignored
  until a new transaction begins. Raise the default to the protocol
  minimum of 64 MiB.
  
  This applies the latest spec change:
  
  https://github.com/kovidgoyal/kitty/commit/32ea1041921607836e37815e0ab3692264a6cc81
  ```
- [`8867c37`](https://github.com/ghostty-org/ghostty/commit/8867c37c55b578b9eb4cfaba41cb9023e557176d) terminal: update Kitty clipboard text input validation to spec ([#14005](https://github.com/ghostty-org/ghostty/issues/14005)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate decoded OSC 5522 metadata, read MIME lists, and alias lists as
  UTF-8. Treat an alias without a target MIME type as an invalid write
  packet.
  
  Malformed write packets now return EINVAL and terminate the in-flight
  transaction instead of leaving it active. Malformed reads are dropped
  without disturbing an active write.
  
  Latest changes upstream to spec:
  
  https://github.com/kovidgoyal/kitty/commit/458421af4656a8f90beca7d95e4c1ff7093cf269
  ```

