import optimal_path as op
import flight_paths as fp
import graph as g

def setup_flight_path(str):
  graph = g.Graph()
  start_vertex = 0
  flight_path = fp.FlightPath(start_vertex,'')
  flight_path.build_from_string(graph,str)
  flight_path.link_jetstreams()
  optimal_path = op.OptimalPath(flight_path)
  optimal_path.calculate(flight_path.start)
  return optimal_path.cost[flight_path.end],optimal_path.path_as_flight_path_tuples(flight_path.end)

def test_trivial():
  trivial = """10
0 1 1"""
  cost,path = setup_flight_path(trivial)
  assert cost == 1


