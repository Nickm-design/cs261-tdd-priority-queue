# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# Nick Morris

class MaxHeap:

   def __init__(self):
      self._data = []
   
   def _size(self):
      return len(self._data)

   def _is_empty(self):
      return self._data == []

   def _last_index(self):
      if self._is_empty():
         return self._size() - 1
      return self
