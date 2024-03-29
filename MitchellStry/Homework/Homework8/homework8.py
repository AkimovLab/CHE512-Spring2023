"""
Need to solve for equation 7 of Crossing Classified and Corrected Fewest Switches Surface Hopping paper.

H = E(ax[orbital]) ([orbital]+ E(-t[orbaital](k) (k+1 + k +1 [orbital)] + E((1/2)K(x^2)+m(v^2))
molecule is k
x is a vibrational degree of freedom
v is velocity
K is force constant amu/Pa*s^2
m is mass amu
t is hopping amplitude
a is local electron phonon coupling (cm)^-1/(angstroms)
L is length in angstroms
omega is Phonon frequency
g is Electron-phonon coupling strength
N is number of electrons
"""
import math
import numpy as np
f=open("Hamiltonian_File.txt", "w+")
import sys
import matplotlib.pyplot as plt
#The below is homeworks 3,5,6.

a=3500.0
Kb=1.380649*10**-23
T=300.0
gamma=100.0
C=0.1
t= 1.0
L=5.0
m=250.0
V=[]
K=[]
N=0
omega1=0
omega=0
j=0
i=0
t=0
H=0
#The numbers above are from the literature.
class problemsolving:
    """
    This class solves the hamiltonian.
    """
    def matrixmaking(N,omega):
        """
        This function makes the matrixes.
        Args:
            c (matrix): Fermion opperator
            b (matrix): Phonon opperator
            N (float): number of electrons
            omega1 (float): Frequency
        Returns:
            c (matrix): Fermion opperator
            b (matrix): Phonon opperator
            N (float): number of electrons
            omega1 (float): Frequency
        """
        N=N
        omega1=omega
        c = np.zeros((L,N))
        b = np.zeros((L,))
        return N,omega1,c,b
    N,omega1,c,b= matrixmaking(N,omega)
    print(F"The number of electrons is {N}, the frequency is {omega1}, the fermion opperator is {c} and the phonon opperator is {b}.")
    def energies (L,N,omega1):
        """
        This function solves the energies.
        Args:
            c[i] (matrix): Fermion opperator
            b[i] (matrix): Phonon opperator
            omega1 (float): Frequency
        Returns:
            K (matrix): The kenetic energy
            V (matrix): The potential energy
        """
        for i in range(L):
            for j in range(N):
                c[i,j] = np.sqrt(2.0/(L+1)) * np.sin((j+1)*np.pi*(i+1)/(L+1))
            b[i] = np.sqrt(1.0/(2.0*omega1)) * (np.sqrt(omega1) * i + 1j)
        K = np.zeros((N*L, N*L)) 
        V = np.zeros((N*L, N*L)) 
        """
        Calculate the matrices for the kinetic and potential energies
        """
        return K,V
    K,V,= energies(L,N,omega1)
    def matrixsolve(L,N,j,i,t,omega1,K,V):
        """
        Solves the Matrixes
        Args:
            L (float): length
            N (float): number of electrons
            t (float): Hopping amplitude
            omega1 (float): Frequency
        Returns:
            K (matrix): The kenetic energy
            V (matrix): The potentail energy
        """
        for i in range(L):
            for j in range(N):
                K[i*N+j,i*N+(j+1)%N] = -t
                K[i*N+j,(i+1)%L*N+j] = -t
                K[i*N+j,i*N+j] = omega1*(j+0.5)
                V[i*N+j,i*N+j] = g*b[i]
        return K,V
    K,V,= matrixsolve(L,N,j,i,t,omega1)
    print(F"The solution to the matrixes is Kenetic={K}, and Potential={V}")
    def finishedhamil(K,V):
        """
        Solves the Hamiltonian
        Args:
            K (matrix): The kenetic energy
            V (matrix): The potential energy
        Returns:
            H (matrix): The hamiltonian solution
        """
        f.write(F"The solution to the hamiltonian is {H}. \n")
        f.clos
        X=K
        Y=V
        plt.plot(X,Y)
        plt.xlabel("Kenetic Energy")
        plt.ylabel("Potential Energy")
        plt.title("Hamiltonian")
        plt.show()
        H=K+V
        print(F'The solution to the hamiltonian is {H}')
        return H
    H=finishedhamil(K,V)
