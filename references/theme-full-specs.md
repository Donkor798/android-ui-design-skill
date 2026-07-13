# Theme Full Specs — 50 个主题完整配色数值

> **内部色板（纯 Markdown 表）。** 只把 HEX/token 抄进 `design-spec` 第 1 章。
> **禁止**输出为 `colors_*.xml` / 任何 app 资源文件。
>
> 数值以 `scripts/generate_theme.py` 的 `THEMES` 为单一真相；本文件可用
> `python3 scripts/generate_theme.py --write-full-specs` 重新生成。

---

## NEON DARK — 霓虹暗黑

- **ID**: `neon_dark` · **Prefix**: `nd_` · **Mode**: Dark
- **材质 / 场景**: 湿沥青路面 + 粉红/青色灯管
- **动画基调**: Fast & Electric
- **灵魂色分工**: primary=CTA粉 · score=金 · highlight/timer=青
- **Toolbar 点缀**: 底边 1dp primary@40%
- **禁止**: Toolbar 内标题外发光

| Token | Value |
|-------|-------|
| nd_background | #0D0D0D |
| nd_surface | #1A1A2E |
| nd_surface_variant | #16213E |
| nd_surface_tint | #1F1035 |
| nd_primary | #E94560 |
| nd_primary_dark | #C73652 |
| nd_secondary | #0F3460 |
| nd_tertiary | #533483 |
| nd_on_background | #EAEAEA |
| nd_on_surface | #EAEAEA |
| nd_on_surface_dim | #757575 |
| nd_on_primary | #FFFFFF |
| nd_correct | #00E676 |
| nd_wrong | #FF1744 |
| nd_score | #FFD700 |
| nd_timer_normal | #00FFCC |
| nd_timer_warning | #FF6D00 |
| nd_highlight | #00FFCC |
| nd_badge | #E94560 |
| nd_star | #FFD700 |
| nd_nav_bar | #1A1A2E |
| nd_nav_selected | #E94560 |
| nd_nav_unselected | #555555 |
| nd_status_bar | #0D0D0D |
| nd_glow | #00FFCC |
| nd_tile_empty | #16213E |
| nd_tile_2 | #1A1A3E |
| nd_tile_4 | #1E1E4A |
| nd_tile_8 | #533483 |
| nd_tile_16 | #6A3D9A |
| nd_tile_32 | #E94560 |
| nd_tile_64 | #C73652 |
| nd_tile_128 | #00FFCC |
| nd_tile_256 | #00CCB0 |
| nd_tile_512 | #FFD700 |
| nd_tile_1024 | #FF6D00 |
| nd_tile_2048 | #FFFFFF |
| nd_overlay | #CC0D0D0D |
| nd_scrim | #990D0D0D |

---

## SPACE GALAXY — 星际宇宙

- **ID**: `space_galaxy` · **Prefix**: `sg_` · **Mode**: Dark
- **材质 / 场景**: 深蓝真空 + 星云紫 + 星点
- **动画基调**: Smooth & Floating
- **灵魂色分工**: primary=星云紫 CTA · score=星光黄 · highlight=星青
- **Toolbar 点缀**: 无；HUD 数字用 secondary
- **禁止**: 整栏紫渐变

| Token | Value |
|-------|-------|
| sg_background | #06061A |
| sg_surface | #0D0D2B |
| sg_surface_variant | #151540 |
| sg_surface_tint | #1A1050 |
| sg_primary | #7B2FBE |
| sg_primary_dark | #5C1F9E |
| sg_secondary | #4CC9F0 |
| sg_tertiary | #F72585 |
| sg_on_background | #E8E8FF |
| sg_on_surface | #E8E8FF |
| sg_on_surface_dim | #6060A0 |
| sg_on_primary | #FFFFFF |
| sg_correct | #4CC9F0 |
| sg_wrong | #F72585 |
| sg_score | #FFD60A |
| sg_timer_normal | #4CC9F0 |
| sg_timer_warning | #F72585 |
| sg_highlight | #4CC9F0 |
| sg_badge | #F72585 |
| sg_star | #FFD60A |
| sg_nav_bar | #0D0D2B |
| sg_nav_selected | #7B2FBE |
| sg_nav_unselected | #404070 |
| sg_status_bar | #06061A |
| sg_glow | #4CC9F0 |
| sg_tile_empty | #0D0D3A |
| sg_tile_2 | #151560 |
| sg_tile_4 | #1E1E80 |
| sg_tile_8 | #4A1E8C |
| sg_tile_16 | #7B2FBE |
| sg_tile_32 | #9B4FDE |
| sg_tile_64 | #4CC9F0 |
| sg_tile_128 | #3BB8DF |
| sg_tile_256 | #F72585 |
| sg_tile_512 | #FFD60A |
| sg_tile_1024 | #FFFFFF |
| sg_tile_2048 | #FFD60A |
| sg_overlay | #CC06061A |
| sg_scrim | #9906061A |

---

## LAVA FIRE — 熔岩火焰

- **ID**: `lava_fire` · **Prefix**: `lf_` · **Mode**: Dark
- **材质 / 场景**: 焦黑岩层 + 熔橙裂缝
- **动画基调**: Dramatic & Intense
- **灵魂色分工**: primary=熔橙 CTA · score=亮黄 · highlight=同黄
- **Toolbar 点缀**: 无 elevation
- **禁止**: 全局常驻红闪背景

| Token | Value |
|-------|-------|
| lf_background | #0A0000 |
| lf_surface | #1A0800 |
| lf_surface_variant | #2D1000 |
| lf_surface_tint | #3D1500 |
| lf_primary | #FF4500 |
| lf_primary_dark | #CC3700 |
| lf_secondary | #FFB700 |
| lf_tertiary | #FF0050 |
| lf_on_background | #FFE0CC |
| lf_on_surface | #FFE0CC |
| lf_on_surface_dim | #8B5E40 |
| lf_on_primary | #FFFFFF |
| lf_correct | #FFB700 |
| lf_wrong | #FF0050 |
| lf_score | #FFE566 |
| lf_timer_normal | #FFB700 |
| lf_timer_warning | #FF0050 |
| lf_highlight | #FFB700 |
| lf_badge | #FF4500 |
| lf_star | #FFE566 |
| lf_nav_bar | #1A0800 |
| lf_nav_selected | #FF4500 |
| lf_nav_unselected | #5C3020 |
| lf_status_bar | #0A0000 |
| lf_glow | #FFB700 |
| lf_tile_empty | #1A0800 |
| lf_tile_2 | #2D1000 |
| lf_tile_4 | #4A1800 |
| lf_tile_8 | #7A2800 |
| lf_tile_16 | #AA3800 |
| lf_tile_32 | #CC3700 |
| lf_tile_64 | #FF4500 |
| lf_tile_128 | #FF6B00 |
| lf_tile_256 | #FFB700 |
| lf_tile_512 | #FFD700 |
| lf_tile_1024 | #FFE566 |
| lf_tile_2048 | #FFFFFF |
| lf_overlay | #CC0A0000 |
| lf_scrim | #990A0000 |

---

## MIDNIGHT LUXURY — 午夜奢华

- **ID**: `midnight_luxury` · **Prefix**: `ml_` · **Mode**: Dark
- **材质 / 场景**: 哑光黑漆 + 香槟金细线
- **动画基调**: Smooth & Fluid
- **灵魂色分工**: primary=香槟金 CTA/描边 · score=同金
- **Toolbar 点缀**: 底边 1dp 金 hairline
- **禁止**: 厚金条铺满顶栏

| Token | Value |
|-------|-------|
| ml_background | #0A0A0A |
| ml_surface | #141414 |
| ml_surface_variant | #1E1E1E |
| ml_surface_tint | #1A1A0A |
| ml_primary | #D4AF37 |
| ml_primary_dark | #B8941F |
| ml_secondary | #C0C0C0 |
| ml_tertiary | #E8D5A3 |
| ml_on_background | #F5F5F0 |
| ml_on_surface | #F5F5F0 |
| ml_on_surface_dim | #808080 |
| ml_on_primary | #0A0A0A |
| ml_correct | #4CAF50 |
| ml_wrong | #F44336 |
| ml_score | #D4AF37 |
| ml_timer_normal | #C0C0C0 |
| ml_timer_warning | #FF6F00 |
| ml_highlight | #D4AF37 |
| ml_badge | #D4AF37 |
| ml_star | #D4AF37 |
| ml_nav_bar | #141414 |
| ml_nav_selected | #D4AF37 |
| ml_nav_unselected | #505050 |
| ml_status_bar | #0A0A0A |
| ml_glow | #D4AF37 |
| ml_tile_empty | #1E1E1E |
| ml_tile_2 | #2A2A2A |
| ml_tile_4 | #363636 |
| ml_tile_8 | #4A3810 |
| ml_tile_16 | #6B5220 |
| ml_tile_32 | #8C6C2A |
| ml_tile_64 | #B8941F |
| ml_tile_128 | #D4AF37 |
| ml_tile_256 | #DFC060 |
| ml_tile_512 | #E8D080 |
| ml_tile_1024 | #F0E0A0 |
| ml_tile_2048 | #FFFFFF |
| ml_overlay | #E50A0A0A |
| ml_scrim | #990A0A0A |

---

## DEEP SEA — 深海秘境

- **ID**: `deep_sea` · **Prefix**: `ds_` · **Mode**: Dark
- **材质 / 场景**: 深渊蓝黑 + 生物荧光青
- **动画基调**: Smooth & Floating
- **灵魂色分工**: primary=生物荧光青 CTA · score=同青 · highlight=浅荧光
- **Toolbar 点缀**: 无
- **禁止**: 高饱和红作主 CTA

| Token | Value |
|-------|-------|
| ds_background | #000A1A |
| ds_surface | #001830 |
| ds_surface_variant | #00243F |
| ds_surface_tint | #00305A |
| ds_primary | #00CFFF |
| ds_primary_dark | #009CC0 |
| ds_secondary | #0055AA |
| ds_tertiary | #7FFFFF |
| ds_on_background | #B0E8FF |
| ds_on_surface | #B0E8FF |
| ds_on_surface_dim | #405070 |
| ds_on_primary | #000A1A |
| ds_correct | #7FFFFF |
| ds_wrong | #FF4466 |
| ds_score | #00CFFF |
| ds_timer_normal | #00CFFF |
| ds_timer_warning | #FF4466 |
| ds_highlight | #7FFFFF |
| ds_badge | #00CFFF |
| ds_star | #00CFFF |
| ds_nav_bar | #001830 |
| ds_nav_selected | #00CFFF |
| ds_nav_unselected | #204060 |
| ds_status_bar | #000A1A |
| ds_glow | #7FFFFF |
| ds_tile_empty | #00243F |
| ds_tile_2 | #003060 |
| ds_tile_4 | #004080 |
| ds_tile_8 | #0055AA |
| ds_tile_16 | #0070CC |
| ds_tile_32 | #0090EE |
| ds_tile_64 | #00CFFF |
| ds_tile_128 | #7FFFFF |
| ds_tile_256 | #AAFFFF |
| ds_tile_512 | #FF4466 |
| ds_tile_1024 | #FF8800 |
| ds_tile_2048 | #FFFFFF |
| ds_overlay | #CC000A1A |
| ds_scrim | #99000A1A |

---

## AURORA NIGHT — 极光暗夜

- **ID**: `aurora_night` · **Prefix**: `an_` · **Mode**: Dark
- **材质 / 场景**: 极夜天空 + 绿紫光带
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| an_background | #060812 |
| an_surface | #0C1020 |
| an_surface_variant | #131828 |
| an_surface_tint | #1A2030 |
| an_primary | #00FF88 |
| an_primary_dark | #00CC66 |
| an_secondary | #AA00FF |
| an_tertiary | #00CCFF |
| an_on_background | #D0FFE8 |
| an_on_surface | #D0FFE8 |
| an_on_surface_dim | #406050 |
| an_on_primary | #060812 |
| an_correct | #00FF88 |
| an_wrong | #FF4488 |
| an_score | #00CCFF |
| an_timer_normal | #00FF88 |
| an_timer_warning | #FF4488 |
| an_highlight | #AA00FF |
| an_badge | #00FF88 |
| an_star | #00CCFF |
| an_nav_bar | #0C1020 |
| an_nav_selected | #00FF88 |
| an_nav_unselected | #304040 |
| an_status_bar | #060812 |
| an_glow | #AA00FF |
| an_tile_empty | #131828 |
| an_tile_2 | #1A2535 |
| an_tile_4 | #003322 |
| an_tile_8 | #006644 |
| an_tile_16 | #00AA66 |
| an_tile_32 | #00FF88 |
| an_tile_64 | #00CCFF |
| an_tile_128 | #AA00FF |
| an_tile_256 | #CC44FF |
| an_tile_512 | #FF4488 |
| an_tile_1024 | #FFCC00 |
| an_tile_2048 | #FFFFFF |
| an_overlay | #CC060812 |
| an_scrim | #99060812 |

