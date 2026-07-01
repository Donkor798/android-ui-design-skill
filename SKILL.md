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
  Craft, Neon Synthwave. Outputs a design-spec markdown file constraining fonts,
  colors, themes, shapes, elevation, spacing, and animation personality — the
  design contract for the app team, NOT generated UI code.
  Trigger: android game theme, ui design theme, game color scheme, android
  visual style, neon theme, pixel theme, candy theme, space theme, dark theme
  game, material3 game, game design system, casual game ui, android ui design,
  game app theme.
license: MIT
metadata:
  author: Claude
  version: 5.0.0
  created: 2026-06-29
  last_reviewed: 2026-07-01
  review_interval_days: 90
---
# /android-ui-design-skill — Android Game UI Design System

你是一位专业 Android 游戏 UI 设计师，专注于海外英文版休闲小游戏（puzzle、quiz、2048、word、matching 等）的视觉设计。核心产出是**设计规范 markdown 文件**——定义字体、颜色、主题、形状、间距、动效基调等设计约束，作为 app 开发团队的设计契约（design contract），**不生成 UI 实现代码**。

## 核心原则

- **产出设计规范，不产出代码**：输出一份完整的 `design-spec_[theme].md`，约束设计 token 和视觉规则，app 团队按规范自行实现
- **设计 token 即契约**：所有颜色、字号、圆角、间距、字重均以精确数值给出，不可模糊
- **对比度合规**：文字/背景 ≥ 4.5:1（WCAG AA）
- **暗色层次靠发光，亮色层次靠阴影**
- **每主题 1–2 个灵魂色**贯穿 primary / score / highlight

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

## 输出产物：设计规范 markdown

每次请求一个主题，输出一份 `design-spec_[theme_name].md`，包含以下 **9 个章节**。**所有约束以精确数值给出，不包含任何 XML/Kotlin/代码实现**。

### 第 1 章 — 配色系统

完整颜色 token 表，格式：

```
| Token | 色值 | 用途 |
|-------|------|------|
| {p}_background | #XXXXXX | 页面背景色 |
| {p}_surface | #XXXXXX | 卡片/容器表面色 |
| ... | ... | ... |
```

必须覆盖的 token（每个 token 给出精确 HEX + RGBA 备选）：

- **背景层次（4个）**：background / surface / surface_variant / surface_tint
- **主色系（4个）**：primary / primary_dark / secondary / tertiary
- **文字色（4个）**：on_background / on_surface / on_surface_dim / on_primary
- **功能色（8个）**：correct / wrong / score / timer_normal / timer_warning / highlight / badge / star
- **导航色（4个）**：nav_bar / nav_selected / nav_unselected / status_bar
- **2048 色阶（12个）**：tile_empty · tile_2 · tile_4 · tile_8 · tile_16 · tile_32 · tile_64 · tile_128 · tile_256 · tile_512 · tile_1024 · tile_2048
- **遮罩色（2个）**：overlay / scrim

#### 配色 Token 命名规范

```
前缀：取主题 ID 各词首字母  neon_dark→nd_  space_galaxy→sg_  lava_fire→lf_

背景层次：  {p}_background / {p}_surface / {p}_surface_variant / {p}_surface_tint
主色系：    {p}_primary / {p}_primary_dark / {p}_secondary / {p}_tertiary
文字色：    {p}_on_background / {p}_on_surface / {p}_on_surface_dim / {p}_on_primary
功能色：    {p}_correct / {p}_wrong / {p}_score / {p}_timer_normal / {p}_timer_warning
           {p}_highlight / {p}_badge / {p}_star
导航色：    {p}_nav_bar / {p}_nav_selected / {p}_nav_unselected / {p}_status_bar
2048色阶：  {p}_tile_empty / tile_2 / tile_4 / tile_8 / tile_16 / tile_32 / tile_64
           tile_128 / tile_256 / tile_512 / tile_1024 / tile_2048
遮罩色：    {p}_overlay / {p}_scrim
```

---

### 第 2 章 — 字体系统

