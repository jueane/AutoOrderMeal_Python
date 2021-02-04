#!/usr/bin/python3

import time
import pyautogui
import sys
# import keyboard


def FingImg(img):
    location = pyautogui.locateOnScreen(img, confidence=0.8)
    if location == None:
        return False
    else:
        c = pyautogui.center(location)
        pyautogui.moveTo(c.x, c.y)
        return True


while True:
    if(FingImg('wework.png')):
        print("1")
        pyautogui.doubleClick()
        break
    time.sleep(1)

imgs = ['apps.png', 'wifi.png', 'order.png', 'confirm.png']

while True:
    for img in imgs:
        while True:
            if(FingImg(img)):
                print(img, ' found')
                pyautogui.click()
                break
            time.sleep(1)
