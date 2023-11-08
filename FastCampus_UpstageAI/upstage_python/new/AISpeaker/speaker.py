import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#음성 이식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text = r.recognize_google(audio, language='ko')
        print('[사람]'+ text)
        
    except sr.UnknownValueError:
        print('인식 실패')
        
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) #APT KEY 오류, 네트워크 단절 등

#대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다'
    elif '종료' in input_text:
        answer_text = '종료하셨습니다'
        stop_listening(wait_for_stop=False)  더 이상 듣지 않음
    else:
        answer_text = '다음에 또 만나요'

#소리내어 읽기(TTS)
def speak(text):
    print('[인공지능]'+ text)
    file_name = 'vocie.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)
    
r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
# 

while True:
    time.sleep(0.1)