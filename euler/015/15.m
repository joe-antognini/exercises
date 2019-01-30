(* Project Euler *)
(* Problem 15 *)
(* Joe Antognini *)
(* February 11 2013 *)

(* The function.  Each path can be represented by a series of 0's and 1's, a
0 representing a move down and a 1 representing a move right.  For an n x n
grid 2n moves are required -- n moves down and n moves right.  Each path is
therefore a sequence of n 0's and n 1's.  The number of unique paths is the
number of permutations of a list of n 0's and n 1's. *)
calcPaths[n_] := (2 n)!/(n!)^2;

(* Test case. *)
calcPaths[2]

(* The answer. *)
answer = calcPaths[20]

Print[answer]
