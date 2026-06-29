# Screen Layouts — 所有页面布局规范

所有布局均适配任意主题，颜色引用 `@color/{theme_prefix}_*`，尺寸引用 `@dimen/game_*`。

---

## 页面总览

| 类别 | 页面 | 文件名 |
|------|------|--------|
| App Shell | 首页 | `activity_home.xml` |
| App Shell | 历史页 | `activity_history.xml` |
| App Shell | 统计页 | `activity_statistics.xml` |
| App Shell | 设置页 | `activity_settings.xml` |
| App Shell | 玩法说明 | `activity_how_to_play.xml` |
| App Shell | 排行榜 | `activity_leaderboard.xml` |
| App Shell | 新手引导 | `activity_onboarding.xml` |
| 游戏页 | Quiz / 答题 | `activity_game_quiz.xml` |
| 游戏页 | 2048 | `activity_game_2048.xml` |
| 游戏页 | Puzzle 拼图 | `activity_game_puzzle.xml` |
| 游戏页 | Word Search | `activity_game_word_search.xml` |
| 游戏页 | Matching 配对 | `activity_game_matching.xml` |
| 游戏页 | Sudoku 数独 | `activity_game_sudoku.xml` |
| 结果/弹层 | 游戏结束 | `activity_game_over.xml` |
| 结果/弹层 | 暂停弹窗 | `dialog_pause.xml` |
| 结果/弹层 | 过关弹窗 | `dialog_level_complete.xml` |

---

## 首页 — activity_home.xml

**结构**：CoordinatorLayout > ConstraintLayout + BottomNavigationView

**关键视图**：`iv_logo`(140dp) · `tv_app_name`(HeadlineMedium) · `tv_tagline`(BodyMedium) ·
`card_daily_challenge`(可隐藏) · `btn_play`(240dp×56dp) · `tv_last_score` · `bottom_nav`

**Bottom Nav 菜单**（`res/menu/bottom_nav_menu.xml`）：Home · History · Stats · Settings

**verticalBias**：logo=0.22，PLAY 按钮在页面中下方

---

## 历史页 — activity_history.xml

**结构**：CoordinatorLayout > Toolbar + LinearLayout(ChipGroup + RecyclerView/EmptyState) + BottomNav

**筛选 Chips**：All · Won · Lost · Best Scores（`ChipGroup` singleSelection）

**RecyclerView item** `item_history_row.xml`：
- `iv_game_icon`(36dp) · `tv_game_type`(TitleSmall) · `tv_date`(LabelSmall) ·
  `tv_score`(TitleMedium bold, `{p}_score`) · `tv_duration`(LabelSmall) ·
  `chip_difficulty`(Easy/Medium/Hard) · `chip_result`(WIN绿/LOSE红)

**空状态**：大图标(80dp) + "No games yet. Start playing!" + `btn_play_now`

---

## 统计页 — activity_statistics.xml

**结构**：CoordinatorLayout > Toolbar + NestedScrollView(LinearLayout) + BottomNav

**KPI 行**：4 张卡片水平链（Total Games · Best Score · Win Rate · Streak），高度 `game_kpi_card_height`(80dp)
- 每卡：`tv_kpi_value`(HeadlineSmall bold, `{p}_score`) + `tv_kpi_label`(LabelSmall dim)

**图表区**：`card_chart`(高度200dp)内含 `chart_area` View（接 MPAndroidChart）

**游戏分类**：`ll_game_breakdown` LinearLayout，按游戏类型逐行展示

**成就区**：`grid_achievements` GridLayout 4列

---

## 设置页 — activity_settings.xml

**结构**：CoordinatorLayout > Toolbar + NestedScrollView(LinearLayout) + BottomNav

**分组**（每组前有 Section Header `{p}_primary` 色小标题）：
- **AUDIO**：Sound Effects · Background Music · Vibration（`SwitchMaterial`）
- **APPEARANCE**：5主题 RadioGroup，每行 RadioButton + 主题名 + 16dp 色块预览圆
- **GAMEPLAY**：Difficulty（Easy/Medium/Hard RadioGroup）· Timer Switch
- **DATA**：`btn_reset`（outlined，`{p}_wrong` 色）· 底部 `tv_version`

---

## 玩法说明页 — activity_how_to_play.xml

