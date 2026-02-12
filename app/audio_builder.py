from pydub import AudioSegment
import os, random

def build_final_audio(narration_path, music_folder, output):
    narration = AudioSegment.from_mp3(narration_path)

    songs = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    if not songs:
        narration.export(output, format="mp3")
        return

    random.shuffle(songs)

    intro = AudioSegment.from_mp3(os.path.join(music_folder, songs[0]))
    outros = [AudioSegment.from_mp3(os.path.join(music_folder, s)) for s in songs[1:]]

    final = intro + narration

    for o in outros:
        final += o

    final.export(output, format="mp3")
