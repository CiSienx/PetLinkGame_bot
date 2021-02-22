import pyautogui as pa
import keyboard as key
import random
import numpy as np
from PIL import ImageGrab

pos = [(541, 233),(824, 646)]
listX = []
listY = []
pa.PAUSE = 0.0

for i in range(7):
    listX.append(pos[0][0] + i * 45)
for i in range(10):
    listY.append(pos[0][1] + i * 45)

while True:
    if key.is_pressed("q"):
        for i in range(7):
            for j in range(10):
                if i % 2 != 0:
                    pa.click(listX[i],listY[j])
                else :
                    pa.click(listX[i],listY[9 - j])
        for i in range(7):
            for j in range(10):
                if i % 2 == 0:
                    pa.click(listX[i],listY[j])
                else :
                    pa.click(listX[i],listY[9 - j])
    elif key.is_pressed("w"):
        for j in range(10):
            for i in range(7):
                if j % 2 != 0:
                    pa.click(listX[i], listY[j])
                else:
                    pa.click(listX[6 - i], listY[j])
        for j in range(10):
            for i in range(7):
                if j % 2 == 0:
                    pa.click(listX[i], listY[j])
                else:
                    pa.click(listX[6 - i], listY[j])
    elif key.is_pressed("e"):
        for i in range(70):
            pa.click(listX[random.randrange(0,7,1)], listY[random.randrange(0,7,1)])
    elif key.is_pressed("r"):
        for i in range(70):
            if key.is_pressed("x"):
                break
            img = ImageGrab.grab(bbox=(listX[i//10]+4,listY[i%10]+4,listX[i//10]+5,listY[i%10]+5))
            val = np.asarray(img)
            val = val[0][0][1]
            for j in range(i+1):
                if val < 80:
                    break
                pa.click(listX[i//10],listY[i%10])
                pa.click(listX[j//10],listY[j%10])

    elif key.is_pressed("z"):
        break
