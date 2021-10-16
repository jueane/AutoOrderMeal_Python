#!/usr/bin/python3
import sys
import time
import pyautogui


def FindImg(img):
    print("finding {}".format(img))
    location = pyautogui.locateOnScreen(img, confidence=0.8)
    if location is None:
        return False
    else:
        c = pyautogui.center(location)
        pyautogui.moveTo(c.x, c.y)
        return True


def IsImageExist(img):
    print("finding {}".format(img))
    location = pyautogui.locateOnScreen(img, confidence=0.8)
    if location is None:
        return False
    else:
        return True


intervalTime = 3
gettrace = getattr(sys, 'gettrace', None)
if gettrace is None:
    intervalTime = 5
elif gettrace():
    intervalTime = 3
else:
    intervalTime = 0.3

print("interval:", intervalTime)


def MakeSureClickImage(img, confirmImage):
    while True:
        if IsImageExist(confirmImage):
            print(confirmImage, ' exist')
            break
        if FindImg(img):
            print(img, ' found')
            pyautogui.click()
        time.sleep(intervalTime)


imgGroups = [["wework.png", "menu.png"],
             ["app1.png", "app2.png"],
             ["order.png", "refresh.png"],
             ["refresh.png", "confirm.png"],
             ["confirm.png", "success.png"]]

for imgList in imgGroups:
    MakeSureClickImage(imgList[0], imgList[1])
