# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:51:01 2022

@author: Currys
"""

import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation
Nx = 400
xmin = -4
xmax = 4

Nt = 180
tmin = 0
tmax = 20
k = 1 

x_array = np.linspace(xmin, xmax, Nx)
t_array = np.linspace(tmin, tmax, Nt)
v_x = k * x_array ** 2
#when we have worked out the input function...
#in which the user can enter in their own values/text file
#the x_array above can be replaced to generate the graph for the values they have.
psi = np.exp(-(x_array+2)**2)

dt = t_array[1] - t_array[0]
dx = x_array[1] - x_array[0]

v_x_matrix = diags(v_x)

H = -0.5 * FinDiff(0, dx, 2).matrix(x_array.shape) + v_x_matrix
H[0, :] = H[-1, :] = 0
H[0, 0] = H[-1, -1] = 1

I_plus = eye(Nx) + 1j * dt / 2. * H
I_minus = eye(Nx) - 1j * dt / 2. * H
U = inv(I_minus).dot(I_plus)


psi_list = []
for t in t_array:
    psi = U.dot(psi)
    psi[0] = psi[-1] = 0
    psi_list.append(np.abs(psi))
    

fig, ax = plt.subplots()

ax.set_xlabel("X [arbitary units]")
ax.set_ylabel("$|\Psi(x, t)|$", color="C0")

ax_twin = ax.twinx()
ax_twin.plot(x_array, v_x, color="C1")
ax_twin.set_ylabel("V(x) [arbitary units]", color="C1")

line, = ax.plot([], [], color="C0", lw=2)
ax.grid()
xdata, ydata = [], []

def run(psi):
    line.set_data(x_array, np.abs(psi)**2)
    return line,

ax.set_xlim(x_array[0], x_array[-1])
ax.set_ylim(0, 1)

ani = animation.FuncAnimation(fig, run, psi_list, interval=10)
ani.save("particle_in_squarewell_schro.gif", fps=120, dpi=300)