# プロジェクト名

このプロジェクトは、動画ファイル（MP4）を操作して、音声ファイル（WAV）や字幕ファイル（SRT）を組み合わせ、MKV ファイルを生成し、最後に VLC を使用してストリーミングするためのスクリプト集です。

## 使用方法

### 準備

1. このプロジェクトをクローンまたはダウンロードしてローカルマシンに保存します。
2. 必要なライブラリやツールがインストールされていることを確認します（例：ffmpeg、VLCなど）。

### ディレクトリ構造のセットアップ

`main.py` と同じディレクトリに以下のディレクトリを作成します：

- `mp4`: MP4 ファイルを格納するディレクトリ。
- `wav`: WAV ファイルを格納するディレクトリ。
- `srt`: SRT ファイルを格納するディレクトリ。
- `mkv`: MKV ファイルを出力するディレクトリ。

### ファイルのセットアップ

1. `mp4` ディレクトリに結合する MP4 動画ファイルを配置します。
2. `wav` ディレクトリに対応する音声ファイル（WAV）を配置します。
3. `srt` ディレクトリに対応する字幕ファイル（SRT）を配置します。

### スクリプトの実行

1. `main.py` を実行して、MP4 ファイル、音声ファイル、字幕ファイルを組み合わせて MKV ファイルを生成します。
2. `mkv_transfer.py` を実行して、MKV ファイルを別のディレクトリに転送または変換します。
3. `vlc_stream.py` を実行して、生成された MKV ファイルを VLC を使用してストリーミングします。

## 注意事項

- このプロジェクトは、Python 3.6 以上で動作します。
- VLC メディアプレーヤーがインストールされていることを確認してください。
