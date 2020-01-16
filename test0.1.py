import cv2
import time
import numpy
import pyautogui
from PIL import ImageGrab
import os


'''Объявляем каталог из которого будем брать картинки'''
directory = './buttons'

'''  Получим список файлов который будем использовать. 
В переменной files содержится список с названиями '''
files = os.listdir(directory)
files.sort()
print(files)


#search screen position, coordinates x and y, t == screen element
def search_screen_position(t):
    time.sleep(0.1)
    template = cv2.imread(t, 0)
    w, h = template.shape[::-1]
    # инвертируем
    # Скрин Объекта на котором находим объект
    base_screen = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    base_screen.save('1.png')

    # преобразование в cv2 формат
    img_rgb = cv2.imread('1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # преобразование в читабельный формат

    # поиск скриншота
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    loc = numpy.where(res >= 0.95)  # разобрать как работает,

    for pt in zip(*loc[::-1]): # loc = это строка или срез чегото
        x = int(pt[0])
        y = int(pt[1])

    find_screen = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    find_screen.save('3.png')
    return x, y

''' Цикл с шагами
в search_screen_position подставляются аргменты из списка files (files[i])
файлы находятся в папке buttons
'''
for i in range(len(files)):

    print(str(i) + " step " + files[i])         # вывод Шага
    files[i] = "buttons/" + files[i]            #
    time.sleep(0.1)
    x, y = search_screen_position(files[i])
    pyautogui.leftClick(x + x/2, y + y/2)




