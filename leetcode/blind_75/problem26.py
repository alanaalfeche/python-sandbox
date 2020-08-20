'''Problem 26: Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
'''


def max_depth(self, root: TreeNode) -> int:  
    '''This algorithm uses recursion to traverse through the tree until it maximum depth. 

    And for everytime it collapses, it returns +1. +1 is also used to account for the root. 
    '''
    if root is None: return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1