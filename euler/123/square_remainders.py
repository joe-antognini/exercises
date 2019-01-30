#! /usr/bin/env python

from sympy import sieve
import time

def prime_square_remainder(target):
  '''Calculate the least value n such that the remainder exceeds the
  target.'''
  for i, p in enumerate(sieve.primerange(1, 1e6)):
    bini = bin(i+1)[2:][::-1]
    leftterm = 1
    rightterm = 1
    for j, elem in enumerate(bini):
      if elem == '1':
        leftterm *= (2**j * p + 1)
        if j != 0:
          rightterm *= (1 - 2**j * p)
        else:
          rightterm *= (p - 1)
        leftterm %= p**2
        rightterm %= p**2
    if (leftterm + rightterm) % p**2 > target:
      return i + 1

if __name__ == '__main__':
  start_time = time.time()
  print "Answer:", prime_square_remainder(1e10)
  end_time = time.time()
  print "Comuputing time: %g s" % (end_time - start_time)
