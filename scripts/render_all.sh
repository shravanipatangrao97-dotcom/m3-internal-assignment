#!/usr/bin/env bash
set -e

# Change to project root directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

echo "=========================================================="
echo " M3 Calculus Assignment: The Derivative Animation Pipeline"
echo " Student: Shravani Patil"
echo "=========================================================="

# Activate virtual environment if present
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

QUALITY="${1:--qh --fps 30}"
echo "Using render quality: $QUALITY"

echo ""
echo ">>> Rendering Scene 1: The Hook..."
manim $QUALITY scenes/scene_01_hook.py Scene01Hook

echo ""
echo ">>> Rendering Scene 2: Understanding the Concept..."
manim $QUALITY scenes/scene_02_concept.py Scene02Concept

echo ""
echo ">>> Rendering Scene 3: Secant to Tangent..."
manim $QUALITY scenes/scene_03_secant_tangent.py Scene03SecantTangent

echo ""
echo ">>> Rendering Scene 4: Step-by-Step Worked Derivation..."
manim $QUALITY scenes/scene_04_derivation.py Scene04Derivation

echo ""
echo ">>> Rendering Scene 5: What Does the Answer Mean?..."
manim $QUALITY scenes/scene_05_interpretation.py Scene05Interpretation

echo ""
echo ">>> Rendering Scene 6: Summary and Credits..."
manim $QUALITY scenes/scene_06_summary.py Scene06Summary

echo ""
echo ">>> Assembling all 6 scenes into final 1080p video..."
python3 scripts/assemble_video.py

echo ""
echo ">>> Generating Storyboard PDF..."
python3 scripts/generate_storyboard_pdf.py

echo ""
echo "=========================================================="
echo " Render & Assembly Completed Successfully!"
echo " Final Video: output/final_animation_1080p.mp4"
echo " Storyboard:  storyboard/storyboard.pdf"
echo "=========================================================="
