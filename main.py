from core.listen import record_audio
from core.transcribe import transcribe_audio


def main():
    print("JARVIS is listening...")

    audio_file = record_audio(duration=5)

    if not audio_file:
        print("⚠️ No usable audio")
        return

    text = transcribe_audio(audio_file)

    if text:
        print("✅ Transcription complete")
    else:
        print("⚠️ Could not understand audio")


if __name__ == "__main__":
    main()