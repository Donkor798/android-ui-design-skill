# Theme Full Specs — 30 个主题完整配色数值

数值以 `scripts/generate_theme.py` 为准。写作时用材质与场景描述，少用空泛情绪词。

---

## 🌑 NEON DARK — 霓虹暗黑
> 湿沥青路面 + 粉红/青灯管。高对比，适合夜间玩的 speed / quiz。

**灵魂色**：Electric Pink `#E94560` + Neon Cyan `#00FFCC`

```xml
<!-- res/values/colors_neon_dark.xml -->
<resources>
    <!-- 背景层次 -->
    <color name="nd_background">#0D0D0D</color>
    <color name="nd_surface">#1A1A2E</color>
    <color name="nd_surface_variant">#16213E</color>
    <color name="nd_surface_tint">#1F1035</color>

    <!-- 主色系 -->
    <color name="nd_primary">#E94560</color>
    <color name="nd_primary_dark">#C73652</color>
    <color name="nd_secondary">#0F3460</color>
    <color name="nd_tertiary">#533483</color>

    <!-- 文字 -->
    <color name="nd_on_background">#EAEAEA</color>
    <color name="nd_on_surface">#EAEAEA</color>
    <color name="nd_on_surface_dim">#757575</color>
    <color name="nd_on_primary">#FFFFFF</color>

    <!-- 功能色 -->
    <color name="nd_correct">#00E676</color>
    <color name="nd_wrong">#FF1744</color>
    <color name="nd_score">#FFD700</color>
    <color name="nd_timer_normal">#00FFCC</color>
    <color name="nd_timer_warning">#FF6D00</color>
    <color name="nd_highlight">#00FFCC</color>
    <color name="nd_badge">#E94560</color>

    <!-- 导航 -->
    <color name="nd_nav_bar">#1A1A2E</color>
    <color name="nd_nav_selected">#E94560</color>
    <color name="nd_nav_unselected">#555555</color>
    <color name="nd_status_bar">#0D0D0D</color>

    <!-- 2048 瓦片 -->
    <color name="nd_tile_empty">#16213E</color>
    <color name="nd_tile_2">#1A1A3E</color>
    <color name="nd_tile_4">#1E1E4A</color>
    <color name="nd_tile_8">#533483</color>
    <color name="nd_tile_16">#6A3D9A</color>
    <color name="nd_tile_32">#E94560</color>
    <color name="nd_tile_64">#C73652</color>
    <color name="nd_tile_128">#00FFCC</color>
    <color name="nd_tile_256">#00CCB0</color>
    <color name="nd_tile_512">#FFD700</color>
    <color name="nd_tile_1024">#FF6D00</color>
    <color name="nd_tile_2048">#FFFFFF</color>

    <!-- 遮罩 -->
    <color name="nd_overlay">#CC0D0D0D</color>
    <color name="nd_scrim">#990D0D0D</color>
</resources>
```

**字体**：`sans-serif-condensed`，Display/Headline 加 `shadowColor=#00FFCC, shadowRadius=8`

**形状**：按钮 `8dp`，卡片 `8dp`，瓦片 `4dp`，弹窗 `12dp`

**背景渐变**：
```xml
<!-- res/drawable/bg_gradient_neon_dark.xml -->
<shape android:shape="rectangle">
    <gradient android:startColor="#0D0D0D" android:endColor="#1A1A2E"
              android:angle="135" android:type="linear"/>
</shape>
```

**动画基调**：Fast & Electric — `150ms`，`FastOutLinearInInterpolator`，答对时 neon cyan 闪烁 3 次

---

## 🌌 SPACE GALAXY — 星际宇宙
> 深蓝真空底 + 星云紫。适合 puzzle / logic，背景可加稀疏星点。

**灵魂色**：Nebula Purple `#7B2FBE` + Starlight Blue `#4CC9F0`

```xml
<resources>
    <color name="sg_background">#06061A</color>
    <color name="sg_surface">#0D0D2B</color>
    <color name="sg_surface_variant">#151540</color>
    <color name="sg_surface_tint">#1A1050</color>

    <color name="sg_primary">#7B2FBE</color>
    <color name="sg_primary_dark">#5C1F9E</color>
    <color name="sg_secondary">#4CC9F0</color>
    <color name="sg_tertiary">#F72585</color>

    <color name="sg_on_background">#E8E8FF</color>
    <color name="sg_on_surface">#E8E8FF</color>
    <color name="sg_on_surface_dim">#6060A0</color>
    <color name="sg_on_primary">#FFFFFF</color>

    <color name="sg_correct">#4CC9F0</color>
    <color name="sg_wrong">#F72585</color>
    <color name="sg_score">#FFD60A</color>
    <color name="sg_timer_normal">#4CC9F0</color>
    <color name="sg_timer_warning">#F72585</color>
    <color name="sg_highlight">#4CC9F0</color>
    <color name="sg_badge">#F72585</color>

    <color name="sg_nav_bar">#0D0D2B</color>
    <color name="sg_nav_selected">#7B2FBE</color>
    <color name="sg_nav_unselected">#404070</color>
    <color name="sg_status_bar">#06061A</color>

    <color name="sg_tile_empty">#0D0D3A</color>
    <color name="sg_tile_2">#151560</color>
    <color name="sg_tile_4">#1E1E80</color>
    <color name="sg_tile_8">#4A1E8C</color>
    <color name="sg_tile_16">#7B2FBE</color>
    <color name="sg_tile_32">#9B4FDE</color>
    <color name="sg_tile_64">#4CC9F0</color>
    <color name="sg_tile_128">#3BB8DF</color>
    <color name="sg_tile_256">#F72585</color>
    <color name="sg_tile_512">#FFD60A</color>
    <color name="sg_tile_1024">#FFFFFF</color>
    <color name="sg_tile_2048">#FFD60A</color>

    <color name="sg_overlay">#CC06061A</color>
    <color name="sg_scrim">#9906061A</color>
</resources>
```

**背景**：星空渐变 + 粒子效果（推荐 Lottie `stars_bg.json` 或自定义 `StarfieldView`）

**字体**：`sans-serif-light`，标题用轻描边效果

**形状**：按钮 `24dp`（圆润太空舱感），卡片 `16dp`

**动画**：Smooth & Floating — `300ms`，`DecelerateInterpolator`，漂浮感进场

---

## 🌋 LAVA FIRE — 熔岩火焰
> 焦黑岩层 + 熔橙裂缝。适合竞速、高难度关卡反馈。

**灵魂色**：Molten Orange `#FF4500` + Ember Yellow `#FFB700`

```xml
<resources>
    <color name="lf_background">#0A0000</color>
    <color name="lf_surface">#1A0800</color>
    <color name="lf_surface_variant">#2D1000</color>
    <color name="lf_surface_tint">#3D1500</color>

    <color name="lf_primary">#FF4500</color>
    <color name="lf_primary_dark">#CC3700</color>
    <color name="lf_secondary">#FFB700</color>
    <color name="lf_tertiary">#FF0050</color>

    <color name="lf_on_background">#FFE0CC</color>
    <color name="lf_on_surface">#FFE0CC</color>
    <color name="lf_on_surface_dim">#8B5E40</color>
    <color name="lf_on_primary">#FFFFFF</color>

    <color name="lf_correct">#FFB700</color>
    <color name="lf_wrong">#FF0050</color>
    <color name="lf_score">#FFE566</color>
    <color name="lf_timer_normal">#FFB700</color>
    <color name="lf_timer_warning">#FF0050</color>
    <color name="lf_highlight">#FFB700</color>
    <color name="lf_badge">#FF4500</color>

    <color name="lf_nav_bar">#1A0800</color>
    <color name="lf_nav_selected">#FF4500</color>
    <color name="lf_nav_unselected">#5C3020</color>
    <color name="lf_status_bar">#0A0000</color>

    <color name="lf_tile_empty">#1A0800</color>
    <color name="lf_tile_2">#2D1000</color>
    <color name="lf_tile_4">#4A1800</color>
    <color name="lf_tile_8">#7A2800</color>
    <color name="lf_tile_16">#AA3800</color>
    <color name="lf_tile_32">#CC3700</color>
    <color name="lf_tile_64">#FF4500</color>
    <color name="lf_tile_128">#FF6B00</color>
    <color name="lf_tile_256">#FFB700</color>
    <color name="lf_tile_512">#FFD700</color>
    <color name="lf_tile_1024">#FFE566</color>
    <color name="lf_tile_2048">#FFFFFF</color>

    <color name="lf_overlay">#CC0A0000</color>
    <color name="lf_scrim">#990A0000</color>
</resources>
```

**背景**：底部橙红到顶部黑色渐变，建议加热浪扭曲动效

**形状**：按钮 `4dp`（硬朗感），卡片 `6dp`

**动画**：Intense & Fast — `100ms`，答错时屏幕红色闪烁振动

---

## ✨ MIDNIGHT LUXURY — 午夜奢华
> 哑光黑漆 + 香槟金细线。衬线标题，圆角极小，偏成人 trivia。

**灵魂色**：Pure Black `#0A0A0A` + Champagne Gold `#D4AF37`

