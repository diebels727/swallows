import copy
import flight_paths as fp
import graph as g

class OptimalPath:
  def __init__(self,flight_path):
    self.graph = flight_path.graph
    self.visited = set([])
    self.vertices = set(self.graph.V())
    self.cost = {}
    self.path = {}
    for v in self.graph.V():
      self.cost[v] = float("inf")

  def calculate(self,start):
    self.visited.add(start)
    self.cost[start] = 0
    while self.visited != self.vertices:
      min_edge,min_cost = self.determine_min_edge()
      self.visited.add(min_edge.t)

  # Determine edges with tail in optimal set and head in the frontier
  def candidates(self):
    return [edge for edge in self.graph.E() if (edge.s in self.visited) and not (edge.t in self.visited)]

  def determine_min_edge(self):
    candidate = None
    cost = float("inf")
    for current_candidate in self.candidates():
      current_cost = self.cost[current_candidate.s] + current_candidate.w
      if current_cost < cost:
        cost = current_cost
        candidate = current_candidate
    path_to_s = self.path.get(candidate.s) or []
    path = copy.copy(path_to_s)
    path.append(candidate)
    self.cost[candidate.t] = cost
    self.path[candidate.t] = path
    return candidate,cost

  def path_as_flight_path_tuples(self,vertex):
    return ["(%d,%d)" % (edge.s,edge.t) for edge in self.path[vertex] if edge.type == 'jet']
