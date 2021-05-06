class Treenode:

  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    print(str(self.data))

  def isLeaf(self):
    return self.left == None and self.right == None