```xml
<resources>
    <color name="ml_background">#0A0A0A</color>
    <color name="ml_surface">#141414</color>
    <color name="ml_surface_variant">#1E1E1E</color>
    <color name="ml_surface_tint">#1A1A0A</color>

    <color name="ml_primary">#D4AF37</color>
    <color name="ml_primary_dark">#B8941F</color>
    <color name="ml_secondary">#C0C0C0</color>
    <color name="ml_tertiary">#E8D5A3</color>

    <color name="ml_on_background">#F5F5F0</color>
    <color name="ml_on_surface">#F5F5F0</color>
    <color name="ml_on_surface_dim">#808080</color>
    <color name="ml_on_primary">#0A0A0A</color>

    <color name="ml_correct">#4CAF50</color>
    <color name="ml_wrong">#F44336</color>
    <color name="ml_score">#D4AF37</color>
    <color name="ml_timer_normal">#C0C0C0</color>
    <color name="ml_timer_warning">#FF6F00</color>
    <color name="ml_highlight">#D4AF37</color>
    <color name="ml_badge">#D4AF37</color>

    <color name="ml_nav_bar">#141414</color>
    <color name="ml_nav_selected">#D4AF37</color>
    <color name="ml_nav_unselected">#505050</color>
    <color name="ml_status_bar">#0A0A0A</color>

    <color name="ml_tile_empty">#1E1E1E</color>
    <color name="ml_tile_2">#2A2A2A</color>
    <color name="ml_tile_4">#363636</color>
    <color name="ml_tile_8">#4A3810</color>
    <color name="ml_tile_16">#6B5220</color>
    <color name="ml_tile_32">#8C6C2A</color>
    <color name="ml_tile_64">#B8941F</color>
    <color name="ml_tile_128">#D4AF37</color>
    <color name="ml_tile_256">#DFC060</color>
    <color name="ml_tile_512">#E8D080</color>
    <color name="ml_tile_1024">#F0E0A0</color>
    <color name="ml_tile_2048">#FFFFFF</color>

    <color name="ml_overlay">#E50A0A0A</color>
    <color name="ml_scrim">#990A0A0A</color>
</resources>
```

**字体**：`serif`（衬线字体），标题用 `letterSpacing=0.05`

**形状**：按钮 `2dp`（极小圆角，精致感）+ `strokeWidth=1dp, strokeColor=@color/ml_primary`

**背景**：纯黑 + 金色细线纹路（可用 `TileMode.REPEAT` 的斜纹 drawable）

---

## 🌊 OCEAN BREEZE — 海洋清风
> 浅蓝天 + 白浪 + 深海蓝按钮。大众向默认亮色之一。

**灵魂色**：Deep Ocean `#0077B6` + Sky Blue `#48CAE4`

```xml
<resources>
    <color name="ob_background">#E8F4FD</color>
    <color name="ob_surface">#FFFFFF</color>
    <color name="ob_surface_variant">#CAF0F8</color>
    <color name="ob_surface_tint">#E0F7FF</color>

    <color name="ob_primary">#0077B6</color>
    <color name="ob_primary_dark">#005A8E</color>
    <color name="ob_secondary">#00B4D8</color>
    <color name="ob_tertiary">#0096C7</color>

    <color name="ob_on_background">#03045E</color>
    <color name="ob_on_surface">#03045E</color>
    <color name="ob_on_surface_dim">#6B8FAE</color>
    <color name="ob_on_primary">#FFFFFF</color>

    <color name="ob_correct">#06D6A0</color>
    <color name="ob_wrong">#EF476F</color>
    <color name="ob_score">#0096C7</color>
    <color name="ob_timer_normal">#0077B6</color>
    <color name="ob_timer_warning">#FF9E00</color>
    <color name="ob_highlight">#48CAE4</color>
    <color name="ob_badge">#0077B6</color>

    <color name="ob_nav_bar">#FFFFFF</color>
    <color name="ob_nav_selected">#0077B6</color>
    <color name="ob_nav_unselected">#B0C4D8</color>
    <color name="ob_status_bar">#E8F4FD</color>

    <color name="ob_tile_empty">#CAF0F8</color>
    <color name="ob_tile_2">#ADE8F4</color>
    <color name="ob_tile_4">#90E0EF</color>
    <color name="ob_tile_8">#48CAE4</color>
    <color name="ob_tile_16">#00B4D8</color>
    <color name="ob_tile_32">#0096C7</color>
    <color name="ob_tile_64">#0077B6</color>
    <color name="ob_tile_128">#023E8A</color>
    <color name="ob_tile_256">#03045E</color>
    <color name="ob_tile_512">#FFD166</color>
    <color name="ob_tile_1024">#EF476F</color>
    <color name="ob_tile_2048">#06D6A0</color>

    <color name="ob_overlay">#80ADE8F4</color>
    <color name="ob_scrim">#500077B6</color>
</resources>
```

**字体**：`sans-serif`，轻盈感，不加特效

**形状**：按钮 `16dp`（圆润），卡片 `16dp`，弹窗 `24dp`

**背景**：浅蓝渐变，可加波浪形底部 drawable（`WaveView` 或 SVG path）

---

## 🌸 SAKURA SPRING — 樱花春日
> 淡粉花瓣 + 抹茶点缀 + 和纸白。季节活动或偏日式皮肤。

**灵魂色**：Sakura Pink `#FFB7C5` + Matcha Green `#5C8A5F`

```xml
<resources>
    <color name="sk_background">#FFF5F7</color>
    <color name="sk_surface">#FFFFFF</color>
    <color name="sk_surface_variant">#FFE4EA</color>
    <color name="sk_surface_tint">#FFF0F2</color>

    <color name="sk_primary">#E8829A</color>
    <color name="sk_primary_dark">#C96380</color>
    <color name="sk_secondary">#5C8A5F</color>
    <color name="sk_tertiary">#A67C52</color>

    <color name="sk_on_background">#3D1C24</color>
    <color name="sk_on_surface">#3D1C24</color>
    <color name="sk_on_surface_dim">#B08898</color>
    <color name="sk_on_primary">#FFFFFF</color>

    <color name="sk_correct">#5C8A5F</color>
    <color name="sk_wrong">#C96380</color>
    <color name="sk_score">#A67C52</color>
    <color name="sk_timer_normal">#E8829A</color>
    <color name="sk_timer_warning">#C96380</color>
    <color name="sk_highlight">#FFB7C5</color>
    <color name="sk_badge">#E8829A</color>

    <color name="sk_nav_bar">#FFFFFF</color>
    <color name="sk_nav_selected">#E8829A</color>
    <color name="sk_nav_unselected">#D4A8B0</color>
    <color name="sk_status_bar">#FFF5F7</color>

    <color name="sk_tile_empty">#FFE4EA</color>
    <color name="sk_tile_2">#FFCCD6</color>
    <color name="sk_tile_4">#FFB7C5</color>
    <color name="sk_tile_8">#FF9BB0</color>
    <color name="sk_tile_16">#F07A95</color>
    <color name="sk_tile_32">#E8829A</color>
    <color name="sk_tile_64">#C96380</color>
    <color name="sk_tile_128">#5C8A5F</color>
    <color name="sk_tile_256">#4A7050</color>
    <color name="sk_tile_512">#A67C52</color>
    <color name="sk_tile_1024">#8B6344</color>
    <color name="sk_tile_2048">#3D1C24</color>

    <color name="sk_overlay">#80FFB7C5</color>
    <color name="sk_scrim">#50E8829A</color>
</resources>
```

**字体**：`sans-serif-light`，小号字间距 `0.02`，标题用细体

**形状**：按钮 `20dp`，卡片 `16dp`，可用非对称圆角（花瓣感）

**动画**：Soft & Gentle — `400ms`，`AccelerateDecelerateInterpolator`，花瓣飘落粒子

---

## 🎃 HALLOWEEN — 万圣节
> 焦橙南瓜 + 紫雾 + 骨白。限时活动版专用。

**灵魂色**：Pumpkin `#FF6600` + Ghost White `#F0F0F0`

```xml
<resources>
    <color name="hw_background">#0D0800</color>
    <color name="hw_surface">#1A1000</color>
    <color name="hw_surface_variant">#2A1A00</color>
    <color name="hw_surface_tint">#301800</color>

    <color name="hw_primary">#FF6600</color>
    <color name="hw_primary_dark">#CC5200</color>
    <color name="hw_secondary">#8B00FF</color>
    <color name="hw_tertiary">#00CC66</color>

    <color name="hw_on_background">#F0E0C0</color>
    <color name="hw_on_surface">#F0E0C0</color>
    <color name="hw_on_surface_dim">#806040</color>
    <color name="hw_on_primary">#FFFFFF</color>

    <color name="hw_correct">#00CC66</color>
    <color name="hw_wrong">#FF1744</color>
    <color name="hw_score">#FF6600</color>
    <color name="hw_timer_normal">#FF6600</color>
    <color name="hw_timer_warning">#FF1744</color>
    <color name="hw_highlight">#8B00FF</color>
    <color name="hw_badge">#FF6600</color>

    <color name="hw_nav_bar">#1A1000</color>
    <color name="hw_nav_selected">#FF6600</color>
    <color name="hw_nav_unselected">#604020</color>
    <color name="hw_status_bar">#0D0800</color>

    <color name="hw_tile_empty">#1A1000</color>
    <color name="hw_tile_2">#2A1A00</color>
    <color name="hw_tile_4">#3D2800</color>
    <color name="hw_tile_8">#5C3A00</color>
    <color name="hw_tile_16">#7A4E00</color>
    <color name="hw_tile_32">#CC5200</color>
    <color name="hw_tile_64">#FF6600</color>
    <color name="hw_tile_128">#8B00FF</color>
    <color name="hw_tile_256">#6A00CC</color>
    <color name="hw_tile_512">#00CC66</color>
    <color name="hw_tile_1024">#FF1744</color>
    <color name="hw_tile_2048">#F0F0F0</color>

    <color name="hw_overlay">#CC0D0800</color>
    <color name="hw_scrim">#990D0800</color>
</resources>
```

**背景**：月亮+蜘蛛网图案（drawable SVG），渐变从深黑到暗橙

**字体**：`serif` 或自定义 Halloween 字体，适当歪斜

---

## 🎄 CHRISTMAS — 圣诞节
> 圣诞红 + 松针绿 + 金箔。节日运营皮肤。

**灵魂色**：Christmas Red `#CC0000` + Pine Green `#165B33`

