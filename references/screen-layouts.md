# Screen Layouts — 页面结构规范（设计约束，非布局源码）

> **本文件只描述结构与尺寸 token。**  
> 调用本 skill 时：**禁止**把下列内容改写成 `activity_*.xml` / Kotlin 交给 app。  
> 页面文件名（如 `home` / 历史 `activity_*` 称呼）仅作**结构锚点 ID**，不是要求生成该文件。

所有布局均适配任意主题；颜色引用 token `{theme_prefix}_*`，尺寸引用下方 `game_*` 表。

---

## 页面总览

| 类别 | 页面 | 结构锚点 ID（非源码路径） |
|------|------|---------------------------|
| App Shell | 首页 | `home` |
| App Shell | 历史页 | `history` |
| App Shell | 统计页 | `statistics` |
| App Shell | 设置页 | `settings` |
| App Shell | 玩法说明 | `how_to_play` |
| App Shell | 排行榜 | `leaderboard` |
| App Shell | 新手引导 | `onboarding` |
| 游戏页 | Quiz / 答题 | `game_quiz` |
| 游戏页 | 2048 | `game_2048` |
| 游戏页 | Puzzle 拼图 | `game_puzzle` |
| 游戏页 | Word Search | `game_word_search` |
| 游戏页 | Matching 配对 | `game_matching` |
| 游戏页 | Sudoku 数独 | `game_sudoku` |
| 结果/弹层 | 游戏结束 | `game_over` |
| 结果/弹层 | 暂停弹窗 | `dialog_pause` |
| 结果/弹层 | 过关弹窗 | `dialog_level_complete` |

---

## 标题栏变体速查（与 SKILL 第 3 章 B 节一致）

| 变体 | 页面 | 要点 |
|------|------|------|
| **无 Toolbar** | Home · Game Over | 品牌/结果用页面内 H1，不要套 56dp 栏 |
| **A · App Shell** | History · Stats · Settings | 56dp · 背景=background · 标题居中 · 无返回 · 无 elevation |
| **B · Subpage** | How to Play · Leaderboard · 二级页 | 56dp · 左返回 · 标题仍视觉居中 · 右 ≤2 动作 |
| **C · Game HUD** | 各游戏局内页 | 透明/近透明 · 无大标题 · pause + score/timer/hint |
| **D · Overlay** | 全屏插画/部分结果顶栏 | 透明 + 可选半透明圆底图标 |

自定义标题栏结构：`Leading 48×48 | Title 20sp 1行 | Actions ≤2×48`，总高 56dp，左右图标中心距屏边 ≥16dp。

---

## 首页 — `home`

**结构**：内容区 + Bottom Nav（无 Toolbar）

**Hero**：logo 120–140dp · biasY ≈ 0.18–0.24 · app name · tagline · PLAY 56×≥240 · last score 非按钮 · 可选 daily 卡高≤72dp  
**Bottom Nav**：Home · History · Stats · Settings · **64dp**

---

## 历史页 — `history`

Toolbar 变体 A · Chip 筛选 32dp · 双行列表 72dp · 分数 score 色数字字体 · 尾部 ≤1 result chip · 空状态统一

---

## 统计页 — `statistics`

Toolbar 变体 A · KPI 四卡高 80dp（窄屏 2×2）· 图表高 200dp · 分类行 · 成就 4 列

---

## 设置页 — `settings`

Toolbar 变体 A · 行高 56–64 · 分组 AUDIO / APPEARANCE / GAMEPLAY / DATA（Reset = destructive outlined）

---

## 玩法说明 — `how_to_play`

变体 B · 复杂：分页+图280+正文 lineHeight≥1.35 · 简单：步骤卡+底 Primary

---

## Quiz — `game_quiz`

HUD 变体 C：4dp 进度 · pause · 题号 · timer  
问题卡 minH 120 · 答案键 56 间距 12 · 对错改按钮色

---

## 2048 — `game_2048`

HUD：SCORE/BEST chip 40–48 · New compact · 棋盘正方形 · 数字对比≥4.5:1

---

## Word Search — `game_word_search`

HUD：level · timer · 底词 Chip 不进 HUD · 格态 default/selected/found

---

## Matching — `game_matching`

HUD：pairs · moves · timer（≤3 数据位）· 翻面反馈改卡色

---

## 游戏结束 — `game_over`

无 Toolbar · H1 · 星 3×48 · 分数卡 · Play Again Primary · Home Secondary · 一屏一实心主按钮

---

## 暂停 — `dialog_pause`

scrim 60–70% · 宽 280–320 或屏宽−48 · 圆角 12  
竖排：Resume Primary → Restart Secondary → Settings Text → Home Text

---

## 过关 — `dialog_level_complete`

标题 → 星 → 分数 → Continue Primary → Retry/Home Secondary · 星间隔 50–80ms

---

## 排行榜 — `leaderboard`

变体 B · 双行 72dp · 名次 · 昵称 · 分数右对齐 score 色

---

## 新手引导 — `onboarding`

变体 D 或无 · Skip Text · 1–3 页 · 底 Primary · 无 BottomNav

---

## 全局尺寸 Token（规范表 · 禁止输出为 dimens.xml）

| Token | 值 | 用途 |
|-------|-----|------|
| `game_padding_screen` | 16dp | 页边距 |
| `game_padding_card` | 16dp | 卡内边距 |
| `game_button_height` | 56dp | Primary CTA |
| `game_button_height_secondary` | 48dp | Secondary |
| `game_bottom_nav_height` | 64dp | 底栏 |
| `game_toolbar_height` | 56dp | 顶栏 |
| `game_hud_height` | 48–56dp | 局内 HUD |
| `game_logo_size` | 140dp | 首页 logo |
| `game_kpi_card_height` | 80dp | KPI |
| `game_chart_height` | 200dp | 图表 |
| `game_star_size` | 48dp | 结算星 |
| `game_list_row_single` | 56dp | 单行列表 |
| `game_list_row_two_line` | 72dp | 双行列表 |
| `game_chip_height` | 32dp | Chip |
| `game_dialog_min_width` | 280dp | 对话框 |
| `game_dialog_max_width` | 320dp | 对话框上限 |
| `game_toolbar_title_text` | 20sp | 顶栏标题 |
| `game_score_text` | 24sp | 分数参考 |
| `game_timer_text` | 22sp | 计时 |

> 抄进 design-spec 用 Markdown 表。**不要**输出 `<resources><dimen>` 源码给 app。
