#!/usr/bin/python

import sys
import numpy
import pdb
import copy

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
  static_paths = [x for x in structures['keys'] if x > v]
  if len(static_paths) == 0:
    return None
  w = static_paths[0]
  cost = (w-v)*structures['cost_unit']
  return [v,w,cost,'static']

def init_graph(s):
  global graph

  keys = structures['keys']
  keys.sort()
  if keys[0] != s:
    keys = [s] + structures['keys']

  for key in keys:
    static_path = next_static_path(key)
    graph[key] = graph.get(key) or []
    graph[key].append(static_path)
    # graph[key] = (graph.get(key) or []).append(static_path)

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
