import numpy as np
from scipy import integrate
from scipy import sparse

import matplotlib.pyplot as plt
from matplotlib import animation
plt.rc('savefig', dpi=300)


# Initial conditions
dx = 0.002                  #point separation
x = np.arange(0, 10, dx)    

a = int(input("What is the width of the box?\n"))



kx = 50                     # wave number
m = 1                       # mass
sigma = 0.5                 # width of initial gaussian wave-packet
x0 = a/2 + 3.0                    # center of initial gaussian wave-packet


#Wavefunction
A = 1.0 / (sigma * np.sqrt(np.pi))  # normalisation constant
psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)


# Potential V(x)

V0 = int(input("What is your potential?\n"))

def VBox(V0, a, x):   
    V = np.zeros(x.shape)
    for i, _x in enumerate(x):
        if _x > a + 3 and _x < 3:
            V[i] = V0
    return V

        


# Plot of psi0 and V
fig = plt.figure(figsize=(15, 5))
plt.plot(x, VBox(V0, a, x)*0.01, "k--", label=r"$V(x) (x0.01)")
plt.plot(x, np.abs(psi0)**2, "r", label=r"$\vert\psi(t=0,x)\vert^2$")
plt.plot(x, np.real(psi0), "g", label=r"$Re\{\psi(t=0,x)\}$")
plt.legend(loc=1, fontsize=8, fancybox=False)
fig.savefig('Box_initial@2x.png')

print("Total Probability: ", np.sum(np.abs(psi0)**2)*dx)


# Laplacian
D2 = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2


# Solve Schrodinger Equation
hbar = 1
# hbar = 1.0545718176461565e-34
# RHS of Schrodinger Equation
def psi_t(t, psi):
    return -1j * (- 0.5 * hbar / m * D2.dot(psi) + VBox(V0, a, x) / hbar * psi)


# Solve the Initial Value Problem
dt = 0.001  # time interval for snapshots
t0 = 0.0    # initial time
tf = 0.2    # final time
t_eval = np.arange(t0, tf, dt)

print("Solving...")
sol = integrate.solve_ivp(psi_t,
                          t_span=[t0, tf],
                          y0=psi0,
                          t_eval=t_eval,
                          method="RK23")


# Plotting
fig = plt.figure(figsize=(6, 4))
for i, t in enumerate(sol.t):
    plt.plot(x, np.abs(sol.y[:, i])**2)                  # Plot Wavefunctions
    print("Total Prob. in frame", i, "=", np.sum(np.abs(sol.y[:, i])**2)*dx)   # Print probability
plt.plot(x, VBox(V0, a, x) * 0.001, "k--", label=r"$V(x) (x0.001)")   # Plot Potential
plt.legend(loc=1, fontsize=8, fancybox=False)
fig.savefig('step@2x.png')


# Animation
fig = plt.figure(figsize=(8, 6))

ax1 = plt.subplot(2, 1, 1)
ax1.set_xlim(0, 10)
ax1.set_ylim(-1, 3)
title = ax1.set_title('')
line11, = ax1.plot([], [], "k--", label=r"$V(x)$ (x0.001)")
line12, = ax1.plot([], [], "b", label=r"$\vert \psi \vert^2$")
plt.legend(loc=1, fontsize=8, fancybox=False)

ax2 = plt.subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_ylim(-2, 2)
line21, = ax2.plot([], [], "k--", label=r"$V(x)$ (x0.001)")
line22, = ax2.plot([], [], "r", label=r"$Re\{ \psi \}$")
plt.legend(loc=1, fontsize=8, fancybox=False)

  
def init():
    line11.set_data(x, VBox(V0, a, x) * 0.001)
    line21.set_data(x, VBox(V0, a, x) * 0.001)
    return line11, line21


def animate(i):
    line12.set_data(x, np.abs(sol.y[:, i])**2)
    line22.set_data(x, np.real(sol.y[:, i]))
    title.set_text('Time = {0:1.3f}'.format(sol.t[i]))
    return line12, line22


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(sol.t), interval=200, blit=True)


# Save the animation 
print("Generating video")
anim.save('Box.mp4', fps=15, extra_args=['-vcodec', 'libx264'], dpi=600)
print("Generating GIF")
anim.save('Box@2x.gif', writer='pillow', fps=15)
# anim.save('Box@2x.gif', writer='imagemagick', fps=15, dpi=150, extra_args=['-layers Optimize'])
#anim.save('Box@2x.gif', writer='imagemagick', fps=15, dpi=150)
