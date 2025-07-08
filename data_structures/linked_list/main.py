

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  

class LinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
  
  # O(n) - trasverse the entire list
  def append(self, data):
    if not self.head:
      self.size += 1
      self.head = Node(data)
      return
    
    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    
    current_node.next = Node(data)
    self.size += 1

  
  # O(n) - trasverse the entire list
  def delete(self, index):
    current_index = 0
    current_node = self.head
    previous_node = None

    if not current_node:
      return
    
    while current_node:
      if current_index == index and index == 0:
        self.size -= 1
        self.head = current_node.next
        return

      if current_index == index:
        self.size -= 1
        previous_node.next = current_node.next
        return
      previous_node = current_node
      current_node = current_node.next
      current_index += 1
    raise Exception("Index out of bounds")


  
  # O(n) - trasverse the entire list
  def display(self):
    if self.head is None:
      print("Linked List is empty!")
      return
    current_node = self.head

    if not current_node.next:
      print(current_node.data)
      return

    while current_node.next:
      print(current_node.data)
      current_node = current_node.next
    
    print(current_node.data)
  
  # O(n) - traverse the entire list
  def find(self, index):
    current_index = 0
    if not self.head:
      raise Exception("Linked list is empty")
    
    current_node = self.head
    while current_node:
      if index == current_index:
        return current_node.data
      current_index += 1
      current_node = current_node.next
    raise Exception("Index out of bounds")

  # O(n) - traverse the entire list
  def reverse(self):
    previous_node = None
    current_node = self.head

    if(not current_node or not current_node.next):
      return

    while current_node:
      next_node = current_node.next
      current_node.next = previous_node
      previous_node = current_node
      current_node = next_node
      
    self.head = previous_node
    

class DoubleNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  # O(1) - direct access to the end of the list
  def append(self, data):
    if not self.head and not self.tail:
      first_node = DoubleNode(data)
      self.head = first_node
      self.tail = first_node
      return
    
    self.tail.next = DoubleNode(data)
    pre_append_tail = self.tail
    self.tail = self.tail.next
    self.tail.previous = pre_append_tail

  # O(n) - traverse the entire list
  def delete(self, index):
    current_index = 0
    current_node = self.head

    if not current_node:
      raise Exception("Linked List is empty")
    
    while current_node:
      if current_index == index and index == 0:
        self.head = self.head.next
        if self.head:
          self.head.previous = None
        return

      if current_index == index:
        current_node.previous.next = current_node.next
        if current_node.next:
          current_node.next.previous = current_node.previous
        return
      current_node = current_node.next
      current_index += 1
    
    raise Exception("Index out of bounds")

  # O(n) - traverse the entire list
  def display(self):
    current_node = self.head
    if not current_node:
      raise Exception("Linked List is empty")

    while current_node:
      print(current_node.data)
      current_node = current_node.next
  
  # O(n) - traverse the entire list
  def find(self, index):
    current_index = 0
    current_node = self.head

    if not current_node:
      raise Exception("Linked List is empty")
    
    while current_node:
      if index == current_index:
        return current_node.data
      current_node = current_node.next
      current_index += 1
    raise Exception("Index out of bounds")
  
  # O(n) - traverse the entire list
  def reverse(self):
    if not self.tail:
      raise Exception("Linked List is empty")
    reversed_list = DoubleLinkedList()
    current_node = self.tail
    while current_node:
      reversed_list.append(current_node.data)
      current_node = current_node.previous
    
    self.head = reversed_list.head
    self.tail = reversed_list.tail


