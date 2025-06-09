#include "point.h"

Point::Point() : x_(0), y_(0) {}

Point::Point(const Point &other) {
    x_ = other.x_;
    y_ = other.y_;
}

Point::Point(double x, double y) : x_(x), y_(y) {}

double Point::x() const {
    return x_;
}
double Point::y() const {
    return y_;
}

void Point::set_x(double x) {
    x_ = x;
}
void Point::set_y(double y) {
    y_ = y;
}

std::wstring Point::print() const {
    return L"{" + std::to_wstring(x_) + L", " + std::to_wstring(y_) + L"}";
}