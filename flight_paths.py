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
    keys = self.graph.keys()
    keys.sort()
    return keys

  def E(self):
    return self.edges

  def G(self):
    return self.graph


class FlightPath:
  def __init__(self,start,filename):
    self.filename = filename
    self.graph = {}
    self.unit_path_cost = None
    self.end = 0
    self.start = start

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

  def link_jetstreams(self):
    vertices = self.graph.V()
    if vertices[0] != self.start:
      vertices = [self.start] + vertices
    for v in vertices:
      next_edge = self.next_jetstream_edge(v,vertices)
      prev_edge = self.prev_jetstream_edge(v,vertices)
      if not (next_edge.is_null()):
        self.graph.add_edge(next_edge)
      if not (prev_edge.is_null()):
        self.graph.add_edge(prev_edge)

  # Used to locate the next jetstream given a vertex, and ultimately
  # for connecting the flight path graph
  #  For example:  [0 1 5] are a list of jetstream start vertices
  #                given vertex '4', what is the next jetstream start.
  #                the answer is 5
  #
  def next_jetstream_edge(self,s,keys):
    paths = [x for x in keys if x > s]
    if len(paths) == 0:
      return e.NullEdge()
    t = paths[0]
    cost = abs(t-s)*self.unit_path_cost
    edge = e.Edge(s,t,cost,'non-js')
    return edge

  # Used to locate the previous jetstream given a vertex, and ultimately
  # for connecting the flight path graph
  #  For example:  [0 1 5] are a list of jetstream start vertices
  #                given vertex '4', what is the previous jetstream start.
  #                the answer is 1
  #
  def prev_jetstream_edge(self,s,keys):
    paths = [x for x in keys if x < s]
    if len(paths) == 0:
      return e.NullEdge()
    t = paths[len(paths)-1]
    cost = abs(t-s)*self.unit_path_cost
    edge = e.Edge(s,t,cost,'non-js')
    return edge


  def line_to_edge(self,line):
    tuples = line.split()
    s = int(tuples[0])
    t = int(tuples[1])
    cost = int(tuples[2])
    edge = e.Edge(s,t,cost,'jet')
    return edge

def main(filename):
  graph = Graph()
  start_vertex = 0
  flight_path = FlightPath(start_vertex,filename)
  flight_path.build(graph)
  flight_path.link_jetstreams()
  print graph.E()


if __name__ == "__main__":
  main(sys.argv[1])

