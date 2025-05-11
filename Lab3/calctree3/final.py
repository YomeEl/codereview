class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(Node(int(token)))
        else:
            right = stack.pop()
            left = stack.pop()
            op = {"+": -1, "-": -2, "*": -3, "/": -4, "%": -5}[token]
            stack.append(Node(op, left, right))
    return stack.pop()


def evaluate(node):
    if node.value >= 0:
        return node.value
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == -1:
        return left_val + right_val
    elif node.value == -2:
        return left_val - right_val
    elif node.value == -3:
        return left_val * right_val
    elif node.value == -4:
        return left_val // right_val
    elif node.value == -5:
        return left_val % right_val


def remove_multiplication(node):
    if node is None:
        return None
    if node.value == -3:
        return Node(evaluate(node))
    node.left = remove_multiplication(node.left)
    node.right = remove_multiplication(node.right)
    return node


def solve(filename):
    with open(filename, "r") as file:
        tokens = file.read().split()
    tree = build_tree(tokens)
    modified_tree = remove_multiplication(tree)
    return modified_tree


if __name__ == __main__:

    def print_tree(node, indent=""):
        if node is None:
            return
        print(indent + str(node.value))
        if node.left or node.right:
            print_tree(node.left, indent + "  ")
            print_tree(node.right, indent + "  ")

    def test_file(filename):
        print(f"Testing file: {filename}")
        with open(filename, "r") as file:
            tokens = file.read().split()
            print(f"Expression: {' '.join(tokens)}")

        tree = build_tree(tokens)
        expected_tree = build_tree(tokens)  # Original tree for expected value
        modified_tree = remove_multiplication(tree)

        print("\nExpected tree (with multiplication evaluated):")
        expected_value = evaluate(expected_tree)
        print(f"Value: {expected_value}")
        print_tree(expected_tree)

        print("\nActual tree (after removing multiplication):")
        actual_value = evaluate(modified_tree)
        print(f"Value: {actual_value}")
        print_tree(modified_tree)
        print("\n" + "=" * 50 + "\n")

    # Test all files
    test_file("file1.txt")
    test_file("file2.txt")
    test_file("file3.txt")
