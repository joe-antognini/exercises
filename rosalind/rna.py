#! /usr/bin/env python

import sys

def rna_transcribe(s):
  '''Given a string of DNA return the corresponding string of RNA by
  replacing T with U.'''

  outstring = ''
  same_bases = ['A', 'C', 'G']
  for char in s:
    if char in same_bases:
      outstring += char
    elif char == 'T':
      outstring += 'U'
    else:
      raise ValueError('Unacceptable character in string.')

  return outstring

if __name__ == '__main__':
  with open(sys.argv[1]) as INFILE:
    for LINE in INFILE:
      DATA = LINE.strip()
      break

  print rna_transcribe(DATA)
