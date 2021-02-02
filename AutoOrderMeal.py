#!/usr/bin/python3

import time
import pyautogui
import sys
# import keyboard


def IsFind(img):
    location = pyautogui.locateOnScreen(img, confidence=0.8)
    if location == None:
        return False
    else:
        c = pyautogui.center(location)
        pyautogui.moveTo(c.x, c.y)
        return True


def SelectNextCourse():
    ret = pyautogui.locateOnScreen('next.png', confidence=0.8)

    # if ret == None:
    #     ret = pyautogui.locateOnScreen('icon.png', confidence=0.8)

    if ret == None:
        return False
    else:
        print("select next")
        p = pyautogui.center(ret)
        pyautogui.moveTo(p.x, p.y)
        time.sleep(1)
        pyautogui.click()
        return True


while True:
    if(IsFind('wework.png')):
        print("1")
        pyautogui.doubleClick()
        break
    time.sleep(1)


while True:
    if(IsFind('apps.png')):
        print("2")
        pyautogui.click()
        break
    time.sleep(1)


while True:
    if(IsFind('wifi.png')):
        print("3")
        pyautogui.click()
        break
    time.sleep(1)

while True:
    if(IsFind('order.png')):
        print("4")
        pyautogui.click()
        break
    time.sleep(1)

while True:
    if(IsFind('confirm.png')):
        print("5")
        pyautogui.click()
        break
    time.sleep(1)