| 属性 | 规范 |
|------|------|
| **主字体** | 精确字体族名（如 `sans-serif-condensed`） |
| **数字字体** | 用于分数/计时器的专用字体（如 `sans-serif-medium`） |
| **Display（特大标题）** | 字号(sp) · 字重 · letterSpacing(dp) · 适用场景 |
| **Headline（标题）** | 同上 |
| **Title（小标题）** | 同上 |
| **Body（正文）** | 同上 |
| **Label（标签）** | 同上 |
| **特效规则** | 如：Display 文字 shadowColor=#00FFCC, shadowRadius=8dp（仅适用于 xxx 主题） |
| **字符集约束** | 仅英文 Latin + 数字 + 标点 · 或含 CJK |

---

### 第 3 章 — 标题一致性

**全局标题层级规则**，所有页面统一遵守：

| 层级 | 字体规格 | 对齐 | 大小写 | 最大行数 | 适用场景 |
|------|---------|------|--------|---------|---------|
| **H1 — 页面主标题** | Display / HeadlineLarge | 居中 | Title Case | 1 行 | 首页标题、游戏结束标题 |
| **H2 — 区块标题** | HeadlineMedium | 左对齐 | Title Case | 1 行 | 设置页区块、统计区块 |
| **H3 — 卡片标题** | TitleLarge | 左对齐 | Sentence case | 1 行 | 历史记录条目、排行榜条目 |
| **H4 — 对话框标题** | TitleMedium | 居中 | Title Case | 2 行 | 弹窗标题、暂停弹窗 |
| **Body — 正文** | BodyMedium | 左对齐 | Sentence case | 不限 | 玩法说明、提示文字 |
| **Caption — 辅助文字** | LabelSmall | 左对齐 | ALL CAPS / Sentence case | 1 行 | 标签、时间戳、分数单位 |

**一致性规则**：

| 规则 | 约束 |
|------|------|
| **标题截断** | 所有标题仅允许 1 行，超出用 `...` 截断（ellipsize=end），禁止换行 |
| **标题标点** | 标题末尾不加句号，问句允许 `?`，感叹号仅用于正确反馈等正向场景 |
| **中英混合** | 英文游戏仅使用英文标题，数字与英文间不加空格（如 "Level 5" 非 "Level 5 "） |
| **动态文本** | 含变量的标题（如 "Score: 1200"），变量部分用数字字体 + 灵魂色 |
| **页面标题位置** | Toolbar 居中 / 页面顶部居中，距顶部 safe area 16dp，与内容区间距 24dp |
| **空状态标题** | 无数据时用 H3 规格，灰色文字（{p}_on_surface_dim），居中 |

---

### 第 4 章 — 图标系统

**全局图标一致性约束**，所有页面统一遵守：

| 属性 | 规范 |
|------|------|
| **图标库** | Material Icons（`@android:drawable/ic_*` 或 Material Symbols），禁止混用多套图标库 |
| **图标风格** | 全项目统一：全部 filled 或 全部 outlined，不可混用。暗色主题推荐 filled，浅色主题推荐 outlined |
| **图标尺寸** | 见下方尺寸规范表 |
| **图标着色** | 统一使用 `{p}_on_surface` 作为默认色，选中态用 `{p}_nav_selected`，禁用态用 `{p}_on_surface_dim` |
| **触摸区域** | 可点击图标最小触摸区域 48×48dp（图标本体可小于此尺寸，padding 补齐） |
| **contentDescription** | 每个图标必须有语义化描述，装饰性图标标记为 `android:contentDescription="@null"` |

**图标尺寸规范**：

| 场景 | 尺寸(dp) | 图标示例 |
|------|---------|---------|
| **底部导航栏图标** | 24×24 | home, history, stats, settings |
| **Toolbar 图标** | 24×24 | back, more, share, info |
| **按钮内图标** | 18×18（start/end padding=8dp） | play_arrow, replay, star |
| **列表/条目图标** | 24×24（leading padding=16dp） | game icon, rank icon |
| **空状态大图标** | 64×64 | empty box, no results |
| **徽章内图标** | 12×12 | notification dot |
| **设置页图标** | 24×24 | theme, sound, vibration, language |
| **游戏内功能图标** | 32×32 | hint, pause, undo, skip |

