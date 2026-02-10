
import os, datetime, random, requests

def fetch_devotional(topic):
    verses = [f"{topic} scripture {i+1}" for i in range(10)]
    text = f"Daily devotional on {topic}.\n" + "\n".join(verses)
    return text

def fetch_image(topic, save_path):
    try:
        url = f"https://source.unsplash.com/800x600/?{topic},faith"
        r = requests.get(url, timeout=15)
        open(save_path,"wb").write(r.content)
    except:
        pass

def pick_songs():
    songs = [f for f in os.listdir("/app/music") if f.endswith(".mp3")]
    random.shuffle(songs)
    if not songs:
        return [],[]
    return songs[:1], songs[1:4]

def create_devotional(topic):
    today = datetime.date.today().isoformat()
    base = f"/app/output/{today}"
    os.makedirs(base, exist_ok=True)

    text = fetch_devotional(topic)
    open(f"{base}/devotional.txt","w").write(text)
    fetch_image(topic, f"{base}/image.jpg")

    return base, text
