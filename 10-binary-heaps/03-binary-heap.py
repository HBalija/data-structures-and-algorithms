class MaxBinaryHeap:

    values = []

    def insert(self, value):
        """
        Insert a value to a max heap list.
        """
        self.values.append(value)
        if len(self.values) == 1:
            return

        idx = len(self.values) - 1

        # bubble up
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.values[parent_idx] > self.values[idx]:
                break
            # swap values
            self.values[parent_idx], self.values[idx] = self.values[idx], self.values[parent_idx]
            idx = parent_idx

    def extractMax(self):
        """
        Remove root element (max value) and reorder the Heap.
        """
        # pop last element and place it as a first one; this value will be swapped in bubble down
        oldRoot = self.values[0]
        bubbleDownValue = self.values.pop()
        self.values[0] = bubbleDownValue

        # bubble down
        idx = 0
        while True:
            # eslint-disable-line no-constant-condition
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2

            leftChild = leftChildIdx < len(self.values) and self.values[leftChildIdx]
            rightChild = rightChildIdx < len(self.values) and self.values[rightChildIdx]
            # index of child node with greater value
            swapIdx = leftChildIdx if leftChild > rightChild else rightChildIdx

            # stop swapping if bubble value greater than swapIdx value - -> list sorted
            if self.values[swapIdx] <= bubbleDownValue:
                break

            self.values[idx] = self.values[swapIdx]
            self.values[swapIdx] = bubbleDownValue
            idx = swapIdx

        return oldRoot


heap = MaxBinaryHeap()

heap.insert(33)
heap.insert(41)
heap.insert(27)
heap.insert(39)
heap.insert(12)
heap.insert(18)
heap.insert(55)


print(heap.values)  # [ 55, 39, 41, 33, 12, 18, 27 ]

"""
              55
      39              41
  33      12      18        27
"""

heap.extractMax()

print(heap.values)  # [ 41, 39, 27, 33, 12, 18 ]
