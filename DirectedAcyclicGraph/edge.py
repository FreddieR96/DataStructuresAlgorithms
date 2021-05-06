from vertex import Vertex

class Edge:

  def __init__(self, predecessor, successor, weight = 1):
    self.predecessor = predecessor
    self.successor = successor
    self.weight = weight