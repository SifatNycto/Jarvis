import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import os

SAMPLE_RATE = 16000  # Whisper prefers 16kHz


def record_audio(filename="output.wav", duration=5):
    try:
        print(f"🎤 Recording for {duration} seconds...")

        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # Check if audio is silent
        if np.max(audio) == 0:
            print("⚠️ No sound detected.")
            return None

        write(filename, SAMPLE_RATE, audio)
        print(f"✅ Audio saved as {filename}")

        return filename

    except Exception as e:
        print(f"❌ Microphone error: {e}")
        return None