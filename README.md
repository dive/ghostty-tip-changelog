> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 19, 2026 at 13:14 UTC.

## June 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27796816290)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`49a9181`](https://github.com/ghostty-org/ghostty/commit/49a9181560707936c587ae121656d2d762d27849) Update VOUCHED list ([#13043](https://github.com/ghostty-org/ghostty/issues/13043)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12645#discussioncomment-17343861)
  from @tristan957.
  
  Vouch: @qappell
  ```

## June 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27787814657)  
Summary: 1 runs • 8 commits • 3 authors

### Changes

- [`7595203`](https://github.com/ghostty-org/ghostty/commit/7595203bed4f7dde58951c91660f973e3a65a8a7) ci: skip tip release when nothing release-relevant changed since last tip ([@claude](https://github.com/claude))
- [`4a20972`](https://github.com/ghostty-org/ghostty/commit/4a20972fc5e07a136253e717898a949a475e0bc2) macOS: disable liquid class explictly ([@bo2themax](https://github.com/bo2themax))
- [`e2832ae`](https://github.com/ghostty-org/ghostty/commit/e2832ae1fe75b47199ee9be98ae9835ff0f6adfa) macOS: get latest TerminalEntity's kind, title & pwd ([@bo2themax](https://github.com/bo2themax))
  ```text
  This fixes these being wrong after creating a terminal window for the first time.
  ```
- [`1182a76`](https://github.com/ghostty-org/ghostty/commit/1182a76df6966a4b524fb44073acb3b4116548c5) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`b12be54`](https://github.com/ghostty-org/ghostty/commit/b12be54ac37a8f33e5a72fae0c27aabeeb179d6c) Update iTerm2 colorschemes ([#13010](https://github.com/ghostty-org/ghostty/issues/13010)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260608-160426-8c84dd1
  ```
