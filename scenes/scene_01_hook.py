"""
Scene 1: The Hook — Speed at an Instant
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import (
    Scene, Text, VGroup, Line, Arrow, Dot, Circle, Rectangle,
    FadeIn, FadeOut, Write, Create, Transform, Indicate,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR
)
from scenes.helpers import (
    BaseDerivativeScene, BG_COLOR, TEXT_MAIN, TEXT_MUTED,
    COLOR_CURVE, COLOR_SECANT, COLOR_TANGENT, COLOR_ACCENT, CARD_BG, DEFAULT_FONT
)

class Scene01Hook(BaseDerivativeScene):
    def construct(self):
        # 1. Header Banner
        header = self.create_header("Scene 1", "The Hook — The Paradox of Instantaneous Speed")
        self.play(FadeIn(header, shift=DOWN*0.2), run_time=1.5)
        self.wait(1.0)
        
        # 2. Provocative Question
        question = Text(
            "How fast is something moving\nat one exact instant?",
            font=DEFAULT_FONT,
            font_size=36,
            weight="BOLD",
            color=TEXT_MAIN,
            line_spacing=1.3
        ).shift(UP * 1.5)
        
        self.play(Write(question), run_time=2.5)
        self.wait(2.0)
        
        # 3. Motion Track Animation
        # Track line
        track = Line(start=[-5.5, -0.8, 0], end=[5.5, -0.8, 0], stroke_color="#334155", stroke_width=4)
        start_tick = Line(start=[-5.0, -0.6, 0], end=[-5.0, -1.0, 0], stroke_color=TEXT_MUTED, stroke_width=2)
        end_tick = Line(start=[5.0, -0.6, 0], end=[5.0, -1.0, 0], stroke_color=TEXT_MUTED, stroke_width=2)
        t0_label = Text("t = 0", font=DEFAULT_FONT, font_size=18, color=TEXT_MUTED).next_to(start_tick, DOWN, buff=0.15)
        t1_label = Text("t = T", font=DEFAULT_FONT, font_size=18, color=TEXT_MUTED).next_to(end_tick, DOWN, buff=0.15)
        
        # Particle / Car indicator
        particle = Dot(point=[-5.0, -0.8, 0], radius=0.18, color=COLOR_CURVE)
        halo = Circle(radius=0.35, color=COLOR_CURVE, stroke_width=1.5).move_to(particle)
        car_group = VGroup(halo, particle)
        
        self.play(Create(track), Create(start_tick), Create(end_tick), Write(t0_label), Write(t1_label), run_time=1.5)
        self.play(FadeIn(car_group), run_time=0.8)
        self.wait(0.5)
        
        # Animate particle moving across
        vel_vector = Arrow(start=particle.get_center(), end=particle.get_center() + RIGHT*1.2, color=COLOR_ACCENT, buff=0, stroke_width=3)
        self.play(Create(vel_vector), run_time=0.6)
        
        # Move along track
        self.play(
            car_group.animate.move_to([5.0, -0.8, 0]),
            vel_vector.animate.move_to([5.6, -0.8, 0]),
            run_time=3.5,
            rate_func=lambda t: t**1.4  # Accelerating motion
        )
        self.wait(1.0)
        
        # 4. Present the Paradox
        self.play(
            FadeOut(track), FadeOut(start_tick), FadeOut(end_tick),
            FadeOut(t0_label), FadeOut(t1_label), FadeOut(car_group), FadeOut(vel_vector),
            question.animate.shift(UP * 0.8).scale(0.85),
            run_time=1.5
        )
        
        # Paradox Comparison Box
        card1 = self.create_card(width=5.8, height=2.6).shift(LEFT * 3.3 + DOWN * 0.8)
        card2 = self.create_card(width=5.8, height=2.6).shift(RIGHT * 3.3 + DOWN * 0.8)
        
        title_avg = Text("Average Speed", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_CURVE).move_to(card1.get_top() + DOWN*0.4)
        formula_avg = Text("Speed = Δs / Δt", font=DEFAULT_FONT, font_size=22, weight="BOLD", color=TEXT_MAIN).next_to(title_avg, DOWN, buff=0.35)
        desc_avg = Text("Measured over a non-zero\ntime interval (Δt > 0)", font=DEFAULT_FONT, font_size=16, color=TEXT_MUTED, line_spacing=1.2).next_to(formula_avg, DOWN, buff=0.3)
        
        title_inst = Text("Instantaneous Speed", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_SECANT).move_to(card2.get_top() + DOWN*0.4)
        formula_inst = Text("At one instant: Δt = 0", font=DEFAULT_FONT, font_size=22, weight="BOLD", color=TEXT_MAIN).next_to(title_inst, DOWN, buff=0.35)
        desc_inst = Text("Speed = 0 / 0 = Undefined!\nThe Fundamental Paradox", font=DEFAULT_FONT, font_size=16, color=COLOR_ACCENT, line_spacing=1.2).next_to(formula_inst, DOWN, buff=0.3)
        
        group1 = VGroup(card1, title_avg, formula_avg, desc_avg)
        group2 = VGroup(card2, title_inst, formula_inst, desc_inst)
        
        self.play(FadeIn(group1, shift=UP*0.3), run_time=1.5)
        self.wait(2.0)
        self.play(FadeIn(group2, shift=UP*0.3), run_time=1.5)
        self.wait(2.5)
        
        # Resolution Teaser
        resolution = Text(
            "The Solution: Differential Calculus & Limits",
            font=DEFAULT_FONT,
            font_size=22,
            weight="BOLD",
            color=COLOR_TANGENT
        ).to_edge(DOWN, buff=0.6)
        
        self.play(FadeIn(resolution, shift=UP*0.2), run_time=1.5)
        self.wait(3.5)
        
        # Fade out for transition
        self.play(
            FadeOut(header), FadeOut(question), FadeOut(group1), FadeOut(group2), FadeOut(resolution),
            run_time=1.5
        )
        self.wait(0.5)
