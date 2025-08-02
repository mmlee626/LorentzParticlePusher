#include "particle.h"
#include "vec3.h"
#include "constants.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <chrono>

using namespace constants;

double A = 0.001;
double k = 10.0;

Vec3 bField(double x, double y, double z, double t)
{
    // Input a magnetic field function
    // if (t >= 31.42818) return {0, 0, 0}; // No field after this time
    double r = std::sqrt(x*x + y*y);
    double B_mag = A / r * (1. + k * t);
    Vec3 field = {0, 0, B_mag};
    return field; // Converts to natural units if necessary
}

Vec3 eField(double x, double y, double z, double t)
{
    // Input an electric field function
    // if (t >= 31.42818) return {0, 0, 0}; // No field after this time
    Vec3 theta = {y, -x, 0};
    Vec3 theta_hat = theta / norm(theta);
    double E_mag = A * k;
    Vec3 field = theta_hat * E_mag;
    return field; // Converts to natural units if necessary
}

void saveTrajectory(const std::string& filename, const std::vector<Vec3>& traj)
{
    std::ofstream file(filename);
    for (const auto& point : traj)
    {
        file << point[0] << "," << point[1] << "," << point[2] << "\n";
    }
    file.close();
}

void saveScalar(const std::string& filename, const std::vector<double>& data)
{
    std::ofstream file(filename);
    for (const auto& value : data)
    {
        file << value << "\n";
    }
    file.close();
}

int main()
{
    auto start = std::chrono::high_resolution_clock::now();
    std::cout << "Starting simulation...\n";
    int numSteps = 1000000;
    double dt = 0.000031428179;

    std::vector<Particle> particles =
    {
        Particle({0., 1., 0.}, {0.890475171409, 0., 0.}, electron_mass, e),
    };

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Time for trajectory calculation: " << duration.count() / 1000.0 << " seconds" << std::endl;

    for (size_t i = 0; i < particles.size(); ++i)
    {
        for (int step = 0; step < numSteps; ++step) {
            particles[i].step_boris(bField, eField, dt);
            // particles[i].step_rk4_rel(bField, eField, dt);
        }

        std::ofstream file("trajectory" + std::to_string(i) + ".csv");
        for (size_t j = 0; j < particles[i].trajectory.size(); ++j)
        {
            const Vec3& pos = particles[i].trajectory[j];
            file << particles[i].times[j] << "," << pos[0] << "," << pos[1] << "," << pos[2] << "\n";
        }
        file.close();

        // std::ofstream file1("velocities" + std::to_string(i) + ".csv");
        // for (size_t j = 0; j < particles[i].velocities.size(); ++j)
        // {
        //     const Vec3& vel = particles[i].velocities[j];
        //     file1 << particles[i].times[j] << "," << vel[0] << "," << vel[1] << "," << vel[2] << "\n";
        // }
        // file1.close();

        // std::ofstream file2("momentums" + std::to_string(i) + ".csv");
        // for (size_t j = 0; j < particles[i].momentums.size(); ++j)
        // {
        //     const Vec3& mom = particles[i].momentums[j];
        //     file2 << particles[i].times[j] << "," << mom[0] << "," << mom[1] << "," << mom[2] << "\n";
        // }
        // file2.close();

        // saveScalar("energies" + std::to_string(i) + ".csv", particles[i].energies);
        
        std::cout << "Finished particle " << i << "\n";
    }

    end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Final execution time: " << duration.count() / 1000.0 << " seconds" << std::endl;

    return 0;
}
