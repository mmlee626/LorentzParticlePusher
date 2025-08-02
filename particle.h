#ifndef PARTICLE_H
#define PARTICLE_H

#include "vec3.h"
#include <vector>
#include <functional>

class Particle
{
public:
    Vec3 position;      // Particle position at n = i
    Vec3 half_velocity; // Particle velocity at n = i - 0.5
    double timepoint;   // Time at n = i
    double mass;
    double charge;
    std::vector<Vec3> trajectory;
    std::vector<Vec3> velocities;
    std::vector<Vec3> momentums;
    std::vector<double> energies;
    std::vector<double> times;

    Particle(const Vec3& pos, const Vec3& vel, double m, double q);

    void step_rk4(Vec3 (*bField)(double, double, double, double),
              Vec3 (*eField)(double, double, double, double),
              double dt);
    void step_rk4_rel(Vec3 (*bField)(double, double, double, double),
                    Vec3 (*eField)(double, double, double, double),
                    double dt);
    void step_boris(Vec3 (*bField)(double, double, double, double),
              Vec3 (*eField)(double, double, double, double),
              double dt);
    
    Vec3 momentum() const;
    double energy() const;

protected:
    void rk4_core(Vec3 (*bField)(double, double, double, double),
              Vec3 (*eField)(double, double, double, double),
              double dt,
              std::function<Vec3(const Vec3&, const Vec3&)> get_acc);
};

#endif
