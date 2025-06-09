#ifndef DEMOS_H
#define DEMOS_H

#include <string>

#include "point.h"

#define MANUAL_MODE

namespace demos {
#ifdef MANUAL_MODE
    Point read_point(std::wstring hint);
#endif
    void point_demo();
    void line_demo();
    void path_demo();
    void create_point_demo();
    void create_line_demo();
    void line_length_demo();
} // namespace demos

#endif // !DEMOS_H