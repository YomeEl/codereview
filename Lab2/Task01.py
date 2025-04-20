"""Дано число N (> 0) и набор из N чисел.
Создать стек, содержащий исходные числа(последнее число будет вершиной стека),
и вывести ссылку на его вершину.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        return self.top


def create_stack():
    n = int(input("Введите количество чисел (N > 0): "))
    if n <= 0:
        # better to throw exception
        print("Введённое число <= 0")
        return None
    stack = Stack()
    for _ in range(n):
        num = int(input())
        stack.push(num)
    return stack.peek()


def main():
    top_node = create_stack()
    if top_node is None:
        return
    
    print("Ссылка на вершину стека:", top_node)
    print("Значение вершины стека:", top_node.data)


if __name__ == "__main__":
    main()
