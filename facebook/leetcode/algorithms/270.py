"""270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/

Given the root of a binary search tree and a target value,
return the value in the BST that is closest to the target.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def closestValueIterative(self, root: TreeNode, target: float) -> int:
    closestNode = root
    while root:
        if abs(root.val - target) < abs(closestNode.val - target):
            closestNode = root
        
        if target < root.val:
            root = root.left
        else:
            root = root.right
    
    return closestNode.val