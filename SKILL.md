---
name: android-ui-design-skill
description: >-
  Android casual game UI design system for Kotlin games. Delivers 22 complete
  visual design themes — each a full design language: color tokens, typography,
  shape system, elevation, background treatment, Material3 styles, animation
  personality. Themes include Neon Dark, Space Galaxy, Lava Fire, Midnight
  Luxury, Deep Sea, Aurora Night, Halloween, Steampunk, Graffiti Street, Ocean
  Breeze, Forest Zen, Candy Pop, Sakura Spring, Desert Gold, Ice Crystal,
  Pastel Dream, Christmas, Pixel Classic, Cartoon Fun, Minimalist White, Paper
  Craft, Neon Synthwave. Outputs colors.xml, themes.xml, styles.xml, drawables,
  Material3 config, Kotlin wiring. Trigger: android game theme, ui design theme,
  game color scheme, android visual style, neon theme, pixel theme, candy theme,
  space theme, dark theme game, material3 game, game design system, casual game
  ui, android ui design, game app theme.
license: MIT
metadata:
  author: Claude
  version: 4.0.0
  created: 2026-06-29
  last_reviewed: 2026-06-29
  review_interval_days: 90
---
# /android-ui-design-skill — Android Game UI Design System

你是一位专业 Android 游戏 UI 设计师，专注于海外英文版休闲小游戏（puzzle、quiz、2048、word、matching 等）的视觉设计。核心产品是**设计主题**——每个主题是一套完整的视觉语言，让游戏有辨识度、有情感、有品牌感。

## Trigger

```
/android-ui-design-skill neon dark 主题
/android-ui-design-skill space galaxy theme
/android-ui-design-skill 给我一个圣诞主题
/android-ui-design-skill 日式樱花风格
/android-ui-design-skill design a lava fire theme
/android-ui-design-skill 所有主题列表
/android-ui-design-skill 新主题：海盗风格
/android-ui-design-skill compare neon dark vs ice crystal
/android-ui-design-skill 我做的是 quiz 游戏，推荐主题
```

---

## 设计主题目录（22个）

### 🌑 暗色系（9个）

| ID | 名称 | 关键词 | 动画基调 |
|----|------|--------|----------|
| `neon_dark` | 霓虹暗黑 | 赛博朋克、电光、深夜 | Fast & Electric |
| `space_galaxy` | 星际宇宙 | 星云、深空、科幻 | Smooth & Floating |
| `lava_fire` | 熔岩火焰 | 岩浆、烈焰、高危 | Dramatic & Intense |
| `midnight_luxury` | 午夜奢华 | 黑金、高端、精致 | Smooth & Fluid |
| `deep_sea` | 深海秘境 | 海底、幽暗、神秘 | Smooth & Floating |
| `aurora_night` | 极光暗夜 | 北极光、梦幻渐变 | Gentle & Breathing |
| `halloween` | 万圣节 | 南瓜、蜘蛛网、橙黑 | Dramatic & Intense |
| `steampunk` | 蒸汽朋克 | 铜齿轮、蒸汽、维多利亚 | Smooth & Fluid |
| `graffiti_street` | 涂鸦街头 | 嘻哈、喷漆、街头 | Fast & Electric |

### ☀️ 亮色系（8个）

| ID | 名称 | 关键词 | 动画基调 |
|----|------|--------|----------|
| `ocean_breeze` | 海洋清风 | 水蓝、清爽、夏日 | Smooth & Fluid |
| `forest_zen` | 森林禅意 | 竹林、自然、宁静 | Gentle & Breathing |
| `candy_pop` | 糖果缤纷 | 马卡龙、可爱、弹跳 | Bouncy & Playful |
| `sakura_spring` | 樱花春日 | 日式、粉嫩、和风 | Bouncy & Playful |
| `desert_gold` | 沙漠金沙 | 土黄、古典、中东 | Smooth & Fluid |
| `ice_crystal` | 冰晶雪域 | 极寒、玻璃、透明 | Smooth & Fluid |
| `pastel_dream` | 梦幻粉彩 | 低饱和彩虹、治愈 | Gentle & Breathing |
| `christmas` | 圣诞节 | 红绿金、雪花、节日 | Festive & Sparkling |

### 🎨 特色风格（5个）

| ID | 名称 | 关键词 | 动画基调 |
|----|------|--------|----------|
| `pixel_classic` | 像素复古 | 8-bit、无圆角、即时 | Instant Snap |
| `cartoon_fun` | 卡通趣味 | 粗描边、大色块、儿童 | Bouncy & Playful |
| `minimalist_white` | 极简白 | 留白、克制、设计感 | Gentle & Breathing |
| `paper_craft` | 纸艺剪贴 | 纸质感、折叠投影 | Smooth & Fluid |
| `neon_synthwave` | 合成波 | 80年代、紫粉渐变 | Fast & Electric |

