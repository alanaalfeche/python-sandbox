# BST implementation using LinkedList
# Cite: https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child
    
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        '''Three cases to consider when looking for a successor:
        Case 1. If node has a right child, then the successor is the smallest key in the subtree.
        Case 2. If node has no child and is the left child of its parent, then the parent is the successor. 
        Case 3. If node has no child and is the right child of its parent, then the successor is the successor of its parent, excluding this node.

        Only case 1 is implmemented because node will always have a right child 
        '''
        return self.right_child.find_min()

    def find_min(self):
        curr = self
        while curr.has_left_child():
            curr = curr.left_child
        return curr

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                elif self.is_left_child():
                    self.parent.right_child = self.right_child
                self.left_child.parent = self.parent
            elif self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                elif self.is_left_child():
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    # INSERT
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, curr_node):
        if key < curr_node.key:
            if curr_node.has_left_child():
                self._put(key, val, curr_node.left_child)
            else:
                curr_node.left_child = TreeNode(key, val, parent=curr_node)
        else: 
            if curr_node.has_right_child():
                self._put(key, val, curr_node.right_child)
            else: 
                curr_node.right_child = TreeNode(key, val, parent=curr_node)

    # SEARCH
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else: 
            return None
    
    def _get(self, key, curr_node):
        if not curr_node: # if empty tree
            return None
        elif curr_node.key == key:
            return curr_node
        elif key < curr_node.key:
            return self._get(key, curr_node.left_child)
        elif key > curr_node.key:
            return self._get(key, curr_node.right_child)

    # DELETE
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def _delete(self, curr_node):
        '''Three cases to consider when deleting a node
        Case 1. No children
        Case 2. Two children
            - requires to search for a node that will preserve BST
            - find next-largest key in the tree: successor
            - successor is guaranteed to have no more than one child
        Case 3. One child

        Below is the implementation of all three cases in order
        '''
        if curr_node.is_leaf():
            if curr_node == curr_node.parent.left_child:
                curr_node.parent.left_child = None
            else:
                curr_node.parent.right_child = None
        elif curr_node.has_both_children():
            successor = curr_node.find_successor()
            successor.splice_out()
            curr_node.key = successor.key
            curr_node.payload = successor.payload
        elif curr_node.has_any_children():
            if curr_node.has_left_child():
                if curr_node.is_left_child():
                    curr_node.left_child.parent = curr_node.parent
                    curr_node.parent.left_child = curr_node.left_child
                elif curr_node.is_right_child():
                    curr_node.left_child.parent = curr_node.parent
                    curr_node.parent.right_child = curr_node.left_child
                else: # if current node has no parent, then it must be the root
                    curr_node.replace_node_data(
                        curr_node.left_child.key, 
                        curr_node.left_child.payload,
                        curr_node.left_child.left_child,
                        curr_node.left_child.right_child
                    )
            elif curr_node.has_right_child():
                if curr_node.is_left_child():
                    curr_node.right_child.parent = curr_node.parent
                    curr_node.parent.left_child = curr_node.left_child
                elif curr_node.is_right_child():
                    curr_node.right_child.parent = curr_node.parent
                    curr_node.parent.right_child = curr_node.right_child
                else: # if current node has no parent, then it must be the root
                    curr_node.replace_node_data(
                        curr_node.right_child.key, 
                        curr_node.right_child.payload,
                        curr_node.right_child.left_child,
                        curr_node.right_child.right_child
                    )


bst = BinarySearchTree()
bst.put(1, 2)
print(bst.get(1))
bst.delete(1)
print(bst.length())