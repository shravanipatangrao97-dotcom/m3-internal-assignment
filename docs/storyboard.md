# Six-Scene Storyboard Specification

**Project:** The Derivative — From Secant to Tangent  
**Student:** Shravani Patil  
**Subject:** Linear Algebra and Calculus (M3)  
**Total Target Runtime:** ~4 minutes 45 seconds  

---

### Scene 1: The Hook — Speed at an Instant
- **Scene Number:** 1
- **Title:** The Paradox of Instantaneous Speed
- **Duration:** 35 seconds
- **Objective:** Provoke mathematical curiosity by contrasting average speed over a time interval with instantaneous speed at an exact instant.
- **Visual Description:**
  - Dark navy elegant coordinate canvas.
  - An animated object moving along a trajectory with a dynamic velocity vector.
  - Floating thought-provoking questions: *"How fast is something moving at one exact instant?"*
  - Revealing the dilemma $\frac{\Delta s}{\Delta t} \to \frac{0}{0}$.
  - Transition towards coordinate axes establishing the mathematical model.
- **Mathematical Content:**
  - Average velocity: $v_{\text{avg}} = \frac{\Delta s}{\Delta t}$
  - Instantaneous paradox: as $\Delta t \to 0$, ratio approaches $\frac{0}{0}$.
- **Narration Summary:** Speed is distance over time, but at an instant, elapsed time is zero. Calculus resolves this paradox via limits.

---

### Scene 2: Understanding the Concept — Average vs. Instantaneous
- **Scene Number:** 2
- **Title:** The Secant Line and Average Rate of Change
- **Duration:** 45 seconds
- **Objective:** Establish the geometric model of the curve $f(x) = x^2$ and formulate the secant line slope.
- **Visual Description:**
  - Cartesian coordinate axes with clear grid lines.
  - Smooth drawing of the parabolic curve $y = x^2$ in electric blue.
  - Placement of point $P(x_1, f(x_1))$ and point $Q(x_2, f(x_2))$.
  - Secant line drawn in vibrant orange connecting $P$ and $Q$.
  - Slope triangle illustrating $\Delta x = x_2 - x_1$ and $\Delta y = f(x_2) - f(x_1)$.
  - Average rate of change equation card appearing clearly.
- **Mathematical Content:**
  - Curve: $f(x) = x^2$
  - Slope formula: $m_{\text{sec}} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$
- **Narration Summary:** To measure change, we compare two points. The connecting line is a secant, and its slope is the average rate of change.

---

### Scene 3: Secant to Tangent — The Limiting Process
- **Scene Number:** 3
- **Title:** Geometric Convergence: From Secant to Tangent
- **Duration:** 60 seconds
- **Objective:** Provide visual and intuitive proof of the secant line converging to the tangent line as the horizontal offset $h$ tends to zero.
- **Visual Description:**
  - Graph centered at $P(2, 4)$ in cyan/white.
  - Point $Q(2+h, (2+h)^2)$ animated in orange, stepping through positive $h$ values: $h = 2.0, 1.0, 0.5, 0.2, 0.1$.
  - Secant line continuously updating its angle and position.
  - Dynamic slope readout updating in real-time ($6.0 \to 5.0 \to 4.5 \to 4.2 \to 4.1$).
  - As $h \to 0$, the secant line transforms seamlessly into the green tangent line $y = 4x - 4$.
  - Tangent slope labeled prominently as $m = 4$.
- **Mathematical Content:**
  - $h = 2.0 \implies m_{\text{sec}} = 6.0$
  - $h = 1.0 \implies m_{\text{sec}} = 5.0$
  - $h = 0.5 \implies m_{\text{sec}} = 4.5$
  - $h = 0.2 \implies m_{\text{sec}} = 4.2$
  - $h = 0.1 \implies m_{\text{sec}} = 4.1$
  - Tangent line: $y = 4x - 4$, with $m = 4$.
