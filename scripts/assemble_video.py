"""
Assemble rendered Manim scenes into the final video deliverable.
"""
import os
import subprocess
import glob
import sys

SCENE_NAMES = [
    "Scene01Hook",
    "Scene02Concept",
    "Scene03SecantTangent",
    "Scene04Derivation",
    "Scene05Interpretation",
    "Scene06Summary",
]

def find_scene_video(scene_name, quality="1080p30"):
    # Check media/videos/scene_XX/quality/scene_name.mp4 or media/videos/1080p30/
    patterns = [
        f"media/videos/*/{quality}/{scene_name}.mp4",
        f"media/videos/*/*/{scene_name}.mp4",
        f"media/videos/**/{scene_name}.mp4",
    ]
    for pat in patterns:
        matches = glob.glob(pat, recursive=True)
        if matches:
            # Sort by modification time, newest first
            matches.sort(key=os.path.getmtime, reverse=True)
            return matches[0]
    return None

def assemble(output_file="output/final_animation_1080p.mp4"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print("Locating rendered scene videos...")
    scene_files = []
    for s_name in SCENE_NAMES:
        fpath = find_scene_video(s_name)
        if not fpath:
            print(f"Error: Could not find rendered video for {s_name}!")
            print("Please render all scenes first.")
            sys.exit(1)
        scene_files.append(fpath)
        print(f"  Found {s_name}: {fpath}")
        
    concat_list_path = "output/concat_list.txt"
    with open(concat_list_path, "w") as f:
        for fpath in scene_files:
            abs_path = os.path.abspath(fpath)
            f.write(f"file '{abs_path}'\n")
            
    print(f"\nAssembling {len(scene_files)} scenes into {output_file}...")
    
    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        output_file
    ]
    
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        print("Error during video assembly with ffmpeg:")
        print(res.stderr.decode())
        sys.exit(1)
        
    print(f"\nFinal video successfully assembled at: {output_file}")
    
    # Run ffprobe to verify
    probe_cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration,size:stream=width,height,r_frame_rate,codec_name",
        "-of", "default=noprint_wrappers=1",
        output_file
    ]
    probe_res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("\n--- FFprobe Video Metadata Verification ---")
    print(probe_res.stdout.decode().strip())
    print("-------------------------------------------\n")

if __name__ == "__main__":
    assemble()
