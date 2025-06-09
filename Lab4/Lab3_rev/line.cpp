#include "line.h"

#include <math.h>

Line::Line(Point* from, Point* to) 
    : from_(from), to_(to), ownsFrom_(false), ownsTo_(false) {}

Line::Line(double x1, double y1, double x2, double y2) : ownsFrom_(true), ownsTo_(true) {
    from_ = new Point(x1, y1);
    to_ = new Point(x2, y2);
}

Line::~Line() {
    if (ownsFrom_) delete from_;
    if (ownsTo_) delete to_;
}

Point* Line::from() const {
    return from_;
}

Point* Line::to() const {
    return to_;
}

void Line::set_from(Point* from) {
    from_ = from;
}

void Line::set_to(Point* to) {
    to_ = to;
}

#define sqr(x) (x) * (x)
double Line::length() const {
    return sqrt(sqr(from_->x() - to_->x()) + sqr(from_->y() - to_->y()));
}
#undef sqr

size_t Line::truncated_length() const {
    return static_cast<size_t>(length());
}

std::wstring Line::print() const {
    return L"Линия от " + from_->print() + L" до " + to_->print();
}
