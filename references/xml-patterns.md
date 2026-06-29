# XML Patterns — Reusable Snippet Library

## KPI Card (statistics page, 4-card row)

```xml
<!-- Single KPI card — use 4× in horizontal chain for statistics page -->
<com.google.android.material.card.MaterialCardView
    android:id="@+id/card_kpi_total"
    android:layout_width="0dp"
    android:layout_height="@dimen/game_kpi_card_height"
    app:cardCornerRadius="@dimen/game_corner_radius"
    app:cardElevation="@dimen/game_elevation">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:gravity="center"
        android:padding="8dp">

        <TextView
            android:id="@+id/tv_kpi_value"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="0"
            android:textAppearance="?attr/textAppearanceHeadlineSmall"
            android:textStyle="bold"
            android:textColor="@color/THEME_score" />

        <TextView
            android:id="@+id/tv_kpi_label"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="GAMES"
            android:textAppearance="?attr/textAppearanceLabelSmall"
            android:textColor="@color/THEME_on_surface_dim"
            android:textAllCaps="true" />
    </LinearLayout>
</com.google.android.material.card.MaterialCardView>
```

---

## Bottom Navigation (shared across app shell pages)

```xml
<!-- res/menu/bottom_nav_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/nav_home"
        android:icon="@drawable/ic_home"
        android:title="Home" />
    <item
        android:id="@+id/nav_history"
        android:icon="@drawable/ic_history"
        android:title="History" />
    <item
        android:id="@+id/nav_stats"
        android:icon="@drawable/ic_bar_chart"
        android:title="Stats" />
    <item
        android:id="@+id/nav_settings"
        android:icon="@drawable/ic_settings"
        android:title="Settings" />
</menu>
```

```xml
<!-- In layout: -->
<com.google.android.material.bottomnavigation.BottomNavigationView
    android:id="@+id/bottom_nav"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_gravity="bottom"
    android:background="@color/THEME_nav_bar"
    app:menu="@menu/bottom_nav_menu"
    app:itemIconTint="@color/bottom_nav_item_color"
    app:itemTextColor="@color/bottom_nav_item_color"
    app:labelVisibilityMode="labeled" />
```

**Bottom nav item color selector** (`res/color/bottom_nav_item_color.xml`):
```xml
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/THEME_primary" android:state_checked="true" />
    <item android:color="@color/THEME_on_surface_dim" />
</selector>
```

---

## Settings Switch Row

```xml
<!-- Reusable switch row — use <include> for each setting -->
<!-- res/layout/item_setting_switch.xml -->
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="56dp"
    android:orientation="horizontal"
    android:gravity="center_vertical"
    android:paddingHorizontal="4dp">

    <ImageView
        android:id="@+id/iv_setting_icon"
        android:layout_width="24dp"
        android:layout_height="24dp"
        android:src="@drawable/ic_volume_up"
        android:contentDescription="Setting icon"
        android:layout_marginEnd="16dp" />

    <TextView
        android:id="@+id/tv_setting_label"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:text="Sound Effects"
        android:textAppearance="?attr/textAppearanceBodyLarge"
        android:textColor="@color/THEME_on_surface" />

    <com.google.android.material.switchmaterial.SwitchMaterial
        android:id="@+id/sw_setting"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:checked="true"
        android:contentDescription="Toggle sound effects" />
</LinearLayout>
```

---

## Section Header (settings / statistics pages)

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="AUDIO"
    android:textAppearance="?attr/textAppearanceLabelLarge"
    android:textColor="@color/THEME_primary"
    android:textAllCaps="true"
    android:letterSpacing="0.1"
    android:layout_marginTop="16dp"
    android:layout_marginBottom="4dp" />
```

---

## Step Number Circle (how to play page)

```xml
<!-- res/drawable/bg_step_circle.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval">
    <solid android:color="@color/THEME_primary" />
