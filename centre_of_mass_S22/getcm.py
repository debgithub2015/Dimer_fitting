from ase import io
from numpy import *
import sys

splitList = [4, 3, 5, 6, 12, 12, 15, 5 , 6, 12, 12, 10,
12, 12, 15, 6, 12, 12, 12, 12, 12, 13]

dist_cm=zeros(22)

f=open("cm_dist.txt","w+")

for i in range(22):
	ref_filename="/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/centre_of_mass_S22/s%i.xyz"%(i+1)
	atoms_ref=io.read(ref_filename)
        split = splitList[i]
  	atoms_ref.center()

	atoms1 = atoms_ref[0:split]
  	atoms2 = atoms_ref[split:]

	print atoms1, atoms2

  	atoms1cm=atoms1.get_center_of_mass()
	atoms2cm=atoms2.get_center_of_mass()

#  print atoms1cm, atoms2cm
	distcm=sqrt(sum((atoms1cm[0]-atoms2cm[0])**2+(atoms1cm[1]-atoms2cm[1])**2+(atoms1cm[2]-atoms2cm[2])**2))
  
#  print distcm  
	dist_cm[i]=distcm
#  print i, dist_cm[i]
  	f.write("%10.10f\r\n"% dist_cm[i])

f.close()
