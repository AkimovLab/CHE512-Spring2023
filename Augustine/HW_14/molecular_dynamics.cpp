#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
using namespace std;

double time_step_q(double q, double p, double mass, double dt) {
    return q + dt * (p / mass);
}

double time_step_p(double p, double f, double dt) {
    return p + f * dt;
}

double energy_func(double q, double k) {
    return 0.5 * k * q * q;
}

double force_func(double q, double k) {
    return -k * q;
}

int main() {
    // Initialize variables
    double x0 = -1.0, x = x0;
    double p0 = 0.0, p = p0;
    double k = 0.1, mass = 1.0;
    double dt = 0.01;
    int nsteps = 10000;

    // Initialize output files
    ofstream Etot("Etot.txt"), Epot("Epot.txt"), Ekin("Ekin.txt"), 
             xvalues("xvalues.txt"), pvalues("pvalues.txt"), tvalues("tvalues.txt");

    // Initialize vectors to store data
    vector<double> X, P, T, E_pot, E_kin, E_tot;

    // Run simulation
    for (int i = 0; i < nsteps; ++i) {
        // Store current values
        X.push_back(x);
        P.push_back(p);
        T.push_back(i * dt);

        // Calculate energies
        double e_pot = energy_func(x, k);
        double f = force_func(x, k);
        double e_kin = 0.5 * p * p / mass;

        // Store energies
        E_pot.push_back(e_pot);
        E_kin.push_back(e_kin);
        E_tot.push_back(e_kin + e_pot);

        // Update positions and momenta
        x = time_step_q(x, p, mass, dt);
        p = time_step_p(p, f, dt);

        // Write energies and trajectories to output files
        Etot << e_pot + e_kin << "\n";
        Epot << e_pot << "\n";
        Ekin << e_kin << "\n";
        xvalues << x << "\n";
        pvalues << p << "\n";
        tvalues << i * dt << "\n";
    }


    // Close output files
    Etot.close();
    Epot.close();
    Ekin.close();
    xvalues.close();
    pvalues.close();
    tvalues.close();

    return 0;
}
