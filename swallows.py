#!/usr/bin/python

import sys
# import numpy
# import pdb
# import copy

structures = {}
graph = {}
visited = {}
min = {}

def init_structures():
  structures['min'] = {}
  structures['start'] = 0
  structures['visited'] = [0]
  structures['path'] = {}
  structures['path'][0] = []

def next_static_path(v):
  static_paths = [x for x in structures['keys'] if x > v]
  if len(static_paths) == 0:
    return None
  w = static_paths[0]
  cost = (w-v)*structures['cost_unit']
  return [v,w,cost,'static']

def prev_static_path(v):
  static_paths = [x for x in structures['keys'] if x < v]
  if len(static_paths) == 0:
    return None
  w = static_paths[len(static_paths)-1]
  cost = abs(w-v)*structures['cost_unit']
  return [v,w,cost,'static']


def init_min():
  global min
  vertices = graph.keys()
  vertices.sort()
  for v in vertices:
    min[v] = float("inf")
  min[0] = 0

def compute_minimum():
  global min
  vertices = graph.keys()
  vertices.sort()

  for s in vertices:
    edges = graph[s]
    cost_s = min[s]
    for edge in edges:
      print edge
      print min

      if edge == None:
        continue
      t = edge[1]
      w = edge[2]
      cost_t = cost_s + w

      # min[t] = (min.get(t) or float("inf"))
      if cost_t < min[t]:
        min[t] = cost_t

def init_graph(s):
  global graph

  keys = structures['keys']
  keys.sort()
  if keys[0] != s:
    keys = [s] + structures['keys']

  for key in keys:
    next_path = next_static_path(key)
    prev_path = prev_static_path(key)
    graph[key] = graph.get(key) or []
    graph[key].append(next_path)
    graph[key].append(prev_path)

def main(filename):
  init_structures()
  structures['cost_unit'],structures['flight_paths'],structures['end'] = index_flight_paths(filename)
  starts = structures['flight_paths'].keys()
  starts.sort()
  structures['starts'] = starts

  keys = graph.keys()
  keys.sort()
  structures['keys'] = keys

  init_graph(0)

  print graph
  init_min()
  compute_minimum()
  print min



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
    graph[t] = (graph.get(t) or [])
    if t > end:
      end = t
  fh.close()
  return cost_unit,flight_paths,end

def normalize_path_data(line):
  # line.strip()
  tuples = line.split()
  s = int(tuples[0])
  t = int(tuples[1])
  cost = int(tuples[2])
  return s,t,cost,'jet'

if __name__ == "__main__":
  main(sys.argv[1])
