#! /usr/bin/env python

import sys

def dna_string(s):
  '''Given a DNA string, return a dictionary of the number of times that the
  four bases occur.'''

  dna = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
  for char in s:
    dna[char] += 1

  return dna

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print "usage: dna.py filename"
    sys.exit(1)

  with open(sys.argv[1]) as infile:
    DATA = infile.readlines()[0].strip()
  DNA = dna_string(DATA)
  print DNA['A'],
  print DNA['C'],
  print DNA['G'],
  print DNA['T']
