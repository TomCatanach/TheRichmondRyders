import numpy as np
import matplotlib.pyplot as plt


#defining the function for the potential of a wall function where V_0 is the arbitrary potential of the wall, and a is the width of the box.



V = []
V_0 = float(input("What is your potential?\n"))
a = float(input("What is the width of the box?\n"))

x_array = np.linspace(-3*a, 4*a, 500)
V_x = 0


def VBox():
    for i in range(500): 
     if x_array[i] > a or x_array[i] < 0:
        V.append(0)
     else:
        V.append(V_0)        
    return V
 
    
 
#example plot of the potential
plt.plot(x_array, VBox())

    
