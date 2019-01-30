#! /usr/bin/env python

def distinct_powers(n):
  '''Find the number of distinct powers for all combinations of

  2 <= a, b <= n

  of a^b.  Note that this is a brute force method --- there are far more
  elegant ways to do this problem.
  '''

  ret = []
  for a in range(2, n+1):
    for b in range(2, n+1):
      if a**b not in ret:
        ret.append(a**b)

  return len(ret)

if __name__ == '__main__':
  print distinct_powers(100)
