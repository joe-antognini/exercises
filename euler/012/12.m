(* Project Euler     *)
(* Problem 12        *)
(* Joe Antognini     *)
(* December 22, 2012 *)

n = 1;
While[Length[Divisors[n * (n - 1) / 2]] <= 500,
  n++;
]
Print[n * (n-1) / 2]
