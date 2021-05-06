from item import Item
from node import Node

class Hashlist:

  def __init__(self, length = 4, oldItems = None):
    """
    The parent hash sometimes passes an array to this method
    when it makes a larger hashlist after the occupied indexes
    of the items list have crossed a certain threshold.
    """
    i = 0
    self.items = list()
    while i < length:
      self.items.append(None)
      i += 1
    if oldItems:
      for x in oldItems:
        if x:
          item = Item(x.data.key,x.data.value)
          self.items[self.toIndex(x.data.key)] = Node(item)
          while x.next:
            x = x.next
            item = Item(x.data.key,x.data.value)
            self.items[self.toIndex(x.data.key)] = Node(item)

  def __len__(self):
    return len(self.items)

  def __setitem__(self, index, newItem):
    if not type(index) == str:
      raise TypeError
    i = self.toIndex(index)
    node = self.items[i]
    item = Item(index,newItem)
    if node:
      while node:
        if node.data.key == index:
          node.data.value = newItem
          return
        elif not node.next:
          node.next = Node(item)
          return
        node = node.next
    else:
      self.items[i] = Node(item)

  def __getitem__(self, index):
    item = self.items[self.toIndex(index)]
    if item:
      while item:
        if item.data.key == index:
          return item.data.value
        item = item.next

  def __iter__(self):
    for x in self.items:
      yield x

  def remove(self,index):
    """
    First, the index of the item to be removed is found.
    The linked list is traversed until the item is found.
    There are four ways of taking out the item, depending on whether
    it is the first item in the linked list and whether it has a following
    item. The method returns True if the item was the first and only item
    in the linked list, to indicate that the items list has a newly unoccupied
    index.
    """
    i = self.toIndex(index)
    item = self.items[i]
    if item:
      parent = item
      while item:
        if item.data.key == index:
          if parent == item and not item.next:
            self.items[i] = None
            return True
          elif parent == item and item.next:
            self.items[i] = item.next
            return False
          elif item.next:
            parent.next = item.next
            return False
          else:
            parent.next = None
            return False
        if not parent is item:
          parent = parent.next
        item = item.next

  def toIndex(self,key):
    i = 0
    for x in key:
      i += ord(x)
    return i % len(self)
    