---

## HALLOWEEN — 万圣节

- **ID**: `halloween` · **Prefix**: `hw_` · **Mode**: Dark
- **材质 / 场景**: 焦橙南瓜 + 紫雾 + 骨白
- **动画基调**: Dramatic & Intense

| Token | Value |
|-------|-------|
| hw_background | #0D0800 |
| hw_surface | #1A1000 |
| hw_surface_variant | #2A1A00 |
| hw_surface_tint | #301800 |
| hw_primary | #FF6600 |
| hw_primary_dark | #CC5200 |
| hw_secondary | #8B00FF |
| hw_tertiary | #00CC66 |
| hw_on_background | #F0E0C0 |
| hw_on_surface | #F0E0C0 |
| hw_on_surface_dim | #806040 |
| hw_on_primary | #FFFFFF |
| hw_correct | #00CC66 |
| hw_wrong | #FF1744 |
| hw_score | #FF6600 |
| hw_timer_normal | #FF6600 |
| hw_timer_warning | #FF1744 |
| hw_highlight | #8B00FF |
| hw_badge | #FF6600 |
| hw_star | #FF6600 |
| hw_nav_bar | #1A1000 |
| hw_nav_selected | #FF6600 |
| hw_nav_unselected | #604020 |
| hw_status_bar | #0D0800 |
| hw_glow | #8B00FF |
| hw_tile_empty | #1A1000 |
| hw_tile_2 | #2A1A00 |
| hw_tile_4 | #3D2800 |
| hw_tile_8 | #5C3A00 |
| hw_tile_16 | #7A4E00 |
| hw_tile_32 | #CC5200 |
| hw_tile_64 | #FF6600 |
| hw_tile_128 | #8B00FF |
| hw_tile_256 | #6A00CC |
| hw_tile_512 | #00CC66 |
| hw_tile_1024 | #FF1744 |
| hw_tile_2048 | #F0F0F0 |
| hw_overlay | #CC0D0800 |
| hw_scrim | #990D0800 |

---

## STEAMPUNK — 蒸汽朋克

- **ID**: `steampunk` · **Prefix**: `sp_` · **Mode**: Dark
- **材质 / 场景**: 黄铜齿轮 + 皮革褐 + 煤烟灰
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| sp_background | #1A1008 |
| sp_surface | #2A1C0C |
| sp_surface_variant | #3A2810 |
| sp_surface_tint | #4A3418 |
| sp_primary | #B87333 |
| sp_primary_dark | #8A5520 |
| sp_secondary | #D4A838 |
| sp_tertiary | #7A6040 |
| sp_on_background | #F0D898 |
| sp_on_surface | #F0D898 |
| sp_on_surface_dim | #907050 |
| sp_on_primary | #1A1008 |
| sp_correct | #88CC44 |
| sp_wrong | #CC4422 |
| sp_score | #D4A838 |
| sp_timer_normal | #B87333 |
| sp_timer_warning | #CC4422 |
| sp_highlight | #D4A838 |
| sp_badge | #B87333 |
| sp_star | #D4A838 |
| sp_nav_bar | #2A1C0C |
| sp_nav_selected | #B87333 |
| sp_nav_unselected | #706040 |
| sp_status_bar | #1A1008 |
| sp_glow | #D4A838 |
| sp_tile_empty | #2A1C0C |
| sp_tile_2 | #3A2810 |
| sp_tile_4 | #5A3C18 |
| sp_tile_8 | #7A5020 |
| sp_tile_16 | #8A5520 |
| sp_tile_32 | #B87333 |
| sp_tile_64 | #C88840 |
| sp_tile_128 | #D4A838 |
| sp_tile_256 | #E0BC50 |
| sp_tile_512 | #EED068 |
| sp_tile_1024 | #F5E080 |
| sp_tile_2048 | #FFFACC |
| sp_overlay | #CC1A1008 |
| sp_scrim | #991A1008 |

---

## GRAFFITI STREET — 涂鸦街头

- **ID**: `graffiti_street` · **Prefix**: `gs_` · **Mode**: Dark
- **材质 / 场景**: 水泥墙 + 喷漆黄/蓝/红
- **动画基调**: Fast & Electric

| Token | Value |
|-------|-------|
| gs_background | #111111 |
| gs_surface | #1E1E1E |
| gs_surface_variant | #2E2E2E |
| gs_surface_tint | #333333 |
| gs_primary | #FFEB00 |
| gs_primary_dark | #CCBB00 |
| gs_secondary | #0044FF |
| gs_tertiary | #FF2200 |
| gs_on_background | #FFFFFF |
| gs_on_surface | #FFFFFF |
| gs_on_surface_dim | #888888 |
| gs_on_primary | #111111 |
| gs_correct | #00FF44 |
| gs_wrong | #FF2200 |
| gs_score | #FFEB00 |
| gs_timer_normal | #FFEB00 |
| gs_timer_warning | #FF2200 |
| gs_highlight | #0044FF |
| gs_badge | #FF2200 |
| gs_star | #FFEB00 |
| gs_nav_bar | #1E1E1E |
| gs_nav_selected | #FFEB00 |
| gs_nav_unselected | #666666 |
| gs_status_bar | #111111 |
| gs_glow | #0044FF |
| gs_tile_empty | #2E2E2E |
| gs_tile_2 | #3E3E3E |
| gs_tile_4 | #4E4E4E |
| gs_tile_8 | #0033CC |
| gs_tile_16 | #0044FF |
| gs_tile_32 | #3366FF |
| gs_tile_64 | #FFEB00 |
| gs_tile_128 | #FFCC00 |
| gs_tile_256 | #FF2200 |
| gs_tile_512 | #FF5500 |
| gs_tile_1024 | #00FF44 |
| gs_tile_2048 | #FFFFFF |
| gs_overlay | #CC111111 |
| gs_scrim | #99111111 |

---

## OCEAN BREEZE — 海洋清风

- **ID**: `ocean_breeze` · **Prefix**: `ob_` · **Mode**: Light
- **材质 / 场景**: 浅蓝天 + 白浪 + 深海蓝按钮
- **动画基调**: Smooth & Fluid
- **灵魂色分工**: primary=深海蓝 CTA · score=暖点缀可选 · highlight=天蓝
- **Toolbar 点缀**: 无
- **禁止**: 顶栏用深 surface 脏条

| Token | Value |
|-------|-------|
| ob_background | #E8F4FD |
| ob_surface | #FFFFFF |
| ob_surface_variant | #CAF0F8 |
| ob_surface_tint | #E0F7FF |
| ob_primary | #0077B6 |
| ob_primary_dark | #005A8E |
| ob_secondary | #00B4D8 |
| ob_tertiary | #0096C7 |
| ob_on_background | #03045E |
| ob_on_surface | #03045E |
| ob_on_surface_dim | #6B8FAE |
| ob_on_primary | #FFFFFF |
| ob_correct | #06D6A0 |
| ob_wrong | #EF476F |
| ob_score | #0096C7 |
| ob_timer_normal | #0077B6 |
| ob_timer_warning | #FF9E00 |
| ob_highlight | #48CAE4 |
| ob_badge | #0077B6 |
| ob_star | #0096C7 |
| ob_nav_bar | #FFFFFF |
| ob_nav_selected | #0077B6 |
| ob_nav_unselected | #B0C4D8 |
| ob_status_bar | #E8F4FD |
| ob_glow | n/a |
| ob_tile_empty | #CAF0F8 |
| ob_tile_2 | #ADE8F4 |
| ob_tile_4 | #90E0EF |
| ob_tile_8 | #48CAE4 |
| ob_tile_16 | #00B4D8 |
| ob_tile_32 | #0096C7 |
| ob_tile_64 | #0077B6 |
| ob_tile_128 | #023E8A |
| ob_tile_256 | #03045E |
| ob_tile_512 | #FFD166 |
| ob_tile_1024 | #EF476F |
| ob_tile_2048 | #06D6A0 |
| ob_overlay | #80ADE8F4 |
| ob_scrim | #500077B6 |

---

## FOREST ZEN — 森林竹影

- **ID**: `forest_zen` · **Prefix**: `fz_` · **Mode**: Light
- **材质 / 场景**: 竹绿 + 苔藓 + 米白纸感
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| fz_background | #F1F8E9 |
| fz_surface | #FFFFFF |
| fz_surface_variant | #DCEDC8 |
| fz_surface_tint | #E8F5E9 |
| fz_primary | #2E7D32 |
| fz_primary_dark | #1B5E20 |
| fz_secondary | #66BB6A |
| fz_tertiary | #A67C52 |
| fz_on_background | #1B3A1C |
| fz_on_surface | #1B3A1C |
| fz_on_surface_dim | #7A9E7B |
| fz_on_primary | #FFFFFF |
| fz_correct | #00C853 |
| fz_wrong | #D32F2F |
| fz_score | #F9A825 |
| fz_timer_normal | #2E7D32 |
| fz_timer_warning | #FF8F00 |
| fz_highlight | #81C784 |
| fz_badge | #2E7D32 |
| fz_star | #F9A825 |
| fz_nav_bar | #FFFFFF |
| fz_nav_selected | #2E7D32 |
| fz_nav_unselected | #9AB89B |
| fz_status_bar | #F1F8E9 |
| fz_glow | n/a |
| fz_tile_empty | #DCEDC8 |
| fz_tile_2 | #C5E1A5 |
| fz_tile_4 | #AED581 |
| fz_tile_8 | #9CCC65 |
| fz_tile_16 | #8BC34A |
| fz_tile_32 | #7CB342 |
| fz_tile_64 | #558B2F |
| fz_tile_128 | #33691E |
| fz_tile_256 | #2E7D32 |
| fz_tile_512 | #1B5E20 |
| fz_tile_1024 | #F9A825 |
| fz_tile_2048 | #E65100 |
| fz_overlay | #80DCEDC8 |
| fz_scrim | #502E7D32 |

---

## CANDY POP — 糖果缤纷

- **ID**: `candy_pop` · **Prefix**: `cp_` · **Mode**: Light
- **材质 / 场景**: 糖纸高饱和 + 厚圆角色块
- **动画基调**: Bouncy & Playful
- **灵魂色分工**: primary=糖粉 CTA · score=柠檬黄
- **Toolbar 点缀**: 动作图标可高饱和 1 个
- **禁止**: 彩虹渐变标题栏

| Token | Value |
|-------|-------|
| cp_background | #FFF0F3 |
| cp_surface | #FFFFFF |
| cp_surface_variant | #FFCCD5 |
| cp_surface_tint | #FFF5F7 |
| cp_primary | #FF4D6D |
| cp_primary_dark | #C9184A |
| cp_secondary | #A4DEF5 |
| cp_tertiary | #FFCB47 |
| cp_on_background | #590D22 |
| cp_on_surface | #590D22 |
| cp_on_surface_dim | #B06070 |
| cp_on_primary | #FFFFFF |
| cp_correct | #06D6A0 |
| cp_wrong | #EF476F |
| cp_score | #F4A261 |
| cp_timer_normal | #FF4D6D |
| cp_timer_warning | #EF476F |
| cp_highlight | #A4DEF5 |
| cp_badge | #FF4D6D |
| cp_star | #F4A261 |
| cp_nav_bar | #FFFFFF |
| cp_nav_selected | #FF4D6D |
| cp_nav_unselected | #D4A0B0 |
| cp_status_bar | #FFF0F3 |
| cp_glow | n/a |
| cp_tile_empty | #FFCCD5 |
| cp_tile_2 | #FFADC0 |
| cp_tile_4 | #FF8FA8 |
| cp_tile_8 | #FF6D8E |
| cp_tile_16 | #FF4D6D |
| cp_tile_32 | #E8365A |
| cp_tile_64 | #C9184A |
| cp_tile_128 | #A4DEF5 |
| cp_tile_256 | #74C2E1 |
| cp_tile_512 | #FFCB47 |
| cp_tile_1024 | #F4A261 |
| cp_tile_2048 | #06D6A0 |
| cp_overlay | #80FFCCD5 |
| cp_scrim | #50FF4D6D |

---

## SAKURA SPRING — 樱花春日

