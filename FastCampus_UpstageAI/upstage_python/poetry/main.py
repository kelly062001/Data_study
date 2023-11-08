from gtts import gTTS

comment = "환영합니다"

comment_to_voice = gTTS(text=comment, lang='ko')
comment_to_voice.save('test_ko.mp3')
