"""
LIFO - last in first out principle
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            raise "stack is empty"

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        else:
            return "stack is empty"
# [1,2,3,4,5,6]
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


stack = Stack()

print(stack.size())
stack.push(10)
stack.push(15)
stack.push(16)
stack.push(17)
stack.push(18)
stack.push(19)
stack.push(20)
print(stack.size())
stack.pop()
print(stack.peek())
