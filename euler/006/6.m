(* Project Euler *)
(* Problem 6 *)
(* Joe Antognini *)
(* December 19, 2012 *)

n = 100;
sumSquare = Total[(#^2) & /@ Range[n]];
squareSum = Total[Range[n]]^2;

Print[squareSum - sumSquare]
