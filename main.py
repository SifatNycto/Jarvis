from features.image_gen import generate_image
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

        text_lower = text.lower()  # ✅ process once

        # 🔻 Exit condition
        if any(cmd in text_lower for cmd in ["shutdown", "shut down", "power off"]):
            print("👋 Shutting down JARVIS...")
            break

        # 🖼️ Image command detection (IMPROVED)
        if "generate" in text_lower and "image" in text_lower:
            # Remove trigger words cleanly
            prompt = text_lower.replace("generate", "").replace("image", "").strip()

            if not prompt:
                speak("What image should I generate?")
                continue

            filepath = generate_image(prompt)

            if filepath:
                speak("Image generated and saved.")
            else:
                speak("Failed to generate image.")

            continue  # skip normal AI

        # 🤖 Normal AI response
        reply = ask_llm(text)

        if reply:
            speak(reply)


if __name__ == "__main__":
    main()