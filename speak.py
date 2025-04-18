
import pyttsx3

def speak(text, voice_id=None, rate=150):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Text to speak")
    parser.add_argument("--voice", help="Voice ID")
    parser.add_argument("--rate", type=int, default=150)

    args = parser.parse_args()
    speak(args.text, args.voice, args.rate)
