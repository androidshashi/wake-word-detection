import pvporcupine
import pyaudio
import struct
from config.config import WAKE_WORD_PATH
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
PORCUPINE_ACCESS_KEY = os.getenv("PORCUPINE_ACCESS_KEY")

def wake_word_listener():
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_ACCESS_KEY,
        keyword_paths=[WAKE_WORD_PATH]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=porcupine.sample_rate,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🎤 Listening for 'Zoya'...")

    try:
        while True:
            audio_data = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, audio_data)

            result = porcupine.process(pcm)
            if result >= 0:
                print("✅ Wake word 'Zoya' detected!")
                # Trigger your assistant logic here
                break

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    wake_word_listener()
