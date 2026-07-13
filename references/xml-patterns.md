# Component Pattern Notes — Internal Constraint Derivation Only

> **⚠️ 内部参考，不是 skill 交付物。**  
> 历史 XML/Kotlin 片段已全部移除。  
> 调用 `/android-ui-design-skill` 时：只把下列**数值与结构**写进 `design-spec` 表格。  
> **禁止**生成或粘贴 app 布局/主题源码。

## KPI 卡（统计页）

| 项 | 约束 |
|----|------|
| 高度 | 80dp |
| 结构 | 上：22–28sp bold 数值（score 色）· 下：11–12sp dim label |
| 布局 | 4 卡均分；屏宽 < 360dp → 2×2 |
| 内边距 | 8–12dp |

## 历史列表行

| 项 | 约束 |
|----|------|
| 行高 | 72dp（双行） |
| Leading | 图标 36dp |
| 主文 | TitleSmall 游戏类型 |
| 副文 | LabelSmall 日期 |
| 尾部 | 分数数字字体 + score 色；最多 1 个 result chip |

## 主按钮 / 次按钮

| 类型 | 高度 | 最小宽 | 备注 |
|------|------|--------|------|
| Primary | 56dp | 240dp | 一屏一个实心 |
| Secondary | 48–56dp | 200dp | 1.5–2dp primary 描边 |
| Text | 48dp 热区 | — | 无底无边 |

## 底栏 / 顶栏

| 组件 | 高度 | 背景 |
|------|------|------|
| Toolbar | 56dp | background，elevation 0，标题 20sp 居中 |
| BottomNav | 64dp | nav_bar；图标 24 + label |
| Game HUD | 48–56dp | 透明/近透明；无大标题 |

## 对话框

| 项 | 约束 |
|----|------|
| 宽 | 280–320dp 或 屏宽−48 |
| 圆角 | 12dp（像素主题 0） |
| Scrim | 约 60–70% |
| Pause 按钮序 | Resume Primary → Restart Secondary → Settings/Home Text |

## Chip

高 32dp · 圆角全圆（主题可覆盖）· 间距 8dp · 选中态全项目统一一种

## 空状态

图标 64dp dim · 标题 H3 dim · 副文最多 2 行 · 可选一颗次/主按钮

> 完整规则以 `SKILL.md` 第 3/8 章为准。本文件仅作速查，永不输出为工程源码。
