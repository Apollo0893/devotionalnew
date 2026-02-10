
import edge_tts, asyncio

async def narrate(text, voice, out):
    tts = edge_tts.Communicate(text, voice)
    await tts.save(out)

def run_tts(text, voice, out):
    asyncio.run(narrate(text, voice, out))
