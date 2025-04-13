"""Дана строка S0, целое число N (≤ 4) и N файлов целых чисел с именами S1, …, SN.
Объединить их содержимое в новом файле-архиве с именем S0, используя следующий формат: в
первом элементе файла-архива хранится число N, в следующих N элементах хранится размер
(число элементов) каждого из исходных файлов, а затем последовательно размещаются данные
из каждого исходного файла.
"""

import struct

S0_NAME = "S0.bin"
N = 3
FILES = ["S1.bin", "S2.bin", "S3.bin"]  # FIXME: use generator


def create_files():
    for filename in FILES:
        with open(filename, "wb") as f:
            if filename == "S1.bin":
                numbers = [1] * 20
            elif filename == "S2.bin":
                numbers = [4, 5, 6, 7]
            elif filename == "S3.bin":
                numbers = [8, 9, 10, 11]
            else:
                numbers = [12, 13, 14, 15]
            for num in numbers:
                f.write(struct.pack("i", num))


def read_files():
    files_data = []
    for item in FILES:
        with open(item, "rb") as file:
            data = []
            while True:
                bytes_read = file.read(4)
                if not bytes_read:
                    break
                data.append(struct.unpack("i", bytes_read)[0])
            files_data.append(data)
    return files_data


def write_archive(filename, data):
    with open(filename, "wb") as archive:
        new_data = [N]

        for i in data:
            new_data.append(len(i))

        for i in data:
            for j in i:
                new_data.append(j)

        for i in new_data:
            archive.write(struct.pack("i", i))


def print_file(filename):
    with open(filename, "rb") as archive_file:
        while True:
            byte_read = archive_file.read(4)
            if not byte_read:
                break
            print(struct.unpack("i", byte_read)[0])


def main():
    create_files()
    data = read_files()
    write_archive(S0_NAME, data)
    print_file(S0_NAME)


if __name__ == "__main__":
    main()
