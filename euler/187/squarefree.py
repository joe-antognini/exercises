#! /usr/bin/env python

from sieve_erato import *
from sympy import sieve
import time

def square_count(N):
  primes = sievebt2lst(sieve_erato(N))
  p_i = 1
  total = 0
  primes_copy = primes[:]
  for p in primes:
    if p >= sqrt(N):
      break
    primes_copy = [s for s in primes_copy if s >= p and s <= N / p]
    total += len(primes_copy)
    p_i += 1

  return total

if __name__ == '__main__':
  N = 10**8
  print "N:", N
  start_time = time.time()
  answer = square_count(N)
  print "Number of semiprimes:", answer
  end_time = time.time()
  print "Computing time (s): %g" % (end_time - start_time)
  
