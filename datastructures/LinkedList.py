from Node import *

class LinkedList:

  ''' The LinkedList Class stores data as Node Objects in a linked list
      push/pop represents a LIFO (last pushed in, first pushed out)
      push/poll a FIFO (first pushed in, first pushed out)

      LinkedList
                        node                            nect_node
         head   |---------|---------|   |---------|---------|
        ------->| data    |next_node|   | data    |next_node|
                |---------|---------|   |---------|---------|
                               |             ^          |
                               |             |          |
                               |-------------|         ___ None
                                                        _

      Node node data  object
      object          data
      linkreference   next_node

  '''

  def __init__(self, head = None):
    self.head = head

  def push(self, data):
    '''Push data ar the top of the linked list'''
    tmpnode = node(data)
    if (self.head == None):
      tmpnode.next_node = self.head
      self.head = tmpnode
    else:
      current = self.head
      while current.next_node:
        current = current.next_node
      current.next_node = tmpnode
    return self.size

  def pop(self):
    '''Pop data from stack, increments size of stack'''
    current = self.head
    if (current == None):
      return None
    last_node = self.head
    if (self.size == 1):
      self.head = None
      return current.data
    else:
      while current.next_node:
        last_node = current
        current = current.next_node
      last_node.next_node = None
    return current.data

  def poll(self):
    '''Returns the first entered element of the list (probably the oldest element in the queue'''
    current = self.head
    if (current == None):
      return None
    next = current.next_node
    self.head = next
    return current.data

  def get_element(self, data):
    '''Returns the first element with the given data, Same as search()'''
    return search(data)

  def size(self):
    '''Number of elements in the List'''
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count

  def traversal(self):
    '''Test function to print all elements in a list'''
    current = self.head
    while current.next_node:
      print(current.data)
      current = current.next_node
    print(current.data)

  def remove(self, data):
    '''Removes an element in the list and reorganize the list'''
    if (self.head == None):
      return
    current = self.head
    if current.data == data:
      self.head = current.next_node
    while current.next_node:
      if current.next_node.data == data:
        current.next_node = current.next_node.next_node
      else:
        current = current.next_node


  def insert_at_first(self, data):
    tmpnode = node(data)
    tmpnode.next_node = self.head
    self.head = tmpnode

  def insert_at_end(self, data):
    '''Insert an element at the top 'of the list. Same as push()'''
    self.push(data)

  def search(self, data):
    '''Returns the first element with the given data or None'''
    current = self.head
    if (current == None):
      return None
    found = False
    while current and found is False:
      if current.data == data:
        found = True
      else:
        current = current.next_node
    if (found is False):
      current = None
    return current