```xml
<resources>
    <color name="xm_background">#F5FFF5</color>
    <color name="xm_surface">#FFFFFF</color>
    <color name="xm_surface_variant">#E8F5E8</color>
    <color name="xm_surface_tint">#F0FFF0</color>

    <color name="xm_primary">#CC0000</color>
    <color name="xm_primary_dark">#990000</color>
    <color name="xm_secondary">#165B33</color>
    <color name="xm_tertiary">#D4AF37</color>

    <color name="xm_on_background">#1A1A1A</color>
    <color name="xm_on_surface">#1A1A1A</color>
    <color name="xm_on_surface_dim">#708070</color>
    <color name="xm_on_primary">#FFFFFF</color>

    <color name="xm_correct">#165B33</color>
    <color name="xm_wrong">#CC0000</color>
    <color name="xm_score">#D4AF37</color>
    <color name="xm_timer_normal">#165B33</color>
    <color name="xm_timer_warning">#CC0000</color>
    <color name="xm_highlight">#D4AF37</color>
    <color name="xm_badge">#CC0000</color>

    <color name="xm_nav_bar">#FFFFFF</color>
    <color name="xm_nav_selected">#CC0000</color>
    <color name="xm_nav_unselected">#A0B0A0</color>
    <color name="xm_status_bar">#F5FFF5</color>

    <color name="xm_tile_empty">#E8F5E8</color>
    <color name="xm_tile_2">#D4EDD4</color>
    <color name="xm_tile_4">#B8DDB8</color>
    <color name="xm_tile_8">#8BC48B</color>
    <color name="xm_tile_16">#5A9E5A</color>
    <color name="xm_tile_32">#165B33</color>
    <color name="xm_tile_64">#CC0000</color>
    <color name="xm_tile_128">#990000</color>
    <color name="xm_tile_256">#D4AF37</color>
    <color name="xm_tile_512">#B8941F</color>
    <color name="xm_tile_1024">#E8D080</color>
    <color name="xm_tile_2048">#FFFFFF</color>

    <color name="xm_overlay">#80E8F5E8</color>
    <color name="xm_scrim">#80165B33</color>
</resources>
```

**背景**：白色+雪花粒子动效（Lottie `snowfall.json`）

---

## ❄️ ICE CRYSTAL — 冰晶雪域
> 霜白玻璃 + 冰蓝描边。卡片可半透明 + 细白边。

**灵魂色**：Ice Blue `#A8D8EA` + Frost White `#F0F8FF`

```xml
<resources>
    <color name="ic_background">#E8F4FD</color>
    <color name="ic_surface">#F0F8FF</color>
    <color name="ic_surface_variant">#D0E8F8</color>
    <color name="ic_surface_tint">#E0F0FF</color>

    <color name="ic_primary">#1E88E5</color>
    <color name="ic_primary_dark">#1565C0</color>
    <color name="ic_secondary">#78C8E6</color>
    <color name="ic_tertiary">#B0D8F0</color>

    <color name="ic_on_background">#0D2137</color>
    <color name="ic_on_surface">#0D2137</color>
    <color name="ic_on_surface_dim">#7090B0</color>
    <color name="ic_on_primary">#FFFFFF</color>

    <color name="ic_correct">#00BCD4</color>
    <color name="ic_wrong">#F06292</color>
    <color name="ic_score">#1E88E5</color>
    <color name="ic_timer_normal">#1E88E5</color>
    <color name="ic_timer_warning">#F06292</color>
    <color name="ic_highlight">#78C8E6</color>
    <color name="ic_badge">#1E88E5</color>

    <color name="ic_nav_bar">#F0F8FF</color>
    <color name="ic_nav_selected">#1E88E5</color>
    <color name="ic_nav_unselected">#90B8D0</color>
    <color name="ic_status_bar">#E8F4FD</color>

    <color name="ic_tile_empty">#D0E8F8</color>
    <color name="ic_tile_2">#B8DCF4</color>
    <color name="ic_tile_4">#9ED0EE</color>
    <color name="ic_tile_8">#78C8E6</color>
    <color name="ic_tile_16">#4AB8DE</color>
    <color name="ic_tile_32">#1E88E5</color>
    <color name="ic_tile_64">#1565C0</color>
    <color name="ic_tile_128">#0D47A1</color>
    <color name="ic_tile_256">#F06292</color>
    <color name="ic_tile_512">#E91E63</color>
    <color name="ic_tile_1024">#FFFFFF</color>
    <color name="ic_tile_2048">#FFD700</color>

    <color name="ic_overlay">#80D0E8F8</color>
    <color name="ic_scrim">#501E88E5</color>
</resources>
```

**卡片**：玻璃拟态效果（`alpha=0.7`，`blurRadius`，细描边 `strokeColor=#80FFFFFF`）

---

## 🎮 PIXEL CLASSIC — 像素复古
> 8-bit 调色盘，0 圆角，无过渡动画。2048 / arcade 友好。

**灵魂色**：CRT Orange `#FF6B35` + Phosphor Yellow `#FFBE0B`

```xml
<resources>
    <color name="pc_background">#1E1E1E</color>
    <color name="pc_surface">#2D2D2D</color>
    <color name="pc_surface_variant">#3D3D3D</color>
    <color name="pc_surface_tint">#353535</color>

    <color name="pc_primary">#FF6B35</color>
    <color name="pc_primary_dark">#D4562A</color>
    <color name="pc_secondary">#F7C59F</color>
    <color name="pc_tertiary">#4CC9F0</color>

    <color name="pc_on_background">#FFFFFF</color>
    <color name="pc_on_surface">#FFFFFF</color>
    <color name="pc_on_surface_dim">#BDBDBD</color>
    <color name="pc_on_primary">#FFFFFF</color>

    <color name="pc_correct">#06D6A0</color>
    <color name="pc_wrong">#FF4757</color>
    <color name="pc_score">#FFBE0B</color>
    <color name="pc_timer_normal">#FFBE0B</color>
    <color name="pc_timer_warning">#FF6B35</color>
    <color name="pc_highlight">#4CC9F0</color>
    <color name="pc_badge">#FF6B35</color>
    <color name="pc_border">#FF6B35</color>

    <color name="pc_nav_bar">#2D2D2D</color>
    <color name="pc_nav_selected">#FF6B35</color>
    <color name="pc_nav_unselected">#707070</color>
    <color name="pc_status_bar">#1E1E1E</color>

    <color name="pc_tile_empty">#2D2D2D</color>
    <color name="pc_tile_2">#3D3D3D</color>
    <color name="pc_tile_4">#4D4D4D</color>
    <color name="pc_tile_8">#FF6B35</color>
    <color name="pc_tile_16">#D4562A</color>
    <color name="pc_tile_32">#FFBE0B</color>
    <color name="pc_tile_64">#D4A00A</color>
    <color name="pc_tile_128">#4CC9F0</color>
    <color name="pc_tile_256">#3BACC8</color>
    <color name="pc_tile_512">#06D6A0</color>
    <color name="pc_tile_1024">#05B386</color>
    <color name="pc_tile_2048">#FFBE0B</color>

    <color name="pc_overlay">#CC1E1E1E</color>
    <color name="pc_scrim">#991E1E1E</color>
</resources>
```

**特殊设计规则**：
- 所有圆角必须 `0dp`
- 按钮使用 `strokeWidth=2dp`，`strokeColor=@color/pc_border`
- 字体：`monospace`，`textAllCaps=true`
- 禁止使用渐变，只用纯色
- 动画：无过渡，瞬间切换（duration=0ms 或用帧动画）

---

## 🌿 FOREST ZEN — 森林竹影
> 竹绿 + 苔藓 + 米白纸感。长时间阅读友好。

**灵魂色**：Deep Green `#2E7D32` + Bamboo `#A5D6A7`

```xml
<resources>
    <color name="fz_background">#F1F8E9</color>
    <color name="fz_surface">#FFFFFF</color>
    <color name="fz_surface_variant">#DCEDC8</color>
    <color name="fz_surface_tint">#E8F5E9</color>

    <color name="fz_primary">#2E7D32</color>
    <color name="fz_primary_dark">#1B5E20</color>
    <color name="fz_secondary">#66BB6A</color>
    <color name="fz_tertiary">#A67C52</color>

    <color name="fz_on_background">#1B3A1C</color>
    <color name="fz_on_surface">#1B3A1C</color>
    <color name="fz_on_surface_dim">#7A9E7B</color>
    <color name="fz_on_primary">#FFFFFF</color>

    <color name="fz_correct">#00C853</color>
    <color name="fz_wrong">#D32F2F</color>
    <color name="fz_score">#F9A825</color>
    <color name="fz_timer_normal">#2E7D32</color>
    <color name="fz_timer_warning">#FF8F00</color>
    <color name="fz_highlight">#81C784</color>
    <color name="fz_badge">#2E7D32</color>

    <color name="fz_nav_bar">#FFFFFF</color>
    <color name="fz_nav_selected">#2E7D32</color>
    <color name="fz_nav_unselected">#9AB89B</color>
    <color name="fz_status_bar">#F1F8E9</color>

    <color name="fz_tile_empty">#DCEDC8</color>
    <color name="fz_tile_2">#C5E1A5</color>
    <color name="fz_tile_4">#AED581</color>
    <color name="fz_tile_8">#9CCC65</color>
    <color name="fz_tile_16">#8BC34A</color>
    <color name="fz_tile_32">#7CB342</color>
    <color name="fz_tile_64">#558B2F</color>
    <color name="fz_tile_128">#33691E</color>
    <color name="fz_tile_256">#2E7D32</color>
    <color name="fz_tile_512">#1B5E20</color>
    <color name="fz_tile_1024">#F9A825</color>
    <color name="fz_tile_2048">#E65100</color>

    <color name="fz_overlay">#80DCEDC8</color>
    <color name="fz_scrim">#502E7D32</color>
</resources>
```

