(* Project Euler *)
(* Problem 9 *)
(* Joe Antognini *)
(* December 20, 2012 *)

n = 2000000;
maxN = 1;
While[Prime[maxN] < n, maxN += 1]
maxN -= 1;

answer = Total[Table[Prime[j], {j, maxN}]]
Print[answer]
