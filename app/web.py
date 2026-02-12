import os
import datetime
from flask import Flask, render_template, send_file, request, redirect
from generator import build_devotional
from tts import narrate
from audio_builder import build_final_audio

app = Flask(__name__)

OUTPUT_DIR = "output"
MUSIC_DIR = "music"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

VOICE = os.getenv("VOICE", "en-US-AriaNeural")
TOPIC = os.getenv("WEEKLY_TOPIC", "Faith")

def today_folder():
d = datetime.date.today().isoformat()
folder = os.path.join(OUTPUT_DIR, d)
os.makedirs(folder, exist_ok=True)
return folder

@app.route("/")
def index():
archives = sorted(os.listdir(OUTPUT_DIR), reverse=True)
return render_template("index.html", archives=archives)

@app.route("/generate")
def generate():
try:
topic = request.args.get("topic", TOPIC)
voice = request.args.get("voice", VOICE)

```
    folder = today_folder()

    print("Generating devotional on:", topic)

    text = build_devotional(topic)

    text_file = os.path.join(folder, "devotional.txt")
    with open(text_file, "w", encoding="utf-8") as f:
        f.write(text)

    narration_mp3 = os.path.join(folder, "narration.mp3")
    final_mp3 = os.path.join(folder, "final.mp3")

    print("Running TTS...")
    narrate(text, voice, narration_mp3)

    print("Adding music...")
    build_final_audio(narration_mp3, MUSIC_DIR, final_mp3)

    return redirect("/")

except Exception as e:
    print("ERROR:", e)
    return f"Generation failed: {e}"
```

@app.route("/play/<date>")
def play(date):
path = os.path.join(OUTPUT_DIR, date, "final.mp3")
return send_file(path, mimetype="audio/mpeg")

@app.route("/upload", methods=["POST"])
def upload():
file = request.files.get("file")
if not file:
return redirect("/")

```
save_path = os.path.join(MUSIC_DIR, file.filename)
file.save(save_path)
return redirect("/")
```

@app.route("/archive/<date>")
def archive(date):
text_path = os.path.join(OUTPUT_DIR, date, "devotional.txt")

```
text = ""
if os.path.exists(text_path):
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

return render_template("archive.html", date=date, text=text)
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=8095)

