'''Problem 48: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
'''


def invert_tree(root):
    '''This algorithms inverts a binary tree using iterative approach. This can also be done recursively as follows:
        if root is not None:
            return root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root
    '''
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root