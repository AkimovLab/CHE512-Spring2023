# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 11:23:43 2023

@author: aobeng2
"""
#import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import math
import pylab as plt
#import scipy.linalg as la

class LVC:
    '''
    This is a class that calculates the lvc hamiltonian, H for a 10 dimensional system from Hs, HsB and HB

    Args:
         called_func (PyObject): This is the function whose values are choosen
         Hs (matrix): values are generated from pre-defined values form paper
         HsB (matrix): values are generated from pre-defined values form paper
         HB (matrix): values are generated from pre-defined values form paper

    '''
    def __init__(self):
        self.Px = 2
        self.Py = 5
        self.omega_X = 2
        self.omega_Y = 3/2
        self.delta = 3
        self.delta_1_2 = -7/4
        self.Cx = 1/4
        self.Cy = 3
        self.X_intial = 3/2
        self.Y_initial = 3/4
        self.X = 1
        self.Y = 10
        self.angle = 2 * np.pi
        self.U = np.array([[np.cos(self.angle/2), -1 * (np.sin(self.angle/2))], # Equation (5)
                           [np.sin(self.angle/2), np.cos(self.angle/2)]])
        self.I2 = -1 * self.U
        self.VA = 0.5 * (self.omega_X**2*((self.X - self.X_intial)**2) + self.omega_Y**2 * ( (self.Y - self.Y_initial)**2) + self.delta)
        self.VD = 0.5 * (self.omega_X**2*((self.X + self.X_intial)**2) + self.omega_Y**2 *( (self.Y + self.Y_initial)**2) + self.delta)
        self.VC = self.Cx * self.X + self.Cy * self.Y + self.delta_1_2
        

    def set_X(self, X):  #Setting Up varibales for X for iterations
        '''
        This is a function takes the values of X from the iteration and uses it in VA, VD, and VC

        Args:
          VA (float): Obtained from vlaues defined in the __init__ function and the vlaue of X from iterations
          VC (float): Obtained from vlaues defined in the __init__ function and the vlaue of X from iterations
          VD (float): Obtained from vlaues defined in the __init__ function and the vlaue of X from iterations

        '''
        self.X = X
        self.VA = 0.5 * (self.omega_X**2*((self.X - self.X_intial)**2) + self.omega_Y**2 * ( (self.Y - self.Y_initial)**2) + self.delta) #equation (17)
        self.VD = 0.5 * (self.omega_X**2*((self.X + self.X_intial)**2) + self.omega_Y**2 *( (self.Y + self.Y_initial)**2) + self.delta) #equation (18)
        self.VC = self.Cx * self.X + self.Cy * self.Y + self.delta_1_2 #equation (16)
    
    
    def Hs(self):
        '''
        This is a function calulates the value of Ts and Hs from the values of TS

        Args:
          Ts (matrix): Obtained from vlaues defined in the __init__ function and the vlaue of X from iterations
          Hs (Matrix): Obtained from the matrix Ts, I2 and VA, VC  and VD from set_X funtion

        '''

        Ts = 0.5 * (self.Px*self.Px + self.Py*self.Py) # Equation 15
        Hs = Ts*self.I2 + np.array([[self.VA, self.VC],
                                    [self.VC, self.VD]])  # Writing equation (12)
        return Hs
    
    '''
    Writing the algorithm to find HsB and HB,The system is assumed to be 10 dimensional 
    Linear vibronic system
    The coupling constant lambda(jx) and lambda (jy)
    '''

    def HB_HsB(self):
        '''
        This is a function calulates the value of Ts and Hs from the values of TS

        Args:
          Writing the algorithm to find HsB and HB,The system is assumed to be 10 dimensional
          Linear vibronic system
          The coupling constant lambda(jx) and lambda (jy)

        '''

        omega_j = 3 # Frequency Value Assumed from figure 2
        lambda_jx = 4
        lambda_jy = lambda_jx
        # lambda_jx and lambda_jy are coupling constant of the system
        pj = 10 #momenta of the system
        omega_j_saquared = omega_j **2
        HsB = 0
        HB = 0
        N = 10
        #Q_j is the mass weighted coordinate of the system
        for Q_j in range(1, N + 1 - 2):
            HsB +=  (pj ** 2 + omega_j_saquared * Q_j ** 2 ) * self.I2 # Iterating through the number of dimension minus 2 to find summation
            HB +=  (lambda_jx * self.X + lambda_jy * self.Y) * self.I2 * Q_j   #Solving for equation (13)

        HsB = HsB * 0.5  #Multiplying result obtained from summation function by 0.5 to get equation (14)

        return HsB, HB

    def H(self):
        Hs = self.Hs()
        HsB, HB = self.HB_HsB()
        H = Hs + HsB + HB # This is obatined from equation (11)
        return H
lvc = LVC()

# Define a range of values for X
X_values = np.arange(1, 6)

# Initialize string to store content
file_content = ""


# Loop over the X values and calculate the Hamiltonian for each value
for X in X_values:
    lvc.X = X * 5
    H = lvc.H()
    Hs = lvc.Hs()
    HsB, HB = lvc.HB_HsB()
    
    plot_title = f'Plot {X}: LVC Hamiltonian against X, X = {X}'
    H, X = H, X
    f1 = plt.figure()
    plt.plot( H, 'r', label='H', linestyle='--')
    #plt.plot( X  , 'b-', label='X')
    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('X', fontsize=17)
    plt.ylabel('Lvc Hamiltonian', fontsize=17)
    plt.title(plot_title)
    #Assigning file name variables that generates unique image name for each plotted graph
    #filename = f'''Fig. {X}. LVC Hamiltonian against X, X = {X}'''
    filename = "fig_" +str(X) + "_LVC_Hamiltonian_against_X_X_is_"+str(X) 
    f1.savefig(filename)
    print(filename)
    #print(X)
    

    # Append iteration content to the file content string
    file_content += f"""LVC Hamiltonian, X = {X}: H = Hs + HsB + HB\n"""
    file_content += f'''________________________________________\nHB = {HB}\n________________________________________\n'''
    file_content += f'HS = {Hs}\n________________________________________\n'
    file_content += f'HSB = {HsB}\n________________________________________\n'
    file_content += f'''H = {H}\n________________________________________\n
    
'''
    
    

# Write the final content to the text file
with open('lvc_hamiltonian_output_file.txt', 'w') as f:
    f.write(file_content)
    

















