# importing required libraries
#from numpy import true_divide
from pysat.formula import CNF
import sys
from copy import deepcopy
import time

inputfile = '150_sat'  #

# start timer
start_time = time.time()

# set for maintaining true and false literals
assign_tru = set()
assign_fals = set()


# function to check whether a cnf "l1" consisting of literals "lit" is solvable or not
def solvability(l1, lit):
    tru =[]
    fals = []
    global assign_tru, assign_fals
    assign_tru = set(assign_tru)
    assign_fals = set(assign_fals)

    # storing unit literals in form of a list
    units_ = [i for i in l1 if len(i)==1]
    units = list(set([i for sublist in units_ for i in sublist]))

    # if there exist a unit literal
    if(len(units)):
        for unit in units:
            # if the literal is false
            if unit<0:
                # add it to assign_fals
                assign_fals.add(unit)
                fals.append(abs(unit))
                
                # traversing the cnf clause by clause
                i=0
                while(1):
                    # if the unit literal is present, remove the clause
                    if unit in l1[i]:
                        l1.remove(l1[i])
                        i=i-1
                    # if inverse of unit clause present, remove the literal from that clause
                    elif abs(unit) in l1[i]:
                        l1[i].remove(abs(unit))
                    i = i+1
                    # come out of iteration if the cnf is finishes
                    if i>= len(l1):
                        break
            # unit literal is true
            else:
                # add to assign_tru
                assign_tru.add(unit)
                tru.append(unit)
                
                # traversing the cnf clause by clause
                i = 0
                while(1):
                    # if inverse of unit clause present, remove the literal from that clause
                    if -unit in l1[i]:
                        l1[i].remove(-unit)
                    # if the unit literal is present, remove the clause
                    elif unit in l1[i]:
                        l1.remove(l1[i])
                        i = i-1
                    i = i+1
                    # come out of iteration if the cnf is finishes
                    if i>= len(l1):
                        break
    
    
    # when no clause remain, it means all clauses have been checked and it is SAT
    if len(l1) ==0:
        return True
    
    # if there is a empty list in cnf
    # means cnf is UNSAT
    # clear assign_tru and assign_fals
    if sum(len(clause)==0 for clause in l1):
        for i in tru:
            assign_tru.remove(i)
        for i in fals:
            assign_fals.remove(-i)
        return False
    
    # revised list of literals for new cnf
    lit = list(set([abs(i) for sublist in l1 for i in sublist]))
    
    # 
    first = lit[0]
    
    l1_new_1= deepcopy(l1)
    l1_new_2= deepcopy(l1)
    l1_new_1.append([first])
    l1_new_2.append([-first])

    
    if solvability(l1_new_1, deepcopy(lit)):
        return True
    elif solvability(l1_new_2, deepcopy(lit)):
        return True
    else:
        for i in tru:
            assign_tru.remove(i)
        for i in fals:
            assign_fals.remove(-i)
        return False
    




if __name__=='__main__':
    
    cnf = CNF(from_file='input/'+inputfile+'.cnf')
    l1 = cnf.clauses
    #num_clauses = len(l1)
    
    lit = list(set([abs(i) for sublist in l1 for i in sublist]))
    #num_lit = len(lit)
    
    

    if (solvability(l1, lit)):
        print("SAT")
        
        l_true = list(assign_tru)
        l_false = list(assign_fals)
        
        
        l_true.extend(l_false)
        print("Model: ", sorted(l_true, key=abs))
        print("Time taken : ", time.time()-start_time, "seconds")

        sys.stdout = open("output/output_of_" + inputfile + ".txt", "+w")
        print("SAT")
        print("Model: ", sorted(l_true, key=abs))
        print("Time taken : ", time.time()-start_time, "seconds")
        sys.stdout.close()
        
        
    else:
        print("UNSAT")
        print("Time taken : ", time.time()-start_time, "seconds")
        sys.stdout = open("output/output_of_" + inputfile + ".txt", "+w")
        print("UNSAT")
        print("Time taken : ", time.time()-start_time, "seconds")
        sys.stdout.close()
    