- **ID**: `sakura_spring` · **Prefix**: `sk_` · **Mode**: Light
- **材质 / 场景**: 淡粉花瓣 + 抹茶点缀 + 和纸白
- **动画基调**: Bouncy & Playful
- **灵魂色分工**: primary=樱粉 CTA · score=抹茶点缀 · highlight=淡粉
- **Toolbar 点缀**: 无
- **禁止**: Toolbar 大插画头图

| Token | Value |
|-------|-------|
| sk_background | #FFF5F7 |
| sk_surface | #FFFFFF |
| sk_surface_variant | #FFE4EA |
| sk_surface_tint | #FFF0F2 |
| sk_primary | #E8829A |
| sk_primary_dark | #C96380 |
| sk_secondary | #5C8A5F |
| sk_tertiary | #A67C52 |
| sk_on_background | #3D1C24 |
| sk_on_surface | #3D1C24 |
| sk_on_surface_dim | #B08898 |
| sk_on_primary | #FFFFFF |
| sk_correct | #5C8A5F |
| sk_wrong | #C96380 |
| sk_score | #A67C52 |
| sk_timer_normal | #E8829A |
| sk_timer_warning | #C96380 |
| sk_highlight | #FFB7C5 |
| sk_badge | #E8829A |
| sk_star | #A67C52 |
| sk_nav_bar | #FFFFFF |
| sk_nav_selected | #E8829A |
| sk_nav_unselected | #D4A8B0 |
| sk_status_bar | #FFF5F7 |
| sk_glow | n/a |
| sk_tile_empty | #FFE4EA |
| sk_tile_2 | #FFCCD6 |
| sk_tile_4 | #FFB7C5 |
| sk_tile_8 | #FF9BB0 |
| sk_tile_16 | #F07A95 |
| sk_tile_32 | #E8829A |
| sk_tile_64 | #C96380 |
| sk_tile_128 | #5C8A5F |
| sk_tile_256 | #4A7050 |
| sk_tile_512 | #A67C52 |
| sk_tile_1024 | #8B6344 |
| sk_tile_2048 | #3D1C24 |
| sk_overlay | #80FFB7C5 |
| sk_scrim | #50E8829A |

---

## DESERT GOLD — 沙漠金沙

- **ID**: `desert_gold` · **Prefix**: `dg_` · **Mode**: Light
- **材质 / 场景**: 沙土暖黄 + 陶土红 + 烈日高光
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| dg_background | #FDF3E7 |
| dg_surface | #FFFFFF |
| dg_surface_variant | #F0DFC0 |
| dg_surface_tint | #FAF0E0 |
| dg_primary | #A0522D |
| dg_primary_dark | #7A3B1E |
| dg_secondary | #C8A96E |
| dg_tertiary | #D4AF37 |
| dg_on_background | #2C1A0E |
| dg_on_surface | #2C1A0E |
| dg_on_surface_dim | #9E7050 |
| dg_on_primary | #FDF3E7 |
| dg_correct | #4CAF50 |
| dg_wrong | #D32F2F |
| dg_score | #D4AF37 |
| dg_timer_normal | #A0522D |
| dg_timer_warning | #D32F2F |
| dg_highlight | #D4AF37 |
| dg_badge | #A0522D |
| dg_star | #D4AF37 |
| dg_nav_bar | #FFFFFF |
| dg_nav_selected | #A0522D |
| dg_nav_unselected | #C0A080 |
| dg_status_bar | #FDF3E7 |
| dg_glow | n/a |
| dg_tile_empty | #F0DFC0 |
| dg_tile_2 | #E8D0A0 |
| dg_tile_4 | #DFC080 |
| dg_tile_8 | #D4AF37 |
| dg_tile_16 | #C8A96E |
| dg_tile_32 | #B8904A |
| dg_tile_64 | #A0522D |
| dg_tile_128 | #7A3B1E |
| dg_tile_256 | #5C2810 |
| dg_tile_512 | #3A1A08 |
| dg_tile_1024 | #D4AF37 |
| dg_tile_2048 | #FFFFFF |
| dg_overlay | #80F0DFC0 |
| dg_scrim | #50A0522D |

---

## ICE CRYSTAL — 冰晶雪域

- **ID**: `ice_crystal` · **Prefix**: `ic_` · **Mode**: Light
- **材质 / 场景**: 霜白玻璃 + 冰蓝描边
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| ic_background | #E8F4FD |
| ic_surface | #F0F8FF |
| ic_surface_variant | #D0E8F8 |
| ic_surface_tint | #E0F0FF |
| ic_primary | #1E88E5 |
| ic_primary_dark | #1565C0 |
| ic_secondary | #78C8E6 |
| ic_tertiary | #B0D8F0 |
| ic_on_background | #0D2137 |
| ic_on_surface | #0D2137 |
| ic_on_surface_dim | #7090B0 |
| ic_on_primary | #FFFFFF |
| ic_correct | #00BCD4 |
| ic_wrong | #F06292 |
| ic_score | #1E88E5 |
| ic_timer_normal | #1E88E5 |
| ic_timer_warning | #F06292 |
| ic_highlight | #78C8E6 |
| ic_badge | #1E88E5 |
| ic_star | #1E88E5 |
| ic_nav_bar | #F0F8FF |
| ic_nav_selected | #1E88E5 |
| ic_nav_unselected | #90B8D0 |
| ic_status_bar | #E8F4FD |
| ic_glow | n/a |
| ic_tile_empty | #D0E8F8 |
| ic_tile_2 | #B8DCF4 |
| ic_tile_4 | #9ED0EE |
| ic_tile_8 | #78C8E6 |
| ic_tile_16 | #4AB8DE |
| ic_tile_32 | #1E88E5 |
| ic_tile_64 | #1565C0 |
| ic_tile_128 | #0D47A1 |
| ic_tile_256 | #F06292 |
| ic_tile_512 | #E91E63 |
| ic_tile_1024 | #FFFFFF |
| ic_tile_2048 | #FFD700 |
| ic_overlay | #80D0E8F8 |
| ic_scrim | #501E88E5 |

---

## PASTEL DREAM — 柔彩色卡

- **ID**: `pastel_dream` · **Prefix**: `pd_` · **Mode**: Light
- **材质 / 场景**: 低饱和马卡龙色阶，无强对比
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| pd_background | #FAFAFA |
| pd_surface | #FFFFFF |
| pd_surface_variant | #F0EEF8 |
| pd_surface_tint | #F5F3FC |
| pd_primary | #9B72CF |
| pd_primary_dark | #7B52AF |
| pd_secondary | #72B7CF |
| pd_tertiary | #CF9B72 |
| pd_on_background | #2D1B5A |
| pd_on_surface | #2D1B5A |
| pd_on_surface_dim | #9080B0 |
| pd_on_primary | #FFFFFF |
| pd_correct | #B5EAD7 |
| pd_wrong | #FFABAB |
| pd_score | #FFD700 |
| pd_timer_normal | #9B72CF |
| pd_timer_warning | #FFABAB |
| pd_highlight | #C3B1E1 |
| pd_badge | #9B72CF |
| pd_star | #FFD700 |
| pd_nav_bar | #FFFFFF |
| pd_nav_selected | #9B72CF |
| pd_nav_unselected | #C0B0D8 |
| pd_status_bar | #FAFAFA |
| pd_glow | n/a |
| pd_tile_empty | #F0EEF8 |
| pd_tile_2 | #FFABAB |
| pd_tile_4 | #FFDAAB |
| pd_tile_8 | #FFFFAB |
| pd_tile_16 | #B5EAD7 |
| pd_tile_32 | #ABE4FF |
| pd_tile_64 | #C3B1E1 |
| pd_tile_128 | #FFB7C5 |
| pd_tile_256 | #9B72CF |
| pd_tile_512 | #72B7CF |
| pd_tile_1024 | #CF9B72 |
| pd_tile_2048 | #FFD700 |
| pd_overlay | #80C3B1E1 |
| pd_scrim | #509B72CF |

---

## CHRISTMAS — 圣诞节

- **ID**: `christmas` · **Prefix**: `xm_` · **Mode**: Light
- **材质 / 场景**: 圣诞红 + 松针绿 + 金箔
- **动画基调**: Festive & Sparkling
- **灵魂色分工**: primary=圣诞红 · secondary=松绿 · score=金
- **Toolbar 点缀**: 无或细金线
- **禁止**: 局内持续下雪挡字

| Token | Value |
|-------|-------|
| xm_background | #F5FFF5 |
| xm_surface | #FFFFFF |
| xm_surface_variant | #E8F5E8 |
| xm_surface_tint | #F0FFF0 |
| xm_primary | #CC0000 |
| xm_primary_dark | #990000 |
| xm_secondary | #165B33 |
| xm_tertiary | #D4AF37 |
| xm_on_background | #1A1A1A |
| xm_on_surface | #1A1A1A |
| xm_on_surface_dim | #708070 |
| xm_on_primary | #FFFFFF |
| xm_correct | #165B33 |
| xm_wrong | #CC0000 |
| xm_score | #D4AF37 |
| xm_timer_normal | #165B33 |
| xm_timer_warning | #CC0000 |
| xm_highlight | #D4AF37 |
| xm_badge | #CC0000 |
| xm_star | #D4AF37 |
| xm_nav_bar | #FFFFFF |
| xm_nav_selected | #CC0000 |
| xm_nav_unselected | #A0B0A0 |
| xm_status_bar | #F5FFF5 |
| xm_glow | n/a |
| xm_tile_empty | #E8F5E8 |
| xm_tile_2 | #D4EDD4 |
| xm_tile_4 | #B8DDB8 |
| xm_tile_8 | #8BC48B |
| xm_tile_16 | #5A9E5A |
| xm_tile_32 | #165B33 |
| xm_tile_64 | #CC0000 |
| xm_tile_128 | #990000 |
| xm_tile_256 | #D4AF37 |
| xm_tile_512 | #B8941F |
| xm_tile_1024 | #E8D080 |
| xm_tile_2048 | #FFFFFF |
| xm_overlay | #80E8F5E8 |
| xm_scrim | #80165B33 |

---

## PIXEL CLASSIC — 像素复古

- **ID**: `pixel_classic` · **Prefix**: `pc_` · **Mode**: Dark
- **材质 / 场景**: 8-bit 调色盘，硬像素边，无抗锯齿感
- **动画基调**: Instant Snap
- **灵魂色分工**: primary= thruster · score=高亮黄
- **Toolbar 点缀**: 0 圆角硬边
- **禁止**: 任何阴影与抗锯齿圆角

| Token | Value |
|-------|-------|
| pc_background | #1E1E1E |
| pc_surface | #2D2D2D |
| pc_surface_variant | #3D3D3D |
| pc_surface_tint | #353535 |
| pc_primary | #FF6B35 |
| pc_primary_dark | #D4562A |
| pc_secondary | #F7C59F |
| pc_tertiary | #4CC9F0 |
| pc_on_background | #FFFFFF |
| pc_on_surface | #FFFFFF |
| pc_on_surface_dim | #BDBDBD |
| pc_on_primary | #FFFFFF |
| pc_correct | #06D6A0 |
| pc_wrong | #FF4757 |
| pc_score | #FFBE0B |
| pc_timer_normal | #FFBE0B |
| pc_timer_warning | #FF6B35 |
| pc_highlight | #4CC9F0 |
| pc_badge | #FF6B35 |
| pc_star | #FFBE0B |
| pc_nav_bar | #2D2D2D |
| pc_nav_selected | #FF6B35 |
| pc_nav_unselected | #707070 |
| pc_status_bar | #1E1E1E |
| pc_glow | #4CC9F0 |
| pc_tile_empty | #2D2D2D |
| pc_tile_2 | #3D3D3D |
| pc_tile_4 | #4D4D4D |
| pc_tile_8 | #FF6B35 |
| pc_tile_16 | #D4562A |
| pc_tile_32 | #FFBE0B |
| pc_tile_64 | #D4A00A |
| pc_tile_128 | #4CC9F0 |
| pc_tile_256 | #3BACC8 |
| pc_tile_512 | #06D6A0 |
| pc_tile_1024 | #05B386 |
| pc_tile_2048 | #FFBE0B |
| pc_overlay | #CC1E1E1E |
| pc_scrim | #991E1E1E |
| pc_border | #FF6B35 |

---

## CARTOON FUN — 卡通趣味

- **ID**: `cartoon_fun` · **Prefix**: `cf_` · **Mode**: Light
- **材质 / 场景**: 粗黑描边 + 原色块，儿童动画感
- **动画基调**: Bouncy & Playful

