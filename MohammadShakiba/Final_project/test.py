import ctypes

mylib = ctypes.cdll.LoadLibrary('./libmain.so')

data = [1.0, 2.0, 3.0, 4.0, 5.0]
n = len(data)

# Convert the data array to a C-style array of doubles
c_data = (ctypes.c_double * n)(*data)

# Call the sum_parallel function
result = mylib.sum_parallel(c_data, n)
#result = mylib.sum_parallel(data, n)

print(result)

mylib.hello_world_p()

mylib.run_md()

