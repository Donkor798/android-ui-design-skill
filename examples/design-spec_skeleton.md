# design-spec_[theme_id] — 骨架模板（只填规范，不写源码）

> 复制本文件为 `design-spec_<theme_id>.md` 后按表填空。  
> **禁止** XML / Kotlin / Compose / `colors.xml`。

## 0. 主题辨识卡（必填，防换皮）

| 字段 | 填写 |
|------|------|
| Theme ID / 中文名 | |
| 模式 | Dark / Light |
| 材质一句话 | （场景 + 材质，禁止「精致/治愈」） |
| 灵魂色 1–2 | HEX + 名称 |
| 灵魂色分工 | primary= · score= · highlight= |
| Toolbar 唯一点缀 | （如 1dp hairline / 无） |
| 动画基调 | （8 选 1） |
| 本主题禁止 1 条 | |

---

## 第 1 章 — 配色系统

| Token | 色值 | 用途 |
|-------|------|------|
| {p}_background | | 页面背景 |
| {p}_surface | | 卡片表面 |
| {p}_surface_variant | | 次级表面 |
| {p}_surface_tint | | 染色表面 |
| {p}_primary | | CTA / 主强调 |
| {p}_primary_dark | | Pressed |
| {p}_secondary | | 次强调 |
| {p}_tertiary | | 点缀 |
| {p}_on_background | | 背景上文字 |
| {p}_on_surface | | 表面上文字 |
| {p}_on_surface_dim | | 次级文字 |
| {p}_on_primary | | 主色上文字 |
| {p}_correct | | 正确 |
| {p}_wrong | | 错误 |
| {p}_score | | 分数 |
| {p}_timer_normal | | 计时正常 |
| {p}_timer_warning | | 计时警告 |
| {p}_highlight | | 高亮/提示 |
| {p}_badge | | 徽章 |
| {p}_star | | 星级 |
| {p}_nav_bar | | 底栏背景 |
| {p}_nav_selected | | 底栏选中 |
| {p}_nav_unselected | | 底栏未选中 |
| {p}_status_bar | | 状态栏 |
| {p}_glow | | 深色发光；浅色写 n/a |
| {p}_overlay | | 遮罩 |
| {p}_scrim | | 弹窗遮罩 |
| 2048 tiles | 按需附录 | 非 2048 可省略 |

### 质量闸自检

| 检查项 | 结果 |
|--------|------|
| on_background / background ≥ 4.5:1 | ☐ |
| on_surface / surface ≥ 4.5:1 | ☐ |
| on_primary / primary ≥ 4.5:1 | ☐ |
| 灵魂色 ≤ 2 且分工已写 | ☐ |
| glow 深色有值 / 浅色 n/a | ☐ |

---

## 第 2 章 — 字体系统

| 属性 | 规范 |
|------|------|
| 主字体 | |
| 数字字体 | |
| Display | sp · weight · tracking · 仅 H1 |
| Headline | |
| Title / Toolbar Title | **20sp Medium** |
| Body | sp + lineHeight |
| Label | ≥12sp |
| 特效 | 仅 Display；Toolbar/Body 禁止 |

---

## 第 3 章 — 标题 + Toolbar + HUD

### 标题层级
（沿用全局 H1–H4 / Toolbar Title / Body / Caption）

### Toolbar 变体默认

| 变体 | 本主题参数 |
|------|------------|
| A App Shell | 背景 token · hairline 有/无 · 点缀 |
| B Subpage | 同上 + 返回箭头规格 |
| C Game HUD | 高 48–56 · 透明规则 |
| D Overlay | 圆底图标规则 |

### Game HUD 分玩法
（Quiz / 2048 / Word / Matching / Puzzle 各一行：leading · 数据位 · 数字色）

### 反模式
确认未触犯 SKILL 第 3 章 B5 十条。

---

## 第 4 章 — 图标
风格 filled/outlined · 尺寸表引用全局 · 着色 token

---

## 第 5 章 — 形状

| 组件 | 圆角 dp | 描边 |
|------|---------|------|
| 按钮 | | |
| 卡片 | | |
| 弹窗 | | |
| Chip | | |
| 瓦片 | | |
| Toolbar | 0 | |

---

## 第 6 章 — 高度与阴影
深色 glow blur 表 / 浅色 elevation 表

---

## 第 7 章 — 背景处理

| 页面 | 背景类型 | 规格 | 粒子/纹理上限 |
|------|----------|------|----------------|
| 首页 | | | |
| 列表壳 | | | |
| 局内 | | | 不得抢棋盘/题目 |
| 弹窗后 | scrim | | |

---

## 第 8 章 — 组件
按钮体系 56dp · Chip · 列表密度 · 首页 Hero · 弹窗/Pause/Game Over 全表填数值

---

## 第 9 章 — 动画
基调表 + 反馈优先级

---

## 间距 / 状态 / 无障碍
引用全局 token；bottom_nav=64 · toolbar=56 · button=56
