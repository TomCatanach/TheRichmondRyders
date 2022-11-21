import numpy as np
from scipy import integrate
from scipy import sparse

import matplotlib.pyplot as plt
plt.rc('savefig', dpi=300)


# spatial separation
dx    = 0.04                      
    
# spatial grid points
x     = np.arange(0, 10, dx) 

#wave number
kx    = 0.3                    
#mass - smaller number the more high
m     = 2      
# width -  up or down             
sigma = 0.2                      
# center of gaussian wave-packet at initial 
x0    = 4.0       

a= float(input("what is the position of step?\n"))

x = -1-a

# Initial Wavefunction
A = 1.0 / (sigma * np.sqrt(np.pi))  # normalization constant
psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)


# Potential V(x)
V = []
V0 = int(input("What is your potential?\n"))

def VStep(V0, a, x):
    V = []
    for i in range(500): 
     if x[i] > a :
        V.append(V0)
     else:
        V.append(0)        
    return V



# Make a plot of psi0 and V
fig = plt.figure(figsize=(15, 5))
plt.plot(x, VStep(V0, a, x), "k--", label=r"$V(x) (x0.01)")
plt.plot(x, np.abs(psi0)**2, "r", label=r"$\vert\psi(t=0,x)\vert^2$")
plt.plot(x, np.real(psi0), "g", label=r"$Re\{\psi(t=0,x)\}$")
plt.legend(loc=1, fontsize=8, fancybox=False)
fig.savefig('step_initial@2x.png')

print("Total Probability: ", np.sum(np.abs(psi0)**2)*dx)


# Laplace Operator (Finite Difference)
D2 = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2


# Solve Schrodinger Equation
hbar = 1
# hbar = 1.0545718176461565e-34
# RHS of Schrodinger Equation
def psi_t(t, psi):
    for i in range (500):
        return -1j * (- 0.5 * hbar / m * D2.dot(psi) + VStep(V0, a, x)[i] / hbar * psi)


# Solve the Initial Value Problem
dt = 0.001  # time interval for snapshots
t0 = 0.0    # initial time
tf = 0.2    # final time
t_eval = np.arange(t0, tf, dt)  # recorded time shots

print("Solving initial value problem")
sol = integrate.solve_ivp(psi_t,
                          t_span=[t0, tf],
                          y0=psi0,
                          t_eval=t_eval,
                          method="RK23")


# Plotting
fig = plt.figure(figsize=(6, 4))
for i, t in enumerate(sol.t):
    plt.plot(x, np.abs(sol.y[:, i])**2)                 
    # Plot Wavefunctions
    print("Total Prob. in frame", i, "=", np.sum(np.abs(sol.y[:, i])**2)*dx)   # Print Total Probability (Should = 1)
plt.plot(x, VStep(V0, a, x), "k--", label=r"$V(x) (x0.001)")   # Plot Potential
plt.legend(loc=1, fontsize=8, fancybox=False)
fig.savefig('step@2x.png')

   
fig, ax = plt.subplots(1,1, figsize=(7,5))


#ax.grid()
ln1, = plt.plot([], [], 'r-', lw=2, markersize=8, label='wavefunc')
time_text = ax.text(0.70, 15, '', fontsize=15,
           bbox=dict(facecolor='white', edgecolor='black'))
ax.set_ylim(-5,25)
ax.set_xlim(0.2)
ax.set_ylabel('$|\psi(x)|^2$', fontsize=30)
ax.set_xlabel('$x/L$', fontsize=30)
ax.legend(loc='upper left')
ax.set_title('Animation')
plt.show()




# Save the animation into a short video
print("Generating mp4")
print("Generating GIF")
# anim.save('step@2x.gif', writer='pillow', fps=15)
# anim.save('step@2x.gif', writer='imagemagick', fps=15, dpi=150, extra_args=['-layers Optimize'])


plt.show()