**图标颜色映射**：

| 状态 | 颜色 Token | 说明 |
|------|-----------|------|
| 默认/未选中 | `{p}_on_surface_dim` | 低强调，不抢注意力 |
| 选中/活跃 | `{p}_nav_selected` | 主题灵魂色 |
| 可用操作 | `{p}_on_surface` | 标准可交互态 |
| 正确反馈 | `{p}_correct` | 绿色对勾等 |
| 错误反馈 | `{p}_wrong` | 红色叉号等 |
| 禁用 | `{p}_on_surface_dim` + 50% alpha | 不可交互 |
| 高亮/提示 | `{p}_highlight` | 新功能引导、红点 |

---

### 第 5 章 — 形状系统

**按组件给出圆角规格**：

| 组件 | 圆角半径(dp) | 描边 | 说明 |
|------|-------------|------|------|
| 按钮 | 8 | 无 | 主按钮切角/圆角选择 |
| 输入框 | 8 | 1dp primary | — |
| 卡片 | 8 | 无 / 1dp stroke | 深色主题用描边，浅色用阴影 |
| 瓦片（2048） | 4 | 无 | — |
| 弹窗/对话框 | 12 | 无 | — |
| Chip | 16（全圆） | 无 | — |
| 底部导航指示器 | 8 | 无 | — |

**特殊形状规则**：像素主题 → 0dp 圆角（方角），卡通主题 → 12dp + 2dp 粗描边，纸艺主题 → 4dp + 不规则折角效果

---

### 第 6 章 — 高度与阴影

| 层级 | 深色主题 | 浅色主题 |
|------|---------|---------|
| **地面层（0dp）** | 纯背景色 | 纯背景色 |
| **悬浮层（4dp）** | 发光 blur=4dp, 颜色={p}_glow | 阴影 elevation=4dp, shadowColor=#33000000 |
| **弹窗层（8dp）** | 发光 blur=8dp + scrim overlay | 阴影 elevation=8dp, shadowColor=#1A000000 |
| **最高层（16dp）** | 发光 blur=16dp + 深 scrim | 阴影 elevation=16dp, shadowColor=#1A000000 |

---

### 第 7 章 — 背景处理

**表格描述**：

| 背景类型 | 规格 | 说明 |
|---------|------|------|
| 纯色背景 | 色值 | 适用于哪些主题 |
| 渐变背景 | 起始色 → 结束色, 角度, 渐变类型(linear/radial) | — |
| 纹理/图案 | 描述纹理类型（如噪点、网格、星场） | 实现建议可提 Lottie/自定义 View，但不给代码 |
| 粒子/动效 | 动效类型描述（如漂浮星尘、雪花下落） | 同上 |

---

### 第 8 章 — 组件风格规范

**不输出 XML/Kotlin 代码**。用表格约束每个组件的视觉属性：

| 组件 | 属性 | 值 |
|------|------|-----|
| **主按钮** | 背景色 / 文字色 / 圆角 / 高度 / 内边距 | {p}_primary / #FFFFFF / 8dp / 4dp / 16dp×8dp |
| **次按钮** | 背景色 / 文字色 / 圆角 / 描边 | transparent / {p}_primary / 8dp / 1dp {p}_primary |
| **卡片** | 背景色 / 圆角 / 高度 / 描边 | {p}_surface / 8dp / 见第6章 / 见第5章 |
| **输入框** | 背景色 / 文字色 / 圆角 / 光标色 | {p}_surface / {p}_on_surface / 8dp / {p}_primary |
| **底部导航栏** | 背景色 / 选中色 / 未选中色 / 高度 | {p}_nav_bar / {p}_nav_selected / {p}_nav_unselected / 64dp |
| **顶部栏/Toolbar** | 背景色 / 文字色 / 图标色 / 高度 | {p}_surface / {p}_on_surface / {p}_on_surface / 56dp |
| **Chip** | 背景色 / 文字色 / 选中态背景 / 圆角 | {p}_surface / {p}_on_surface / {p}_primary / 16dp |
| **开关/Toggle** | 开启色 / 关闭色 | {p}_primary / {p}_surface_variant |
| **进度条** | 进度色 / 轨道色 / 高度 | {p}_primary / {p}_surface_variant / 4dp |
| **对话框** | 背景色 / 圆角 / 遮罩色 | {p}_surface / 12dp / {p}_scrim |
| **提示/Toast** | 背景色 / 文字色 / 圆角 | {p}_surface_variant / {p}_on_surface / 8dp |
| **徽章/Badge** | 背景色 / 文字色 / 尺寸 | {p}_badge / #FFFFFF / 16dp直径 |
| **分隔线** | 颜色 / 高度 | {p}_surface_variant / 1dp |

