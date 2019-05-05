class Nodes:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)

class BST(object):
    def __init__(self, val = None):
        if val == None:
            self.root = None
        else:
            self.root = Nodes(val)
    def set_root(self, val):
        self.root = Nodes(val)
    def insert(self, val):
        if self.root == None:
            self.set_root(val)
        else:
            self.tree_insert(self.root, val)
    def walk(self, order):
        if order == 'pre':
            return self.tree_walk_pre_order(self.root)
        if order == 'in':
            return self.tree_walk_in_order(self.root)
        if order == 'post':
            return self.tree_walk_post_order(self.root)
    def find(self, val):
        return self.tree_search_itarative(self.root, val)
    def minimum(self):
        node = self.root
        parent = None
        while node != None:
            parent = node
            node = node.left
        try:
            return parent.value
        except:
            return None
    def maximum(self):
        node = self.root
        parent = None
        while node != None:
            parent = node
            node = node.right
        if parent == None:
            return None
        else:
            return parent.value
    # private functions
    def tree_insert(self, node, val):
        if val < node.value:
            if node.left:
                self.tree_insert(node.left, val)
            else:
                node.left = Nodes(val)
        elif val >= node.value:
            if node.right:
                self.tree_insert(node.right, val)
            else:
                node.right = Nodes(val)
    def tree_walk_in_order(self, node):
        if node != None:
            self.tree_walk_in_order(node.left)
            print(node)
            self.tree_walk_in_order(node.right)
    def tree_walk_pre_order(self, node):
        if node != None:
            print(node)
            self.tree_walk_pre_order(node.left)
            self.tree_walk_pre_order(node.right)
    def tree_walk_post_order(self, node):
        if node != None:
            self.tree_walk_post_order(node.left)
            self.tree_walk_post_order(node.right)
            print(node)
    def tree_search_recursive(self, node, val):
        if node == None or node.value == val:
            return node
        if val < node.value:
            return self.tree_search_recursive(node.left, val)
        else:
            return self.tree_search_recursive(node.right, val)
    def tree_search_itarative(self, node, val):
        while node != None and node.value != val:
            if val < node.value:
                node = node.left
            else:
                node = node.right
        return node
test = BST()
test.insert(15)
test.insert(6)
test.insert(18)
test.insert(3)
test.insert(7)
test.insert(17)
test.insert(20)
test.insert(2)
test.insert(4)
test.insert(13)
test.insert(9)
test.walk('post')
