import numpy as np
import matplotlib.pyplot as plt

#Function variables

x_array = np.linspace(-5, 5, 500)
V_x = 0

#defining the function for the potential of a particle in a box where V_0 is the arbitrary potential of the box, and a is the width of the box.



V = []
V_0 = int(input("What is your potential?\n"))
a = float(input("What is the width of the box?\n"))

 

def VBox():
    for i in range(500): 
     if x_array[i] > a or x_array[i] < 0:
        V.append(V_0)
     else:
        V.append(0)        
    return V
 
    
 
#example plot of the potential
plt.plot(x_array, VBox())

    

