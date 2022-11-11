import numpy as np
import matplotlib.pyplot as plt

#Function variables

x_array = np.linspace(-5, 5, 500)
V_x = 0

#defining the function for the simple harmonic oscillator

k = float(input("What is the value of k?\n"))


def VSHO():
    
    V_x = k * x_array ** 2
    return V_x


#example plot of the potential 
plt.plot(x_array, VSHO())

    

