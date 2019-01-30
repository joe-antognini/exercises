#! /usr/bin/env python

from sympy.ntheory.primetest import isprime
from sympy import sieve
import time

def quadratic_primes(max_coefficient):
  '''Calculate the product of the coefficients that generate the most primes
  for a sequence of n starting with n=0 of the form:

  n^2 + an + b

  for |a| < max_coefficient and |b| < max_coefficient.
  '''

  b_lst = list(sieve.primerange(1, max_coefficient))

  max_n = 0
  for a in range(-max_coefficient + 1, max_coefficient):
    for b in b_lst:
      n = 0
      while isprime(n**2 + a * n + b):
        n += 1
      if n > max_n:
        max_n = n
        max_product = a * b

  return max_product

if __name__ == '__main__':
  START_TIME = time.time()
  MAX_COEFFICIENT = 1000
  print "Max coefficient:", MAX_COEFFICIENT
  print "Solution:", quadratic_primes(MAX_COEFFICIENT)
  print "Running time: %.2g" % (time.time() - START_TIME)
