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

def Ad(u, t):
    A=[[1, 0, -u*math.sin(t)/10, math.cos(t)/10, -u*math.sin(t)/200], [0, 1, u*math.cos(t)/10, math.sin(t)/10, u*math.cos(t)/200], [0, 0, 1, 0, 1/10], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    return A
