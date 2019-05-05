class Nodes:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
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
    def delete(self, val):
        node = self.tree_search_itarative(self.root, val)
        if not (node.left != None and node.right != None):
            if node.left == None and node.right == None:
                temp = None
            elif node.left != None and node.right == None:
                temp = node.left
            else:
                temp = node.right
            if temp != None:
                temp.parent = node.parent
            if node.parent == None:
                self.root = temp
            else:
                if node.parent.left == node:
                    node.parent.left = temp
                else:
                    node.parent.right = temp
        else:
            temp_node = self.tree_minimum(node.right)
            self.delete(temp_node.value)
            node.value = temp_node.value



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
        return self.tree_minimum(node)
    def maximum(self):
        node = self.root
        return self.tree_maximum(node)
    def node_successor(self, val):
        node = self.tree_search_itarative(self.root, val)
        if node.right != None:
            return self.tree_minimum(node.right)
        while node.parent != None and node.parent.right == node:
            node = node.parent
        return node.parent
    def node_predecessor(self, val):
        node = self.tree_search_itarative(self.root, val)
        if node.left != None:
            return self.tree_minimum(node.left)
        while node.parent != None and node.parent.left == node:
            node = node.parent
        return node.parent


    # private functions
    def tree_insert(self, node, val):
        if val < node.value:
            if node.left:
                self.tree_insert(node.left, val)
            else:
                temp = Nodes(val)
                temp.parent = node
                node.left = temp

        elif val >= node.value:
            if node.right:
                self.tree_insert(node.right, val)
            else:
                temp = Nodes(val)
                temp.parent = node
                node.right = temp
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
    def tree_minimum(self,node):
        parent = None
        while node != None:
            parent = node
            node = node.left
        return parent
    def tree_maximum(self,node):
        parent = None
        while node != None:
            parent = node
            node = node.right
        return parent
test = BST()
test.insert(15)
test.insert(5)
test.insert(16)
test.insert(3)
test.insert(12)
test.insert(20)
test.insert(10)
test.insert(13)
test.insert(18)
test.insert(23)
test.insert(6)
test.insert(7)
test.delete(5)
test.walk('in')
