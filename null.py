import pandas as pd
import numpy as np
k = int(input("Enter the size of sudoku: "))
f = k*k
df = pd.DataFrame(np.zeros((2*f,f), dtype=int))
df.to_csv("input/new-unsolved.csv",index=False,header=False)