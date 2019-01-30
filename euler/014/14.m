(* Project Euler *)
(* Problem 14 *)
(* Joe Antognini *)
(* December 24, 2012 *)

(* We're using recursion to solve this problem, so this is necessary. *)
$RecursionLimit = 10^6;

Clear[collatz]
collatz[1] = 1;
collatz[n_] := collatz[n] = 1 + If[EvenQ[n], collatz[n / 2],
  collatz[3n + 1]]

maxn = 10^6;
answer = Ordering[Table[collatz[n], {n, maxn}], -1][[1]]
Print[answer]
