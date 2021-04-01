"""515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the root of a binary tree,
return an array of the largest value in each row of the tree (0-indexed).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def largestValues(root: TreeNode) -> List[int]:
    if not root:
        return []
    
    queue = [root]
    result = []
    
    while queue:
        values, children = [], []
        for node in queue:
            values.append(node.val)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
                
        queue = children
        result.append(max(values))
        values.clear()
    
    return result
                