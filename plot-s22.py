import numpy as np
import pylab as pl

Ryd = 13.6057*1000
#sep_list = np.array([-0.8, -0.4,-0.3,  -0.2, -0.15, -0.1, -0.05, -0.025, 0.0, 0.025,0.05, 0.075, 0.1, 0.125,  0.15, 0.175,  0.2, 0.225, 0.25,0.275, 0.3, 0.325,0.35,0.375, 0.4,0.45,0.5,0.6,0.65, 0.7, 1.0,  1.5,  2.0,   3.0, 5.0])

for Num in range(1,23):
	Es= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-vdW-df-rutgers/PEC_%i.txt"%(Num))
	Es2= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-vdW-df2-rutgers/PEC_%i.txt"%(Num))
	Es3= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-rvv10-rutgers/PEC_%i.txt"%(Num))
	Es4= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-vdW-df-cx-rutgers/PEC_%i.txt"%(Num))
	Es5= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-optb88-rutgers/PEC_%i.txt"%(Num))
	Es6= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-rev-vdW-df2-rutgers/PEC_%i.txt"%(Num))
	Es7= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/S22-DF3-2.3253-6.8-rutgers/PEC_%i-b86R.txt"%(Num))
        Es8= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/QC_data/QC_S%i_energy.txt"%(Num))
	Es9= np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/QC_s22x5_data/QC_S%i-s22x5_energy.txt"%(Num)) 
	pl.ylabel('binding energy (in meV)')
	pl.xlabel('center_of_mass separation')
#	pl.plot(sep_list,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
#	pl.plot(sep_list,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
#	pl.plot(sep_list,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
#	pl.plot(sep_list,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
#	pl.plot(sep_list,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
#	pl.plot(sep_list,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
#	pl.plot(sep_list,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
#	if Num!=7 and Num!=15 : 
#		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
#        pl.title("S22-%i"%(Num))
        if Num==1 :
	        eqdist=3.2085775286
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.5,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-136.31,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -150, 10])
        if Num==2 :
                eqdist=2.9089819292
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.0,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-215.86,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -250, 10])
        if Num==3 :
                eqdist=2.9925896853
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*1.7,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-808.4,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -950, 10])
        if Num==4 :
                eqdist=3.2286860753
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*1.9,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-693.16,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -800, 10])
        if Num==5 :
		eqdist=6.0751482197
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*1.9,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-889.67,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -1000, 10])
        if Num==6 :
		eqdist=5.1362816011
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*1.9,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-731,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -800, 10])
        if Num==7 :
		eqdist=5.9741432049
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		#pl.plot(Es9[:,0]*2,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-719.82,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -800, 10])
        if Num==8 :
		eqdist=3.7178040269
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*3.6,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-22.79,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -40, 10])
        if Num==9 :
		eqdist=3.7183960483
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*3.6,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-64.5,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -80, 10])
        if Num==10 :
		eqdist=3.7161242668
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.6,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-62.35,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -80, 10])
        if Num==11 :
		eqdist=3.7646579075
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*3.8,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-112.66,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -160, 10])
        if Num==12 :
		eqdist=3.4790218111
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*3.3,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-180.6,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -250, 10])
        if Num==13 :
		eqdist=3.1659049763
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*3.3,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-418.82,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -460, 10])
        if Num==14 :
		eqdist=3.4981573181
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*3.3,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-197.37,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -300, 10])
        if Num==15 :
		eqdist=3.1716232527
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		#pl.plot(Es9[:,0]*3,Es9[:,1]/23.06035*1000,'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-501.38,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -600, 10])
        if Num==16 :
		eqdist=4.4216545105
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.7,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-64.93,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -80, 10])
        if Num==17 :
		eqdist=3.3802649620
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.7,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-141.47,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -150, 10])
        if Num==18 :
		eqdist=3.5601912326
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.7,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-99.76,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -120, 10])
        if Num==19 :
		eqdist=3.9502149301
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.4,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-195.65,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -220, 10])
        if Num==20 :
		eqdist=4.9086426317
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.6,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-116.53,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -140, 10])
        if Num==21 :
		eqdist=4.8838123806
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.5,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-241.66,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -280, 10])
        if Num==22 :
		eqdist=4.9206132506
                distcm1=np.loadtxt("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22/KB_test/cm_dist_our_script/dist_cm_S%i.txt"%(Num))
                distcm=distcm1-eqdist
		pl.plot(distcm,Es*Ryd, label="S-%i,vdW-DF"%(Num))#*sep_list**6)
		pl.plot(distcm,Es2*Ryd,label="S-%i,vdW-DF2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es3*Ryd,label="S-%i,rVV10"%(Num) )#*sep_list**6)
		pl.plot(distcm,Es4*Ryd, label="S-%i,vdw-df-cx"%(Num))#*sep_list**6)
		pl.plot(distcm,Es5*Ryd, label="S-%i,optb88"%(Num))#*sep_list**6)
		pl.plot(distcm,Es6*Ryd, label="S-%i,rev-vdw-df2"%(Num))#*sep_list**6)
		pl.plot(distcm,Es7*Ryd, label="S-%i,DF3-2.3253-6.8"%(Num))#*sep_list**6)
		pl.plot(Es8[:,0],Es8[:,1]/23.06035*1000,'o-', label='QC_result',color='gray')
		#pl.plot(Es9[:,0]*2.2,Es9[:,1],'x-', label='QC_s22x5',color='blue')
                pl.plot(0.0,-304.87,'x',label='QC_Takatani',color='red')
	  	pl.axis([-1, 6, -350, 10])
	pl.legend()
	pl.savefig("compare_S22-%i.jpeg"%(Num))
	pl.close()
#        pl.show()
