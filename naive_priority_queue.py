# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Nick Morris

class NaivePriorityQueue:

    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        self.data.sort()
        return self.data.pop()
    
    def is_empty(self):
        return self.data == []