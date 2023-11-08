# TTS (Text to Speech)
# STT (Speech to Text)

from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'

# 영어
# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)
# playsound(file_name)


# # 한국어
# text = '파이썬을 배우면 이런 것도 할 수 있어요'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save('sample.mp3')
# playsound(file_name) #.mp3 파일 재생


#긴문장 (파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save('sample.mp3')
playsound(file_name) #.mp3 파일 재생