''' Implements a node as an element of a linked list
object data           the data to store
object next_node      a reference of the next node in the list, None if last element of the list
'''

class node:
  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node