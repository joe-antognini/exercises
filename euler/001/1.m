(* Project Euler *)
(* Problem 1 *)
(* Joe Antognini *)
(* December 12 2012 *)

(* The solution *)

divisTotal[n_] := 
  Total[Select[Range[n - 1], Divisible[#, 3] || Divisible[#, 5] &]]

(* Compute the solution. *)
n = 1000
answer = divisTotal[n]
Print[answer]