</shape>
```

```xml
<TextView
    android:id="@+id/tv_step_number"
    android:layout_width="32dp"
    android:layout_height="32dp"
    android:text="1"
    android:gravity="center"
    android:textStyle="bold"
    android:textAppearance="?attr/textAppearanceTitleSmall"
    android:textColor="@color/THEME_on_primary"
    android:background="@drawable/bg_step_circle" />
```

---

## Difficulty Badge Chip

```kotlin
// Kotlin: set chip color based on difficulty
fun setDifficultyChip(chip: Chip, difficulty: String) {
    val (text, bgColor, textColor) = when (difficulty.lowercase()) {
        "easy"   -> Triple("Easy",   R.color.chip_easy_bg,   R.color.chip_easy_text)
        "hard"   -> Triple("Hard",   R.color.chip_hard_bg,   R.color.chip_hard_text)
        else     -> Triple("Medium", R.color.chip_medium_bg, R.color.chip_medium_text)
    }
    chip.text = text
    chip.chipBackgroundColor = ColorStateList.valueOf(ContextCompat.getColor(chip.context, bgColor))
    chip.setTextColor(ContextCompat.getColor(chip.context, textColor))
}
```

---

## Score Bar (top of any game screen)

```xml
<!-- res/layout/include_score_bar.xml -->
<merge xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <com.google.android.material.card.MaterialCardView
        android:id="@+id/card_score"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:cardCornerRadius="@dimen/game_corner_radius"
        app:cardElevation="@dimen/game_elevation">

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="8dp"
            android:minWidth="80dp"
            android:gravity="center">

            <TextView
                android:id="@+id/tv_score_label"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="SCORE"
                android:textAppearance="?attr/textAppearanceLabelSmall"
                android:textAllCaps="true" />

            <TextView
                android:id="@+id/tv_score_value"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="0"
                android:textAppearance="?attr/textAppearanceTitleLarge"
                android:textStyle="bold" />
        </LinearLayout>
    </com.google.android.material.card.MaterialCardView>

</merge>
```

---

## Answer Button (quiz game)

```xml
<!-- Single answer button — repeat 4× with ids btn_answer_a/b/c/d -->
<com.google.android.material.button.MaterialButton
    android:id="@+id/btn_answer_a"
    android:layout_width="0dp"
    android:layout_height="@dimen/game_button_height"
    android:layout_marginHorizontal="16dp"
    android:text="A. Answer option here"
    android:textAppearance="?attr/textAppearanceTitleSmall"
    android:gravity="start|center_vertical"
    android:paddingStart="16dp"
    app:cornerRadius="@dimen/game_corner_radius"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintTop_toBottomOf="@id/card_question"
    android:layout_marginTop="24dp" />
```

**State color via selector** (`res/color/answer_button_bg.xml`):
```xml
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:color="@color/THEME_correct" android:state_activated="true" android:state_checked="true"/>
    <item android:color="@color/THEME_wrong"   android:state_activated="true" android:state_checked="false"/>
    <item android:color="@color/THEME_surface" />
</selector>
```

---

## 2048 Tile Drawable

```xml
<!-- res/drawable/bg_tile_2048.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <corners android:radius="@dimen/game_corner_radius" />
    <solid android:color="@color/THEME_tile_2" />
</shape>
```

Swap `@color/THEME_tile_2` dynamically in Kotlin:
```kotlin
fun setTileValue(tv: TextView, value: Int) {
    val (bgColor, textColor) = tileColorMap[value] ?: tileColorMap[2048]!!
    (tv.background as? GradientDrawable)?.setColor(ContextCompat.getColor(this, bgColor))
    tv.setTextColor(ContextCompat.getColor(this, textColor))
    tv.text = if (value == 0) "" else value.toString()
}
```

---

## Game Button (primary action)

```xml
<!-- res/drawable/bg_button_primary.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <corners android:radius="@dimen/game_corner_radius" />
    <solid android:color="@color/THEME_primary" />
    <padding android:left="16dp" android:right="16dp"
             android:top="12dp" android:bottom="12dp" />
