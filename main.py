from core.listen import record_audio


def main():
    print("JARVIS is listening...")

    audio_file = record_audio(duration=5)

    if audio_file:
        print("🎧 Audio captured successfully.")
    else:
        print("⚠️ No usable audio.")


if __name__ == "__main__":
    main()