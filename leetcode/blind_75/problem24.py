'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''


def is_valid_bst(root):
    
    def traverse_inorder(root, inorder):
        if root is None:
            return

        traverse_inorder(root.left, inorder)
        inorder.append(root.val)
        traverse_inorder(root.right, inorder)

    inorder = []
    traverse_inorder(root, inorder)

    for i in range(1, len(inorder)):
        if inorder[i-1] >= inorder[i]:
            return False

    return True