| Token | Value |
|-------|-------|
| cf_background | #FFF9E6 |
| cf_surface | #FFFFFF |
| cf_surface_variant | #FFE8CC |
| cf_surface_tint | #FFF0D8 |
| cf_primary | #FF3333 |
| cf_primary_dark | #CC0000 |
| cf_secondary | #FFD700 |
| cf_tertiary | #33CC33 |
| cf_on_background | #1A1A1A |
| cf_on_surface | #1A1A1A |
| cf_on_surface_dim | #888888 |
| cf_on_primary | #FFFFFF |
| cf_correct | #33CC33 |
| cf_wrong | #FF3333 |
| cf_score | #FFD700 |
| cf_timer_normal | #FF9900 |
| cf_timer_warning | #FF3333 |
| cf_highlight | #FFD700 |
| cf_badge | #FF3333 |
| cf_star | #FFD700 |
| cf_nav_bar | #FFFFFF |
| cf_nav_selected | #FF3333 |
| cf_nav_unselected | #BBBBBB |
| cf_status_bar | #FFF9E6 |
| cf_glow | n/a |
| cf_tile_empty | #FFE8CC |
| cf_tile_2 | #FFD0A0 |
| cf_tile_4 | #FFB870 |
| cf_tile_8 | #FF9900 |
| cf_tile_16 | #FF6600 |
| cf_tile_32 | #FF3333 |
| cf_tile_64 | #CC0000 |
| cf_tile_128 | #33CC33 |
| cf_tile_256 | #009900 |
| cf_tile_512 | #FFD700 |
| cf_tile_1024 | #FF9900 |
| cf_tile_2048 | #1A1A1A |
| cf_overlay | #80FFE8CC |
| cf_scrim | #50FF3333 |

---

## MINIMALIST WHITE — 极简白

- **ID**: `minimalist_white` · **Prefix**: `mw_` · **Mode**: Light
- **材质 / 场景**: 大量留白 + 单一系统蓝强调
- **动画基调**: Gentle & Breathing
- **灵魂色分工**: primary=系统蓝唯一强调 · score=同主色或深灰
- **Toolbar 点缀**: 无
- **禁止**: 装饰纹理与多强调色

| Token | Value |
|-------|-------|
| mw_background | #F5F5F7 |
| mw_surface | #FFFFFF |
| mw_surface_variant | #F0F0F0 |
| mw_surface_tint | #FAFAFA |
| mw_primary | #0071E3 |
| mw_primary_dark | #0055B0 |
| mw_secondary | #6E6E73 |
| mw_tertiary | #1C1C1E |
| mw_on_background | #1C1C1E |
| mw_on_surface | #1C1C1E |
| mw_on_surface_dim | #8E8E93 |
| mw_on_primary | #FFFFFF |
| mw_correct | #30D158 |
| mw_wrong | #FF3B30 |
| mw_score | #0071E3 |
| mw_timer_normal | #0071E3 |
| mw_timer_warning | #FF3B30 |
| mw_highlight | #0071E3 |
| mw_badge | #0071E3 |
| mw_star | #0071E3 |
| mw_nav_bar | #FFFFFF |
| mw_nav_selected | #0071E3 |
| mw_nav_unselected | #C7C7CC |
| mw_status_bar | #F5F5F7 |
| mw_glow | n/a |
| mw_tile_empty | #F0F0F0 |
| mw_tile_2 | #E5E5EA |
| mw_tile_4 | #D1D1D6 |
| mw_tile_8 | #AEAEB2 |
| mw_tile_16 | #8E8E93 |
| mw_tile_32 | #636366 |
| mw_tile_64 | #48484A |
| mw_tile_128 | #0071E3 |
| mw_tile_256 | #0055B0 |
| mw_tile_512 | #30D158 |
| mw_tile_1024 | #FF9F0A |
| mw_tile_2048 | #FF3B30 |
| mw_overlay | #80F0F0F0 |
| mw_scrim | #500071E3 |

---

## PAPER CRAFT — 纸艺剪贴

- **ID**: `paper_craft` · **Prefix**: `ppc_` · **Mode**: Light
- **材质 / 场景**: 牛皮纸底 + 叠层阴影 + 手撕边缘感
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| ppc_background | #F0E6D0 |
| ppc_surface | #F8F0E0 |
| ppc_surface_variant | #E8D8B8 |
| ppc_surface_tint | #F0E8D8 |
| ppc_primary | #8B5E3C |
| ppc_primary_dark | #6B3E1C |
| ppc_secondary | #D4936A |
| ppc_tertiary | #5B8A4A |
| ppc_on_background | #2C1A0C |
| ppc_on_surface | #2C1A0C |
| ppc_on_surface_dim | #9E7850 |
| ppc_on_primary | #F8F0E0 |
| ppc_correct | #5B8A4A |
| ppc_wrong | #C04040 |
| ppc_score | #8B5E3C |
| ppc_timer_normal | #8B5E3C |
| ppc_timer_warning | #C04040 |
| ppc_highlight | #D4936A |
| ppc_badge | #8B5E3C |
| ppc_star | #8B5E3C |
| ppc_nav_bar | #F8F0E0 |
| ppc_nav_selected | #8B5E3C |
| ppc_nav_unselected | #C0A080 |
| ppc_status_bar | #F0E6D0 |
| ppc_glow | n/a |
| ppc_tile_empty | #E8D8B8 |
| ppc_tile_2 | #F0D8A0 |
| ppc_tile_4 | #E8C880 |
| ppc_tile_8 | #D4B060 |
| ppc_tile_16 | #C09040 |
| ppc_tile_32 | #D4936A |
| ppc_tile_64 | #8B5E3C |
| ppc_tile_128 | #5B8A4A |
| ppc_tile_256 | #3A6A2A |
| ppc_tile_512 | #4A6A9A |
| ppc_tile_1024 | #C04040 |
| ppc_tile_2048 | #2C1A0C |
| ppc_overlay | #80E8D8B8 |
| ppc_scrim | #508B5E3C |

---

## NEON SYNTHWAVE — 合成波

- **ID**: `neon_synthwave` · **Prefix**: `sw_` · **Mode**: Dark
- **材质 / 场景**: 80s 紫粉网格 + 地平线渐变
- **动画基调**: Fast & Electric
- **灵魂色分工**: primary=品红 · secondary=青 · score=黄
- **Toolbar 点缀**: 可选 1dp 品红底边
- **禁止**: 多条霓虹描边同时用在顶栏

| Token | Value |
|-------|-------|
| sw_background | #0A0010 |
| sw_surface | #14002A |
| sw_surface_variant | #1E0040 |
| sw_surface_tint | #250050 |
| sw_primary | #FF00FF |
| sw_primary_dark | #CC00CC |
| sw_secondary | #00FFFF |
| sw_tertiary | #FF6EC7 |
| sw_on_background | #FFE8FF |
| sw_on_surface | #FFE8FF |
| sw_on_surface_dim | #8040A0 |
| sw_on_primary | #FFFFFF |
| sw_correct | #00FFFF |
| sw_wrong | #FF0055 |
| sw_score | #FFFF00 |
| sw_timer_normal | #00FFFF |
| sw_timer_warning | #FF0055 |
| sw_highlight | #FF00FF |
| sw_badge | #FF00FF |
| sw_star | #FFFF00 |
| sw_nav_bar | #14002A |
| sw_nav_selected | #FF00FF |
| sw_nav_unselected | #604080 |
| sw_status_bar | #0A0010 |
| sw_glow | #FF00FF |
| sw_tile_empty | #1E0040 |
| sw_tile_2 | #2A0060 |
| sw_tile_4 | #40008A |
| sw_tile_8 | #6600BB |
| sw_tile_16 | #9900DD |
| sw_tile_32 | #CC00CC |
| sw_tile_64 | #FF00FF |
| sw_tile_128 | #00FFFF |
| sw_tile_256 | #00CCFF |
| sw_tile_512 | #FFFF00 |
| sw_tile_1024 | #FF6EC7 |
| sw_tile_2048 | #FFFFFF |
| sw_overlay | #CC0A0010 |
| sw_scrim | #990A0010 |

---

## NOIR CINEMA — 黑色电影

- **ID**: `noir_cinema` · **Prefix**: `nc_` · **Mode**: Dark
- **材质 / 场景**: 高反差黑白 + 一点血红
- **动画基调**: Smooth & Fluid
- **灵魂色分工**: primary=血红点缀 · 其余近灰度
- **Toolbar 点缀**: 1dp 极细浅线
- **禁止**: 彩色渐变与圆角大胶囊栏

| Token | Value |
|-------|-------|
| nc_background | #0A0A0A |
| nc_surface | #161616 |
| nc_surface_variant | #222222 |
| nc_surface_tint | #1C1212 |
| nc_primary | #E8E8E8 |
| nc_primary_dark | #BDBDBD |
| nc_secondary | #8A1C1C |
| nc_tertiary | #C4A35A |
| nc_on_background | #F2F2F2 |
| nc_on_surface | #F2F2F2 |
| nc_on_surface_dim | #7A7A7A |
| nc_on_primary | #0A0A0A |
| nc_correct | #6FBF73 |
| nc_wrong | #C62828 |
| nc_score | #C4A35A |
| nc_timer_normal | #E8E8E8 |
| nc_timer_warning | #C62828 |
| nc_highlight | #8A1C1C |
| nc_badge | #8A1C1C |
| nc_star | #C4A35A |
| nc_nav_bar | #161616 |
| nc_nav_selected | #E8E8E8 |
| nc_nav_unselected | #555555 |
| nc_status_bar | #0A0A0A |
| nc_glow | #8A1C1C |
| nc_tile_empty | #1C1C1C |
| nc_tile_2 | #2A2A2A |
| nc_tile_4 | #3A3A3A |
| nc_tile_8 | #4A4A4A |
| nc_tile_16 | #6A6A6A |
| nc_tile_32 | #8A1C1C |
| nc_tile_64 | #A02424 |
| nc_tile_128 | #C4A35A |
| nc_tile_256 | #D4B86A |
| nc_tile_512 | #E8E8E8 |
| nc_tile_1024 | #F5F5F5 |
| nc_tile_2048 | #FFFFFF |
| nc_overlay | #E50A0A0A |
| nc_scrim | #990A0A0A |

---

## CYBER MINT — 薄荷赛博

- **ID**: `cyber_mint` · **Prefix**: `cm_` · **Mode**: Dark
- **材质 / 场景**: 墨绿终端底 + 薄荷绿光标
- **动画基调**: Fast & Electric

| Token | Value |
|-------|-------|
| cm_background | #04120F |
| cm_surface | #0A1F1A |
| cm_surface_variant | #123028 |
| cm_surface_tint | #0F2A22 |
| cm_primary | #3DFFB5 |
| cm_primary_dark | #20C98A |
| cm_secondary | #1FA2A2 |
| cm_tertiary | #A8FFCE |
| cm_on_background | #D8FFF0 |
| cm_on_surface | #D8FFF0 |
| cm_on_surface_dim | #4A7A68 |
| cm_on_primary | #04120F |
| cm_correct | #3DFFB5 |
| cm_wrong | #FF4D6D |
| cm_score | #A8FFCE |
| cm_timer_normal | #3DFFB5 |
| cm_timer_warning | #FF8A3D |
| cm_highlight | #A8FFCE |
| cm_badge | #3DFFB5 |
| cm_star | #A8FFCE |
| cm_nav_bar | #0A1F1A |
| cm_nav_selected | #3DFFB5 |
| cm_nav_unselected | #3A5A50 |
| cm_status_bar | #04120F |
| cm_glow | #A8FFCE |
| cm_tile_empty | #123028 |
| cm_tile_2 | #163A30 |
| cm_tile_4 | #1A4A3C |
| cm_tile_8 | #1FA2A2 |
| cm_tile_16 | #20C98A |
| cm_tile_32 | #3DFFB5 |
| cm_tile_64 | #6AFFC8 |
| cm_tile_128 | #A8FFCE |
| cm_tile_256 | #D8FFF0 |
| cm_tile_512 | #FF8A3D |
| cm_tile_1024 | #FF4D6D |
| cm_tile_2048 | #FFFFFF |
| cm_overlay | #CC04120F |
| cm_scrim | #9904120F |

---

## EMBER COAL — 余烬炭火

- **ID**: `ember_coal` · **Prefix**: `ec_` · **Mode**: Dark
- **材质 / 场景**: 炭黑底 + 暗红余烬 + 琥珀火花
- **动画基调**: Dramatic & Intense

