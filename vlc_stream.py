import vlc
import os 
import time
from itertools import zip_longest

#####################
# vlcで再生させていく
#####################

def vlc_streaming(mkv_sort, srt_sort):
    instance = vlc.Instance('--sub-source=marq')
    player = instance.media_player_new()

    while True:
        for mkv_file, srt_file in zip_longest(mkv_sort, srt_sort):
            if srt_file is None:
                mkv = os.path.join(r"F:\test_mkv", mkv_file)
                
                media = instance.media_new(mkv)
                player.set_media(media)
                
                player.play()
                
                start_time = time.time()
                
                # player.play()が早すぎて、うまく再生されない。　なのでwhile文で再生されるまでtime.sleep(0.1)を繰り返させ、うまく再生されるようにする。
                while player.get_state() not in (vlc.State.Playing, vlc.State.Error, vlc.State.Ended):
                    if time.time() - start_time > 2:
                        print(f'再生が開始されませんでした。: {mkv}')
                        player.stop()
                        break 
                    time.sleep(0.1)
                
                
                if player.get_state() == vlc.State.Playing:
                    duration = player.get_length() / 1000 
                    time.sleep(duration)
            else:
                mkv = os.path.join(r"F:\test_mkv", mkv_file)
                srt = os.path.join(r"F:\test_srt", srt_file)

                media = instance.media_new(mkv)
                media.add_option(f':sub-file={srt}')
                player.set_media(media)
                
                player.play()
                
                start_time = time.time()
                
                # player.play()が早すぎて、うまく再生されない。　なのでwhile文で再生されるまでtime.sleep(0.1)を繰り返させ、うまく再生されるようにする。
                while player.get_state() not in (vlc.State.Playing, vlc.State.Error, vlc.State.Ended):
                    if time.time() - start_time > 2:
                        print(f'再生が開始されませんでした。: {mkv}')
                        player.stop()
                        break 
                    time.sleep(0.1)
                
                
                if player.get_state() == vlc.State.Playing:
                    duration = player.get_length() / 1000 
                    time.sleep(duration)
                
        while True:
            continue
            

