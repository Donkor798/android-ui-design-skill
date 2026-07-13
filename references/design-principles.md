# Design Principles — 深/浅色与 Material 映射规则

> **⚠️ 内部参考。** 历史 Kotlin/XML 示例已移除或不应外泄。  
> 调用 skill 时：只把规则写进 `design-spec` 表格；**禁止**向 app 交付 themes/styles 源码。

## 深色主题 vs 浅色主题

### 深色主题

**层次感靠发光，不靠阴影**
- 深色背景上看不见常规 shadow → 用 surface 提亮、primary tint、`{p}_glow` blur 描述分层
- design-spec 第 6 章：悬浮 blur=4/8/16 + glow 色

**状态栏**：深色背景 → 浅色图标；`status_bar` ≈ `background`

### 浅色主题

**层次感靠阴影 + 浅 surface**
- 卡片 elevation 2–8dp；shadowColor 约 `#1A000000`–`#33000000`
- 状态栏：浅色背景 → 深色图标

---

## Material3 角色映射（规范语言 · 非 themes.xml）

| Material 角色 | 本体系 token |
|---------------|--------------|
| colorPrimary | `{p}_primary` |
| colorOnPrimary | `{p}_on_primary` |
| colorSecondary | `{p}_secondary` |
| android:colorBackground | `{p}_background` |
| colorSurface | `{p}_surface` |
| colorOnSurface | `{p}_on_surface` |
| colorSurfaceVariant | `{p}_surface_variant` |
| colorError | `{p}_wrong` |
| Button / Card / BottomNav / Toolbar | 见 SKILL 第 8 章数值表 |

**禁止**在 design-spec 输出完整 `Theme.Game.*` / `Widget.Game.*` 资源 XML。

---

## Toolbar 规范摘要

| 项 | 值 |
|----|-----|
| 背景 | `{p}_background`（与页面齐平） |
| 标题 | `{p}_on_background` · 20sp Medium |
| 导航图标 | tint `{p}_on_surface` |
| elevation | 0 |

---

## 动态主题切换（产品规则）

- 主题 ID 与存储 key 一一对应（如 `neon_dark`）
- 切换后应用新 token；**实现代码不在本 skill 交付范围**
