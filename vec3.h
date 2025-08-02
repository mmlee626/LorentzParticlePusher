#ifndef VEC3_H
#define VEC3_H

#include <array>
#include <cmath>

using Vec3 = std::array<double, 3>;

inline Vec3 operator+(const Vec3& a, const Vec3& b) {
    return {a[0] + b[0], a[1] + b[1], a[2] + b[2]};
}

inline Vec3 operator-(const Vec3& a, const Vec3& b) {
    return {a[0] - b[0], a[1] - b[1], a[2] - b[2]};
}

inline Vec3 operator*(double scalar, const Vec3& v) {
    return {scalar * v[0], scalar * v[1], scalar * v[2]};
}

inline Vec3 operator*(const Vec3& v, double scalar) {
    return scalar * v;
}

inline Vec3 operator/(const Vec3& v, double scalar) {
    return {v[0] / scalar, v[1] / scalar, v[2] / scalar};
}

inline Vec3 cross(const Vec3& a, const Vec3& b) {
    return {
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    };
}

inline double dot(const Vec3& a, const Vec3& b) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

inline double norm(const Vec3& v) {
    return std::sqrt(dot(v, v));
}

#endif // VEC3_H