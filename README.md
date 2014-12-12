# swallows.py

This program implements a solution to solve a minimum cost graph problem.  The number of edges in this graph is on the order of thousands and runs in O(mn).

A flight path graph may look, as follows:

![graph] (https://github.com/diebels727/swallows/raw/graphic/graph.png)

The jetstreams are identified by segments 0-3 and 2-4.  The non-jetstream path 0-1-2-3-4 has a constant cost for flying between vertices -- in this case it is a cost of 10.

The minimum cost path for a swallow to fly, on this graph is: 0 -> 3, 3 -> 2, and 2 -> 4, with a minimum cost of 12. 

## Running the Program

Run swallows.py and provide a flight path data file.

```bash
./chmod +x swallows.py
./swallows.py <flight-path-data-file>
```

The data file is expected to be in the format as follows:

```bash
10
0 3
2 4
```

This data file describes the graph above.

## Running Tests

Install pytest.

```bash
pip install pytest
```

Configure your python path from the project root.

```bash
export PYTHONPATH=$PYTHONPATH:`pwd`
```

Run the tests from the project root.

```bash
./py.test
```

