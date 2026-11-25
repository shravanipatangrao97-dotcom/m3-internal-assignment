"""
Main runner for the M3 Derivative Animation project.
Allows rendering individual scenes or all six scenes in sequence.
"""
import argparse
import sys
import os

from scenes.scene_01_hook import Scene01Hook
from scenes.scene_02_concept import Scene02Concept
from scenes.scene_03_secant_tangent import Scene03SecantTangent
from scenes.scene_04_derivation import Scene04Derivation
from scenes.scene_05_interpretation import Scene05Interpretation
from scenes.scene_06_summary import Scene06Summary

SCENES = {
    1: ("Scene01Hook", Scene01Hook, "scenes/scene_01_hook.py"),
    2: ("Scene02Concept", Scene02Concept, "scenes/scene_02_concept.py"),
    3: ("Scene03SecantTangent", Scene03SecantTangent, "scenes/scene_03_secant_tangent.py"),
    4: ("Scene04Derivation", Scene04Derivation, "scenes/scene_04_derivation.py"),
    5: ("Scene05Interpretation", Scene05Interpretation, "scenes/scene_05_interpretation.py"),
    6: ("Scene06Summary", Scene06Summary, "scenes/scene_06_summary.py"),
}

def main():
    parser = argparse.ArgumentParser(description="Render M3 Derivative Animation Scenes")
    parser.add_argument("--scene", type=int, choices=[1, 2, 3, 4, 5, 6], help="Scene number to render (1-6)")
    parser.add_argument("--all", action="store_true", help="Render all 6 scenes")
    parser.add_argument("-q", "--quality", choices=["l", "m", "h", "k"], default="h", help="Quality: l (480p), m (720p), h (1080p), k (4k)")
    
    args = parser.parse_args()
    
    if not args.scene and not args.all:
        parser.print_help()
        sys.exit(1)
        
    targets = list(SCENES.keys()) if args.all else [args.scene]
    
    for s_num in targets:
        name, cls, path = SCENES[s_num]
        print(f"\n==========================================")
        print(f" Rendering Scene {s_num}: {name} ({args.quality} quality)")
        print(f"==========================================\n")
        cmd = f"manim -q{args.quality} {path} {name}"
        exit_code = os.system(cmd)
        if exit_code != 0:
            print(f"Error rendering Scene {s_num}!")
            sys.exit(exit_code)
            
    print("\nAll requested scenes rendered successfully!")

if __name__ == "__main__":
    main()
