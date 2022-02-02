#!/usr/bin/python3
import random
import csv
from pysat.card import *
import sys
import math
from pysat.formula import CNF
from pysat.solvers import Solver, Minisat22
import numpy as np
import pandas as pd
import time

start_time = time.time()
# taking input
input_csv_file = "output/output_of_new-unsolved.csv"

# rows of csv file
file = open(input_csv_file)
reader = csv.reader(file)
N = len(list(reader))
N = int(N/2)
D = int(math.sqrt(N))

# assigning a dictionary for easy reading in CSV
digits = {str(x):x for x in range(1,N+1)}
rows = []
with open(input_csv_file,'r') as csvfile:
    # reading csv file
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        row_int=[]
        for element in row:
            row_int.append(int(element))
        rows.append(row_int)

if __name__ == '__main__':
    def var(r, c, v):
        # allocating variables for the first matrix
        assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
        return (r-1)*N*N+(c-1)*N+(v-1)+1

    def var2(r, c, v):
        # allocating variables for the second matrix
        assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
        return (r-1)*N*N+(c-1)*N+(v-1)+1 + D**6
    # initializing CNF for the two sudokus
    cnf = CNF()
    # --------check conditions of a valid input ---------
    # only one element should be present in each cell of sudoku
    for r in range(1,N+1):
        for c in range(1, N+1):
            temp = []
            temp2 = []
            for v in range(1,N+1):
                temp.append(var(r,c,v))
                temp2.append(var2(r,c,v))
            
            cnf.extend(CardEnc.equals(temp,bound=1, encoding=0))
            cnf.extend(CardEnc.equals(temp2,bound=1, encoding=0))
    # for each column every number should appear exactly once
    for c in range(1, N+1):
        for v in range(1,N+1):
            l1 = []
            q1 = []
            for r in range(1,N+1):
                l1.append(var(r,c,v))
                q1.append(var2(r,c,v))
            
            cnf.extend(CardEnc.equals(l1,bound=1,encoding=0))
            cnf.extend(CardEnc.equals(q1,bound=1,encoding=0))
    # for each row every number should appear exactly once
    for r in range(1,N+1):
        for v in range(1,N+1):
            l2 = []
            q2 = []
            for c in range(1,N+1):
                l2.append(var(r,c,v))
                q2.append(var2(r,c,v))
            
            cnf.extend(CardEnc.equals(l2, bound=1, encoding=0))
            cnf.extend(CardEnc.equals(q2, bound=1, encoding=0))
    
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
                cnf.extend(CardEnc.equals(q3,bound=1,encoding=0))

    # encoding the given values in the first sudoku in CNF
    for r in range(1, N+1):
        for c in range(1,N+1):
            for v in range(1,N+1):
                l5 = []
                l5.append(var(r,c,v))
                l5.append(var2(r,c,v))
                cnf.extend(CardEnc.atmost(l5,bound=1,encoding=0))
    #------------------------------------------------------------            


    flag = True
    itr = 0
    # creating a list of cells, from which entries will be removed
    test_list = []
    for i in range(1,2*N+1):
        for j in range(1,N+1):
            test_list.append([i,j])
    #randomising the selected cell        
    random.shuffle(test_list)


    for r in range(1,N+1):
        for c in range(1,N+1):
            # if there is an entry in first sudoku
            if rows[r-1][c-1] > 0:
                l4 = []
                l4.append(var(r,c,int(rows[r-1][c-1])))
                cnf.extend(CardEnc.equals(l4, encoding=0))
            # if there is an entry in second sudoku
            if rows[r-1+N][c-1] > 0:
                q4 = []
                q4.append(var2(r,c,int(rows[r-1+N][c-1])))
                cnf.extend(CardEnc.equals(q4, encoding=0))

    # implementing binary search to find maximum number of holes
    # min_index will start from zero and max_index will point to
    # the last entry in test_list
    # min_index, i.e., no. of zeros will increase till a point where
    # a valid solution exist           
    min_index = 0
    max_index = len(test_list)-1
    while(max_index - min_index > 1):
        # created a copy of CNF
        cnf2 = cnf.copy()
        check = True


        # finding a mid_index
        # no. of holes will be created till mid_index
        # check whether it is a valid sudoku
        
        mid_index = int((max_index+min_index)/2)
        for k in range(mid_index):
            random_r = test_list[k][0]
            random_c = test_list[k][1]
            if random_r <= N:
                temp = var(random_r,random_c,int(rows[random_r-1][random_c-1]))
            else:
                temp = var2(random_r-N,random_c,int(rows[random_r-1][random_c-1]))   
            cnf2.clauses.remove([temp])  
        # check satisfiability
        s = Minisat22()
        s.append_formula(cnf2.clauses,no_return=False)
        count = 0
        for x in s.enum_models():
            count += 1
            if(count>1):
                # check if multiple solution exist
                check = False
                break
        if check == True:
            # if single solution exist -> increase min_index
            min_index = mid_index
        else:
            # if multiple solution exist -> decrease max_index to mid_index
            max_index = mid_index

    # creating holes
    for i in range(mid_index):
        random_r = test_list[i][0]
        random_c = test_list[i][1]
        rows[random_r-1][random_c-1] = 0
       
                
# printing in the terminal
    for i in range(N):
        print(rows[i])
    print("****")
    for i in range(N):
        print(rows[i+N])
    print("No of Holes = ",min_index)

# save in csv file name="output.csv"
    df = pd.DataFrame(np.array(rows))
    output_file_name = "output.csv"
    df.to_csv(output_file_name,index=False,header=False)
print("--- %s seconds ---" % (time.time() - start_time))