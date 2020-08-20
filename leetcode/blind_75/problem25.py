'''Problem 100: Same Tree

https://leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''


def is_same_tree(p, q):
    '''This algorithm uses recursion to compare the left and right leaf of the tree.'''     
    # both None  
    if not p and not q:
        return True
    # one is None
    if not p or not q:
        return False
    # if root values are different
    if p.val != q.val:
        return False
    return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
    
