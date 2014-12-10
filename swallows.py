#!/usr/bin/python

import sys
import flight_paths as fp
import graph as g

class OptimalPath:
  def __init__(self,flight_path):
    self.graph = flight_path.graph
    self.visited = set([])
    self.vertices = set(self.graph.V())
    self.cost = {}

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
        self.cost[current_candidate.t] = current_cost
        candidate = current_candidate
    return candidate,cost

def main(filename):
  graph = g.Graph()
  start_vertex = 0
  flight_path = fp.FlightPath(start_vertex,filename)
  flight_path.build(graph)
  flight_path.link_jetstreams()
  optimal_path = OptimalPath(flight_path)
  optimal_path.calculate(flight_path.start)
  print optimal_path.cost

if __name__ == "__main__":
  main(sys.argv[1])
