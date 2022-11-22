import numpy as np
import matplotlib.pyplot as plt


#defining the function for the potential of a particle in a box where V0 is the arbitrary potential of the box, and a is the width of the box.



V = []
V0 = int(input("What is your potential?\n"))
a = float(input("What is the width of the box?\n"))

x_array = np.linspace(-3*a, 4*a, 500)



def VBox(V0, a, x_array):
    for i in range(500): 
     if x_array[i] > a or x_array[i] < 0:
        V.append(V0)
     else:
        V.append(0)        
    return V
 
    
 
#example plot of the potential
plt.plot(x_array, VBox(V0, a, x_array))

    

