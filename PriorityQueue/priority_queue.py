from arraya import Arraya

class PriorityQueue:

  def __init__(self, init = 5):
    self.front = 0
    self.rear = 0
    self.queue = Arraya(init)
    self.makeNew = False

  def add(self, item):
    """
    If the queue is full then the length of the queue is doubled. You can tell this 
    if the front of the queue is at index 0 and the rear
    of the queue is at the rear of the array or if the front of the queue is only one
    index ahead of the rear, which means the queue has snaked round but has now filled up.

    If the queue is empty, then the item is added to the rear index. Otherwise, the queue
    is traversed until the item is smaller than the item at that index. The item is added to this
    index and all subsequent items in the queue are moved back by one position.
    """
    if ((self.front == 0 and self.makeNew) or ((self.front > self.rear) and (self.front - self.rear == 1))):
      new = Arraya(len(self.queue) * 2)
      i = self.front
      a = 0
      stop = False
      while not stop:
        new[a] = self.queue[i, self.front, self.rear]
        i += 1
        a += 1
        if i == len(self.queue):
          i = 0
        if i == self.rear:
          stop = True
      self.front = 0
      self.rear = a
      self.queue = new
    if (self.front == 0 and self.rear == 0) or item > self.queue[self.rear - 1, self.front, self.rear]:
      self.queue[self.rear, self.front, self.rear] = item
    else:
      i = self.front
      while self.queue[i, self.front, self.rear] and item >= self.queue[i, self.front, self.rear]:
        if i == len(self.queue) - 1:
          i = 0
        else:
          i += 1
      hold = self.queue[i, self.front, self.rear]
      self.queue[i, self.front, self.rear] = item
      stop = False
      while hold and not stop:
        if i == len(self.queue) - 1:
          i = -1
        temp = self.queue[i + 1, self.front, self.rear]
        self.queue[i + 1, self.front, self.rear] = hold
        hold = temp
        i += 1
        stop = i == self.rear
    self.rear += 1
    self.makeNew = False
    if self.rear == len(self.queue):
      self.rear = 0
      self.makeNew = True

  def pop(self):
    item = self.queue[self.front, self.front, self.rear]
    self.queue[self.front] = None
    self.queue.logicalSize -= 1
    self.front += 1
    if self.front > len(self.queue):
      self.front = 0
    return item