import sys
import numpy as np
from scipy import optimize
	
C6eval=[ ] 
C6expt=[ ]
with open ("test.txt") as f:
    content = f.readlines()
#    print content
    for line in content: 
        C6eval.append(float(line.split()[0]))
        C6expt.append(float(line.split()[1]))
    print C6eval, C6expt

    N= len(C6eval)
 
def MARD(factor):
   return np.sum(np.abs((factor*C6eval[1:]-C6expt[1:])/C6expt[1:]))/N

factor=optimize.fsolve(MARD,1.5)


