import numpy as np
import ctypes

# Load the shared library
lib = ctypes.CDLL('./libmatmul.so')

# Define the argument types of the function
matmul = lib.matmul_
matmul.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32),
                   np.ctypeslib.ndpointer(dtype=np.float32),
                   np.ctypeslib.ndpointer(dtype=np.float32),
                   ctypes.c_int]

# Set the return type of the function
matmul.restype = None

# Define the input matrices
N = 3
A = np.random.rand(N,N).astype(np.float32)
B = np.random.rand(N,N).astype(np.float32)

# Allocate space for the output matrix
C = np.zeros((N,N), dtype=np.float32)

# Call the Fortran function
matmul(A, B, C, N)

# Print the results
print("A =")
print(A)
print("B =")
print(B)
print("C =")
print(C)
