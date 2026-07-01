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
      "cmd": "! grep -q '<?xml\\|</resources>\\|ConstraintLayout' {output}/design-spec_*.md"
    },
    {
      "id": "spec-no-kotlin-code",
      "type": "command",
      "text": "Design spec contains no Kotlin code blocks (no fun / class / val patterns)",
      "cmd": "! grep -qE '^fun |^class |^val |^object ' {output}/design-spec_*.md"
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
      "text": "Design spec chapter 3 includes heading hierarchy with alignment, capitalization, and truncation rules"
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
      "id": "spec-animation-table",
      "type": "llm-judge",
      "text": "Design spec chapter 9 includes duration, interpolator, and feedback pattern descriptions"
    }
  ],
  "golden": [
    {
      "id": "neon-dark",
      "input": "inputs/neon_dark.txt",
      "expected": null,
      "expected_status": "pending-first-green"
    },
    {
      "id": "candy-pop",
      "input": "inputs/candy_pop.txt",
      "expected": null,
      "expected_status": "pending-first-green"
    },
    {
      "id": "ocean-breeze",
      "input": "inputs/ocean_breeze.txt",
      "expected": null,
      "expected_status": "pending-first-green"
    }
  ]
}
```
