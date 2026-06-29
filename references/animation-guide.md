# Animation Guide — 7种动画基调 Kotlin 实现

## 基调一：Fast & Electric（霓虹暗黑、合成波）

**特点**：快速、闪烁、电流感，duration ≤ 150ms

```kotlin
// 答对闪烁效果 — neon cyan 闪烁3次
fun animateCorrect(view: View, glowColor: Int) {
    val originalBg = view.background
    val flashAnim = ObjectAnimator.ofArgb(
        view, "backgroundColor", glowColor, Color.TRANSPARENT
    ).apply {
        duration = 150
        repeatCount = 3
        repeatMode = ValueAnimator.REVERSE
        interpolator = LinearInterpolator()
    }
    flashAnim.start()
}

// 按钮按压 — 瞬间缩小弹回
fun applyElectricButtonAnim(button: View) {
    button.setOnTouchListener { v, event ->
        when (event.action) {
            MotionEvent.ACTION_DOWN -> v.animate().scaleX(0.94f).scaleY(0.94f).setDuration(80).start()
            MotionEvent.ACTION_UP, MotionEvent.ACTION_CANCEL ->
                v.animate().scaleX(1f).scaleY(1f).setDuration(80).start()
        }
        false
    }
}

// 页面转场 — 快速淡入
fun transitionFast(outView: View, inView: View) {
    outView.animate().alpha(0f).setDuration(100).start()
    inView.alpha = 0f
    inView.visibility = View.VISIBLE
    inView.animate().alpha(1f).setDuration(100).setStartDelay(80).start()
}
```

---

## 基调二：Smooth & Floating（星际宇宙、极光暗夜）

**特点**：慢速、漂浮、惯性感，duration 250–400ms

```kotlin
// 浮动进场动画
fun animateFloatIn(view: View) {
    view.translationY = 60f
    view.alpha = 0f
    view.visibility = View.VISIBLE
    view.animate()
        .translationY(0f)
        .alpha(1f)
        .setDuration(350)
        .setInterpolator(DecelerateInterpolator(2f))
        .start()
}

// 瓦片合并 — 漂浮膨胀感
fun animateTileMerge(tile: View) {
    tile.animate()
        .scaleX(1.15f).scaleY(1.15f)
        .setDuration(150)
        .setInterpolator(DecelerateInterpolator())
        .withEndAction {
            tile.animate()
                .scaleX(1f).scaleY(1f)
                .setDuration(200)
                .setInterpolator(AccelerateDecelerateInterpolator())
                .start()
        }.start()
}

// 答题结果 — 缓慢脉冲
fun animateCorrectPulse(view: View, color: Int) {
    ValueAnimator.ofFloat(1f, 1.08f, 1f).apply {
        duration = 400
        interpolator = AccelerateDecelerateInterpolator()
        addUpdateListener { view.scaleX = it.animatedValue as Float; view.scaleY = it.animatedValue as Float }
        start()
    }
}
```

---

## 基调三：Bouncy & Playful（糖果缤纷、樱花春日、梦幻粉彩）

**特点**：弹跳、果冻感，使用弹性插值器

```kotlin
// 自定义弹跳插值器
class BounceEaseOutInterpolator : Interpolator {
    override fun getInterpolation(t: Float): Float {
        return when {
            t < 1 / 2.75f -> 7.5625f * t * t
            t < 2 / 2.75f -> { val t2 = t - 1.5f / 2.75f; 7.5625f * t2 * t2 + 0.75f }
            t < 2.5 / 2.75f -> { val t2 = t - 2.25f / 2.75f; 7.5625f * t2 * t2 + 0.9375f }
            else -> { val t2 = t - 2.625f / 2.75f; 7.5625f * t2 * t2 + 0.984375f }
        }
    }
}

// 按钮弹跳进场
fun animateBounceIn(view: View) {
    view.scaleX = 0f
    view.scaleY = 0f
    view.visibility = View.VISIBLE
    view.animate()
        .scaleX(1f).scaleY(1f)
        .setDuration(500)
        .setInterpolator(BounceEaseOutInterpolator())
        .start()
}

// 答对 — 果冻弹跳庆祝
fun animateCelebrate(view: View) {
    val bounceX = ObjectAnimator.ofFloat(view, "scaleX", 1f, 1.3f, 0.9f, 1.1f, 1f)
    val bounceY = ObjectAnimator.ofFloat(view, "scaleY", 1f, 0.7f, 1.1f, 0.95f, 1f)
    AnimatorSet().apply {
        playTogether(bounceX, bounceY)
        duration = 500
        start()
    }
}
```

---

## 基调四：Dramatic & Intense（熔岩火焰、万圣节）

**特点**：剧烈、摇晃、屏幕震动，duration 100–200ms

