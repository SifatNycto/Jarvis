import pyttsx3


def speak(text):
    try:
        engine = pyttsx3.init()  # 🔥 create fresh engine every time

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # change index if needed

        engine.setProperty('rate', 175)  # optional: speed

        print("🔊 Speaking...")

        engine.say(text)
        engine.runAndWait()

        engine.stop()  # 🔥 important cleanup

    except Exception as e:
        print(f"❌ TTS error: {e}")