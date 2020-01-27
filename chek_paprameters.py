import os
import sys

#
# directory = './buttons_bla'
#
# '''  Получим список файлов который будем использовать.
# В переменной files содержится список с названиями '''
# files = os.listdir(directory)
#
# for i in range(60):
#     print(files[i])
#     i += 1


if len(sys.argv) > 1:
    step = int(sys.argv[1])
else:
    step = 0
print(step + 9)