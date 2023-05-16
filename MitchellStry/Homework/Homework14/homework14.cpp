#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
double sconst=1.0;
double m=1.0;
double tstep=0.01;
double ttime=10.0;

void updateeuler(double &p,double &v,double &f){
    f=-sconst*p;
    double a=f/m;
    p+=v*tstep;
    v+=a*tstep;
}
void updateeulermidpoint(double &p,double &v,double &f){
    double ip=p+v*tstep/2;
    double iv=v+(-sconst*p/m)*tstep/2;
    f=-sconst*ip;
    double a=f/m;
    p+=iv*tstep;
    v+=a*tstep;
}
int main(){
    ofstream o_file("output.txt");
    double p=1.0;
    double v=0.0;
    double f=0.0;
    o_file<<"Euler method:"<<endl;
    for (double t=0.0;t<=ttime;t+=tstep){
        o_file<<t<<" "<<p<<" "<<v<<" "<<f<<endl;
        updateeuler(p,v,f);
    }
    p=1.0;
    v=0.0;
    f=0.0;
    o_file<<"\nEuler midpoint method:"<<endl;
    for (double t=0.0;t<=ttime;t+=tstep) {
        o_file<<t<<" "<<p<<" "<<v<<" "<<f<<endl;
        updateeulermidpoint(p,v,f);
    }
    o_file.close();
    return 0;
}
