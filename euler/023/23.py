#! /usr/bin/env python

#
# Project Euler
# Problem 23
#
# Joe Antognini
# Fri Jan 17 16:26:11 EST 2014
#

from bisect import bisect_left

maxnum = 28123
#maxnum = 10000

file = open('23.dat', 'r')
abundant = map(int, file.readlines())
file.close()

def binary_search(a, x, lo=0, hi=None):
  hi = hi if hi is not None else len(a)
  pos = bisect_left(a, x, lo, hi)
  return (pos if pos != hi and a[pos] == x else -1)

def calc_total(maxnum, sums):
  '''Calculate the total of all numbers not in sums up to maxnum.'''

  total = 0
  for i in range(maxnum):
    if i not in sums:
      total += i
  return total

def all_sums(maxnum):
  '''Perform the calculation by computing every possible sum.'''
  i = 0
  sums = []
  abundant_iter_i = iter(abundant)
  abundant_i = abundant_iter_i.next()
  while abundant_i < maxnum / 2:
    abundant_iter_j = iter(abundant[i:])
    abundant_j = abundant_iter_j.next()
    while abundant_i + abundant_j < maxnum:
      sum = abundant_i + abundant_j

      # This may be the bottleneck for the code.  Do a binary search instead.
      if binary_search(sums, sum) == -1:
      #if sum not in sums:
        sums.append(sum)
      abundant_j = abundant_iter_j.next()
    abundant_i = abundant_iter_i.next()
    i += 1

  return calc_total(maxnum, sums)

def some_sums(maxnum):
  '''Perform the calculation by computing whether the sums exist for each
  number.'''
  
  no_sum = []

  for x in range(maxnum):
    abundant_iter = iter(abundant)
    while True:
      try:
        abundant_i = abundant_iter.next()
      except StopIteration:
        no_sum.append(x)
        break
      if binary_search(abundant, x - abundant_i) != -1:
        break
  
  return sum(no_sum)

print some_sums(maxnum)
