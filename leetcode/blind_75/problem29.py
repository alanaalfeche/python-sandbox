'''Problem 29: Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 

The path must contain at least one node and does not need to go through the root.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''This algorithm uses depth-first search to traverse through the tree, summing the values of individual nodes in a subtree. 

    https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/419793/Python-recursive-solution-beats-98-in-time-and-75-in-memory
    '''
    def max_path_sum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res 
        
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, root.val + left + right)
        return max(root.val + max(left, right), 0)