---

## 🍬 CANDY POP — 糖果缤纷
> 糖纸高饱和 + 厚圆角。Match-3 / bubble 首选。

**灵魂色**：Bubblegum `#FF4D6D` + Sky Candy `#A4DEF5`

```xml
<resources>
    <color name="cp_background">#FFF0F3</color>
    <color name="cp_surface">#FFFFFF</color>
    <color name="cp_surface_variant">#FFCCD5</color>
    <color name="cp_surface_tint">#FFF5F7</color>

    <color name="cp_primary">#FF4D6D</color>
    <color name="cp_primary_dark">#C9184A</color>
    <color name="cp_secondary">#A4DEF5</color>
    <color name="cp_tertiary">#FFCB47</color>

    <color name="cp_on_background">#590D22</color>
    <color name="cp_on_surface">#590D22</color>
    <color name="cp_on_surface_dim">#B06070</color>
    <color name="cp_on_primary">#FFFFFF</color>

    <color name="cp_correct">#06D6A0</color>
    <color name="cp_wrong">#EF476F</color>
    <color name="cp_score">#F4A261</color>
    <color name="cp_timer_normal">#FF4D6D</color>
    <color name="cp_timer_warning">#EF476F</color>
    <color name="cp_highlight">#A4DEF5</color>
    <color name="cp_badge">#FF4D6D</color>

    <color name="cp_nav_bar">#FFFFFF</color>
    <color name="cp_nav_selected">#FF4D6D</color>
    <color name="cp_nav_unselected">#D4A0B0</color>
    <color name="cp_status_bar">#FFF0F3</color>

    <color name="cp_tile_empty">#FFCCD5</color>
    <color name="cp_tile_2">#FFADC0</color>
    <color name="cp_tile_4">#FF8FA8</color>
    <color name="cp_tile_8">#FF6D8E</color>
    <color name="cp_tile_16">#FF4D6D</color>
    <color name="cp_tile_32">#E8365A</color>
    <color name="cp_tile_64">#C9184A</color>
    <color name="cp_tile_128">#A4DEF5</color>
    <color name="cp_tile_256">#74C2E1</color>
    <color name="cp_tile_512">#FFCB47</color>
    <color name="cp_tile_1024">#F4A261</color>
    <color name="cp_tile_2048">#06D6A0</color>

    <color name="cp_overlay">#80FFCCD5</color>
    <color name="cp_scrim">#50FF4D6D</color>
</resources>
```

---

## 🌅 DESERT GOLD — 沙漠金沙
> 沙土暖黄 + 陶土红。暖色 trivia / puzzle。

**灵魂色**：Sand `#C8A96E` + Terracotta `#A0522D`

```xml
<resources>
    <color name="dg_background">#FDF3E7</color>
    <color name="dg_surface">#FFFFFF</color>
    <color name="dg_surface_variant">#F0DFC0</color>
    <color name="dg_surface_tint">#FAF0E0</color>

    <color name="dg_primary">#A0522D</color>
    <color name="dg_primary_dark">#7A3B1E</color>
    <color name="dg_secondary">#C8A96E</color>
    <color name="dg_tertiary">#D4AF37</color>

    <color name="dg_on_background">#2C1A0E</color>
    <color name="dg_on_surface">#2C1A0E</color>
    <color name="dg_on_surface_dim">#9E7050</color>
    <color name="dg_on_primary">#FDF3E7</color>

    <color name="dg_correct">#4CAF50</color>
    <color name="dg_wrong">#D32F2F</color>
    <color name="dg_score">#D4AF37</color>
    <color name="dg_timer_normal">#A0522D</color>
    <color name="dg_timer_warning">#D32F2F</color>
    <color name="dg_highlight">#D4AF37</color>
    <color name="dg_badge">#A0522D</color>

    <color name="dg_nav_bar">#FFFFFF</color>
    <color name="dg_nav_selected">#A0522D</color>
    <color name="dg_nav_unselected">#C0A080</color>
    <color name="dg_status_bar">#FDF3E7</color>

    <color name="dg_tile_empty">#F0DFC0</color>
    <color name="dg_tile_2">#E8D0A0</color>
    <color name="dg_tile_4">#DFC080</color>
    <color name="dg_tile_8">#D4AF37</color>
    <color name="dg_tile_16">#C8A96E</color>
    <color name="dg_tile_32">#B8904A</color>
    <color name="dg_tile_64">#A0522D</color>
    <color name="dg_tile_128">#7A3B1E</color>
    <color name="dg_tile_256">#5C2810</color>
    <color name="dg_tile_512">#3A1A08</color>
    <color name="dg_tile_1024">#D4AF37</color>
    <color name="dg_tile_2048">#FFFFFF</color>

    <color name="dg_overlay">#80F0DFC0</color>
    <color name="dg_scrim">#50A0522D</color>
</resources>
```

---

## 🌈 PASTEL DREAM — 柔彩色卡
> 低饱和马卡龙色阶，无强对比。轻量 puzzle / kids。

**灵魂色**：Lavender `#C3B1E1` + Mint `#B5EAD7`

```xml
<resources>
    <color name="pd_background">#FAFAFA</color>
    <color name="pd_surface">#FFFFFF</color>
    <color name="pd_surface_variant">#F0EEF8</color>
    <color name="pd_surface_tint">#F5F3FC</color>

    <color name="pd_primary">#9B72CF</color>
    <color name="pd_primary_dark">#7B52AF</color>
    <color name="pd_secondary">#72B7CF</color>
    <color name="pd_tertiary">#CF9B72</color>

    <color name="pd_on_background">#2D1B5A</color>
    <color name="pd_on_surface">#2D1B5A</color>
    <color name="pd_on_surface_dim">#9080B0</color>
    <color name="pd_on_primary">#FFFFFF</color>

    <color name="pd_correct">#B5EAD7</color>
    <color name="pd_wrong">#FFABAB</color>
    <color name="pd_score">#FFD700</color>
    <color name="pd_timer_normal">#9B72CF</color>
    <color name="pd_timer_warning">#FFABAB</color>
    <color name="pd_highlight">#C3B1E1</color>
    <color name="pd_badge">#9B72CF</color>

    <color name="pd_nav_bar">#FFFFFF</color>
    <color name="pd_nav_selected">#9B72CF</color>
    <color name="pd_nav_unselected">#C0B0D8</color>
    <color name="pd_status_bar">#FAFAFA</color>

    <!-- 2048 瓦片用彩虹色阶 -->
    <color name="pd_tile_empty">#F0EEF8</color>
    <color name="pd_tile_2">#FFABAB</color>
    <color name="pd_tile_4">#FFDAAB</color>
    <color name="pd_tile_8">#FFFFAB</color>
    <color name="pd_tile_16">#B5EAD7</color>
    <color name="pd_tile_32">#ABE4FF</color>
    <color name="pd_tile_64">#C3B1E1</color>
    <color name="pd_tile_128">#FFB7C5</color>
    <color name="pd_tile_256">#9B72CF</color>
    <color name="pd_tile_512">#72B7CF</color>
    <color name="pd_tile_1024">#CF9B72</color>
    <color name="pd_tile_2048">#FFD700</color>

    <color name="pd_overlay">#80C3B1E1</color>
    <color name="pd_scrim">#509B72CF</color>
</resources>
```

---

## ⚡ NEON SYNTHWAVE — 合成波
> 1980年代复古未来，紫粉霓虹渐变，格子地板，无限延伸感。

**灵魂色**：Hot Magenta `#FF00FF` + Electric Cyan `#00FFFF`

```xml
<resources>
    <color name="sw_background">#0A0010</color>
    <color name="sw_surface">#14002A</color>
    <color name="sw_surface_variant">#1E0040</color>
    <color name="sw_surface_tint">#250050</color>

    <color name="sw_primary">#FF00FF</color>
    <color name="sw_primary_dark">#CC00CC</color>
    <color name="sw_secondary">#00FFFF</color>
    <color name="sw_tertiary">#FF6EC7</color>

    <color name="sw_on_background">#FFE8FF</color>
    <color name="sw_on_surface">#FFE8FF</color>
    <color name="sw_on_surface_dim">#8040A0</color>
    <color name="sw_on_primary">#FFFFFF</color>

    <color name="sw_correct">#00FFFF</color>
    <color name="sw_wrong">#FF0055</color>
    <color name="sw_score">#FFFF00</color>
    <color name="sw_timer_normal">#00FFFF</color>
    <color name="sw_timer_warning">#FF0055</color>
    <color name="sw_highlight">#FF00FF</color>
    <color name="sw_badge">#FF00FF</color>

    <color name="sw_nav_bar">#14002A</color>
    <color name="sw_nav_selected">#FF00FF</color>
    <color name="sw_nav_unselected">#604080</color>
    <color name="sw_status_bar">#0A0010</color>

    <color name="sw_tile_empty">#1E0040</color>
    <color name="sw_tile_2">#2A0060</color>
    <color name="sw_tile_4">#40008A</color>
    <color name="sw_tile_8">#6600BB</color>
    <color name="sw_tile_16">#9900DD</color>
    <color name="sw_tile_32">#CC00CC</color>
    <color name="sw_tile_64">#FF00FF</color>
    <color name="sw_tile_128">#00FFFF</color>
    <color name="sw_tile_256">#00CCFF</color>
    <color name="sw_tile_512">#FFFF00</color>
    <color name="sw_tile_1024">#FF6EC7</color>
    <color name="sw_tile_2048">#FFFFFF</color>

    <color name="sw_overlay">#CC0A0010</color>
    <color name="sw_scrim">#990A0010</color>
</resources>
```

