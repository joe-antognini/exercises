(* Project Euler *)
(* Problem 9 *)
(* Joe Antognini *)
(* December 20, 2012 *)

n = 1000;
c = Floor[n / 3];
noSolution = True;

While[c < n - 1 && noSolution,
  b = 1;
  c += 1;
  While[b < (n - 1) - c && noSolution,
    b += 1;
    a = n - c - b;
    If[a^2 + b^2 == c^2,
      noSolution = False;
      solution = {a, b, c};];
    ];
];

Print[a b c]