```kotlin
// 屏幕摇晃（答错）
fun shakeView(view: View) {
    val shake = ObjectAnimator.ofFloat(
        view, "translationX",
        0f, -20f, 20f, -15f, 15f, -10f, 10f, -5f, 5f, 0f
    ).apply {
        duration = 400
        interpolator = LinearInterpolator()
    }
    shake.start()
}

// 屏幕红色闪烁（生命减少）
fun flashError(rootView: View) {
    val overlay = View(rootView.context).apply {
        setBackgroundColor(Color.parseColor("#80FF0000"))
        layoutParams = ViewGroup.LayoutParams(MATCH_PARENT, MATCH_PARENT)
    }
    (rootView as? ViewGroup)?.addView(overlay)
    overlay.animate().alpha(0f).setDuration(300).withEndAction {
        (rootView as? ViewGroup)?.removeView(overlay)
    }.start()
}

// 按钮按压 — 猛力下沉
fun applyIntenseButtonAnim(button: View) {
    button.setOnTouchListener { v, event ->
        when (event.action) {
            MotionEvent.ACTION_DOWN -> {
                v.animate().scaleX(0.88f).scaleY(0.88f).translationZ(-4f).setDuration(100).start()
            }
            MotionEvent.ACTION_UP -> {
                v.animate().scaleX(1f).scaleY(1f).translationZ(0f).setDuration(150)
                    .setInterpolator(OvershootInterpolator(3f)).start()
            }
        }
        false
    }
}
```

---

## 基调五：Instant Snap（像素复古）

**特点**：无过渡，0ms，完全像素跳变风格

```kotlin
// 像素风格：禁用所有动画
fun disableAllAnimations(activity: Activity) {
    val window = activity.window
    window.setWindowAnimations(0)
}

// 瓦片更新 — 瞬间切换背景色，无动画
fun updateTileInstant(tile: TextView, value: Int, colors: Map<Int, Int>) {
    tile.text = if (value == 0) "" else value.toString()
    tile.setBackgroundColor(colors[value] ?: Color.GRAY)
    // 故意不加动画
}

// 答题结果 — 颜色瞬变
fun flashCorrectInstant(button: View, originalColor: Int, correctColor: Int) {
    button.setBackgroundColor(correctColor)
    Handler(Looper.getMainLooper()).postDelayed({
        button.setBackgroundColor(originalColor)
    }, 500) // 只停留500ms，无过渡
}
```

---

## 基调六：Gentle & Breathing（森林禅意）

**特点**：呼吸感，缓慢淡入淡出，duration 500–800ms

```kotlin
// 呼吸动画（主界面Logo或背景装饰）
fun startBreathingAnimation(view: View) {
    val breathe = ObjectAnimator.ofFloat(view, "alpha", 0.7f, 1.0f).apply {
        duration = 2000
        repeatCount = ObjectAnimator.INFINITE
        repeatMode = ObjectAnimator.REVERSE
        interpolator = AccelerateDecelerateInterpolator()
    }
    breathe.start()
}

// 页面进场 — 从下方缓慢升起
fun animateSlideUpGentle(view: View) {
    view.translationY = 40f
    view.alpha = 0f
    view.visibility = View.VISIBLE
    view.animate()
        .translationY(0f)
        .alpha(1f)
        .setDuration(600)
        .setInterpolator(AccelerateDecelerateInterpolator())
        .start()
}

// 答对 — 柔光扩散
fun animateCorrectGlow(view: View) {
    ValueAnimator.ofFloat(0f, 1f, 0f).apply {
        duration = 800
        addUpdateListener {
            val alpha = (it.animatedValue as Float * 255).toInt()
            view.background?.alpha = alpha
        }
        start()
    }
}
```

---

## 基调七：Festive & Sparkling（圣诞、万圣节）

**特点**：闪光粒子、彩色爆炸，适合节日主题

```kotlin
// 简易粒子爆炸（答对庆祝）
class ConfettiView(context: Context) : View(context) {
    private val particles = mutableListOf<Particle>()
    private val colors = intArrayOf(
        Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.MAGENTA
    )
    private val paint = Paint()
    private val random = Random()
    private var animating = false

    data class Particle(
        var x: Float, var y: Float,
        var vx: Float, var vy: Float,
        val color: Int, val size: Float,
        var alpha: Int = 255, var rotation: Float = 0f
    )

    fun burst(originX: Float, originY: Float) {
        particles.clear()
        repeat(30) {
            particles.add(Particle(
                x = originX, y = originY,
                vx = (random.nextFloat() - 0.5f) * 20f,
                vy = (random.nextFloat() - 1f) * 15f,
                color = colors[random.nextInt(colors.size)],
                size = random.nextFloat() * 12f + 6f
            ))
        }
        animating = true
        animate()
    }

    private fun animate() {
        if (!animating) return
        particles.forEach { p ->
            p.x += p.vx; p.vy += 0.5f; p.y += p.vy
            p.alpha = (p.alpha - 5).coerceAtLeast(0)
            p.rotation += 5f
        }
        if (particles.all { it.alpha == 0 }) { animating = false; return }
        invalidate()
        postDelayed(::animate, 16)
    }

    override fun onDraw(canvas: Canvas) {
        particles.forEach { p ->
            paint.color = p.color; paint.alpha = p.alpha
            canvas.drawRect(p.x, p.y, p.x + p.size, p.y + p.size, paint)
        }
    }
}
```
