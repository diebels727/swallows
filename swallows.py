#!/usr/bin/python

import sys
import numpy

def main(filename):
  cost_unit,flight_paths = index_flight_paths(filename)
  print cost_unit
  print flight_paths
  # cost_per_mile = content[0]
  # flight_paths = content[1:]

  #index flight paths


def index_flight_paths(filename):
  fh = open(filename, "r" )
  cost_str = fh.readline()
  cost_unit = int(cost_str)
  flight_paths = {}
  for line in fh:
    s,t,cost = normalize_path_data(line)
    flight_paths[s] = (flight_paths.get(s) or [s,t,cost])
  return cost_unit,flight_paths


  fh.close()
  return array

def normalize_path_data(line):
  # line.strip()
  tuples = line.split()
  s = int(tuples[0])
  t = int(tuples[1])
  cost = int(tuples[2])
  return s,t,cost

if __name__ == "__main__":
  main(sys.argv[1])
