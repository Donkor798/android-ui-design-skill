# android-ui-design-skill

Android casual game UI design system for Kotlin/Compose games. 50 complete visual design themes, each with color tokens, typography, shape system, elevation, background treatment, component specs, and animation personality.

**Output (only)**: A `design-spec_[theme].md` file — the design contract for the app team.  
**Not output**: layout XML, Kotlin/Compose UI, `colors.xml` / `themes.xml` / `dimens.xml`, or any drop-in app source.

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
规范是给实现同学用的契约；**实现源码请在工程会话中另写**，不要由本 skill 直接生成进 app。

## Output: Design Spec Markdown

Each locked theme request produces a `design-spec_[theme_name].md` with 9 chapters:

| Chapter | Content |
|---------|---------|
| 1. Color System | Tokens + glow + contrast quality gates; 2048 tiles on demand |
| 2. Typography | Scale, number/HUD type, caption length limits, effect scope |
| 3. Title & Toolbar | Hierarchy + Toolbar variants + Game HUD by genre + anti-patterns |
| 4. Icon System | Library, style, sizing, color mapping, touch targets |
| 5. Shape System | Corner radii per component, stroke rules |
| 6. Elevation & Shadow | Dark glow vs light shadow specs |
| 7. Background | Solid, gradient, texture descriptions |
| 8. Component Specs | Buttons 56dp, chips, list density, home hero, dialogs/results |
| 9. Animation Personality | Duration, interpolator, feedback priority |

Plus: spacing tokens, Loading / Empty / Error states, accessibility constraints, design-spec checklist.

## 50 Themes

| Category | Themes |
|----------|--------|
| Dark (19) | Neon Dark · Space Galaxy · Lava Fire · Midnight Luxury · Deep Sea · Aurora Night · Halloween · Steampunk · Graffiti Street · Noir Cinema · Cyber Mint · Ember Coal · Cyberpunk City · Pirate Cove · Royal Velvet · Industrial Steel · Night Market · Moonlit Garden · Jungle Adventure |
| Light (19) | Ocean Breeze · Forest Zen · Candy Pop · Sakura Spring · Desert Gold · Ice Crystal · Pastel Dream · Christmas · Matcha Cafe · Coral Reef · Honey Amber · Sunset Plaza · Tropical Fruit · Bubble Tea · Farm Cottage · Cloud Sky · Lavender Fields · Citrus Fresh · Snow Festival |
| Signature (12) | Pixel Classic · Cartoon Fun · Minimalist White · Paper Craft · Neon Synthwave · Arcade Cabinet · Crystal Gem · Clay Stopmotion · Board Game Table · Comic Halftone · Ink Wash · Retro Poster |

## Scripts (internal / design-spec helpers)

```bash
# Constraint summary text (not layout XML)
python3 scripts/generate_layout.py --list-screens
python3 scripts/generate_layout.py --list-themes
python3 scripts/generate_layout.py --screen game_quiz --theme neon_dark

# Color tokens as markdown tables (not colors.xml)
python3 scripts/generate_theme.py --list
python3 scripts/generate_theme.py --theme neon_dark --output ./output
python3 scripts/generate_theme.py --write-full-specs

python3 scripts/run_evals.py --validate
```

## Structure

```
android-ui-design-skill/
├── SKILL.md                      # 50 themes + selection + design-spec-only contract
├── AGENTS.md
├── examples/                     # design-spec skeleton + neon_dark gold sample
├── references/                   # Internal numeric/rule references (do not ship as app source)
├── scripts/                      # Token/constraint helpers (no app XML emission)
├── evals/
├── install.sh
└── README.md
```
