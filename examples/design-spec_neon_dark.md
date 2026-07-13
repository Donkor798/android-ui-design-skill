# design-spec_neon_dark — Neon Dark 设计规范

> **交付形态**：设计契约 Markdown。  
> **禁止**：XML / Kotlin / Compose / 资源文件。  
> Theme ID: `neon_dark` · Prefix: `nd_` · Mode: Dark

## 0. 主题辨识卡

| 字段 | 值 |
|------|-----|
| 材质一句话 | 湿沥青路面 + 粉红/青色灯管，高对比夜间竞速感 |
| 灵魂色 | Electric Pink `#E94560` · Neon Cyan `#00FFCC` |
| 灵魂色分工 | primary=CTA/选中 · score=金 `#FFD700` · highlight/timer=青 `#00FFCC` |
| Toolbar 点缀 | 可选底边 1dp `nd_primary` @40%；默认无 elevation |
| 动画基调 | Fast & Electric（80–150ms · FastOutLinearIn） |
| 本主题禁止 | Toolbar/正文标题外发光；整栏 primary 填充；局内完整 Toolbar |

---

## 第 1 章 — 配色系统

| Token | 色值 | 用途 |
|-------|------|------|
| nd_background | #0D0D0D | 页面背景 |
| nd_surface | #1A1A2E | 卡片/容器 |
| nd_surface_variant | #16213E | 次级表面/轨道 |
| nd_surface_tint | #1F1035 | 染色表面 |
| nd_primary | #E94560 | CTA、选中、强调 |
| nd_primary_dark | #C73652 | Pressed |
| nd_secondary | #0F3460 | 次强调容器 |
| nd_tertiary | #533483 | 点缀紫 |
| nd_on_background | #EAEAEA | 背景上主文字 |
| nd_on_surface | #EAEAEA | 表面上文字 |
| nd_on_surface_dim | #757575 | 次级文字/未选中 |
| nd_on_primary | #FFFFFF | 主色上文字 |
| nd_correct | #00E676 | 正确 |
| nd_wrong | #FF1744 | 错误 |
| nd_score | #FFD700 | 分数 |
| nd_timer_normal | #00FFCC | 计时正常 |
| nd_timer_warning | #FF6D00 | 计时警告 |
| nd_highlight | #00FFCC | 提示/选中格 |
| nd_badge | #E94560 | 徽章 |
| nd_star | #FFD700 | 星级点亮 |
| nd_nav_bar | #1A1A2E | 底栏（可与 surface 同） |
| nd_nav_selected | #E94560 | 底栏选中 |
| nd_nav_unselected | #555555 | 底栏未选中 |
| nd_status_bar | #0D0D0D | 状态栏 = background |
| nd_glow | #00FFCC | 深色悬浮发光 |
| nd_overlay | #CC0D0D0D | 轻遮罩 |
| nd_scrim | #990D0D0D | 弹窗遮罩约 60% |
| nd_tile_empty … tile_2048 | 见 theme-full-specs | 仅 2048 附录 |

### 质量闸

| 检查项 | 结果 |
|--------|------|
| on_background / background | 通过（浅灰 on 近黑） |
| on_primary / primary | 通过（白 on 粉） |
| 灵魂色数量 | 2（粉+青），金仅作 score |
| glow | 有 HEX |
| 禁用 Material 默认紫 | 是 |

---

## 第 2 章 — 字体系统

| 属性 | 规范 |
|------|------|
| 主字体 | `sans-serif-condensed` |
| 数字字体 | `sans-serif-medium`（分数/计时等宽感优先） |
| Display | 32sp · Bold · tracking 0 · **仅** 首页 app name / Game Over H1；允许 `shadowColor=#00FFCC, radius=8dp` |
| Headline | 24sp · Medium |
| Title / Toolbar Title | **20sp · Medium · tracking 0–0.01** · 无特效 |
| Body | 14–16sp · Regular · lineHeight ≥ 1.35 |
| Label | 12sp · Medium · 可 ALL CAPS |
| 特效范围 | Display/H1 only；Toolbar、Body、Label **禁止** 发光字 |

### 文案长度
Toolbar 标题 ≤22 · Primary 按钮 ≤16 · Chip ≤14 · 均 1 行 ellipsize。

---

## 第 3 章 — 标题一致性 + 标题栏

### A. 层级
全局 H1–H4 / Toolbar Title 20sp / Body / Caption（见 skill 默认表）。动态数字用数字字体 + `nd_score` 或 timer token。

### B. Toolbar 变体

| 变体 | 高度 | 背景 | 标题 | 左右 | 分隔 |
|------|------|------|------|------|------|
| A App Shell | 56 | nd_background | 20sp 居中 | 无返回 · 右 ≤1 | 默认无；可选 1dp primary@40% 底边 |
| B Subpage | 56 | nd_background | 视觉居中 | arrow_back 24 · 右 ≤2 | 可选 hairline surface_variant |
| C Game HUD | 48–56 | 透明或 background@8% | 无大标题 | pause 32 · 数据位 ≤3 | **禁止**分隔与阴影 |
| D Overlay | 56 | 透明 | 可选短标题 | 半透明圆底返回 | 无 |

