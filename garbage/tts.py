from gtts import gTTS
import os

def text_to_speech_gtts(text, filename="output.mp3", lang='ru'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    return True

if __name__ == "__main__":
    user_text = input()

    if not user_text.strip():
        exit()

    filename = "output.mp3"
    lang = "en"

    success = text_to_speech_gtts(user_text, filename, lang)
 
    if success:
        file_path = os.path.abspath(filename)
