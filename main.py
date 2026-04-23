from core.listen import record_audio


def main():
    print("JARVIS listening...")

    audio = record_audio(duration=5)

    if audio:
        print("Audio captured successfully")
    else:
        print("No usable audio")


if __name__ == "__main__":
    main()