首页 / Game Over：**无 Toolbar**。

### B6. Game HUD

| 玩法 | Leading | 数据位 | 数字色 |
|------|---------|--------|--------|
| Quiz | pause | timer · 题号 | timer 青 / dim |
| 2048 | 可选 pause | SCORE · BEST chip | score 金 |
| Word | pause | level · timer | timer |
| Matching | pause | pairs · moves · timer | score / on_surface / timer |
| Puzzle | pause · undo | timer · errors | timer / wrong |

### 反模式（本主题特别强调）
禁止 28sp+ 塞进 56dp 栏；禁止顶栏大渐变/强 glow；禁止局内套 Settings 风 Toolbar。

---

## 第 4 章 — 图标系统

| 项 | 值 |
|----|-----|
| 库 | Material Icons / Symbols |
| 风格 | **filled**（暗色） |
| Toolbar / 底栏图标 | 24dp · 热区 48dp |
| 局内功能 | 32dp 视觉 / 48 热区 |
| 默认色 | on_surface；选中 nav_selected；dim 未选中 |

---

## 第 5 章 — 形状系统

| 组件 | 圆角 | 描边 |
|------|------|------|
| 按钮 | 8dp | 无（次按钮 1.5–2dp primary） |
| 卡片 | 8dp | 1dp surface_variant 或 primary@30%（深色分层） |
| 瓦片 2048 | 4dp | 无 |
| 弹窗 | 12dp | 无 |
| Chip | 16dp 全圆 | 未选可选 1dp |
| Toolbar | 0 | 可选底边细线 |

---

## 第 6 章 — 高度与阴影

| 层级 | 规范（深色） |
|------|----------------|
| 地面 0 | background |
| 悬浮 4 | glow blur=4 · nd_glow；卡片优先描边而非大 elevation |
| 弹窗 8 | scrim + 可选 glow blur=8 |
| 最高 16 | 深 scrim；少用 |

---

## 第 7 章 — 背景处理

| 页面 | 类型 | 规格 | 上限 |
|------|------|------|------|
| 首页 | 纯色 + 可选极弱径向 | background；中心可 5–8% primary 暗晕 | 禁止动态粒子抢 PLAY |
| 列表壳 (History/Stats/Settings) | 纯色 background | 与 Toolbar 齐平 | 禁止大图头 |
| 局内 | 纯色 background | 棋盘/题卡为视觉中心 | **禁止**强粒子/扫描线铺满 |
| 弹窗后 | scrim | nd_scrim ~60% | 内容可读 |

纹理：可选 2–3% 噪点叠加描述即可，不强制。

---

## 第 8 章 — 组件风格规范

### 按钮体系

| 类型 | 高度 | 最小宽 | 背景/描边 | 文字 |
|------|------|--------|-----------|------|
| Primary CTA | **56dp** | 240 | 实心 nd_primary | on_primary · ≤16 字符 |
| Secondary | 48–56 | 200 | 透明 + 1.5–2dp primary | primary |
| Text | 48 热区 | — | 无 | primary |
| Compact | 40 | — | 实心或线框 | 12–14sp |
| Destructive | 48–56 | — | outlined wrong | wrong |

**一屏一主**；Pause 竖排 Resume→Restart→Settings→Home。

### Chip
高 32 · 间距 8 · 选中 solid primary 或 primary@20%（全项目择一）。

### 列表密度
单行 56–64 · 双行 72 · KPI 80 · 窄屏 KPI 2×2。

### 首页 Hero
logo 120–140 · name Display 可青光 · tagline dim · PLAY 56×≥240 · last score 非按钮 · 无 Toolbar。

### 弹窗
宽 280–320 或屏宽−48 · 圆角 12 · surface · scrim 60% · 标题 H4。

### 顶栏
见第 3 章；高度 56 · elevation 0 · 标题 20sp。

### 底栏
高 **64** · nav_bar · 选中 primary · 未选 dim（本规范不展开专章，数值锁定）。

---

## 第 9 章 — 动画基调：Fast & Electric

| 属性 | 值 |
|------|-----|
| duration | 80–150ms |
| 曲线 | FastOutLinearIn |
| 按钮 | 按压 scale 94% · 80ms |
| 正确 | **优先** 组件变 correct；可选短闪 ≤3 次/秒 |
| 错误 | 组件 wrong + 水平抖 ±8dp；禁止连续全屏红闪 |
| 转场 | fade 100/100 |

---

## 间距（摘录）

| Token | 值 |
|-------|-----|
| screen padding | 16 |
| button_height | **56** |
| bottom_nav_height | **64** |
| toolbar_height | **56** |
| chip_height | 32 |
| dialog min/max width | 280 / 320 |

## 全局状态 / 无障碍
Loading 48 primary 居中 · Empty 64 图标 dim · Error wrong 图标 + Retry Primary。  
最小字 12sp · 热区 48 · 对比度 AA · 闪烁 ≤3 次/秒。

## 自检清单
- [x] 仅 markdown 规范，无源码  
- [x] glow + 质量闸  
- [x] Toolbar 变体 + HUD  
- [x] 主按钮 56 · 底栏 64  
- [x] 背景分层未抢局内  
