#include <iostream>
#include <string>
#include <map>

#include "demos.h"

enum class Task { 
    kPoint, kLine, kPath, kCreatePoint, kCreateLine, kLineLength, 
    kExit, kErrTask
};

std::map<Task, std::wstring> texts {
    { Task::kPoint, L"1\tТочка координат" },
    { Task::kLine, L"2\tПрямая" },
    { Task::kPath, L"3\tЛоманая" },
    { Task::kCreatePoint, L"4.1\tСоздаём точку" },
    { Task::kCreateLine, L"4.2\tСоздаём линию" },
    { Task::kLineLength, L"5\tДлина линии" }
};

Task select_task(const std::wstring selection) {
    if (selection == L"-1") return Task::kExit;
    for (const auto &pair : texts) {
        size_t tabIndex = pair.second.find(L"\t");
        if (pair.second.substr(0, tabIndex) == selection) return pair.first;
    }
    return Task::kErrTask;
}

std::wstring show_main_page() {
    std::wcout << L"Номер\tНазвание\n";
    for (const auto &pair : texts) {
        std::wcout << pair.second << std::endl;
    }
    std::wcout << L"Введите номер задачи или -1, чтобы выйти: ";
    std::wstring selection;
    std::wcin >> selection;
    return selection;
}

void run_demo(Task task) {
    switch (task) {
    case Task::kPoint: 
        demos::point_demo();
        break;
    case Task::kLine: 
        demos::line_demo();
        break;
    case Task::kPath: 
        demos::path_demo();
        break;
    case Task::kCreatePoint: 
        demos::create_point_demo();
        break;
    case Task::kCreateLine: 
        demos::create_line_demo();
        break;
    case Task::kLineLength: 
        demos::line_length_demo();
        break;
    default: 
        return;
    }
    system("pause");
}

int main() {
    system("chcp 1251");
    setlocale(LC_ALL, "ru-RU");

    while (true) {
        std::wstring selection = show_main_page();
        Task task = select_task(selection);
        if (task == Task::kExit) break;
        run_demo(task);
    }

    return 0;
}
