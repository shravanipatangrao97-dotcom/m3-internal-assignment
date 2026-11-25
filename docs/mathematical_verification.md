# Mathematical Verification Document

**Project:** The Derivative — From Secant to Tangent  
**Student:** Shravani Patil  
**Course:** Linear Algebra and Calculus (M3)  
**Target Topic:** Transition from Average Rate of Change to Instantaneous Rate of Change  

---

## 1. Mathematical Objective

The goal of this project is to rigorously demonstrate and visualize how the average rate of change between two points on a smooth curve converges to the instantaneous rate of change (the derivative) at a single point via a limit process.

We investigate the standard quadratic function:
$$f(x) = x^2$$

Specifically, we compute and interpret the derivative at the point:
$$a = 2$$

---

## 2. Theoretical Derivation

### Step 1: Average Rate of Change (Secant Slope)
For any function $f(x)$ over an interval $[x_1, x_2]$, the average rate of change is defined as the ratio of the change in output to the change in input:
$$\text{Average Rate of Change} = \frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

Geometrically, this quotient is the slope $m_{\text{sec}}$ of the secant line passing through points $P(x_1, f(x_1))$ and $Q(x_2, f(x_2))$.

### Step 2: Parametrization with Offset $h$
Let:
- $x_1 = 2$
- $x_2 = 2 + h$, where $h \neq 0$ represents the horizontal displacement.

Evaluating $f(x) = x^2$ at these inputs:
$$f(2) = 2^2 = 4$$
$$f(2+h) = (2+h)^2 = 4 + 4h + h^2$$

### Step 3: Difference Quotient Calculation
The difference quotient represents the slope of the secant line through $P(2, 4)$ and $Q(2+h, (2+h)^2)$:
$$m_{\text{sec}} = \frac{f(2+h) - f(2)}{(2+h) - 2} = \frac{(4 + 4h + h^2) - 4}{h}$$

Simplifying the numerator:
$$m_{\text{sec}} = \frac{4h + h^2}{h} = \frac{h(4 + h)}{h}$$

### Step 4: Division Validity ($h \neq 0$)
Because $Q$ is initially distinct from $P$, the increment $h \neq 0$. Therefore, dividing numerator and denominator by $h$ is algebraically sound:
$$m_{\text{sec}} = 4 + h \quad (\text{for } h \neq 0)$$

*Note on Rigor:* We do not substitute $h=0$ into the original indeterminate form $\frac{0}{0}$. The cancellation is valid precisely because $h$ is approaching zero without being equal to zero.

### Step 5: The Limit Process (Instantaneous Rate of Change)
The instantaneous rate of change (derivative) at $x = 2$ is defined as the limit of the difference quotient as $h$ approaches zero:
$$f'(2) = \lim_{h \to 0} \frac{f(2+h) - f(2)}{h} = \lim_{h \to 0} (4 + h)$$

Evaluating the limit:
$$f'(2) = 4 + 0 = 4$$

Thus, the instantaneous rate of change of $f(x) = x^2$ at $x = 2$ is exactly **4**.

---

## 3. Geometric Tangent Line Equation

At $x = 2$, the curve passes through $P(2, 4)$. The slope of the tangent line is $m = f'(2) = 4$.

Using the point-slope form:
$$y - y_1 = m(x - x_1)$$
$$y - 4 = 4(x - 2)$$
$$y - 4 = 4x - 8$$
$$y = 4x - 4$$

### Verification of Tangent Properties:
1. **Passes through $P(2,4)$:** At $x = 2$, $y = 4(2) - 4 = 8 - 4 = 4$. (Verified)
2. **Slope:** $dy/dx = 4$. (Verified)
3. **Local Tangency:** The quadratic and line satisfy:
   $$x^2 - (4x - 4) = x^2 - 4x + 4 = (x - 2)^2 \ge 0$$
   The difference has a double root at $x = 2$, confirming tangency without crossing.

---

## 4. Numerical Convergence Table

To demonstrate the limiting process dynamically, five positive values of $h$ are evaluated:

| Step | $h$ | Point $P(x_1, y_1)$ | Point $Q(x_2, y_2)$ | $\Delta x = h$ | $\Delta y = f(2+h)-f(2)$ | Secant Slope $m_{\text{sec}} = 4+h$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | **2.0** | $(2, 4)$ | $(4, 16)$ | $2.0$ | $16 - 4 = 12.0$ | $\frac{12.0}{2.0} = \mathbf{6.0}$ |
| 2 | **1.0** | $(2, 4)$ | $(3, 9)$ | $1.0$ | $9 - 4 = 5.0$ | $\frac{5.0}{1.0} = \mathbf{5.0}$ |
| 3 | **0.5** | $(2, 4)$ | $(2.5, 6.25)$ | $0.5$ | $6.25 - 4 = 2.25$ | $\frac{2.25}{0.5} = \mathbf{4.5}$ |
| 4 | **0.2** | $(2, 4)$ | $(2.2, 4.84)$ | $0.2$ | $4.84 - 4 = 0.84$ | $\frac{0.84}{0.2} = \mathbf{4.2}$ |
| 5 | **0.1** | $(2, 4)$ | $(2.1, 4.41)$ | $0.1$ | $4.41 - 4 = 0.41$ | $\frac{0.41}{0.1} = \mathbf{4.1}$ |
| Limit | $\mathbf{h \to 0}$ | $(2, 4)$ | $(2, 4)$ | $0$ | $0$ | $\mathbf{f'(2) = 4.0}$ |

As $h \to 0^+$ through $\{2.0, 1.0, 0.5, 0.2, 0.1\}$, the secant slope values strictly decrease towards the limit $4.0$:
$$6.0 \longrightarrow 5.0 \longrightarrow 4.5 \longrightarrow 4.2 \longrightarrow 4.1 \longrightarrow \mathbf{4.0}$$

---

## 5. Conclusion
Every algebraic step and numerical point has been independently verified. The transition from the discrete difference quotient to the continuous derivative is mathematically sound, avoiding invalid division by zero while preserving complete analytical precision.
