import sys
from numpy import *

Ryd = 13.6057*1000

for Num in range(1,23):
  Eval = zeros(35)
  ErefA = 0
  ErefB = 0
  nonloc = zeros(35)
  nonlocA = 0
  nonlocB = 0
  C6val = zeros(37)
  C6refA = 0
  C6refB = 0
  lines = 0
  sep_list=zeros(35)  
 
  for i in range(35):
#   print "System%i/S22_%02d_%02d.txt"%(Num,Num,i)
     file = open("System%i/S22_%02d_%02d.txt"%(Num,Num,i))
     content = file.readlines()
     file.close()
     for line in content:
	if '!' in line:
		val=float(line.split()[-2])
		Eval[i] = val
	
	if 'Non-local corr. energy' in line:
		lines = float(line.split()[-2])
	y = lines

     nonloc[i]=y

     for line in content:
	if 'C6 coefficient' in line:
		lines = float(line.split()[-1])
	x = lines

     C6val[i]=x

  file= open("../cm_dist_our_script/dist_cm_S%i.txt"%(Num))
  content=file.readlines()
  file.close()
  lines=0
  for line in content:
       	val = float(line.split()[0])
        listnum=lines
        lines +=1
#        print listnum, val
        sep_list[listnum]=val
#    
#  print sep_list


  imin = Eval.argmin()
  file = open("System%i/S22_%02d_00_RefA.txt"%(Num,Num))
  content = file.readlines()
  file.close()
  for line in content:
    if '!' in line:
       ErefA = float(line.split()[-2])
    if 'Non-local corr. energy' in line:
 	lines = float(line.split()[-2])
    y = lines

  nonlocA=y
  for line in content:
    if 'C6 coefficient' in line:
       lines = float(line.split()[-1])
    x = lines
  C6refA = x
  C6val[35]=C6refA
  file = open("System%i/S22_%02d_00_RefB.txt"%(Num,Num))
  content = file.readlines()
  file.close()
  for line in content:
    if '!' in line:
       ErefB = float(line.split()[-2])
    if 'Non-local corr. energy' in line:
 	lines = float(line.split()[-2])
    y = lines

  nonlocB=y
  for line in content:
    if 'C6 coefficient' in line:
       lines = float(line.split()[-1])
    x = lines
  C6refB = x
  C6val[36]=C6refB
       
  savetxt('C6_%i.txt'%Num,C6val )
  savetxt('NLC_%i.txt'%Num,nonloc - nonlocA-nonlocB )

  

#  savetxt('PEC_%i-b86R.txt'%Num,Eval - ErefA-ErefB )
#  sep_list = [-0.8, -0.4,-0.3,  -0.2, -0.15, -0.1, -0.05, -0.025, 0.0, 0.025,0.05, 0.075, 0.1, 0.125,  0.15, 0.175,  0.2, 0.225, 0.25,0.275, 0.3, 0.325,0.35,0.375, 0.4,0.45,0.5,0.6,0.65, 0.7, 1.0,  1.5,  2.0,   3.0, 5.0]
  savetxt('PEC_%i.txt'%Num,Eval - ErefA-ErefB )
  #print transpose(sep_list),'\t',Eval - ErefA-ErefB
  print Num,'\t',sep_list[imin],'\t', (Eval[imin] - ErefA-ErefB )*Ryd,'\t', (nonloc[imin] - nonlocA-nonlocB )*Ryd,'\t',C6val[imin]
  Epred =  (Eval[imin] - ErefA- ErefB )*Ryd
 # print Epred
#  from ase.data.s22 import s22, get_interaction_energy_s22
#  EQC = get_interaction_energy_s22(s22[Num-1])
#  print 'QC energy', EQC*1000
#  print (Epred-EQC)/EQC

