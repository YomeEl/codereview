"""
Даны ссылки A1 и A2 на первый и последний элементы непустого двусвязного списка,
содержащего четное количество элементов.
Преобразовать список в два циклических списка (записав в свойство Next последнего
элемента списка ссылку на его первый элемент, а в свойство Prev первого элемента —
ссылку на последний элемент), первый из которых содержит первую половину элементов
исходного списка, а второй — вторую половину.
Вывести ссылки A3 и A4 на два средних элемента исходного списка (элемент A3
должен входить в первый циклический список, а элемент A4 — во второй).
Новые объекты типа Node не создавать.
"""

import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def dispose(self):
        print(f"Узел с удалёнными данными {self.data}")
        self.next = None
        self.prev = None
        gc.collect()


class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.first is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def print_list(self, head, is_circular=False):
        if head is None:
            print("Empty list")
            return

        temp = head
        first_iteration = True
        while first_iteration or (temp is not None and temp != head):
            first_iteration = False
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("(circular)" if is_circular else "None")

    def split_into_circular_lists(self):
        if self.first is None or self.last is None:
            return None, None, None, None

        slow = fast = self.first
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        a3 = slow
        a4 = slow.next

        first_half_head = self.first
        first_half_tail = a3

        second_half_head = a4
        second_half_tail = self.last

        if first_half_tail:
            first_half_tail.next = first_half_head
            first_half_head.prev = first_half_tail

        if second_half_tail:
            second_half_tail.next = second_half_head
            second_half_head.prev = second_half_tail

        return first_half_head, second_half_head, a3, a4

    def print(self):
        current_node = self.first
        while current_node:
            print(current_node.data)
            current_node = current_node.next


dll = DoublyLinkedList()
for i in range(1, 7):
    dll.push(i)

print("Исходный список:")
dll.print_list(dll.first)

C1, C2, A3, A4 = dll.split_into_circular_lists()

print("Первый циклический список:")
dll.print_list(C1, is_circular=True)
print("Второй циклический список:")
dll.print_list(C2, is_circular=True)

print("Средние элементы исходного списка:")
print("A3:", A3.data if A3 else "null")
print("A4:", A4.data if A4 else "null")
