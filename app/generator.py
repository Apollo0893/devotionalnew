import os
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
MODEL = os.getenv("OLLAMA_MODEL", "llama3")

def build_devotional(topic):
    prompt = f"""
Create a powerful 3-4 minute Christian devotional about: {topic}

Structure:
- Title
- Opening prayer
- Scripture references
- Deep reflection
- Encouragement
- Closing prayer

Make it emotionally moving and pastoral.
"""

    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        if r.status_code == 200:
            return r.json()["response"]

    except Exception as e:
        print("LLM not reachable:", e)

    # Fallback devotional if ollama fails
    return f"""
Daily Devotional: {topic}

Scripture:
"Be strong and courageous. Do not be afraid." – Joshua 1:9

Reflection:
Today we reflect on {topic}. Even when life feels uncertain,
God is guiding each step. Walk forward in faith knowing He
goes before you.

Prayer:
Lord, strengthen our hearts today. Help us walk in faith and
trust your plan. Amen.
"""
