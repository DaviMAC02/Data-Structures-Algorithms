

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  

class LinkedList:
  def __init__(self):
    self.head = None
  
  # O(n) - trasverse the entire list
  def append(self, data):
    if not self.head:
      self.head = Node(data)
      return
    
    current_node = self.head
    while current_node.next:
      current_node = current_node.next
    
    current_node.next = Node(data)
  
  # O(n) - trasverse the entire list
  def delete(self, index):
    current_index = 0
    current_node = self.head
    previous_node = None

    if not current_node:
      return
    
    while current_node:
      if current_index == index and index == 0:
        self.head = current_node.next
        return

      if current_index == index:
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
    
  

# Create a new singly linked list
ll = LinkedList()

# Append elements
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

# Display the list
print("Initial list:")
ll.display()  # Output: 10, 20, 30, 40

# Find a value by index
print("\nElement at index 2:", ll.find(2))  # Output: 30

# Delete the element at index 1 (value 20)
ll.delete(1)
print("\nAfter deleting index 1:")
ll.display()  # Output: 10, 30, 40

# Reverse the list
ll.reverse()
print("\nAfter reversing:")
ll.display()  # Output: 40, 30, 10

# Delete head
ll.delete(0)
print("\nAfter deleting head (was 40):")
ll.display()  # Output: 30, 10

# Try deleting tail
ll.delete(1)
print("\nAfter deleting tail (was 10):")
ll.display()  # Output: 30



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



# Create a new doubly linked list
dll = DoubleLinkedList()

# Append some elements
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

# Display the list
print("Initial list:")
dll.display()  # Output: 10, 20, 30, 40

# Find a value by index
print("\nElement at index 2:", dll.find(2))  # Output: 30

# Delete the element at index 1 (value 20)
dll.delete(1)
print("\nAfter deleting index 1:")
dll.display()  # Output: 10, 30, 40

# Reverse the list
dll.reverse()
print("\nAfter reversing:")
dll.display()  # Output: 40, 30, 10

# Try deleting head
dll.delete(0)
print("\nAfter deleting head (now 40):")
dll.display()  # Output: 30, 10

# Try deleting tail
dll.delete(1)
print("\nAfter deleting tail (now 10):")
dll.display()  # Output: 30

  
    

