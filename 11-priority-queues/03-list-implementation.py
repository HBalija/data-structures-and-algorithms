"""
Priority queue - List

Sort O(n log n)time
Dequeue O(n)time
"""


class PriorityQueue:

    def __init__(self):
        self.values = []

    def enqueue(self, val, priority):
        self.values.append(dict(val=val, priority=priority))
        self.sort()

    def dequeue(self):
        return self.values.pop(0)

    def sort(self):
        self.values.sort(key=lambda x: x['priority'])


q = PriorityQueue()

q.enqueue('B', 3)
q.enqueue('C', 5)
q.enqueue('D', 2)
q.enqueue('Q', 20)
q.enqueue('P', 1.5)

print(q.values)

"""
values sorted based on priority

[ { val: 'P', priority: 1.5 },
  { val: 'D', priority: 2 },
  { val: 'B', priority: 3 },
  { val: 'C', priority: 5 },
  { val: 'Q', priority: 20 } ]
"""
