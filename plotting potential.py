import numpy as np
import matplotlib.pyplot as plt



Nx = 301
Nt = 100000
dx=1e-7
x = np.linspace(0, 1, Nx)

Nx = 301
Nt = 100000
dx = 1/(Nx-1)
dt=1e-7
x = np.linspace(0,1, Nx)
psi0 = np.sqrt(2)*np.sin(np.pi*x)
mu, sigma = 1/2, 1/20
V = -1e4*np.exp(-(x-mu)**2/(2*sigma**2))

np.sum(np.absolute(psi0)**2)*dx

dt/dx**2
plt.figure(figsize=(8,3))
plt.plot(x,V)
plt.xlabel('$x$')
plt.ylabel('$V(x)$')
plt.show()

psi = np.zeros([Nt,Nx])
psi[0] = psi0


plt.show()