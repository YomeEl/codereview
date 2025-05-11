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
            op = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5}[token]
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
    with open(filename, 'r') as file:
        tokens = file.read().split()
    tree = build_tree(tokens)
    modified_tree = remove_multiplication(tree)
    return modified_tree
	
	
def print_tree(node, indent=""):
    if node is None:
        return
    print(indent + str(node.value))
    if node.left or node.right:
        print_tree(node.left, indent + "  ")
        print_tree(node.right, indent + "  ")