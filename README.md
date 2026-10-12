> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 12, 2026 at 14:13 UTC.

## October 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38210273538), [2](https://github.com/ghostty-org/ghostty/actions/runs/38206984263), [3](https://github.com/ghostty-org/ghostty/actions/runs/38203368652), [4](https://github.com/ghostty-org/ghostty/actions/runs/38195601411)  
Summary: 4 runs • 16 commits • 6 authors

### Changes

- [`78a89ce`](https://github.com/ghostty-org/ghostty/commit/78a89cebec38846f83c9723aa53b88d011a76afc) gtk: connect tab split tree signals to the window the tab is in ([@thomasfedb](https://github.com/thomasfedb))
- [`1e9e14a`](https://github.com/ghostty-org/ghostty/commit/1e9e14af5df14211892f5fc15fd21a49c7d94868) gtk: connect tab split tree signals to the window the tab is in ([#14474](https://github.com/ghostty-org/ghostty/issues/14474)) ([@jcollie](https://github.com/jcollie))
  ```text
  **Issue**
  A tab's split tree "changed" handler was connected to the window that
  created the tab, and never moved when the tab was dragged out or moved
  with move_tab_to_new_window. Splits created in a moved tab were wired to
  the old window, so toggle_fullscreen from them fullscreened the old
  window.
  
  To reproduce: open a second tab, run move_tab_to_new_window, create a
  split in the moved tab, then run toggle_fullscreen from that split.
  
  **Fix**
  The handler is now connected when a tab is attached to a window and
  disconnected when it's detached.
  
  First pass written with Claude Code (Claude Opus 5.5), reviewed and
  reprompted by me. Tested on Fedora 44.
  ```
- [`edfd83a`](https://github.com/ghostty-org/ghostty/commit/edfd83ad0b19cadb019c3f16be707a931c36f0d8) gtk: fix mouse cursor shape when selecting text ([@dkinzler](https://github.com/dkinzler))
  ```text
  Fixes #14380
  
  Set the mouse cursor shape on the `RenderSurface` widget instead of on
  `Surface`. To find the cursor shape to show, GTK starts at the widget
  under the mouse and walks up the tree to find an ancestor that has a
  cursor shape set. But when pointer grab is active, GTK will stop looking
  at the widget the grab started at. When selecting text, the widget under
  the mouse is `RenderSurface` and pointer grab is active so that lookup
  stops there and the shape set on `Surface` is ignored.
  ```
- [`7685d36`](https://github.com/ghostty-org/ghostty/commit/7685d36c04c36d7cb8a02703b0f04ff1795d74e7) gtk: fix mouse cursor shape when selecting text ([#14558](https://github.com/ghostty-org/ghostty/issues/14558)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14380 where the mouse cursor shape reverts to the default when
  selecting text.
  
  Set the mouse cursor shape on the `RenderSurface` widget instead of on
  `Surface`. To find the cursor shape to show, GTK starts at the widget
  under the mouse and walks up the tree to find an ancestor that has a
  cursor shape set. But when pointer grab is active, GTK will stop looking
  at the widget the grab started at. When selecting text, the widget under
  the mouse is `RenderSurface` and pointer grab is active so that lookup
  stops there and the shape set on `Surface` is ignored.
  
  Manually tested that everything cursor-related still works: hiding the
  cursor with the `mouse-hide-while-typing` option, setting mouse shape
  with OSC22 and other widgets like the search UI still set their own
  shape.
  
  AI Disclosure: Changes and PR written by myself, used AI in researching
  GTK's mouse cursor logic.
  ```
- [`0df8c48`](https://github.com/ghostty-org/ghostty/commit/0df8c48688a15670d76578a068d178ac76eafbdf) terminal: DECSTR turns off ISO character protection ([@jcollie](https://github.com/jcollie))
  ```text
  The screen remembers which protection mode (DEC or ISO) was used most
  recently, because ISO protection (SPA/EPA) makes ED, EL and ECH skip
  protected cells while DEC protection (DECSCA) doesn't. DECSTR cleared the
  cursor's protected attribute but left that mode alone, so after a soft
  reset an ED 2 still left ISO-protected characters on the screen.
  
  xterm resets the protection mode on DECSTR, so do the same. This fixes
  esctest's ED_0, which failed after ECH_respectsISOProtection because
  the protected character survived esctest's reset between tests.
  
  In xterm (patch 412), SPA sets the mode to ISO_PROTECT:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L5367-L5372
  
  DECSTR calls VTReset with full=False, which calls ReallyReset:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L6154-L6156
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14566-L14568
  
  and ReallyReset sets it back to OFF_PROTECT for both RIS and DECSTR,
  before the part that only RIS does:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14428-L14432
  ```
- [`d0c0d40`](https://github.com/ghostty-org/ghostty/commit/d0c0d4008b0beb4a16dba902c59e36e8ebdad5de) terminal: TBC with no parameter clears the tab stop at the cursor ([@jcollie](https://github.com/jcollie))
  ```text
  The parameter of TBC (CSI Ps g) defaults to 0, which clears the tab stop
  at the cursor, but a bare CSI g has no parameters at all, and the stream
  logged it as an invalid tab clear command and dropped it. Treat it as 0.
  
  This fixes esctest's TBC_Default.
  
  In xterm (patch 412), a missing or zero parameter clears the tab stop
  at the cursor:
  
    https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L4301-L4308
  ```
- [`4af7e19`](https://github.com/ghostty-org/ghostty/commit/4af7e19c716535075b0c27647d665007e61931d4) terminal: match wide char selection rendering to copying ([@fornwall](https://github.com/fornwall))
  ```text
  Fix two cases where a wide char was not rendered as selected when it
  should (that is, it was included when copying):
  
  1. Selecting leftward onto the spacer tail of a wide char.
  2. Selecting rightward onto the spacer head of a wrapped wide char.
  ```
- [`42a6564`](https://github.com/ghostty-org/ghostty/commit/42a65647b0ea99a2fa6cd787f89bfa62e42b44c5) terminal: clear pending wrap when printing with DECAWM off ([@fornwall](https://github.com/fornwall))
  ```text
  Make printing with DECAWM disabled clear the pending wrap flag,
  avoiding an unexpected wrap after DECAWM is re-enabled.
  ```
- [`d3d4c15`](https://github.com/ghostty-org/ghostty/commit/d3d4c15d6aaedf13ca2c1b395744635cc01b424c) terminal: match wide char selection rendering to copying ([#14651](https://github.com/ghostty-org/ghostty/issues/14651)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix two cases where a wide char was not rendered as selected when it
  should (that is, it was included when copying):
  
  1. Selecting leftward onto the spacer tail of a wide char.
  2. Selecting rightward onto the spacer head of a wrapped wide char.
  
  Before:
  <img width="532" height="108" alt="before"
  src="https://github.com/user-attachments/assets/a2287a87-d2a0-4f5c-af96-2691688478f2"
  />
  
  After:
  <img width="532" height="108" alt="after"
  src="https://github.com/user-attachments/assets/4d065ba8-659c-4c4e-bbe8-2a4016882b2b"
  />
  
  AI disclosure: Created using opus 5.5 through claude code. Reviewed,
  modified and tested by me.
  ```
- [`698f8f4`](https://github.com/ghostty-org/ghostty/commit/698f8f4edb6eabb8a5d0d07892aff6fab52000a0) terminal: clear pending wrap when printing with DECAWM off ([#14652](https://github.com/ghostty-org/ghostty/issues/14652)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Make printing with [DECAWM](https://vt100.net/docs/vt510-rm/DECAWM.html)
  disabled clear the pending wrap flag, avoiding an unexpected wrap after
  `DECAWM` is re-enabled.
  
  Test case:
  
  ```sh
  #!/bin/sh
  printf '\033[2J\033[H\033[?7l'     # Clear screen and disable DECAWM
  printf "%$(tput cols)s" | tr ' ' a # Fill row with 'a', setting pending wrap
  printf '\033[Z'                    # Cursor Backward Tabulation (CBT)
  printf 'X\033[?7hY\n'              # Print 'X', enable DECAWM, print 'Y'
  ```
  
  - Before: `Y` appears at the start of the second row.
  - After: `Y` appears immediately after `X` on the first row.
  - Matches the three terminal emulators I tested with: xterm, kitty and
  mac terminal.
  
  AI disclosure: Initially created using opus 5.5 through claude code.
  Iterated on, reviewed and tested by me.
  ````
- [`3434608`](https://github.com/ghostty-org/ghostty/commit/34346087b28c28f2edd3bafd7935f50c4ded8483) terminal: TBC with no parameter clears the tab stop at the cursor ([#14644](https://github.com/ghostty-org/ghostty/issues/14644)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The parameter of TBC (CSI Ps g) defaults to 0, which clears the tab stop
  at the cursor, but a bare CSI g has no parameters at all, and the stream
  logged it as an invalid tab clear command and dropped it. Treat it as 0.
  
  This fixes esctest's TBC_Default.
  
  In xterm (patch 412), a missing or zero parameter clears the tab stop at
  the cursor:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L4301-L4308
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`aeda37b`](https://github.com/ghostty-org/ghostty/commit/aeda37b305ee3d897ff1bfeddfe39d7fa9366a74) terminal: DECSTR turns off ISO character protection ([#14643](https://github.com/ghostty-org/ghostty/issues/14643)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The screen remembers which protection mode (DEC or ISO) was used most
  recently, because ISO protection (SPA/EPA) makes ED, EL and ECH skip
  protected cells while DEC protection (DECSCA) doesn't. DECSTR cleared
  the cursor's protected attribute but left that mode alone, so after a
  soft reset an ED 2 still left ISO-protected characters on the screen.
  
  xterm resets the protection mode on DECSTR, so do the same. This fixes
  esctest's ED_0, which failed after ECH_respectsISOProtection because the
  protected character survived esctest's reset between tests.
  
  In xterm (patch 412), SPA sets the mode to ISO_PROTECT:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L5367-L5372
  
  DECSTR calls VTReset with full=False, which calls ReallyReset:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L6154-L6156
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14566-L14568
  
  and ReallyReset sets it back to OFF_PROTECT for both RIS and DECSTR,
  before the part that only RIS does:
  
  
  https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/charproc.c#L14428-L14432
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`e602944`](https://github.com/ghostty-org/ghostty/commit/e60294498eaa9ad54be67e2509301d75fd326e50) build(deps): bump actions/download-artifact from 8.0.1 to 8.0.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 8.0.1 to 8.0.2.
  - [Release notes](https://github.com/actions/download-artifact/releases)
  - [Commits](https://github.com/actions/download-artifact/compare/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c...9000827ccba6bdab643e8b6fd33ac0654aef8333)
  
  ---
  updated-dependencies:
  - dependency-name: actions/download-artifact
    dependency-version: 8.0.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`fb24459`](https://github.com/ghostty-org/ghostty/commit/fb24459b1698e92c8ace31e4dd9ff30d0cb3cf0a) build(deps): bump actions/upload-artifact from 7.0.1 to 7.0.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 7.0.1 to 7.0.2.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a...cf430e030ddbb5b0abf93d22962f4752f3646cd9)
  
  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-version: 7.0.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`27e1ad9`](https://github.com/ghostty-org/ghostty/commit/27e1ad9436f35121298f5684f198532b6f4035c9) build(deps): bump actions/upload-artifact from 7.0.1 to 7.0.2 ([#14655](https://github.com/ghostty-org/ghostty/issues/14655)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/upload-artifact](https://github.com/actions/upload-artifact)
  from 7.0.1 to 7.0.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/upload-artifact/releases">actions/upload-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Improves artifact download retries when the service returns HTTP 429
  (rate limiting), including honoring valid Retry-After headers.</li>
  <li>Updates <code>@​actions/artifact</code> to v6.3.1.</li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/tunc-d"><code>@​tunc-d</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/821">actions/upload-artifact#821</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/upload-artifact/compare/v7.0.1...v7.0.2">https://github.com/actions/upload-artifact/compare/v7.0.1...v7.0.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/cf430e030ddbb5b0abf93d22962f4752f3646cd9"><code>cf430e0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/822">#822</a>
  from actions/tunc-d-prepare-upload-v7-0-2</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/c2acdedd35a8824a1552c7137f8c18288c3ea469"><code>c2acded</code></a>
  chore: prepare v7.0.2 release</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/4687c1bbaa0a58abb517d90b4bbade6754c80c1a"><code>4687c1b</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/821">#821</a>
  from actions/tunc-d-upload-artifact-package-bump</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/8cbe1bebdb858105d8fdd88f81404d4de4595719"><code>8cbe1be</code></a>
  Bump <code>@​actions/artifact</code> to 6.3.1</li>
  <li>See full diff in <a
  href="https://github.com/actions/upload-artifact/compare/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a...cf430e030ddbb5b0abf93d22962f4752f3646cd9">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/upload-artifact&package-manager=github_actions&previous-version=7.0.1&new-version=7.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`6d53baf`](https://github.com/ghostty-org/ghostty/commit/6d53bafb1739dce288c653743cceedc54bcadedc) build(deps): bump actions/download-artifact from 8.0.1 to 8.0.2 ([#14654](https://github.com/ghostty-org/ghostty/issues/14654)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/download-artifact](https://github.com/actions/download-artifact)
  from 8.0.1 to 8.0.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/download-artifact/releases">actions/download-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v8.0.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update the readme by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/473">actions/download-artifact#473</a></li>
  <li>Improves artifact download retries when the service returns HTTP 429
  (rate limiting), including honoring valid Retry-After headers.</li>
  <li>Update <code>@​actions/artifact</code> to 6.3.1 by <a
  href="https://github.com/tunc-d"><code>@​tunc-d</code></a> in <a
  href="https://redirect.github.com/actions/download-artifact/pull/492">actions/download-artifact#492</a></li>
  <li>Prepare download-artifact v8.0.2 by <a
  href="https://github.com/tunc-d"><code>@​tunc-d</code></a> in <a
  href="https://redirect.github.com/actions/download-artifact/pull/493">actions/download-artifact#493</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/tunc-d"><code>@​tunc-d</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/actions/download-artifact/pull/492">actions/download-artifact#492</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/download-artifact/compare/v8.0.1...v8.0.2">https://github.com/actions/download-artifact/compare/v8.0.1...v8.0.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/download-artifact/commit/9000827ccba6bdab643e8b6fd33ac0654aef8333"><code>9000827</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/493">#493</a>
  from actions/tunc-d-prepare-download-v8-0-2</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/e455989ae00f5bdd4054f05d3e972c6bf8a62dc5"><code>e455989</code></a>
  Prepare download-artifact v8.0.2</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/a00b90c4a2f01d73a8c89552caabca6ea3b43137"><code>a00b90c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/492">#492</a>
  from actions/tunc-d-download-artifact-package-bump</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/29bb7ce6af5345aeab5bb4774ce7249ee3ccc27f"><code>29bb7ce</code></a>
  Update <code>@​actions/artifact</code> to 6.3.1</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/484a0b528fb4d7bd804637ccb632e47a0e638317"><code>484a0b5</code></a>
  Update the readme (<a
  href="https://redirect.github.com/actions/download-artifact/issues/473">#473</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/download-artifact/compare/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c...9000827ccba6bdab643e8b6fd33ac0654aef8333">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/download-artifact&package-manager=github_actions&previous-version=8.0.1&new-version=8.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## October 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38175388089), [2](https://github.com/ghostty-org/ghostty/actions/runs/38165255491), [3](https://github.com/ghostty-org/ghostty/actions/runs/38145817228), [4](https://github.com/ghostty-org/ghostty/actions/runs/38145546635), [5](https://github.com/ghostty-org/ghostty/actions/runs/38104361585)  
Summary: 5 runs • 13 commits • 5 authors

### Changes

- [`1d8215c`](https://github.com/ghostty-org/ghostty/commit/1d8215c95057bade2c77ae4e0b1c22442d5a15cb) Update VOUCHED list ([#14650](https://github.com/ghostty-org/ghostty/issues/14650)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14649#discussioncomment-18869510)
  from @jcollie.
  
  Vouch: @ollieatkinson
  ```
- [`1e5cdb8`](https://github.com/ghostty-org/ghostty/commit/1e5cdb865807abc990181efb8ebfa9122955cce2) Update VOUCHED list ([#14647](https://github.com/ghostty-org/ghostty/issues/14647)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14640#discussioncomment-18868231)
  from @jcollie.
  
  Vouch: @gaborbernat
  ```
- [`8d8b1ce`](https://github.com/ghostty-org/ghostty/commit/8d8b1ce00c5f1a29d5989a2b0b89b6b88f3b8781) terminal: include wide char wrapped onto next page when copying selection ([@fornwall](https://github.com/fornwall))
  ```text
  Copying a selection whose end lands on the spacer head before a wrapped
  wide character (for example an emoji at the right edge) dropped that
  character when the wrapped row started a new page.
  
  PageFormatter only handled the move onto the next row within a page and
  left a TODO for the cross-page case. Move the handling into
  PageListFormatter, which can advance the end pin across pages, and drop
  the in-page code: search, the only other PageFormatter user, always
  formats whole pages, so nothing relied on it.
  ```
- [`b1d9492`](https://github.com/ghostty-org/ghostty/commit/b1d9492cfa5d0d22c534a00e81bea623957113e7) terminal: include wide char wrapped onto next page when copying selection ([#14632](https://github.com/ghostty-org/ghostty/issues/14632)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Copying a selection whose end lands on the spacer head before a wrapped
  wide character (for example an emoji at the right edge) dropped that
  character when the wrapped row started a new page.
  
  `PageFormatter` only handled the move onto the next row within a page
  and left a TODO for the cross-page case. Move the handling into
  `PageListFormatter`, which can advance the end pin across pages, and
  drop the in-page code: search, the only other `PageFormatter` user,
  always formats whole pages, so nothing relied on it.
  
  Testing note (this confused me): The shell line editor (at least for
  zsh) can interfere with creating a spacer head before a wrapped wide
  character, so best to output wide characters directly to the terminal
  outside of the shell line editor.
  
  AI disclosure: Created with gpt-6 astra using codex. Reviewed and
  modified by me.
  ```
- [`2485de9`](https://github.com/ghostty-org/ghostty/commit/2485de98f194200506ff1cd374a9aed652fcccc9) termio: nushell integration documentation clarification ([@paaloeye](https://github.com/paaloeye))
  ```text
  - explicit acknowledgement of the parse-time constant requirement for `source` command in Nushell
  - split from: https://github.com/ghostty-org/ghostty/pull/14616
  ```
- [`3175f67`](https://github.com/ghostty-org/ghostty/commit/3175f67336e5fcd5e20c2a70a1645ec6c6019d27) libghostty-vt: report CSI 8 t window resize requests ([@jcollie](https://github.com/jcollie))
  ```text
  libghostty-vt parsed resize requests and then dropped them, so embedders
  had no way to honor them the way the app now can.
  ```
- [`211149d`](https://github.com/ghostty-org/ghostty/commit/211149dbc05767c4644d6c2591c21b8759c52839) test/esctest: honor resize requests ([@jcollie](https://github.com/jcollie))
  ```text
  Tests that resize the terminal, such as DECCOLM, failed because the
  runner's terminal ignored them.
  ```
- [`6104c78`](https://github.com/ghostty-org/ghostty/commit/6104c78f1a122d769e5dc92b6029197c9f612f40) terminal: support CSI 19 t (report screen size in characters) ([@jcollie](https://github.com/jcollie))
  ```text
  Respond to XTWINOPS CSI 19 t with CSI 9 ; rows ; cols t. Ghostty has no
  knowledge of the physical screen size, so, like VTE, report the size of
  the text area in characters (the same values as CSI 18 t).
  
  This is wired through both the libghostty-vt stream terminal and the
  termio stream handler, and exposed in the C API as
  GHOSTTY_SIZE_REPORT_CSI_19_T.
  ```
- [`226d719`](https://github.com/ghostty-org/ghostty/commit/226d7191f4a58c78bc18948c5b08a273081e09ee) termio: nushell integration documentation clarification ([#14624](https://github.com/ghostty-org/ghostty/issues/14624)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - explicit acknowledgement of the parse-time constant requirement for
  `source` command in Nushell
  - split from: https://github.com/ghostty-org/ghostty/pull/14616
  ```
- [`6408960`](https://github.com/ghostty-org/ghostty/commit/6408960527c0cde4ca47d1af588e172d46356bb6) terminal: support CSI 19 t (report screen size in characters) ([#14633](https://github.com/ghostty-org/ghostty/issues/14633)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Respond to XTWINOPS CSI 19 t with CSI 9 ; rows ; cols t. Ghostty has no
  knowledge of the physical screen size, so, like VTE, report the size of
  the text area in characters (the same values as CSI 18 t).
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`d66a353`](https://github.com/ghostty-org/ghostty/commit/d66a353aa4cd7266d150586dd555c35ecdb06810) libghostty-vt: report CSI 8 t window resize requests ([#14610](https://github.com/ghostty-org/ghostty/issues/14610)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt parsed resize requests and then dropped them, so embedders
  had no way to honor them the way the app now can.
  
  AI disclosure: Claude Code assisted in the implementation of this PR.
  ```
- [`6603157`](https://github.com/ghostty-org/ghostty/commit/66031576b7a8dcafa6d695c0bf23f15ae81aaf26) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`24da727`](https://github.com/ghostty-org/ghostty/commit/24da727f6857b5350b4a502bdcb30ab942b36e81) Update iTerm2 colorschemes ([#14634](https://github.com/ghostty-org/ghostty/issues/14634)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261005-151109-31756e7
  ```

## October 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38089240001), [2](https://github.com/ghostty-org/ghostty/actions/runs/38083192720), [3](https://github.com/ghostty-org/ghostty/actions/runs/38081318922), [4](https://github.com/ghostty-org/ghostty/actions/runs/38080640871), [5](https://github.com/ghostty-org/ghostty/actions/runs/38050071133)  
Summary: 5 runs • 16 commits • 8 authors

### Changes

- [`9fa2e3a`](https://github.com/ghostty-org/ghostty/commit/9fa2e3aaffdc7ae30f7cc417d1ce706957ae58a0) libghostty-vt: add prompt-based viewport scrolling ([@elias8](https://github.com/elias8))
- [`e3ac620`](https://github.com/ghostty-org/ghostty/commit/e3ac62001ef2a6c9c4b4bb4231535c1c3c3e4ae3) feat(lib-vt): expose prompt navigation through the C API ([#14618](https://github.com/ghostty-org/ghostty/issues/14618)) ([@trag1c](https://github.com/trag1c))
  ```text
  Adds `GHOSTTY_SCROLL_VIEWPORT_DELTA_PROMPT` to the existing
  `ghostty_terminal_scroll_viewport` API. This allows libghostty consumers
  to navigate between shell prompts using the same native implementation
  as Ghostty's `jump_to_prompt` action.
  
  The signed `delta_prompt` count moves backward or forward from the
  viewport top, treating multiline prompt continuations as one group. This
  also fixes two boundary cases in the shared traversal: navigating
  backward through a trimmed prompt and navigating forward when the
  current prompt continues to the last retained row.
  
  AI disclosure: I used Codex to assist with the implementation.
  ```
- [`4144f6d`](https://github.com/ghostty-org/ghostty/commit/4144f6dea4dbf9586c797e535a04f1cfd381d8a7) core: demote 'adjusting page capacity' log message to debug ([@jcollie](https://github.com/jcollie))
- [`6161591`](https://github.com/ghostty-org/ghostty/commit/61615915c8f423b1497ac2a1ae68885cad353892) core: demote 'adjusting page capacity' log message to debug ([#14631](https://github.com/ghostty-org/ghostty/issues/14631)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This can really spam the logs, and isn't really useful outside of a
  developer context anyway.
  ```
- [`b10ba7e`](https://github.com/ghostty-org/ghostty/commit/b10ba7ea26502f8e637e5f698d8d001a6256d9c4) terminal: preserve grapheme data when widening wraps ([@fornwall](https://github.com/fornwall))
  ```text
  With grapheme clustering (mode 2027) enabled, a cluster can widen
  after it has been printed. Codepoints that join a cluster without
  changing its width, such as a zero-width joiner, are stored on the
  cluster's single narrow cell. A later joining codepoint can then make
  the cluster two columns wide (for example a heart, a zero-width joiner,
  then thumbs up).
  
  When that happens in the last column and auto-wrap is enabled, the
  cluster wraps to the next line and its stored codepoints have to move
  with it. Copy them before wrapping instead of looking them up on the
  row above afterwards. That row isn't the original one when the wrap
  scrolls a single-row screen or a margin region, or doesn't scroll at
  all below the scroll region. So the codepoints were dropped, taken
  from an unrelated cell, or the lookup panicked.
  ```
- [`6dae79d`](https://github.com/ghostty-org/ghostty/commit/6dae79db927110b29970a0fbe7979949c6a3ffd4) terminal: re-attach wrapped grapheme data in one allocation ([@fornwall](https://github.com/fornwall))
  ```text
  Re-attach the grapheme codepoints copied across a widening wrap with a
  single setGraphemes call instead of appending them one at a time.
  Appending probed the grapheme map and could reallocate the chunk once
  per codepoint, which cost about 10% on input where every wrap carries
  a maximal cluster.
  
  Screen.setGraphemes mirrors appendGrapheme: on a full grapheme map or
  allocator it grows the page's grapheme capacity, reloads the cell and
  retries. Add a test that wraps onto a compacted page with no grapheme
  capacity so that path is covered.
  ```
- [`b7207b2`](https://github.com/ghostty-org/ghostty/commit/b7207b2ef6aa3e05af992a6febb9ee83ad69bb8c) libghostty-vt: update program status protocol to revision 0.4 ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only change in behavior is the reply to the support query. It
  used to be a bare `?`. It now also lists the states and kinds the
  terminal accepts, computed at comptime.
  
  The rest is documentation to match revisions 0.3 and 0.4.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
    https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`9cd19b4`](https://github.com/ghostty-org/ghostty/commit/9cd19b40de63f5bd172d1fcf30b667c8186d8923) libghostty-vt: update program status protocol to revision 0.4 ([#14630](https://github.com/ghostty-org/ghostty/issues/14630)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only change in behavior is the reply to the support query. It used
  to be a bare `?`. It now also lists the states and kinds the terminal
  accepts, computed at comptime.
  
  The rest is documentation to match revisions 0.3 and 0.4.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
  https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`2551d93`](https://github.com/ghostty-org/ghostty/commit/2551d9323505043ee6f4fcd5fc6f116bbe06f1df) terminal: preserve grapheme data when widening wraps ([#14552](https://github.com/ghostty-org/ghostty/issues/14552)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With [grapheme
  clustering](https://mitchellh.com/writing/grapheme-clusters-in-terminals#grapheme-clustering-in-terminals)
  enabled, a cluster can widen after it has been printed. Codepoints that
  join a cluster without changing its width, such as a zero-width joiner,
  are stored on the cluster's single narrow cell. A later joining
  codepoint can then make the cluster two columns wide (for example a
  heart, a zero-width joiner, then thumbs up).
  
  When that happens in the last column and auto-wrap is enabled, the
  cluster wraps to the next line and its stored codepoints have to move
  with it. Copy them before wrapping instead of looking them up on the row
  above afterwards: that row isn't the original one when the wrap scrolls
  a single-row screen or a margin region, or doesn't scroll at all below
  the scroll region.
  
  To reproduce, open a window and run the below using a safe build:
  
  ```sh
  # \033[?2027h    Enable grapheme-cluster handling (mode 2027).
  # \033[2J        Clear the visible screen.
  # \033[1;2r      Set the scrolling region to rows 1–2 and home the cursor.
  # \033[999;999H  Move to the bottom-right corner (coordinates are clamped).
  # \u2764         Print a heart, initially one cell wide.
  # \u200d         Append a zero-width joiner to the heart.
  # \U0001f44d     Append thumbs up, widening the cluster and triggering wrapping.
  # \033[r         Restore full-screen scrolling and home the cursor.
  # \033[999;1H    Move to the first column of the bottom row (below grapheme).
  # \n             Print a newline.
  printf '\033[?2027h\033[2J\033[1;2r\033[999;999H\u2764\u200d\U0001f44d\033[r\033[999;1H\n'
  ```
  
  - Before: Panics in safe builds when the cluster widens at the
  bottom-right corner below a scroll region. In release builds it unwraps
  a missing grapheme lookup, which is undefined behavior (a ReleaseFast
  test run segfaults).
  - After: it wraps with its grapheme data intact.
  
  AI disclosure: Initially created with the help of gpt-6 astra in codex.
  Iterated on, reviewed and tested by me.
  ````
- [`b804cb8`](https://github.com/ghostty-org/ghostty/commit/b804cb8fd7f48f471b741ffeaac240b61a31d694) benchmark: measure the terminal formatter with every extra ([@robmorgan](https://github.com/robmorgan))
  ```text
  The formatter benchmark only measured ScreenFormatter with no extras,
  the path clipboard copy, write_screen_file and search use. The
  libghostty-vt C API formats a whole terminal with
  ghostty_formatter_terminal_new, a TerminalFormatter whose extras
  (palette, modes, scrolling region, tabstops, cursor, style and so on)
  describe the terminal's state as well as its contents, and nothing
  measured it.
  
  --formatter=terminal formats with a TerminalFormatter and every extra,
  for every mode and region. With --mode=roundtrip both formats use it,
  so the round trip checks that the output reconstructs that state too,
  not only the contents. The default, --formatter=screen, is unchanged.
  ```
- [`1de05f1`](https://github.com/ghostty-org/ghostty/commit/1de05f1a780b279dcbfc89d93b43b850bd50e517) core: use std.Io.Dir.max_path_bytes ([@paaloeye](https://github.com/paaloeye))
  ```text
  Replace all `std.fs.max_path_bytes` with `std.Io.Dir.max_path_bytes`.
  
  `std.fs.max_path_bytes` is deprected starting from 0.16.0.
  ```
- [`10f6eb4`](https://github.com/ghostty-org/ghostty/commit/10f6eb4603a3f154f8493593da5cfeb895680cbf) cli/list-themes: don't crash when no themes match the search ([@jcollie](https://github.com/jcollie))
  ```text
  With a search that matches nothing, the filtered list is empty, and
  three keys in normal mode assumed a selected theme existed:
  
  - Enter opened the save screen, which indexes the selected theme while
    drawing.
  - G and End set the selection to `len - 1`, which underflows.
  - c and C indexed the selected theme to copy its name or path.
  
  Enter now only opens the save screen when there is a theme to save,
  G and End saturate at zero, and c and C do nothing on an empty list.
  ```
- [`c986a09`](https://github.com/ghostty-org/ghostty/commit/c986a09dc4c04d641914995e4a8ee706d9ea4e4b) cli/list-themes: don't crash when no themes match the search ([#14612](https://github.com/ghostty-org/ghostty/issues/14612)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With a search that matches nothing, the filtered list is empty, and
  three keys in normal mode assumed a selected theme existed:
  
  - Enter opened the save screen, which indexes the selected theme while
  drawing.
  - G and End set the selection to `len - 1`, which underflows.
  - c and C indexed the selected theme to copy its name or path.
  
  Enter now only opens the save screen when there is a theme to save, G
  and End saturate at zero, and c and C do nothing on an empty list.
  
  AI disclosure: Claude Code assisted in the development of this PR.
  ```
- [`747dd53`](https://github.com/ghostty-org/ghostty/commit/747dd538d5a71bc84e980177db3b23c082ed5781) core: use std.Io.Dir.max_path_bytes ([#14611](https://github.com/ghostty-org/ghostty/issues/14611)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace all `std.fs.max_path_bytes` with `std.Io.Dir.max_path_bytes`.
  
  `std.fs.max_path_bytes` is deprected starting from 0.16.0.
  ```
- [`65f2b48`](https://github.com/ghostty-org/ghostty/commit/65f2b4838f1d5946aa19080bfb84732871c7b695) benchmark: measure the terminal formatter with every extra ([#14581](https://github.com/ghostty-org/ghostty/issues/14581)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The formatter benchmark only measures `ScreenFormatter` with no extras,
  the path clipboard copy, `write_screen_file` and search use. The
  libghostty-vt C API formats a whole terminal with
  `ghostty_formatter_terminal_new`, a lovely `TerminalFormatter` whose
  extras(palette, modes, scrolling region, cursor, etc.) describe the
  terminal's state as well as its contents. As far as I'm aware, nothing
  measured that path.
  
  This PR adds `--formatter=terminal` to the benchmarks, which formats
  with a `TerminalFormatter` and every extra. It works with every mode and
  region. With `--mode=roundtrip`, both formats use it, so the round trip
  also checks that the output reconstructs the terminal state, not just
  the contents. The default, `--formatter=screen`, is unchanged.
  
  ### Numbers
  
  Here is the `ghostty-bench +terminal-formatter`, ReleaseFast on my
  Macbook Pro M1 Max with a median of 60 hyperfine runs and the `noop`
  baseline subtracted:
  
  | Input | main `screen` | this PR `screen` | this PR `terminal` |
  | --- | --- | --- | --- |
  | `ghostty-gen +styled --seed=42`, 640 KB, 80×24 | 1,687 µs | 1,688 µs |
  1,718 µs |
  | Claude Code session, 120×40, alternate screen | 7.67 µs | 7.62 µs |
  16.27 µs |
  
  **Note:** The existing path is unchanged. The extras add a fixed ~8.6 µs
  per format, mostly the 256-entry palette and modes.
  
  AI disclosure: Written with help from Claude Code using Opus 5.5. I
  reviewed, tested and ran the benchmarks myself.
  ```
- [`1da3ac4`](https://github.com/ghostty-org/ghostty/commit/1da3ac43bef626ec1155c366c1960cb0f4f74d1f) Update VOUCHED list ([#14623](https://github.com/ghostty-org/ghostty/issues/14623)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14486#issuecomment-6097215618)
  from @trag1c.
  
  Denounce: @rebecca-bell-2001
  ```

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
Summary: 4 runs • 45 commits • 12 authors

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
- [`6fbb560`](https://github.com/ghostty-org/ghostty/commit/6fbb560cd3bff42fe06af60aef320526b62a8004) cli: include the port in the ssh-terminfo cache key ([@stepankandrushin](https://github.com/stepankandrushin))
  ```text
  The ssh-terminfo cache keyed destinations as user@hostname from `ssh -G`,
  ignoring the port. Two machines behind one address on different ports
  (e.g. user@host:2221 and user@host:2218) shared a key, so once the first
  was cached the terminfo install was skipped for the second, which still
  got TERM=xterm-ghostty without the terminfo installed.
  
  The key now carries the port when it isn't 22: user@host:port, or
  user@[addr]:port for IPv6. Port 22 keeps the old user@host form, so
  existing caches stay valid.
  
  `+ssh-cache` accepts the new form: a bare `host` query matches that host
  on every port, a bare `host:port` query that port for any user, and
  `user@host:port` one exact entry.
  
  AI disclosure: the cause was found and the patch written with Claude
  Code (Claude Opus 5.5). Reviewed and tested by me.
  ```
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
- [`1360297`](https://github.com/ghostty-org/ghostty/commit/136029788c13c8bff81506571ab0009dcc095da2) macos: honor window-save-state=never for restorable windows ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Normal terminal windows remain eligible for native AppKit restoration
  when window-save-state is never, allowing background window snapshots
  to contend with window updates.
  
  Apply the setting when creating a terminal window and assign its
  restoration class and identifier only when restoration is enabled.
  ```
- [`e55c687`](https://github.com/ghostty-org/ghostty/commit/e55c687a4bdf46a4a7a9f51f040798fc11e62154) input: encode ctrl+alt+shift+backspace in legacy mode ([@fornwall](https://github.com/fornwall))
  ```text
  The legacy backspace table, taken from foot's keymap.h, was missing
  foot's Shift+Alt+Ctrl row. The chord fell through to the unmodified
  entry and sent a bare DEL (BS under DECBKM), dropping both the Alt
  prefix and Ctrl. Send ESC BS like Alt+Ctrl and Shift+Alt+Ctrl+Super.
  ```
- [`83edd49`](https://github.com/ghostty-org/ghostty/commit/83edd491e3024ae5e50393d62877b8897da1cccd) Update VOUCHED list ([#14510](https://github.com/ghostty-org/ghostty/issues/14510)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14507#discussioncomment-18705479)
  from @jcollie.
  
  Vouch: @mlabbe
  ```
- [`934ef81`](https://github.com/ghostty-org/ghostty/commit/934ef81401f0c0d27740c44810eede26011a18da) macos: update window restoration on config reload ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Existing terminal windows retained their creation-time restoration
  policy after configuration changes.
  
  Refresh that policy on global config reload and share setup with window
  creation, preserving the custom-command exclusion.
  ```
- [`0e75d01`](https://github.com/ghostty-org/ghostty/commit/0e75d015fe085772b8ecffdba672b60c04af73fe) macos: simplify window restoration setup ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Let isRestorable control preservation while assigning the restoration
  class and identifier consistently for every terminal window.
  
  Remove the restoration test fixture that creates AppKit windows and
  broadcasts configuration changes through the shared test host.
  ```
- [`f523504`](https://github.com/ghostty-org/ghostty/commit/f523504ea5c9f41d150d1eb93cc7a748b90f9361) macos: honor window-save-state=never for restorable windows ([#14506](https://github.com/ghostty-org/ghostty/issues/14506)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  With `window-save-state = never`, normal terminal windows are still
  marked `isRestorable`. Ghostty disables saving through
  `NSQuitAlwaysKeepsWindows`, but AppKit continued taking persistent-UI
  window snapshots in my reproduction on macOS 27.2 (26B5091g).
  
  Make `TerminalController.windowDidLoad()` also honor `never` when
  setting `window.isRestorable`, and only assign the restoration class and
  identifier when that flag is enabled. This adds no work to move, resize,
  or rendering callbacks.
  
  For newly created windows, `default` and `always` retain the existing
  behavior, including the exclusion of windows launched with a custom
  command. The follow-up commit also covers windows that are already open:
  on config reload, each terminal window re-syncs its restoration state
  through the same path used at window creation. Windows started with a
  custom command stay excluded.
  
  ### Reproduction and measurements
  
  I reproduced intermittent roughly 500 ms stalls while repeatedly
  focusing left/right between several Ghostty windows and other
  applications in OmniWM's Niri layout. `window-save-state = never` was
  set before restarting Ghostty.
  
  The issue reproduced on 1.3.1 and an unmodified build of `76895d97b`. In
  the latter, paired process samples showed
  `NSPersistentUIWindowSnapshotter` waiting through
  `SLSConnectionSynchronizeSLSCATransaction`, alongside Ghostty's main
  thread waiting on the connection lock under
  `SLSConnectionSetLastSLSCATransaction`.
  
  Comparing unmodified and patched builds of the same commit over two
  approximately 20-second navigation captures:
  
  | Measurement | Unmodified | Patched |
  | --- | ---: | ---: |
  | Focus presses | 113 | 129 |
  | Successful Ghostty AX frame-write attempts | 2,155 | 2,995 |
  | Ghostty AX frame-write attempts around 500 ms | 5 | 0 |
  | Slowest Ghostty AX frame-write attempt | 539.8 ms | 22.5 ms |
  | Ghostty main-thread samples in the CA/SkyLight connection-lock wait |
  2,205 / 12,544 | 0 / 12,173 |
  
  The persistent-UI snapshot worker was absent from the patched sample,
  and navigation feels noticeably smoother. These are aggregate samples
  from one before/after pair with different input counts, not a controlled
  end-to-end latency benchmark. Both Ghostty builds used ReleaseLocal with
  the same ReleaseFast core, while OmniWM remained the same instrumented
  Debug process.
  
  ### Validation
  
  - `macos/build.nu --action test`: 275 passed, 1 skipped, 0 failed.
  - New `macos/Tests/Terminal/TerminalControllerRestorationTests.swift`:
  reload flips restoration on an open window between `never`, `default`
  and `always`; custom-command windows stay non-restorable across reloads;
  surface-level config changes leave it alone.
  - `macos/build.nu --configuration ReleaseLocal`: passed.
  - Strict SwiftLint on both changed files: passed.
  - Manual navigation reproduction with the patched build: noticeably
  smoother, with the results above.
  
  ### AI disclosure
  
  I used OpenAI Codex to assist with diagnosis, implement the two-line
  change, run verification, analyze the captures, and draft this
  description. I reproduced the issue and tested the patched app
  interactively.
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
- [`dfd7baf`](https://github.com/ghostty-org/ghostty/commit/dfd7bafcd3a0c34a0557f68c383bb56486a62eab) cli: address review feedback on the ssh-cache port ([@stepankandrushin](https://github.com/stepankandrushin))
  ```text
  - matchesQuery treats a missing port as port 22.
  - isValidPort uses std.ascii.isDigit and rejects leading zeros, so
    host:22 and host:022 can't become distinct keys.
  ```
- [`f5a7f70`](https://github.com/ghostty-org/ghostty/commit/f5a7f706f0ef8751b9f47397b1c12880572b2330) Update VOUCHED list ([#14520](https://github.com/ghostty-org/ghostty/issues/14520)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14517#discussioncomment-18722576)
  from @pluiedev.
  
  Denounce: @davidpmclaughlin
  ```
- [`822e842`](https://github.com/ghostty-org/ghostty/commit/822e84272f60e320526e6c2c223ccdf786d334c9) Update VOUCHED list ([#14522](https://github.com/ghostty-org/ghostty/issues/14522)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14066#discussioncomment-18724022)
  from @jcollie.
  
  Vouch: @moonward
  ```
- [`befcdfd`](https://github.com/ghostty-org/ghostty/commit/befcdfd2c3a1cb24d9ec886e93c95b2b5daa7028) cli: include the port in the ssh-terminfo cache key ([#14472](https://github.com/ghostty-org/ghostty/issues/14472)) ([@jparise](https://github.com/jparise))
  ```text
  The ssh-terminfo cache keyed destinations as user@hostname from `ssh
  -G`, ignoring the port. Two machines behind one address on different
  ports (e.g. user@host:2221 and user@host:2218) shared a key, so once the
  first was cached the terminfo install was skipped for the second, which
  still got TERM=xterm-ghostty without the terminfo installed.
  
  The key now carries the port when it isn't 22: user@host:port, or
  user@[addr]:port for IPv6. Port 22 keeps the old user@host form, so
  existing caches stay valid.
  
  `+ssh-cache` accepts the new form: a bare `host` query matches that host
  on every port, a bare `host:port` query that port for any user, and
  `user@host:port` one exact entry.
  
  AI disclosure: the cause was found and the patch written with Claude
  Code (Claude Opus 5.5). Reviewed and tested by me.
  
  Discussed in #14465.
  ```
- [`406f2e5`](https://github.com/ghostty-org/ghostty/commit/406f2e54401978ad0bbf312b465554465b901f4e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`f96c971`](https://github.com/ghostty-org/ghostty/commit/f96c9711b9f72ecf75e0fd50f3434529b4dea5b6) Update VOUCHED list ([#14528](https://github.com/ghostty-org/ghostty/issues/14528)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12713#discussioncomment-18737824)
  from @jcollie.
  
  Vouch: @maddythewisp
  ```
- [`e6db5b6`](https://github.com/ghostty-org/ghostty/commit/e6db5b633a9ae820fea1620af52dbf87cc7e430c) terminal: fix crash after shrinking columns splits a wide char ([@fornwall](https://github.com/fornwall))
  ```text
  Narrowing without reflow cleared only the cells past the new width, so a
  wide char whose spacer tail was cut kept its head in the new last column.
  Every operation pairing a head with the cell after it then reached past
  the row end: insertBlanks and eraseLine(.left) panic in Screen.clearCells,
  and rowWillBeShifted writes cells[cols].
  
  Clear the orphaned head along with the cut columns.
  ```
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
- [`157c44f`](https://github.com/ghostty-org/ghostty/commit/157c44f643c9209e31bb92f4c2c4bcec9c6d23d5) input: UTF-8 encode the button in 1005 mouse reports ([@fornwall](https://github.com/fornwall))
  ```text
  In UTF-8 mouse mode (DECSET 1005) the button value was written as a
  single raw byte. xterm encodes it as UTF-8 like the coordinates, so
  values from 128 (buttons 8 and 9) take two bytes. The raw byte made
  the report invalid UTF-8.
  ```
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
- [`35a81a9`](https://github.com/ghostty-org/ghostty/commit/35a81a980bb9fce09a1ea762a68b55f8eb3477ed) renderer: always release shaders  ([#14542](https://github.com/ghostty-org/ghostty/issues/14542)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  shaders are only fread by releaseGpuResources while the display is
  unrealized and only the gtk apprt unrealizes. The mac apprt never does
  automatically so each closed surface leaked its five render pipelines
  and shader library. Updated so threadExit now marks the display
  unrealized before releasing GPU resources.
  ```
- [`c3203ea`](https://github.com/ghostty-org/ghostty/commit/c3203ea4b169a18eb2ccfe92847e426d8afea858) Update VOUCHED list ([#14550](https://github.com/ghostty-org/ghostty/issues/14550)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14549#discussioncomment-18767762)
  from @jcollie.
  
  Vouch: @robmorgan
  ```

