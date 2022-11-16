# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:17:58 2022

@author: Laptop
REDEFINE BARRIER IN ALL OF THE PROGRAM
I THINK IT WAS DEF(POTENTIAL_BARRIER)
"""


# specify constants
hbar = 1.0   # planck's constant
m = 1.9      # particle mass
valid = 1
while valid == 1:
    form = input("""Specify the form of potential to be computed:\n
               1. Forward step potential\n
               2. Backward step potential\n
               3. Barrier potential ($v>v_0$)\n
               4. Barrier potential ($v<v_0$)\n
               5. Infinite potential well\n
               NOTE: Please enter '1', '2', '3', '4', '5'.\n""")
    if form == 1:
        def barrier(x, width, height):
            for i in range(x):
                if V[i]>width:
                    V.append(V0)
                else:
                    V.append(0)
            return V
        valid = 2
        
    elif form == 2:
        def barrier(x, width, height):
            for i in range(x):
                if V[i]<0:
                    V.append(V0)
                else:
                    V.append(0)
            return V
        valid = 2
    
    elif form == 3:
        def barrier(x, width, height):
            return height * (theta(x) - theta(x - width))
        """ do something to make this v>v_0"""
        valid = 2
    
    elif form == 4:
        def barrier(x, width, height):
            return height * (theta(x) - theta(x - width))
        valid = 2
        
    elif form == 5:
        def barrier(x, width, height):
            for i in range(x):
                if V[i]>width or V[i]<0:
                    V.append(0)
            return V
        valid = 2
    
    else:
        print(form," is not an accepted value, returning to selection menu...\n ")
        valid = 1

######################################################################
# Create the animation

# specify time steps and duration
dt = 0.01
N_steps = 50
t_max = 120
frames = int(t_max / float(N_steps * dt))


# specify range in x coordinate
N = 2 ** 11
dx = 0.1
x = dx * (np.arange(N) - 0.5 * N)

# specify potential
V0 = float(input("Desired quantity for potential:\n"))
L = hbar / np.sqrt(2 * m * V0)
a = 3 * L
x0 = -60 * L
V_x = barrier(x, a, V0)
V_x[x < -98] = 1E6
V_x[x > 98] = 1E6

# specify initial momentum and quantities derived from it
p0 = np.sqrt(2 * m * 0.2 * V0)
dp2 = p0 * p0 * 1./80
d = hbar / np.sqrt(2 * dp2)

k0 = p0 / hbar
v0 = p0 / m
psi_x0 = gauss_x(x, d, x0, k0)

# define the Schrodinger object which performs the calculations
S = Schrodinger(x=x,
                psi_x0=psi_x0,
                V_x=V_x,
                hbar=hbar,
                m=m,
                k0=-28)
