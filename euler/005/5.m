(* Project Euler *)
(* Problem 5 *)
(* Joe Antognini *)
(* December 14 2012 *)

n = 20;
allFactors = Sort[Flatten[FactorInteger /@ Range[n], 1]];

(* Make sure to memoize *)
Clear[getFactors]
getFactors[n_] := getFactors[n] = Select[allFactors, #[[1]] == n &];
uniqueFactors = DeleteDuplicates[allFactors[[All, 1]]];
factors = 
  DeleteDuplicates[
     Select[allFactors, #[[2]] == Max[getFactors[#[[1]]][[All, 2]]] &]];

answer = Fold[Times, 1, #[[1]]^#[[2]] & /@ factors]
Print[answer]
