class stack(object):
    def __init__(self, val = None):
        if val == None:
            self.storage = []
            self.top = 0
        else:
            self.storage = [val]
            self.top = 1
    def stack_empty(self):
        if self.storage == []:
            return True
        else:
            return False
    def push(self, val):
        if self.top == len(self.storage):
            self.storage.append(val)
            self.top += 1
        else:
            self.storage[self.top] = val
            self.top += 1
    def pop(self):
        self.top -= 1
        return self.storage[self.top]
    def __str__(self):
        return str(self.storage[:self.top])
# test = stack()
# test.stack_empty()
# test = stack('5')
# test.push(3)
# test.push(10)
# test.stack_empty()
# test.pop()
# test.push(7)
# print(test)
