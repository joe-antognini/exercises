#! /usr/bin/env python

#
# Project Euler
# Problem 9
#
# Joe Antognini
# December 21, 2012
#

n = 1000
c = n / 3
no_solution = True

while c < n - 1 and no_solution:
  b = 2
  c += 1
  while b < (n - 1) - c and no_solution:
    a = n - b - c
    if a * a + b * b == c * c:
      solution = (a, b, c)
      no_solution = False
    b += 1

if not no_solution:
  print reduce(lambda x, y: x * y, solution)
else:
  print "no solution found"
