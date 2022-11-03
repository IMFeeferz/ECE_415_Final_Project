from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

wdir = 'C:/Users/afeef/OneDrive/Documents/ECE_415/Project/ECE_415_Final_Project'

while 1:  
    if pyautogui.locateOnScreen('flower.png', confidence = 0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I cannot see it")
        time.sleep(0.5)