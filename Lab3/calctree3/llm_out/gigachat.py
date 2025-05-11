class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(tokens):
    stack = []
    operators = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5}
    
    for token in tokens:
        if token.isdigit():
            node = TreeNode(int(token))
            stack.append(node)
        else:
            op_value = operators.get(token)
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            
            right_node = stack.pop()
            left_node = stack.pop()
            new_node = TreeNode(op_value, left_node, right_node)
            stack.append(new_node)
    
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    
    return stack[-1]

def evaluate(node):
    if node is None or isinstance(node.value, int) and node.value >= 0:
        return node.value
    
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    
    if node.value == -3:  # Multiplication
        return left_val * right_val
    elif node.value == -1:
        return left_val + right_val
    elif node.value == -2:
        return left_val - right_val
    elif node.value == -4:
        return left_val // right_val
    elif node.value == -5:
        return left_val % right_val

def remove_multiplications(root):
    if root is None:
        return None
    
    # Evaluate multiplication nodes immediately
    if root.value == -3:
        evaluated_value = evaluate(root)
        return TreeNode(evaluated_value)
    
    # Recursively process subtrees
    root.left = remove_multiplications(root.left)
    root.right = remove_multiplications(root.right)
    
    return root

def main(filename):
    with open(filename, 'r') as f:
        tokens = f.read().strip().split()
    
    tree_root = build_tree(tokens)
    modified_root = remove_multiplications(tree_root)
    return modified_root

if __name__ == "__main__":
    result = main('expression.txt')
    print(result)