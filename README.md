# The Derivative — From Secant to Tangent

**Student:** Shravani Patil  
**Subject:** Linear Algebra and Calculus (M3)  
**Assessment:** Internal Assessment Project  
**Repository:** [https://github.com/shravanipatangrao97-dotcom/m3-internal-assignment](https://github.com/shravanipatangrao97-dotcom/m3-internal-assignment)  

---

## 1. Project Overview

This project provides an original, mathematically rigorous, and visually elegant animation that teaches the fundamental concept of the derivative through the geometric transition from a **secant line** (average rate of change) to a **tangent line** (instantaneous rate of change).

The entire demonstration focuses on the canonical quadratic model:
$$f(x) = x^2$$

We compute and visualize the exact instantaneous rate of change at:
$$a = 2$$

Final derivative result:
$$f'(2) = 4$$

Tangent line equation:
$$y = 4x - 4$$

---

## 2. Mathematical Content & Derivation Summary

1. **Average Rate of Change:**
   $$\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$$
   Geometrically represents the slope of a secant line connecting two points $P$ and $Q$.

2. **Parametric Setup:**
   For $x_1 = 2$ and $x_2 = 2 + h$:
   $$f(2) = 4, \quad f(2+h) = (2+h)^2 = 4 + 4h + h^2$$

3. **Difference Quotient Simplification:**
   $$\frac{f(2+h) - f(2)}{h} = \frac{(4+4h+h^2) - 4}{h} = \frac{4h + h^2}{h} = \frac{h(4+h)}{h}$$
   For $h \neq 0$, division by $h$ is mathematically valid:
   $$m_{\text{sec}} = 4 + h$$

4. **Limit Evaluation:**
   $$f'(2) = \lim_{h \to 0} (4 + h) = 4$$

5. **Numerical Convergence:**
   - $h = 2.0 \implies m = 6.0$
   - $h = 1.0 \implies m = 5.0$
   - $h = 0.5 \implies m = 4.5$
   - $h = 0.2 \implies m = 4.2$
   - $h = 0.1 \implies m = 4.1$
   - Limit as $h \to 0 \implies m = 4.0$ (Tangent line slope)

---

## 3. Deliverables

- **Final 1080p Video:** `output/final_animation_1080p.mp4` (1920x1080, 30 fps, H.264)
- **Storyboard PDF:** `storyboard/storyboard.pdf` (6-scene specification generated with ReportLab)
- **Mathematical Verification:** `docs/mathematical_verification.md`
- **Narration Script:** `docs/narration_script.md`
- **Storyboard Specification:** `docs/storyboard.md`
- **References & AI Disclosure:** `docs/references.md`
- **Executable Pipeline Script:** `scripts/render_all.sh`

---

## 4. Project Structure

```
m3-internal-assignment/
├── scenes/
│   ├── __init__.py
│   ├── helpers.py                 # Shared palette, styling, and LaTeX-free UI helpers
│   ├── scene_01_hook.py           # Scene 1: Paradox of Instantaneous Speed
│   ├── scene_02_concept.py        # Scene 2: Secant Line & Average Rate of Change
│   ├── scene_03_secant_tangent.py # Scene 3: Geometric Convergence (h -> 0)
│   ├── scene_04_derivation.py     # Scene 4: Step-by-Step Analytical Derivation
│   ├── scene_05_interpretation.py # Scene 5: Tangent Line & Meaning of Slope
│   └── scene_06_summary.py        # Scene 6: Core Takeaways & Project Credits
├── docs/
│   ├── mathematical_verification.md
│   ├── narration_script.md
│   ├── storyboard.md
│   └── references.md
├── storyboard/
│   └── storyboard.pdf
├── output/
│   └── final_animation_1080p.mp4
├── scripts/
│   ├── render_all.sh              # Full render and build pipeline
│   ├── assemble_video.py          # Scene concatenation and metadata check
│   └── generate_storyboard_pdf.py # ReportLab PDF generator
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 5. Setup & Execution Instructions

### Prerequisites
- Python 3.12+
- FFmpeg (for video concatenation and audio handling)

### Installation
```bash
# Clone the repository
git clone https://github.com/shravanipatangrao97-dotcom/m3-internal-assignment.git
cd m3-internal-assignment

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Rendering

**Render all scenes and build final video:**
```bash
./scripts/render_all.sh
```

**Or render individual scenes:**
```bash
# Scene 1
manim -qh --fps 30 scenes/scene_01_hook.py Scene01Hook

# Scene 3 (visual highlight)
manim -qh --fps 30 scenes/scene_03_secant_tangent.py Scene03SecantTangent
```

**Generate Storyboard PDF:**
```bash
python3 scripts/generate_storyboard_pdf.py
```

**Assemble final deliverable:**
```bash
python3 scripts/assemble_video.py
```

---

## 6. Technical Video Verification

Verified via `ffprobe`:
- **Format:** MP4 (H.264 video, yuv420p)
- **Resolution:** 1920 × 1080 (16:9 Landscape)
- **Framerate:** 30 FPS
- **Total Duration:** 209.6 seconds (~3 minutes 30 seconds, compliant with the 7-minute limit)
- **File Size:** ~7.08 MB

---

## 7. Voiceover Synchronization

A student-friendly narration script is provided at `docs/narration_script.md`.

To merge a recorded voiceover track:
```bash
ffmpeg -i output/final_animation_1080p.mp4 -i assets/audio/voiceover.wav -c:v copy -c:a aac -b:a 192k -shortest output/final_submission_with_voiceover.mp4
```

---

## 8. Academic Integrity & References

- Standard university calculus syllabus references (differential calculus, rates of change, difference quotient limits).
- Architecture inspired by educational animations from Grant Sanderson (3Blue1Brown) and the `m3-manim-animation-kit` starter reference.
- AI Assistant Disclosure: Developed with assistance from Antigravity (Gemini) for coding, debugging, rendering workflows, and document generation.
