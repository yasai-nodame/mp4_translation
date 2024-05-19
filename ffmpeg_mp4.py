import ffmpeg 
import os 


soccer_mp4 = r"F:\test_ffmpeg\8K9co4OYRlP5APKk.mp4"
soccer_mp4_1 = r"F:\test_ffmpeg\HFeBeDRL8I3M_2ir.mp4"


def ffmpeg_translation(mp4_file):
    input_file = ffmpeg.input(mp4_file)
    

