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

  path = ["%d%d" % (edge.s,edge.t) for edge in optimal_path.path[flight_path.end] if edge.type == 'jet']

  return optimal_path.cost[flight_path.end],path

def test_trivial():
  trivial = """10
0 1 1"""
  cost,path = setup_flight_path(trivial)
  assert cost == 1

def test_over_weight():
  weight = """10
  0 1 100"""
  cost,path = setup_flight_path(weight)
  assert cost == 10

def test_under_weight():
  weight = """0
  0 1 100"""
  cost,path = setup_flight_path(weight)
  assert cost == 0
  assert path == []

def test_sample():
  sample = """50
  0 5 10
  1 3 5
  3 7 12
  6 11 20
  14 17 8
  19 24 14
  21 22 2"""
  cost,path = setup_flight_path(sample)
  assert cost == 352
  assert path == ['05', '611', '1417', '1924']

def test_backtrack():
  backtrack = """10
  0 3 1
  2 5 1"""
  cost,path = setup_flight_path(backtrack)
  assert cost == 12
  assert path == ['03','25']

def test_rainbow():
  rainbow = """50
  1 6 14
  3 4 2"""
  cost,path = setup_flight_path(rainbow)
  assert cost == 64
  assert path == ['16']

def test_sequence():
  rainbow = """1
  0 1 1
  1 2 1
  2 3 1"""
  cost,path = setup_flight_path(rainbow)
  assert cost == 3
  assert path == ['01','12','23']




