class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_item

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    def show(self):
        return self.heap


max_heap = MaxHeap()

max_heap.push(10)
max_heap.push(15)
max_heap.push(20)
max_heap.push(35)
max_heap.push(25)
max_heap.push(30)
max_heap.push(40)
max_heap.push(47)
max_heap.push(49)

# print(max_heap.size())
# print(max_heap.peek())
# # max_heap.pop()
# print(max_heap.peek())
# print(max_heap.show())