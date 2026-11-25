"""
Scene 4: Step-by-Step Worked Derivation — Analytical Proof
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    Scene, Text, VGroup, Line, Rectangle,
    FadeIn, FadeOut, Write, Create, Transform, Indicate,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR
)
from scenes.helpers import (
    BaseDerivativeScene, BG_COLOR, TEXT_MAIN, TEXT_MUTED,
    COLOR_CURVE, COLOR_SECANT, COLOR_TANGENT, COLOR_ACCENT,
    CARD_BG, CARD_BORDER, DEFAULT_FONT
)

class Scene04Derivation(BaseDerivativeScene):
    def construct(self):
        # 1. Header Banner
        header = self.create_header("Scene 4", "Step-by-Step Worked Derivation — Analytical Proof")
        self.play(FadeIn(header, shift=DOWN*0.2), run_time=1.2)
        self.wait(1.0)
        
        # 2. Main Derivation Board Card
        board = self.create_card(width=13.0, height=5.6).shift(DOWN * 0.4)
        self.play(FadeIn(board), run_time=1.0)
        
        # 3. Step 1: Definition of Derivative
        step1_title = Text("1. Formal Definition of the Derivative", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_CURVE)
        step1_title.move_to(board.get_top() + DOWN*0.45).align_to(board, LEFT).shift(RIGHT*0.6)
        
        step1_eq = Text("f'(a) = lim [ f(a + h) - f(a) ] / h   (as h → 0)", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=TEXT_MAIN)
        step1_eq.next_to(step1_title, DOWN, buff=0.2).align_to(step1_title, LEFT).shift(RIGHT*0.4)
        
        self.play(Write(step1_title), run_time=1.2)
        self.play(Write(step1_eq), run_time=1.8)
        self.wait(3.0)
        
        # 4. Step 2: Evaluate f(2) and f(2 + h) for f(x) = x²
        step2_title = Text("2. Evaluate f(2) and f(2 + h) for f(x) = x²", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_CURVE)
        step2_title.next_to(step1_eq, DOWN, buff=0.35).align_to(step1_title, LEFT)
        
        step2_line1 = Text("• f(2) = 2² = 4", font=DEFAULT_FONT, font_size=18, color=TEXT_MAIN)
        step2_line2 = Text("• f(2 + h) = (2 + h)² = 4 + 4h + h²", font=DEFAULT_FONT, font_size=18, color=COLOR_ACCENT)
        step2_group = VGroup(step2_line1, step2_line2).arrange(RIGHT, buff=0.8).next_to(step2_title, DOWN, buff=0.18).align_to(step1_eq, LEFT)
        
        self.play(Write(step2_title), run_time=1.2)
        self.play(Write(step2_group), run_time=2.0)
        self.wait(3.5)
        
        # 5. Step 3: Substitute into Difference Quotient
        step3_title = Text("3. Substitute into the Difference Quotient", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_CURVE)
        step3_title.next_to(step2_group, DOWN, buff=0.35).align_to(step1_title, LEFT)
        
        step3_eq1 = Text("f'(2) = lim [ (4 + 4h + h²) - 4 ] / h", font=DEFAULT_FONT, font_size=19, color=TEXT_MAIN)
        step3_eq1.next_to(step3_title, DOWN, buff=0.18).align_to(step1_eq, LEFT)
        
        step3_eq2 = Text("      = lim [ 4h + h² ] / h", font=DEFAULT_FONT, font_size=19, color=TEXT_MAIN)
        step3_eq2.next_to(step3_eq1, DOWN, buff=0.15).align_to(step3_eq1, LEFT)
        
        self.play(Write(step3_title), run_time=1.2)
        self.play(Write(step3_eq1), run_time=1.8)
        self.wait(2.0)
        self.play(Write(step3_eq2), run_time=1.8)
        self.wait(3.5)
        
        # 6. Step 4: Division Validity & Final Limit
        # Transition out upper steps smoothly to leave ample room for crucial simplification
        self.play(
            FadeOut(step1_title), FadeOut(step1_eq),
            FadeOut(step2_title), FadeOut(step2_group),
            step3_title.animate.move_to(board.get_top() + DOWN*0.5).align_to(board, LEFT).shift(RIGHT*0.6),
            step3_eq1.animate.next_to(board.get_top() + DOWN*0.9, DOWN, buff=0.1).align_to(board, LEFT).shift(RIGHT*1.0),
            step3_eq2.animate.next_to(board.get_top() + DOWN*1.5, DOWN, buff=0.1).align_to(board, LEFT).shift(RIGHT*1.0),
            run_time=1.5
        )
        self.wait(1.5)
        
        step4_title = Text("4. Factor and Simplify (Crucial Condition: h ≠ 0)", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_SECANT)
        step4_title.next_to(step3_eq2, DOWN, buff=0.35).align_to(step3_title, LEFT)
        
        step4_eq = Text("      = lim [ h(4 + h) ] / h = lim (4 + h)    [Valid because h ≠ 0]", font=DEFAULT_FONT, font_size=19, weight="BOLD", color=COLOR_ACCENT)
        step4_eq.next_to(step4_title, DOWN, buff=0.18).align_to(step3_eq1, LEFT)
        
        # Rigor note callout
        rigor_box = self.create_card(width=11.8, height=0.75, corner_radius=0.1).next_to(step4_eq, DOWN, buff=0.25).align_to(step3_title, LEFT)
        rigor_box.set_fill(color="#241B0A", opacity=0.9)
        rigor_box.set_stroke(color=COLOR_ACCENT, width=1.0)
        rigor_txt = Text("Mathematical Rigor: We never substitute h = 0 into 0/0. We simplify the ratio first!", font=DEFAULT_FONT, font_size=14, color=COLOR_ACCENT).move_to(rigor_box.get_center())
        
        self.play(Write(step4_title), run_time=1.2)
        self.play(Write(step4_eq), run_time=2.0)
        self.play(FadeIn(rigor_box), Write(rigor_txt), run_time=1.2)
        self.wait(4.5)
        
        # 7. Final Evaluation Step
        step5_title = Text("5. Evaluate the Limit as h → 0", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_TANGENT)
        step5_title.next_to(rigor_box, DOWN, buff=0.3).align_to(step3_title, LEFT)
        
        step5_eq = Text("f'(2) = 4 + 0 = 4", font=DEFAULT_FONT, font_size=24, weight="BOLD", color=TEXT_MAIN)
        step5_eq.next_to(step5_title, DOWN, buff=0.18).align_to(step3_eq1, LEFT)
        
        # Result Badge Box
        result_badge = self.create_card(width=4.5, height=1.0, corner_radius=0.15)
        result_badge.set_fill(color="#0F382B", opacity=0.9)
        result_badge.set_stroke(color=COLOR_TANGENT, width=2.0)
        result_badge.next_to(step5_eq, RIGHT, buff=1.0)
        result_txt = Text("Result: f'(2) = 4", font=DEFAULT_FONT, font_size=24, weight="BOLD", color=COLOR_TANGENT).move_to(result_badge.get_center())
        
        self.play(Write(step5_title), run_time=1.2)
        self.play(Write(step5_eq), FadeIn(result_badge), Write(result_txt), run_time=2.0)
        self.wait(5.5)
        
        # Fade out for transition
        self.play(
            FadeOut(header), FadeOut(board),
            FadeOut(step3_title), FadeOut(step3_eq1), FadeOut(step3_eq2),
            FadeOut(step4_title), FadeOut(step4_eq), FadeOut(rigor_box), FadeOut(rigor_txt),
            FadeOut(step5_title), FadeOut(step5_eq), FadeOut(result_badge), FadeOut(result_txt),
            run_time=1.5
        )
        self.wait(0.5)
