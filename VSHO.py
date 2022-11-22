import numpy as np
import matplotlib.pyplot as plt

#Function variables

x_array = np.linspace(-5, 5, 500)
V_x = 0

#defining the function for the simple harmonic oscillator

def VSHO(k):
    
    V_x = k * x_array ** 2
    return V_x


#example plot of the potential for k=4
plt.plot(x_array, VSHO(4))
 
    

