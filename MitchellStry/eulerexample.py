import matplotlib.pyplot as plt
import numpy as np
import math
def timestep(q,p,mass,f,dt):
    """
    q is coordinate
    p is momentum
    mass is mass
    f is force
    dt is timestep of integration
    """
    qn=q+dt*(p/mass)
    pn=p+f*dt

    return qn,pn

def enerforc(q,k):
    """
    U=1/2*k*q**2
    F=-du/dq=-k*q
    """
    ener=0.5*k*q**2
    forc=-k*q
    return ener,forc

def md(q0,p0,mass,k,dt,nstep):
    """
    q0 start coord
    p0 start moment
    mass
    k force constant potential
    dt integration timestep
    nstep number steps
    """
    X,P,T,Epot,Ekin,Etot=[],[],[],[],[],[]
    x,p=q0,p0
    for i in range(nstep):
        X.append(x)
        P.append(p)
        T.append(i*dt)
        epot,f=enerforc(x,k)
        Epot.append(epot)
        ekin=0.5*p*p/M
        Ekin.append(ekin)
        Etot.append(ekin+epot)
        x,p=timestep(x,p,mass,f,dt)
    return X,P,T,Epot,Ekin,Etot
K=0.1
M=1.0
X,P,T,Epot,Ekin,Etot=md(-1,0.0,M,K,0.25,250)
xnp=np.array(X)
tnp=np.array(T)
omega=math.sqrt(K/M)
exact=-np.cos(omega*tnp)
plt.plot(T,X)
plt.plot(tnp,exact)
%%store[omega]
