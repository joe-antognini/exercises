#! /usr/bin/env python

def spiral_diag_sum(N):
  '''Return the sum along the diagonals of an N x N grid of numbers.'''

  ret = 1 # The center is counted twice
  for i in range(3, N+1, 2):
    ret += 4 * i**2 - 6 * (i - 1)
  
  return ret

if __name__ == '__main__':
  print sprial_diag_sum(1001)
