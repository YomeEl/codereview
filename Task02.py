'''
Дан файл целых чисел, содержащий более 50 элементов.
Уменьшить его размер до 50 элементов, удалив из файла необходимое количество начальных элементов.
'''
import pickle
import struct


# тут я заполняю бинарник вещественными числами
f = open('file33.bin', 'wb')
for i in range(75):
    f.write(struct.pack('f', i))
f.close()

# считываю файл с элементами от 0 до 74
f = open('file33.bin', 'rb')
data = f.read()
n = len(data)//4
file = struct.unpack('f' * n, data)
f.close()
arr = []

# тут удаляем первые элементы, чтобы количество элементов было 50
for i in range(len(file)-50, len(file)):
    arr.append(file[i])

#тут мы открываем файл для записи, и перезаписываем элементы в файл 
f = open('file33.bin', 'wb')
for i in arr:
    f.write(struct.pack('f', i))

f.close()

# тут я открываю файл еще раз чтобы убедиться что все записалось верно
f = open('file33.bin', 'rb')
data = f.read()
n = len(data)//4
file = struct.unpack('f' * n, data)
f.close()
print(file, len(file))
