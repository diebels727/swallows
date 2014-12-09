#!/usr/bin/python

import sys
import numpy
import pdb

structures = {}
graph = {}
visited = {}

def init_structures():
  structures['min'] = {}
  structures['start'] = 0
  structures['visited'] = [0]
  structures['path'] = {}
  structures['path'][0] = []

def next_static_path(v):
  static_paths = [x for x in structures['starts'] if x >= v]
  if len(static_paths) == 0:
    return None
  w = static_paths[0]
  cost = (w-v)*structures['cost_unit']
  return [v,w,cost,'static']

def init_graph(vertex):
  if vertex == None:
    return
  if visited.get(vertex):
    return

  visited[vertex] = True

  flight_paths = structures['flight_paths']
  flight_path = flight_paths.get(vertex)

  static_path = next_static_path(vertex)

  print static_path

  graph[vertex] = (graph.get(vertex) or [])

  if (static_path==None) and (flight_path==None):
    return

  if static_path:
    graph[vertex].append(static_path)
  if flight_path:
    graph[vertex].append(flight_path)

  if static_path:
    init_graph(static_path[1])
  if flight_path:
    init_graph(flight_path[1])

def main(filename):
  init_structures()
  structures['cost_unit'],structures['flight_paths'],structures['end'] = index_flight_paths(filename)
  starts = structures['flight_paths'].keys()
  starts.sort()
  structures['starts'] = starts
  init_graph(0)
  print graph



def index_flight_paths(filename):
  fh = open(filename, "r" )
  cost_str = fh.readline()
  cost_unit = int(cost_str)
  flight_paths = {}
  end = 0
  for line in fh:
    s,t,cost,path_type = normalize_path_data(line)
    flight_paths[s] = (flight_paths.get(s) or [s,t,cost,path_type])
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
