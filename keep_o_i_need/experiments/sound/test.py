# from playsound import playsound
import winsound
import time
from threading import Thread
from time import sleep

from winsound import PlaySound

print('METKA_001')

print(winsound.SND_NOSTOP)
print(winsound.SND_ASYNC)


# winsound.PlaySound('WonderHill.wav', winsound.SND_APPLICATION)

winsound.PlaySound('WonderHill.wav', winsound.SND_ASYNC)

# winsound.PlaySound('WonderHill.wav', winsound.SND_NOSTOP)

print('METKA_002')


def func():
    winsound.PlaySound('WonderHill.wav', winsound.SND_ASYNC)
    print('qweqweqe')
    # for i in range(5):
    #     print(f"from child thread: {i}")
    #     sleep(0.5)

th_music = Thread(target=func)
th_music.start()
th_music.join()

i = 0
while i < 10:
    time.sleep(1)
    print('METKA_00III')
    PlaySound('WonderHill2.wav', winsound.SND_ASYNC)
    i += 1

print('METKA_003')

# PlaySound('file_example_MP3_700KB.mp3', winsound.SND_LOOP)
