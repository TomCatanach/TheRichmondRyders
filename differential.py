# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 00:08:43 2022

@author: Thomas
"""

import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation

class schrodinger:
    
    def form(x):
        """
        Parameters
        ----------
        choices for what form the relation should be
        -------
        output
            the apropriate equation ready to be computed and approximated
        """
        valid = 1
        
        while valid ==  1:
            form = input("Form of data to be operated on: Reccomended[R] or Custom[C]\n")
        
            if form == "R":
                valid = 2
                return np.sin(x)
                
            elif form == "C":
                valid = 2
                print("the function follows the form y = acos(x) + ibsin(x)\n")
                a=input("Please input value for a: ")
                b=input("Please input value for b: ")
                return a*np.cos(x) + b*np.sin(x)
                
            else:
                print("This is not an accepted input parameter, please enter Reccomended[R] or Custom[C]:\n")
                valid=1
    
    
    def diff2(x,form(x)): # doesnt work - i want the output from form to be read into the function
        #make form global?
        """
        second derivative calculation
        """
        # Define a grid in x
        N = 100 # larger N creates a larger resolution for the fit
        x_array = np.linspace(0, 2 * np.pi, N)
    
        # Loop over the grid and calculate the second order derivative at each point
        second_order = []
    
        #lower values of h make for a plot with higher resolution
        #numerical calculation approaches exact calculation as h tends to 0
        h = 0.1
        
        for x in x_array:
            second_order_derivative = (form(x - h) - 2 * form(x) + form(x + h)) / h ** 2 # second order differential
            second_order.append(second_order_derivative)
            
        return second_order_derivative
    
    def diff1(x,form(x)):
        """
        first derivative calculation
        """
        # Define a grid in x
        N = 100 # larger N creates a larger resolution for the fit
        x_array = np.linspace(0, 2 * np.pi, N)
    
        # Loop over the grid and calculate the second order derivative at each point
        first_order = []
    
        #lower values of h make for a plot with higher resolution
        #numerical calculation approaches exact calculation as h tends to 0
        #increasing h also increases computational time and may be an issue for slower machines
        #or more complex functions
        h = 0.1
        
        for x in x_array:
            first_order_derivative = (form(x + h) - form(x)) / h # an attempt at writing the first order differential
            first_order.append(first_order_derivative)
            
        return first_order_derivative


"""
below is not needed for the derivative but was helpful 
for checking the correct function was calculated numerically for various inputs
   
# Plot the results
plt.rcParams["axes.labelsize"] = 16
fig, ax = plt.subplots()
ax.plot(x_array, f(x_array), label="f(x)")
ax.plot(x_array, -np.sin(x_array), label="$y''$ calculated exactly")
ax.plot(x_array, ypp_method1, "--", label="$y''$ calculated numerically")
ax.set(xlabel="x")
ax.set(ylabel="y")
ax.legend()
plt.show()
"""

