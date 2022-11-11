import numpy as np
import matplotlib.pyplot as plt

#Function variables


x1 = int(input("What is your potential?\n"))
x2 = float(input("What is the position of the step in the x axis??\n"))




x_array = np.linspace(-x2, x1, 500)
V_x = 0

#defining the function for the potential  where V0 is the potential of the step and a is its position on the x axis
V = []
V0 = int(input("What is your potential?\n"))
a = float(input("What is the position of the step in the x axis??\n"))

def VStep(V_0, a, x_array):
    for i in range(500): 
     if x_array[i] > a :
        V.append(V0)
     else:
        V.append(0)        
    return V


#example plot of the potential 
plt.plot(x_array, VStep(V0, a, x_array))

    

