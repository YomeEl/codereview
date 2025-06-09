#include "demos.h"

#include <iostream>
#include <array>
#include <string>

#include "point.h"
#include "line.h"
#include "path.h"

namespace demos {

#ifdef MANUAL_MODE
Point read_point(std::wstring hint) {
    double x, y; 
    std::wcout << hint << L", x: ";
    std::wcin >> x;
    std::wcout << hint << L", y: ";
    std::wcin >> y;
    return Point(x, y);
}
#endif

void point_demo() {
#ifdef MANUAL_MODE
    Point a = read_point(L"Точка A");
    Point b = read_point(L"Точка B");
    Point c = read_point(L"Точка C");
#else
    Point a(1, 1);
    Point b(2, 2);
    Point c(3, 3);
#endif
    std::wcout 
        << L"A: " << a.print() 
        << L"\nB: " << b.print() 
        << L"\nC: " << c.print() 
        << std::endl;
}

void line_demo() {
#ifdef MANUAL_MODE
    Point first_line_from = read_point(L"Начало первого отрезка");
    Point first_line_to = read_point(L"Конец первого отрезка");
    Point second_line_from = read_point(L"Начало второго отрезка");
    Point second_line_to = read_point(L"Конец второго отрезка");
#else
    Point first_line_from(1, 3);
    Point first_line_to(23, 8);
    Point second_line_from(5, 10);
    Point second_line_to(25, 10);
#endif

    Line first_line(&first_line_from, &first_line_to);
    Line second_line(&second_line_from, &second_line_to);
    Line third_line(&first_line_from, &second_line_to);

    std::wcout << L"Начальное состояние линий" << std::endl;

    std::wcout 
        << L"\t1: " << first_line.print() 
        << L"\n\t2: " << second_line.print() 
        << L"\n\t3: " << third_line.print() << std::endl;

    std::wcout << L"Сдвигаем начало первой линии в точку (2, 4)" << std::endl;
    first_line.from()->set_x(2);
    first_line.from()->set_y(4);

    std::wcout << L"Сдвигаем конец второй линии в точку (30, 15)" << std::endl;
    second_line.to()->set_x(30);
    second_line.to()->set_y(15);

    std::wcout 
        << L"\t1: " << first_line.print() 
        << L"\n\t2: " << second_line.print() 
        << L"\n\t3: " << third_line.print() << std::endl;

    std::wcout << L"Сдвигаем конец первой линии в точку (5, 5)" << std::endl;
    first_line.to()->set_x(5);
    first_line.to()->set_y(5);

    std::wcout 
        << L"\t1: " << first_line.print() 
        << L"\n\t2: " << second_line.print() 
        << L"\n\t3: " << third_line.print() << std::endl;
}

void path_demo() {
#ifdef MANUAL_MODE
    Point path_from = read_point(L"Начало первой ломаной");
    Point path_to = read_point(L"Конец первой ломаной");
    
    Point first_path_center = read_point(L"Средняя точка первой ломаной");
    Point second_path_center_first = 
        read_point(L"Первая средняя точка второй ломаной");
    Point second_path_center_second = 
        read_point(L"Вторая средняя точка второй ломаной");
#else
    Point path_from(1, 5);
    Point path_to(5, 3);
    
    Point first_path_center(2, 8);
    Point second_path_center_first(2, -5);
    Point second_path_center_second(4, -8);
#endif

    Path path1;
    path1.append(&path_from);
    path1.append(&first_path_center);
    path1.append(&path_to);

    Path path2;
    path2.append(&path_from);
    path2.append(&second_path_center_first);
    path2.append(&second_path_center_second);
    path2.append(&path_to);

    std::wcout << L"Начальное состояние ломаных\n";
    std::wcout << 
        L"\t1: " << path1.print() << L"\n\t2: " << path2.print() << L"\n";

    std::wcout << 
        L"Сдвигаем начало первой ломаной в точку {0, 1}\n";
    path1.first()->set_x(0);
    path1.first()->set_y(1);
    std::wcout << 
        L"\t1: " << path1.print() << L"\n\t2: " << path2.print() << L"\n";
}

void create_point_demo() {
    Point a(3, 5);
    std::wcout << a.print() << std::endl;
    Point b(25, 6);
    std::wcout << b.print() << std::endl;
    Point c(7, 8);
    std::wcout << c.print() << std::endl;
}

void create_line_demo() {
#ifdef MANUAL_MODE
    Point first_line_from = read_point(L"Начало первого отрезка");
    Point first_line_to = read_point(L"Конец первого отрезка");
    Point second_line_from = read_point(L"Начало второго отрезка");
    Point second_line_to = read_point(L"Конец второго отрезка");

    Line line1(
        first_line_from.x(), first_line_from.y(), 
        first_line_to.x(), first_line_to.y()
    );
    Line line2(
        second_line_from.x(), second_line_from.y(), 
        second_line_to.x(), second_line_to.y()
    );
#else
    Line line1(1, 3, 23, 8);
    Line line2(5, 10, 25, 10);
#endif
    Line line3(line1.from(), line2.to());

    std::wcout << L"Начальное состояние линий" << std::endl;

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;

    std::wcout << L"Сдвигаем начало первой линии в точку (2, 4)" << std::endl;
    line1.from()->set_x(2);
    line1.from()->set_y(4);

    std::wcout << L"Сдвигаем конец второй линии в точку (30, 15)" << std::endl;
    line2.to()->set_x(30);
    line2.to()->set_y(15);

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;

    std::wcout << L"Сдвигаем конец первой линии в точку (5, 5)" << std::endl;
    line1.to()->set_x(5);
    line1.to()->set_y(5);

    std::wcout 
        << L"\t1: " << line1.print() 
        << L"\n\t2: " << line2.print() 
        << L"\n\t3: " << line3.print() << std::endl;
}


void line_length_demo() {
#ifdef MANUAL_MODE
    Point lineFrom = read_point(L"Начало отрезка");
    Point lineTo = read_point(L"Конец отрезка");
    Line line(lineFrom.x(), lineFrom.y(), lineTo.x(), lineTo.y());
#else
    Line line(1,1,10,15);
#endif
    std::wcout << line.print() << std::endl;
    std::wcout << L"Длина линии: " << line.length() << std::endl;
    std::wcout 
        << L"Целая часть длины линии: " << line.truncated_length() << std::endl;
}

} // namespace demos