**变体 A（复杂游戏：2048/数独/拼图）**：ViewPager2 + TabLayout 点状指示器 + btn_skip + btn_next
- 每个 slide：`iv_tutorial_image`(280dp) + `tv_slide_title`(HeadlineSmall) + `tv_slide_desc`(BodyMedium)
- 最后一页 btn_next 变为"GOT IT!"

**变体 B（简单游戏：quiz/matching）**：NestedScrollView + 步骤卡片 × N + `btn_start_playing`
- 每张卡：步骤圆形编号(32dp) + `tv_step_title`(TitleMedium) + `tv_step_desc`(BodyMedium)

---

## Quiz 游戏页 — activity_game_quiz.xml

**结构**：ConstraintLayout

**关键视图（从上到下）**：
1. `LinearProgressIndicator` pb_progress（全宽，顶部）
2. `ibtn_pause`(40dp) + `tv_question_number` + `tv_timer`(HeadlineSmall, `{p}_score`)
3. `card_question`(minHeight=120dp)内 `tv_question`(TitleMedium, center gravity)
4. `btn_answer_a/b/c/d`(0dp宽, 56dp高, 间距12dp, gravity=start)

**答案按钮状态色**（StateListDrawable）：默认=surface · 答对=correct · 答错=wrong

---

## 2048 游戏页 — activity_game_2048.xml

**结构**：ConstraintLayout

**顶部行**：`card_score`(SCORE/tv_score) · `card_best`(BEST/tv_best) · `btn_new_game`

**棋盘**：`fl_board_container`(0dp正方形, 16dp边距) > `grid_board`(GridLayout 4×4) + `v_gesture_overlay`

**瓦片**：每格 TextView，`app:layout_columnWeight="1"`, `app:layout_rowWeight="1"`, `margin=4dp`

**手势 Kotlin**：GestureDetector.SimpleOnGestureListener 检测 onFling，|dx|>100 或 |dy|>100 触发方向

---

## Word Search 游戏页 — activity_game_word_search.xml

**结构**：ConstraintLayout

**顶部**：`tv_level`(start) + `tv_timer`(end)

**字母格**：`fl_grid_container`(0dp正方形) > `grid_letters`(GridLayout NxN，程序动态生成 TextView)

**单词列表**：底部 `HorizontalScrollView` > `ll_word_list`(horizontal LinearLayout，词语 Chip 样式)

**字母格背景**（StateListDrawable）：默认=surface · selected=highlight · activated=correct

---

## Matching 配对游戏页 — activity_game_matching.xml

**结构**：ConstraintLayout

**顶部**：`tv_pairs`("Pairs: 0/8") + `tv_moves` + `tv_timer`

**卡片格**：`grid_cards`(GridLayout 4×4，卡片翻转动画用 rotationY 180°)

**每张卡**：前面(FrameLayout 图案) + 背面(FrameLayout 卡背颜色)，`card_flip` 动画

---

## 游戏结束页 — activity_game_over.xml

**关键视图**：`tv_game_over_title`(HeadlineLarge, `{p}_primary`) · 星星行(3×48dp ImageView) ·
`card_score_summary`(Your Score / Best Score) · `btn_play_again`(240dp) · `btn_home`(outlined 200dp)

---

## 暂停弹窗 — dialog_pause.xml

**结构**：FrameLayout(match_parent, `{p}_overlay`) > MaterialCardView(280dp, center) > LinearLayout
- Resume · Restart · Settings · Home（最后两个用 outlined 样式）

---

## 通用尺寸 (res/values/dimens_game.xml)

```xml
<resources>
    <dimen name="game_padding_screen">16dp</dimen>
    <dimen name="game_padding_card">12dp</dimen>
    <dimen name="game_button_height">56dp</dimen>
    <dimen name="game_button_height_secondary">48dp</dimen>
    <dimen name="game_bottom_nav_height">56dp</dimen>
    <dimen name="game_toolbar_height">56dp</dimen>
    <dimen name="game_tile_2048">72dp</dimen>
    <dimen name="game_tile_gap">8dp</dimen>
    <dimen name="game_logo_size">140dp</dimen>
    <dimen name="game_kpi_card_height">80dp</dimen>
    <dimen name="game_chart_height">200dp</dimen>
    <dimen name="game_star_size">48dp</dimen>
    <dimen name="game_step_number_size">32dp</dimen>
    <dimen name="game_score_text">24sp</dimen>
    <dimen name="game_question_text">20sp</dimen>
    <dimen name="game_answer_text">16sp</dimen>
    <dimen name="game_timer_text">28sp</dimen>
</resources>
```