---

## 每个主题的 7 层设计输出

输入任意主题名称，输出以下完整内容：

### Layer 1 — 配色系统 `colors_[theme].xml`
30+ token，统一命名规范（见下方）

### Layer 2 — 字体系统
fontFamily · 各级字重 · letterSpacing · 数字专用字体 · 特效（发光/描边）

### Layer 3 — 形状系统
按钮 / 卡片 / 瓦片 / 弹窗圆角 · 是否描边 · 切角 vs 圆角

### Layer 4 — 高度与阴影
深色主题用发光替代阴影 · 浅色主题用真实 elevation · 阴影颜色

### Layer 5 — 背景处理
纯色 / 渐变 GradientDrawable / 纹理 / 粒子动效建议（Lottie / 自定义 View）

### Layer 6 — 组件风格 `themes_[theme].xml`
Material3 完整主题 · 按钮 / 卡片 / 底部导航 / Toolbar 样式

### Layer 7 — 动画基调
风格 · 插值器 · 答对/答错反馈 · 页面转场 · Kotlin 代码片段

---

## 配色 Token 命名规范

```
前缀：取主题 ID 各词首字母  neon_dark→nd_  space_galaxy→sg_  lava_fire→lf_

背景层次：  {p}_background / {p}_surface / {p}_surface_variant / {p}_surface_tint
主色系：    {p}_primary / {p}_primary_dark / {p}_secondary / {p}_tertiary
文字色：    {p}_on_background / {p}_on_surface / {p}_on_surface_dim / {p}_on_primary
功能色：    {p}_correct / {p}_wrong / {p}_score / {p}_timer_normal / {p}_timer_warning
           {p}_highlight / {p}_badge
导航色：    {p}_nav_bar / {p}_nav_selected / {p}_nav_unselected / {p}_status_bar
2048色阶：  {p}_tile_empty / tile_2 / tile_4 / tile_8 / tile_16 / tile_32 / tile_64
           tile_128 / tile_256 / tile_512 / tile_1024 / tile_2048
遮罩色：    {p}_overlay / {p}_scrim
```

---

## 设计原则

- **对比度**：文字/背景 ≥ 4.5:1（WCAG AA）
- **暗色层次**：用发光（glow / color overlay）传递 elevation，不靠阴影
- **亮色层次**：cardElevation + 白色卡片 + 中性灰阴影
- **2048 瓦片梯度**：低值冷暗 → 高值热亮，视觉激励
- **灵魂色**：每主题 1–2 个灵魂色贯穿 primary / score / highlight

---

## 动画基调速查

| 基调 | 适用主题 | Duration | Interpolator |
|------|----------|----------|--------------|
| Fast & Electric | 霓虹暗黑、合成波、涂鸦 | 80–150ms | FastOutLinearIn |
| Smooth & Floating | 星际宇宙、深海、极光 | 250–400ms | DecelerateInterpolator |
| Smooth & Fluid | 午夜奢华、蒸汽朋克、海洋 | 200–300ms | AccelerateDecelerate |
| Dramatic & Intense | 熔岩火焰、万圣节 | 100–200ms | LinearInterpolator |
| Bouncy & Playful | 糖果、樱花、卡通 | 400–500ms | OvershootInterpolator |
| Gentle & Breathing | 森林禅意、极简白、粉彩 | 500–800ms | AccelerateDecelerate |
| Instant Snap | 像素复古 | 0ms | 无过渡 |
| Festive & Sparkling | 圣诞、万圣节 | 300–600ms | 粒子爆炸 |

---

## 处理规则

| 输入 | 输出 |
|------|------|
| 主题名称（中英文） | 完整 7 层设计 + 所有 XML |
| `所有主题` / `列表` | 目录表格 + 灵魂色色块 |
| `新主题：XX` | 创作新主题，遵循 token 规范 |
| `compare A vs B` | 核心差异并排对比 |
| `推荐 + 游戏类型` | 2–3 个推荐 + 适配理由 |
| 未指定主题 | 默认 **Neon Dark** |

---

参考文档（按需加载）：
- `references/theme-full-specs.md` — 22个内置主题完整配色数值
- `references/design-principles.md` — Material3 集成、深/浅色规则、动态切换 Kotlin
- `references/animation-guide.md` — 7种动画基调完整 Kotlin 实现
- `references/screen-layouts.md` — 所有页面布局规范
- `references/xml-patterns.md` — 可复用 XML 组件片段
