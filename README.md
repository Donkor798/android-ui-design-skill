# android-ui-design-skill

Android casual game UI design system for Kotlin games. 30 complete visual design themes, each with color tokens, typography, shape system, elevation, background treatment, Material3 styles, and animation personality.

**Output**: A `design-spec_[theme].md` file — the design contract for the app team. No UI code generated.

**Selection rule**: if the user has not named a theme, recommend **exactly 3** options and wait for an explicit pick. Never default to Neon Dark.

## Installation

```bash
# Claude Code
cp -R ./android-ui-design-skill ~/.claude/skills/android-ui-design-skill

# Auto-detect platform
./install.sh
```

## Usage

```
/android-ui-design-skill neon dark theme
/android-ui-design-skill 所有主题列表
/android-ui-design-skill space galaxy theme
/android-ui-design-skill compare candy pop vs sakura spring
/android-ui-design-skill 新主题：海盗风格
/android-ui-design-skill 推荐适合 quiz 游戏的主题
/android-ui-design-skill 帮我做个 2048 主题
```

未点名主题时，skill 会给出 3 张推荐卡片并停下；用户回复序号或主题名后再写完整规范。

## Output: Design Spec Markdown

Each locked theme request produces a `design-spec_[theme_name].md` with 9 chapters:

| Chapter | Content |
|---------|---------|
| 1. Color System | 30+ color tokens with exact HEX values |
| 2. Typography | Font family, scale, weight, letterSpacing, effects |
| 3. Title & Heading Consistency | Heading hierarchy, alignment, capitalization, truncation |
| 4. Icon System | Icon library, style, sizing, color mapping, touch targets |
| 5. Shape System | Corner radii per component, stroke rules |
| 6. Elevation & Shadow | Dark glow vs light shadow specs |
| 7. Background | Solid, gradient, texture descriptions |
| 8. Component Specs | Visual attributes for Material3 components |
| 9. Animation Personality | Duration, interpolator, feedback patterns |

Plus: spacing tokens, Loading / Empty / Error states, accessibility constraints.

## 30 Themes

| Category | Themes |
|----------|--------|
| Dark (12) | Neon Dark · Space Galaxy · Lava Fire · Midnight Luxury · Deep Sea · Aurora Night · Halloween · Steampunk · Graffiti Street · Noir Cinema · Cyber Mint · Ember Coal |
| Light (12) | Ocean Breeze · Forest Zen · Candy Pop · Sakura Spring · Desert Gold · Ice Crystal · Pastel Dream · Christmas · Matcha Cafe · Coral Reef · Honey Amber · Sunset Plaza |
| Signature (6) | Pixel Classic · Cartoon Fun · Minimalist White · Paper Craft · Neon Synthwave · Arcade Cabinet |

## Scripts

```bash
python3 scripts/generate_layout.py --list-screens
python3 scripts/generate_layout.py --list-themes
python3 scripts/generate_theme.py --list
python3 scripts/run_evals.py --validate
```

## Structure

```
android-ui-design-skill/
├── SKILL.md                      # 30 themes + selection flow + 9-chapter design spec
├── AGENTS.md
├── references/
│   ├── theme-full-specs.md       # All 30 themes: color values + design notes
│   ├── design-principles.md      # Material3 integration, dark/light rules
│   ├── animation-guide.md        # Animation personalities
│   ├── screen-layouts.md         # Page layout structure specs
│   └── xml-patterns.md           # Component spec reference (constraint basis)
├── scripts/
│   ├── generate_layout.py
│   ├── generate_theme.py
│   ├── run_pipeline.py
│   └── run_evals.py
├── evals/
│   └── android-ui-design-skill.eval.md
├── install.sh
└── README.md
```
