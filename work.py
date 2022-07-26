import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import mss
import mss.tools
import pyautogui
import time
from random import randint


class Work:
    def __init__(self, work_tool):
        self.work_tool = work_tool
        print('Начало работы')
    def work_start(self):
        print(self.work_tool)


        template = cv.imread(self.work_tool,0)
        pyautogui.PAUSE = 1
        random_time = randint(1, 20) * 0.1
        x = 0
        y = 0

        with mss.mss() as sct:
            # Get information of monitor 
            monitor_number = 2
            mon = sct.monitors[monitor_number]

            # The screen part to capture
            monitor = {
                "top": mon["top"] + 1,
                "left": mon["left"] + 1,
                "width": 1900,
                "height": 1200,
                "mon": monitor_number,
            }

            #Name
            output = "screen.png"

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        img_rgb = cv.imread('screen.png')
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        print('ищу петух')
        print(x,y)
        for pt in zip(*loc[::-1]):
    #       cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,200,0), 2) Рисонок квадрата
            x = pt[0]+30
            y = pt[1]+40
            pyautogui.moveTo(x,y,duration=1)
            pyautogui.click()                    #Клик по петуху
            print('петух найден')
            print(x,y)
            pyautogui.move(randint(-500, 500),randint(-500, 500),duration=1)
            time.sleep(1.5)
            break



        
    # pyautogui.click()                    Клик по петуху
    # cv.imwrite('res.png',img_rgb)        Рисунок результата
        time.sleep(random_time)
    #   pyautogui.moveTo(500,500)             Перемещение мыши 500х500



    