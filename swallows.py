#!/usr/bin/python

import sys

def main(filename):
  fh = open(filename, "r" )
  array = []
  for line in fh:
      line = line.strip()
      print line
      array.append( line )
  fh.close()

if __name__ == "__main__":
  main(sys.argv[1])
