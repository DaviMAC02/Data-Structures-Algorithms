from data_structures.linked_list.main import LinkedList

class ArrayQueue:
  def __init__(self):
    self.queue = []
  
  # O(n) - it copies the original array and insert at the end for fixed sized arrays/ O(1) for dynamic arrays
  def enqueue(self, data):
    self.queue.append(data)
  
  # O(n) - it copies the original array starting from the second item
  def dequeue(self):
    self.queue = self.queue[1:]
  
  # O(1) - direct memory access
  def peek(self):
    return self.queue[0]
  
  # O(1) - built in array prop
  def size(self):
    return len(self.queue)
  
  # O(1) - built in array prop
  def is_empty(self):
    return len(self.queue) == 0
  

class LinkedListQueue:
  def __init__(self):
    self.queue = LinkedList()
  
  # O(n) - traverse the entire list ans insert at the end
  def enqueue(self, data):
    self.queue.append(data)
  # O(1) - just assign head to the second item and drop first pointer
  def dequeue(self):
    self.queue.head = self.queue.head.next
  # O(1) - direct memory access
  def peek(self):
    return self.queue.head
  # O(n) - needs to traverse the entire list to count the size
  def size(self):
    size = 0
    
    current_node = self.queue.head
    while current_node:
      size += 1
      current_node = current_node.next
    
    return size
  # O(1) - no head no list
  def is_empty(self):
    return not self.queue.head