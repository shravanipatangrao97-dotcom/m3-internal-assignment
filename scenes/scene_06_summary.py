"""
Scene 6: Summary and Credits — Core Takeaways & Project Attribution
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

class Scene06Summary(BaseDerivativeScene):
    def construct(self):
        # 1. Header Banner
        header = self.create_header("Scene 6", "Summary & Credits — Key Takeaways")
        self.play(FadeIn(header, shift=DOWN*0.2), run_time=1.2)
        self.wait(0.8)
        
        # 2. Part 1: Three Core Takeaways
        t1_box = self.create_card(width=12.2, height=1.0, corner_radius=0.12).shift(UP * 1.5)
        t1_icon = Text("1", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_SECANT).move_to(t1_box.get_left() + RIGHT*0.4)
        t1_txt = Text("Secant Line: Measures the average rate of change across an interval [x₁, x₂].", font=DEFAULT_FONT, font_size=16, color=TEXT_MAIN).next_to(t1_icon, RIGHT, buff=0.3)
        g1 = VGroup(t1_box, t1_icon, t1_txt)
        
        t2_box = self.create_card(width=12.2, height=1.0, corner_radius=0.12).shift(UP * 0.35)
        t2_icon = Text("2", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_TANGENT).move_to(t2_box.get_left() + RIGHT*0.4)
        t2_txt = Text("Tangent Line: Measures the instantaneous rate of change at an exact point x = a.", font=DEFAULT_FONT, font_size=16, color=TEXT_MAIN).next_to(t2_icon, RIGHT, buff=0.3)
        g2 = VGroup(t2_box, t2_icon, t2_txt)
        
        t3_box = self.create_card(width=12.2, height=1.0, corner_radius=0.12).shift(DOWN * 0.8)
        t3_icon = Text("3", font=DEFAULT_FONT, font_size=18, weight="BOLD", color=COLOR_CURVE).move_to(t3_box.get_left() + RIGHT*0.4)
        t3_txt = Text("The Derivative: Obtained by taking the limit of the difference quotient as h → 0.", font=DEFAULT_FONT, font_size=16, color=TEXT_MAIN).next_to(t3_icon, RIGHT, buff=0.3)
        g3 = VGroup(t3_box, t3_icon, t3_txt)
        
        self.play(FadeIn(g1, shift=LEFT*0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeIn(g2, shift=LEFT*0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeIn(g3, shift=LEFT*0.3), run_time=1.0)
        self.wait(2.5)
        
        # Result equation & Closing Motto
        banner = self.create_card(width=12.2, height=1.1, corner_radius=0.15).shift(DOWN * 2.2)
        banner.set_fill(color="#0F382B", opacity=0.9)
        banner.set_stroke(color=COLOR_TANGENT, width=1.5)
        
        eq_txt = Text("f'(2) = 4    |    Tangent: y = 4x - 4", font=DEFAULT_FONT, font_size=20, weight="BOLD", color=COLOR_TANGENT).move_to(banner.get_top() + DOWN*0.35)
        motto = Text("“From two points to one tangent. That is the idea behind the derivative.”", font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_ACCENT).next_to(eq_txt, DOWN, buff=0.15)
        
        g_banner = VGroup(banner, eq_txt, motto)
        self.play(FadeIn(g_banner, shift=UP*0.3), run_time=1.5)
        self.wait(4.5)
        
        # 3. Transition to Credits Card
        self.play(
            FadeOut(g1), FadeOut(g2), FadeOut(g3), FadeOut(g_banner),
            run_time=1.2
        )
        self.wait(0.5)
        
        # Credits Display
        credits_card = self.create_card(width=12.0, height=5.2).shift(DOWN * 0.4)
        credits_title = Text("PROJECT CREDITS & ATTRIBUTION", font=DEFAULT_FONT, font_size=22, weight="BOLD", color=COLOR_CURVE).move_to(credits_card.get_top() + DOWN*0.45)
        
        c_lines = [
            ("Student Name:", "Shravani Patil"),
            ("Subject:", "Linear Algebra and Calculus (M3)"),
            ("Project Title:", "The Derivative — From Secant to Tangent"),
            ("Tools & Stack:", "Python 3.12, Manim Community Edition, FFmpeg, ReportLab"),
            ("Academic References:", "Calculus by Stewart; Thomas' Calculus; 3Blue1Brown"),
            ("Starter Attribution:", "Inspired by m3-manim-animation-kit (Soham Dhande, MIT)"),
            ("AI Tools Disclosure:", "Assisted by Antigravity (Gemini) for coding & rendering")
        ]
        
        credit_entries = []
        for label, val in c_lines:
            lbl_m = Text(label, font=DEFAULT_FONT, font_size=15, weight="BOLD", color=TEXT_MUTED)
            val_m = Text(val, font=DEFAULT_FONT, font_size=15, color=TEXT_MAIN)
            row = VGroup(lbl_m, val_m).arrange(RIGHT, buff=0.3)
            lbl_m.align_to(row, LEFT)
            credit_entries.append(row)
            
        credits_group = VGroup(*credit_entries).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        credits_group.next_to(credits_title, DOWN, buff=0.35).align_to(credits_card, LEFT).shift(RIGHT*0.8)
        
        self.play(FadeIn(credits_card), Write(credits_title), run_time=1.2)
        self.play(FadeIn(credits_group, shift=UP*0.2), run_time=1.8)
        self.wait(4.0)
        
        self.play(FadeOut(header), FadeOut(credits_card), FadeOut(credits_title), FadeOut(credits_group), run_time=1.5)
        self.wait(0.5)
