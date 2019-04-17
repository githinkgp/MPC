#!/usr/bin/env python
import math
import numpy as np
from casadi import *
from array import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from move import move
import time
from Ad import Ad

fig=plt.figure()
ax=plt.axes()
ax.set_xlim((0, 100))
ax.set_ylim((0, 100))

X0=[1,1,0]
dt=0.1
u=5
w=1

N=5
x=np.zeros((N,3),dtype=np.float)
x[0]=X0
a=ax.scatter(x[0,0],x[0,1])
rectangle=plt.Rectangle([50,50],20,20,fc='r')
ax.add_patch(rectangle)
#plt.pause(0.5)

lambda_y=np.identity(3*N)
print "lambday:", np.shape(lambda_y)
yref=[[60],[60],[math.pi/2]]
yref_bar=yref

#C=[[1, 0, 0, 0, 0],[0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
flag=1
while flag==1:
A=Ad(2, 0)
A_bar=A
An=A
C_bar=np.zeros((3*N,5*N),dtype=np.int)
for n in range(N):
    if n!= 0:
        An=np.matmul(An,A)
        A_bar=np.append(A_bar,A,axis=0)
        yref_bar=np.append(yref_bar,yref,axis=0)
    C_bar[n*3][n*5]=1
    C_bar[n*3+1][n*5+1]=1
    C_bar[n*3+2][n*5+2]=1
C_barT=np.transpose(C_bar)
A_barT=np.transpose(A_bar)
#yref_bar=np.transpose(yref_bar)
print "yrefbar:", np.shape(yref_bar)
print "C_bar:", np.shape(C_bar)
print "A_bar:", np.shape(A_bar)
x = SX.sym('x',5,1)

print "x:", np.shape(x)
m=np.matmul(C_bar,A_bar)  
print "m:", np.shape(m)  
nlp = {'x':x, 'f':mtimes([mtimes(m,x).T, lambda_y, mtimes(m,x)])-mtimes([mtimes(m,x).T, lambda_y, yref_bar])-mtimes([yref_bar.T, lambda_y, mtimes(m,x)])}

S = nlpsol('S', 'ipopt', nlp)

print(S)

r = S(x0=[0,0,0,2,0], lbx=[0,0,0,0,-1], ubx=[100,100,6.28,5,1])

x_opt = r['x']
print('x_opt: ', x_opt)

#for n in range(N-1):
#    a.remove()
#    x[n+1]=move(x[n],u,w,dt)
#    A=Ad(u, x[n][2])
#    A_bar=
#    a=ax.scatter(x[n+1,0],x[n+1,1])
#    plt.pause(0.5)
    
#plt.show()



