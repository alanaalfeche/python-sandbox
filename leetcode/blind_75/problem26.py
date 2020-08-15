'''
Problem 26. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
'''


def max_depth(self, root: TreeNode) -> int:  
    if not root:
        return 0
    queue = [root]
    depth = 0
    while queue:
        children = []
        depth += 1 # the number of times fn goes inside while loop is the number of valid parents
        for node in queue: 
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        queue = children
    return depth
