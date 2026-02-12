import os, requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

def generate_reflection(topic, verses):
    try:
        prompt = f"""
Write a 15 minute Christian devotional about {topic}.

Include:
- engaging pastoral tone
- explanation of verses
- life application
- prayer at end

Verses:
{verses}
"""

        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        return r.json()["response"]

    except Exception as e:
        print("LLM ERROR:", e)
        return f"Let us reflect today on {topic} and seek wisdom in God's word."
