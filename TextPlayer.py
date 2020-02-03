import winsound
import time
import os

def Refresh(ttll):
    i = (frames * ttll) // length
    with open('TXTs/'+arr[i],'r') as f:
        print(f.read())

winsound.PlaySound('audio.wav', flags=1)

start = int(time.time()*1000)
frames = 6570
length = 219149
arr = os.listdir('TXTs')

while True:
    ttl = int(time.time()*1000) - start
    if ttl > length:
        break
    Refresh(ttl)
