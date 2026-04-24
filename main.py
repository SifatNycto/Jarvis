from core.listen import record_audio
from core.transcribe import transcribe_audio
from core.brain import ask_llm
from core.speak import speak


def main():
    print("🤖 JARVIS is online... (say 'shutdown' to stop)\n")

    while True:
        audio_file = record_audio(duration=7)
        if not audio_file:
            continue

        text = transcribe_audio(audio_file)
        if not text:
            continue

        # Exit condition
        if "shutdown" in text.lower():
            print("👋 Shutting down JARVIS...")
            break

        reply = ask_llm(text)

        if reply:
            speak(reply)


if __name__ == "__main__":
    main()