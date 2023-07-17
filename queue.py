"""
FIFO - first in first out principle
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            raise "queue is empty"

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return "queue is empty"

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


queue = Queue()
# queue.enqueue(10)
# queue.enqueue(11)
# queue.enqueue(12)
# queue.enqueue(13)
# queue.enqueue(14)
# queue.enqueue(15)
# queue.enqueue(16)
# queue.enqueue(17)
# queue.enqueue(18)
# queue.enqueue(19)

print(queue.size())
# queue.dequeue()
print(queue.peek())
print(queue.isEmpty())
