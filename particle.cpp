#include "particle.h"
#include "constants.h"
#include <iostream>

using namespace constants;

Particle::Particle(const Vec3& pos, const Vec3& vel, double m, double q)
    : position(pos), half_velocity(vel), mass(m), charge(q) {}

void Particle::rk4_core(Vec3 (*bField)(double, double, double, double),
                        Vec3 (*eField)(double, double, double, double),
                        double dt,
                        std::function<Vec3(const Vec3&, const Vec3&)> get_acc)
{
    // Runge-Kutta 4th order integration
    Vec3 k1 = half_velocity;
    Vec3 l1 = get_acc(position, half_velocity);

    Vec3 k2 = half_velocity + 0.5 * dt * l1;
    Vec3 l2 = get_acc(position + 0.5 * dt * k1, k2);

    Vec3 k3 = half_velocity + 0.5 * dt * l2;
    Vec3 l3 = get_acc(position + 0.5 * dt * k2, k3);

    Vec3 k4 = half_velocity + dt * l3;
    Vec3 l4 = get_acc(position + dt * k3, k4);

    position = position + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
    half_velocity = half_velocity + (dt / 6.0) * (l1 + 2.0 * l2 + 2.0 * l3 + l4);

    timepoint += dt;

    trajectory.push_back(position);
    velocities.push_back(half_velocity);
    times.push_back(times.empty() ? 0.0 : timepoint);
}

void Particle::step_rk4(Vec3 (*bField)(double, double, double, double),
                        Vec3 (*eField)(double, double, double, double),
                        double dt)
{
    auto get_acc = [&](const Vec3& pos, const Vec3& vel) -> Vec3 {
        Vec3 B = bField(pos[0], pos[1], pos[2], timepoint);
        Vec3 E = eField(pos[0], pos[1], pos[2], timepoint);
        Vec3 vxB = cross(vel, B);
        return {
            charge * (vxB[0] + E[0]) / mass,
            charge * (vxB[1] + E[1]) / mass,
            charge * (vxB[2] + E[2]) / mass
        };
    };

    rk4_core(bField, eField, dt, get_acc);
}

void Particle::step_rk4_rel(Vec3 (*bField)(double, double, double, double),
                            Vec3 (*eField)(double, double, double, double),
                            double dt)
{
    auto gamma = [](const Vec3& v) {
        return 1.0 / std::sqrt(1.0 - (norm(v) * norm(v)) / (c * c));
    };

    auto get_acc = [&](const Vec3& pos, const Vec3& vel) -> Vec3 {
        Vec3 B = bField(pos[0], pos[1], pos[2], timepoint);
        Vec3 E = eField(pos[0], pos[1], pos[2], timepoint);
        Vec3 vxB = cross(vel, B);
        double g = gamma(vel);
        return charge / mass / g * (vxB + E - dot(vel, E) * vel / c / c);
    };
    
    rk4_core(bField, eField, dt, get_acc);
}

void Particle::step_boris(Vec3 (*bField)(double, double, double, double),
                           Vec3 (*eField)(double, double, double, double),
                           double dt)
{
    Vec3 B = bField(position[0], position[1], position[2], timepoint);
    Vec3 E = eField(position[0], position[1], position[2], timepoint);

    double gamma_nhalf = 1.0 / std::sqrt(1.0 - (norm(half_velocity) * norm(half_velocity)) / (c * c));
    Vec3 u_nhalf = half_velocity * gamma_nhalf;
    
    // First half electric impulse
    Vec3 u_minus = u_nhalf + (charge / (2.0 * mass)) * E * dt;

    double gamma_n = std::sqrt(1.0 + (norm(u_minus) * norm(u_minus)) / (c * c));

    // Magnetic impulse
    Vec3 t = charge * B * dt / (2.0 * mass * gamma_n);
    Vec3 s = 2 * t / (1 + norm(t) * norm(t));
    Vec3 u_prime = u_minus + cross(u_minus, t);
    Vec3 u_plus = u_minus + cross(u_prime, s);

    // Second half electric impulse
    Vec3 u_phalf = u_plus + (charge / (2.0 * mass)) * E * dt;

    double gamma_phalf = std::sqrt(1.0 + (norm(u_phalf) * norm(u_phalf)) / (c * c));

    // Update half_velocity, position, and time
    half_velocity = u_phalf / gamma_phalf;
    position = position + half_velocity * dt;
    timepoint = timepoint + dt;

    // Store trajectory, velocities, energies, and times
    trajectory.push_back(position);
    velocities.push_back(half_velocity);
    momentums.push_back(momentum());
    energies.push_back(energy());
    times.push_back(times.empty() ? 0.0 : timepoint);

    // Print fields
    // std::cout << "B: " << B[0] << ", " << B[1] << ", " << B[2] << "\n";
    // std::cout << "E: " << E[0] << ", " << E[1] << ", " << E[2] << "\n";
}

Vec3 Particle::momentum() const
{
    return mass * half_velocity / std::sqrt(1.0 - (norm(half_velocity) * norm(half_velocity)) / (c * c));
}

double Particle::energy() const
{
    double gamma = 1.0 / std::sqrt(1.0 - (norm(half_velocity) * norm(half_velocity)) / (c * c));
    return mass * c * c * gamma;
}
