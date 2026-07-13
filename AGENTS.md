# android-ui-design-skill

Android casual game **design-spec** system for Kotlin/Compose game apps. Provides 50 visual design themes as a full design language: color tokens, typography, shape, elevation, background, component specs, animation personality.

## Delivery contract (hard)

| Deliver | Do NOT deliver |
|---------|----------------|
| `design-spec_[theme].md` (markdown design contract) | App source: layout XML, Kotlin/Compose UI, `colors.xml`, `themes.xml`, `styles.xml`, `dimens.xml` |
| Exact tokens in **tables** (HEX, sp, dp) | Copy-paste resource files or View code |
| Structure described in prose / tables | `activity_*.xml` trees, `@+id/` dumps |

When theme is unspecified: recommend exactly 3 themes (card format) and wait for an explicit pick. Do not default to Neon Dark.

If the user asks for implementation code while this skill is active: refuse source delivery, point them to the design-spec, and suggest a separate implementation session.

## Activation

Invoke with `/android-ui-design-skill` or describe a task matching:
- "design a theme for my android game"
- "neon dark / space galaxy / candy pop theme"
- "game color scheme / ui style"
- "compare two themes" / "recommend theme for quiz game"

## Examples

```
/android-ui-design-skill neon dark theme
/android-ui-design-skill 所有主题列表
/android-ui-design-skill 新主题：海盗风格
/android-ui-design-skill compare sakura spring vs candy pop
/android-ui-design-skill 推荐适合 2048 游戏的主题
```

## Details

See [SKILL.md](./SKILL.md) for the 50-theme catalogue, forced 3-pick selection flow, identity card + 9-chapter design-spec system, delivery boundary, and token naming rules.

Gold sample: [examples/design-spec_neon_dark.md](./examples/design-spec_neon_dark.md). Skeleton: [examples/design-spec_skeleton.md](./examples/design-spec_skeleton.md).
