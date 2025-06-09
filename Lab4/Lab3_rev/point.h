#ifndef POINT_H
#define POINT_H

#include <string>

class Point {
public:
    Point();
    Point(const Point &other);
    Point(double x, double y);

    double x() const;
    double y() const;

    void set_x(double x);
    void set_y(double y);
    
    std::wstring print() const;
    
private: 
    double x_;
    double y_;
};

#endif // !POINT_H
