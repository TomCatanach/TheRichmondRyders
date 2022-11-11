import numpy as np
import matplotlib.pyplot as plt

#Function variables

x_array = np.linspace(-5, 5, 500)
V_x = 0

#defining the function for the potential 
V = []
a = 0

def VStep(V_0, a):
    for i in range(500): 
     if x_array[i] > a :
        V.append(V_0)
     else:
        V.append(0)        
    return V


#example plot of the potential for V_0 = 4 and a = 3
plt.plot(x_array, VStep(4,0.5))

    