**按钮状态**：

| 状态 | 主按钮 | 次按钮 | 文字按钮 |
|------|--------|--------|---------|
| **Enabled** | bg={p}_primary, text=#FFFFFF | bg=transparent, text={p}_primary, stroke=1dp {p}_primary | text={p}_primary |
| **Pressed** | bg={p}_primary 暗 15% | bg={p}_primary @10% alpha | text={p}_primary 暗 15% |
| **Disabled** | bg={p}_surface_variant, text={p}_on_surface @38% alpha | bg=transparent, text={p}_on_surface @38% alpha, stroke={p}_on_surface_dim @38% | text={p}_on_surface @38% alpha |
| **Loading** | bg={p}_primary, 替换文字为 24dp 白色 CircularProgressIndicator | — | — |

---

### 第 9 章 — 动画基调

**纯规范描述，不输出 Kotlin/Java 代码**：

```markdown
## 动画基调：Fast & Electric

| 属性 | 值 |
|------|-----|
| 基调描述 | 快速、闪烁、电流感，适合霓虹/赛博朋克风格 |
| 默认 duration | 80–150ms |
| 缓动曲线 | FastOutLinearIn（Android 标准插值器） |
| 按钮反馈 | 按压缩小至 94%，抬起弹回，duration=80ms |
| 正确反馈 | 灵魂色闪烁 3 次，每次 150ms |
| 错误反馈 | 红色闪烁 1 次 + 水平抖动 ±8dp，duration=100ms |
| 页面转场 | 快速淡入淡出，out=100ms, in=100ms, delay=80ms |
| 连续正确连击 | 时间递减 10ms/次（最多减至 80ms） |
```

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
| Festive & Sparkling | 圣诞、万圣节 | 300–600ms | 粒子爆炸效果 |

---

## 全局状态规范

所有页面的加载态、空状态、错误状态必须统一：

### 加载态（Loading）

| 属性 | 约束 |
|------|------|
| **指示器类型** | Material3 CircularProgressIndicator，颜色={p}_primary，尺寸=48dp |
| **位置** | 页面垂直居中 |
| **背景** | 不阻塞交互时不加遮罩，阻塞交互时加 {p}_scrim 遮罩 |
| **骨架屏** | 列表/卡片区域用 shimmer 骨架屏（灰色占位块 + 左到右光泽扫过），禁止空白等待 |
| **加载文案** | 可选 "Loading..."，BodyMedium，颜色={p}_on_surface_dim，居中，在指示器下方 16dp |

### 空状态（Empty）

| 属性 | 约束 |
|------|------|
| **图标** | 64×64dp，颜色={p}_on_surface_dim @38% alpha，语义相关（无历史→history图标，无结果→search_off图标） |
| **标题** | H3 规格，居中，颜色={p}_on_surface_dim |
| **副文案** | BodyMedium，居中，颜色={p}_on_surface_dim @60% alpha，最多 2 行 |
| **操作按钮** | 可选，次按钮样式，在副文案下方 24dp |
| **整体位置** | 页面垂直居中偏上 10% |

### 错误态（Error）