**背景**：透视格子地板渐变（Synthwave 标志性视觉）
```xml
<!-- res/drawable/bg_synthwave_grid.xml — 用代码绘制更准确 -->
<!-- 推荐：自定义 SynthwaveGridView，绘制向远处收缩的紫色网格 -->
```

**字体**：`sans-serif-condensed`，标题大写，加 `shadowColor=#FF00FF, shadowRadius=12`

---

## 🌊 DEEP SEA — 深海秘境
> 深海4000米，压迫感与神秘感并存。发光的生物、幽暗的蓝黑。

**灵魂色**：Abyss Blue `#001B44` + Bioluminescent `#00CFFF`

```xml
<resources>
    <color name="ds_background">#000A1A</color>
    <color name="ds_surface">#001830</color>
    <color name="ds_surface_variant">#00243F</color>
    <color name="ds_surface_tint">#00305A</color>
    <color name="ds_primary">#00CFFF</color>
    <color name="ds_primary_dark">#009CC0</color>
    <color name="ds_secondary">#0055AA</color>
    <color name="ds_tertiary">#7FFFFF</color>
    <color name="ds_on_background">#B0E8FF</color>
    <color name="ds_on_surface">#B0E8FF</color>
    <color name="ds_on_surface_dim">#405070</color>
    <color name="ds_on_primary">#000A1A</color>
    <color name="ds_correct">#7FFFFF</color>
    <color name="ds_wrong">#FF4466</color>
    <color name="ds_score">#00CFFF</color>
    <color name="ds_timer_normal">#00CFFF</color>
    <color name="ds_timer_warning">#FF4466</color>
    <color name="ds_highlight">#7FFFFF</color>
    <color name="ds_badge">#00CFFF</color>
    <color name="ds_nav_bar">#001830</color>
    <color name="ds_nav_selected">#00CFFF</color>
    <color name="ds_nav_unselected">#204060</color>
    <color name="ds_status_bar">#000A1A</color>
    <color name="ds_tile_empty">#00243F</color>
    <color name="ds_tile_2">#003060</color>
    <color name="ds_tile_4">#004080</color>
    <color name="ds_tile_8">#0055AA</color>
    <color name="ds_tile_16">#0070CC</color>
    <color name="ds_tile_32">#0090EE</color>
    <color name="ds_tile_64">#00CFFF</color>
    <color name="ds_tile_128">#7FFFFF</color>
    <color name="ds_tile_256">#AAFFFF</color>
    <color name="ds_tile_512">#FF4466</color>
    <color name="ds_tile_1024">#FF8800</color>
    <color name="ds_tile_2048">#FFFFFF</color>
    <color name="ds_overlay">#CC000A1A</color>
    <color name="ds_scrim">#99000A1A</color>
</resources>
```

**背景**：深蓝渐变 + 粒子气泡上浮动效（Lottie `bubbles.json`）

**形状**：按钮 `12dp`，卡片 `12dp`（模拟水滴弧感）

**字体**：`sans-serif-light`，标题加 `shadowColor=#00CFFF, shadowRadius=10`（生物发光效果）

---

## 🌌 AURORA NIGHT — 极光暗夜
> 北极圈的奇异天空，绿紫渐变在黑暗中流动。梦幻、冷静、壮观。

**灵魂色**：Aurora Green `#00FF88` + Aurora Purple `#AA00FF`

```xml
<resources>
    <color name="an_background">#060812</color>
    <color name="an_surface">#0C1020</color>
    <color name="an_surface_variant">#131828</color>
    <color name="an_surface_tint">#1A2030</color>
    <color name="an_primary">#00FF88</color>
    <color name="an_primary_dark">#00CC66</color>
    <color name="an_secondary">#AA00FF</color>
    <color name="an_tertiary">#00CCFF</color>
    <color name="an_on_background">#D0FFE8</color>
    <color name="an_on_surface">#D0FFE8</color>
    <color name="an_on_surface_dim">#406050</color>
    <color name="an_on_primary">#060812</color>
    <color name="an_correct">#00FF88</color>
    <color name="an_wrong">#FF4488</color>
    <color name="an_score">#00CCFF</color>
    <color name="an_timer_normal">#00FF88</color>
    <color name="an_timer_warning">#FF4488</color>
    <color name="an_highlight">#AA00FF</color>
    <color name="an_badge">#00FF88</color>
    <color name="an_nav_bar">#0C1020</color>
    <color name="an_nav_selected">#00FF88</color>
    <color name="an_nav_unselected">#304040</color>
    <color name="an_status_bar">#060812</color>
    <color name="an_tile_empty">#131828</color>
    <color name="an_tile_2">#1A2535</color>
    <color name="an_tile_4">#003322</color>
    <color name="an_tile_8">#006644</color>
    <color name="an_tile_16">#00AA66</color>
    <color name="an_tile_32">#00FF88</color>
    <color name="an_tile_64">#00CCFF</color>
    <color name="an_tile_128">#AA00FF</color>
    <color name="an_tile_256">#CC44FF</color>
    <color name="an_tile_512">#FF4488</color>
    <color name="an_tile_1024">#FFCC00</color>
    <color name="an_tile_2048">#FFFFFF</color>
    <color name="an_overlay">#CC060812</color>
    <color name="an_scrim">#99060812</color>
</resources>
```

**背景**：黑色底 + 绿紫极光渐变层（`GradientDrawable` sweep型 或 SVG 动画）

**形状**：按钮 `20dp`（曲线感），卡片 `16dp`

---

## ⚙️ STEAMPUNK — 蒸汽朋克
> 维多利亚时代的机械美学，铜管、齿轮、蒸汽，棕铜暗金配色。

**灵魂色**：Copper `#B87333` + Brass `#D4A838`

```xml
<resources>
    <color name="sp_background">#1A1008</color>
    <color name="sp_surface">#2A1C0C</color>
    <color name="sp_surface_variant">#3A2810</color>
    <color name="sp_surface_tint">#4A3418</color>
    <color name="sp_primary">#B87333</color>
    <color name="sp_primary_dark">#8A5520</color>
    <color name="sp_secondary">#D4A838</color>
    <color name="sp_tertiary">#7A6040</color>
    <color name="sp_on_background">#F0D898</color>
    <color name="sp_on_surface">#F0D898</color>
    <color name="sp_on_surface_dim">#907050</color>
    <color name="sp_on_primary">#1A1008</color>
    <color name="sp_correct">#88CC44</color>
    <color name="sp_wrong">#CC4422</color>
    <color name="sp_score">#D4A838</color>
    <color name="sp_timer_normal">#B87333</color>
    <color name="sp_timer_warning">#CC4422</color>
    <color name="sp_highlight">#D4A838</color>
    <color name="sp_badge">#B87333</color>
    <color name="sp_nav_bar">#2A1C0C</color>
    <color name="sp_nav_selected">#B87333</color>
    <color name="sp_nav_unselected">#706040</color>
    <color name="sp_status_bar">#1A1008</color>
    <color name="sp_tile_empty">#2A1C0C</color>
    <color name="sp_tile_2">#3A2810</color>
    <color name="sp_tile_4">#5A3C18</color>
    <color name="sp_tile_8">#7A5020</color>
    <color name="sp_tile_16">#8A5520</color>
    <color name="sp_tile_32">#B87333</color>
    <color name="sp_tile_64">#C88840</color>
    <color name="sp_tile_128">#D4A838</color>
    <color name="sp_tile_256">#E0BC50</color>
    <color name="sp_tile_512">#EED068</color>
    <color name="sp_tile_1024">#F5E080</color>
    <color name="sp_tile_2048">#FFFACC</color>
    <color name="sp_overlay">#CC1A1008</color>
    <color name="sp_scrim">#991A1008</color>
</resources>
```

**字体**：`serif`，衬线字体强调维多利亚感，letterSpacing=0.05

**形状**：按钮 `4dp` + `strokeWidth=2dp, strokeColor=@color/sp_secondary`（铆钉边框感）

**背景**：深棕 + 齿轮纹路 TileMode repeat drawable

---

## 🎨 GRAFFITI STREET — 涂鸦街头
> 地铁站的喷漆墙，嘻哈街头文化，高饱和撞色，粗犷有力。

**灵魂色**：Spray Yellow `#FFEB00` + Electric Blue `#0044FF`

```xml
<resources>
    <color name="gs_background">#111111</color>
    <color name="gs_surface">#1E1E1E</color>
    <color name="gs_surface_variant">#2E2E2E</color>
    <color name="gs_surface_tint">#333333</color>
    <color name="gs_primary">#FFEB00</color>
    <color name="gs_primary_dark">#CCBB00</color>
    <color name="gs_secondary">#0044FF</color>
    <color name="gs_tertiary">#FF2200</color>
    <color name="gs_on_background">#FFFFFF</color>
    <color name="gs_on_surface">#FFFFFF</color>
    <color name="gs_on_surface_dim">#888888</color>
    <color name="gs_on_primary">#111111</color>
    <color name="gs_correct">#00FF44</color>
    <color name="gs_wrong">#FF2200</color>
    <color name="gs_score">#FFEB00</color>
    <color name="gs_timer_normal">#FFEB00</color>
    <color name="gs_timer_warning">#FF2200</color>
    <color name="gs_highlight">#0044FF</color>
    <color name="gs_badge">#FF2200</color>
    <color name="gs_nav_bar">#1E1E1E</color>
    <color name="gs_nav_selected">#FFEB00</color>
    <color name="gs_nav_unselected">#666666</color>
    <color name="gs_status_bar">#111111</color>
    <color name="gs_tile_empty">#2E2E2E</color>
    <color name="gs_tile_2">#3E3E3E</color>
    <color name="gs_tile_4">#4E4E4E</color>
    <color name="gs_tile_8">#0033CC</color>
    <color name="gs_tile_16">#0044FF</color>
    <color name="gs_tile_32">#3366FF</color>
    <color name="gs_tile_64">#FFEB00</color>
    <color name="gs_tile_128">#FFCC00</color>
    <color name="gs_tile_256">#FF2200</color>
    <color name="gs_tile_512">#FF5500</color>
    <color name="gs_tile_1024">#00FF44</color>
    <color name="gs_tile_2048">#FFFFFF</color>
    <color name="gs_overlay">#CC111111</color>
    <color name="gs_scrim">#99111111</color>
</resources>
```

