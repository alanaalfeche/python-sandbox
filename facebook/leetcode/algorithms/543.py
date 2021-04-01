"""543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.diameter = 0

    def longest_path(node):
        if not node:
            return 0

        left_path = longest_path(node.left)
        right_path = longest_path(node.right)

        self.diameter = max(self.diameter, left_path + right_path)
        return max(left_path, right_path) + 1

    longest_path(root)
    return self.diameter