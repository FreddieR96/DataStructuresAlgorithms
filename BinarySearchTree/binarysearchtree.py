from treenode import Treenode

class Binarysearchtree:

  def __init__(self, item = None):
    self.root = item

  def remove(self, item, root = None, parent = None, right = False):
    """
    Removes a node from the tree when the item parameter corresponds
    to the node's data. If the item is not the tree root, then the tree
    will be descended until the node is found and the function will be called
    again, but with parameters of the node parent and whether or not the node is
    a left or a right child of its parent.

    In this way, the parent has its left or right node replaced with the left or
    right child of the target node, if the target only has one child. If the target
    has two children, then it is replaced by the rightmost descendant of its left child.
    """
    if not root:
      root = self.root
    if item == root.data and root.left and not root.right:
      if parent and not right:
        parent.left = root.left
      elif parent and right:
        parent.right = root.left
      else:
        root = root.left
        self.root = root
    elif item == root.data and root.right and not root.left:
      if parent and not right:
        parent.left = root.right
      elif parent and right:
        parent.right = root.right
      else:
        root = root.right
        self.root = root
    elif item == root.data and not root.left and not root.right:
      if item == self.root.data:
        self.root = None
      elif right:
        parent.right = None
      else:
        parent.left = None
    elif item == root.data:
      nodeparent = root.left
      node = root.left
      while node.right:
        nodeparent = node
        node = node.right
      if not node == root.left:
        self.remove(node.data, node, nodeparent, True)
        node.left = root.left
        node.right = root.right
        if parent and right:
          parent.right = node
        elif parent and not right:
          parent.left = node
        else:
          self.root = node 
      else:
        node.right = root.right
        if parent and right:
          parent.right = node
        elif parent and not right:
          parent.left = node
        else:
          self.root = self.root.left
    else:
      node = root
      parent = root
      right = False
      while not node.data == item:
        parent = node
        if item > node.data:
          node = node.right
          right = True
        elif item < node.data:
          node = node.left
          right = False
      self.remove(item, node, parent, right)

  def add(self, item):
    if not self.root:
      self.root = Treenode(item)
      return
    node = self.root
    attached = False
    while not attached:
      if item <= node.data:
        if node.left:
          node = node.left
        else:
          node.left = Treenode(item)
          attached = True
      elif item > node.data:
        if node.right:
          node = node.right
        else:
          node.right = Treenode(item)
          attached = True

  def preorder(self, tree = None):
    if not tree:
      tree = self.root
    print(tree.data)
    if tree.left:
      self.preorder(tree.left)
    if tree.right:
      self.preorder(tree.right)

  def levelorder(self):
    nodes = []
    data = []
    nodes.append(self.root)
    data.append(self.root.data)
    while nodes:
      i = nodes.length - 1
      a = 0
      while a <= i:
        node = nodes.pop(0)
        data.append(node.data)
        if node.left:
          nodes.append(node.left)
        if node.right:
          nodes.append(node.right)
        a += 1
    for x in data:
      print(x)

  def __str__(self):
    self.preorder()