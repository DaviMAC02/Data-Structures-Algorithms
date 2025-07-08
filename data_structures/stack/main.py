
from data_structures.linked_list.main import LinkedList


class ArrayStack:
  def __init__(self):
    self.stack = []
  
  # O(1) - direct access the end of the stack
  def push(self, data):
    self.stack.append(data)

  # O(1) if dynamic array with available space .pop/ O(n) if needs to rewrite in another array
  def pop(self):
    if len(self.stack) == 0:
      raise Exception("Stack is empty")
    item = self.stack[-1]
    self.stack = self.stack[:-1] # This case the complexity is O(n) - .pop would amortize and result in O(1)
    return item

  # O(1) - direct access the end of the stack
  def peek(self):
    return self.stack[-1]
  
  # O(1) - arrays have built in size prop
  def is_empty(self):
    return len(self.stack) == 0

class LinkedListStack:
  def __init__(self):
    self.stack = LinkedList()
  
  # O(n) - traverse the entire linked list
  def push(self, data):
    self.stack.append(data)
  
  # O(n) - traverse the entire linked list
  def pop(self):
    if not self.stack.head:
      raise Exception("Stack is empty")
    item = self.stack.find(self.stack.size - 1)
    self.stack.delete(self.stack.size - 1)
    return item
  
  # O(n) - traverse the entire linked list
  def peek(self):
    return self.stack.find(self.stack.size - 1)

  # O(1) - direct access to head
  def is_empty(self):
    return self.stack.head is None
  
