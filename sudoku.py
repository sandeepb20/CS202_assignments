# importing necessary libraries and SATsolver
import random
import csv
from pysat.card import *
import sys
import math
from pysat.formula import CNF
from pysat.solvers import Solver, Minisat22

# reading input from the CSV File
file = open("input.csv")
reader = csv.reader(file)
N= len(list(reader))

N = int(N/2)
# D is the size of sudoku
# for D = 3, Sudoku is of 9x9 size
D = int(math.sqrt(N))

if __name__ == '__main__':
    # assigning a dictionary for easy reading in CSV
    digits = {str(x):x for x in range(1,N+1)}
    rows = []
    with open("input.csv",'r') as csvfile:
        # taking input from the CSV
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            row_int=[]
            for element in row:
                row_int.append(int(element))
            rows.append(row_int)

    # allocating variables for the first matrix
    def var(r, c, v):
        assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
        return (r-1)*N*N+(c-1)*N+(v-1)+1

    # allocating variables for the second matrix
    def var2(r, c, v):
        assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
        return (r-1)*N*N+(c-1)*N+(v-1)+1 + D**6

    # initializing CNFs for the two sudokus
    cnf = CNF()
    cnf_2 = CNF()

    # only one element should be present in each cell of sudoku
    for r in range(1,N+1):
        for c in range(1, N+1):
            temp = []
            temp2 = []
            for v in range(1,N+1):
                temp.append(var(r,c,v))
                temp2.append(var2(r,c,v))
            
            cnf.extend(CardEnc.equals(temp,bound=1, encoding=0))
            cnf_2.extend(CardEnc.equals(temp2,bound=1, encoding=0))
    
    # for each column every number should appear exactly once
    for c in range(1, N+1):
        for v in range(1,N+1):
            l1 = []
            q1 = []
            for r in range(1,N+1):
                l1.append(var(r,c,v))
                q1.append(var2(r,c,v))
            
            cnf.extend(CardEnc.equals(l1,bound=1,encoding=0))
            cnf_2.extend(CardEnc.equals(q1,bound=1,encoding=0))

    # for each row every number should appear exactly once
    for r in range(1,N+1):
        for v in range(1,N+1):
            l2 = []
            q2 = []
            for c in range(1,N+1):
                l2.append(var(r,c,v))
                q2.append(var2(r,c,v))
            
            cnf.extend(CardEnc.equals(l2, bound=1, encoding=0))
            cnf_2.extend(CardEnc.equals(q2, bound=1, encoding=0))
    
    # for each sub grid, a number should come exactly once
    for v in range(1,N+1):
        for sr in range(0,D):
            for sc in range(0,D):
                l3 = []
                q3 = []
                for rd in range(1,D+1):
                    for cd in range(1,D+1):
                        l3.append(var(sr*D + rd, sc*D+cd, v))
                        q3.append(var2(sr*D + rd, sc*D+cd, v))
                cnf.extend(CardEnc.equals(l3,bound=1,encoding=0))
                cnf_2.extend(CardEnc.equals(q3,bound=1,encoding=0))

    # encoding the given values in the first sudoku in CNF
    for r in range(1,N+1):
        for c in range(1,N+1):
            if rows[r-1][c-1] > 0:
                l4 = []
                l4.append(var(r,c,int(rows[r-1][c-1])))
                cnf.extend(CardEnc.equals(l4, encoding=0))

    # encoding the given values in the second sudoku in CNF
    for r in range(1,N+1):
        for c in range(1,N+1):
            if rows[r-1+N][c-1] > 0:
                q4 = []
                q4.append(var2(r,c,int(rows[r-1+N][c-1])))
                cnf_2.extend(CardEnc.equals(q4, encoding=0))

    # combining the two CNFs
    cnf.extend(cnf_2)

    # each corresponding cell of the two sudoku must not contain same value
    for r in range(1, N+1):
        for c in range(1,N+1):
            for v in range(1,N+1):
                l5 = []
                l5.append(var(r,c,v))
                l5.append(var2(r,c,v))
                cnf.extend(CardEnc.atmost(l5,bound=1,encoding=0))


    # initiating the Minisat22 solver
    m = Minisat22()
    if (m.append_formula(cnf.clauses,no_return=False)):
        print("True")
        diffSudoku=[]
        for x in m.enum_models():
            diffSudoku+=[x]
            if(len(diffSudoku)>5000):
                break
            sudoku_=random.choice(diffSudoku)
        # placing the obtained model in a list
        sys.stdout = open("new_list.py", "w")
        print("my_list = ", sudoku_)
        sys.stdout.close()
    else:
        print("False")