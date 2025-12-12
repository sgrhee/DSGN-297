import serial
ser = serial.Serial('COM14') # the name of your port here
print('Opening port: ' + str(ser.name))
import pygame
import sys

WIDTH = 600
HEIGHT = 600
n1_int = 0
n2_int = 0
upp = Actor('catup.jpg')
upp.pos = (300, 300)
fallen = Actor('plushdown.jpg')
fallen.pos = (300, 300)


def update():
    global n1_int, n2_int, n3_int

    if ser.in_waiting > 0:
        # 1. decode() turns bytes into a normal string
        # 2. strip() removes whitespace (newlines)
        line = ser.readline().decode('utf-8').strip()

        # 3. Clean up: remove b', (, ), and quotes if they stuck around
        clean_line = line.replace("b'", "").replace("'", "").replace("(", "").replace(")", "")

        parts = clean_line.split(',')

        # Check if we actually got 3 parts to avoid crashing
        if len(parts) >= 3:
            # 4. Convert to float FIRST, then to int
            n1_int = int(float(parts[0]))
            n2_int = int(float(parts[1]))
            n3_int = int(float(parts[2]))

def draw():
   screen.fill((0, 0, 0))
   threshold = 5
   if abs(n2_int) > abs(n3_int) and abs(n2_int) > threshold:
       msg = "All good here"
       color = (0, 255, 0) # Green
       sidenote = "we upppp & ballin haha"
       upp.draw()
   elif abs(n3_int) > abs(n2_int) and abs(n3_int) > threshold:
       msg = "SHARK DOWNNN SEND HELP"
       sidenote = "ai weiwei is so funny"
       color = (0, 0, 255) # Blue
       fallen.draw()
   else:
       msg = "SHARK SIDEWAYS STILL SEND HELP"
       sidenote = "ai weiwei is so funny"
       color = (0, 0, 255) # Blue
       fallen.draw()
   screen.draw.text(msg, (50, 50), fontsize=40, color=color)
   screen.draw.text(sidenote, (500,500), fontsize=15, color=(0,0,0))
