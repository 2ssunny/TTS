from gtts import gTTS


def gtts_test(text: str) -> None:
    tts = gTTS(text)
    tts.save(f"{text}.mp3")


txt = open("tts.txt", "r", encoding="utf-8")
call = txt.readlines()
txt.close()
for i in range(0, len(call)):
    gtts_test(call[i].replace("\n", ""))
