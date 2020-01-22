import os


directory = './buttons'

'''  Получим список файлов который будем использовать. 
В переменной files содержится список с названиями '''
files = os.listdir(directory)

for i in range(55, len(files)):
    print(files[i])
    i += 1





