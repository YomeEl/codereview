#include "path.h"

Path::Path() : size_(1), count_(0) {
    points_ = new Point*[1];
}

Path::Path(Point **points, size_t count) {
    size_ = count;
    points_ = new Point*[size_];
    count_ = count;
    for (size_t i = 0; i < count; i++) {
        points_[i] = points[i];
    }
}

Path::~Path() {
    delete[] points_;
}

void Path::append(Point *point) {
    insert(point);
}

Point *Path::operator[](const size_t index) {
    if (index >= count_) return nullptr;
    return points_[index];
}

size_t Path::count() const {
    return count_;
}

Point *Path::first() const {
    if (count_ == 0) return nullptr;
    return points_[0];
}

Point *Path::last() const {
    if (count_ == 0) return nullptr;
    return points_[count_ - 1];
}

std::wstring Path::print() const {
    std::wstring result = L"[";
    for (size_t i = 0; i < count_; i++)
    {
        result += points_[i]->print() + L", ";
    }

    return result.substr(0, result.length() - 2) + L"]";
}

void Path::insert(Point *point) {
    if (count_ == size_) grow();
    points_[count_++] = point;
}

void Path::grow() {
    Point ** new_array = new Point*[size_ * 2];
    for (size_t i = 0; i < count_; i++)
    {
        new_array[i] = points_[i];
    }
    delete[] points_;
    points_ = new_array;
    size_ *= 2;
}
