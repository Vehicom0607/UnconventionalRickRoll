import pyautogui as gui
import time
screenWidth, screenHeight = gui.size()
time.sleep(5)

import cv2
img = cv2.imread('./processedframes/frame2.png')
indexes = []
for rowindx, row in enumerate(img):
    for colindx, pixel in enumerate(row):
        if pixel[0] != 0:
            print(colindx, rowindx)
            indexes.append([colindx, rowindx])

for indexindex, index in enumerate(indexes):
    if indexindex%5 == 0:
        gui.moveTo(int(index[0]*1.5)+8, int(index[1]*1.5)+145)
        gui.click()

