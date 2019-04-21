#!/usr/bin/env python
path_do_mpc = '../'
# Add do-mpc path to the current directory
import sys
sys.path.insert(0,path_do_mpc+'code')
sys.path.append(r"/Users/githinjohn/Documents/casadi-osx-py27-v3.4.5")
from casadi import *
import math

x    = SX.sym("x") # Concentration A
y    = SX.sym("y") # Concentration B
phi    = SX.sym("phi") # Reactor Temprature
vx = SX.sym("vx")
vy = SX.sym("vy")
w = SX.sym("w")


d      = SX.sym("d") # Vdot/V_R [h^-1]
delta  = SX.sym("delta") #Q_dot second control input


#Define aux variables

C_m1, C_m2, C_f, C_r, D_f, D_r, B_f, B_r, C_r, C_d  = np.ones(10)
lf=1
lr=1
m=1
I_z=1

# Define the differential equations
dx = vx*cos(phi)-vy*sin(phi)
dy = vx*sin(phi)+vy*cos(phi)
dphi = w
dvx = (((C_m1-C_m2*vx)*d-C_r-C_d*vx**2)-(D_f*sin(C_f*atan(B_f*(-atan((w*lf + vy)/vx)+delta))))*sin(delta)+m*vy*w)/m
dvy = ((D_r*sin(C_r*atan(B_r*atan((w*lr-vy)/vx))))+(D_f*sin(C_f*atan(B_f*(-atan((w*lf + vy)/vx)+delta))))*cos(delta)-m*vx*w)/m
dw = ((D_f*sin(C_f*atan(B_f*(-atan((w*lf + vy)/vx)+delta))))*lf*cos(delta)-(D_r*sin(C_r*atan(B_r*atan((w*lr-vy)/vx))))*lr)/I_z


#print gradient(dx,phi)
grad_dvx_vx=gradient(dvx,vx)
grad_dvx_vy=gradient(dvx,vy)
grad_dvx_w=gradient(dvx,w)
grad_dvx_d=gradient(dvx,d)
grad_dvx_delta=gradient(dvx,delta)

grad_dvy_vx=gradient(dvy,vx)
grad_dvy_vy=gradient(dvy,vy)
grad_dvy_w=gradient(dvy,w)
grad_dvy_d=gradient(dvy,d)
grad_dvy_delta=gradient(dvy,delta)

grad_dw_vx=gradient(dw,vx)
grad_dw_vy=gradient(dw,vy)
grad_dw_w=gradient(dw,w)
grad_dw_d=gradient(dw,d)
grad_dw_delta=gradient(dw,delta)



f=Function('f', [x,y,phi,vx,vy,w,d,delta], [grad_dvx_vx,grad_dvx_vy,grad_dvx_w,grad_dvx_d,grad_dvx_delta,grad_dvy_vx,grad_dvy_vy,grad_dvy_w,grad_dvy_d, grad_dvy_delta,grad_dw_vx,grad_dw_vy,grad_dw_w,grad_dw_d,grad_dw_delta])

z=f(1,1,1,1,1,1,0,0)
print z
