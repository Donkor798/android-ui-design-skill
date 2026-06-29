# android-ui-design-skill — Eval Spec

This eval spec defines the binary quality gates for the android-ui-design-skill.
Run with: `python3 scripts/run_evals.py`

```json
{
  "skill": "android-ui-design-skill",
  "run": "python3 scripts/run_pipeline.py --screen {input} --output {output}",
  "criteria": [
    {
      "id": "xml-valid",
      "type": "command",
      "text": "Generated layout XML starts with <?xml and contains ConstraintLayout",
      "cmd": "grep -l 'ConstraintLayout' {output}/res/layout/*.xml"
    },
    {
      "id": "colors-file-exists",
      "type": "command",
      "text": "A colors_*.xml file was generated in res/values/",
      "cmd": "ls {output}/res/values/colors_*.xml"
    },
    {
      "id": "no-hardcoded-hex",
      "type": "command",
      "text": "No hardcoded hex colors in layout XML (all use @color/ references)",
      "cmd": "! grep -rE 'android:background=\"#|android:textColor=\"#' {output}/res/layout/"
    },
    {
      "id": "button-drawable-exists",
      "type": "command",
      "text": "A bg_button_*.xml drawable was generated",
      "cmd": "ls {output}/res/drawable/bg_button_*.xml"
    },
    {
      "id": "content-descriptions",
      "type": "llm-judge",
      "text": "Interactive views (ImageButton, buttons with icons) include android:contentDescription"
    },
    {
      "id": "constraint-chains-closed",
      "type": "llm-judge",
      "text": "All ConstraintLayout views have complete constraint attributes (no missing constraint warnings)"
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
