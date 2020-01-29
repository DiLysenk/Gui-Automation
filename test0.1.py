import cv2
import time
import numpy
import pyautogui
from PIL import ImageGrab
import os
import sys



'''Объявляем каталог из которого будем брать картинки'''
directory = './buttons_bla'

'''  Получим список файлов который будем использовать. 
В переменной files содержится список с названиями '''
files = os.listdir(directory)

"""добавление параметра в командной строке, если нет нечего то step = 0, если строка больше 1 то считывается"""
if len(sys.argv) > 1:
    step = int(sys.argv[1])      #step - начало списка искомых объектов
else:
    step = 0

"""добавление параметра в командной строке, если нет нечего то end = 0, если строка больше 1 то считывается"""
if len(sys.argv) > 1:
    end_script = int(sys.argv[2])   #end - конец списка искомых объектов
else:
    end_script = len(files)

"""Поиск координат верхнего левого угла кнопки"""


def search_screen_position(path_screen_button):
    # объявляет искомый объект
    template = cv2.imread(path_screen_button, 0)
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

    loc = numpy.where(res >= 0.94)  # разобрать как работает,

    for pt in zip(*loc[::-1]):  # loc = это строка или срез чегото
        x = int(pt[0])
        y = int(pt[1])

    find_screen = ImageGrab.grab(bbox=(x, y, x + w, y + h))

    find_screen.save('3.png')

    return x, y


' Цикл с шагами в search_screen_position подставляются аргменты из списка '
'files(files[i]) файлы находятся в папке buttons_bla '

# цикл работает с файлами, ищет совпадения и инициализирует действие

for i in range(step, end_script):

    # вывод Шага с названием файла перед его нахождением
    print("step " + str(i) + ': ' + files[i])

    if files[i].find('!') != -1:
        # поиск индекса параметра паузы
        index_sleep_time = files[i].find('!') + 1
        # определение паузы и после символа "!"
        sleep_time = int(files[i][index_sleep_time: index_sleep_time + 2])
        # установка паузы
        time.sleep(1.1 * sleep_time)

    # конкатенация имени папки с именем файла что бы получился путь
    files[i] = "buttons_bla/" + files[i]
    time.sleep(0.1)

    # Поиск координат левого верхнего угла картинки
    try:
        x, y = search_screen_position(files[i])
    except:
        time.sleep(10)  # не изменять, так задуманно
        x, y = search_screen_position(files[i])

    # Клик по кнопке,  если в файле указан параметр то клик происходит ПКМ
    if files[i].find('rr') != -1:
        pyautogui.rightClick(x + 10, y + 10)
    elif files[i].find('dd') != -1:
        pyautogui.leftClick(x + 10, y + 10)
        pyautogui.leftClick(x + 10, y + 10)
    else:
        pyautogui.leftClick(x + 10, y + 10)

    time.sleep(0.1)
