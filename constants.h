#ifndef CONSTANTS_H
#define CONSTANTS_H

// Unit system toggle
#define USE_NATURAL_UNITS   // Comment this line to use SI units

namespace constants {

constexpr double pi = 3.14159265358979323846; // Pi constant

#ifdef USE_NATURAL_UNITS
    constexpr double c = 1.0;          // Speed of light
    constexpr double e = 1.0;          // Elementary charge
    constexpr double B_conversion = 0.299792458; // Conversion factor for magnetic field in natural units
    constexpr double E_conversion = 1e-9; // Conversion factor for electric field in natural units
    constexpr double proton_mass = 0.938272; // Proton mass in GeV/c^2
    constexpr double electron_mass = 0.0005109989; // Electron mass in GeV/c^2
    constexpr double muon_mass = 0.1056583; // Muon mass in GeV/c^2
#else
    constexpr double c = 2.99792458e8;     // m/s
    constexpr double e = 1.602176634e-19; // C (elementary charge)
    constexpr double B_conversion = 1.0; // Conversion factor for magnetic field in SI units
    constexpr double E_conversion = 1.0; // Conversion factor for magnetic field in SI units
    constexpr double proton_mass = 1.6726219e-27; // kg
    constexpr double electron_mass = 9.10938356e-31; // kg
    constexpr double muon_mass = 1.8835316e-28; // kg
#endif

}

#endif // CONSTANTS_H