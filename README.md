# Swallows.py

This implementation runs in O(mn).

Run swallows.py and provide a flight path data file.

```bash
./chmod +x swallows.py
./swallows.py <flight-path-data-file>
```

The path data file is expected in the following format:

<unit path cost>
<start> <end> <path cost>

For example:

10
0 5 1
2 7 4

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