- **Narration Summary:** Bringing $Q$ closer to $P$ rotates the secant line until it matches the slope of the curve at $P$, becoming the tangent.

---

### Scene 4: Worked Derivation — Step-by-Step Algebra
- **Scene Number:** 4
- **Title:** Analytical Derivation: Limit of the Difference Quotient
- **Duration:** 70 seconds
- **Objective:** Rigorously derive $f'(2) = 4$ through algebraic expansion and limit evaluation without skipping steps.
- **Visual Description:**
  - Focused, distraction-free derivation layout with pristine mathematical typography.
  - Step 1: Definition of derivative $f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$.
  - Step 2: Evaluation of $f(2) = 4$ and $f(2+h) = (2+h)^2 = 4 + 4h + h^2$.
  - Step 3: Difference quotient setup $\frac{(4 + 4h + h^2) - 4}{h}$.
  - Step 4: Cancellation of $4$ and $-4$, leaving $\frac{4h + h^2}{h}$.
  - Step 5: Factoring $h(4+h)/h$ and highlighting the algebraic rule $h \neq 0$.
  - Step 6: Simplified quotient $(4 + h)$.
  - Step 7: Limit evaluation as $h \to 0 \implies 4 + 0 = 4$.
  - Result highlighted with green rounded focus box: $f'(2) = 4$.
- **Mathematical Content:**
  - $f'(2) = \lim_{h \to 0} \frac{f(2+h) - f(2)}{h} = \lim_{h \to 0} \frac{4h+h^2}{h} = \lim_{h \to 0}(4+h) = 4$.
- **Narration Summary:** Each algebraic step confirms our geometric observation. Cancelling $h$ is justified because $h$ approaches zero but is not zero.

---

### Scene 5: Geometric Interpretation — What Does the Answer Mean?
- **Scene Number:** 5
- **Title:** Physical & Geometric Meaning of the Derivative
- **Duration:** 45 seconds
- **Objective:** Reconnect the algebraic calculation back to the geometry of the curve and the physical concept of instantaneous rate.
- **Visual Description:**
  - Close-up view of the parabola $y = x^2$ around $P(2, 4)$.
  - Bold green tangent line $y = 4x - 4$ extending through the frame.
  - Right-angled slope triangle with run $= 1$ and rise $= 4$, emphasizing steepness.
  - Direct comparison visual showing the secant line (two points, average rate) versus tangent line (one point, instantaneous rate).
- **Mathematical Content:**
  - Point-slope form: $y - 4 = 4(x - 2) \implies y = 4x - 4$.
  - Derivative $f'(2) = 4 \iff$ slope of tangent at $x = 2$.
- **Narration Summary:** The value $4$ is the exact instantaneous rate of change and the slope of the unique tangent line touching $(2,4)$.

---

### Scene 6: Summary and Credits — Takeaways & Attribution
- **Scene Number:** 6
- **Title:** Core Takeaways and Project Credits
- **Duration:** 35 seconds
- **Objective:** Consolidate the core mathematical principles and provide complete academic and project attribution.
- **Visual Description:**
  - Three structured takeaway cards:
    1. Secant Line: Average rate of change over an interval.
    2. Tangent Line: Instantaneous rate of change at a point.
    3. Derivative: The limiting value of difference quotients.
  - Prominent banner: $f'(2) = 4$.
  - Memorable closing line: *"From two points to one tangent. That is the idea behind the derivative."*
  - Comprehensive credits card:
    - Student: Shravani Patil
    - Subject: Linear Algebra and Calculus (M3)
    - Institution: University Internal Assessment
    - References: Stewart, Thomas, 3Blue1Brown
    - AI Tools Disclosure: Antigravity (Gemini)
- **Mathematical Content:**
  - Summary of $f'(2) = \lim_{h \to 0} \frac{\Delta y}{\Delta x} = 4$.
- **Narration Summary:** Recap of the three pillars of differential calculus, with closing acknowledgment.