| Token | Value |
|-------|-------|
| ec_background | #100806 |
| ec_surface | #1C100C |
| ec_surface_variant | #2A1812 |
| ec_surface_tint | #301A12 |
| ec_primary | #E85D04 |
| ec_primary_dark | #B84503 |
| ec_secondary | #DC2F02 |
| ec_tertiary | #F48C06 |
| ec_on_background | #FFE8D6 |
| ec_on_surface | #FFE8D6 |
| ec_on_surface_dim | #8A5A40 |
| ec_on_primary | #100806 |
| ec_correct | #90BE6D |
| ec_wrong | #DC2F02 |
| ec_score | #F48C06 |
| ec_timer_normal | #F48C06 |
| ec_timer_warning | #DC2F02 |
| ec_highlight | #F48C06 |
| ec_badge | #E85D04 |
| ec_star | #F48C06 |
| ec_nav_bar | #1C100C |
| ec_nav_selected | #E85D04 |
| ec_nav_unselected | #5A3A2A |
| ec_status_bar | #100806 |
| ec_glow | #F48C06 |
| ec_tile_empty | #2A1812 |
| ec_tile_2 | #3A2018 |
| ec_tile_4 | #4A2818 |
| ec_tile_8 | #6A3410 |
| ec_tile_16 | #9A4010 |
| ec_tile_32 | #B84503 |
| ec_tile_64 | #E85D04 |
| ec_tile_128 | #F48C06 |
| ec_tile_256 | #FFB703 |
| ec_tile_512 | #DC2F02 |
| ec_tile_1024 | #FFD166 |
| ec_tile_2048 | #FFFFFF |
| ec_overlay | #CC100806 |
| ec_scrim | #99100806 |

---

## MATCHA CAFE — 抹茶咖啡馆

- **ID**: `matcha_cafe` · **Prefix**: `mc_` · **Mode**: Light
- **材质 / 场景**: 抹茶绿 + 燕麦奶色 + 木桌褐
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| mc_background | #F4F1E8 |
| mc_surface | #FFFCF5 |
| mc_surface_variant | #E4E8D4 |
| mc_surface_tint | #F0EDE2 |
| mc_primary | #5F7A45 |
| mc_primary_dark | #465C32 |
| mc_secondary | #C4A574 |
| mc_tertiary | #8B6F47 |
| mc_on_background | #2A2E22 |
| mc_on_surface | #2A2E22 |
| mc_on_surface_dim | #7A8070 |
| mc_on_primary | #FFFCF5 |
| mc_correct | #5F7A45 |
| mc_wrong | #B54A3A |
| mc_score | #C4A574 |
| mc_timer_normal | #5F7A45 |
| mc_timer_warning | #B54A3A |
| mc_highlight | #A8C47A |
| mc_badge | #5F7A45 |
| mc_star | #C4A574 |
| mc_nav_bar | #FFFCF5 |
| mc_nav_selected | #5F7A45 |
| mc_nav_unselected | #A8A898 |
| mc_status_bar | #F4F1E8 |
| mc_glow | n/a |
| mc_tile_empty | #E4E8D4 |
| mc_tile_2 | #D4DCC0 |
| mc_tile_4 | #C0CCAA |
| mc_tile_8 | #A8C47A |
| mc_tile_16 | #8BA85C |
| mc_tile_32 | #5F7A45 |
| mc_tile_64 | #465C32 |
| mc_tile_128 | #C4A574 |
| mc_tile_256 | #8B6F47 |
| mc_tile_512 | #B54A3A |
| mc_tile_1024 | #E8D5A3 |
| mc_tile_2048 | #2A2E22 |
| mc_overlay | #80E4E8D4 |
| mc_scrim | #505F7A45 |

---

## CORAL REEF — 珊瑚礁

- **ID**: `coral_reef` · **Prefix**: `cr_` · **Mode**: Light
- **材质 / 场景**: 珊瑚粉 + 潟湖蓝 + 浅沙底
- **动画基调**: Bouncy & Playful

| Token | Value |
|-------|-------|
| cr_background | #FFF5F2 |
| cr_surface | #FFFFFF |
| cr_surface_variant | #FFE0D6 |
| cr_surface_tint | #FFF0EC |
| cr_primary | #FF6F61 |
| cr_primary_dark | #E2554A |
| cr_secondary | #00A8A8 |
| cr_tertiary | #FFB4A2 |
| cr_on_background | #3A1F1A |
| cr_on_surface | #3A1F1A |
| cr_on_surface_dim | #A07870 |
| cr_on_primary | #FFFFFF |
| cr_correct | #2BB673 |
| cr_wrong | #E2554A |
| cr_score | #00A8A8 |
| cr_timer_normal | #00A8A8 |
| cr_timer_warning | #FF6F61 |
| cr_highlight | #FFB4A2 |
| cr_badge | #FF6F61 |
| cr_star | #00A8A8 |
| cr_nav_bar | #FFFFFF |
| cr_nav_selected | #FF6F61 |
| cr_nav_unselected | #C8A8A0 |
| cr_status_bar | #FFF5F2 |
| cr_glow | n/a |
| cr_tile_empty | #FFE0D6 |
| cr_tile_2 | #FFD0C4 |
| cr_tile_4 | #FFB4A2 |
| cr_tile_8 | #FF8F7A |
| cr_tile_16 | #FF6F61 |
| cr_tile_32 | #E2554A |
| cr_tile_64 | #00A8A8 |
| cr_tile_128 | #008F8F |
| cr_tile_256 | #2BB673 |
| cr_tile_512 | #FFD166 |
| cr_tile_1024 | #3A1F1A |
| cr_tile_2048 | #FFFFFF |
| cr_overlay | #80FFE0D6 |
| cr_scrim | #50FF6F61 |

---

## HONEY AMBER — 蜂蜜琥珀

- **ID**: `honey_amber` · **Prefix**: `ha_` · **Mode**: Light
- **材质 / 场景**: 蜂蜡金 + 奶油白 + 焦糖边
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| ha_background | #FFF8EB |
| ha_surface | #FFFCF5 |
| ha_surface_variant | #F5E6C8 |
| ha_surface_tint | #FFF4E0 |
| ha_primary | #D4A017 |
| ha_primary_dark | #A67C0A |
| ha_secondary | #E8B86D |
| ha_tertiary | #8B5A2B |
| ha_on_background | #3A2A12 |
| ha_on_surface | #3A2A12 |
| ha_on_surface_dim | #9A8050 |
| ha_on_primary | #3A2A12 |
| ha_correct | #6B9E3A |
| ha_wrong | #C4472A |
| ha_score | #D4A017 |
| ha_timer_normal | #D4A017 |
| ha_timer_warning | #C4472A |
| ha_highlight | #E8B86D |
| ha_badge | #D4A017 |
| ha_star | #D4A017 |
| ha_nav_bar | #FFFCF5 |
| ha_nav_selected | #D4A017 |
| ha_nav_unselected | #C0A878 |
| ha_status_bar | #FFF8EB |
| ha_glow | n/a |
| ha_tile_empty | #F5E6C8 |
| ha_tile_2 | #F0DCA8 |
| ha_tile_4 | #E8D08A |
| ha_tile_8 | #E8B86D |
| ha_tile_16 | #D4A017 |
| ha_tile_32 | #A67C0A |
| ha_tile_64 | #8B5A2B |
| ha_tile_128 | #6B9E3A |
| ha_tile_256 | #C4472A |
| ha_tile_512 | #F0C040 |
| ha_tile_1024 | #FFF8EB |
| ha_tile_2048 | #3A2A12 |
| ha_overlay | #80F5E6C8 |
| ha_scrim | #50D4A017 |

---

## SUNSET PLAZA — 落日广场

- **ID**: `sunset_plaza` · **Prefix**: `sz_` · **Mode**: Light
- **材质 / 场景**: 晚霞橘粉 + 石砖暖灰 + 余晖金
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| sz_background | #FFF1E8 |
| sz_surface | #FFFAF6 |
| sz_surface_variant | #FFD8C2 |
| sz_surface_tint | #FFE8DA |
| sz_primary | #E76F51 |
| sz_primary_dark | #C4553A |
| sz_secondary | #F4A261 |
| sz_tertiary | #2A9D8F |
| sz_on_background | #3A2218 |
| sz_on_surface | #3A2218 |
| sz_on_surface_dim | #A07A68 |
| sz_on_primary | #FFFFFF |
| sz_correct | #2A9D8F |
| sz_wrong | #C4553A |
| sz_score | #F4A261 |
| sz_timer_normal | #E76F51 |
| sz_timer_warning | #C4553A |
| sz_highlight | #F4A261 |
| sz_badge | #E76F51 |
| sz_star | #F4A261 |
| sz_nav_bar | #FFFAF6 |
| sz_nav_selected | #E76F51 |
| sz_nav_unselected | #C8A898 |
| sz_status_bar | #FFF1E8 |
| sz_glow | n/a |
| sz_tile_empty | #FFD8C2 |
| sz_tile_2 | #FFC8A8 |
| sz_tile_4 | #F4A261 |
| sz_tile_8 | #E98A4A |
| sz_tile_16 | #E76F51 |
| sz_tile_32 | #C4553A |
| sz_tile_64 | #2A9D8F |
| sz_tile_128 | #1F7A70 |
| sz_tile_256 | #E9C46A |
| sz_tile_512 | #264653 |
| sz_tile_1024 | #FFFFFF |
| sz_tile_2048 | #3A2218 |
| sz_overlay | #80FFD8C2 |
| sz_scrim | #50E76F51 |

---

## ARCADE CABINET — 街机柜

- **ID**: `arcade_cabinet` · **Prefix**: `ac_` · **Mode**: Dark
- **材质 / 场景**: CRT 磷光绿 + 机柜深紫 + thruster 橙按钮
- **动画基调**: Instant Snap
- **灵魂色分工**: primary=磷光绿 · CTA 可 thruster 橙
- **Toolbar 点缀**: 0 动画硬切
- **禁止**: Material 大圆角与长 fade

| Token | Value |
|-------|-------|
| ac_background | #0B0B14 |
| ac_surface | #161625 |
| ac_surface_variant | #222238 |
| ac_surface_tint | #1A1A2E |
| ac_primary | #39FF14 |
| ac_primary_dark | #28C40E |
| ac_secondary | #FF6B00 |
| ac_tertiary | #00E5FF |
| ac_on_background | #E8FFE8 |
| ac_on_surface | #E8FFE8 |
| ac_on_surface_dim | #5A7A5A |
| ac_on_primary | #0B0B14 |
| ac_correct | #39FF14 |
| ac_wrong | #FF2A55 |
| ac_score | #FF6B00 |
| ac_timer_normal | #39FF14 |
| ac_timer_warning | #FF6B00 |
| ac_highlight | #00E5FF |
| ac_badge | #FF6B00 |
| ac_star | #FF6B00 |
| ac_nav_bar | #161625 |
| ac_nav_selected | #39FF14 |
| ac_nav_unselected | #4A4A68 |
| ac_status_bar | #0B0B14 |
| ac_glow | #00E5FF |
| ac_tile_empty | #222238 |
| ac_tile_2 | #2A2A48 |
| ac_tile_4 | #323260 |
| ac_tile_8 | #28C40E |
| ac_tile_16 | #39FF14 |
| ac_tile_32 | #00E5FF |
| ac_tile_64 | #00B8CC |
| ac_tile_128 | #FF6B00 |
| ac_tile_256 | #FF8C33 |
| ac_tile_512 | #FF2A55 |
| ac_tile_1024 | #FFE600 |
| ac_tile_2048 | #FFFFFF |
| ac_overlay | #CC0B0B14 |
| ac_scrim | #990B0B14 |

---

## CYBERPUNK CITY — 赛博朋克都市

- **ID**: `cyberpunk_city` · **Prefix**: `cc_` · **Mode**: Dark
- **材质 / 场景**: 霓虹雨夜 + 全息青/品红
- **动画基调**: Fast & Electric

| Token | Value |
|-------|-------|
| cc_background | #0A0A12 |
| cc_surface | #12121F |
| cc_surface_variant | #1A1A2E |
| cc_surface_tint | #1E1535 |
| cc_primary | #00F0FF |
| cc_primary_dark | #00B8C4 |
| cc_secondary | #FF2A6D |
| cc_tertiary | #F9F002 |
| cc_on_background | #E8F4FF |
| cc_on_surface | #E8F4FF |
| cc_on_surface_dim | #5A6A80 |
| cc_on_primary | #0A0A12 |
| cc_correct | #00F0FF |
| cc_wrong | #FF2A6D |
| cc_score | #F9F002 |
| cc_timer_normal | #00F0FF |
| cc_timer_warning | #FF2A6D |
| cc_highlight | #F9F002 |
| cc_badge | #FF2A6D |
| cc_star | #F9F002 |
| cc_nav_bar | #12121F |
| cc_nav_selected | #00F0FF |
| cc_nav_unselected | #4A4A68 |
| cc_status_bar | #0A0A12 |
| cc_glow | #F9F002 |
| cc_tile_empty | #1A1A2E |
| cc_tile_2 | #222240 |
| cc_tile_4 | #2A2A55 |
| cc_tile_8 | #003A50 |
| cc_tile_16 | #007A90 |
| cc_tile_32 | #00B8C4 |
| cc_tile_64 | #00F0FF |
| cc_tile_128 | #FF2A6D |
| cc_tile_256 | #FF5A8D |
| cc_tile_512 | #F9F002 |
| cc_tile_1024 | #FFFFFF |
| cc_tile_2048 | #00F0FF |
| cc_overlay | #CC0A0A12 |
| cc_scrim | #990A0A12 |

