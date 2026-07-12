# Design Principles — Material3 集成指南

## 深色主题 vs 浅色主题设计规则

### 深色主题（Neon Dark / Space Galaxy / Lava Fire / Midnight Luxury / Deep Sea / Aurora Night / Halloween / Steampunk / Graffiti Street / Noir Cinema / Cyber Mint / Ember Coal / Neon Synthwave / Pixel Classic / Arcade Cabinet）

**层次感靠发光，不靠阴影**：
```kotlin
// 深色主题：elevation 通过颜色叠加（color overlay）体现，不用 shadowColor
// Material3 深色主题中，elevation 会自动在 surface 上叠加 primary 色调
// 不要在深色背景上设置 android:elevation 期望看到阴影，因为阴影在暗色背景不可见

// 正确做法：用发光效果替代阴影
fun applyGlowEffect(view: View, glowColor: Int) {
    view.outlineProvider = ViewOutlineProvider.BACKGROUND
    view.elevation = 0f
    // 通过 background drawable 的 shadowColor 模拟发光
    // 或使用 RenderEffect (API 31+)
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        view.setRenderEffect(
            RenderEffect.createBlurEffect(4f, 4f, Shader.TileMode.CLAMP)
        )
    }
}
```

**状态栏配置**（深色主题用亮色图标）：
```kotlin
WindowCompat.setDecorFitsSystemWindows(window, false)
WindowInsetsControllerCompat(window, window.decorView).apply {
    isAppearanceLightStatusBars = false  // 深色背景 → 白色状态栏图标
    isAppearanceLightNavigationBars = false
}
window.statusBarColor = Color.TRANSPARENT
```

### 浅色主题（Ocean Breeze / Forest Zen / Candy Pop / Sakura Spring / Desert Gold / Ice Crystal / Pastel Dream / Christmas / Matcha Cafe / Coral Reef / Honey Amber / Sunset Plaza / Cartoon Fun / Minimalist White / Paper Craft）

**层次感靠阴影和白色背景**：
```kotlin
// 浅色主题：elevation + cardElevation 产生真实阴影
// 卡片用白色背景，背后有阴影
binding.cardQuestion.elevation = 4.dpToPx(this).toFloat()
binding.cardQuestion.useCompatPadding = true
```

**状态栏配置**（浅色主题用深色图标）：
```kotlin
WindowInsetsControllerCompat(window, window.decorView).apply {
    isAppearanceLightStatusBars = true  // 浅色背景 → 深色状态栏图标
    isAppearanceLightNavigationBars = true
}
```

---

## Material3 Theme 完整结构模板

每个主题都应在 `res/values/themes.xml` 中声明 Material3 主题：

```xml
<!-- res/values/themes_neon_dark.xml -->
<resources>
    <style name="Theme.Game.NeonDark" parent="Theme.Material3.Dark.NoActionBar">
        <!-- 主色系 -->
        <item name="colorPrimary">@color/nd_primary</item>
        <item name="colorOnPrimary">@color/nd_on_primary</item>
        <item name="colorPrimaryContainer">@color/nd_secondary</item>
        <item name="colorOnPrimaryContainer">@color/nd_on_surface</item>

        <!-- 次色系 -->
        <item name="colorSecondary">@color/nd_secondary</item>
        <item name="colorOnSecondary">@color/nd_on_primary</item>

        <!-- 背景 -->
        <item name="android:colorBackground">@color/nd_background</item>
        <item name="colorSurface">@color/nd_surface</item>
        <item name="colorOnSurface">@color/nd_on_surface</item>
        <item name="colorSurfaceVariant">@color/nd_surface_variant</item>
        <item name="colorOnSurfaceVariant">@color/nd_on_surface_dim</item>

        <!-- 错误色 -->
        <item name="colorError">@color/nd_wrong</item>
        <item name="colorOnError">#FFFFFF</item>

        <!-- 组件样式 -->
        <item name="materialButtonStyle">@style/Widget.Game.Button.NeonDark</item>
        <item name="materialCardViewStyle">@style/Widget.Game.Card.NeonDark</item>
        <item name="bottomNavigationStyle">@style/Widget.Game.BottomNav.NeonDark</item>
        <item name="toolbarStyle">@style/Widget.Game.Toolbar.NeonDark</item>

        <!-- 字体 -->
        <item name="android:fontFamily">sans-serif-condensed</item>

        <!-- 形状 -->
        <item name="shapeAppearanceSmallComponent">@style/Shape.Game.Small.NeonDark</item>
        <item name="shapeAppearanceMediumComponent">@style/Shape.Game.Medium.NeonDark</item>
        <item name="shapeAppearanceLargeComponent">@style/Shape.Game.Large.NeonDark</item>
    </style>

    <!-- 形状 -->
    <style name="Shape.Game.Small.NeonDark" parent="">
        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">8dp</item>
    </style>
    <style name="Shape.Game.Medium.NeonDark" parent="">
        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">8dp</item>
    </style>
    <style name="Shape.Game.Large.NeonDark" parent="">
        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">12dp</item>
    </style>

    <!-- 按钮 -->
    <style name="Widget.Game.Button.NeonDark" parent="Widget.Material3.Button">
        <item name="backgroundTint">@color/nd_primary</item>
        <item name="android:textColor">@color/nd_on_primary</item>
        <item name="cornerRadius">8dp</item>
        <item name="android:stateListAnimator">@null</item>
        <item name="android:elevation">6dp</item>
    </style>

    <!-- 卡片 -->
    <style name="Widget.Game.Card.NeonDark" parent="Widget.Material3.CardView.Elevated">
        <item name="cardBackgroundColor">@color/nd_surface</item>
        <item name="cardCornerRadius">8dp</item>
        <item name="cardElevation">0dp</item>
        <item name="strokeColor">@color/nd_primary</item>
        <item name="strokeWidth">1dp</item>
    </style>

    <!-- 底部导航 -->
    <style name="Widget.Game.BottomNav.NeonDark" parent="Widget.Material3.BottomNavigationView">
        <item name="android:background">@color/nd_nav_bar</item>
        <item name="itemIconTint">@color/bottom_nav_item_nd</item>
        <item name="itemTextColor">@color/bottom_nav_item_nd</item>
        <item name="itemActiveIndicatorStyle">@style/Widget.Game.NavIndicator.NeonDark</item>
    </style>

    <style name="Widget.Game.NavIndicator.NeonDark" parent="Widget.Material3.BottomNavigationView.ActiveIndicator">
        <item name="android:color">@color/nd_secondary</item>
        <item name="shapeAppearance">@style/Shape.Game.Small.NeonDark</item>
    </style>

    <!-- Toolbar -->
    <style name="Widget.Game.Toolbar.NeonDark" parent="Widget.Material3.Toolbar">
        <item name="android:background">@color/nd_surface</item>
        <item name="titleTextColor">@color/nd_on_surface</item>
        <item name="navigationIconTint">@color/nd_on_surface</item>
    </style>

</resources>
```

