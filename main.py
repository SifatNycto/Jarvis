from core.listen import record_audio
from core.transcribe import transcribe_audio
from core.brain import ask_llm
from core.speak import speak


def main():
    print("JARVIS is listening...")

    audio_file = record_audio(duration=7)
    if not audio_file:
        return

    text = transcribe_audio(audio_file)
    if not text:
        return

    reply = ask_llm(text)

    if reply:
        speak(reply)


if __name__ == "__main__":
    main()