---

## PIRATE COVE — 海盗海湾

- **ID**: `pirate_cove` · **Prefix**: `pi_` · **Mode**: Dark
- **材质 / 场景**: 橡木甲板 + 旧金 + 深海蓝
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| pi_background | #0C100E |
| pi_surface | #161C18 |
| pi_surface_variant | #1E2820 |
| pi_surface_tint | #243028 |
| pi_primary | #C9A227 |
| pi_primary_dark | #A07E1A |
| pi_secondary | #1B4F72 |
| pi_tertiary | #8B3A2A |
| pi_on_background | #F0E6C8 |
| pi_on_surface | #F0E6C8 |
| pi_on_surface_dim | #7A8068 |
| pi_on_primary | #0C100E |
| pi_correct | #4CAF50 |
| pi_wrong | #C62828 |
| pi_score | #C9A227 |
| pi_timer_normal | #C9A227 |
| pi_timer_warning | #C62828 |
| pi_highlight | #1B4F72 |
| pi_badge | #C9A227 |
| pi_star | #C9A227 |
| pi_nav_bar | #161C18 |
| pi_nav_selected | #C9A227 |
| pi_nav_unselected | #4A5548 |
| pi_status_bar | #0C100E |
| pi_glow | #1B4F72 |
| pi_tile_empty | #1E2820 |
| pi_tile_2 | #283228 |
| pi_tile_4 | #344038 |
| pi_tile_8 | #3A4A50 |
| pi_tile_16 | #1B4F72 |
| pi_tile_32 | #2A6A90 |
| pi_tile_64 | #8B3A2A |
| pi_tile_128 | #A07E1A |
| pi_tile_256 | #C9A227 |
| pi_tile_512 | #E0C040 |
| pi_tile_1024 | #F0E6C8 |
| pi_tile_2048 | #FFFFFF |
| pi_overlay | #CC0C100E |
| pi_scrim | #990C100E |

---

## ROYAL VELVET — 皇家天鹅绒

- **ID**: `royal_velvet` · **Prefix**: `rv_` · **Mode**: Dark
- **材质 / 场景**: 紫丝绒 + 金冠线
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| rv_background | #0F0818 |
| rv_surface | #1A1028 |
| rv_surface_variant | #241838 |
| rv_surface_tint | #2E1E48 |
| rv_primary | #C9A84C |
| rv_primary_dark | #A88A30 |
| rv_secondary | #6B2D8B |
| rv_tertiary | #9B4DB8 |
| rv_on_background | #F5E8C8 |
| rv_on_surface | #F5E8C8 |
| rv_on_surface_dim | #7A6888 |
| rv_on_primary | #0F0818 |
| rv_correct | #6BCB77 |
| rv_wrong | #E74C3C |
| rv_score | #C9A84C |
| rv_timer_normal | #C9A84C |
| rv_timer_warning | #E74C3C |
| rv_highlight | #9B4DB8 |
| rv_badge | #C9A84C |
| rv_star | #C9A84C |
| rv_nav_bar | #1A1028 |
| rv_nav_selected | #C9A84C |
| rv_nav_unselected | #504060 |
| rv_status_bar | #0F0818 |
| rv_glow | #9B4DB8 |
| rv_tile_empty | #241838 |
| rv_tile_2 | #2E1E48 |
| rv_tile_4 | #3A2860 |
| rv_tile_8 | #4A3080 |
| rv_tile_16 | #6B2D8B |
| rv_tile_32 | #9B4DB8 |
| rv_tile_64 | #A88A30 |
| rv_tile_128 | #C9A84C |
| rv_tile_256 | #D4BC68 |
| rv_tile_512 | #E8D080 |
| rv_tile_1024 | #F5E8C8 |
| rv_tile_2048 | #FFFFFF |
| rv_overlay | #CC0F0818 |
| rv_scrim | #990F0818 |

---

## INDUSTRIAL STEEL — 工业钢铁

- **ID**: `industrial_steel` · **Prefix**: `is_` · **Mode**: Dark
- **材质 / 场景**: 钢板灰 + 警示橙
- **动画基调**: Fast & Electric

| Token | Value |
|-------|-------|
| is_background | #121418 |
| is_surface | #1C1E24 |
| is_surface_variant | #282A32 |
| is_surface_tint | #30323A |
| is_primary | #FF6B00 |
| is_primary_dark | #CC5500 |
| is_secondary | #8A9199 |
| is_tertiary | #4FC3F7 |
| is_on_background | #E8EAED |
| is_on_surface | #E8EAED |
| is_on_surface_dim | #6A7078 |
| is_on_primary | #121418 |
| is_correct | #66BB6A |
| is_wrong | #EF5350 |
| is_score | #FF6B00 |
| is_timer_normal | #4FC3F7 |
| is_timer_warning | #EF5350 |
| is_highlight | #FF6B00 |
| is_badge | #FF6B00 |
| is_star | #FF6B00 |
| is_nav_bar | #1C1E24 |
| is_nav_selected | #FF6B00 |
| is_nav_unselected | #505860 |
| is_status_bar | #121418 |
| is_glow | #FF6B00 |
| is_tile_empty | #282A32 |
| is_tile_2 | #343640 |
| is_tile_4 | #404248 |
| is_tile_8 | #505860 |
| is_tile_16 | #606870 |
| is_tile_32 | #8A9199 |
| is_tile_64 | #CC5500 |
| is_tile_128 | #FF6B00 |
| is_tile_256 | #FF8A33 |
| is_tile_512 | #4FC3F7 |
| is_tile_1024 | #66BB6A |
| is_tile_2048 | #FFFFFF |
| is_overlay | #CC121418 |
| is_scrim | #99121418 |

---

## NIGHT MARKET — 夜市灯笼

- **ID**: `night_market` · **Prefix**: `nm_` · **Mode**: Dark
- **材质 / 场景**: 灯笼暖橙 + 夜市红
- **动画基调**: Festive & Sparkling

| Token | Value |
|-------|-------|
| nm_background | #0E0A08 |
| nm_surface | #1A1410 |
| nm_surface_variant | #261C16 |
| nm_surface_tint | #302418 |
| nm_primary | #FF6B35 |
| nm_primary_dark | #D4521A |
| nm_secondary | #FFD166 |
| nm_tertiary | #E63946 |
| nm_on_background | #FFE8D6 |
| nm_on_surface | #FFE8D6 |
| nm_on_surface_dim | #8A6A50 |
| nm_on_primary | #0E0A08 |
| nm_correct | #2A9D8F |
| nm_wrong | #E63946 |
| nm_score | #FFD166 |
| nm_timer_normal | #FFD166 |
| nm_timer_warning | #E63946 |
| nm_highlight | #FF6B35 |
| nm_badge | #E63946 |
| nm_star | #FFD166 |
| nm_nav_bar | #1A1410 |
| nm_nav_selected | #FF6B35 |
| nm_nav_unselected | #5A4030 |
| nm_status_bar | #0E0A08 |
| nm_glow | #FF6B35 |
| nm_tile_empty | #261C16 |
| nm_tile_2 | #322418 |
| nm_tile_4 | #3E3020 |
| nm_tile_8 | #5A4028 |
| nm_tile_16 | #D4521A |
| nm_tile_32 | #FF6B35 |
| nm_tile_64 | #FF8A55 |
| nm_tile_128 | #FFD166 |
| nm_tile_256 | #E63946 |
| nm_tile_512 | #2A9D8F |
| nm_tile_1024 | #FFE8D6 |
| nm_tile_2048 | #FFFFFF |
| nm_overlay | #CC0E0A08 |
| nm_scrim | #990E0A08 |

---

## MOONLIT GARDEN — 月下花园

- **ID**: `moonlit_garden` · **Prefix**: `mg_` · **Mode**: Dark
- **材质 / 场景**: 月下苔绿 + 淡紫月光
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| mg_background | #0A1210 |
| mg_surface | #121C18 |
| mg_surface_variant | #1A2820 |
| mg_surface_tint | #203028 |
| mg_primary | #7EC8A3 |
| mg_primary_dark | #5AA882 |
| mg_secondary | #C4B5E0 |
| mg_tertiary | #E8E0F0 |
| mg_on_background | #E0F0E8 |
| mg_on_surface | #E0F0E8 |
| mg_on_surface_dim | #5A7868 |
| mg_on_primary | #0A1210 |
| mg_correct | #7EC8A3 |
| mg_wrong | #E07080 |
| mg_score | #C4B5E0 |
| mg_timer_normal | #7EC8A3 |
| mg_timer_warning | #E07080 |
| mg_highlight | #C4B5E0 |
| mg_badge | #7EC8A3 |
| mg_star | #C4B5E0 |
| mg_nav_bar | #121C18 |
| mg_nav_selected | #7EC8A3 |
| mg_nav_unselected | #3A5048 |
| mg_status_bar | #0A1210 |
| mg_glow | #C4B5E0 |
| mg_tile_empty | #1A2820 |
| mg_tile_2 | #223028 |
| mg_tile_4 | #2A3A30 |
| mg_tile_8 | #3A5040 |
| mg_tile_16 | #5AA882 |
| mg_tile_32 | #7EC8A3 |
| mg_tile_64 | #A0D8B8 |
| mg_tile_128 | #C4B5E0 |
| mg_tile_256 | #D0C8E8 |
| mg_tile_512 | #E8E0F0 |
| mg_tile_1024 | #FFFFFF |
| mg_tile_2048 | #7EC8A3 |
| mg_overlay | #CC0A1210 |
| mg_scrim | #990A1210 |

---

## TROPICAL FRUIT — 热带水果

- **ID**: `tropical_fruit` · **Prefix**: `tf_` · **Mode**: Light
- **材质 / 场景**: 芒果橙 + 青柠 + 浅沙
- **动画基调**: Bouncy & Playful

| Token | Value |
|-------|-------|
| tf_background | #FFF8F0 |
| tf_surface | #FFFFFF |
| tf_surface_variant | #FFE8D0 |
| tf_surface_tint | #FFF0E0 |
| tf_primary | #FF6B35 |
| tf_primary_dark | #E05520 |
| tf_secondary | #00B4A0 |
| tf_tertiary | #FFD166 |
| tf_on_background | #3A2010 |
| tf_on_surface | #3A2010 |
| tf_on_surface_dim | #A07850 |
| tf_on_primary | #FFFFFF |
| tf_correct | #00B4A0 |
| tf_wrong | #E63946 |
| tf_score | #FFD166 |
| tf_timer_normal | #FF6B35 |
| tf_timer_warning | #E63946 |
| tf_highlight | #00B4A0 |
| tf_badge | #FF6B35 |
| tf_star | #FFD166 |
| tf_nav_bar | #FFFFFF |
| tf_nav_selected | #FF6B35 |
| tf_nav_unselected | #C0A080 |
| tf_status_bar | #FFF8F0 |
| tf_glow | n/a |
| tf_tile_empty | #FFE8D0 |
| tf_tile_2 | #FFD8B0 |
| tf_tile_4 | #FFC890 |
| tf_tile_8 | #FFB070 |
| tf_tile_16 | #FF6B35 |
| tf_tile_32 | #E05520 |
| tf_tile_64 | #00B4A0 |
| tf_tile_128 | #008F80 |
| tf_tile_256 | #FFD166 |
| tf_tile_512 | #E63946 |
| tf_tile_1024 | #3A2010 |
| tf_tile_2048 | #FFFFFF |
| tf_overlay | #80FFE8D0 |
| tf_scrim | #50FF6B35 |

---

## BUBBLE TEA — 奶茶时光

