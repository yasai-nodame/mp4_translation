import vlc
import os 
import re
import time

mkv_dir = os.listdir(r"F:\test_mkv")
mkv_sort = sorted(mkv_dir, key=lambda x: int(re.search(r'\d+', x).group()))
instance = vlc.Instance('--sub-source=marq')
player = instance.media_player_new()

for i in range(10):
    mkv = os.path.join(r"F:\test_mkv", f'output{i}.mkv')

    media = instance.media_new(mkv)
    player.set_media(media)
    player.play()
    
    
    duration = player.get_length() / 1000
    time.sleep(duration)

while player.get_state() == vlc.State.Playing:
    continue






# for mkv_file in mkv_sort:
#     mkv = os.path.join(r"F:\test_mkv", mkv_file)
#     media = instance.media_new(mkv)
#     player.set_media(media)
#     player.play()
#     if player.get_state() == vlc.State.Playing:
#         duration = player.get_length() / 1000
#         time.sleep(duration)

# while True:
#     pass