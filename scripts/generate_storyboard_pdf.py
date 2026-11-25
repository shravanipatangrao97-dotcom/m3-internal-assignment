"""
Generate a professional Six-Scene Storyboard PDF using ReportLab.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (pages after 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "M3 Calculus Assessment: The Derivative — From Secant to Tangent")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, footer_text)
        self.drawString(54, 36, "Student: Shravani Patil  |  Subject: Linear Algebra & Calculus (M3)")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        
        self.restoreState()

def build_pdf(filename="storyboard/storyboard.pdf"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2B6CB0"),
        spaceAfter=15
    )
    
    meta_style = ParagraphStyle(
        'MetaText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#4A5568")
    )
    
    h1_style = ParagraphStyle(
        'SceneH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1A365D"),
        spaceBefore=10,
        spaceAfter=6
    )
    
    label_style = ParagraphStyle(
        'FieldLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#2D3748")
    )
    
    body_style = ParagraphStyle(
        'FieldBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#2D3748")
    )
    
    math_style = ParagraphStyle(
        'MathBody',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2C5282")
    )

    story = []
    
    # Header block
    story.append(Paragraph("Six-Scene Storyboard Specification", title_style))
    story.append(Paragraph("The Derivative: From Secant to Tangent — Linear Algebra & Calculus (M3)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2B6CB0"), spaceAfter=12))
    
    # Metadata summary table
    meta_data = [
        [
            Paragraph("<b>Student Name:</b> Shravani Patil", meta_style),
            Paragraph("<b>Course:</b> Linear Algebra & Calculus (M3)", meta_style)
        ],
        [
            Paragraph("<b>Project Duration:</b> ~4m 45s (Max 7m)", meta_style),
            Paragraph("<b>Resolution:</b> 1080p Landscape (1920x1080, 30fps)", meta_style)
        ],
        [
            Paragraph("<b>Primary Example:</b> f(x) = x² at x = 2", meta_style),
            Paragraph("<b>Target Result:</b> f'(2) = 4, Tangent: y = 4x - 4", meta_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[250, 254])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EDF2F7")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 14))
    
    scenes_data = [
        {
            "num": "SCENE 1",
            "title": "The Hook — The Paradox of Instantaneous Speed",
            "duration": "Approx. 35 seconds",
            "objective": "Spark mathematical curiosity by contrasting average speed over an interval with speed at an exact instant.",
            "visuals": "Dark navy mathematical background. Smooth moving particle on an arc with dynamic velocity vector. Display question: 'How fast is something moving at one exact instant?'. Reveal dilemma Delta s / Delta t -> 0/0. Transition seamlessly to coordinate axes.",
            "math": "v_avg = Delta s / Delta t\nInstantaneous speed requires Delta t -> 0: ratio approaches 0/0 (indeterminate).",
            "narration": "Have you ever checked your speedometer and wondered how speed can be measured at one exact instant? Speed is distance over time, but at one instant elapsed time is zero! Calculus solves this paradox with limits."
        },
        {
            "num": "SCENE 2",
            "title": "Understanding the Concept — Secant & Average Rate",
            "duration": "Approx. 45 seconds",
            "objective": "Introduce f(x) = x², plot points P and Q, construct secant line, and define average rate of change.",
            "visuals": "Coordinate system with grid lines. Electric blue parabola y = x². Fixed point P(x1, f(x1)) and second point Q(x2, f(x2)). Orange secant line connecting P and Q. Slope triangle showing Delta x and Delta y. Equation card for average rate of change.",
            "math": "f(x) = x²\nAverage rate of change = [f(x2) - f(x1)] / (x2 - x1)\nSlope of secant line m_sec = Delta y / Delta x",
            "narration": "Let's examine f(x) = x². To measure change, we choose two points, P and Q. The line between them is a secant line, whose slope gives the average rate of change over that interval. But what happens if the points get closer?"
        },
        {
            "num": "SCENE 3",
            "title": "Secant to Tangent — Geometric Limiting Process",
            "duration": "Approx. 60 seconds",
            "objective": "Provide geometric intuition by animating Q approaching P across decreasing h values to reveal the tangent line.",
            "visuals": "Parabola y = x². Fixed point P(2, 4) in cyan. Variable point Q(2+h, (2+h)²) stepping through h = 2.0, 1.0, 0.5, 0.2, 0.1. Orange secant line pivots dynamically. Real-time slope readout: 6.0 -> 5.0 -> 4.5 -> 4.2 -> 4.1. Morph into green tangent line y = 4x - 4.",
            "math": "h=2.0 -> m_sec=6.0\nh=1.0 -> m_sec=5.0\nh=0.5 -> m_sec=4.5\nh=0.2 -> m_sec=4.2\nh=0.1 -> m_sec=4.1\nLimit h->0 -> m_tan = 4.0; Tangent: y = 4x - 4",
            "narration": "Fix P at (2, 4). As Q slides toward P with shrinking h, the secant line rotates smoothly, hugging the curve tighter and tighter. As h approaches zero, the secant becomes the tangent line with an exact slope of 4."
        },
        {
            "num": "SCENE 4",
            "title": "Step-by-Step Worked Derivation — Analytical Proof",
            "duration": "Approx. 70 seconds",
            "objective": "Rigorously derive f'(2) = 4 using difference quotient limit, justifying h != 0 cancellation.",
            "visuals": "Clean algebraic workspace. Reveal step-by-step: derivative definition, evaluate f(2)=4 and f(2+h)=4+4h+h², substitute into difference quotient, cancel 4 and -4, factor h(4+h)/h, highlight valid cancellation rule h != 0, evaluate limit as h->0 = 4. Box final result.",
            "math": "f'(a) = lim_{h->0} [f(a+h) - f(a)] / h\nf'(2) = lim_{h->0} [(4+4h+h²) - 4] / h\n      = lim_{h->0} [4h + h²] / h\n      = lim_{h->0} (4 + h)  [for h != 0]\n      = 4 + 0 = 4",
            "narration": "The formal definition of derivative is the limit of the difference quotient. Substituting f(2)=4 and expanding (2+h)² gives 4+4h+h². After subtracting 4 and dividing by h (valid because h != 0), we get 4+h. As h approaches 0, the limit is exactly 4."
        },
        {
            "num": "SCENE 5",
            "title": "What Does the Answer Mean? — Geometric Meaning",
            "duration": "Approx. 45 seconds",
            "objective": "Connect the algebraic result f'(2)=4 back to geometry, tangent line equation, and rate of change.",
            "visuals": "Zoomed view of y = x² at (2, 4). Bold green tangent line y = 4x - 4. Slope triangle with run=1, rise=4. Direct visual side-by-side comparison between secant (two points, average rate) and tangent (one point, instantaneous rate).",
            "math": "Point-Slope Form: y - y1 = m(x - x1)\ny - 4 = 4(x - 2) => y = 4x - 4\nLocal tangency verified: x² - (4x - 4) = (x - 2)² >= 0",
            "narration": "The derivative 4 represents the exact instantaneous rate of change at x = 2. It is the slope of the unique tangent line touching the curve at (2, 4). While a secant cuts through two points, the tangent gives the curve's instantaneous direction."
        },
        {
            "num": "SCENE 6",
            "title": "Summary & Credits — Key Takeaways & Attribution",
            "duration": "Approx. 35 seconds",
            "objective": "Consolidate the three core takeaways, highlight the central theme, and present academic credits.",
            "visuals": "Three structured takeaway cards: (1) Secant = Average Rate, (2) Tangent = Instantaneous Rate, (3) Derivative = Limit of Secant Slopes. Final equation banner: f'(2) = 4. Closing motto: 'From two points to one tangent.' Academic credits card with references and AI disclosure.",
            "math": "f'(2) = lim_{h->0} Delta y / Delta x = 4\nTangent equation: y = 4x - 4",
            "narration": "Remember: secants measure average rate, tangents measure instantaneous rate, and the derivative is the bridge connecting them via limits. From two points to one tangent: that is the essence of calculus."
        }
    ]
    
    for idx, sc in enumerate(scenes_data):
        scene_content = []
        
        # Scene heading banner
        header_text = f"<b>{sc['num']} — {sc['title']}</b>"
        scene_content.append(Paragraph(header_text, h1_style))
        
        # Details table
        table_rows = [
            [
                Paragraph("<b>Duration:</b>", label_style),
                Paragraph(sc['duration'], body_style)
            ],
            [
                Paragraph("<b>Objective:</b>", label_style),
                Paragraph(sc['objective'], body_style)
            ],
            [
                Paragraph("<b>Visual Elements:</b>", label_style),
                Paragraph(sc['visuals'], body_style)
            ],
            [
                Paragraph("<b>Mathematical Content:</b>", label_style),
                Paragraph(sc['math'].replace("\n", "<br/>"), math_style)
            ],
            [
                Paragraph("<b>Narration Summary:</b>", label_style),
                Paragraph(f"<i>\"{sc['narration']}\"</i>", body_style)
            ]
        ]
        
        scene_table = Table(table_rows, colWidths=[100, 404])
        scene_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#EDF2F7")),
        ]))
        
        scene_content.append(scene_table)
        scene_content.append(Spacer(1, 12))
        
        # Keep each scene together so it doesn't break awkwardly across pages
        story.append(KeepTogether(scene_content))
        
        # Page breaks to keep layout clean (e.g. 2 scenes per page)
        if idx in [1, 3]:
            story.append(PageBreak())

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_pdf()
