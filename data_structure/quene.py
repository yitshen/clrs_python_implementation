class Nodes(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def enqueue(self, val):
        new_node = Nodes(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    def dequeue(self):
        if self.length == 0:
            print('Empty queue!')
        else:
            self.head = self.head.next
            self.length -= 1
    def __len__(self):
        return self.length
    def __str__(self):
        temp = self.head
        result = []
        while temp != None:
            result.append(temp.val)
            temp = temp.next
        return str(result)
test = queue()
test.enqueue(5)
test.enqueue(6)
test.enqueue(7)
test.enqueue(8)
len(test)
print(test)
print(test)
test.dequeue()
print(test)
len(test)
test.tail.val
