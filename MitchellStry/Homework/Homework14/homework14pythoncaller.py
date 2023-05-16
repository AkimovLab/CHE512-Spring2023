import subprocess

compilecmd="g++ -o homework14pythonrun  homework14.cpp"
subprocess.run(compilecmd,shell=True,check=True)
runcmd="./homework14"
output=subprocess.checkoutput(runcmd,shell=True)
print(output.decode())
