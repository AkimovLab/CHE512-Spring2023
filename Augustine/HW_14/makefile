all: molecular_dynamics.exe

molecular_dynamics.exe: molecular_dynamics.o
	g++ -o molecular_dynamics.exe molecular_dynamics.o

molecular_dynamics.o: molecular_dynamics.cpp
	g++ -c molecular_dynamics.cpp
     
clean:
	rm molecular_dynamics.o molecular_dynamics.exe
