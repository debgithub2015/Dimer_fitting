import sys
import numpy as np
import pylab as pl
import scipy.optimize as optimization

def f(x,a,b,c):
   return a+b*x+c*x*x

#Zval = np.loadtxt('Zvsmard.txt')[:,0]
#MARDval=np.loadtxt('Zvsmard.txt')[:,2]
bval=np.loadtxt('b-scale.txt')[:,0]
MAPEval=np.loadtxt('b-scale.txt')[:,1]
#print Zval, MARDval
print bval, MAPEval

#x0= np.array([0.0,0.0,0.0])
#sigma=np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])

#xfit=optimization.curve_fit(f,Zval,MARDval,x0,sigma)
#xmin=optimization.fmin(f,np.array([0,0]))
xfit=optimization.curve_fit(f,bval,MAPEval)
a,b,c= xfit[0]
pconv=xfit[1]
print pconv
print xfit
print ("Optimal parameters are a=%g, b=%g, and c=%g" % (a, b, c))

yfitted=f(bval,*xfit[0])
print yfitted

def root(x):
    return f(x,*xfit[0])


xroot=optimization.fsolve(root,0)
print xroot


def g(x): return  xfit[0][0]+xfit[0][1]*x+xfit[0][2]*x*x
def g_der(x): return xfit[0][1]+2.0*x*xfit[0][2]

x0=[10.]

res = optimization.minimize(g,x0,method='Newton-CG',jac=g_der)

print res


pl.plot(bval,MAPEval,'+-')
pl.plot(bval,yfitted,'-')
pl.show()

