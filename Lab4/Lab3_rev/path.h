#ifndef PATH_H
#define PATH_H

#include <string>

#include "point.h"

class Path {
public:
    Path();
    Path(Point **points, size_t count);

    ~Path();
    
    void append(Point *point);
    
    Point* operator[](const size_t index);
    size_t count() const;

    Point* first() const;
    Point* last() const;

    std::wstring print() const;

private:
    void insert(Point *point);
    void grow();

private:
    size_t size_;
    size_t count_;
    Point **points_;
};

#endif // !PATH_H