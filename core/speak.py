import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')


# 👇 TEMP DEBUG (ADD THIS) || for checking voice model
# for v in voices:
#     print(v.id)

    
engine.setProperty('voice', voices[1].id)


def speak(text):
    try:
        print("🔊 Speaking...")
        
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"❌ TTS error: {e}")
