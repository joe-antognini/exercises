#! /usr/bin/env python

import sudoku
import sys
import numpy as np
from sudoku import Board

problems = np.genfromtxt('p096_sudoku.txt', comments='G', dtype=str)
problems = np.split(problems, 50)

token = 0
for i, problem in enumerate(problems):
  nums = map(lambda x: map(int, list(x)), problem)
  board = Board(np.array(nums))
  boards = [board]

  print "Solving board", i
  try:
    sudoku.solve(boards)
  except IndexError:
    "Board", i, "has no solution!"
    sys.exit(1)

  solved_board = boards[-1]
  token += int(''.join(map(str, solved_board[0][:3])))

print
print "Solution:", token
