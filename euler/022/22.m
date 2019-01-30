(* Project Euler *)
(* Problem 22 *)
(* Joe Antognini *)
(* July 2, 2013 *)

(* First import the data. *)
names = Import["22.txt", "Text"]
names = StringSplit[names, ","];
names = StringDrop[#, -1] & /@ (StringDrop[#, 1] & /@ names);

(* Now sort the list. *)
names = Sort[names];

(* The ASCII number for A is 65, so everything needs to have 64 subtracted
from it. *)
capAVal = 64;
nameVal[str_] := Total[(#-capAVal) & /@ ToCharacterCode[str]]

ans = 0;
For[i=1, i<=Length[names], i++,
  ans += i * nameVal[names[[i]]];
]

Print[ans]
