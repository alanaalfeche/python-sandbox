"""938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree,
return the sum of values of all nodes with a value in the range [low, high].
"""
def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    self.range_sum = 0

    def dfs(node):
        if node:
            if low <= node.val <= high:
                self.range_sum += node.val
                
            if node.val > low:
                dfs(node.left)

            if node.val < high:
                dfs(node.right)

    dfs(root)
    return self.range_sum