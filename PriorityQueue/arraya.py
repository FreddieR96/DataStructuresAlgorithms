class Arraya(object):

  def __init__(self, capacity, fillValue = None):
    self.items = list()
    self.logicalSize = 0
    for count in range(capacity):
      self.items.append(fillValue)
      if not fillValue == None:
        self.logicalSize += 1

  def __len__(self):
    return len(self.items)

  def __iter__(self):
    i = 0
    while i < self.logicalSize:
      yield self.items[i]
      i += 1

  def __str__(self):
    for i in self.items:
      print(str(i))

  def __getitem__(self, index):
    try:
      first = index[1]
      rear = index[2]
      index = index[0]
      if first > rear and (index > rear and index < first and index >= 0):
        raise IndexError
      elif first != 0 and rear > first and (index - first) > self.logicalSize:
        raise IndexError
      elif first == 0 and rear > first and index > self.logicalSize:
        raise IndexError
      return self.items[index]
    except TypeError:
      if index > self.logicalSize - 1:
        raise IndexError
      return self.items[index]

  def __setitem__(self, index, newItem):
    try:
      first = index[1]
      rear = index[2]
      index = index[0]
      if first > rear and (index > rear and index < first and index >= 0):
        raise IndexError
      elif first != 0 and rear > first and (index - first) > self.logicalSize:
        raise IndexError
      old = self.items[index]
      self.items[index] = newItem
      if old == None:
        self.logicalSize += 1
    except TypeError:
      if index > self.logicalSize:
        raise IndexError
      old = self.items[index]
      self.items[index] = newItem
      if old == None:
        self.logicalSize += 1

  def last(self, index, first, rear):
    return ((first > rear and (index > rear and index < front)) or \
           ((first != 0 and rear > first) and (index - first == self.logicalSize)) or \
           (first == 0 and index == self.logicalSize - 1))

  def append(self, item):
    self.logicalSize += 1
    self.items[logicalSize - 1] = item

  def insert(self, item, targetIndex = None):
    if targetIndex == None:
      targetIndex = self.logicalSize
    if targetIndex > self.logicalSize:
      raise IndexError
    i = self.logicalSize
    while not i == targetIndex:
      self.items[i] = self.items[i - 1]
      i -= 1
    self.items[targetIndex] = item
    self.logicalSize += 1
    
  def remove(self, targetIndex = None):
    if targetIndex == None:
      targetIndex = self.logicalSize - 1
    if targetIndex > self.logicalSize - 1:
      raise IndexError
    i = targetIndex
    while i < self.logicalSize - 1:
        self.items[i] = self.items[i + 1]
        i += 1
    self.logicalSize -= 1