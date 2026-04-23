from core.listen import record_audio
from core.transcribe import transcribe_audio
from core.brain import ask_llm


def main():
    print("JARVIS is listening...")

    audio_file = record_audio(duration=5)
    if not audio_file:
        return

    text = transcribe_audio(audio_file)
    if not text:
        return

    ask_llm(text)


if __name__ == "__main__":
    main()