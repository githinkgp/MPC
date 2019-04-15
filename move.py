#!/usr/bin/env python
import math
import numpy as np
from casadi import *
from array import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def move(x,u,w,dt):
    x_new=x[0]+dt*u*math.cos(x[2])
    y_new=x[1]+dt*u*math.sin(x[2])
    t_new=x[2]+dt*w
    
    return x_new, y_new, t_new
