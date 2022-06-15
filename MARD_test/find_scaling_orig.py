import pandas as pd
import numpy as np
from scipy import optimize
df = pd.read_excel('Zval_test2.xlsx')

Zvals = df.keys()

values = np.transpose(df.as_matrix())
ref = values[25]
filter_no_spin = values[26] >0# >0 all but spin, ==1 only noble atoms

filter_noble = values[26] == 1
no_filter = values[26]*0 + 1

filter_selected = filter_no_spin


N = len(ref)


def MARD(data, ref):
    return np.sum(np.abs((data - ref)/ref))/N


def MARD_filter(data, ref, filter):
    Nf = sum(filter)
    return np.sum(np.abs(filter*((data - ref)/ref)))/Nf


def find_factor(data, ref, guess=1.0):
    def f(s):
        return MARD_filter(data*s, ref, filter_selected)
    scale = optimize.fmin(f, guess)[0]
    mard = MARD(data*scale, ref)
    mard_filter = MARD_filter(data*scale, ref, filter_selected)
    return scale, mard, mard_filter

for i in range(25):
    scale, mard, mard_filter = find_factor(values[i],ref)
    print(Zvals[i], scale, mard, mard_filter)
