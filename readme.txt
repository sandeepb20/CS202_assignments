------------------- Sudoku Pair Solver and Generator -------------------

Question 1:
Problem Statement:
Given a sudoku pair in a CSV File, of size D (D = 3 means 9x9 Sudoku), we
are required to solve them, such that no two corresponding cells of them
does not contain the same value.

We will use Minisat22 Solver for solving the sudoku-pair using CNF encoding.
CardEnc will be used to create clauses for different conditions.

sudoku.py contains the code to solve the sudoku problems in the input folder.
"input" folder contains some test cases, named <size>-unsolved.csv, where
size ={2,3,4,5,6} which are non zero sudoku. There are some empty sudokus too,
named <size>-unsolved0.csv . If tester wants to check for any random sudoku,
he/she can put that sudoku in new-unsolved.csv. The output will be shown on
terminal as well as in a csv file in the folder "output", which is named
accordingly, i.e., for new-unsolved.csv, output file is new-solved.csv.

How test a file:
1. Go to sudoku.py
2. in line 15:  write the name of input file.
   like for new-unsolved.csv, line would be
   input_csv_file = "new-unsolved.csv"
3. to generate unique sudoku at each execution,
   in line 19:  generate_random_sudoku must set to True
   if set False, it will throw the same sudoku
   (for an empty sudoku)
4. output would be shown in the terminal and a csv will
   be updated corresponding to the input file.
5. Terminal will give True and print the sudoku if
   solution exist, else it gives False. Along with
   execution time


Example 1:

line 15: input_csv_file = "3-unsolved.csv"
line 19: generate_random_sudoku = True

0,0,0,0,0,0,0,0,0
0,2,1,8,9,0,4,0,0
0,4,0,2,5,0,9,7,6
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,6,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,9,8,5,6,0,3,2,1
0,9,0,0,8,0,0,7,6
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,4,0,3,1,8,7,9,0
0,0,0,0,0,0,0,0,2
0,0,0,0,0,0,0,3,0
0,5,3,4,0,0,9,8,7
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0

command:
python3 sudoku.py

output:

True
Sudoku 1
[[9 5 7 6 4 3 8 1 2]
 [6 2 1 8 9 7 4 5 3]
 [8 4 3 2 5 1 9 7 6]
 [1 6 5 7 8 9 2 3 4]
 [3 7 9 4 2 6 1 8 5]
 [4 8 2 1 3 5 6 9 7]
 [5 3 6 9 1 2 7 4 8]
 [2 1 4 3 7 8 5 6 9]
 [7 9 8 5 6 4 3 2 1]]
 *******************
Sudoku 2
[[4 9 2 1 8 5 3 7 6]
 [3 1 8 2 7 6 5 4 9]
 [5 6 7 9 3 4 1 2 8]
 [2 4 6 3 1 8 7 9 5]
 [1 3 5 7 4 9 8 6 2]
 [8 7 9 5 6 2 4 3 1]
 [6 5 3 4 2 1 9 8 7]
 [7 2 1 8 9 3 6 5 4]
 [9 8 4 6 5 7 2 1 3]]
--- 0.05856180191040039 seconds ---

command: 
python3 sudoku.py

output:

True
Sudoku 1
[[5 7 9 6 4 3 1 8 2]
 [6 2 1 8 9 7 4 3 5]
 [8 4 3 2 5 1 9 7 6]
 [9 5 2 4 7 6 8 1 3]
 [4 1 6 9 3 8 2 5 7]
 [3 8 7 1 2 5 6 9 4]
 [2 6 5 3 1 9 7 4 8]
 [1 3 4 7 8 2 5 6 9]
 [7 9 8 5 6 4 3 2 1]]
 *******************
Sudoku 2
[[4 9 1 2 8 5 3 7 6]
 [7 6 8 1 3 4 2 5 9]
 [5 3 2 9 6 7 8 4 1]
 [2 4 6 3 1 8 7 9 5]
 [3 8 7 5 4 9 6 1 2]
 [9 1 5 6 7 2 4 3 8]
 [1 5 3 4 2 6 9 8 7]
 [6 7 9 8 5 3 1 2 4]
 [8 2 4 7 9 1 5 6 3]]
--- 0.0445711612701416 seconds ---

so, here we got multiple answers.

Example 2:

input_csv_file = "new-unsolved.csv"

1,0,0,0
0,0,0,0
0,0,0,0
0,0,0,0
1,0,0,0
0,0,0,0
0,0,0,0
0,0,0,0

commands:
python3 sudoku.py

output :

False
--- 0.004499912261962891 seconds ---


Question2:
Problem Statement:
We are required to generate a sudoku pair.

We will give an empty sudoku of size K to the solver sudoku.py, which will
generate a filled sudoku out of it. Which again will be given to gen.py to
create maximum holes till a solution exist. Following these steps we will
get our sudoku pair.

