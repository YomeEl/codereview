"""Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вывести указатель на шестой элемент этого списка P6.
Известно, что в исходном списке не менее 6 элементов
"""


class BadIndexError(Exception):
    def __init__(self, index):
        super().__init__(f"Index {index} not present")


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, new_data):
        self.length += 1
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        self.length += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def find_node(self, index):
        if index < 0:
            raise BadIndexError(index)

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
            if current_node is None:
                raise BadIndexError(index)
        return current_node

    def find_index(self, data):
        current_node = self.head
        for i in range(self.length):
            if current_node.data == data:
                return i
            current_node = current_node.next
        return -1

    def insert_at_index(self, data, index):
        if (self.head is None and index != 0) or index < 0:
            raise BadIndexError(index)

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        previous_node = self.find_node(index - 1)
        current_node = previous_node.next
        previous_node.next = new_node
        new_node.next = current_node
        self.length += 1

    def update_node(self, value, index):
        node = self.find_node(index)
        node.data = value

    def remove_first_node(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.length -= 1

    def remove_last_node(self):
        if self.head is None:
            return
        new_last = self.find_node(self.length - 1)
        new_last.next = None
        self.length -= 1

    def remove_at_index(self, index):
        if self.head is None:
            return
        if index >= self.length or index < 0:
            raise BadIndexError(index)
        if index == 0:
            self.remove_first_node()
            return

        prev = self.find_node(index - 1)
        prev.next = prev.next.next
        self.length -= 1

    def remove_node(self, data):
        index = self.find_index(data)
        self.remove_at_index(index)

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


def init_list(length):
    the_list = LinkedList()
    for i in range(length):
        the_list.push(i + 1)
    return the_list


LENGTH = 8
INDEX_TO_FIND = 5


def main():
    the_list = init_list(LENGTH)
    sixth_node = the_list.find_node(INDEX_TO_FIND)
    print(f"Шестой элемент списка: {repr(sixth_node)}")


if __name__ == "__main__":
    main()