- [`c04e2b6`](https://github.com/ghostty-org/ghostty/commit/c04e2b64d9ff78be14e2f14be250f622a16cd518) macOS: get latest TerminalEntity's kind, title, pwd and screenshot ([#13007](https://github.com/ghostty-org/ghostty/issues/13007)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes these being wrong after creating a terminal window for the
  first time.
  
  Found them when trying [App Intent
  Testing](https://developer.apple.com/documentation/AppIntentsTesting/testing-your-app-intents-code),
  and confirmed them with macOS 26 as well (which is expected)
  
  <img width="2560" height="546" alt="Xnip2026-06-13_20-48-50"
  src="https://github.com/user-attachments/assets/7b13217d-66f5-48e2-ad69-9a489c22ad82"
  />
  
  ## AI Disclosure
  
  Claude drafted the initial version, i manually refined and tested them
  myself.
  ```
- [`136ced5`](https://github.com/ghostty-org/ghostty/commit/136ced5d51cf6ae6b76d01ef2b42183168200693) macOS: disable liquid class explicitly for layers in icon ([#12999](https://github.com/ghostty-org/ghostty/issues/12999)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the tiny border in app icon on macOS 27. It seems like macOS 27
  will [enable liquid
  glass](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer/#Apply-Liquid-Glass-effects-to-groups-and-layers)
  for layers in icon that do not disable liquid glass explicitly.
  
  <img width="2662" height="1061" alt="Xnip2026-06-12_09-52-19"
  src="https://github.com/user-attachments/assets/a25f0157-64ef-46cd-8c27-f23eddd1df09"
  />
  
  > Left is Icon Composer 1.5 in Xcode 26, right is Icon Composer 2.0 in
  Xcode 27
  
  I know macOS 27 is still in beta, and default behaviors are very likely
  to change before public release. But I think this change is reasonable,
  and it's the original intention.
  
  Relates to #13001
  
  ---
  
  Before(Left) and After(Right)
  <table>
      <tr>
        <td><img width="522" height="294" alt="Xnip2026-06-12_09-36-37"
  
  src="https://github.com/user-attachments/assets/84682907-9ed7-4d93-9b18-2ffd3354e1ad"
  /></td>
        <td><img width="542" height="274" alt="Xnip2026-06-12_09-39-31"
  
  src="https://github.com/user-attachments/assets/5ae3af36-a081-4a8f-a204-10b48bc113ee"
  /></td>
      </tr>
      <tr>
        <td><img width="572" height="290" alt="Xnip2026-06-12_09-39-46"
  
  src="https://github.com/user-attachments/assets/a8622bf0-4973-403c-ac31-9fa087d7c012"
  /></td>
        <td><img width="516" height="284" alt="Xnip2026-06-12_09-40-05"
  
  src="https://github.com/user-attachments/assets/212ef852-54c2-47fe-9452-7214fbcb7511"
  /></td>
      </tr>
    </table>
  ```
- [`f9c52d0`](https://github.com/ghostty-org/ghostty/commit/f9c52d0cd9d0da0cd970a5863b94c655c285d83e) build: skip tip release when nothing release-relevant changed since last tip ([#12989](https://github.com/ghostty-org/ghostty/issues/12989)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  There's a [short
  discussion](https://discord.com/channels/1005603569187160125/1005603569711452192/1504521818495651910)
  about this in Discord, I don't any existing discussion or issues.
  
  ### AI Disclosure
  
  Claude implemented this, changes are looking good to me, but I could be
  wrong.
  ```

## June 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27707274148)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`adce7b9`](https://github.com/ghostty-org/ghostty/commit/adce7b900ab7d13defea487a0a963c7786f7750b) Update VOUCHED list ([#13036](https://github.com/ghostty-org/ghostty/issues/13036)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13028#discussioncomment-17341591)
  from @bo2themax.
  
  Vouch: @exlee
  ```

## June 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27648954469), [2](https://github.com/ghostty-org/ghostty/actions/runs/27619391100)  
Summary: 2 runs • 7 commits • 3 authors

### Changes

- [`e2689b0`](https://github.com/ghostty-org/ghostty/commit/e2689b0ebb8112f9794eb4f0170aa24564071487) Update VOUCHED list ([#13032](https://github.com/ghostty-org/ghostty/issues/13032)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13030#issuecomment-4723744256)
  from @jcollie.
  
  Vouch: @kostich
  ```
- [`e8e7fea`](https://github.com/ghostty-org/ghostty/commit/e8e7fea103ab8bff5384673a60e04b59939738dd) Update VOUCHED list ([#13033](https://github.com/ghostty-org/ghostty/issues/13033)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13031#discussioncomment-17329468)
  from @jcollie.
  
  Vouch: @kostich
  ```
- [`4668a37`](https://github.com/ghostty-org/ghostty/commit/4668a371c1b8e70dd70f3ea7b05995db56a0f341) overrode function syncAppearance in order to update the tab bar as well ([@sahilkmishra](https://github.com/sahilkmishra))
- [`749d454`](https://github.com/ghostty-org/ghostty/commit/749d45490a56b5719174b670cf02395bc2e46e7f) fix swiftlint ([@sahilkmishra](https://github.com/sahilkmishra))
- [`c3ceb55`](https://github.com/ghostty-org/ghostty/commit/c3ceb55f5faf5dfc227c572ffd1e8004a03485fb) added comment explaining fix ([@sahilkmishra](https://github.com/sahilkmishra))
- [`8e8a8dc`](https://github.com/ghostty-org/ghostty/commit/8e8a8dc113423be0d733fc0f7a0b07b403c1ee94) added async fix in order to resolve first second tab issue ([@sahilkmishra](https://github.com/sahilkmishra))
- [`124c9d5`](https://github.com/ghostty-org/ghostty/commit/124c9d57d004de14466ce3e86e08cc508027ca2c) macOS: overrode function syncAppearance in order to update the tab bar as well ([#13017](https://github.com/ghostty-org/ghostty/issues/13017)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  #12949
  I'm unsure about the performance implications of overriding
  syncAppearance as opposed to other methods(ie setupKVO or
  setupTabGroupObservation) but I found that this shows the tab group
  correctly.
  ```

## June 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27525292229)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`fdbf9ff`](https://github.com/ghostty-org/ghostty/commit/fdbf9ff3a31d7531b691cb49c98fc465a1a503a0) Update VOUCHED list ([#13023](https://github.com/ghostty-org/ghostty/issues/13023)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13017#issuecomment-4704742285)
  from @bo2themax.
  
  Vouch: @sahilkmishra
  ```

## June 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27510472710)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`699387c`](https://github.com/ghostty-org/ghostty/commit/699387c2c16dd5723e8825ad608538142b07b86b) Update VOUCHED list ([#13018](https://github.com/ghostty-org/ghostty/issues/13018)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13013#discussioncomment-17300150)
  from @jcollie.
  
  Vouch: @ajr-khll
  ```

