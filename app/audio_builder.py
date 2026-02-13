import os
import random
import subprocess

def build_final_audio(narration_mp3, music_dir, output_mp3):
    songs = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]

    if not songs:
        # no music → just copy narration
        subprocess.run(["cp", narration_mp3, output_mp3])
        return

    random.shuffle(songs)

    intro = os.path.join(music_dir, songs[0])
    outro = [os.path.join(music_dir, s) for s in songs[1:3]]

    files = [intro, narration_mp3] + outro

    concat_list = "/tmp/concat.txt"
    with open(concat_list, "w") as f:
        for path in files:
            f.write(f"file '{os.path.abspath(path)}'\n")

    subprocess.run([
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        output_mp3
    ])
