class Directedgraph:

  def __init__(self):
    self.vertices = []
    self.root = None

  def sizeVertices(self):
    return len(self.vertices)

  def sizeEdges(self):
    i = 0
    for vertex in self.vertices:
      for edge in vertex.edges:
        if edge.predecessor == vertex:
          i += 1
    return i

  def addVertex(self, vertex):
    if vertex in self.vertices:
      print("Vertex already in graph")
      return
    if not self.vertices:
      self.root = vertex
    self.vertices.append(vertex)

  def addEdge(self, theEdge):
    predecessor = theEdge.predecessor
    successor = theEdge.successor
    if predecessor == successor:
      print("edge predecessor and successor can't be the same")
      return
    if not predecessor in self.vertices or not successor in self.vertices:
      print("predecessor and/or successor not in graph")
      return
    for vertex in self.vertices:
      for edge in vertex.edges:
        if (edge.predecessor == predecessor and edge.successor == successor) \
        or (edge.successor == predecessor and edge.predecessor == successor):
          print("edge already in graph")
          return
    predecessor.edges.append(theEdge)
    if self.checkCycle():
      predecessor.edges.remove(theEdge)
      print("edge causes a cycle")

  def checkCycle(self, vertex = None, coveredList = None):
    """
    Assigns a unique list to every vertex in the graph, detailing how
    to get there from the root vertex. It returns True if a vertex is going 
    to appear twice in a coveredlist, indicating there is a cycle in the graph
    or sub graph.
    """
    if not vertex:
      vertex = self.root
      coveredList = []
    else:
      coveredList = list(coveredList)
    for edge in vertex.edges:
      if edge.successor in coveredList:
        return True
      coveredList.append(edge.predecessor)
      if self.checkCycle(edge.successor, coveredList):
        return True
    return False
      
  def breadthFirstTraversal(self):
    vertices = []
    results = []
    vertices.append(self.root)
    while vertices:
      vertex = vertices.pop(0)
      for edge in vertex.edges:
        vertices.append(edge.successor)
      results.append(vertex)
    return results

  def depthFirstTraversal(self, vertex = None, results = None):
    if not vertex:
      vertex = self.root
      results = []
    for edge in vertex.edges:
      results.append(edge.successor)
      self.depthFirstTraversal(edge.successor, results)
    return results

  def dijkstra(self, rootVertex = None, endVertex = None):
    """
    This method is a dijkstra algorithm that returns a grid with each vertex,
    its minimum distance from the selected root, its parent, and an array of directions
    for the quickest path to get there from the selected root.
    
    At first, a grid is prepared from all the vertices in the graph. The vertex
    is added, the minimum distance and parent are set to false, and the directions
    array is empty.

    For every vertex in the array, all of its unvisited edges are checked and if the minimum
    distance value is greater than the parent minimum distance plus edge weight, the values
    will be updated with the minimum distance, the parent vertex, and the directions will be
    the parent's directions plus the parent itself. The parent vertex will then be marked.

    The parent vertex will then be reassigned as the unmarked vertex with the smallest minimum
    distance to the root and a parent value. The parent value is required to stop subgraphs
    disconnected from the root being included.

    If an endVertex parameter is given the function will return directions of getting there
    from the root vertex.
    """
    results = []
    root = 0
    a = 0
    for vertex in self.vertices:
      i = []
      i.append(vertex)
      i.append(False)
      i.append(False)
      i.append([])
      results.append(i)
      if rootVertex and rootVertex == vertex.value:
        root = a
      elif vertex == self.root:
        root = a
      a += 1
      vertex.marked = False
    results[root][1] = 0
    results[root][2] = True
    vertex = results[root]
    while vertex:
      for edge in vertex[0].edges:
        if not edge.successor.marked:
          child = None
          for result in results:
            if result[0] == edge.successor:
              child = result
              break
          if not child[1] or child[1] > vertex[1] + edge.weight:
            child[1] = vertex[1] + edge.weight
            child[2] = vertex[0]
            child[3] = list(vertex[3])
            child[3].append(vertex[0])
      vertex[0].marked = True
      if endVertex and vertex[0].value == endVertex:
        return vertex[3]
      vertex = None
      a = 0
      for result in results:
        if not vertex and not result[0].marked and result[2]:
          vertex = result
        if vertex and not result[0].marked and result[2] and result[1] < vertex[1]:
          vertex = result
        a += 1
    return results 
            
    
    
      