- **ID**: `bubble_tea` · **Prefix**: `bt_` · **Mode**: Light
- **材质 / 场景**: 奶茶褐 + 珍珠粉 + 燕麦底
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| bt_background | #FBF3EA |
| bt_surface | #FFFCF7 |
| bt_surface_variant | #F0E0D0 |
| bt_surface_tint | #F8ECE0 |
| bt_primary | #C47A4A |
| bt_primary_dark | #A06038 |
| bt_secondary | #8B5E4A |
| bt_tertiary | #E8B4B8 |
| bt_on_background | #3A2A20 |
| bt_on_surface | #3A2A20 |
| bt_on_surface_dim | #9A8070 |
| bt_on_primary | #FFFCF7 |
| bt_correct | #6B9E5A |
| bt_wrong | #C4473A |
| bt_score | #C47A4A |
| bt_timer_normal | #C47A4A |
| bt_timer_warning | #C4473A |
| bt_highlight | #E8B4B8 |
| bt_badge | #C47A4A |
| bt_star | #C47A4A |
| bt_nav_bar | #FFFCF7 |
| bt_nav_selected | #C47A4A |
| bt_nav_unselected | #C0A090 |
| bt_status_bar | #FBF3EA |
| bt_glow | n/a |
| bt_tile_empty | #F0E0D0 |
| bt_tile_2 | #E8D0B8 |
| bt_tile_4 | #D8B898 |
| bt_tile_8 | #C8A078 |
| bt_tile_16 | #C47A4A |
| bt_tile_32 | #A06038 |
| bt_tile_64 | #8B5E4A |
| bt_tile_128 | #E8B4B8 |
| bt_tile_256 | #D09098 |
| bt_tile_512 | #6B9E5A |
| bt_tile_1024 | #3A2A20 |
| bt_tile_2048 | #FFFFFF |
| bt_overlay | #80F0E0D0 |
| bt_scrim | #50C47A4A |

---

## FARM COTTAGE — 田园小屋

- **ID**: `farm_cottage` · **Prefix**: `fc_` · **Mode**: Light
- **材质 / 场景**: 田园绿 + 干草金 + 亚麻白
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| fc_background | #F5F0E6 |
| fc_surface | #FFFEF8 |
| fc_surface_variant | #E8E0D0 |
| fc_surface_tint | #F0EBE0 |
| fc_primary | #5B8C3E |
| fc_primary_dark | #456C2E |
| fc_secondary | #D4A05A |
| fc_tertiary | #8B5A2B |
| fc_on_background | #2A2A1A |
| fc_on_surface | #2A2A1A |
| fc_on_surface_dim | #7A7A60 |
| fc_on_primary | #FFFEF8 |
| fc_correct | #5B8C3E |
| fc_wrong | #C04030 |
| fc_score | #D4A05A |
| fc_timer_normal | #5B8C3E |
| fc_timer_warning | #C04030 |
| fc_highlight | #D4A05A |
| fc_badge | #5B8C3E |
| fc_star | #D4A05A |
| fc_nav_bar | #FFFEF8 |
| fc_nav_selected | #5B8C3E |
| fc_nav_unselected | #A0A088 |
| fc_status_bar | #F5F0E6 |
| fc_glow | n/a |
| fc_tile_empty | #E8E0D0 |
| fc_tile_2 | #D8D0B8 |
| fc_tile_4 | #C0C0A0 |
| fc_tile_8 | #A0B080 |
| fc_tile_16 | #80A060 |
| fc_tile_32 | #5B8C3E |
| fc_tile_64 | #456C2E |
| fc_tile_128 | #D4A05A |
| fc_tile_256 | #8B5A2B |
| fc_tile_512 | #C04030 |
| fc_tile_1024 | #2A2A1A |
| fc_tile_2048 | #FFFFFF |
| fc_overlay | #80E8E0D0 |
| fc_scrim | #505B8C3E |

---

## CLOUD SKY — 云朵天空

- **ID**: `cloud_sky` · **Prefix**: `cs_` · **Mode**: Light
- **材质 / 场景**: 积云白 + 天蓝 + 珊瑚点缀
- **动画基调**: Smooth & Floating

| Token | Value |
|-------|-------|
| cs_background | #E8F4FC |
| cs_surface | #FFFFFF |
| cs_surface_variant | #D0E8F8 |
| cs_surface_tint | #E0F0FA |
| cs_primary | #4A90D9 |
| cs_primary_dark | #3570B0 |
| cs_secondary | #7EC8E8 |
| cs_tertiary | #FFB4A0 |
| cs_on_background | #1A3050 |
| cs_on_surface | #1A3050 |
| cs_on_surface_dim | #7090B0 |
| cs_on_primary | #FFFFFF |
| cs_correct | #3DB87A |
| cs_wrong | #E85A5A |
| cs_score | #4A90D9 |
| cs_timer_normal | #4A90D9 |
| cs_timer_warning | #E85A5A |
| cs_highlight | #7EC8E8 |
| cs_badge | #4A90D9 |
| cs_star | #4A90D9 |
| cs_nav_bar | #FFFFFF |
| cs_nav_selected | #4A90D9 |
| cs_nav_unselected | #A0C0D8 |
| cs_status_bar | #E8F4FC |
| cs_glow | n/a |
| cs_tile_empty | #D0E8F8 |
| cs_tile_2 | #B8DCF0 |
| cs_tile_4 | #A0D0E8 |
| cs_tile_8 | #7EC8E8 |
| cs_tile_16 | #4A90D9 |
| cs_tile_32 | #3570B0 |
| cs_tile_64 | #FFB4A0 |
| cs_tile_128 | #FF9080 |
| cs_tile_256 | #3DB87A |
| cs_tile_512 | #E85A5A |
| cs_tile_1024 | #1A3050 |
| cs_tile_2048 | #FFFFFF |
| cs_overlay | #80D0E8F8 |
| cs_scrim | #504A90D9 |

---

## LAVENDER FIELDS — 薰衣草田

- **ID**: `lavender_fields` · **Prefix**: `lv_` · **Mode**: Light
- **材质 / 场景**: 薰衣草紫 + 干草黄
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| lv_background | #F5F0FA |
| lv_surface | #FFFEFF |
| lv_surface_variant | #E8DCF5 |
| lv_surface_tint | #F0E8F8 |
| lv_primary | #7B5EA7 |
| lv_primary_dark | #5E4580 |
| lv_secondary | #B8A0D0 |
| lv_tertiary | #E8C8A0 |
| lv_on_background | #2A1A3A |
| lv_on_surface | #2A1A3A |
| lv_on_surface_dim | #8070A0 |
| lv_on_primary | #FFFFFF |
| lv_correct | #6B9E5A |
| lv_wrong | #C05060 |
| lv_score | #7B5EA7 |
| lv_timer_normal | #7B5EA7 |
| lv_timer_warning | #C05060 |
| lv_highlight | #B8A0D0 |
| lv_badge | #7B5EA7 |
| lv_star | #7B5EA7 |
| lv_nav_bar | #FFFEFF |
| lv_nav_selected | #7B5EA7 |
| lv_nav_unselected | #B0A0C8 |
| lv_status_bar | #F5F0FA |
| lv_glow | n/a |
| lv_tile_empty | #E8DCF5 |
| lv_tile_2 | #D8C8E8 |
| lv_tile_4 | #C8B0E0 |
| lv_tile_8 | #B8A0D0 |
| lv_tile_16 | #9A80C0 |
| lv_tile_32 | #7B5EA7 |
| lv_tile_64 | #5E4580 |
| lv_tile_128 | #E8C8A0 |
| lv_tile_256 | #6B9E5A |
| lv_tile_512 | #C05060 |
| lv_tile_1024 | #2A1A3A |
| lv_tile_2048 | #FFFFFF |
| lv_overlay | #80E8DCF5 |
| lv_scrim | #507B5EA7 |

---

## CITRUS FRESH — 柑橘清新

- **ID**: `citrus_fresh` · **Prefix**: `ct_` · **Mode**: Light
- **材质 / 场景**: 橙橘 + 青绿点缀
- **动画基调**: Bouncy & Playful

| Token | Value |
|-------|-------|
| ct_background | #FFF9E8 |
| ct_surface | #FFFEF5 |
| ct_surface_variant | #FFF0C8 |
| ct_surface_tint | #FFF5D8 |
| ct_primary | #F4A261 |
| ct_primary_dark | #D4853A |
| ct_secondary | #2A9D8F |
| ct_tertiary | #E76F51 |
| ct_on_background | #3A2A10 |
| ct_on_surface | #3A2A10 |
| ct_on_surface_dim | #9A8050 |
| ct_on_primary | #FFFFFF |
| ct_correct | #2A9D8F |
| ct_wrong | #E76F51 |
| ct_score | #F4A261 |
| ct_timer_normal | #F4A261 |
| ct_timer_warning | #E76F51 |
| ct_highlight | #2A9D8F |
| ct_badge | #F4A261 |
| ct_star | #F4A261 |
| ct_nav_bar | #FFFEF5 |
| ct_nav_selected | #F4A261 |
| ct_nav_unselected | #C0A870 |
| ct_status_bar | #FFF9E8 |
| ct_glow | n/a |
| ct_tile_empty | #FFF0C8 |
| ct_tile_2 | #FFE8A8 |
| ct_tile_4 | #FFD888 |
| ct_tile_8 | #FFC868 |
| ct_tile_16 | #F4A261 |
| ct_tile_32 | #D4853A |
| ct_tile_64 | #2A9D8F |
| ct_tile_128 | #1F7A70 |
| ct_tile_256 | #E76F51 |
| ct_tile_512 | #E9C46A |
| ct_tile_1024 | #3A2A10 |
| ct_tile_2048 | #FFFFFF |
| ct_overlay | #80FFF0C8 |
| ct_scrim | #50F4A261 |

---

## CRYSTAL GEM — 水晶宝石

- **ID**: `crystal_gem` · **Prefix**: `cg_` · **Mode**: Dark
- **材质 / 场景**: 紫晶 + 冰青切面
- **动画基调**: Smooth & Floating

| Token | Value |
|-------|-------|
| cg_background | #0C0A18 |
| cg_surface | #14122A |
| cg_surface_variant | #1E1A3A |
| cg_surface_tint | #282250 |
| cg_primary | #B388FF |
| cg_primary_dark | #8A5CD6 |
| cg_secondary | #00E5FF |
| cg_tertiary | #FF80AB |
| cg_on_background | #E8E0FF |
| cg_on_surface | #E8E0FF |
| cg_on_surface_dim | #6860A0 |
| cg_on_primary | #0C0A18 |
| cg_correct | #69F0AE |
| cg_wrong | #FF5252 |
| cg_score | #00E5FF |
| cg_timer_normal | #B388FF |
| cg_timer_warning | #FF5252 |
| cg_highlight | #00E5FF |
| cg_badge | #B388FF |
| cg_star | #00E5FF |
| cg_nav_bar | #14122A |
| cg_nav_selected | #B388FF |
| cg_nav_unselected | #4A4570 |
| cg_status_bar | #0C0A18 |
| cg_glow | #00E5FF |
| cg_tile_empty | #1E1A3A |
| cg_tile_2 | #2A2450 |
| cg_tile_4 | #3A3070 |
| cg_tile_8 | #5A40A0 |
| cg_tile_16 | #8A5CD6 |
| cg_tile_32 | #B388FF |
| cg_tile_64 | #00E5FF |
| cg_tile_128 | #00B8CC |
| cg_tile_256 | #FF80AB |
| cg_tile_512 | #69F0AE |
| cg_tile_1024 | #FFFFFF |
| cg_tile_2048 | #B388FF |
| cg_overlay | #CC0C0A18 |
| cg_scrim | #990C0A18 |

---

## CLAY STOPMOTION — 粘土定格

- **ID**: `clay_stopmotion` · **Prefix**: `cl_` · **Mode**: Light
- **材质 / 场景**: 陶土橙 + 粘土绿 + 米色
- **动画基调**: Bouncy & Playful

| Token | Value |
|-------|-------|
| cl_background | #F5EDE3 |
| cl_surface | #FFF8F0 |
| cl_surface_variant | #E8D8C8 |
| cl_surface_tint | #F0E8DC |
| cl_primary | #E07A5F |
| cl_primary_dark | #C45A40 |
| cl_secondary | #81B29A |
| cl_tertiary | #F2CC8F |
| cl_on_background | #3D2C2E |
| cl_on_surface | #3D2C2E |
| cl_on_surface_dim | #9A8070 |
| cl_on_primary | #FFFFFF |
| cl_correct | #81B29A |
| cl_wrong | #E07A5F |
| cl_score | #F2CC8F |
| cl_timer_normal | #E07A5F |
| cl_timer_warning | #C45A40 |
| cl_highlight | #81B29A |
| cl_badge | #E07A5F |
| cl_star | #F2CC8F |
| cl_nav_bar | #FFF8F0 |
| cl_nav_selected | #E07A5F |
| cl_nav_unselected | #C0A890 |
| cl_status_bar | #F5EDE3 |
| cl_glow | n/a |
| cl_tile_empty | #E8D8C8 |
| cl_tile_2 | #D8C0A8 |
| cl_tile_4 | #C8A888 |
| cl_tile_8 | #E07A5F |
| cl_tile_16 | #C45A40 |
| cl_tile_32 | #81B29A |
| cl_tile_64 | #5A9078 |
| cl_tile_128 | #F2CC8F |
| cl_tile_256 | #D4A85A |
| cl_tile_512 | #3D2C2E |
| cl_tile_1024 | #FFFFFF |
| cl_tile_2048 | #E07A5F |
| cl_overlay | #80E8D8C8 |
| cl_scrim | #50E07A5F |

