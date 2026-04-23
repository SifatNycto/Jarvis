from faster_whisper import WhisperModel

# Load model once (important)
model_size = "base"
model = WhisperModel(model_size, compute_type="int8")


def transcribe_audio(audio_path):
    try:
        segments, _ = model.transcribe(audio_path)

        text = ""
        for segment in segments:
            text += segment.text

        text = text.strip()

        if not text:
            print("⚠️ No speech detected")
            return None

        print(f"🧠 You said: {text}")
        return text

    except Exception as e:
        print(f"❌ Transcription error: {e}")
        return None