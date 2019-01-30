(* Project Euler *)
(* Problem 2 *)
(* Joe Antognini *)
(* December 12 2012 *)

n = 1;
total = 0;
maxn = 4000000;
While[Fibonacci[n] < maxn, 
 If[EvenQ[Fibonacci[n]], total += Fibonacci[n]]; n += 1]
answer = total
Print[answer]
