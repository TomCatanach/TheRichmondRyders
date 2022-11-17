import numpy as np
import matplotlib.pyplot as plt



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


# normalization constant
A = 1.0 / (sigma * np.sqrt(np.pi)) 

# Initial Wavefunction
psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)


# Potential V(x)
x_Vmin = 5         # center of V(x)
T      = 1           # peroid of SHO 
omega = 2 * np.pi / T
k = omega**2 * m
V = 0.5 * k * (x - x_Vmin)**2


# Make a plot of psi0 and V 
plt.plot(x, V*0.01, "k--", label=r"$V(x) = \frac{1}{2}m\omega^2 (x-5)^2$ (x0.01)")
plt.plot(x, np.abs(psi0)**2, "r", label=r"$\vert\psi(x)$")
plt.legend(loc=1, fontsize=8, fancybox=False)
print("Tot Prob: ", np.sum(np.abs(psi0)**2)*dx)


plt.show()


