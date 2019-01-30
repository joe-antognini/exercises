#! /usr/bin/env python

from math import sqrt
from sympy import sieve
import time

def count_squarefree(N):
  '''Return the number of squarefree integers below N.'''

  mobius = [1] * int(sqrt(N))
  for p in sieve.primerange(2, int(sqrt(N))):
    for i in xrange(p, int(sqrt(N)), p):
      mobius[i-1] = -mobius[i-1]
    for i in xrange(p**2, int(sqrt(N)), p**2):
      mobius[i-1] = 0

  return sum([(N / p**2) * mobius[p-1] for p in xrange(1, int(sqrt(N)))])

if __name__ == '__main__':
  n = 50
  N = 2**n
  print "N: 2^%d" % n
  start_time = time.time()
  print "Answer:", count_squarefree(N)
  end_time = time.time()
  print "Computing time: %g" % (end_time - start_time)
