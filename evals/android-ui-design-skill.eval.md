# android-ui-design-skill — Eval Spec

This eval spec defines the binary quality gates for the android-ui-design-skill.
Run with: `python3 scripts/run_evals.py`

```json
{
  "skill": "android-ui-design-skill",
  "run": "python3 scripts/run_pipeline.py --screen {input} --output {output}",
  "criteria": [
    {
      "id": "spec-md-exists",
      "type": "command",
      "text": "A design-spec_*.md file was generated",
      "cmd": "ls {output}/design-spec_*.md"
    },
    {
      "id": "spec-has-9-chapters",
      "type": "command",
      "text": "Design spec contains all 9 required chapter headings",
      "cmd": "grep -c '### 第 . 章' {output}/design-spec_*.md"
    },
    {
      "id": "spec-has-state-specs",
      "type": "command",
      "text": "Design spec includes Loading/Empty/Error state specifications",
      "cmd": "grep -qE '(加载态|空状态|错误态)' {output}/design-spec_*.md"
    },
    {
      "id": "spec-has-a11y",
      "type": "command",
      "text": "Design spec includes accessibility constraints",
      "cmd": "grep -q '无障碍约束' {output}/design-spec_*.md"
    },
    {
      "id": "spec-color-tokens",
      "type": "command",
      "text": "Design spec includes color token table with HEX values",
      "cmd": "grep -c '#[0-9A-Fa-f]\\{6\\}' {output}/design-spec_*.md | grep -q '[3-9][0-9]'"
    },
    {
      "id": "spec-no-xml-code",
      "type": "command",
      "text": "Design spec contains no XML code blocks (no <?xml or </resources>)",
      "cmd": "! grep -qE '<\\?xml|</resources>|ConstraintLayout|@\\+id/' {output}/design-spec_*.md"
    },
    {
      "id": "spec-no-kotlin-code",
      "type": "command",
      "text": "Design spec contains no Kotlin/Compose implementation code",
      "cmd": "! grep -qE '^fun |^class |^val |^object |@Composable|ViewBinding|setContentView' {output}/design-spec_*.md"
    },
    {
      "id": "spec-no-android-resource-files",
      "type": "command",
      "text": "Design spec does not embed colors/themes/dimens resource file shapes",
      "cmd": "! grep -qE '<color name=|<dimen name=|<style name=\"Theme\\.|colors_[a-z_]+\\.xml' {output}/design-spec_*.md"
    },
    {
      "id": "spec-has-button-states",
      "type": "command",
      "text": "Design spec includes button state specs (enabled/pressed/disabled/loading)",
      "cmd": "grep -qE '(Pressed|Disabled|Loading)' {output}/design-spec_*.md"
    },
    {
      "id": "spec-typography-table",
      "type": "llm-judge",
      "text": "Design spec chapter 2 includes font family, scale levels, weight and letterSpacing specs"
    },
    {
      "id": "spec-heading-hierarchy",
      "type": "llm-judge",
      "text": "Design spec chapter 3 includes heading hierarchy with alignment, capitalization, truncation rules, AND toolbar/top-bar constraints (variant A/B/C/D or equivalent height/title size/anti-pattern rules)"
    },
    {
      "id": "spec-toolbar-system",
      "type": "llm-judge",
      "text": "Design spec constrains custom title bars: 56dp height, ~20sp title, visual center, max 2 actions, background usually page background not heavy primary fill, no thick gradient bars"
    },
    {
      "id": "spec-button-height-56",
      "type": "command",
      "text": "Primary button height is specified as 56dp (not the 4dp progress-track typo)",
      "cmd": "grep -qE '56[[:space:]]*dp' {output}/design-spec_*.md && ! grep -qE '主按钮.*4dp|Primary.*height.*4dp|/ 4dp / 16dp' {output}/design-spec_*.md"
    },
    {
      "id": "spec-dialog-or-hud",
      "type": "llm-judge",
      "text": "Design spec includes dialog/result constraints (width/scrim/button order) and/or Game HUD rules (no full toolbar in-game, score/timer typography)"
    },
    {
      "id": "spec-color-quality-gates",
      "type": "llm-judge",
      "text": "Design spec chapter 1 mentions contrast or quality checks and soul-color roles (primary/score/highlight); glow token present or explicitly n/a for light themes"
    },
    {
      "id": "spec-icon-system",
      "type": "llm-judge",
      "text": "Design spec chapter 4 includes icon library, style, sizing table, and color mapping"
    },
    {
      "id": "spec-shape-table",
      "type": "llm-judge",
      "text": "Design spec chapter 5 includes corner radius per component"
    },
    {
      "id": "spec-identity-card",
      "type": "llm-judge",
      "text": "Design spec starts with a theme identity card: material one-liner, soul-color roles (primary/score/highlight), toolbar accent, animation personality, and one theme-specific forbid"
    },
    {
      "id": "spec-background-layers",
      "type": "llm-judge",
      "text": "Design spec chapter 7 specifies backgrounds by page role (home / shell / in-game / dialog scrim) with limits so in-game background does not compete with board/question"
    },
    {
      "id": "spec-animation-table",
      "type": "llm-judge",
      "text": "Design spec chapter 9 includes duration, interpolator, and feedback pattern descriptions"
    }
  ],
  "golden": [
    {
      "id": "quiz-neon-dark",
      "input": "inputs/quiz_neon_dark.txt",
      "expected": null,
      "expected_status": "pending-first-green"
    },
    {
      "id": "main-menu-candy-pop",
      "input": "inputs/main_menu_candy_pop.txt",
      "expected": null,
      "expected_status": "pending-first-green"
    },
    {
      "id": "game-over-ocean-breeze",
      "input": "inputs/game_over_ocean_breeze.txt",
      "expected": null,
      "expected_status": "pending-first-green"
    }
  ]
}
```
