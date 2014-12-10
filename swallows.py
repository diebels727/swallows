#!/usr/bin/python

import sys
# import numpy
import pdb
# import copy

cost_unit = None
flight_paths = {}
end = None
graph = {}
edges = []
visited = set([])
vertices = set([])
min = {}
keys = []
frontier = set([])

def next_static_path(v):
  global cost_unit
  static_paths = [x for x in keys if x > v]
  if len(static_paths) == 0:
    return None
  w = static_paths[0]
  cost = (w-v)*cost_unit
  return [v,w,cost,'static']

def prev_static_path(v):
  global cost_unit
  static_paths = [x for x in keys if x < v]
  if len(static_paths) == 0:
    return None
  w = static_paths[len(static_paths)-1]
  cost = abs(w-v)*cost_unit
  return [v,w,cost,'static']

def init_min(s):
  global min
  vertices = graph.keys()
  vertices.sort()
  for v in vertices:
    min[v] = float("inf")
  min[s] = 0

def compute_minimum(s):
  global min
  global frontier
  global visited
  visited.add(s)
  min[s] = 0

  while visited != vertices:
    frontier = vertices - visited
    candidate,cost = calculate_min()
    t = candidate[1]
    visited.add(t)

def calculate_min():
  global min
  min_candidate = None
  min_cost = float("inf")

  for edge in candidate_edges():
    s = edge[0]
    t = edge[1]
    w = edge[2]
    current_cost = min[s] + w
    if current_cost <= min_cost:
      min_cost = current_cost
      min[t] = current_cost
      min_candidate = edge
  return min_candidate,min_cost

def candidate_edges():
  return [edge for edge in edges if (edge[0] in visited) and not (edge[1] in visited)]

def init_graph(s):
  global graph
  global keys
  global edges
  keys = graph.keys()
  keys.sort()
  if keys[0] != s:
    keys = [s] + keys
  for key in keys:
    next_path = next_static_path(key)
    prev_path = prev_static_path(key)
    graph[key] = graph.get(key) or []
    if next_path != None:
      graph[key].append(next_path)
      edges.append(next_path)
    if prev_path != None:
      graph[key].append(prev_path)
      edges.append(prev_path)

def init_vertices():
  global vertices
  vertices = set(graph.keys())

def init_visited():
  global visited
  visited = set([])

def main(filename):
  global cost_unit
  global flight_paths
  global end
  cost_unit,flight_paths,end = index_flight_paths(filename)

  init_graph(0)
  init_min(0)
  init_vertices()
  init_visited()

  compute_minimum(0)
  print min[end]

def index_flight_paths(filename):
  fh = open(filename, "r" )
  cost_str = fh.readline()
  cost_unit = int(cost_str)
  flight_paths = {}
  end = 0
  for line in fh:
    s,t,cost,path_type = normalize_path_data(line)
    flight_paths[s] = (flight_paths.get(s) or [])
    flight_paths[s].append([s,t,cost,path_type])
    graph[s] = (graph.get(s) or [])
    graph[s].append([s,t,cost,path_type])
    edges.append([s,t,cost,path_type])
    graph[t] = (graph.get(t) or [])
    if t > end:
      end = t
  fh.close()
  return cost_unit,flight_paths,end

def normalize_path_data(line):
  tuples = line.split()
  s = int(tuples[0])
  t = int(tuples[1])
  cost = int(tuples[2])
  return s,t,cost,'jet'

if __name__ == "__main__":
  main(sys.argv[1])
