> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 14, 2026 at 07:36 UTC.

## June 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27282569352)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`5659cef`](https://github.com/ghostty-org/ghostty/commit/5659cef41f4f2f7a478d0800a11836fa17e64d66) Update VOUCHED list ([#12978](https://github.com/ghostty-org/ghostty/issues/12978)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12977#discussioncomment-17251869)
  from @jcollie.
  
  Vouch: @jamesarch
  ```

## June 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27142450381), [2](https://github.com/ghostty-org/ghostty/actions/runs/27113839529)  
Summary: 2 runs • 7 commits • 4 authors

### Changes

- [`3263ce5`](https://github.com/ghostty-org/ghostty/commit/3263ce5122480fe4d59a1189f67a3aac65949aa1) terminal: support click_events=2 ([@alexbathome](https://github.com/alexbathome))
- [`97777cf`](https://github.com/ghostty-org/ghostty/commit/97777cf5a32fd8943ab5c15d6ccee709a15943b4) fix: fix tests, change enum fields to lowercase ([@alexbathome](https://github.com/alexbathome))
- [`3ba5e9c`](https://github.com/ghostty-org/ghostty/commit/3ba5e9c24390412fb1dbb08c51008f1efdcff97b) Update VOUCHED list ([#12958](https://github.com/ghostty-org/ghostty/issues/12958)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12954#discussioncomment-17215965)
  from @pluiedev.
  
  Vouch: @alexbathome
  ```
- [`fd882c6`](https://github.com/ghostty-org/ghostty/commit/fd882c67cc3d95e9cc7fd837f33fbd0ef64017c4) pr review: added saturated arithmetic ([@alexbathome](https://github.com/alexbathome))
- [`69095e2`](https://github.com/ghostty-org/ghostty/commit/69095e298ab88bb0eb5ba541f4c505f2c22d07f5) terminal: support click_events=2 ([#12953](https://github.com/ghostty-org/ghostty/issues/12953)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Context
  
  Implements the OSC 133 `click_events=2` such that click events on the
  terminal are sent to the shell where the y coordinate is sent relative
  to the prompt pin.
  
  See
  https://sw.kovidgoyal.net/kitty/shell-integration/#click_events=1|2:~:text=click%5Fevents,xterm
  further detailed explanation.
  
  This should close https://github.com/ghostty-org/ghostty/issues/10865
  
  ### Testing
  
  I did some basic manual testing here via the following:
  ```
  ghostty  main
  ❯ printf '\033]133;A;click_events=1\007' && cat
  ^[[<0;49;4M^[[<0;48;8M^[[<0;47;12M^C
  
  ghostty  main  5s
  ❯ printf '\033]133;A;click_events=2\007' && cat
  ^[[<0;50;1M^[[<0;49;4M^[[<0;48;9M^[[<0;48;14M^C
  ```
  
  #### Notes
  
  This is my first Ghostty PR. All code here is hand-rolled, AI was used
  to do "smart" code searches/point me in the right direction.
  
  I'm actively trying to learn Zig, Ghostty, and get more involved with
  the community here so I'm avoiding obtuse usage of AI where possible.
  
  Any feedback or tips are more than welcome! Thank you! :pray:
  ````
- [`002fd41`](https://github.com/ghostty-org/ghostty/commit/002fd41429036e973d7257174f40bc1e3106ceb7) lib-vt: add pwd_changed callback for OSC 7/9/1337 (Zongyuan Li)
  ```text
  Previously the libghostty-vt stream handler dropped .report_pwd as a
  no-op, so embedders never saw shell-reported cwd changes and the
  terminal's pwd field was never populated from escape sequences.
  
  Wire the action to setPwd and expose a pwd_changed callback analogous
  to title_changed via GHOSTTY_TERMINAL_OPT_PWD_CHANGED. The payload is
  passed through unparsed; embedders read it with ghostty_terminal_get
  and decode any URI scheme themselves.
  ```
- [`2ba5e6b`](https://github.com/ghostty-org/ghostty/commit/2ba5e6b92963c9c9470fb30338989bb38fa11857) lib-vt: add pwd_changed callback for OSC 7/9/1337 ([#12956](https://github.com/ghostty-org/ghostty/issues/12956)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously the libghostty-vt stream handler dropped .report_pwd as a
  no-op, so embedders never saw shell-reported cwd changes and the
  terminal's pwd field was never populated from escape sequences.
  
  Wire the action to setPwd and expose a pwd_changed callback analogous to
  title_changed via GHOSTTY_TERMINAL_OPT_PWD_CHANGED. The payload is
  passed through unparsed; embedders read it with ghostty_terminal_get and
  decode any URI scheme themselves.
  
  This is proposed in
  [discussion#12927](https://github.com/ghostty-org/ghostty/discussions/12927)
  ```

