import numpy as np
import matplotlib.pyplot as plt

#Function variables

x_array = np.linspace(-5, 5, 500)
V_x = 0

#defining the function for the potential of a particle in a box where V_0 is the arbitrary potential of the box, and a is the range of the box.

V = []
a = 0

def VBox(V_0, a):
    for i in range(500): 
     if x_array[i] > a or x_array[i] < 0:
        V.append(V_0)
     else:
        V.append(0)        
    return V


#example plot of the potential for V_0 = 4 and a = 3
plt.plot(x_array, VBox(4,3))

    