**字体**：`sans-serif-black`，`textAllCaps=true`，大号 `letterSpacing=0.08`

**形状**：按钮 `0dp`（硬方块）+ `strokeWidth=3dp`（粗描边）

---

## 🎪 CARTOON FUN — 卡通趣味
> 粗黑描边 + 原色块。儿童向主皮肤。

**灵魂色**：Cartoon Red `#FF3333` + Sun Yellow `#FFD700`

```xml
<resources>
    <color name="cf_background">#FFF9E6</color>
    <color name="cf_surface">#FFFFFF</color>
    <color name="cf_surface_variant">#FFE8CC</color>
    <color name="cf_surface_tint">#FFF0D8</color>
    <color name="cf_primary">#FF3333</color>
    <color name="cf_primary_dark">#CC0000</color>
    <color name="cf_secondary">#FFD700</color>
    <color name="cf_tertiary">#33CC33</color>
    <color name="cf_on_background">#1A1A1A</color>
    <color name="cf_on_surface">#1A1A1A</color>
    <color name="cf_on_surface_dim">#888888</color>
    <color name="cf_on_primary">#FFFFFF</color>
    <color name="cf_correct">#33CC33</color>
    <color name="cf_wrong">#FF3333</color>
    <color name="cf_score">#FFD700</color>
    <color name="cf_timer_normal">#FF9900</color>
    <color name="cf_timer_warning">#FF3333</color>
    <color name="cf_highlight">#FFD700</color>
    <color name="cf_badge">#FF3333</color>
    <color name="cf_nav_bar">#FFFFFF</color>
    <color name="cf_nav_selected">#FF3333</color>
    <color name="cf_nav_unselected">#BBBBBB</color>
    <color name="cf_status_bar">#FFF9E6</color>
    <color name="cf_tile_empty">#FFE8CC</color>
    <color name="cf_tile_2">#FFD0A0</color>
    <color name="cf_tile_4">#FFB870</color>
    <color name="cf_tile_8">#FF9900</color>
    <color name="cf_tile_16">#FF6600</color>
    <color name="cf_tile_32">#FF3333</color>
    <color name="cf_tile_64">#CC0000</color>
    <color name="cf_tile_128">#33CC33</color>
    <color name="cf_tile_256">#009900</color>
    <color name="cf_tile_512">#FFD700</color>
    <color name="cf_tile_1024">#FF9900</color>
    <color name="cf_tile_2048">#1A1A1A</color>
    <color name="cf_overlay">#80FFE8CC</color>
    <color name="cf_scrim">#50FF3333</color>
</resources>
```

**形状**：按钮 `20dp` + `strokeWidth=3dp, strokeColor=#1A1A1A`（卡通粗描边）

**字体**：`sans-serif-medium`，`textAllCaps=false`，字体大一号（比标准大 2sp）

---

## ⬜ MINIMALIST WHITE — 极简白
> 大量留白 + 单一系统蓝强调。适合 quiz / 设置页重内容。

**灵魂色**：Pure White `#FFFFFF` + Accent Black `#1C1C1E`

```xml
<resources>
    <color name="mw_background">#F5F5F7</color>
    <color name="mw_surface">#FFFFFF</color>
    <color name="mw_surface_variant">#F0F0F0</color>
    <color name="mw_surface_tint">#FAFAFA</color>
    <color name="mw_primary">#0071E3</color>
    <color name="mw_primary_dark">#0055B0</color>
    <color name="mw_secondary">#6E6E73</color>
    <color name="mw_tertiary">#1C1C1E</color>
    <color name="mw_on_background">#1C1C1E</color>
    <color name="mw_on_surface">#1C1C1E</color>
    <color name="mw_on_surface_dim">#8E8E93</color>
    <color name="mw_on_primary">#FFFFFF</color>
    <color name="mw_correct">#30D158</color>
    <color name="mw_wrong">#FF3B30</color>
    <color name="mw_score">#0071E3</color>
    <color name="mw_timer_normal">#0071E3</color>
    <color name="mw_timer_warning">#FF3B30</color>
    <color name="mw_highlight">#0071E3</color>
    <color name="mw_badge">#0071E3</color>
    <color name="mw_nav_bar">#FFFFFF</color>
    <color name="mw_nav_selected">#0071E3</color>
    <color name="mw_nav_unselected">#C7C7CC</color>
    <color name="mw_status_bar">#F5F5F7</color>
    <color name="mw_tile_empty">#F0F0F0</color>
    <color name="mw_tile_2">#E5E5EA</color>
    <color name="mw_tile_4">#D1D1D6</color>
    <color name="mw_tile_8">#AEAEB2</color>
    <color name="mw_tile_16">#8E8E93</color>
    <color name="mw_tile_32">#636366</color>
    <color name="mw_tile_64">#48484A</color>
    <color name="mw_tile_128">#0071E3</color>
    <color name="mw_tile_256">#0055B0</color>
    <color name="mw_tile_512">#30D158</color>
    <color name="mw_tile_1024">#FF9F0A</color>
    <color name="mw_tile_2048">#FF3B30</color>
    <color name="mw_overlay">#80F0F0F0</color>
    <color name="mw_scrim">#500071E3</color>
</resources>
```

**形状**：按钮 `10dp`（苹果标准），卡片 `12dp`，`strokeWidth=0`（无描边）

**字体**：`sans-serif` (SF Pro 替代)，`fontWeight=400`/`600`，严格遵守 Material3 type scale

---

## 📄 PAPER CRAFT — 纸艺剪贴
> 牛皮纸底 + 叠层阴影。word / crossword 友好。

**灵魂色**：Cream Paper `#F5E6C8` + Craft Brown `#8B5E3C`

```xml
<resources>
    <color name="ppc_background">#F0E6D0</color>
    <color name="ppc_surface">#F8F0E0</color>
    <color name="ppc_surface_variant">#E8D8B8</color>
    <color name="ppc_surface_tint">#F0E8D8</color>
    <color name="ppc_primary">#8B5E3C</color>
    <color name="ppc_primary_dark">#6B3E1C</color>
    <color name="ppc_secondary">#D4936A</color>
    <color name="ppc_tertiary">#5B8A4A</color>
    <color name="ppc_on_background">#2C1A0C</color>
    <color name="ppc_on_surface">#2C1A0C</color>
    <color name="ppc_on_surface_dim">#9E7850</color>
    <color name="ppc_on_primary">#F8F0E0</color>
    <color name="ppc_correct">#5B8A4A</color>
    <color name="ppc_wrong">#C04040</color>
    <color name="ppc_score">#8B5E3C</color>
    <color name="ppc_timer_normal">#8B5E3C</color>
    <color name="ppc_timer_warning">#C04040</color>
    <color name="ppc_highlight">#D4936A</color>
    <color name="ppc_badge">#8B5E3C</color>
    <color name="ppc_nav_bar">#F8F0E0</color>
    <color name="ppc_nav_selected">#8B5E3C</color>
    <color name="ppc_nav_unselected">#C0A080</color>
    <color name="ppc_status_bar">#F0E6D0</color>
    <color name="ppc_tile_empty">#E8D8B8</color>
    <color name="ppc_tile_2">#F0D8A0</color>
    <color name="ppc_tile_4">#E8C880</color>
    <color name="ppc_tile_8">#D4B060</color>
    <color name="ppc_tile_16">#C09040</color>
    <color name="ppc_tile_32">#D4936A</color>
    <color name="ppc_tile_64">#8B5E3C</color>
    <color name="ppc_tile_128">#5B8A4A</color>
    <color name="ppc_tile_256">#3A6A2A</color>
    <color name="ppc_tile_512">#4A6A9A</color>
    <color name="ppc_tile_1024">#C04040</color>
    <color name="ppc_tile_2048">#2C1A0C</color>
    <color name="ppc_overlay">#80E8D8B8</color>
    <color name="ppc_scrim">#508B5E3C</color>
</resources>
```

**特殊设计**：卡片用 `cardElevation=8dp` + `shadowColor=#8B5E3C`（纸张叠放投影）

**形状**：非对称圆角建议（用 `ShapeAppearance` 设置不同角），模拟手剪效果

---

## 🎞 NOIR CINEMA — 黑色电影
> 高反差黑白银幕，只留一点血红做强调。适合 trivia、推理 quiz。

**灵魂色**：Bone White `#E8E8E8` + Blood Accent `#8A1C1C`

