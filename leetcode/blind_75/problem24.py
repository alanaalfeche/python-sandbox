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
    def helper(node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        return helper(node.right, val, upper) and helper(node.left, lower, val)
    return helper(root)