# Имеется набор геометрических фигур разного цвета.
# Среди фигур могут встречаться круги, квадраты и отрезки.
# Для каждой фигуры известно, какого она цвета.
# Кроме того, для круга известен его радиус (тип int), для квадрата – размер стороны (тип int), для отрезка–длина (тип float).
# Написать функцию, позволяющую ввести с клавиатуры данные для одной фигуры.
# Используя эту функцию, ввести сведения об N фигурах и сохранить их в бинарном файле.
# Распечатать на экране содержимое данного файла в виде таблицы.
# Для решения использовать классы, обязательно наличие конструктора(ов),для вывода информации переопределить метод __str__()

import pickle


class Figure: #класс для фигур
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Цвет: {self.color}"


class Circle(Figure): #класс для круга
    def __init__(self, color, radius):
        super().__init__(color) #возвращает специальный объект, который передает вызовы методов (в данном случае — метода __init__) от производного класса к базовому
        self.radius = radius

    def __str__(self):
        return f" {super().__str__()}, Радиус: {self.radius}"


class Square(Figure): #класс для квадрата
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def __str__(self):
        return f" {super().__str__()}, Сторона: {self.side}"


class Segment(Figure): #класс для отрезка
    def __init__(self, color, length):
        super().__init__(color)
        self.length = length

    def __str__(self):
        return f" {super().__str__()}, Длина: {self.length}"


def input_figure(): #ввод данных
    figure = input("Введите тип фигуры (круг, квадрат, отрезок): ").lower()
    color = input("Введите цвет фигуры: ")
    if figure == "круг":
        radius = int(input("Введите радиус круга: "))
        return Circle(color, radius)
    elif figure == "квадрат":
        side = int(input("Введите размер стороны квадрата: "))
        return Square(color, side)
    elif figure == "отрезок":
        length = float(input("Введите длину отрезка: "))
        return Segment(color, length)
    else:
        print("Ошибка: Неизвестный тип фигуры.")
        return None

def file_rd(figures, file): #создание бинарного файла и запись в него данных
    with open(file, 'wb') as f:
        pickle.dump(figures, f)
    print(f"Данные сохранены в файл '{file}'.")

def rid_file(file): #чтение бинарного файла
    with open(file, 'rb') as f:
        figures = pickle.load(f)
    return figures

def print_figures(figures): #вывод в виде таблицы
    if not figures:
        print("Нет данных для отображения.")
        return

    print("." * 50)
    print(f"Тип фигуры | Описание")
    print("." * 50)
    for figure in figures:
        figure_type = figure.__class__.__name__  #получаем имя класса
        print(f'{figure_type} | {str(figure)}') #используем переопределенный __str__()
    print("." * 50)

file = "figures.bin"
figures = []
n = int(input("Введите количество фигур: "))
for i in range(n):
    figure = input_figure()
    if figure:
        figures.append(figure)
file_rd(figures, file)
loaded_figures = rid_file(file)
print_figures(loaded_figures)
