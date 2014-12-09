#!/usr/bin/python

import sys
import numpy

def init_structures(structures):
  structures['min'] = {}
  structures['start'] = 0
  structures['visited'] = [0]
  structures['path'] = {}
  structures['path'][0] = []

# def calculate_min(start,structures):
#   min_cost = float('inf')


def main(filename):
  structures = {}
  init_structures(structures)
  structures['cost_unit'],structures['flight_paths'],structures['end'] = index_flight_paths(filename)

  print structures


def index_flight_paths(filename):
  fh = open(filename, "r" )
  cost_str = fh.readline()
  cost_unit = int(cost_str)
  flight_paths = {}
  end = 0
  for line in fh:
    s,t,cost = normalize_path_data(line)
    flight_paths[s] = (flight_paths.get(s) or [s,t,cost])
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
  return s,t,cost

if __name__ == "__main__":
  main(sys.argv[1])
