from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

import pygame


from playsound import playsound

playsound('WonderHill.wav')
# Источник: https://pythonpip.ru/osnovy/10-audiomoduley-python-dlya-vosproizvedeniya-i-zapisi


# pygame.mixer.init()
# pygame.mixer.music.load("WonderHill.mp3")
# pygame.mixer.music.play(-1)

# import winsound
#
# filename = ' WonderHill.mp3 '
# winsound.PlaySound(filename, winsound.SND_FILENAME)
# Источник: https://pythonpip.ru/osnovy/10-audiomoduley-python-dlya-vosproizvedeniya-i-zapisi


# import simpleaudio as simple_audio
#
# filename = ' WonderHill.mp3 '
# wave_object = simple_audio.WaveObject.from_wave_file( filename )
# play_object = wave_object.play( )
# play_object.wait_done( )
# # Источник: https://pythonpip.ru/osnovy/10-audiomoduley-python-dlya-vosproizvedeniya-i-zapisi

# from pydub import AudioSegment
# from pydub.playback import play

# sound_audio = AudioSegment.from_mp3('WonderHill.mp3')
# sound_audio = AudioSegment.from_mp3('C:/Users/User/IdeaProjects/py-ex/keep_o_i_need/experiments/sound/WonderHill.mp3')
# play(sound_audio)
# Источник: https://pythonpip.ru/osnovy/10-audiomoduley-python-dlya-vosproizvedeniya-i-zapisi

'''
# playsound("WonderHill.mp3")


INPUT_FILE = "C:/out/sound/WonderHill.mp3"

# читать файл MP3
# song = AudioSegment.from_mp3("C:/Users/User/IdeaProjects/py-ex/keep_o_i_need/experiments/sound/WonderHill.mp3")
song = AudioSegment.from_mp3(INPUT_FILE)
# you can also read from other formats such as MP4
#  song = AudioSegment.from_file("audio_file.mp4", "mp4")
# play(song)

# print ('hello pythom sound')

'''