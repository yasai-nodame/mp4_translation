import os 
import re 

import ffmpeg_mp4 
import mp4_segment 
import mkv_transfer
import vlc_stream
import env 

def main():
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
    
    ffmpeg_mp4.wav_and_srt(mp4_file, wav_dir, srt_dir)
    
    mp4_segment.segment(mp4_file, mp4_dir)

    mkv_transfer.conversion(wav_sort, srt_sort, mp4_sort, wav_dir, mp4_dir, srt_dir, mkv_dir)
    
    # 昇順にする
    mkv_sort = sorted(mkv_list, key=lambda x: int(re.search(r'\d+', x).group()))

    vlc_stream.vlc_streaming(mkv_sort, srt_sort)


if __name__ == '__main__':
    main()