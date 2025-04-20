"""Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вывести указатель на второй элемент этого списка P2.
Известно, что в исходном списке не менее 5 элементов.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def first(self):
        return self.head


def init_list():
    the_list = List()
    the_list.insert(1)
    the_list.insert(2)
    the_list.insert(3)
    the_list.insert(4)
    return the_list


def main():
    the_list = init_list()
    print(the_list)
    second_node = the_list.first().next
    print("Указатель на второй элемент (P2):", second_node)


if __name__ == "__main__":
    main()
