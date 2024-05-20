# import ffmpeg 
import os 
from moviepy.editor import VideoFileClip
import speech_recognition as sr

import env

soccer_mp4 = env.os.environ.get('MP4_FILE')

mp4_wav = env.os.environ.get('WAV_FILE')

# mp4ファイルをwavファイルに変換
clip = VideoFileClip(soccer_mp4)
clip.audio.write_audiofile(os.path.join(test_wav, 'output.wav'))

# wavファイルからテキストを抽出
r = sr.Recognizer()
try:
    with sr.AudioFile(mp4_wav) as source:
        audio = r.record(source)
        
        text = r.recognize_google(audio, language='en-US')
        # テキスト抽出
        print(text)
        
except Exception as e:
    print('エラーが出ました。', e)

