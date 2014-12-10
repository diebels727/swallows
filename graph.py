class Graph:
  def __init__(self):
    self.graph = {}
    self.edges = []
    self.vertices = []

  def add_edge(self,edge):
    s = edge.s
    t = edge.t
    self.graph[s] = (self.graph.get(s) or [])
    self.graph[s].append(edge)
    self.graph[t] = (self.graph.get(t) or [])
    self.edges.append(edge)

  def V(self):
    keys = self.graph.keys()
    keys.sort()
    return keys

  def E(self):
    return self.edges

  def G(self):
    return self.graph