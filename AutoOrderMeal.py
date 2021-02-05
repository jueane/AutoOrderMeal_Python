#!/usr/bin/python3

import time
import pyautogui
import sys
# import keyboard


def FingImg(img):
    print("finding {}".format(img))
    location = pyautogui.locateOnScreen(img, confidence=0.8)
    if location == None:
        return False
    else:
        c = pyautogui.center(location)
        pyautogui.moveTo(c.x, c.y)
        return True


def WaitUntilFindImg_Click(img):
    while True:
        if(FingImg(img)):
            print(img, ' found')
            pyautogui.click()
            break
    time.sleep(1)


def WaitUntilFindImg_DoubleClick(img):
    while True:
        if(FingImg(img)):
            print(img, ' found')
            pyautogui.doubleClick()
            break
    time.sleep(1)


WaitUntilFindImg_DoubleClick('wework.png')

while True:
    if(FingImg('app1.png') or FingImg('app2.png')):
        print('app', ' found')
        pyautogui.click()
        break
    time.sleep(1)

imgs = ['wifi.png', 'order.png', 'confirm.png']

while True:
    for img in imgs:
        while True:
            if(FingImg(img)):
                print(img, ' found')
                pyautogui.click()
                break
            time.sleep(1)
