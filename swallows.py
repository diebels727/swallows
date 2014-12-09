#!/usr/bin/python

import sys

def main(filename):
  content = read_file(filename)

def read_file(filename):
  fh = open(filename, "r" )
  array = []
  for line in fh:
      line = line.strip()
      array.append( line )
  fh.close()
  return array


if __name__ == "__main__":
  main(sys.argv[1])
