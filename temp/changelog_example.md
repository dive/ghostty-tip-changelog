> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> Entries are grouped by UTC day and combine commits across all successful runs for each day.

## February 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22219871214), [2](https://github.com/ghostty-org/ghostty/actions/runs/22211628446), [3](https://github.com/ghostty-org/ghostty/actions/runs/22210903027), [4](https://github.com/ghostty-org/ghostty/actions/runs/22206371589)

### Changes

- [`585bf3f`](https://github.com/ghostty-org/ghostty/commit/585bf3fcd25be3d1d70383a0f1b55e0f6744d639) Update es_AR translations with additional strings for 1.3 ([#10861](https://github.com/ghostty-org/ghostty/issues/10861)) ([@alanmoyano](https://github.com/alanmoyano))
  <details>
  <summary>Details</summary>
  
  - Adds the three new string
  - Changes one string for better wording
  
  </details>
- [`c4c87f8`](https://github.com/ghostty-org/ghostty/commit/c4c87f8c85fb7339c093538196847fc3d0eed3c8) make palette inversion opt-in ([@jake-stewart](https://github.com/jake-stewart))
- [`f66a84b`](https://github.com/ghostty-org/ghostty/commit/f66a84b18a44838831af5819cdad1ba85d9592e4) improve light theme detection ([@jake-stewart](https://github.com/jake-stewart))
- [`acf8cc7`](https://github.com/ghostty-org/ghostty/commit/acf8cc74195f8f778e933a3e8c218891d79a36e4) i18n: Update and slightly clean up Russian translation ([#10633](https://github.com/ghostty-org/ghostty/issues/10633)) ([@TicClick](https://github.com/TicClick))
  <details>
  <summary>Details</summary>
  
  as per [#10632](https://github.com/ghostty-org/ghostty/issues/10632)
  
  </details>
- [`0eaf77d`](https://github.com/ghostty-org/ghostty/commit/0eaf77da5fe0cbfe24ac5e0585a04d80d51fb952) WIP: Make palette inversion opt-in ([#10877](https://github.com/ghostty-org/ghostty/issues/10877)) ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  From [#10554](https://github.com/ghostty-org/ghostty/issues/10554)
  
  > I can see there being space for some kind of new sequence that tells
  the terminal that "hey, I want a semantic palette" or something, that is
  better adjusted to themes automatically. But, I don't think we should
  this by default.
  
  > So my concrete proposal is to eliminate the inversion and bg => fg
  ramp and do a more typical dark => light ramp (still taking into account
  bg/fg, but keeping 16 black and 231 white). I think this is the only way
  we can really make this a default on feature. I think this would address
  all the negative reactions we've gotten to it.
  
  This adds a new `palette-harmonious`, disabled by default, which allows
  generated light themes to be inverted.
  
  </details>
- [`2863849`](https://github.com/ghostty-org/ghostty/commit/2863849fcae7ef46342e14af30fc3d850cd2109a) ci: milestone workflow should use our vouch app token ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  This increases our rate limits and the vouch app already has the
  permissions required for the milestone workflow.
  
  </details>
- [`c316472`](https://github.com/ghostty-org/ghostty/commit/c316472362dc9d6ced051b2d07c4ea5ee542822e) ci: milestone workflow should use our vouch app token ([#10879](https://github.com/ghostty-org/ghostty/issues/10879)) ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  This increases our rate limits and the vouch app already has the
  permissions required for the milestone workflow.
  
  cc @trag1c
  
  </details>
- [`df47dc1`](https://github.com/ghostty-org/ghostty/commit/df47dc1a98b9df29152ee1b24daea5f50883c99a) ci: milestone workflow should use our vouch app token ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  This increases our rate limits and the vouch app already has the
  permissions required for the milestone workflow.
  
  </details>
- [`a6b6033`](https://github.com/ghostty-org/ghostty/commit/a6b603385236bad5a592eb078d3e72a39c8215c1) ci: pass milestone token via github-token parameter ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  If I am reading the upstream action right, even if you set GITHUB_TOKEN
  env var its defaulting to `github.token`, so we need to specify as a
  param.
  
  </details>
- [`1fa4e78`](https://github.com/ghostty-org/ghostty/commit/1fa4e787eb1f50729153d09b7f455ebb9fc4ccc9) ci: pass milestone token via github-token parameter ([#10881](https://github.com/ghostty-org/ghostty/issues/10881)) ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  If I am reading the upstream action right, even if you set GITHUB_TOKEN
  env var its defaulting to `github.token`, so we need to specify as a
  param.
  
  </details>
- [`786bad9`](https://github.com/ghostty-org/ghostty/commit/786bad9774cfa4753a11f8bb46b47aedc974bf3e) macos: swiftlint 'colon' rule ([@jparise](https://github.com/jparise))
- [`6ade5df`](https://github.com/ghostty-org/ghostty/commit/6ade5df7990d8f2fbd7dce5c05f43ba43bd510e5) macos: swiftlint 'comma' rule ([@jparise](https://github.com/jparise))
- [`a8903c1`](https://github.com/ghostty-org/ghostty/commit/a8903c1bb199aa52b63d20593361672f27a4d4ba) macos: swiftlint 'comment_spacing' rule ([@jparise](https://github.com/jparise))
- [`56d67ce`](https://github.com/ghostty-org/ghostty/commit/56d67ce88f05f9cf499ae483f34212722475ebf4) macos: swiftlint 'control_statement' rule ([@jparise](https://github.com/jparise))
- [`1b827e3`](https://github.com/ghostty-org/ghostty/commit/1b827e3e45f93b30767bfc4aa5e2131594dc60d0) macos: swiftlint 'empty_enum_arguments' rule ([@jparise](https://github.com/jparise))
- [`a83c8f8`](https://github.com/ghostty-org/ghostty/commit/a83c8f8a9d2b82956a02c24f82f5ab0ddaf9998c) macos: swiftlint 'empty_parentheses_with_trailing_closure' rule ([@jparise](https://github.com/jparise))
- [`9287a61`](https://github.com/ghostty-org/ghostty/commit/9287a61920da4262cd6c544dbd51c3e918d50174) macos: swiftlint 'implicit_optional_initialization' rule ([@jparise](https://github.com/jparise))
- [`32e540c`](https://github.com/ghostty-org/ghostty/commit/32e540c248815bed6a09bcf76ea1df536e25bf4f) macos: swiftlint 'legacy_constant' rule ([@jparise](https://github.com/jparise))
- [`b10dcc9`](https://github.com/ghostty-org/ghostty/commit/b10dcc96299aea9e4c276896a7331a3a2ded837f) macos: swiftlint 'legacy_constructor' rule ([@jparise](https://github.com/jparise))
- [`6052f66`](https://github.com/ghostty-org/ghostty/commit/6052f664cf83921114d05c6db19bb3ff1fb23063) macos: swiftlint 'opening_brace' rule ([@jparise](https://github.com/jparise))
- [`25b38b2`](https://github.com/ghostty-org/ghostty/commit/25b38b291e8128df96258b342fff914f71f80cac) macos: swiftlint 'private_over_fileprivate' rule ([@jparise](https://github.com/jparise))
- [`6af9599`](https://github.com/ghostty-org/ghostty/commit/6af959920e9815750998ea8e3dcb11a1264fee86) macos: swiftlint 'syntactic_sugar' rule ([@jparise](https://github.com/jparise))
- [`33dce85`](https://github.com/ghostty-org/ghostty/commit/33dce8511efa5432059e7593e20f0c53d7da080d) macos: swiftlint 'trailing_semicolon' rule ([@jparise](https://github.com/jparise))
- [`b532cd5`](https://github.com/ghostty-org/ghostty/commit/b532cd55d626fd1e472c288ce42151f8e6945634) macos: swiftlint 'trailing_whitespace' rule ([@jparise](https://github.com/jparise))
- [`540adb0`](https://github.com/ghostty-org/ghostty/commit/540adb0da3494cfdae9264782e9e38281ca0997f) macos: swiftlint 'unneeded_synthesized_initializer' rule ([@jparise](https://github.com/jparise))
- [`a36d2f5`](https://github.com/ghostty-org/ghostty/commit/a36d2f5420dee5b0ac1d0c55e83e1ea6dea3b879) macos: swiftlint 'unused_closure_parameter' rule ([@jparise](https://github.com/jparise))
- [`629a656`](https://github.com/ghostty-org/ghostty/commit/629a656e5329b35c970fdba3ee10fc5b366d2ba0) macos: swiftlint 'vertical_whitespace' rule ([@jparise](https://github.com/jparise))
- [`f4d70df`](https://github.com/ghostty-org/ghostty/commit/f4d70df34c8d564a7824144433d9bf30dfcef3e0) macos: swiftlint 'implicit_getter' rule ([@jparise](https://github.com/jparise))
- [`9bae26a`](https://github.com/ghostty-org/ghostty/commit/9bae26ab455110a7b28872c65dc82efb9d352027) macos: swiftlint 'orphaned_doc_comment' rule ([@jparise](https://github.com/jparise))
- [`a7719a8`](https://github.com/ghostty-org/ghostty/commit/a7719a8db6bae10c57bad6a73b94def4826fff5b) macos: swiftlint 'shorthand_operator' rule ([@jparise](https://github.com/jparise))
- [`c418e4b`](https://github.com/ghostty-org/ghostty/commit/c418e4b581d61969d3f02c2adae4e2e862f07b58) macos: swiftlint 'unused_optional_binding' rule ([@jparise](https://github.com/jparise))
- [`dbf2e0e`](https://github.com/ghostty-org/ghostty/commit/dbf2e0e087ced90a8f844fc028d73d9b2e40e668) macos: swiftlint 'vertical_parameter_alignment' rule ([@jparise](https://github.com/jparise))
- [`a6fcb46`](https://github.com/ghostty-org/ghostty/commit/a6fcb46e18b14a9199446dd0f053ebe08ef33bc9) macos: autofixable swiftlint rules ([#10878](https://github.com/ghostty-org/ghostty/issues/10878)) ([@mitchellh](https://github.com/mitchellh))
  <details>
  <summary>Details</summary>
  
  Apply fixes for all of the SwiftLint rules that can be automatically
  fixed (`--fix`) or addressed via some minor reformatting.
  
  Each rule is in its own commit for easier review.
  
  </details>
- [`ca700b2`](https://github.com/ghostty-org/ghostty/commit/ca700b2d7b8d9e9e9ed46df2e1bb49a13b2fe606) additional strings for 3.0 ([@phush0](https://github.com/phush0))
- [`d1cb225`](https://github.com/ghostty-org/ghostty/commit/d1cb225895f6f3b195a5477d41d89b69216d5fc6) Fix translation for 'Open in Ghostty' ([@phush0](https://github.com/phush0))
- [`42c81db`](https://github.com/ghostty-org/ghostty/commit/42c81dbccc7c62ccc1eaef7fd724af9e308814ef) bg_BG additional strings for 1.3 ([#10836](https://github.com/ghostty-org/ghostty/issues/10836)) ([@trag1c](https://github.com/trag1c))

