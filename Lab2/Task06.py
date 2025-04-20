"""
Dynamic74.
Даны ссылки A1 и A2 на барьерный и текущий элементы двусвязного списка
(о списке с барьерным элементом см. задание Dynamic70).
Также дано число N(>0) и набор из N чисел. Описать класс IntListB, содержащий следующие члены:
• закрытые поля barrier и current типа Node (барьерный и текущий элементы списка);
• конструктор с параметрами a_barrier и a_current — барьерным и текущим элементами
  существующего списка;
• процедура insert_last(d), которая добавляет новый элемент со значением d в конец списка
  (d — входной параметр целого типа, добавленный элемент становится текущим);
• процедура put (без параметров), которая выводит ссылку на поле current,
  используя метод put класса IntListB.
С помощью метода insert_last добавить в конец исходного списка данный набор чисел(в том же порядке)
и вывести сссылку на текущий элемент полученного списка, используя для этого
метод put класса IntListB.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class IntListB:
    def __init__(self, a_barrier, a_current):
        self.barrier = a_barrier
        self.current = a_current

    def insert_last(self, d):
        new_node = Node(d)
        last = self.barrier.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.barrier
        self.barrier.prev = new_node
        self.current = new_node

    def put(self):
        print(f"Ссылка на текущий элемент: {self.current}")


def main():
    barrier = Node(0)
    barrier.next = barrier
    barrier.prev = barrier

    current = barrier

    the_list = IntListB(barrier, current)

    the_list.insert_last(10)
    the_list.insert_last(20)
    the_list.insert_last(30)
    the_list.insert_last(40)
    the_list.insert_last(50)

    the_list.put()


if __name__ == "__main__":
    main()
