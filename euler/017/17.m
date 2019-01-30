(* Project Euler *)
(* Problem 17 *)
(* Joe Antognini *)
(* February 19 2013 *)

(* Define some letter counts.  First do the numbers 1-9 *)

numLengthsLstOne = {{0, 0}, {1, 3}, {2, 3}, {3, 5}, {4, 4}, {5, 
    4}, {6, 3}, {7, 5}, {8, 5}, {9, 4}};

(* Now do the tens 10-90 *)

numLengthsLstTen = {{0, 0}, {2, 6}, {3, 6}, {4, 5}, {5, 5}, 
  {6, 5}, {7, 7}, {8, 6}, {9, 6}};

(* We have to do the teens separately.  Everything else can be built 
   up from the ones and tens. *)

teens = {{{1, 0}, 3}, {{1, 1}, 6}, {{1, 2}, 6}, {{1, 3}, 8}, 
  {{1, 4}, 8}, {{1, 5}, 7}, {{1, 6}, 7}, {{1, 7}, 9}, {{1, 8}, 8}, 
  {{1, 9}, 8}};

(* Turn the above lists into functions. *)
(numLengthOne[#[[1]]] = #[[
      2]]) & /@ numLengthsLstOne;
(numLengthTen[#[[1]]] = #[[2]]) & /@ numLengthsLstTen;
(numLengthTeens[#[[1]]] = #[[2]]) & /@ teens;

(* Now we work backwards.  Count the letters in a single digit 
   number, two digit number, etc. *)

spellOutOnes[lst_] := numLengthOne[lst[[1]]];

(* Account for the edge case of the teens. *)

spellOutTen[lst_] := 
  If[lst[[1]] != 1 && lst[[1]] != 0, 
   numLengthTen[lst[[1]]] + spellOutOnes[lst[[2 ;;]]], 
   If[lst[[1]] == 1, numLengthTeens[lst], 
    spellOutOnes[lst[[2 ;;]]]]];
(* Account for the edge case of a number divisible by 100 -- no 
   'and' *)
spellOutHundred[lst_] := 
  If[lst[[2]] != 0 || lst[[3]] != 0, 
   numLengthOne[lst[[1]]] + spellOutTen[lst[[2 ;;]]] + 10, 
   numLengthOne[lst[[1]]] + 7];

(* Determine how many digits the number has and choose the 
   appropriate function. *)

spellOut[lst_] := 
 If[Length[lst] == 4, 11, 
  If[Length[lst] == 3, spellOutHundred[lst], 
   If[Length[lst] == 2, spellOutTen[lst], 
    If[Length[lst] == 1, spellOutOnes[lst]]]]]

(* This is the function that puts it all together.  Split each number 
   up, count the letters, and take the sum. *)

numLetterCount[n_] := 
  Total[(spellOut[IntegerDigits[#]]) & /@ Range[n]];

(* The answer *)
answer = numLetterCount[1000]

Print[answer]
