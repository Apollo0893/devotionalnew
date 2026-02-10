
from flask import Flask, render_template, request, redirect, send_from_directory
import os, json
from generator import create_devotional, pick_songs
from tts import run_tts

app = Flask(__name__)
OUTPUT="/app/output"
MUSIC="/app/music"

def get_archives():
    return sorted([d for d in os.listdir(OUTPUT) if os.path.isdir(f"{OUTPUT}/{d}")], reverse=True)

@app.route("/")
def home():
    return render_template("index.html", archives=get_archives())

@app.route("/generate")
def generate():
    topic=request.args.get("topic","Peace")
    voice=request.args.get("voice","en-US-AriaNeural")

    base,text=create_devotional(topic)
    audio=f"{base}/devotional.mp3"
    run_tts(text,voice,audio)

    pre,post=pick_songs()
    open(f"{base}/playlist.json","w").write(json.dumps({"pre":pre,"post":post}))
    return redirect("/")

@app.route("/upload",methods=["POST"])
def upload():
    f=request.files["song"]
    if f:
        f.save(f"{MUSIC}/{f.filename}")
    return redirect("/")

@app.route("/output/<path:p>")
def out(p):
    return send_from_directory(OUTPUT,p)

@app.route("/music/<path:p>")
def mus(p):
    return send_from_directory(MUSIC,p)

app.run(host="0.0.0.0",port=8095)
