import os 
import env 
import re 
import speech_recognition as sr
from itertools import zip_longest
import ffmpeg 
import vlc 

# a = sr.Recognizer()

# wav_dir = r"F:\test_wav"
# sort = sorted(os.listdir(wav_dir), key=lambda x: int(re.search(r'\d+', x).group()))
# for i,wav_file in enumerate(sort):
#     abs_file = os.path.join(wav_dir, wav_file)
#     try:
#         with sr.AudioFile(abs_file) as source:
#             b = a.record(source)
#             text = a.recognize_google(b, language='en-US')
            
#             with open(rf"F:\test_srt/output{i}.srt", 'w') as f:
#                 f.write(f'{i + 1}\n')
#                 f.write(f'00:00:00,000 --> 00:00:02,000\n')
#                 f.write(text)
            
#     except sr.exceptions.UnknownValueError as e:
#         continue


def test():
    wav = os.listdir(r"F:\test_wav")
    srt = os.listdir(r"F:\test_srt")
    mp4 = os.listdir(r"F:\test_mp4")
    wav_sort = sorted(wav, key=lambda x: int(re.search(r'\d+', x).group()))
    srt_sort = sorted(srt, key=lambda x: int(re.search(r'\d+', x).group()))
    mp4_sort = sorted(mp4, key=lambda x: int(re.search(r'\d+', x).group()))
    
    mkv = r"F:\test_mkv"
    
    i = 0
    
    for wav_file, srt_file, mp4_file in zip_longest(wav_sort, srt_sort, mp4_sort):
        try:
            if srt_file is None:
                wav = rf"F:\test_wav\{wav_file}"
                mp4 = rf"F:\test_mp4\{mp4_file}"
                
                a = ffmpeg.input(wav)
                c = ffmpeg.input(mp4)
                
                output = (
                    ffmpeg.output(c['v'], a['a'], os.path.join(mkv, f'output{i}.mkv'), c='copy')
                )
                ffmpeg.run(output)
                
                i += 1
                
            else:
                wav = rf"F:\test_wav\{wav_file}"
                srt = rf"F:\test_srt\{srt_file}"
                mp4 = rf"F:\test_mp4\{mp4_file}"
                
                a = ffmpeg.input(wav)
                b = ffmpeg.input(srt)
                c = ffmpeg.input(mp4)
                
                output = (
                    ffmpeg.output(c['v'], a['a'], b['s'], os.path.join(mkv, f'output{i}.mkv'), c='copy')
                )
                ffmpeg.run(output)
                
                i += 1
        except Exception as e:
            print('ファイルが見つからなかったのでスキップします。', e)
    
    # instance = vlc.Instance('--sub-source=marq')
    # player = instance.media_player_new()
    # media = instance.media_new(mkv)
    # player.set_media(media)
    # player.play()
    
    # while True:
    #     continue
    
    
test()