---

## BOARD GAME TABLE — 桌游木桌

- **ID**: `board_game_table` · **Prefix**: `bg_` · **Mode**: Light
- **材质 / 场景**: 胡桃木桌 + 深绿毡 + 黄铜
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| bg_background | #EDE4D4 |
| bg_surface | #F8F2E8 |
| bg_surface_variant | #DDD0B8 |
| bg_surface_tint | #E8DCC8 |
| bg_primary | #8B4513 |
| bg_primary_dark | #6B3410 |
| bg_secondary | #2E5A3C |
| bg_tertiary | #C4A35A |
| bg_on_background | #2C1A0C |
| bg_on_surface | #2C1A0C |
| bg_on_surface_dim | #8A7050 |
| bg_on_primary | #F8F2E8 |
| bg_correct | #2E5A3C |
| bg_wrong | #A02828 |
| bg_score | #C4A35A |
| bg_timer_normal | #8B4513 |
| bg_timer_warning | #A02828 |
| bg_highlight | #C4A35A |
| bg_badge | #8B4513 |
| bg_star | #C4A35A |
| bg_nav_bar | #F8F2E8 |
| bg_nav_selected | #8B4513 |
| bg_nav_unselected | #B0A080 |
| bg_status_bar | #EDE4D4 |
| bg_glow | n/a |
| bg_tile_empty | #DDD0B8 |
| bg_tile_2 | #CDB890 |
| bg_tile_4 | #BDA070 |
| bg_tile_8 | #A08050 |
| bg_tile_16 | #8B4513 |
| bg_tile_32 | #6B3410 |
| bg_tile_64 | #2E5A3C |
| bg_tile_128 | #1E4030 |
| bg_tile_256 | #C4A35A |
| bg_tile_512 | #A02828 |
| bg_tile_1024 | #2C1A0C |
| bg_tile_2048 | #FFFFFF |
| bg_overlay | #80DDD0B8 |
| bg_scrim | #508B4513 |

---

## COMIC HALFTONE — 漫画网点

- **ID**: `comic_halftone` · **Prefix**: `ch_` · **Mode**: Light
- **材质 / 场景**: 网点底 + 原色红/蓝/黄
- **动画基调**: Fast & Electric

| Token | Value |
|-------|-------|
| ch_background | #FFF8E7 |
| ch_surface | #FFFFFF |
| ch_surface_variant | #FFE8C0 |
| ch_surface_tint | #FFF0D0 |
| ch_primary | #FF1744 |
| ch_primary_dark | #D50000 |
| ch_secondary | #2979FF |
| ch_tertiary | #FFD600 |
| ch_on_background | #1A1A1A |
| ch_on_surface | #1A1A1A |
| ch_on_surface_dim | #707070 |
| ch_on_primary | #FFFFFF |
| ch_correct | #00C853 |
| ch_wrong | #FF1744 |
| ch_score | #FFD600 |
| ch_timer_normal | #2979FF |
| ch_timer_warning | #FF1744 |
| ch_highlight | #FFD600 |
| ch_badge | #FF1744 |
| ch_star | #FFD600 |
| ch_nav_bar | #FFFFFF |
| ch_nav_selected | #FF1744 |
| ch_nav_unselected | #B0B0B0 |
| ch_status_bar | #FFF8E7 |
| ch_glow | n/a |
| ch_tile_empty | #FFE8C0 |
| ch_tile_2 | #FFD890 |
| ch_tile_4 | #FFC060 |
| ch_tile_8 | #2979FF |
| ch_tile_16 | #1565C0 |
| ch_tile_32 | #FF1744 |
| ch_tile_64 | #D50000 |
| ch_tile_128 | #FFD600 |
| ch_tile_256 | #FFAB00 |
| ch_tile_512 | #00C853 |
| ch_tile_1024 | #1A1A1A |
| ch_tile_2048 | #FFFFFF |
| ch_overlay | #80FFE8C0 |
| ch_scrim | #50FF1744 |
| ch_border | #1A1A1A |

---

## INK WASH — 水墨丹青

- **ID**: `ink_wash` · **Prefix**: `iw_` · **Mode**: Light
- **材质 / 场景**: 宣纸白 + 浓墨 + 朱砂点
- **动画基调**: Gentle & Breathing

| Token | Value |
|-------|-------|
| iw_background | #F2EFE6 |
| iw_surface | #FAF8F2 |
| iw_surface_variant | #E0DCD0 |
| iw_surface_tint | #EBE8DC |
| iw_primary | #2C2C2C |
| iw_primary_dark | #1A1A1A |
| iw_secondary | #8B3A3A |
| iw_tertiary | #4A6A5A |
| iw_on_background | #1A1A1A |
| iw_on_surface | #1A1A1A |
| iw_on_surface_dim | #7A7870 |
| iw_on_primary | #FAF8F2 |
| iw_correct | #4A6A5A |
| iw_wrong | #8B3A3A |
| iw_score | #2C2C2C |
| iw_timer_normal | #2C2C2C |
| iw_timer_warning | #8B3A3A |
| iw_highlight | #4A6A5A |
| iw_badge | #8B3A3A |
| iw_star | #2C2C2C |
| iw_nav_bar | #FAF8F2 |
| iw_nav_selected | #2C2C2C |
| iw_nav_unselected | #A8A8A0 |
| iw_status_bar | #F2EFE6 |
| iw_glow | n/a |
| iw_tile_empty | #E0DCD0 |
| iw_tile_2 | #D0CCC0 |
| iw_tile_4 | #B8B4A8 |
| iw_tile_8 | #909088 |
| iw_tile_16 | #686860 |
| iw_tile_32 | #4A4A48 |
| iw_tile_64 | #2C2C2C |
| iw_tile_128 | #8B3A3A |
| iw_tile_256 | #4A6A5A |
| iw_tile_512 | #1A1A1A |
| iw_tile_1024 | #FAF8F2 |
| iw_tile_2048 | #2C2C2C |
| iw_overlay | #80E0DCD0 |
| iw_scrim | #502C2C2C |

---

## RETRO POSTER — 复古海报

- **ID**: `retro_poster` · **Prefix**: `rp_` · **Mode**: Light
- **材质 / 场景**: 复古纸黄 + 海报橙 + 海军蓝
- **动画基调**: Smooth & Fluid

| Token | Value |
|-------|-------|
| rp_background | #F5E6C8 |
| rp_surface | #FFF5E0 |
| rp_surface_variant | #E8D0A0 |
| rp_surface_tint | #F0E0B8 |
| rp_primary | #E85D04 |
| rp_primary_dark | #C44A00 |
| rp_secondary | #023E8A |
| rp_tertiary | #FFB703 |
| rp_on_background | #2A1A08 |
| rp_on_surface | #2A1A08 |
| rp_on_surface_dim | #8A7050 |
| rp_on_primary | #FFF5E0 |
| rp_correct | #2A9D8F |
| rp_wrong | #D00000 |
| rp_score | #FFB703 |
| rp_timer_normal | #E85D04 |
| rp_timer_warning | #D00000 |
| rp_highlight | #023E8A |
| rp_badge | #E85D04 |
| rp_star | #FFB703 |
| rp_nav_bar | #FFF5E0 |
| rp_nav_selected | #E85D04 |
| rp_nav_unselected | #B0A080 |
| rp_status_bar | #F5E6C8 |
| rp_glow | n/a |
| rp_tile_empty | #E8D0A0 |
| rp_tile_2 | #D8B880 |
| rp_tile_4 | #C8A060 |
| rp_tile_8 | #E85D04 |
| rp_tile_16 | #C44A00 |
| rp_tile_32 | #023E8A |
| rp_tile_64 | #0353A4 |
| rp_tile_128 | #FFB703 |
| rp_tile_256 | #D00000 |
| rp_tile_512 | #2A9D8F |
| rp_tile_1024 | #2A1A08 |
| rp_tile_2048 | #FFFFFF |
| rp_overlay | #80E8D0A0 |
| rp_scrim | #50E85D04 |

---

## JUNGLE ADVENTURE — 丛林探险

- **ID**: `jungle_adventure` · **Prefix**: `ja_` · **Mode**: Dark
- **材质 / 场景**: 密林绿 + 探险金
- **动画基调**: Dramatic & Intense

| Token | Value |
|-------|-------|
| ja_background | #0A140C |
| ja_surface | #121C14 |
| ja_surface_variant | #1A2A1C |
| ja_surface_tint | #223424 |
| ja_primary | #F4A261 |
| ja_primary_dark | #D4853A |
| ja_secondary | #2D6A4F |
| ja_tertiary | #95D5B2 |
| ja_on_background | #E8F0E0 |
| ja_on_surface | #E8F0E0 |
| ja_on_surface_dim | #5A7860 |
| ja_on_primary | #0A140C |
| ja_correct | #95D5B2 |
| ja_wrong | #E63946 |
| ja_score | #F4A261 |
| ja_timer_normal | #95D5B2 |
| ja_timer_warning | #E63946 |
| ja_highlight | #F4A261 |
| ja_badge | #F4A261 |
| ja_star | #F4A261 |
| ja_nav_bar | #121C14 |
| ja_nav_selected | #F4A261 |
| ja_nav_unselected | #3A5040 |
| ja_status_bar | #0A140C |
| ja_glow | #F4A261 |
| ja_tile_empty | #1A2A1C |
| ja_tile_2 | #223424 |
| ja_tile_4 | #2A4030 |
| ja_tile_8 | #2D6A4F |
| ja_tile_16 | #40916C |
| ja_tile_32 | #52B788 |
| ja_tile_64 | #95D5B2 |
| ja_tile_128 | #D4853A |
| ja_tile_256 | #F4A261 |
| ja_tile_512 | #E63946 |
| ja_tile_1024 | #E8F0E0 |
| ja_tile_2048 | #FFFFFF |
| ja_overlay | #CC0A140C |
| ja_scrim | #990A140C |

---

## SNOW FESTIVAL — 冰雪节庆

- **ID**: `snow_festival` · **Prefix**: `sf_` · **Mode**: Light
- **材质 / 场景**: 霜白 + 节日蓝 + 圣诞红点缀
- **动画基调**: Festive & Sparkling

| Token | Value |
|-------|-------|
| sf_background | #F0F7FC |
| sf_surface | #FFFFFF |
| sf_surface_variant | #D8EAF5 |
| sf_surface_tint | #E8F2F8 |
| sf_primary | #1E88E5 |
| sf_primary_dark | #1565C0 |
| sf_secondary | #E53935 |
| sf_tertiary | #FFD54F |
| sf_on_background | #0D2137 |
| sf_on_surface | #0D2137 |
| sf_on_surface_dim | #7090B0 |
| sf_on_primary | #FFFFFF |
| sf_correct | #43A047 |
| sf_wrong | #E53935 |
| sf_score | #FFD54F |
| sf_timer_normal | #1E88E5 |
| sf_timer_warning | #E53935 |
| sf_highlight | #FFD54F |
| sf_badge | #E53935 |
| sf_star | #FFD54F |
| sf_nav_bar | #FFFFFF |
| sf_nav_selected | #1E88E5 |
| sf_nav_unselected | #90B0C8 |
| sf_status_bar | #F0F7FC |
| sf_glow | n/a |
| sf_tile_empty | #D8EAF5 |
| sf_tile_2 | #C0DCF0 |
| sf_tile_4 | #A8D0E8 |
| sf_tile_8 | #78B8E0 |
| sf_tile_16 | #1E88E5 |
| sf_tile_32 | #1565C0 |
| sf_tile_64 | #E53935 |
| sf_tile_128 | #C62828 |
| sf_tile_256 | #FFD54F |
| sf_tile_512 | #43A047 |
| sf_tile_1024 | #0D2137 |
| sf_tile_2048 | #FFFFFF |
| sf_overlay | #80D8EAF5 |
| sf_scrim | #501E88E5 |

---
