import board
import time
import audiocore
import audiopwmio
import digitalio

# a push button circuit on GP15, set as an input pin
buttonpin = digitalio.DigitalInOut(board.GP16)
buttonpin.direction = digitalio.Direction.INPUT
buttonpin.pull = digitalio.Pull.UP # simplify the button circuit
# load the sound files into variables
sound1 = open("dum.wav", "rb")
# prepare the sound files to play
wav1 = audiocore.WaveFile(sound1)
# set the pin to play sound from
a = audiopwmio.PWMAudioOut(board.GP15)
# button state variables    
times_pressed = 0
button = 1
old_button = 1

while 1:
    button = buttonpin.value 
    if (button == 0 and old_button == 1):
        print("0")
        a.play(wav1) # play the sound
        while a.playing:
            time.sleep(.05)
    old_button = button