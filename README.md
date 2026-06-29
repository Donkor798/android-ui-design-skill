# android-ui-design-skill

Android casual game UI design system for Kotlin games. 22 complete visual design themes, each delivering color tokens, typography, shape system, elevation, background treatment, Material3 styles, and animation personality.

## Installation

```bash
# Claude Code
cp -R ./android-ui-design-skill ~/.claude/skills/android-ui-design-skill

# Auto-detect platform
./install.sh
```

## Usage

Start a new session and type:

```
/android-ui-design-skill neon dark theme
/android-ui-design-skill 所有主题列表
/android-ui-design-skill space galaxy theme
/android-ui-design-skill compare candy pop vs sakura spring
/android-ui-design-skill 新主题：海盗风格
/android-ui-design-skill 推荐适合 quiz 游戏的主题
```

## 22 Themes

| Category | Themes |
|----------|--------|
| Dark (9) | Neon Dark · Space Galaxy · Lava Fire · Midnight Luxury · Deep Sea · Aurora Night · Halloween · Steampunk · Graffiti Street |
| Light (8) | Ocean Breeze · Forest Zen · Candy Pop · Sakura Spring · Desert Gold · Ice Crystal · Pastel Dream · Christmas |
| Special (5) | Pixel Classic · Cartoon Fun · Minimalist White · Paper Craft · Neon Synthwave |

## Scripts

```bash
python3 scripts/generate_layout.py --list-screens
python3 scripts/generate_layout.py --list-themes
python3 scripts/generate_layout.py --screen quiz --theme neon_dark --output ./output/
python3 scripts/run_pipeline.py --screen game_2048 --theme candy_pop
python3 scripts/run_evals.py --validate
```

## Structure

```
android-ui-design-skill/
├── SKILL.md                      # 22 themes catalogue + 7-layer design system
├── AGENTS.md
├── references/
│   ├── theme-full-specs.md       # All 22 themes: complete color XML + design notes
│   ├── design-principles.md      # Material3 integration, dark/light rules, theme switching
│   ├── animation-guide.md        # 7 animation personalities, full Kotlin code
│   ├── screen-layouts.md         # All page layout specs (home/game/history/stats/settings/HTP)
│   └── xml-patterns.md           # Reusable XML component snippets
├── scripts/
│   ├── generate_layout.py        # Generate XML layout for any screen + theme
│   ├── generate_theme.py         # List / reference theme metadata
│   ├── run_pipeline.py           # Orchestrator
│   └── run_evals.py              # Regression test runner
├── evals/
│   └── android-ui-design-skill.eval.md
├── install.sh
└── README.md
```
