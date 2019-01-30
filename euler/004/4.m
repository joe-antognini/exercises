(* Project Euler *)
(* Problem 4 *)
(* Joe Antognini *)
(* December 13 2012 *)

palindromeQ[n_] := 
  IntegerString[n] == StringReverse[IntegerString[n]];

products = Flatten[Table[i j, {i, 100, 999}, {j, i, 999}]];
answer = Max[Select[products, palindromeQ[#] &]]

Print[answer]
