#!/usr/bin/python3
import random
import csv
from pysat.card import *
import sys
import math
from pysat.formula import CNF
from pysat.solvers import Solver, Minisat22
import numpy as np

file = open("sudoku.csv")
reader = csv.reader(file)
N = len(list(reader))
N = int(N/2)
D = int(math.sqrt(N))


digits = {str(x):x for x in range(1,N+1)}
rows = []
with open("sudoku.csv",'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        row_int=[]
        for element in row:
            row_int.append(int(element))
        rows.append(row_int)
def var(r, c, v):
    assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
    return (r-1)*N*N+(c-1)*N+(v-1)+1
def var2(r, c, v):
    assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
    return (r-1)*N*N+(c-1)*N+(v-1)+1 + D**6
def check_solution(rows):
    cnf = CNF()
    cnf_2 = CNF()
    for r in range(1,N+1):
        for c in range(1, N+1):
            temp = []
            temp2 = []
            for v in range(1,N+1):
                temp.append(var(r,c,v))
                temp2.append(var2(r,c,v))
            cnf.extend(CardEnc.equals(temp,bound=1, encoding=0))
            cnf_2.extend(CardEnc.equals(temp2,bound=1, encoding=0))
    for c in range(1, N+1):
        for v in range(1,N+1):
            l1 = []
            q1 = []
            for r in range(1,N+1):
                l1.append(var(r,c,v))
                q1.append(var2(r,c,v))
            cnf.extend(CardEnc.equals(l1,bound=1,encoding=0))
            cnf_2.extend(CardEnc.equals(q1,bound=1,encoding=0))
    for r in range(1,N+1):
        for v in range(1,N+1):
            l2 = []
            q2 = []
            for c in range(1,N+1):
                l2.append(var(r,c,v))
                q2.append(var2(r,c,v))
            cnf.extend(CardEnc.equals(l2, bound=1, encoding=0))
            cnf_2.extend(CardEnc.equals(q2, bound=1, encoding=0))
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
    for r in range(1,N+1):
        for c in range(1,N+1):
            if rows[r-1][c-1] > 0:
                l4 = []
                l4.append(var(r,c,int(rows[r-1][c-1])))
                cnf.extend(CardEnc.equals(l4, encoding=0))
    for r in range(1,N+1):
        for c in range(1,N+1):
            if rows[r-1+N][c-1] > 0:
                q4 = []
                q4.append(var2(r,c,int(rows[r-1+N][c-1])))
                cnf_2.extend(CardEnc.equals(q4, encoding=0))
    cnf.extend(cnf_2)
    for r in range(1, N+1):
        for c in range(1,N+1):
            for v in range(1,N+1):
                l5 = []
                l5.append(var(r,c,v))
                l5.append(var2(r,c,v))
                cnf.extend(CardEnc.atmost(l5,bound=1,encoding=0))
    
    with Minisat22(bootstrap_with=cnf.clauses) as m:
        return m.solve()


flag = True
itr = 0
while(flag):

    random_r = random.randint(1,len(rows)) - 1
    random_c = random.randint(1,len(rows[0])) - 1


    if rows[random_r][random_c] != 0 :
        value = rows[random_r][random_c]
        for t in range(1,N+1):
            if t!= value:
                rows[random_r][random_c] = t
                if check_solution(rows) == True:
                    print("yes")
                    print(value)
                    rows[random_r][random_c] = value
                    flag = False
                    break
        if flag == True:
            rows[random_r][random_c]=0
            itr = itr+1

print("No of holes = ", itr)
for i in range(N):
    print(rows[i])
print("************")
for i in range(N):
    print(rows[i+N])
    
    
    