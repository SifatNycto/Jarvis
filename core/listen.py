import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

SAMPLE_RATE = 16000  # Best for speech models


def record_audio(filename="output.wav", duration=5):
    try:
        print("🎤 Speak now... (about to record)")

        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()
        
        print("Max audio level:", np.max(np.abs(audio)))

        # Check silence
        if np.max(np.abs(audio)) < 500:
            print("⚠️ No sound detected")
            return None

        write(filename, SAMPLE_RATE, audio)

        print(f"✅ Audio saved as {filename}")
        return filename

    except Exception as e:
        print(f"❌ Microphone error: {e}")
        return None