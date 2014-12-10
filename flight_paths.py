#!/usr/bin/python

import sys
import edge as e
# import graph as g

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
    return self.graph.keys()

  def E(self):
    return self.edges

  def G(self):
    return self.graph

class FlightPath:
  def __init__(self,filename):
    self.filename = filename
    self.graph = {}
    self.unit_path_cost = None
    self.end = 0

  def build(self,graph):
    self.graph = graph
    fh = open(self.filename, "r" )

    cost_str = fh.readline()
    self.unit_path_cost = int(cost_str)

    for line in fh:
      edge = self.line_to_edge(line)
      self.graph.add_edge(edge)
      if edge.t > self.end:
        self.end = edge.t
    fh.close()

  def line_to_edge(self,line):
    tuples = line.split()
    s = int(tuples[0])
    t = int(tuples[1])
    cost = int(tuples[2])
    edge = e.Edge(s,t,cost,'jet')
    return edge

def main(filename):
  graph = Graph()
  flight_path = FlightPath(filename)
  flight_path.build(graph)
  print graph.V()


if __name__ == "__main__":
  main(sys.argv[1])

