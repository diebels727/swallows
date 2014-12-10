#!/usr/bin/python

import sys
import optimal_path as op
import flight_paths as fp
import graph as g

def main(filename):
  graph = g.Graph()
  start_vertex = 0
  flight_path = fp.FlightPath(start_vertex,filename)
  flight_path.build(graph)
  flight_path.link_jetstreams()
  optimal_path = op.OptimalPath(flight_path)
  optimal_path.calculate(flight_path.start)
  # print optimal_path.path[flight_path.end]
  print "Optimal Jetstream Sequence:"
  print optimal_path.path_as_flight_path_tuples(flight_path.end)
  print "Minimum Cost:"
  print optimal_path.cost[flight_path.end]

if __name__ == "__main__":
  main(sys.argv[1])
