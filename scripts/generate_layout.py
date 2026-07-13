#!/usr/bin/env python3
"""
generate_layout.py — Print design constraints (text) for a given screen + theme.

Outputs a human-readable constraint summary for authoring design-spec markdown.
Does NOT generate Android layout XML or Kotlin.

Usage:
    python3 scripts/generate_layout.py --screen game_quiz --theme neon_dark
    python3 scripts/generate_layout.py --list-screens
    python3 scripts/generate_layout.py --list-themes
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent

# ── Theme metadata ────────────────────────────────────────────────────────────
THEMES: dict[str, dict] = {
    "neon_dark":        {"prefix": "nd",  "corner": "8dp",  "tile_corner": "4dp",  "elevation": "6dp",  "dark": True,  "animation": "Fast & Electric",    "duration": "80–150ms",  "interpolator": "FastOutLinearIn",           "font": "sans-serif-condensed", "stroke": "1dp"},
    "space_galaxy":     {"prefix": "sg",  "corner": "24dp", "tile_corner": "12dp", "elevation": "0dp",  "dark": True,  "animation": "Smooth & Floating",   "duration": "250–400ms", "interpolator": "DecelerateInterpolator",    "font": "sans-serif-light",     "stroke": "0dp"},
    "lava_fire":        {"prefix": "lf",  "corner": "4dp",  "tile_corner": "2dp",  "elevation": "0dp",  "dark": True,  "animation": "Dramatic & Intense",  "duration": "100–200ms", "interpolator": "LinearInterpolator",        "font": "sans-serif",           "stroke": "0dp"},
    "midnight_luxury":  {"prefix": "ml",  "corner": "2dp",  "tile_corner": "2dp",  "elevation": "4dp",  "dark": True,  "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "1dp"},
    "deep_sea":         {"prefix": "ds",  "corner": "12dp", "tile_corner": "8dp",  "elevation": "0dp",  "dark": True,  "animation": "Smooth & Floating",   "duration": "300–400ms", "interpolator": "DecelerateInterpolator",    "font": "sans-serif-light",     "stroke": "0dp"},
    "aurora_night":     {"prefix": "an",  "corner": "20dp", "tile_corner": "10dp", "elevation": "0dp",  "dark": True,  "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif-light",     "stroke": "0dp"},
    "halloween":        {"prefix": "hw",  "corner": "8dp",  "tile_corner": "4dp",  "elevation": "0dp",  "dark": True,  "animation": "Dramatic & Intense",  "duration": "100–200ms", "interpolator": "LinearInterpolator",        "font": "serif",                "stroke": "1dp"},
    "steampunk":        {"prefix": "sp",  "corner": "4dp",  "tile_corner": "2dp",  "elevation": "4dp",  "dark": True,  "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "2dp"},
    "graffiti_street":  {"prefix": "gs",  "corner": "0dp",  "tile_corner": "0dp",  "elevation": "0dp",  "dark": True,  "animation": "Fast & Electric",     "duration": "80–150ms",  "interpolator": "FastOutLinearIn",           "font": "sans-serif-black",     "stroke": "3dp"},
    "ocean_breeze":     {"prefix": "ob",  "corner": "16dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "forest_zen":       {"prefix": "fz",  "corner": "12dp", "tile_corner": "8dp",  "elevation": "2dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "candy_pop":        {"prefix": "cp",  "corner": "24dp", "tile_corner": "12dp", "elevation": "8dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "400–500ms", "interpolator": "OvershootInterpolator(2f)", "font": "sans-serif-medium",    "stroke": "0dp"},
    "sakura_spring":    {"prefix": "sk",  "corner": "20dp", "tile_corner": "10dp", "elevation": "4dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "400–500ms", "interpolator": "OvershootInterpolator(2f)", "font": "sans-serif-light",     "stroke": "0dp"},
    "desert_gold":      {"prefix": "dg",  "corner": "8dp",  "tile_corner": "4dp",  "elevation": "4dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "1dp"},
    "ice_crystal":      {"prefix": "ic",  "corner": "16dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif-light",     "stroke": "1dp"},
    "pastel_dream":     {"prefix": "pd",  "corner": "16dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "christmas":        {"prefix": "xm",  "corner": "12dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Festive & Sparkling", "duration": "300–600ms", "interpolator": "OvershootInterpolator",     "font": "sans-serif-medium",    "stroke": "0dp"},
    "pixel_classic":    {"prefix": "pc",  "corner": "0dp",  "tile_corner": "0dp",  "elevation": "0dp",  "dark": True,  "animation": "Instant Snap",        "duration": "0ms",       "interpolator": "none (instant)",            "font": "monospace",            "stroke": "2dp"},
    "cartoon_fun":      {"prefix": "cf",  "corner": "20dp", "tile_corner": "8dp",  "elevation": "6dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "400–500ms", "interpolator": "OvershootInterpolator(3f)", "font": "sans-serif-medium",    "stroke": "3dp"},
    "minimalist_white": {"prefix": "mw",  "corner": "10dp", "tile_corner": "6dp",  "elevation": "2dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "paper_craft":      {"prefix": "ppc", "corner": "8dp",  "tile_corner": "4dp",  "elevation": "8dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "neon_synthwave":   {"prefix": "sw",  "corner": "8dp",  "tile_corner": "4dp",  "elevation": "0dp",  "dark": True,  "animation": "Fast & Electric",     "duration": "80–150ms",  "interpolator": "FastOutLinearIn",           "font": "sans-serif-condensed", "stroke": "1dp"},
    "noir_cinema":      {"prefix": "nc",  "corner": "2dp",  "tile_corner": "2dp",  "elevation": "4dp",  "dark": True,  "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "1dp"},
    "cyber_mint":       {"prefix": "cm",  "corner": "6dp",  "tile_corner": "4dp",  "elevation": "0dp",  "dark": True,  "animation": "Fast & Electric",     "duration": "80–150ms",  "interpolator": "FastOutLinearIn",           "font": "monospace",            "stroke": "1dp"},
    "ember_coal":       {"prefix": "ec",  "corner": "4dp",  "tile_corner": "2dp",  "elevation": "0dp",  "dark": True,  "animation": "Dramatic & Intense",  "duration": "100–200ms", "interpolator": "LinearInterpolator",        "font": "sans-serif",           "stroke": "0dp"},
    "matcha_cafe":      {"prefix": "mc",  "corner": "12dp", "tile_corner": "8dp",  "elevation": "2dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "coral_reef":       {"prefix": "cr",  "corner": "20dp", "tile_corner": "10dp", "elevation": "6dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "400–500ms", "interpolator": "OvershootInterpolator(2f)", "font": "sans-serif-medium",    "stroke": "0dp"},
    "honey_amber":      {"prefix": "ha",  "corner": "14dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "sunset_plaza":     {"prefix": "sz",  "corner": "12dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "arcade_cabinet":   {"prefix": "ac",  "corner": "0dp",  "tile_corner": "0dp",  "elevation": "0dp",  "dark": True,  "animation": "Instant Snap",        "duration": "0–80ms",    "interpolator": "none (instant)",            "font": "monospace",            "stroke": "2dp"},
    "cyberpunk_city":   {"prefix": "cc",  "corner": "6dp",  "tile_corner": "4dp",  "elevation": "0dp",  "dark": True,  "animation": "Fast & Electric",     "duration": "80–150ms",  "interpolator": "FastOutLinearIn",           "font": "sans-serif-condensed", "stroke": "1dp"},
    "pirate_cove":      {"prefix": "pi",  "corner": "6dp",  "tile_corner": "4dp",  "elevation": "4dp",  "dark": True,  "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "2dp"},
    "royal_velvet":     {"prefix": "rv",  "corner": "4dp",  "tile_corner": "2dp",  "elevation": "4dp",  "dark": True,  "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "1dp"},
    "industrial_steel": {"prefix": "is",  "corner": "2dp",  "tile_corner": "2dp",  "elevation": "2dp",  "dark": True,  "animation": "Fast & Electric",     "duration": "100–200ms", "interpolator": "LinearInterpolator",        "font": "sans-serif-condensed", "stroke": "2dp"},
    "night_market":     {"prefix": "nm",  "corner": "10dp", "tile_corner": "6dp",  "elevation": "0dp",  "dark": True,  "animation": "Festive & Sparkling", "duration": "250–450ms", "interpolator": "OvershootInterpolator",     "font": "sans-serif-medium",    "stroke": "0dp"},
    "moonlit_garden":   {"prefix": "mg",  "corner": "16dp", "tile_corner": "10dp", "elevation": "0dp",  "dark": True,  "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif-light",     "stroke": "0dp"},
    "tropical_fruit":   {"prefix": "tf",  "corner": "20dp", "tile_corner": "10dp", "elevation": "6dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "400–500ms", "interpolator": "OvershootInterpolator(2f)", "font": "sans-serif-medium",    "stroke": "0dp"},
    "bubble_tea":       {"prefix": "bt",  "corner": "18dp", "tile_corner": "10dp", "elevation": "4dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "400–600ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "farm_cottage":     {"prefix": "fc",  "corner": "12dp", "tile_corner": "8dp",  "elevation": "3dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif",           "stroke": "0dp"},
    "cloud_sky":        {"prefix": "cs",  "corner": "24dp", "tile_corner": "12dp", "elevation": "2dp",  "dark": False, "animation": "Smooth & Floating",   "duration": "300–450ms", "interpolator": "DecelerateInterpolator",    "font": "sans-serif-light",     "stroke": "0dp"},
    "lavender_fields":  {"prefix": "lv",  "corner": "16dp", "tile_corner": "8dp",  "elevation": "3dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif-light",     "stroke": "0dp"},
    "citrus_fresh":     {"prefix": "ct",  "corner": "14dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "350–450ms", "interpolator": "OvershootInterpolator",     "font": "sans-serif-medium",    "stroke": "0dp"},
    "crystal_gem":      {"prefix": "cg",  "corner": "12dp", "tile_corner": "6dp",  "elevation": "0dp",  "dark": True,  "animation": "Smooth & Floating",   "duration": "250–400ms", "interpolator": "DecelerateInterpolator",    "font": "sans-serif-light",     "stroke": "1dp"},
    "clay_stopmotion":  {"prefix": "cl",  "corner": "16dp", "tile_corner": "10dp", "elevation": "6dp",  "dark": False, "animation": "Bouncy & Playful",    "duration": "400–550ms", "interpolator": "OvershootInterpolator(2f)", "font": "sans-serif-medium",    "stroke": "0dp"},
    "board_game_table": {"prefix": "bg",  "corner": "8dp",  "tile_corner": "4dp",  "elevation": "6dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "1dp"},
    "comic_halftone":   {"prefix": "ch",  "corner": "4dp",  "tile_corner": "2dp",  "elevation": "0dp",  "dark": False, "animation": "Fast & Electric",     "duration": "80–150ms",  "interpolator": "FastOutLinearIn",           "font": "sans-serif-black",     "stroke": "3dp"},
    "ink_wash":         {"prefix": "iw",  "corner": "2dp",  "tile_corner": "2dp",  "elevation": "1dp",  "dark": False, "animation": "Gentle & Breathing",  "duration": "500–800ms", "interpolator": "AccelerateDecelerate",      "font": "serif",                "stroke": "0dp"},
    "retro_poster":     {"prefix": "rp",  "corner": "0dp",  "tile_corner": "0dp",  "elevation": "4dp",  "dark": False, "animation": "Smooth & Fluid",      "duration": "200–300ms", "interpolator": "AccelerateDecelerate",      "font": "sans-serif-condensed", "stroke": "2dp"},
    "jungle_adventure": {"prefix": "ja",  "corner": "10dp", "tile_corner": "6dp",  "elevation": "0dp",  "dark": True,  "animation": "Dramatic & Intense",  "duration": "150–250ms", "interpolator": "LinearInterpolator",        "font": "sans-serif",           "stroke": "1dp"},
    "snow_festival":    {"prefix": "sf",  "corner": "16dp", "tile_corner": "8dp",  "elevation": "4dp",  "dark": False, "animation": "Festive & Sparkling", "duration": "300–600ms", "interpolator": "OvershootInterpolator",     "font": "sans-serif-medium",    "stroke": "0dp"},
}

# ── Screen design constraints ─────────────────────────────────────────────────
# Each screen defines: title, components list, spacing rules, notes
SCREENS: dict[str, dict] = {
    "home": {
        "title": "首页 (activity_home.xml)",
        "layout": "CoordinatorLayout > ConstraintLayout + BottomNavigationView",
        "components": [
            ("iv_logo",            "140×140dp, verticalBias=0.22"),
            ("tv_app_name",        "textAppearanceHeadlineMedium, bold"),
            ("tv_tagline",         "textAppearanceBodyMedium, {p}_on_surface_dim"),
            ("card_daily",         "可选: 0dp宽, 80dp高, marginH=16dp"),
            ("btn_play",           "240dp宽 × 56dp高, filled, center"),
            ("tv_last_score",      "textAppearanceLabelLarge, {p}_score"),
            ("bottom_nav",         "height=56dp, 4 items: Home/History/Stats/Settings"),
        ],
        "spacing": [
            "屏幕水平边距: 16dp",
            "logo → app_name: 12dp",
            "app_name → tagline: 4dp",
            "tagline → card_daily: 24dp",
            "card_daily → btn_play: 32dp (或直接 btn_play verticalBias=0.55)",
        ],
        "notes": [],
    },
    "history": {
        "title": "历史页 (activity_history.xml)",
        "layout": "CoordinatorLayout > Toolbar + ChipGroup + RecyclerView + BottomNav",
        "components": [
            ("toolbar",            "56dp高, title='History', {p}_surface 背景"),
            ("chip_group",         "ChipGroup singleSelection: All/Won/Lost/Best，marginV=8dp"),
            ("rv_history",         "LinearLayoutManager, item=item_history_row.xml"),
            ("view_empty",         "80dp 图标 + 'No games yet. Start playing!' + btn_play_now"),
        ],
        "spacing": [
            "ChipGroup marginH=16dp, 各 Chip 间距 8dp",
            "RecyclerView item paddingV=12dp, paddingH=16dp",
            "item 内: icon=36dp, 左边距=12dp, 文字列宽占满剩余空间",
        ],
        "notes": [
            "tv_score: textAppearanceTitleMedium bold, 颜色 {p}_score",
            "chip_result: WIN={p}_correct 背景, LOSE={p}_wrong 背景",
        ],
    },
    "statistics": {
        "title": "统计页 (activity_statistics.xml)",
        "layout": "CoordinatorLayout > Toolbar + NestedScrollView(LinearLayout) + BottomNav",
        "components": [
            ("kpi_row",            "4张卡水平均分, 高度80dp, 圆角{corner}"),
            ("tv_kpi_value",       "textAppearanceHeadlineSmall bold, {p}_score"),
            ("tv_kpi_label",       "textAppearanceLabelSmall, {p}_on_surface_dim"),
            ("card_chart",         "高度200dp, 内含图表View(MPAndroidChart)"),
            ("ll_game_breakdown",  "按游戏类型逐行, 每行含图标36dp+名称+数值"),
            ("grid_achievements",  "GridLayout 4列, 每格60dp×80dp"),
        ],
        "spacing": [
            "KPI 卡间距: 8dp, 组边距 marginH=16dp",
            "card_chart marginTop=16dp",
            "各 Section 间距: 24dp",
        ],
        "notes": [],
    },
    "settings": {
        "title": "设置页 (activity_settings.xml)",
        "layout": "CoordinatorLayout > Toolbar + NestedScrollView(LinearLayout) + BottomNav",
        "components": [
            ("section_header",     "textAppearanceLabelMedium, {p}_primary, marginTop=24dp"),
            ("switch_sound",       "SwitchMaterial, 行高52dp, paddingH=16dp"),
            ("switch_music",       "SwitchMaterial"),
            ("switch_vibration",   "SwitchMaterial"),
            ("theme_radio_group",  "RadioGroup, 每行: RadioButton + 主题名 + 16dp 色圆"),
            ("difficulty_group",   "RadioGroup horizontal: Easy/Medium/Hard"),
            ("btn_reset",          "outlined, {p}_wrong 描边色, marginTop=16dp"),
            ("tv_version",         "textAppearanceLabelSmall, center, marginTop=32dp"),
        ],
        "spacing": [
            "Section header marginTop=24dp, marginBottom=8dp",
            "Switch 行高52dp, 分隔线 1dp {p}_surface_variant",
            "主题行高56dp, 色圆size=16dp, marginEnd=12dp",
        ],
        "notes": [
            "深色主题: Section header 用 {p}_primary",
            "浅色主题: Section header 用 {p}_on_surface_dim",
        ],
    },
    "how_to_play": {
        "title": "玩法说明页 (activity_how_to_play.xml)",
        "layout": "变体A(复杂游戏): ViewPager2+TabLayout | 变体B(简单游戏): NestedScrollView+步骤卡",
        "components": [
            ("变体A - vp_slides",   "ViewPager2, 每slide: iv_tutorial(280dp) + 标题 + 描述"),
            ("变体A - tab_dots",    "TabLayout dot模式, marginTop=12dp"),
            ("变体A - btn_next",    "右下角悬浮, 最后页变为'GOT IT!'"),
            ("变体B - step_card",   "每张卡: 步骤圆(32dp) + tv_step_title + tv_step_desc"),
            ("btn_start",           "240dp×56dp, filled, 页面底部固定"),
        ],
        "spacing": [
            "变体A slide paddingH=24dp",
            "变体B 步骤圆左边距16dp, 圆与文字间距12dp",
            "步骤卡 paddingV=16dp, 步骤间距8dp",
        ],
        "notes": ["步骤圆: 32dp, filled={p}_primary, text={p}_on_primary"],
    },
    "leaderboard": {
        "title": "排行榜页 (activity_leaderboard.xml)",
        "layout": "CoordinatorLayout > Toolbar + RecyclerView + BottomNav",
        "components": [
            ("card_top3",          "前3名特殊展示: 奖杯图标+名次+头像+昵称+分数, 高160dp"),
            ("rv_leaderboard",     "4名之后列表, item: rank + avatar + name + score"),
            ("tv_my_rank",         "固定底部条: '你的排名: #N', {p}_highlight 背景"),
        ],
        "spacing": [
            "top3 卡 marginH=16dp, 内部3列等分",
            "列表 item paddingV=12dp, paddingH=16dp",
            "my_rank 条高48dp",
        ],
        "notes": ["第1名高度比2、3名多8dp(突出感)"],
    },
    "onboarding": {
        "title": "新手引导页 (activity_onboarding.xml)",
        "layout": "ConstraintLayout 全屏, ViewPager2 + 底部指示器 + 按钮",
        "components": [
            ("vp_onboarding",      "全屏 ViewPager2, 无页边距"),
            ("page_indicator",     "圆点指示器, 激活=8dp, 非激活=6dp, {p}_primary"),
            ("btn_skip",           "右上角 TextButton, '{p}_on_surface_dim'"),
            ("btn_next",           "底部右侧 FAB 或 FilledButton 240dp"),
        ],
        "spacing": [
            "page 插图上部 1/2 屏幕, 文字下部 1/2",
            "指示器 marginBottom=24dp",
            "btn_next marginBottom=32dp",
        ],
        "notes": [],
    },
    "game_quiz": {
        "title": "Quiz 游戏页 (activity_game_quiz.xml)",
        "layout": "ConstraintLayout 全屏",
        "components": [
            ("pb_progress",        "LinearProgressIndicator, 全宽顶部, height=4dp, indicatorColor={p}_primary"),
            ("ibtn_pause",         "40×40dp, 图标按钮, marginStart=16dp, marginTop=8dp"),
            ("tv_question_number", "textAppearanceLabelLarge, {p}_on_surface_dim"),
            ("tv_timer",           "textAppearanceHeadlineSmall bold, {p}_score, marginEnd=16dp"),
            ("card_question",      "0dp宽, minHeight=120dp, padding=16dp, {p}_surface"),
            ("tv_question",        "textAppearanceTitleMedium, {p}_on_surface, gravity=center"),
            ("btn_answer_a/b/c/d", "0dp宽 × 56dp高, gravity=start|center_vertical, paddingStart=16dp"),
        ],
        "spacing": [
            "card_question marginH=16dp, marginTop=16dp",
            "btn_answer_a marginTop=24dp (从card底部)",
            "btn_answer b/c/d 各 marginTop=12dp",
            "按钮 marginH=16dp",
        ],
        "notes": [
            "答案按钮状态: 默认={p}_surface, 答对={p}_correct, 答错={p}_wrong",
            "深色主题: card 无elevation, 加 strokeWidth=1dp strokeColor={p}_primary",
            "浅色主题: cardElevation=4dp",
        ],
    },
    "game_2048": {
        "title": "2048 游戏页 (activity_game_2048.xml)",
        "layout": "ConstraintLayout 全屏",
        "components": [
            ("card_score",         "SCORE标签+tv_score, 高64dp, 宽按比例"),
            ("card_best",          "BEST标签+tv_best, 高64dp"),
            ("btn_new_game",       "textAppearanceLabelLarge, outlined 样式"),
            ("fl_board_container", "0dp正方形, marginH=16dp, marginTop=16dp"),
            ("grid_board",         "GridLayout 4×4, 内嵌于 fl_board_container"),
            ("tile_cell",          "layout_columnWeight=1, layout_rowWeight=1, margin=4dp"),
            ("v_gesture_overlay",  "透明手势捕获层, match_parent覆盖棋盘"),
        ],
        "spacing": [
            "顶部3个元素 chain: packed, marginH=16dp",
            "棋盘 marginH=16dp, 棋盘内 padding=8dp",
            "瓦片间距: margin=4dp (每格 margin, 棋盘 padding=8dp 产生边框感)",
        ],
        "notes": [
            "瓦片圆角: {tile_corner} (同主题 tile_corner 值)",
            "2值瓦片: textAppearanceTitleLarge, 2048值: textAppearanceHeadlineSmall",
            "瓦片文字色: 低值用暗色, 高值用亮色(见 theme-full-specs.md)",
        ],
    },
    "game_word_search": {
        "title": "Word Search 游戏页 (activity_game_word_search.xml)",
        "layout": "ConstraintLayout 全屏",
        "components": [
            ("tv_level",           "textAppearanceTitleMedium, start对齐"),
            ("tv_timer",           "textAppearanceTitleMedium bold, {p}_score, end对齐"),
            ("fl_grid_container",  "0dp正方形, marginH=8dp"),
            ("grid_letters",       "GridLayout N×N, 程序动态生成 TextView"),
            ("letter_cell",        "正方形, textAppearanceLabelLarge, gravity=center"),
            ("hsv_word_list",      "HorizontalScrollView, 高48dp, 底部"),
            ("ll_word_chips",      "horizontal LinearLayout, Chip样式词条"),
        ],
        "spacing": [
            "grid marginH=8dp (字母格要尽量大)",
            "字母格间距: 2dp",
            "词条 Chip paddingH=12dp, marginEnd=8dp",
        ],
        "notes": [
            "字母格状态: 默认={p}_surface, 选中={p}_highlight, 已找到={p}_correct",
            "已找到的单词 Chip 加删除线效果",
        ],
    },
    "game_matching": {
        "title": "Matching 配对游戏页 (activity_game_matching.xml)",
        "layout": "ConstraintLayout 全屏",
        "components": [
            ("tv_pairs",           "textAppearanceTitleMedium, 'Pairs: 0/8'"),
            ("tv_moves",           "textAppearanceLabelLarge, {p}_on_surface_dim"),
            ("tv_timer",           "textAppearanceTitleMedium bold, {p}_score"),
            ("grid_cards",         "GridLayout 4×4, 卡片正方形"),
            ("card_front",         "FrameLayout 图案/文字面"),
            ("card_back",          "{p}_surface_variant 背景, 图案遮盖"),
        ],
        "spacing": [
            "顶部状态行 marginH=16dp, marginTop=12dp",
            "grid marginH=12dp, 卡片间距6dp",
        ],
        "notes": [
            "翻牌: rotationY 0→90° (消失) + 换内容 + 90→0° (出现), 各150ms",
            "匹配成功: scaleX/Y 1→1.1→1, {p}_correct 边框闪烁",
            "匹配失败: 翻回, 轻微 shakeX 动画",
        ],
    },
    "game_sudoku": {
        "title": "数独游戏页 (activity_game_sudoku.xml)",
        "layout": "ConstraintLayout 全屏",
        "components": [
            ("tv_timer",           "textAppearanceHeadlineSmall bold, {p}_score"),
            ("tv_mistakes",        "textAppearanceLabelLarge, {p}_wrong"),
            ("fl_board",           "0dp正方形, marginH=8dp, 边框1dp {p}_on_surface"),
            ("sudoku_cell",        "正方形, 9×9 GridLayout, 每格TextAppearanceBodyLarge"),
            ("ll_numpad",          "horizontal, 1–9 + 删除, 每键高56dp, 宽均分"),
        ],
        "spacing": [
            "棋盘 marginH=8dp",
            "3×3宫格之间描边2dp, 单格之间描边0.5dp",
            "数字键盘 marginH=16dp, marginTop=12dp",
        ],
        "notes": [
            "预填数字: {p}_on_surface bold; 用户填写: {p}_primary",
            "错误数字: {p}_wrong 背景高亮",
            "选中格: {p}_highlight 背景",
        ],
    },
    "game_over": {
        "title": "游戏结束页 (activity_game_over.xml)",
        "layout": "ConstraintLayout 全屏, 内容居中",
        "components": [
            ("tv_title",           "textAppearanceHeadlineLarge, {p}_primary, 'Game Over' / 'You Win!'"),
            ("star_row",           "3×48dp ImageView 水平排列, marginTop=16dp"),
            ("card_score_summary", "0dp宽, 内含 Your Score + Best Score, 两列"),
            ("btn_play_again",     "240dp×56dp, filled, marginTop=32dp"),
            ("btn_home",           "200dp×48dp, outlined, marginTop=12dp"),
        ],
        "spacing": [
            "内容组 verticalBias=0.45",
            "tv_title marginBottom=12dp",
            "star_row 每星间距8dp",
            "card_score_summary marginH=24dp, marginTop=24dp, padding=20dp",
        ],
        "notes": [
            "胜利: 粒子/星星爆炸动效",
            "失败: 轻微下沉进场动画",
        ],
    },
    "pause": {
        "title": "暂停弹窗 (dialog_pause.xml)",
        "layout": "FrameLayout match_parent ({p}_overlay 半透明) > MaterialCardView 居中",
        "components": [
            ("card_dialog",        "宽280dp, 圆角{corner}, {p}_surface 背景"),
            ("tv_paused",          "textAppearanceHeadlineSmall, center, marginTop=24dp"),
            ("btn_resume",         "0dp宽, 56dp高, filled, marginH=20dp, marginTop=20dp"),
            ("btn_restart",        "0dp宽, 48dp高, outlined, marginH=20dp, marginTop=12dp"),
            ("btn_settings",       "0dp宽, 48dp高, outlined, marginH=20dp, marginTop=8dp"),
            ("btn_home",           "0dp宽, 48dp高, text样式, marginH=20dp, marginBottom=20dp"),
        ],
        "spacing": [
            "弹窗 padding 内: 按钮间距 8–12dp",
            "弹窗与屏幕边缘: 32dp 保证不贴边",
        ],
        "notes": ["点击遮罩区域: 等同 Resume (可选)"],
    },
    "level_complete": {
        "title": "过关弹窗 (dialog_level_complete.xml)",
        "layout": "FrameLayout match_parent ({p}_overlay) > MaterialCardView 居中",
        "components": [
            ("card_dialog",        "宽300dp, 圆角{corner}"),
            ("iv_trophy",          "64dp, {p}_score 色调"),
            ("tv_level_complete",  "textAppearanceHeadlineMedium, {p}_primary"),
            ("star_row",           "3×40dp star, marginV=8dp"),
            ("tv_score",           "textAppearanceHeadlineSmall bold, {p}_score"),
            ("btn_next_level",     "240dp×56dp, filled"),
            ("btn_replay",         "180dp×48dp, outlined, marginTop=8dp"),
        ],
        "spacing": [
            "所有内容 paddingH=20dp, paddingV=24dp",
            "星行 marginV=12dp",
        ],
        "notes": [],
    },
}

# Legacy aliases
SCREEN_ALIASES = {
    "quiz":       "game_quiz",
    "2048":       "game_2048",
    "word":       "game_word_search",
    "main_menu":  "home",
    "game_over_screen": "game_over",
}

SEPARATOR = "─" * 60


def render_constraints(screen_id: str, theme_id: str) -> str:
    t = THEMES[theme_id]
    p = t["prefix"]
    s = SCREENS[screen_id]

    corner    = t["corner"]
    tile_c    = t["tile_corner"]
    elev      = t["elevation"]
    dark      = t["dark"]
    anim      = t["animation"]
    dur       = t["duration"]
    interp    = t["interpolator"]
    font      = t["font"]
    stroke    = t["stroke"]
    elev_rule = "glow/color-overlay (no shadow)" if dark else f"cardElevation={elev}, neutral shadow"

    lines: list[str] = []

    lines.append(f"\n{'═'*60}")
    lines.append(f"  Screen : {s['title']}")
    lines.append(f"  Theme  : {theme_id.replace('_', ' ').title()} ({p}_*)  {'[DARK]' if dark else '[LIGHT]'}")
    lines.append(f"{'═'*60}")

    lines.append(f"\n▸ Layout Structure")
    lines.append(f"  {s['layout']}")

    lines.append(f"\n▸ Components & Sizing")
    for name, spec in s["components"]:
        spec_r = spec.replace("{p}", p).replace("{corner}", corner).replace("{tile_corner}", tile_c)
        lines.append(f"  {name:<28}  {spec_r}")

    lines.append(f"\n▸ Spacing Rules")
    for rule in s["spacing"]:
        lines.append(f"  • {rule}")

    lines.append(f"\n▸ Shape & Stroke")
    lines.append(f"  Button corner radius : {corner}")
    lines.append(f"  Card corner radius   : {corner}")
    lines.append(f"  Tile corner radius   : {tile_c}")
    lines.append(f"  Stroke width         : {stroke}")
    if stroke != "0dp":
        lines.append(f"  Stroke color         : @color/{p}_primary")
    else:
        lines.append(f"  Stroke               : none")

    lines.append(f"\n▸ Elevation & Shadow")
    lines.append(f"  Rule                 : {elev_rule}")
    if not dark:
        lines.append(f"  Button elevation     : {elev}")
        lines.append(f"  Card elevation       : {elev}")
        lines.append(f"  Dialog elevation     : 8dp")

    lines.append(f"\n▸ Typography")
    lines.append(f"  Font family          : {font}")
    if dark:
        lines.append(f"  Title shadow         : shadowColor=@color/{p}_primary, shadowRadius=8")
    if "pixel" in theme_id:
        lines.append(f"  Special              : textAllCaps=true on all buttons")
    if "graffiti" in theme_id:
        lines.append(f"  Special              : textAllCaps=true, letterSpacing=0.08")
    if "midnight" in theme_id or "steampunk" in theme_id:
        lines.append(f"  Special              : letterSpacing=0.05")

    lines.append(f"\n▸ Animation")
    lines.append(f"  Personality          : {anim}")
    lines.append(f"  Duration             : {dur}")
    lines.append(f"  Interpolator         : {interp}")
    lines.append(f"  Answer correct       : {_anim_correct(theme_id, p)}")
    lines.append(f"  Answer wrong         : {_anim_wrong(theme_id, p)}")
    lines.append(f"  Page transition      : {_anim_transition(theme_id)}")

    if s["notes"]:
        lines.append(f"\n▸ Theme-Specific Notes")
        for note in s["notes"]:
            note_r = note.replace("{p}", p).replace("{corner}", corner)
            lines.append(f"  ⚠ {note_r}")

    lines.append(f"\n{'─'*60}")
    lines.append(f"  Full color tokens    : references/theme-full-specs.md (HEX tables only)")
    lines.append(f"  Design rules         : references/design-principles.md (ignore code samples)")
    lines.append(f"  Animation personality: references/animation-guide.md (durations only)")
    lines.append(f"  Output contract      : design-spec markdown ONLY — no app XML/Kotlin")
    lines.append(f"{'─'*60}\n")

    return "\n".join(lines)


def _anim_correct(theme_id: str, p: str) -> str:
    m = {
        "neon_dark":       f"@color/{p}_highlight neon flash ×3, 150ms",
        "space_galaxy":    "slow pulse scaleX/Y 1→1.08→1, 400ms",
        "lava_fire":       "orange burst flash, 100ms shake",
        "midnight_luxury": "gold glow fade, 300ms",
        "deep_sea":        "bioluminescent ripple, 350ms",
        "aurora_night":    "aurora shimmer alpha pulse, 600ms",
        "halloween":       "pumpkin orange flash + shake, 200ms",
        "steampunk":       "brass shimmer, 250ms",
        "graffiti_street": f"@color/{p}_correct instant flash, 100ms",
        "ocean_breeze":    "wave ripple + green flash, 300ms",
        "forest_zen":      "soft green glow expand, 600ms",
        "candy_pop":       "jelly bounce scaleX/Y sequence, 500ms",
        "sakura_spring":   "petal burst particle + pink glow, 400ms",
        "desert_gold":     "gold shimmer + scale 1→1.05→1, 300ms",
        "ice_crystal":     "ice sparkle flash, 300ms",
        "pastel_dream":    "rainbow shimmer fade, 700ms",
        "christmas":       "snowflake confetti burst, 500ms",
        "pixel_classic":   "instant color swap (no anim), 0ms",
        "cartoon_fun":     "big jelly bounce scaleX/Y, 500ms OvershootInterpolator(3f)",
        "minimalist_white":"subtle scale 1→1.03→1, 400ms",
        "paper_craft":     "paper fold ripple, 350ms",
        "neon_synthwave":  f"@color/{p}_secondary cyan flash ×3, 120ms",
        "noir_cinema":     "white flash then red accent blink, 250ms",
        "cyber_mint":      f"@color/{p}_primary terminal blink ×2, 100ms",
        "ember_coal":      "ember spark flash + scale 1→1.06→1, 180ms",
        "matcha_cafe":     "soft green steam rise, 600ms",
        "coral_reef":      "bubble pop scale overshoot, 450ms",
        "honey_amber":     "honey drip glow, 300ms",
        "sunset_plaza":    "warm gold flare, 280ms",
        "cyberpunk_city":  f"@color/{p}_secondary pink flash ×2, 120ms",
        "pirate_cove":     "gold coin shimmer, 280ms",
        "royal_velvet":    "crown gold glow fade, 300ms",
        "industrial_steel":"warning-orange strobe, 120ms",
        "night_market":    "lantern warm flare, 350ms",
        "moonlit_garden":  "moonbeam soft pulse, 600ms",
        "tropical_fruit":  "juice splash overshoot, 450ms",
        "bubble_tea":      "pearl bounce soft, 500ms",
        "farm_cottage":    "leaf green expand, 600ms",
        "cloud_sky":       "cloud puff scale, 400ms",
        "lavender_fields": "lavender haze fade, 650ms",
        "citrus_fresh":    "citrus zest pop, 400ms",
        "crystal_gem":     "facet sparkle flash, 300ms",
        "clay_stopmotion": "clay squash stretch, 480ms",
        "board_game_table":"wood chip settle, 300ms",
        "comic_halftone":  f"@color/{p}_score star burst, 100ms",
        "ink_wash":        "ink blot expand, 550ms",
        "retro_poster":    "poster stamp slam, 250ms",
        "jungle_adventure":"leaf burst flash, 200ms",
        "snow_festival":   "snowflake confetti, 500ms",
        "arcade_cabinet":  f"@color/{p}_primary CRT flash, 0ms cut",
    }
    return m.get(theme_id, "scale pulse 1→1.08→1, 400ms")


def _anim_wrong(theme_id: str, p: str) -> str:
    m = {
        "neon_dark":       "shakeX ±20dp, 400ms linear",
        "space_galaxy":    "slow fade-to-red, 300ms",
        "lava_fire":       "full-screen red flash + shakeX, 200ms",
        "midnight_luxury": "subtle shakeX ±10dp, 300ms",
        "deep_sea":        "red warning ripple, 350ms",
        "aurora_night":    "red alpha pulse, 400ms",
        "halloween":       "purple flash + shakeX, 300ms",
        "steampunk":       "shakeX ±8dp, 250ms",
        "graffiti_street": f"@color/{p}_wrong instant flash, 100ms",
        "ocean_breeze":    "red wave, shakeX ±12dp, 300ms",
        "forest_zen":      "gentle shakeX ±8dp, 500ms",
        "candy_pop":       "sad bounce scaleY squeeze, 400ms",
        "sakura_spring":   "wilted petal droop + shakeX, 400ms",
        "desert_gold":     "shakeX ±10dp, 300ms",
        "ice_crystal":     "ice crack flash, shakeX ±12dp, 300ms",
        "pastel_dream":    "soft shakeX ±8dp, 500ms",
        "christmas":       "coal-black flash, shakeX, 300ms",
        "pixel_classic":   "instant wrong color (no anim), 0ms",
        "cartoon_fun":     "big sad shakeX ±20dp, 500ms",
        "minimalist_white":"shakeX ±6dp, 300ms",
        "paper_craft":     "paper scrunch shakeX, 350ms",
        "neon_synthwave":  f"@color/{p}_wrong red flash + shakeX, 120ms",
        "noir_cinema":     "hard cut to red frame, shakeX ±6dp, 250ms",
        "cyber_mint":      "red cursor glitch shakeX, 120ms",
        "ember_coal":      "coal spark red flash + shakeX, 180ms",
        "matcha_cafe":     "gentle shakeX ±8dp, 500ms",
        "coral_reef":      "deflate scaleY + red tint, 400ms",
        "honey_amber":     "shakeX ±10dp, 300ms",
        "sunset_plaza":    "warm red wash + shakeX, 280ms",
        "cyberpunk_city":  "glitch shakeX + red, 150ms",
        "pirate_cove":     "shakeX ±12dp, 280ms",
        "royal_velvet":    "subtle shakeX ±8dp, 300ms",
        "industrial_steel":"alarm red flash + shake, 150ms",
        "night_market":    "lantern red wash + shake, 300ms",
        "moonlit_garden":  "soft red pulse, 500ms",
        "tropical_fruit":  "deflate bounce, 400ms",
        "bubble_tea":      "straw wobble shakeX, 450ms",
        "farm_cottage":    "gentle shakeX ±8dp, 500ms",
        "cloud_sky":       "cloud scatter shake, 400ms",
        "lavender_fields": "soft shakeX ±8dp, 550ms",
        "citrus_fresh":    "sour squeeze shake, 350ms",
        "crystal_gem":     "crack flash + shakeX, 280ms",
        "clay_stopmotion": "clay flatten shake, 450ms",
        "board_game_table":"tile rattle shakeX, 300ms",
        "comic_halftone":  f"@color/{p}_wrong POW flash, 100ms",
        "ink_wash":        "ink splash shake, 500ms",
        "retro_poster":    "stamp reject shake, 250ms",
        "jungle_adventure":"vine whip shakeX, 200ms",
        "snow_festival":   "frost red flash + shake, 350ms",
        "arcade_cabinet":  "instant wrong palette swap, 0ms",
    }
    return m.get(theme_id, "shakeX ±15dp, 400ms")


def _anim_transition(theme_id: str) -> str:
    m = {
        "neon_dark":       "alpha fade 100ms in/out",
        "space_galaxy":    "slide-up + fade, 350ms decelerate",
        "lava_fire":       "slide-right wipe, 200ms linear",
        "midnight_luxury": "cross-fade, 250ms",
        "deep_sea":        "fade + scale 0.95→1, 350ms",
        "aurora_night":    "slow fade, 600ms",
        "halloween":       "swipe-left, 200ms linear",
        "steampunk":       "cross-fade, 250ms",
        "graffiti_street": "instant cut (no transition), 0ms",
        "ocean_breeze":    "slide-up, 300ms AccelerateDecelerate",
        "forest_zen":      "gentle fade, 600ms",
        "candy_pop":       "slide-up + overshoot, 450ms",
        "sakura_spring":   "petal-drift slide-up, 400ms",
        "desert_gold":     "cross-fade, 300ms",
        "ice_crystal":     "frost-slide from top, 300ms",
        "pastel_dream":    "soft fade, 600ms",
        "christmas":       "snow-slide down, 400ms",
        "pixel_classic":   "instant cut, 0ms",
        "cartoon_fun":     "bounce slide-up, 500ms",
        "minimalist_white":"fade, 400ms",
        "paper_craft":     "page-flip slide, 350ms",
        "neon_synthwave":  "scan-line wipe, 120ms",
        "noir_cinema":     "hard cut / iris cross-fade, 250ms",
        "cyber_mint":      "terminal scroll-up, 100ms",
        "ember_coal":      "ember wipe-up, 180ms",
        "matcha_cafe":     "soft fade, 600ms",
        "coral_reef":      "bubble slide-up + overshoot, 450ms",
        "honey_amber":     "cross-fade, 300ms",
        "sunset_plaza":    "horizon slide-up, 300ms",
        "cyberpunk_city":  "scan-line wipe, 120ms",
        "pirate_cove":     "cross-fade, 280ms",
        "royal_velvet":    "curtain fade, 300ms",
        "industrial_steel":"hard cut / wipe, 150ms",
        "night_market":    "lantern fade-up, 350ms",
        "moonlit_garden":  "soft moon fade, 600ms",
        "tropical_fruit":  "slide-up + overshoot, 450ms",
        "bubble_tea":      "soft fade, 500ms",
        "farm_cottage":    "gentle fade, 600ms",
        "cloud_sky":       "float fade-up, 400ms",
        "lavender_fields": "soft fade, 600ms",
        "citrus_fresh":    "slide-up, 350ms",
        "crystal_gem":     "facet cross-fade, 300ms",
        "clay_stopmotion": "frame-step slide, 450ms",
        "board_game_table":"page-slide, 300ms",
        "comic_halftone":  "panel cut, 100ms",
        "ink_wash":        "brush wipe, 550ms",
        "retro_poster":    "poster flip, 250ms",
        "jungle_adventure":"vine wipe, 200ms",
        "snow_festival":   "snow-slide down, 400ms",
        "arcade_cabinet":  "instant cut, 0ms",
    }
    return m.get(theme_id, "fade, 300ms")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print design constraints for a screen + theme combination."
    )
    parser.add_argument("--screen", help="Screen ID")
    parser.add_argument("--theme", default="neon_dark", help="Theme ID (default: neon_dark)")
    parser.add_argument("--list-screens", action="store_true")
    parser.add_argument("--list-themes", action="store_true")
    args = parser.parse_args(argv)

    if args.list_screens:
        print(f"\n{'ID':<22} Title")
        print("─" * 55)
        for sid, s in SCREENS.items():
            print(f"  {sid:<22} {s['title']}")
        print(f"\n  Aliases: {', '.join(SCREEN_ALIASES.keys())}")
        return 0

    if args.list_themes:
        print(f"\n{'ID':<22} Corner   Anim")
        print("─" * 60)
        for tid, t in THEMES.items():
            mode = "DARK " if t["dark"] else "LIGHT"
            print(f"  {tid:<22} {t['corner']:<8} {mode}  {t['animation']}")
        return 0

    if not args.screen:
        parser.print_help()
        return 1

    screen = SCREEN_ALIASES.get(args.screen, args.screen)
    if screen not in SCREENS:
        print(f"ERROR: unknown screen '{args.screen}'. Use --list-screens.", file=sys.stderr)
        return 1

    theme = args.theme
    if theme not in THEMES:
        print(f"ERROR: unknown theme '{theme}'. Use --list-themes.", file=sys.stderr)
        return 1

    print(render_constraints(screen, theme))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
