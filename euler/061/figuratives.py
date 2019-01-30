#! /usr/bin/env python

#
# Project Euler
# Problem 61
#
# Find the sum of the only ordered set of six cyclic 4-digit numbers for
# which each polygonal type is represented by a different number in the set.
#

import time
start_time = time.time()

# First generate the figurative numbers
N = 150 # Some large number...
lb = 1000
ub = 10000
triangles = [n*(n+1)/2 for n in range(N)]
triangles = [elem for elem in triangles if lb <= elem < ub]
squares = [n*n for n in range(N)]
squares = [elem for elem in squares if lb <= elem < ub]
pentagons = [n*(3*n-1)/2 for n in range(N)]
pentagons = [elem for elem in pentagons if lb <= elem < ub]
hexagons = [n*(2*n-1) for n in range(N)]
hexagons = [elem for elem in hexagons if lb <= elem < ub]
heptagons = [n*(5*n-3)/2 for n in range(N)]
heptagons = [elem for elem in heptagons if lb <= elem < ub]
octagons = [n*(3*n-2) for n in range(N)]
octagons = [elem for elem in octagons if lb <= elem < ub]

figures = [squares, pentagons, hexagons, heptagons, octagons]
#figures = [squares, pentagons]

def split_integer(n):
  '''Return a list with the first two digits and last two digits.'''
  if n < lb or n >= ub:
    raise ValueError('split_integer(): n must be four digits long')

  first = n / 100
  last = n % 100

  return [first, last]

def find_index(lst, n):
  '''Return the index of the first element of the list that is greater than
  or equal to n.'''
  lstlen = len(lst)
  if lstlen <= 1:
    return 0
  if split_integer(lst[lstlen/2])[0] > n:
    return find_index(lst[:lstlen/2], n)
  else:
    return find_index(lst[lstlen/2:], n) + lstlen/2

def next_link(cur_figures, prev, first_half):
  if len(cur_figures) == 0 and prev == first_half:
    return True
  elif len(cur_figures) == 0 and prev != first_half:
    return False

  # Find the next link
  for figure in cur_figures:
    i = find_index(figure, prev)
    other_figures = [elem for elem in cur_figures if elem != figure]
    while split_integer(figure[i])[0] == prev:
      next = split_integer(figure[i])[1]
      if next_link(other_figures, next, first_half):
        global total
        total += figure[i]
        return True
      i += 1  

  return False

for elem in triangles:
  total = 0
  prev, next = split_integer(elem)
  if next_link(figures, next, prev):
    total += elem
    break

print "Solution:", total
print "Running time:", time.time() - start_time, "s"
