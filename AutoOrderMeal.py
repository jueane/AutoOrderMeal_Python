#!/usr/bin/python3

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


def MakeSureClickImage(img, confirmImage):
    while True:
        if IsImageExist(confirmImage):
            break
        if FindImg(img):
            print(img, ' found')
            pyautogui.click()
            time.sleep(2)


MakeSureClickImage("wework.png", "menu.png")

MakeSureClickImage("app1.png", "app2.png")

MakeSureClickImage("wifi.png", "order.png")

MakeSureClickImage("order.png", "confirm.png")

MakeSureClickImage("confirm.png", "success.png")

# WaitUntilFindImg_DoubleClick('wework.png')
#
# while True:
#     if (FingImg('app1.png') or FingImg('app2.png')):
#         print('app', ' found')
#         pyautogui.click()
#         break
#     time.sleep(1)
#
# imgs = ['wifi.png', 'order.png', 'confirm.png']
#
# for img in imgs:
#     while True:
#         if (FingImg(img)):
#             print(img, ' found')
#             pyautogui.click()
#             break
#         time.sleep(1)
