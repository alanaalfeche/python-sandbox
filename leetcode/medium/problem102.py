'''Problem 102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        while queue:
            parent, children = [], []
            for node in queue:
                parent.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            result.append(parent)
            queue = children
        
        return result
