import os 
import ffmpeg 
from itertools import zip_longest
import re 

import env

def create_mkv(mp4_input, audio_input, subtitle_input, output_path):
    # MP4 ファイル、オーディオ、字幕を組み合わせて MKV ファイルを作成する関数
    output = ffmpeg.output(mp4_input['v'], audio_input['a'], subtitle_input['s'], output_path, c='copy')
    ffmpeg.run(output)

def main(wav_sort, srt_sort, mp4_sort, wav_dir, mp4_dir, srt_dir, mkv_dir):
    for i, (mp4_file, wav_file, srt_file) in enumerate(zip_longest(mp4_sort, wav_sort, srt_sort)):
        try:
            mp4_path = os.path.join(mp4_dir, mp4_file) if mp4_file else None
            wav_path = os.path.join(wav_dir, wav_file) if wav_file else None
            srt_path = os.path.join(srt_dir, srt_file) if srt_file else None
            output_path = os.path.join(mkv_dir, f'output{i}.mkv')

            if not mp4_path:
                # MP4 ファイルがない場合
                create_mkv(ffmpeg.input(mp4_path), None, None, output_path)
            elif not wav_path and not srt_path:
                # WAV ファイルと字幕ファイルがない場合
                create_mkv(ffmpeg.input(mp4_path), None, None, output_path)
            elif not wav_path:
                # WAV ファイルがない場合
                create_mkv(ffmpeg.input(mp4_path), None, ffmpeg.input(srt_path), output_path)
            elif not srt_path:
                # 字幕ファイルがない場合
                create_mkv(ffmpeg.input(mp4_path), ffmpeg.input(wav_path), None, output_path)
            else:
                # 全てのファイルが存在する場合
                create_mkv(ffmpeg.input(mp4_path), ffmpeg.input(wav_path), ffmpeg.input(srt_path), output_path)
        except Exception as e:
            print(f'エラーが発生しました: {e}')

if __name__ == '__main__':
    # mp4ファイルをセット
    mp4_file = 'Untitled.mp4'

    # WAVディレクトリをセット
    wav_dir = env.os.environ.get('WAV_DIRECTORY')

    # srtディレクトリをセット
    srt_dir = env.os.environ.get('SRT_DIRECTORY')
    
    # mkvディレクトリをセット
    mkv_dir = env.os.environ.get('MKV_DIRECTORY')

    # mp4ディレクトリをセット
    mp4_dir = env.os.environ.get('MP4_DIRECTORY')
    
    # ファイルを全て取得
    wav_list = os.listdir(wav_dir)
    srt_list = os.listdir(srt_dir)
    mkv_list = os.listdir(mkv_dir)
    mp4_list = os.listdir(mp4_dir)
    
    # 昇順にする
    wav_sort = sorted(wav_list, key=lambda x: int(re.search(r'\d+', x).group()))
    srt_sort = sorted(srt_list, key=lambda x: int(re.search(r'\d+', x).group()))
    mp4_sort = sorted(mp4_list, key=lambda x: int(re.search(r'\d+', x).group()))

    # main 関数の呼び出し
    main(wav_sort, srt_sort, mp4_sort, wav_dir, mp4_dir, srt_dir, mkv_dir)
