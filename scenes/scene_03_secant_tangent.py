"""
Scene 3: Secant Approaching Tangent — Geometric Intuition of the Limit
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    Scene, Text, VGroup, Line, Dot, Circle,
    FadeIn, FadeOut, Write, Create, Transform, Indicate, ReplacementTransform,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR
)
from scenes.helpers import (
    BaseDerivativeScene, BG_COLOR, TEXT_MAIN, TEXT_MUTED,
    COLOR_CURVE, COLOR_SECANT, COLOR_TANGENT, COLOR_ACCENT,
    COLOR_POINT_P, CARD_BG, CARD_BORDER, DEFAULT_FONT
)

class Scene03SecantTangent(BaseDerivativeScene):
    def construct(self):
        # 1. Header Banner
        header = self.create_header("Scene 3", "Secant Approaching Tangent — The Limiting Process")
        self.play(FadeIn(header, shift=DOWN*0.2), run_time=1.2)
        self.wait(1.0)
        
        # 2. Axes & Parabola setup (Left Side)
        axes, num_lbls, x_lbl, y_lbl = self.create_parabola_axes(
            x_range=[0, 4.4, 1],
            y_range=[0, 18, 3],
            x_length=5.6,
            y_length=5.2
        )
        graph_group = VGroup(axes, num_lbls, x_lbl, y_lbl).shift(LEFT * 3.4 + DOWN * 0.4)
        
        parabola = axes.plot(lambda x: x**2, x_range=[0, 4.2], color=COLOR_CURVE, stroke_width=3.5)
        curve_label = Text("f(x) = x²", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_CURVE)
        curve_label.next_to(axes.c2p(4.0, 16), LEFT, buff=0.15).shift(UP * 0.1)
        
        self.play(Create(axes), FadeIn(num_lbls), Write(x_lbl), Write(y_lbl), run_time=1.4)
        self.play(Create(parabola), Write(curve_label), run_time=1.5)
        self.wait(1.0)
        
        # 3. Fixed Point P(2, 4)
        xp, yp = 2.0, 4.0
        p_pt = axes.c2p(xp, yp)
        dot_p = Dot(p_pt, radius=0.13, color=COLOR_POINT_P)
        halo_p = Circle(radius=0.24, color=COLOR_POINT_P, stroke_width=1.5).move_to(p_pt)
        p_group = VGroup(halo_p, dot_p)
        label_p = Text("P(2, 4)", font=DEFAULT_FONT, font_size=17, weight="BOLD", color=COLOR_POINT_P)
        label_p.next_to(dot_p, DL, buff=0.15)
        
        self.play(FadeIn(p_group), Write(label_p), run_time=1.2)
        self.wait(1.5)
        
        # 4. Right Side Dashboard Card
        card = self.create_card(width=6.0, height=5.2).shift(RIGHT * 3.3 + DOWN * 0.4)
        dashboard_title = Text("Secant Slope Convergence", font=DEFAULT_FONT, font_size=19, weight="BOLD", color=TEXT_MAIN)
        dashboard_title.move_to(card.get_top() + DOWN*0.4)
        
        formula_box = self.create_card(width=5.4, height=0.9, corner_radius=0.1).move_to(card.get_top() + DOWN*1.15)
        formula_box.set_fill(color="#1A243B", opacity=0.9)
        formula_text = Text("m_sec = [f(2+h) - f(2)] / h = 4 + h", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_ACCENT)
        formula_text.move_to(formula_box.get_center())
        
        # Live indicators in card
        h_label = Text("Horizontal Step (h):", font=DEFAULT_FONT, font_size=15, color=TEXT_MUTED).shift(RIGHT*1.8 + UP*0.5)
        q_label = Text("Point Q Coordinates:", font=DEFAULT_FONT, font_size=15, color=TEXT_MUTED).shift(RIGHT*1.8 + DOWN*0.1)
        slope_label = Text("Secant Slope (m_sec):", font=DEFAULT_FONT, font_size=15, color=TEXT_MUTED).shift(RIGHT*1.8 + DOWN*0.7)
        
        self.play(
            FadeIn(card), FadeIn(dashboard_title),
            FadeIn(formula_box), FadeIn(formula_text),
            Write(h_label), Write(q_label), Write(slope_label),
            run_time=1.5
        )
        self.wait(1.5)
        
        # Helper to compute secant line mobject
        def get_secant_line(h_val, color=COLOR_SECANT):
            xq = xp + h_val
            yq = xq**2
            m = (yq - yp) / (xq - xp)
            x_min = max(0.2, xp - 1.2)
            x_max = min(4.3, xq + 0.5)
            y_min = yp + m * (x_min - xp)
            y_max = yp + m * (x_max - xp)
            return Line(axes.c2p(x_min, y_min), axes.c2p(x_max, y_max), stroke_color=color, stroke_width=3)
        
        # Steps for h
        h_values = [2.0, 1.0, 0.5, 0.2, 0.1]
        
        # Initial h = 2.0
        h_curr = h_values[0]
        xq, yq = xp + h_curr, (xp + h_curr)**2
        dot_q = Dot(axes.c2p(xq, yq), radius=0.12, color=COLOR_SECANT)
        label_q = Text("Q", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_SECANT).next_to(dot_q, UR, buff=0.1)
        secant_line = get_secant_line(h_curr)
        
        h_val_text = Text(f"{h_curr:.1f}", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_SECANT).next_to(h_label, RIGHT, buff=0.3)
        q_val_text = Text(f"({xq:.1f}, {yq:.1f})", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_SECANT).next_to(q_label, RIGHT, buff=0.3)
        slope_val_text = Text(f"{4.0 + h_curr:.1f}", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_ACCENT).next_to(slope_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(dot_q), Write(label_q), Create(secant_line),
            Write(h_val_text), Write(q_val_text), Write(slope_val_text),
            run_time=1.5
        )
        self.wait(3.5)
        
        # Step through remaining h values: 1.0, 0.5, 0.2, 0.1
        for next_h in h_values[1:]:
            next_xq = xp + next_h
            next_yq = next_xq**2
            next_dot_q = Dot(axes.c2p(next_xq, next_yq), radius=0.12, color=COLOR_SECANT)
            next_label_q = Text("Q", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_SECANT).next_to(next_dot_q, UR, buff=0.1)
            next_secant = get_secant_line(next_h)
            
            next_h_text = Text(f"{next_h:.1f}", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_SECANT).next_to(h_label, RIGHT, buff=0.3)
            next_q_text = Text(f"({next_xq:.2f}, {next_yq:.2f})", font=DEFAULT_FONT, font_size=15, weight="BOLD", color=COLOR_SECANT).next_to(q_label, RIGHT, buff=0.3)
            next_slope_text = Text(f"{4.0 + next_h:.2f}", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_ACCENT).next_to(slope_label, RIGHT, buff=0.3)
            
            self.play(
                Transform(dot_q, next_dot_q),
                Transform(label_q, next_label_q),
                Transform(secant_line, next_secant),
                Transform(h_val_text, next_h_text),
                Transform(q_val_text, next_q_text),
                Transform(slope_val_text, next_slope_text),
                run_time=2.2
            )
            self.wait(2.8)
        
        # 5. The Limiting Case: h -> 0 yields Tangent Line y = 4x - 4
        limit_banner = self.create_card(width=5.4, height=1.1, corner_radius=0.1).shift(RIGHT * 3.3 + DOWN * 2.1)
        limit_banner.set_fill(color="#0F382B", opacity=0.9)
        limit_banner.set_stroke(color=COLOR_TANGENT, width=1.5)
        
        limit_txt1 = Text("Limit as h → 0:  Tangent Line!", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_TANGENT).move_to(limit_banner.get_top() + DOWN*0.35)
        limit_txt2 = Text("Slope m = 4.0  |  Equation: y = 4x - 4", font=DEFAULT_FONT, font_size=15, weight="BOLD", color=TEXT_MAIN).next_to(limit_txt1, DOWN, buff=0.15)
        
        # Tangent line passing through (2, 4) with slope 4
        tangent_line = Line(
            start=axes.c2p(1.0, 0.0),
            end=axes.c2p(3.8, 11.2),
            stroke_color=COLOR_TANGENT,
            stroke_width=4
        )
        
        self.play(
            FadeOut(dot_q), FadeOut(label_q),
            ReplacementTransform(secant_line, tangent_line),
            FadeIn(limit_banner), Write(limit_txt1), Write(limit_txt2),
            run_time=2.5
        )
        self.wait(5.5)
        
        # Fade out for transition
        self.play(
            FadeOut(header), FadeOut(graph_group), FadeOut(parabola), FadeOut(curve_label),
            FadeOut(p_group), FadeOut(label_p), FadeOut(tangent_line),
            FadeOut(card), FadeOut(dashboard_title), FadeOut(formula_box), FadeOut(formula_text),
            FadeOut(h_label), FadeOut(q_label), FadeOut(slope_label),
            FadeOut(h_val_text), FadeOut(q_val_text), FadeOut(slope_val_text),
            FadeOut(limit_banner), FadeOut(limit_txt1), FadeOut(limit_txt2),
            run_time=1.5
        )
        self.wait(0.5)
