import numpy as np
import matplotlib.pyplot as plt

#Function variables

x_array = np.linspace(-5, 5, 500)
V_x = 0

#defining the function for the potential  where V_0 is the potential of the step and a is its position on the x axis
V = []
V_0 = int(input("What is your potential?\n"))
a = float(input("What is the position of the step in the x axis??\n"))

def VStep():
    for i in range(500): 
     if x_array[i] > a :
        V.append(V_0)
     else:
        V.append(0)        
    return V


#example plot of the potential 
plt.plot(x_array, VStep())

    