We will use Minisat22 Solver for solving the sudoku-pair using CNF encoding.
CardEnc will be used to create clauses for different conditions.

Steps:
1. At first, we will generate an empty sudoku of size K, (say k=4), using
   "null.py"

   command:
   python3 null.py

   output:
   Enter the size of sudoku: 

   now enter the size of sudoku
   command:
   4

2. now a matrix of two sudokus is created of size 2*K*K X K*K (2*16 X 16)
   at "input/new-unsolved.csv"

3.  now we will solve this matrix using "sudoku.py"
    Note: "new-unsolved" must be written in line 15 of "sudoku.py"

    command:
    python3 sudoku.py

    output:
    <will output as shown in question 1>
    "output/output_of_new-unsolved.csv" will be created

4. Now run gen.py
   command:
   python3 gen.py

   output:

[3, 0, 4, 15, 0, 8, 0, 0, 0, 6, 0, 0, 10, 7, 2, 0]
[0, 9, 0, 0, 0, 12, 13, 0, 14, 7, 4, 15, 11, 1, 16, 3]
[12, 11, 0, 0, 5, 0, 16, 7, 0, 3, 10, 0, 14, 13, 0, 4]
[0, 7, 16, 14, 0, 2, 4, 3, 0, 0, 0, 11, 5, 12, 6, 15]
[15, 4, 0, 0, 2, 1, 6, 8, 0, 0, 7, 14, 13, 0, 12, 0]
[1, 0, 11, 0, 7, 5, 3, 0, 0, 15, 0, 12, 6, 0, 0, 0]
[7, 6, 0, 9, 12, 10, 0, 4, 0, 13, 11, 8, 16, 5, 3, 0]
[0, 0, 0, 0, 16, 11, 14, 9, 4, 5, 3, 6, 0, 15, 1, 0]
[5, 12, 0, 16, 0, 0, 10, 15, 6, 11, 0, 0, 4, 0, 14, 8]
[6, 0, 15, 11, 8, 0, 0, 16, 0, 4, 0, 13, 12, 10, 9, 5]
[0, 0, 0, 0, 0, 4, 9, 0, 12, 0, 15, 5, 3, 16, 7, 0]
[0, 2, 0, 7, 0, 0, 5, 0, 0, 0, 16, 10, 1, 11, 0, 13]
[14, 3, 10, 2, 0, 9, 0, 0, 15, 0, 6, 0, 7, 8, 0, 12]
[0, 0, 6, 0, 0, 0, 0, 1, 0, 12, 0, 0, 0, 0, 10, 14]
[9, 15, 0, 0, 14, 0, 0, 0, 11, 8, 13, 4, 0, 3, 5, 0]
[16, 5, 12, 0, 3, 0, 8, 0, 0, 14, 9, 0, 0, 0, 0, 0]
****
[0, 0, 0, 0, 10, 6, 16, 0, 4, 0, 0, 2, 13, 0, 0, 12]
[15, 13, 0, 10, 0, 14, 0, 5, 9, 8, 3, 0, 2, 0, 4, 0]
[1, 5, 12, 0, 0, 4, 3, 13, 0, 15, 14, 11, 0, 0, 0, 0]
[0, 2, 0, 6, 11, 9, 15, 8, 0, 10, 0, 13, 7, 0, 14, 0]
[3, 16, 8, 4, 1, 5, 9, 6, 0, 12, 0, 10, 14, 13, 0, 0]
[0, 0, 5, 14, 0, 10, 2, 11, 0, 13, 7, 0, 1, 4, 12, 0]
[11, 9, 1, 2, 0, 0, 12, 15, 0, 0, 0, 0, 10, 16, 0, 3]
[12, 0, 10, 13, 14, 16, 0, 3, 15, 1, 9, 5, 0, 8, 0, 2]
[0, 0, 13, 3, 6, 8, 0, 14, 0, 0, 12, 4, 15, 9, 10, 7]
[7, 4, 0, 8, 0, 12, 10, 0, 0, 14, 0, 16, 5, 0, 1, 11]
[14, 0, 0, 0, 16, 15, 0, 0, 10, 9, 0, 0, 4, 12, 3, 0]
[10, 0, 9, 15, 3, 2, 11, 0, 13, 5, 1, 0, 0, 6, 8, 14]
[0, 14, 4, 0, 0, 0, 8, 12, 1, 11, 13, 0, 3, 15, 6, 10]
[8, 3, 0, 0, 9, 0, 6, 0, 14, 16, 10, 15, 0, 5, 0, 0]
[0, 0, 11, 0, 0, 3, 14, 0, 5, 0, 6, 12, 8, 7, 0, 1]
[5, 6, 15, 1, 0, 11, 0, 10, 0, 3, 2, 0, 12, 14, 0, 16]
No of Holes =  203
--- 8.98530888557434 seconds --- 

   this will be saved as a csv file in "output.csv"
And a sudoku pair is generated.
