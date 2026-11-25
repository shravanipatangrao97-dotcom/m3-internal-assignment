"""
Scene 2: Understanding the Concept — Average Rate of Change & The Secant Line
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    Scene, Text, VGroup, Line, Dot, DashedLine,
    FadeIn, FadeOut, Write, Create, Transform, Indicate,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR
)
from scenes.helpers import (
    BaseDerivativeScene, BG_COLOR, TEXT_MAIN, TEXT_MUTED,
    COLOR_CURVE, COLOR_SECANT, COLOR_TANGENT, COLOR_ACCENT,
    COLOR_POINT_P, CARD_BG, DEFAULT_FONT
)

class Scene02Concept(BaseDerivativeScene):
    def construct(self):
        # 1. Header Banner
        header = self.create_header("Scene 2", "Understanding the Concept — Secant & Average Rate")
        self.play(FadeIn(header, shift=DOWN*0.2), run_time=1.2)
        self.wait(1.0)
        
        # 2. Setup Axes and Curve
        # Place graph on the left half of the screen
        axes, num_lbls, x_lbl, y_lbl = self.create_parabola_axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 17, 4],
            x_length=5.6,
            y_length=5.0
        )
        graph_group = VGroup(axes, num_lbls, x_lbl, y_lbl).shift(LEFT * 3.4 + DOWN * 0.4)
        
        # Parabola f(x) = x²
        parabola = axes.plot(lambda x: x**2, x_range=[0, 4.0], color=COLOR_CURVE, stroke_width=3.5)
        curve_label = Text("f(x) = x²", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_CURVE)
        curve_label.next_to(axes.c2p(3.5, 3.5**2), LEFT, buff=0.2).shift(UP * 0.2)
        
        self.play(Create(axes), FadeIn(num_lbls), Write(x_lbl), Write(y_lbl), run_time=1.5)
        self.play(Create(parabola), Write(curve_label), run_time=1.8)
        self.wait(2.0)
        
        # 3. Choose two points P and Q
        # Let x1 = 1.2, x2 = 3.2 for clear visual spacing
        x1, y1 = 1.2, 1.2**2
        x2, y2 = 3.2, 3.2**2
        
        p_coords = axes.c2p(x1, y1)
        q_coords = axes.c2p(x2, y2)
        
        dot_p = Dot(p_coords, radius=0.12, color=COLOR_POINT_P)
        label_p = Text("P (x₁, f(x₁))", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_POINT_P).next_to(dot_p, UL, buff=0.15)
        
        dot_q = Dot(q_coords, radius=0.12, color=COLOR_SECANT)
        label_q = Text("Q (x₂, f(x₂))", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_SECANT).next_to(dot_q, UL, buff=0.15)
        
        self.play(FadeIn(dot_p, scale=0.5), Write(label_p), run_time=1.2)
        self.wait(1.5)
        self.play(FadeIn(dot_q, scale=0.5), Write(label_q), run_time=1.2)
        self.wait(1.5)
        
        # 4. Draw Secant Line
        # Line passing through P and Q extended slightly
        slope_val = (y2 - y1) / (x2 - x1)
        x_start, x_end = 0.5, 3.8
        y_start = y1 + slope_val * (x_start - x1)
        y_end = y1 + slope_val * (x_end - x1)
        
        secant_line = Line(
            start=axes.c2p(x_start, y_start),
            end=axes.c2p(x_end, y_end),
            stroke_color=COLOR_SECANT,
            stroke_width=3
        )
        secant_label = Text("Secant Line", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_SECANT)
        secant_label.next_to(secant_line.get_center(), DR, buff=0.2)
        
        self.play(Create(secant_line), Write(secant_label), run_time=1.5)
        self.wait(2.5)
        
        # 5. Right-Hand Explanation Card
        card = self.create_card(width=6.0, height=5.2).shift(RIGHT * 3.3 + DOWN * 0.4)
        
        card_title = Text("Average Rate of Change", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=TEXT_MAIN).move_to(card.get_top() + DOWN*0.4)
        
        formula_box = self.create_card(width=5.4, height=1.1, corner_radius=0.1).move_to(card.get_top() + DOWN*1.3)
        formula_box.set_fill(color="#1A243B", opacity=0.9)
        formula_text = Text(
            "Average Rate =  f(x₂) - f(x₁)\n                       x₂ - x₁",
            font=DEFAULT_FONT,
            font_size=17,
            weight="BOLD",
            color=COLOR_ACCENT
        ).move_to(formula_box.get_center())
        
        bullets = [
            "• Connects two points P and Q on the curve.",
            "• Measures the overall slope across [x₁, x₂].",
            "• Geometrically: slope of the secant line.",
            "• What happens when x₂ approaches x₁?",
            "  → The secant becomes a tangent line!"
        ]
        
        bullet_group = VGroup(*[
            Text(b, font=DEFAULT_FONT, font_size=15, color=TEXT_MUTED if not b.startswith("  →") else COLOR_TANGENT)
            for b in bullets
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(formula_box, DOWN, buff=0.35).align_to(formula_box, LEFT).shift(RIGHT*0.2)
        
        info_group = VGroup(card, card_title, formula_box, formula_text, bullet_group)
        self.play(FadeIn(info_group, shift=LEFT*0.3), run_time=2.0)
        self.wait(4.5)
        
        # 6. Emphasize Delta x and Delta y
        dx_line = DashedLine(start=axes.c2p(x1, y1), end=axes.c2p(x2, y1), stroke_color=TEXT_MUTED, stroke_width=1.5)
        dy_line = DashedLine(start=axes.c2p(x2, y1), end=axes.c2p(x2, y2), stroke_color=TEXT_MUTED, stroke_width=1.5)
        dx_label = Text("Δx", font=DEFAULT_FONT, font_size=15, color=TEXT_MUTED).next_to(dx_line, DOWN, buff=0.1)
        dy_label = Text("Δy", font=DEFAULT_FONT, font_size=15, color=TEXT_MUTED).next_to(dy_line, RIGHT, buff=0.1)
        
        triangle_group = VGroup(dx_line, dy_line, dx_label, dy_label)
        self.play(Create(triangle_group), run_time=1.5)
        self.wait(4.0)
        
        # Fade out for transition
        self.play(
            FadeOut(header), FadeOut(graph_group), FadeOut(parabola), FadeOut(curve_label),
            FadeOut(dot_p), FadeOut(label_p), FadeOut(dot_q), FadeOut(label_q),
            FadeOut(secant_line), FadeOut(secant_label), FadeOut(triangle_group),
            FadeOut(info_group),
            run_time=1.5
        )
        self.wait(0.5)
