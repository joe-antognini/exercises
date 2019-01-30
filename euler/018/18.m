(* Project Euler *)
(* Problem 18 *)
(* Joe Antognini *)
(* March 11 2013 *)

triangle = Import["18.dat", "Data"];

(* The number of rows *)
nrows = 15;

(* The number of routes *)
nroutes = 2^(nrows - 1);

(* There are not many routes, so we can brute force the search. *)

maxsum = 0;
For[i = 0, i < nroutes, i++,
 (* First translate the number to binary *)
 
 route = IntegerDigits[i, 2, nrows];
 sum = 0;
 k = 1;
 For[j = 1, j <= nrows, j++,
   k += route[[j]];
   sum += triangle[[j, k]];
   ]
  If[sum > maxsum, maxsum = sum;]
 ]

Print[maxsum]
