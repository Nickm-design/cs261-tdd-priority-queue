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
      return self._size() - 1
      
   def _value_at(self, value):
      return self._data[value]

   def _left_child_index(self, value):
      return (2 * value) + 1
   
   def _right_child_index(self, value):
      return (2 * value) +2
   
   def _parent_index(self, value):
      if value % 2 == 0:
         return (value // 2) -1
      return (value // 2) 

   def _parent(self, value):
      if value != self._parent_index(value):
         raise IndexError()
      return self._value_at(value)