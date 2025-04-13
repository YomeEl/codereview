"""Дан файл целых чисел, содержащий более 50 элементов.
Уменьшить его размер до 50 элементов, удалив из файла необходимое количество начальных элементов.
"""

import struct

INITIAL_ELEMENT_COUNT = 75
FINAL_ELEMENT_COUNT = 50
ELEMENT_BYTE_SIZE = 4
FILENAME = "file33.bin"


def create_file(filename):
    f = open(filename, "wb")
    for i in range(INITIAL_ELEMENT_COUNT):
        f.write(struct.pack("f", i))
    f.close()


def read_file(filename):
    f = open(filename, "rb")
    data = f.read()
    element_count = len(data) // ELEMENT_BYTE_SIZE
    arr = struct.unpack("f" * element_count, data)
    f.close()
    return arr


def remove_first_n_elements(input_arr, n):
    arr = []
    for i in range(len(input_arr) - n, len(input_arr)):
        arr.append(input_arr[i])
    return arr


def write_file(arr):
    f = open("file33.bin", "wb")
    for i in arr:
        f.write(struct.pack("f", i))
    f.close()


def main():
    create_file(FILENAME)
    input_arr = read_file(FILENAME)
    output_arr = remove_first_n_elements(input_arr, FINAL_ELEMENT_COUNT)
    write_file(output_arr)
    result_arr = read_file(FILENAME)
    print(result_arr, len(result_arr))


if __name__ == "__main__":
    main()
