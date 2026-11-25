"""
Scene 5: What Does the Answer Mean? — Geometric & Physical Interpretation
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    Scene, Text, VGroup, Line, Dot, Circle, DashedLine,
    FadeIn, FadeOut, Write, Create, Transform, Indicate,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR
)
from scenes.helpers import (
    BaseDerivativeScene, BG_COLOR, TEXT_MAIN, TEXT_MUTED,
    COLOR_CURVE, COLOR_SECANT, COLOR_TANGENT, COLOR_ACCENT,
    COLOR_POINT_P, CARD_BG, DEFAULT_FONT
)

class Scene05Interpretation(BaseDerivativeScene):
    def construct(self):
        # 1. Header Banner
        header = self.create_header("Scene 5", "What Does the Answer Mean? — Geometric Meaning")
        self.play(FadeIn(header, shift=DOWN*0.2), run_time=1.2)
        self.wait(1.0)
        
        # 2. Setup Focused Graph (Left Side)
        axes, num_lbls, x_lbl, y_lbl = self.create_parabola_axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 16, 4],
            x_length=5.6,
            y_length=5.2
        )
        graph_group = VGroup(axes, num_lbls, x_lbl, y_lbl).shift(LEFT * 3.4 + DOWN * 0.4)
        
        parabola = axes.plot(lambda x: x**2, x_range=[0, 3.9], color=COLOR_CURVE, stroke_width=3.5)
        curve_label = Text("y = x²", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_CURVE)
        curve_label.next_to(axes.c2p(3.6, 3.6**2), LEFT, buff=0.15).shift(UP * 0.2)
        
        # Point P(2, 4)
        xp, yp = 2.0, 4.0
        p_pt = axes.c2p(xp, yp)
        dot_p = Dot(p_pt, radius=0.13, color=COLOR_POINT_P)
        halo_p = Circle(radius=0.25, color=COLOR_TANGENT, stroke_width=2).move_to(p_pt)
        p_group = VGroup(halo_p, dot_p)
        label_p = Text("P(2, 4)", font=DEFAULT_FONT, font_size=17, weight="BOLD", color=COLOR_POINT_P).next_to(dot_p, DL, buff=0.15)
        
        # Tangent line y = 4x - 4
        # Range: x from 1.0 to 3.8
        tangent_line = Line(
            start=axes.c2p(1.0, 0.0),
            end=axes.c2p(3.8, 11.2),
            stroke_color=COLOR_TANGENT,
            stroke_width=4
        )
        tangent_label = Text("Tangent: y = 4x - 4", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_TANGENT)
        tangent_label.next_to(tangent_line.get_end(), DR, buff=0.1).shift(LEFT*0.8 + DOWN*0.2)
        
        self.play(Create(axes), FadeIn(num_lbls), Write(x_lbl), Write(y_lbl), run_time=1.4)
        self.play(Create(parabola), Write(curve_label), FadeIn(p_group), Write(label_p), run_time=1.6)
        self.wait(1.5)
        self.play(Create(tangent_line), Write(tangent_label), run_time=1.8)
        self.wait(2.5)
        
        # 3. Slope Triangle: Run = 1, Rise = 4
        run_line = Line(start=axes.c2p(2.0, 4.0), end=axes.c2p(3.0, 4.0), stroke_color=COLOR_ACCENT, stroke_width=3)
        rise_line = Line(start=axes.c2p(3.0, 4.0), end=axes.c2p(3.0, 8.0), stroke_color=COLOR_ACCENT, stroke_width=3)
        run_txt = Text("Run = 1", font=DEFAULT_FONT, font_size=14, color=COLOR_ACCENT).next_to(run_line, DOWN, buff=0.1)
        rise_txt = Text("Rise = 4", font=DEFAULT_FONT, font_size=14, color=COLOR_ACCENT).next_to(rise_line, RIGHT, buff=0.1)
        slope_triangle = VGroup(run_line, rise_line, run_txt, rise_txt)
        
        self.play(Create(slope_triangle), run_time=1.5)
        self.wait(3.0)
        
        # 4. Right Side Explanation Dashboard
        card = self.create_card(width=6.0, height=5.2).shift(RIGHT * 3.3 + DOWN * 0.4)
        card_title = Text("Key Insights at x = 2", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=TEXT_MAIN)
        card_title.move_to(card.get_top() + DOWN*0.4)
        
        # Insight 1: Tangent equation
        box1 = self.create_card(width=5.4, height=1.1, corner_radius=0.1).move_to(card.get_top() + DOWN*1.2)
        box1.set_fill(color="#1A243B", opacity=0.9)
        txt1_top = Text("Point-Slope Equation of Tangent Line:", font=DEFAULT_FONT, font_size=14, color=TEXT_MUTED).move_to(box1.get_top() + DOWN*0.28)
        txt1_eq = Text("y - 4 = 4(x - 2)   ⟹   y = 4x - 4", font=DEFAULT_FONT, font_size=17, weight="BOLD", color=COLOR_TANGENT).next_to(txt1_top, DOWN, buff=0.15)
        
        # Insight 2: Secant vs Tangent Comparison
        box2 = self.create_card(width=5.4, height=2.2, corner_radius=0.1).move_to(card.get_top() + DOWN*3.1)
        box2.set_fill(color="#141E33", opacity=0.9)
        txt2_title = Text("Secant vs. Tangent Comparison:", font=DEFAULT_FONT, font_size=15, weight="BOLD", color=COLOR_ACCENT).move_to(box2.get_top() + DOWN*0.3)
        
        comp_lines = [
            "• Secant Line:",
            "   - Crosses curve at 2 distinct points",
            "   - Measures average rate of change",
            "• Tangent Line:",
            "   - Locally touches curve at exactly 1 point",
            "   - Measures instantaneous rate: f'(2) = 4"
        ]
        comp_group = VGroup(*[
            Text(l, font=DEFAULT_FONT, font_size=13.5, color=COLOR_SECANT if "Secant" in l else (COLOR_TANGENT if "Tangent" in l else TEXT_MAIN))
            for l in comp_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12).next_to(txt2_title, DOWN, buff=0.15).align_to(box2, LEFT).shift(RIGHT*0.3)
        
        right_panel = VGroup(card, card_title, box1, txt1_top, txt1_eq, box2, txt2_title, comp_group)
        self.play(FadeIn(right_panel, shift=LEFT*0.3), run_time=2.0)
        self.wait(5.5)
        
        # Fade out for transition
        self.play(
            FadeOut(header), FadeOut(graph_group), FadeOut(parabola), FadeOut(curve_label),
            FadeOut(p_group), FadeOut(label_p), FadeOut(tangent_line), FadeOut(tangent_label),
            FadeOut(slope_triangle), FadeOut(right_panel),
            run_time=1.5
        )
        self.wait(0.5)
