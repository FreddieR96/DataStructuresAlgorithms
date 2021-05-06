from hashlist import Hashlist

class Hash:

  def __init__(self):
    self.taken = 0
    self.list = Hashlist(4)

  def __setitem__(self,index,newItem):
    if self.taken/4 > len(self.list)/3:
      self.list = Hashlist(len(self.list)*2, self.list)
    old = self.list.items[self.list.toIndex(index)]
    self.list[index] = newItem
    if not old:
      self.taken += 1

  def __getitem__(self,index):
    return self.list[index]

  def remove(self, index):
    if self.list.remove(index):
      self.taken -= 1
  