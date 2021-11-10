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


def MakeSureClickImage(img, confirmImage, intervalTime):
    while True:
        if IsImageExist(confirmImage):
            print(confirmImage, ' exist')
            break
        if FindImg(img):
            print(img, ' found')
            pyautogui.click()
            time.sleep(intervalTime)
        time.sleep(0.2)


imgGroups = [["wework.png", "menu.png", 1],
             ["app1.png", "app2.png", 1],
             ["order.png", "refresh.png", 1],
             #  ["refresh.png", "confirm.png",1],
             ["confirm.png", "success.png", 5]]

for imgList in imgGroups:
    print("Working on ", imgList[0], imgList[1], imgList[2])
    MakeSureClickImage(imgList[0], imgList[1], imgList[2])
