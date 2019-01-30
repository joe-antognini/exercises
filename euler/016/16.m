(* Project Euler *)
(* Problem 16 *)
(* Joe Antognini *)
(* February 15 2013 *)

sumDigits[n_] := Total[IntegerDigits[2^n]];

(* The answer *)
answer = sumDigits[1000]

Print[answer]
