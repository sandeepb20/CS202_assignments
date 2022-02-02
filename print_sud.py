# importing useful libraries
from new_list import my_list
import numpy as np
import csv
from sudoku import N

# Selecting the positive literals in the list which sudoku.py outputed
lis = []
for x in my_list:
    if x>0:
        if(x%N==0):
            lis.append(N)
        else:
            lis.append(x%N)

# splitting the list into two lists for the two sudokus
list1 = []
list2 = []

for i in range(N*N):
    list1.append(lis[i])

for i in range(N*N):
    list2.append(lis[i+N*N])

# first sudoku
print(np.array(list1).reshape(N,N))
print(" *******************")
# second sudoku
print(np.array(list2).reshape(N,N))