---

## 动态主题切换（Runtime Theme Switch）

```kotlin
// GameThemeManager.kt
enum class GameTheme(val styleRes: Int, val prefKey: String) {
    NEON_DARK(R.style.Theme_Game_NeonDark, "neon_dark"),
    SPACE_GALAXY(R.style.Theme_Game_SpaceGalaxy, "space_galaxy"),
    LAVA_FIRE(R.style.Theme_Game_LavaFire, "lava_fire"),
    MIDNIGHT_LUXURY(R.style.Theme_Game_MidnightLuxury, "midnight_luxury"),
    OCEAN_BREEZE(R.style.Theme_Game_OceanBreeze, "ocean_breeze"),
    FOREST_ZEN(R.style.Theme_Game_ForestZen, "forest_zen"),
    CANDY_POP(R.style.Theme_Game_CandyPop, "candy_pop"),
    SAKURA_SPRING(R.style.Theme_Game_SakuraSpring, "sakura_spring"),
    DESERT_GOLD(R.style.Theme_Game_DesertGold, "desert_gold"),
    ICE_CRYSTAL(R.style.Theme_Game_IceCrystal, "ice_crystal"),
    PIXEL_CLASSIC(R.style.Theme_Game_PixelClassic, "pixel_classic"),
    HALLOWEEN(R.style.Theme_Game_Halloween, "halloween"),
    CHRISTMAS(R.style.Theme_Game_Christmas, "christmas"),
    PASTEL_DREAM(R.style.Theme_Game_PastelDream, "pastel_dream"),
    NEON_SYNTHWAVE(R.style.Theme_Game_NeonSynthwave, "neon_synthwave"),
}

object GameThemeManager {
    fun applyTheme(activity: Activity) {
        val prefs = activity.getSharedPreferences("game_prefs", Context.MODE_PRIVATE)
        val themeKey = prefs.getString("theme", GameTheme.NEON_DARK.prefKey)
        val theme = GameTheme.entries.find { it.prefKey == themeKey } ?: GameTheme.NEON_DARK
        activity.setTheme(theme.styleRes)
    }

    fun saveTheme(context: Context, theme: GameTheme) {
        context.getSharedPreferences("game_prefs", Context.MODE_PRIVATE)
            .edit().putString("theme", theme.prefKey).apply()
    }
}

// 在每个 Activity.onCreate() 的最顶部调用，必须在 super.onCreate() 之前：
class HomeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        GameThemeManager.applyTheme(this)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)
    }
}
```

---

## 主题预览卡片组件

设置页展示主题选择器，每个主题用一张预览卡：

```kotlin
// ThemePreviewCard.kt (custom View)
class ThemePreviewCard @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null
) : MaterialCardView(context, attrs) {

    fun bind(theme: GameTheme, isSelected: Boolean) {
        val colors = GameThemeColors.get(theme) // 从资源获取主题色
        setCardBackgroundColor(colors.background)
        strokeColor = if (isSelected) colors.primary else Color.TRANSPARENT
        strokeWidth = if (isSelected) 3.dpToPx(context) else 0

        // 卡片内部：小色块展示主色+辅色+背景
        binding.viewPrimary.setBackgroundColor(colors.primary)
        binding.viewSecondary.setBackgroundColor(colors.secondary)
        binding.tvThemeName.setTextColor(colors.onBackground)
        binding.tvThemeName.text = theme.displayName
    }
}
```
