# Final project for CHE 512

In this project, we intend to transfer code from low-level languages to Python. In order to do that, we use `cpython` library of Python. The Fortran code contains the matrix multiplication and a simple addition subroutines and the C++ code is a copy of the MD code with two other OMP codes that one prints `Hello World!` in parallel and the other provides a parallel version of summation of a data list.

The Fortran and C++ codes should be compiled using:

```
gfortran -shared -fPIC -fopenmp libmatmul.so -c matmul.f90
gcc -shared -fPIC -fopenmp libmain.so -c main.cpp
```

In order to call the functions in Python we use the `test.py` and `matmul.py` files:

```
python matmul.py

export OMP_NUM_THREADS=4
python test.py
```




