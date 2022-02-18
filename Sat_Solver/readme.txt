--------------------------- SAT Solver  ----------------------------
by:
Sandeep Kumar Bijarnia 200856
Kuldeep Singh Chouhan 200530

Problem Satement:
Implement a SAT solver. Given a formula in the DIMACS representation,
your implementation should return:

1) a model if the formula is satisfiable
2) report that the formula is unsatisfiable

_______________________

----Theory----

To create a SAT solver, we will use the DPLL Algorithm, which is a
complete, bcktracking-based search algorithm for deciding whether a
CNF is satisfiable (SAT) or not (UNSAT)
So, the algorithm first searches unit clauses in the CNF and as CNF
is AND of ORs, so unit clauses has to be true. Then it removes clauses,
which have that literal in them. Because a clause connected by ORs is
true if one of them is true.
If negation of the literal is present then, it removes that literal
from the clause, as now the clause will be true only if other literals
would be true.
If there are no unit literals, then it selects, the most frequent
literal and assigns it to be true. If that works, algorithm continues
else it comes back and assign it false.
Such a way a list of true and false assigned literal is maintained and
thus model can be obtained. If each time it came back, then it is UNSAT.

----- Zip Contains -----
sat.py is the solver created by this approach.
The input and output folder contains the test cases and their respective
answers. For running a desired input file, one needs to type the name of
the file (without extension) in line # 6 in sat.py. Output for the same will
be created in output folder with name "output_of_<name of the file>.txt"
and also at the terminal. If user wants to give his own input he can do it
by writing CNF in "test.cnf".

------Output-----
For a satisfiable CNF output would be:
SAT
Model: <one of the possible model>

For an unsatisfiable CNF output would be:
UNSAT


Example 1:
we will check "20_sat_4.cnf"
1)  In line# 6 write "20_sat_4"
    it will look like--->  inputfile = '20_sat_4'
2)  Now on terminal write:
    $ python3 sat.py
3)  "output_of_20_sat_4.txt" will be created, with desired output.
    It will also appear on the terminal.
    >>SAT
    >>Model:  [1, -2, 3, 4, -5, -6, 7, -8, -9, 10, 11, -12, 13, -14, -15, 16, 17, -18, -19, -20]
    >>Time taken :  0.004519462585449219 seconds

Example 2:
we will check "50_unsat_2.cnf"
1)  In line# 6 write "50_unsat_2"
    it will look like--->  inputfile = '50_unsat_2'
2)  Now on terminal write:
    $ python3 sat.py
3)  "output_of_50_unsat_2.txt" will be created, with desired output.
    It will also appear on the terminal.
    >>UNSAT
    >>Time taken :  0.6938498020172119 seconds

Assumptions:
There are no as such assumptions for running of this code.
Only requirement is CNF should be in right format.

Limitations:
If there are no frequent literals, in the CNF, then the code will take
a longer time, because of the way it is written, it searches for a unit
clause to be assigned true/ false. But if the literals appear almost in
equal frequency, it would do a search, which would be expensive and hence
will take a longer time. As observed in the case of "150_unsat_1.cnf".