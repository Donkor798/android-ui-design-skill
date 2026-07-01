# android-ui-design-skill

Android casual game UI design system for Kotlin games. 22 complete visual design themes, each delivering color tokens, typography, shape system, elevation, background treatment, Material3 styles, and animation personality.

**Output**: A `design-spec_[theme].md` file — the design contract for the app team. No UI code generated.

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

## Output: Design Spec Markdown

Each theme request produces a `design-spec_[theme_name].md` with 9 chapters:

| Chapter | Content |
|---------|---------|
| 1. Color System | 30+ color tokens with exact HEX values |
| 2. Typography | Font family, scale, weight, letterSpacing, effects |
| 3. Title & Heading Consistency | Heading hierarchy, alignment, capitalization, truncation rules |
| 4. Icon System | Icon library, style, sizing, color mapping, touch targets |
| 5. Shape System | Corner radii per component, stroke rules |
| 6. Elevation & Shadow | Dark theme glow vs light theme shadow specs |
| 7. Background | Solid, gradient, texture descriptions |
| 8. Component Specs | Visual attributes for all Material3 components |
| 9. Animation Personality | Duration, interpolator, feedback patterns |

Plus: Spacing & Layout tokens, Global State specs (Loading/Empty/Error), Accessibility constraints.

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
python3 scripts/generate_theme.py --list-themes
python3 scripts/run_evals.py --validate
```

## Structure

```
android-ui-design-skill/
├── SKILL.md                      # 22 themes catalogue + 7-chapter design spec system
├── AGENTS.md
├── references/
│   ├── theme-full-specs.md       # All 22 themes: complete color values + design notes
│   ├── design-principles.md      # Material3 integration, dark/light rules
│   ├── animation-guide.md        # 7 animation personalities
│   ├── screen-layouts.md         # Page layout structure specs
│   └── xml-patterns.md           # Component spec reference (design constraint basis)
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