```xml
<resources>
    <color name="nc_background">#0A0A0A</color>
    <color name="nc_surface">#161616</color>
    <color name="nc_surface_variant">#222222</color>
    <color name="nc_surface_tint">#1C1212</color>
    <color name="nc_primary">#E8E8E8</color>
    <color name="nc_primary_dark">#BDBDBD</color>
    <color name="nc_secondary">#8A1C1C</color>
    <color name="nc_tertiary">#C4A35A</color>
    <color name="nc_on_background">#F2F2F2</color>
    <color name="nc_on_surface">#F2F2F2</color>
    <color name="nc_on_surface_dim">#7A7A7A</color>
    <color name="nc_on_primary">#0A0A0A</color>
    <color name="nc_correct">#6FBF73</color>
    <color name="nc_wrong">#C62828</color>
    <color name="nc_score">#C4A35A</color>
    <color name="nc_timer_normal">#E8E8E8</color>
    <color name="nc_timer_warning">#C62828</color>
    <color name="nc_highlight">#8A1C1C</color>
    <color name="nc_badge">#8A1C1C</color>
    <color name="nc_nav_bar">#161616</color>
    <color name="nc_nav_selected">#E8E8E8</color>
    <color name="nc_nav_unselected">#555555</color>
    <color name="nc_status_bar">#0A0A0A</color>
    <color name="nc_tile_empty">#1C1C1C</color>
    <color name="nc_tile_2">#2A2A2A</color>
    <color name="nc_tile_4">#3A3A3A</color>
    <color name="nc_tile_8">#4A4A4A</color>
    <color name="nc_tile_16">#6A6A6A</color>
    <color name="nc_tile_32">#8A1C1C</color>
    <color name="nc_tile_64">#A02424</color>
    <color name="nc_tile_128">#C4A35A</color>
    <color name="nc_tile_256">#D4B86A</color>
    <color name="nc_tile_512">#E8E8E8</color>
    <color name="nc_tile_1024">#F5F5F5</color>
    <color name="nc_tile_2048">#FFFFFF</color>
    <color name="nc_overlay">#E50A0A0A</color>
    <color name="nc_scrim">#990A0A0A</color>
</resources>
```

**字体**：`serif`，标题 `letterSpacing=0.04`，正文不加特效

**形状**：按钮 `2dp` + `1dp` 骨白描边；卡片 `2dp`

**动画**：Smooth & Fluid — 硬切与短 cross-fade，答错时红框一闪

---

## 🖥 CYBER MINT — 薄荷赛博
> 墨绿终端底，薄荷绿光标。像老式 CRT 终端跑分界面。

**灵魂色**：Terminal Mint `#3DFFB5` + Deep Terminal `#04120F`

```xml
<resources>
    <color name="cm_background">#04120F</color>
    <color name="cm_surface">#0A1F1A</color>
    <color name="cm_surface_variant">#123028</color>
    <color name="cm_surface_tint">#0F2A22</color>
    <color name="cm_primary">#3DFFB5</color>
    <color name="cm_primary_dark">#20C98A</color>
    <color name="cm_secondary">#1FA2A2</color>
    <color name="cm_tertiary">#A8FFCE</color>
    <color name="cm_on_background">#D8FFF0</color>
    <color name="cm_on_surface">#D8FFF0</color>
    <color name="cm_on_surface_dim">#4A7A68</color>
    <color name="cm_on_primary">#04120F</color>
    <color name="cm_correct">#3DFFB5</color>
    <color name="cm_wrong">#FF4D6D</color>
    <color name="cm_score">#A8FFCE</color>
    <color name="cm_timer_normal">#3DFFB5</color>
    <color name="cm_timer_warning">#FF8A3D</color>
    <color name="cm_highlight">#A8FFCE</color>
    <color name="cm_badge">#3DFFB5</color>
    <color name="cm_nav_bar">#0A1F1A</color>
    <color name="cm_nav_selected">#3DFFB5</color>
    <color name="cm_nav_unselected">#3A5A50</color>
    <color name="cm_status_bar">#04120F</color>
    <color name="cm_tile_empty">#123028</color>
    <color name="cm_tile_2">#163A30</color>
    <color name="cm_tile_4">#1A4A3C</color>
    <color name="cm_tile_8">#1FA2A2</color>
    <color name="cm_tile_16">#20C98A</color>
    <color name="cm_tile_32">#3DFFB5</color>
    <color name="cm_tile_64">#6AFFC8</color>
    <color name="cm_tile_128">#A8FFCE</color>
    <color name="cm_tile_256">#D8FFF0</color>
    <color name="cm_tile_512">#FF8A3D</color>
    <color name="cm_tile_1024">#FF4D6D</color>
    <color name="cm_tile_2048">#FFFFFF</color>
    <color name="cm_overlay">#CC04120F</color>
    <color name="cm_scrim">#9904120F</color>
</resources>
```

**字体**：`monospace`，数字等宽，标题可轻微 scanline 感（描述即可）

**形状**：按钮 `6dp` + `1dp` mint 描边

**动画**：Fast & Electric — 终端闪烁 100ms 级

---

## 🔥 EMBER COAL — 余烬炭火
> 炭黑底上暗红余烬，偶有琥珀火花。比 Lava Fire 更闷、更暗。

**灵魂色**：Ember Orange `#E85D04` + Coal Black `#100806`

```xml
<resources>
    <color name="ec_background">#100806</color>
    <color name="ec_surface">#1C100C</color>
    <color name="ec_surface_variant">#2A1812</color>
    <color name="ec_surface_tint">#301A12</color>
    <color name="ec_primary">#E85D04</color>
    <color name="ec_primary_dark">#B84503</color>
    <color name="ec_secondary">#DC2F02</color>
    <color name="ec_tertiary">#F48C06</color>
    <color name="ec_on_background">#FFE8D6</color>
    <color name="ec_on_surface">#FFE8D6</color>
    <color name="ec_on_surface_dim">#8A5A40</color>
    <color name="ec_on_primary">#100806</color>
    <color name="ec_correct">#90BE6D</color>
    <color name="ec_wrong">#DC2F02</color>
    <color name="ec_score">#F48C06</color>
    <color name="ec_timer_normal">#F48C06</color>
    <color name="ec_timer_warning">#DC2F02</color>
    <color name="ec_highlight">#F48C06</color>
    <color name="ec_badge">#E85D04</color>
    <color name="ec_nav_bar">#1C100C</color>
    <color name="ec_nav_selected">#E85D04</color>
    <color name="ec_nav_unselected">#5A3A2A</color>
    <color name="ec_status_bar">#100806</color>
    <color name="ec_tile_empty">#2A1812</color>
    <color name="ec_tile_2">#3A2018</color>
    <color name="ec_tile_4">#4A2818</color>
    <color name="ec_tile_8">#6A3410</color>
    <color name="ec_tile_16">#9A4010</color>
    <color name="ec_tile_32">#B84503</color>
    <color name="ec_tile_64">#E85D04</color>
    <color name="ec_tile_128">#F48C06</color>
    <color name="ec_tile_256">#FFB703</color>
    <color name="ec_tile_512">#DC2F02</color>
    <color name="ec_tile_1024">#FFD166</color>
    <color name="ec_tile_2048">#FFFFFF</color>
    <color name="ec_overlay">#CC100806</color>
    <color name="ec_scrim">#99100806</color>
</resources>
```

**字体**：`sans-serif`，标题可加微弱橙色外发光

**形状**：按钮 `4dp`，硬朗；卡片 `4dp`

**动画**：Dramatic & Intense — 180ms 级火花闪

---

## 🍵 MATCHA CAFE — 抹茶咖啡馆
> 抹茶绿 + 燕麦奶色 + 木桌褐。适合 word、crossword 长时间阅读。

**灵魂色**：Matcha `#5F7A45` + Oat Milk `#FFFCF5`

```xml
<resources>
    <color name="mc_background">#F4F1E8</color>
    <color name="mc_surface">#FFFCF5</color>
    <color name="mc_surface_variant">#E4E8D4</color>
    <color name="mc_surface_tint">#F0EDE2</color>
    <color name="mc_primary">#5F7A45</color>
    <color name="mc_primary_dark">#465C32</color>
    <color name="mc_secondary">#C4A574</color>
    <color name="mc_tertiary">#8B6F47</color>
    <color name="mc_on_background">#2A2E22</color>
    <color name="mc_on_surface">#2A2E22</color>
    <color name="mc_on_surface_dim">#7A8070</color>
    <color name="mc_on_primary">#FFFCF5</color>
    <color name="mc_correct">#5F7A45</color>
    <color name="mc_wrong">#B54A3A</color>
    <color name="mc_score">#C4A574</color>
    <color name="mc_timer_normal">#5F7A45</color>
    <color name="mc_timer_warning">#B54A3A</color>
    <color name="mc_highlight">#A8C47A</color>
    <color name="mc_badge">#5F7A45</color>
    <color name="mc_nav_bar">#FFFCF5</color>
    <color name="mc_nav_selected">#5F7A45</color>
    <color name="mc_nav_unselected">#A8A898</color>
    <color name="mc_status_bar">#F4F1E8</color>
    <color name="mc_tile_empty">#E4E8D4</color>
    <color name="mc_tile_2">#D4DCC0</color>
    <color name="mc_tile_4">#C0CCAA</color>
    <color name="mc_tile_8">#A8C47A</color>
    <color name="mc_tile_16">#8BA85C</color>
    <color name="mc_tile_32">#5F7A45</color>
    <color name="mc_tile_64">#465C32</color>
    <color name="mc_tile_128">#C4A574</color>
    <color name="mc_tile_256">#8B6F47</color>
    <color name="mc_tile_512">#B54A3A</color>
    <color name="mc_tile_1024">#E8D5A3</color>
    <color name="mc_tile_2048">#2A2E22</color>
    <color name="mc_overlay">#80E4E8D4</color>
    <color name="mc_scrim">#505F7A45</color>
</resources>
```

**字体**：`sans-serif`，正文字号偏松，适合长文

**形状**：按钮 `12dp`，卡片 `12dp`，无描边

**动画**：Gentle & Breathing — 500–800ms

---

## 🪸 CORAL REEF — 珊瑚礁
> 珊瑚粉 + 潟湖蓝 + 浅沙底。Match-3、bubble 类首选亮色之一。

**灵魂色**：Coral `#FF6F61` + Lagoon `#00A8A8`

