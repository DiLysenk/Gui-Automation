

files = ('123!99')
# поиск индекса параметра паузы
index_sleep_time = files.find('!') + 1
# определение паузы и превращение строки в integer
sleep_time = int(files[index_sleep_time: index_sleep_time + 2])
# установка паузы
print(sleep_time + 10)








