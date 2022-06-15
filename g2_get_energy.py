import sys
from numpy import *
from ase.data.g2_1 import g2_1, get_interaction_energy_g2_1
EQC = get_interaction_energy_g2_1(g2_1[0])
print ('QC energy', EQC*1000)