```xml
<resources>
    <color name="cr_background">#FFF5F2</color>
    <color name="cr_surface">#FFFFFF</color>
    <color name="cr_surface_variant">#FFE0D6</color>
    <color name="cr_surface_tint">#FFF0EC</color>
    <color name="cr_primary">#FF6F61</color>
    <color name="cr_primary_dark">#E2554A</color>
    <color name="cr_secondary">#00A8A8</color>
    <color name="cr_tertiary">#FFB4A2</color>
    <color name="cr_on_background">#3A1F1A</color>
    <color name="cr_on_surface">#3A1F1A</color>
    <color name="cr_on_surface_dim">#A07870</color>
    <color name="cr_on_primary">#FFFFFF</color>
    <color name="cr_correct">#2BB673</color>
    <color name="cr_wrong">#E2554A</color>
    <color name="cr_score">#00A8A8</color>
    <color name="cr_timer_normal">#00A8A8</color>
    <color name="cr_timer_warning">#FF6F61</color>
    <color name="cr_highlight">#FFB4A2</color>
    <color name="cr_badge">#FF6F61</color>
    <color name="cr_nav_bar">#FFFFFF</color>
    <color name="cr_nav_selected">#FF6F61</color>
    <color name="cr_nav_unselected">#C8A8A0</color>
    <color name="cr_status_bar">#FFF5F2</color>
    <color name="cr_tile_empty">#FFE0D6</color>
    <color name="cr_tile_2">#FFD0C4</color>
    <color name="cr_tile_4">#FFB4A2</color>
    <color name="cr_tile_8">#FF8F7A</color>
    <color name="cr_tile_16">#FF6F61</color>
    <color name="cr_tile_32">#E2554A</color>
    <color name="cr_tile_64">#00A8A8</color>
    <color name="cr_tile_128">#008F8F</color>
    <color name="cr_tile_256">#2BB673</color>
    <color name="cr_tile_512">#FFD166</color>
    <color name="cr_tile_1024">#3A1F1A</color>
    <color name="cr_tile_2048">#FFFFFF</color>
    <color name="cr_overlay">#80FFE0D6</color>
    <color name="cr_scrim">#50FF6F61</color>
</resources>
```

**字体**：`sans-serif-medium`，标题可略大

**形状**：按钮 `20dp`，卡片 `16dp`

**动画**：Bouncy & Playful — 气泡 overshoot

---

## 🍯 HONEY AMBER — 蜂蜜琥珀
> 蜂蜡金 + 奶油白 + 焦糖边。数字类游戏可读性好，温暖不刺眼。

**灵魂色**：Honey `#D4A017` + Cream `#FFFCF5`

```xml
<resources>
    <color name="ha_background">#FFF8EB</color>
    <color name="ha_surface">#FFFCF5</color>
    <color name="ha_surface_variant">#F5E6C8</color>
    <color name="ha_surface_tint">#FFF4E0</color>
    <color name="ha_primary">#D4A017</color>
    <color name="ha_primary_dark">#A67C0A</color>
    <color name="ha_secondary">#E8B86D</color>
    <color name="ha_tertiary">#8B5A2B</color>
    <color name="ha_on_background">#3A2A12</color>
    <color name="ha_on_surface">#3A2A12</color>
    <color name="ha_on_surface_dim">#9A8050</color>
    <color name="ha_on_primary">#3A2A12</color>
    <color name="ha_correct">#6B9E3A</color>
    <color name="ha_wrong">#C4472A</color>
    <color name="ha_score">#D4A017</color>
    <color name="ha_timer_normal">#D4A017</color>
    <color name="ha_timer_warning">#C4472A</color>
    <color name="ha_highlight">#E8B86D</color>
    <color name="ha_badge">#D4A017</color>
    <color name="ha_nav_bar">#FFFCF5</color>
    <color name="ha_nav_selected">#D4A017</color>
    <color name="ha_nav_unselected">#C0A878</color>
    <color name="ha_status_bar">#FFF8EB</color>
    <color name="ha_tile_empty">#F5E6C8</color>
    <color name="ha_tile_2">#F0DCA8</color>
    <color name="ha_tile_4">#E8D08A</color>
    <color name="ha_tile_8">#E8B86D</color>
    <color name="ha_tile_16">#D4A017</color>
    <color name="ha_tile_32">#A67C0A</color>
    <color name="ha_tile_64">#8B5A2B</color>
    <color name="ha_tile_128">#6B9E3A</color>
    <color name="ha_tile_256">#C4472A</color>
    <color name="ha_tile_512">#F0C040</color>
    <color name="ha_tile_1024">#FFF8EB</color>
    <color name="ha_tile_2048">#3A2A12</color>
    <color name="ha_overlay">#80F5E6C8</color>
    <color name="ha_scrim">#50D4A017</color>
</resources>
```

**注意**：`on_primary` 用深褐而非白，保证金按钮上文字对比度

**形状**：按钮 `14dp`，卡片 `12dp`

**动画**：Smooth & Fluid

---

## 🌇 SUNSET PLAZA — 落日广场
> 晚霞橘粉 + 石砖暖灰 + 一点青绿点缀。活动页、季节运营常用。

**灵魂色**：Sunset Coral `#E76F51` + Plaza Teal `#2A9D8F`

```xml
<resources>
    <color name="sz_background">#FFF1E8</color>
    <color name="sz_surface">#FFFAF6</color>
    <color name="sz_surface_variant">#FFD8C2</color>
    <color name="sz_surface_tint">#FFE8DA</color>
    <color name="sz_primary">#E76F51</color>
    <color name="sz_primary_dark">#C4553A</color>
    <color name="sz_secondary">#F4A261</color>
    <color name="sz_tertiary">#2A9D8F</color>
    <color name="sz_on_background">#3A2218</color>
    <color name="sz_on_surface">#3A2218</color>
    <color name="sz_on_surface_dim">#A07A68</color>
    <color name="sz_on_primary">#FFFFFF</color>
    <color name="sz_correct">#2A9D8F</color>
    <color name="sz_wrong">#C4553A</color>
    <color name="sz_score">#F4A261</color>
    <color name="sz_timer_normal">#E76F51</color>
    <color name="sz_timer_warning">#C4553A</color>
    <color name="sz_highlight">#F4A261</color>
    <color name="sz_badge">#E76F51</color>
    <color name="sz_nav_bar">#FFFAF6</color>
    <color name="sz_nav_selected">#E76F51</color>
    <color name="sz_nav_unselected">#C8A898</color>
    <color name="sz_status_bar">#FFF1E8</color>
    <color name="sz_tile_empty">#FFD8C2</color>
    <color name="sz_tile_2">#FFC8A8</color>
    <color name="sz_tile_4">#F4A261</color>
    <color name="sz_tile_8">#E98A4A</color>
    <color name="sz_tile_16">#E76F51</color>
    <color name="sz_tile_32">#C4553A</color>
    <color name="sz_tile_64">#2A9D8F</color>
    <color name="sz_tile_128">#1F7A70</color>
    <color name="sz_tile_256">#E9C46A</color>
    <color name="sz_tile_512">#264653</color>
    <color name="sz_tile_1024">#FFFFFF</color>
    <color name="sz_tile_2048">#3A2218</color>
    <color name="sz_overlay">#80FFD8C2</color>
    <color name="sz_scrim">#50E76F51</color>
</resources>
```

**字体**：`sans-serif`，标题可用 medium

**形状**：按钮 `12dp`，卡片 `12dp`

**动画**：Smooth & Fluid — 地平线式上滑

---

## 🕹 ARCADE CABINET — 街机柜
> CRT 磷光绿 + 机柜深紫 + thruster 橙。比 Pixel Classic 更「机台」，适合 arcade / 高分榜。

**灵魂色**：Phosphor Green `#39FF14` + Cabinet Violet `#161625`

```xml
<resources>
    <color name="ac_background">#0B0B14</color>
    <color name="ac_surface">#161625</color>
    <color name="ac_surface_variant">#222238</color>
    <color name="ac_surface_tint">#1A1A2E</color>
    <color name="ac_primary">#39FF14</color>
    <color name="ac_primary_dark">#28C40E</color>
    <color name="ac_secondary">#FF6B00</color>
    <color name="ac_tertiary">#00E5FF</color>
    <color name="ac_on_background">#E8FFE8</color>
    <color name="ac_on_surface">#E8FFE8</color>
    <color name="ac_on_surface_dim">#5A7A5A</color>
    <color name="ac_on_primary">#0B0B14</color>
    <color name="ac_correct">#39FF14</color>
    <color name="ac_wrong">#FF2A55</color>
    <color name="ac_score">#FF6B00</color>
    <color name="ac_timer_normal">#39FF14</color>
    <color name="ac_timer_warning">#FF6B00</color>
    <color name="ac_highlight">#00E5FF</color>
    <color name="ac_badge">#FF6B00</color>
    <color name="ac_nav_bar">#161625</color>
    <color name="ac_nav_selected">#39FF14</color>
    <color name="ac_nav_unselected">#4A4A68</color>
    <color name="ac_status_bar">#0B0B14</color>
    <color name="ac_tile_empty">#222238</color>
    <color name="ac_tile_2">#2A2A48</color>
    <color name="ac_tile_4">#323260</color>
    <color name="ac_tile_8">#28C40E</color>
    <color name="ac_tile_16">#39FF14</color>
    <color name="ac_tile_32">#00E5FF</color>
    <color name="ac_tile_64">#00B8CC</color>
    <color name="ac_tile_128">#FF6B00</color>
    <color name="ac_tile_256">#FF8C33</color>
    <color name="ac_tile_512">#FF2A55</color>
    <color name="ac_tile_1024">#FFE600</color>
    <color name="ac_tile_2048">#FFFFFF</color>
    <color name="ac_overlay">#CC0B0B14</color>
    <color name="ac_scrim">#990B0B14</color>
</resources>
```

**字体**：`monospace`，分数 ALL CAPS

**形状**：全部 `0dp` + `2dp` 磷光绿描边

**动画**：Instant Snap — 切屏无过渡，正确反馈 CRT 闪一下
