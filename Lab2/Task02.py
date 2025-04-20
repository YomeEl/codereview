"""Дан набор из 10 чисел. Создать очередь, содержащую данные числа в
указанном порядке (первое число будет размещаться в  начале очереди,
последнее — в конце), и вывести ссылки A1 и A2 на начало и конец очереди.
"""


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__("Очередь пуста")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError()

        value = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        return value

    def front(self):
        if self.is_empty():
            raise EmptyQueueError()
        return self.first.data

    def rear(self):
        if self.is_empty():
            raise EmptyQueueError()
        return self.last.data

    def print_queue(self):
        current = self.first
        print("Очередь (начало -> конец):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_queue_visual(self):
        current = self.first
        output = []
        while current:
            output.append(f"[{current.data}]")
            current = current.next
        print(" → ".join(output))


def main():
    queue = Queue()

    numbers = list(map(int, input("Введите 10 чисел через пробел: ").split()))

    for num in numbers:
        queue.enqueue(num)

    try:
        queue.print_queue_visual()
        print(f"Ссылка на начало (A1): {queue.first} (значение: {queue.front()})")
        print(f"Ссылка на конец (A2): {queue.last} (значение: {queue.rear()})")
    except EmptyQueueError as error:
        print("Ошибка:", str(error))


if __name__ == "__main__":
    main()