</shape>
```

---

## Letter Cell (word search)

```xml
<!-- res/drawable/bg_letter_cell.xml -->
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_selected="true">
        <shape android:shape="rectangle">
            <corners android:radius="4dp" />
            <solid android:color="@color/THEME_highlight" />
        </shape>
    </item>
    <item android:state_activated="true">
        <shape android:shape="rectangle">
            <corners android:radius="4dp" />
            <solid android:color="@color/THEME_correct" />
        </shape>
    </item>
    <item>
        <shape android:shape="rectangle">
            <corners android:radius="4dp" />
            <solid android:color="@color/THEME_surface" />
            <stroke android:width="1dp" android:color="@color/THEME_surface_variant" />
        </shape>
    </item>
</selector>
```

---

## Timer TextView Styles

```xml
<!-- Pulse animation for low time warning -->
<!-- res/anim/timer_pulse.xml -->
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <scale
        android:fromXScale="1.0" android:toXScale="1.2"
        android:fromYScale="1.0" android:toYScale="1.2"
        android:pivotX="50%" android:pivotY="50%"
        android:duration="300"
        android:repeatMode="reverse"
        android:repeatCount="infinite" />
</set>
```

```kotlin
fun startTimerWarning(tv: TextView, themeWarningColor: Int) {
    tv.setTextColor(themeWarningColor)
    val anim = AnimationUtils.loadAnimation(this, R.anim.timer_pulse)
    tv.startAnimation(anim)
}
```

---

## Pause Button (floating, top-left)

```xml
<ImageButton
    android:id="@+id/ibtn_pause"
    android:layout_width="40dp"
    android:layout_height="40dp"
    android:src="@drawable/ic_pause"
    android:background="?attr/selectableItemBackgroundBorderless"
    android:contentDescription="Pause game"
    android:padding="8dp"
    app:layout_constraintTop_toTopOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    android:layout_marginTop="16dp"
    android:layout_marginStart="16dp" />
```

---

## Star Rating Row (game over)

```xml
<LinearLayout
    android:id="@+id/ll_stars"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:gravity="center_vertical"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintTop_toBottomOf="@id/tv_game_over_title"
    android:layout_marginTop="24dp">

    <ImageView
        android:id="@+id/iv_star_1"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:src="@drawable/ic_star_filled"
        android:contentDescription="Star 1"
        android:layout_marginHorizontal="4dp" />

    <ImageView
        android:id="@+id/iv_star_2"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:src="@drawable/ic_star_empty"
        android:contentDescription="Star 2"
        android:layout_marginHorizontal="4dp" />

    <ImageView
        android:id="@+id/iv_star_3"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:src="@drawable/ic_star_empty"
        android:contentDescription="Star 3"
        android:layout_marginHorizontal="4dp" />

</LinearLayout>
```

---

## Dimensions (res/values/dimens_game.xml)

```xml
<resources>
    <dimen name="game_padding_screen">16dp</dimen>
    <dimen name="game_padding_card">12dp</dimen>
    <dimen name="game_tile_size_2048">72dp</dimen>
    <dimen name="game_tile_gap_2048">8dp</dimen>
    <dimen name="game_button_height">56dp</dimen>
    <dimen name="game_score_text_size">24sp</dimen>
    <dimen name="game_question_text_size">20sp</dimen>
    <dimen name="game_answer_text_size">16sp</dimen>
    <dimen name="game_timer_text_size">28sp</dimen>
    <dimen name="game_logo_size">120dp</dimen>
    <dimen name="game_star_size">48dp</dimen>

    <!-- Per-theme corner radius — override in each theme's dimens -->
    <dimen name="game_corner_radius">8dp</dimen>
    <dimen name="game_elevation">4dp</dimen>
</resources>
```
