import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

SAMPLE_RATE = 16000


def record_audio(filename="output.wav", duration=5):
    try:
        print("🎤 Speak now...")

        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        # check if silent
        if np.max(audio) == 0:
            print("⚠️ No sound detected")
            return None

        write(filename, SAMPLE_RATE, audio)

        print(f"✅ Saved: {filename}")
        return filename

    except Exception as e:
        print(f"❌ Error: {e}")
        return None