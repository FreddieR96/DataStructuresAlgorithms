import math

class Binaryheap:

  def __init__(self, root = None):
    self.heap = []
    if root:
      self.heap.append(root)

  def add(self, item):
    """
    Appends the item to the end of the heap and
    works it upwards every time it is smaller than its parent,
    after ascertaining if it is the left or right child of its
    parent, which yields a min heap.
    """   
    self.heap.append(item)
    i = len(self.heap) - 1
    while i:
      leftChildParent = math.floor((i-1)/2)
      rightChildParent = math.floor((i-2)/2)
      if leftChildParent == rightChildParent:
        if self.heap[i] < self.heap[rightChildParent]:
          temp = self.heap[i]
          self.heap[i] = self.heap[rightChildParent]
          self.heap[rightChildParent] = temp
          i = rightChildParent
      else:
        if self.heap[i] < self.heap[leftChildParent]:
          temp = self.heap[i]
          self.heap[i] = self.heap[leftChildParent]
          self.heap[leftChildParent] = temp
          i = leftChildParent

  def remove(self):
    """
    Takes the top, and smallest, element on the heap as its return
    value, then swaps it with the largest element and pops the smallest
    element out. The largest element is compared to the smaller of its children
    and swapped if necessary. The loop will also finish if there are no more children
    to compare it to.
    """
    result = self.heap[0]
    self.heap[0] = self.heap[len(self.heap)-1]
    self.heap.pop(len(self.heap)-1)
    noRepeat = False
    i = 0
    while not noRepeat:
      noRepeat = True
      try:
        compare = (2*i)+1 if self.heap[(2*i)+2] > self.heap[(2*i)+1] else (2*i)+2
      except IndexError:
        compare = (2*i)+1
      try:
        if self.heap[i] > self.heap[compare]:
          temp = self.heap[i]
          self.heap[i] = self.heap[compare]
          self.heap[compare] = temp
          i = compare
          noRepeat = False
      except IndexError:
        noRepeat = True
    return result
      