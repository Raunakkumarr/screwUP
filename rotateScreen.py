import rotatescreen
import time
import keyboard
import time
import sys
import os

os.system('cmd /c pip install rotate-screen')
os.system('cmd /c pip install time')
os.system('cmd /c pip install keyboard')
os.system('cmd /c pip install sys')

screen = rotatescreen.get_primary_display()
for i in range(10000000):
    angle = i*90 % 360
    screen.rotate_to(angle)
    time.sleep(1)
    if keyboard.is_pressed('tab'):
        screen.rotate_to(0)
        sys.exit()



