"""
Shared helpers, constants, and base classes for the Derivative Animation.
"""
from manim import (
    Scene, Text, VGroup, Line, Rectangle, RoundedRectangle, Axes, Dot, DashedLine,
    UP, DOWN, LEFT, RIGHT, ORIGIN, UL, UR, DL, DR,
    config
)

# Visual Design Palette
BG_COLOR = "#0A0E17"        # Dark navy background
TEXT_MAIN = "#F8FAFC"       # Off-white primary text
TEXT_MUTED = "#94A3B8"      # Light slate secondary text
COLOR_CURVE = "#38BDF8"     # Electric cyan / blue for y = x²
COLOR_SECANT = "#FB923C"    # Vibrant orange for secant & moving Q
COLOR_TANGENT = "#10B981"   # Emerald green for tangent & final derivative
COLOR_ACCENT = "#FACC15"    # Gold / yellow for highlights
COLOR_POINT_P = "#38BDF8"   # Fixed point P (cyan/white)
CARD_BG = "#131C2E"         # Card background
CARD_BORDER = "#1E293B"     # Card border stroke

DEFAULT_FONT = "Helvetica"

class BaseDerivativeScene(Scene):
    """Base scene establishing theme and standard visual layout."""
    
    def setup(self):
        self.camera.background_color = BG_COLOR
        super().setup()

    def create_header(self, scene_number: str, title: str):
        """Creates a standardized top banner."""
        num_text = Text(scene_number.upper(), font=DEFAULT_FONT, font_size=16, weight="BOLD", color=COLOR_CURVE)
        dot = Text("•", font=DEFAULT_FONT, font_size=16, color=TEXT_MUTED)
        title_text = Text(title, font=DEFAULT_FONT, font_size=20, weight="BOLD", color=TEXT_MAIN)
        
        header_group = VGroup(num_text, dot, title_text).arrange(RIGHT, buff=0.25)
        header_group.to_corner(UL, buff=0.5)
        
        divider = Line(
            start=[-7.1, header_group.get_bottom()[1] - 0.15, 0],
            end=[7.1, header_group.get_bottom()[1] - 0.15, 0],
            stroke_width=1.5,
            stroke_color="#1E293B"
        )
        return VGroup(header_group, divider)

    def create_card(self, width: float, height: float, corner_radius: float = 0.2):
        """Creates an elegant background card for equations or takeaways."""
        card = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=corner_radius,
            fill_color=CARD_BG,
            fill_opacity=0.85,
            stroke_color=CARD_BORDER,
            stroke_width=1.5
        )
        return card

    def create_parabola_axes(self, x_range=[0, 4.5, 1], y_range=[0, 18, 3], x_length=6.0, y_length=5.5):
        """Creates scaled, labeled axes for graphing f(x) = x² without LaTeX dependencies."""
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            axis_config={
                "color": TEXT_MUTED,
                "stroke_width": 2,
                "include_ticks": True,
            },
            tips=True
        )
        x_label = Text("x", font=DEFAULT_FONT, font_size=18, color=TEXT_MAIN).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = Text("y", font=DEFAULT_FONT, font_size=18, color=TEXT_MAIN).next_to(axes.y_axis.get_end(), UP, buff=0.15)
        
        # Add coordinate numbers cleanly using Text
        num_labels = VGroup()
        # X-axis ticks
        x_start, x_end, x_step = x_range
        curr_x = x_start + x_step
        while curr_x <= x_end:
            val_str = f"{int(curr_x)}" if curr_x == int(curr_x) else f"{curr_x}"
            t = Text(val_str, font=DEFAULT_FONT, font_size=13, color=TEXT_MUTED).next_to(axes.c2p(curr_x, 0), DOWN, buff=0.15)
            num_labels.add(t)
            curr_x += x_step
            
        # Y-axis ticks
        y_start, y_end, y_step = y_range
        curr_y = y_start + y_step
        while curr_y <= y_end:
            val_str = f"{int(curr_y)}" if curr_y == int(curr_y) else f"{curr_y}"
            t = Text(val_str, font=DEFAULT_FONT, font_size=13, color=TEXT_MUTED).next_to(axes.c2p(0, curr_y), LEFT, buff=0.15)
            num_labels.add(t)
            curr_y += y_step
            
        return axes, num_labels, x_label, y_label
