from moviepy.editor import VideoFileClip
import ffmpeg 
import subprocess
import os 
file = r'Untitled.mp4'
output_dir = r"F:\test_mp4"


a = ffmpeg.input(file)

# FFmpegコマンド
command = [
    'ffmpeg',
    '-i', file,
    '-c:v', 'libx264',  # 動画コーデックを指定（再エンコード）
    '-crf', '23',  # クオリティ設定（0-51、低いほど高品質）
    '-preset', 'fast',  # エンコードプリセット（速度と圧縮率のバランス）
    '-c:a', 'copy',  # オーディオは再エンコードしない
    '-force_key_frames', f'expr:gte(t,n_forced*{2})',  # キーフレームを2秒ごとに強制挿入
    '-segment_time', str(2),  # セグメントの長さを2秒に設定
    '-f', 'segment',  # 出力形式をセグメントに設定
    '-reset_timestamps', '1',  # 各セグメントのタイムスタンプをリセット
    os.path.join(output_dir, 'output%01d.mp4')  # 出力ファイル名の形式
]


subprocess.run(command,check=True)