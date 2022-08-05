import keyboard
import pyautogui as pg
from time import sleep
from datetime import datetime

# while True:
#     print(pg.position())
#     sleep(0.3)
    
while True:
    if keyboard.is_pressed("c"):
        print("pressed!")
        # click reina
        pg.click(1164, 918, button="left")
        sleep(0.01)

        # click select
        pg.click(903, 784, button="left")
        sleep(0.01)

