import os 
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

import env
import deepl

########################################################
# mp4ファイルを用意し、wavファイルに変換とsrtファイル作成
########################################################

def wav_and_srt(mp4_file, wav_dir, srt_dir):
    # mp4ファイルをwavファイルに変換
    clip = VideoFileClip(mp4_file)
    clip.audio.write_audiofile('output.wav')

    clip_duration = clip.duration


    # wavファイルの長さを2秒間隔で分割していく
    if clip_duration >= 2:
        audio_segment = AudioSegment.from_wav('output.wav')
        # clip.durationの長さは約67秒。 それを割り算する。67 ÷ 2 = 33　切り捨ては除算される。
        n_chunks = int(clip_duration // 2) # ここに33つ分に分割されたリストが格納されている。

        for i in range(n_chunks):
            # audio_segmentは1000ミリ秒だから、×1000にしないとダメらしい。
            start_time = i * 2 * 1000 
            end_time = (i+1) * 2 * 1000 
            chunk = audio_segment[start_time:end_time]
            chunk_path = os.path.join(env.os.environ.get('WAV_DIRECTORY'), f'output{i}.wav')
            chunk.export(chunk_path, format='wav')
                

    import re 
    # wavファイルからテキストを抽出
    r = sr.Recognizer()
    wav_list = os.listdir(wav_dir)
    wav_sort = sorted(wav_list, key=lambda x: int(re.search(r'\d+', x).group()))

    for i, wav_file in enumerate(wav_sort):
        srt_file = os.path.join(r"F:\test_srt", f'subtitle{i}.srt')
        wav_file = os.path.join(wav_dir, wav_file)
        try:
            with sr.AudioFile(wav_file) as source:
                # audioに一気にテキストが表示される。 話すたびにテキストに抽出するには分割するべきなのか。違うやり方があるかもしれない。
                audio = r.record(source)
                
                # テキスト抽出
                text = r.recognize_google(audio, language='en-US')
                text = deepl.deepl(text)
                
                with open(rf"F:\test_srt/subtitle{i}.srt", 'w', encoding='utf-8') as f:
                    f.write(f'{i + 1}\n')
                    f.write(f'00:00:00,000 --> 00:00:02,000\n')
                    f.write(text)
                
        except Exception as e:
            print('音声を読み取れませんでした。', e)
            continue

