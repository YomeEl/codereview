#ifndef LINE_H
#define LINE_H

#include <string>

#include "point.h"

class Line {
public:
    Line(Point* from, Point* to);
    Line(double x1, double y1, double x2, double y2);

    ~Line();

    Point* from() const;
    Point* to() const;

    void set_from(Point* from);
    void set_to(Point* to);

    double length() const;
    size_t truncated_length() const; 

    std::wstring print() const;

private:
    Point* from_;
    Point* to_;

    bool ownsFrom_;
    bool ownsTo_;
};

#endif // !LINE_H