(* Project Euler *)
(* Problem 3 *)
(* Joe Antognini *)
(* December 13 2012 *)

(* Solve the problem. *)
TimeConstrained[
 answer = Max[FactorInteger[600851475143][[All, 1]]], 60]

Print[answer]