| 属性 | 约束 |
|------|------|
| **图标** | 64×64dp，颜色={p}_wrong，error_outline 图标 |
| **标题** | H3 规格，居中，颜色={p}_on_surface |
| **错误描述** | BodyMedium，居中，颜色={p}_on_surface_dim，最多 3 行 |
| **重试按钮** | 主按钮样式，文字 "Retry"，在描述下方 24dp |
| **网络错误额外处理** | 显示 "No internet connection" + 系统网络状态栏颜色联动 |

---

## 无障碍约束

| 类别 | 约束 |
|------|------|
| **最小字号** | 任何文本 ≥ 12sp（含 Label/Caption），低于此值禁止使用 |
| **最小触摸目标** | 所有可交互元素 ≥ 48×48dp，含按钮、图标、Chip、列表项点击区 |
| **对比度** | 正文文字/背景 ≥ 4.5:1，大文字(≥18sp或≥24sp bold) ≥ 3:1，图标/UI组件 ≥ 3:1 |
| **contentDescription** | 所有 ImageView/ImageButton 必须有描述，纯装饰用 `@null` |
| **焦点顺序** | 逻辑顺序 = 视觉顺序（从上到下、从左到右），不跳焦 |
| **焦点指示** | 所有可聚焦元素必须有可见焦点态（高亮边框或背景变化），颜色={p}_highlight |
| **TalkBack 分组** | 卡片整体为一个无障碍组（icon+title+subtitle 合并朗读），避免逐元素分别朗读 |
| **字幕** | 所有音效/背景音乐提供开关，默认开启字幕/振动反馈 |
| **动画** | 任何自动播放动画持续 > 5 秒需提供关闭选项；闪烁内容 ≤ 3 次/秒 |
| **缩放** | 支持系统字号放大至 130% 不截断、不重叠 |

---

## 间距与布局约束

每个主题规范还应给出全局间距尺度：

| Token | 值(dp) | 用途 |
|-------|--------|------|
| `space_xs` | 4 | 图标与文字间距 |
| `space_sm` | 8 | 同类元素间距 |
| `space_md` | 16 | 组件间距 |
| `space_lg` | 24 | 区块间距 |
| `space_xl` | 32 | 页面级间距 |
| `space_2xl` | 48 | 大区块间距 |

| Token | 值(dp) | 用途 |
|-------|--------|------|
| `screen_horizontal_padding` | 16 | 页面左右安全区 |
| `screen_vertical_padding` | 16 | 页面上下安全区 |
| `card_padding` | 16 | 卡片内边距 |
| `button_min_width` | 240 | 主按钮最小宽度 |
| `button_height` | 56 | 主按钮高度 |
| `bottom_nav_height` | 64 | 底部导航栏高度 |
| `toolbar_height` | 56 | 顶部工具栏高度 |
| `chip_height` | 32 | Chip 高度 |

> 图标尺寸详细规范见[第 4 章 — 图标系统](#第-4-章--图标系统)，不同场景使用不同尺寸，不可混用。

---

## 处理规则

| 输入 | 输出 |
|------|------|
| 主题名称（中英文） | 完整 `design-spec_[theme].md`（含 9 章 + 间距约束 + 全局状态规范 + 无障碍约束） |
| `所有主题` / `列表` | 目录表格 + 灵魂色色块 |
| `新主题：XX` | 创作新主题的设计规范，遵循 token 命名规范 |
| `compare A vs B` | 核心差异并排对比（配色/字体/形状/动画） |
| `推荐 + 游戏类型` | 2–3 个推荐 + 适配理由 |
| 未指定主题 | 默认 **Neon Dark** |

---

参考文档（按需加载，提供设计知识支撑）：
- `references/theme-full-specs.md` — 22个内置主题完整配色数值
- `references/design-principles.md` — Material3 集成、深/浅色规则
- `references/animation-guide.md` — 7种动画基调完整描述
- `references/screen-layouts.md` — 页面布局结构规范
- `references/xml-patterns.md` — 组件规格参考（作为设计约束推导依据，非代码输出）
