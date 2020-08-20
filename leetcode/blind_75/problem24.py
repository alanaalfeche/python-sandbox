'''Problem 98: Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.

The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.
'''


def is_valid_bst(root):
    '''This algorithm uses in-order traversal to get a list of all nodes in the tree. 

    If the list is in order, then it is a valid BST. Otherwise, return False.
    '''
    def traverse(root, inorder):
        if not root:
            return
        traverse(root.left, inorder)
        inorder.append(root.val)
        traverse(root.right, inorder)

    inorder = []
    traverse(root, inorder)

    for i in range(1, len(inorder)):
        if inorder[i-1] >= inorder[i]:
            return False

    return True