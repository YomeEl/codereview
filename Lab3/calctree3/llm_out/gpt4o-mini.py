class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(TreeNode(int(token)))
        else:
            node = TreeNode(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

def replace_multiplication(node):
    if node is None:
        return None
    if node.value == -3:
        left_subtree = replace_multiplication(node.left)
        right_subtree = replace_multiplication(node.right)
        return TreeNode(f"({left_subtree.value} * {right_subtree.value})")
    node.left = replace_multiplication(node.left)
    node.right = replace_multiplication(node.right)
    return node

def print_tree(node):
    if node is None:
        return ""
    if isinstance(node.value, int):
        return str(node.value)
    left = print_tree(node.left)
    right = print_tree(node.right)
    return f"({left} {node.value} {right})left} {node.value} {right})"

def main(filename):
    with open(filename, 'r') as file:
        expression = file.read().strip().split()
    
    tree = build_tree(expression)
    modified_tree = replace_multiplication(tree)
    return print_tree(modified_tree)

# Test the code using a hypothetical file
# filename = "expression.txt"
# result = main(filename)
# print(result)
