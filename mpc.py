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

fig=plt.figure()
ax=plt.axes()
ax.set_xlim((0, 100))
ax.set_ylim((0, 100))

X0=[1,1,0]
dt=0.1
u=5
w=1

N=10
x=np.zeros((N,3),dtype=np.float)
x[0]=X0
a=ax.scatter(x[0,0],x[0,1])
rectangle=plt.Rectangle([50,50],20,20,fc='r')
ax.add_patch(rectangle)
plt.pause(0.5)

for n in range(N-1):
    a.remove()
    x[n+1]=move(x[n],u,w,dt)
    a=ax.scatter(x[n+1,0],x[n+1,1])
    plt.pause(0.5)
    
plt.show()



