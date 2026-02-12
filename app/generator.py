from llm_reflector import generate_reflection
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
    verses = get_verses(topic, 12)

    reflection = generate_reflection(topic, verses)

    devotional = f"""
Daily Devotional — {topic}

Scripture:
{verses}

Reflection:
{reflection}

Closing Prayer:
Lord, guide us today and help us walk in faith. Amen.
"""

    # enforce minimum 15 min spoken length
    if len(devotional.split()) < 1800:
        devotional += "\n\n" + reflection * 3

    return devotional

