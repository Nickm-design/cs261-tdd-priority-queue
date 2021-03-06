# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Nick Morris

class NaivePriorityQueue:

    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if self.data != []:
            self.data.sort()
            return self.data.pop()
        return None
    
    def is_empty(self):
        return self.data == []