#include <iostream>
#include <fstream>
#include <vector>
#include <string>

double potential_energy(double q, double k) {
    return 0.5 * k * q * q;
}

double force(double q, double k) {
    return -k * q;
}

void time_step(double q, double p, double mass, double f, double dt, double &q_new, double &p_new) {
    q_new = q + dt * (p / mass);
    p_new = p + f * dt;
}

void initialize(double x0, double p0, double &x, double &p) {
    x = x0;
    p = p0;
}

void md(double x0, double p0, double mass, double k, double dt, int nsteps,
        std::vector<double> &X, std::vector<double> &P, std::vector<double> &T,
        std::vector<double> &E_pot, std::vector<double> &E_kin, std::vector<double> &E_tot) {

    double x, p;
    initialize(x0, p0, x, p);

    for (int i = 0; i < nsteps; ++i) {
        X.push_back(x);
        P.push_back(p);
        T.push_back(i * dt);

        double e_pot = potential_energy(x, k);
        double f = force(x, k);

        E_pot.push_back(e_pot);
        double e_kin = 0.5 * p * p / mass;
        E_kin.push_back(e_kin);

        E_tot.push_back(e_kin + e_pot);

        double x_new, p_new;
        time_step(x, p, mass, f, dt, x_new, p_new);
        x = x_new;
        p = p_new;
    }
}

void output_to_file(const std::vector<double> &T, const std::vector<double> &X, const std::vector<double> &P, const std::vector<double> &E_pot, const std::vector<double> &E_kin, const std::vector<double> &E_tot, const std::string &filename) {
    std::ofstream outfile(filename);

    outfile << "Time\tPosition\tMomentum\tPotentialEnergy\tKineticEnergy\tTotalEnergy\n";

    for (size_t i = 0; i < T.size(); ++i) {
        outfile << T[i] << "\t" << X[i] << "\t" << P[i] << "\t" << E_pot[i] << "\t" << E_kin[i] << "\t" << E_tot[i] << "\n";
    }

    outfile.close();
}

int main() {
    double x0 = -1.0, p0 = 0.0, mass = 1.0, k = 0.01, t_max = 100.0;
    int nsteps = 100000;
    double dt = t_max / nsteps;
    std::vector<double> X, P, T, E_pot, E_kin, E_tot;

    md(x0, p0, mass, k, dt, nsteps, X, P, T, E_pot, E_kin, E_tot);

    output_to_file(T, X, P, E_pot, E_kin, E_tot, "output.txt");

    return 0;
}

