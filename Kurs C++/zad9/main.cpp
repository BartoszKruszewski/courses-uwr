#include <iostream>
#include "List.hpp"
#include "List.cpp"
#include "Stack.hpp"
#include "Queue.hpp"

void printTestResult(const std::string &testName, const std::string &params, const std::string &result,
                     const std::string &expected) {
    std::cout << testName << "(" << params << ")\t";
    std::cout << "Result: " << result << "\t";
    std::cout << "Expected: " << expected << std::endl;
}

int main() {

    calc::List<int> list;
    printTestResult("isEmpty", "", list.isEmpty() ? "true" : "false", "true");
    printTestResult("length", "", std::to_string(list.length()), "0");

    list.addFront(1);
    printTestResult("addFront", "1", "", "");
    printTestResult("isEmpty", "", list.isEmpty() ? "true" : "false", "false");
    printTestResult("length", "", std::to_string(list.length()), "1");
    printTestResult("operator[]", "0", std::to_string(list[0]), "1");

    list.addBack(2);
    printTestResult("addBack", "2", "", "");
    printTestResult("length", "", std::to_string(list.length()), "2");
    printTestResult("operator[]", "1", std::to_string(list[1]), "2");

    list.add(3, 1);
    printTestResult("add", "3, 1", "", "");
    printTestResult("length", "", std::to_string(list.length()), "3");
    printTestResult("operator[]", "1", std::to_string(list[1]), "3");

    int pop1 = list.pop(1);
    printTestResult("length", "", std::to_string(list.length()), "2");

    int pop2 = list.popFront();
    printTestResult("popFront", "", std::to_string(pop2), "1");
    printTestResult("length", "", std::to_string(list.length()), "1");

    int pop3 = list.popBack();
    printTestResult("popBack", "", std::to_string(pop3), "2");
    printTestResult("length", "", std::to_string(list.length()), "0");

    list.addFront(1);
    list.addBack(2);
    list.addFront(3);
    list.addBack(2);
    list.addBack(4);
    printTestResult("remove", "2", "", "");
    list.remove(2);
    printTestResult("count", "2", std::to_string(list.count(2)), "0");

    list.addBack(3);
    list.addBack(4);
    list.addBack(4);
    list.addBack(5);
    printTestResult("removeAll", "4", "", "");
    list.removeAll(4);

    printTestResult("index", "3", std::to_string(list.index(3)), "0");
    printTestResult("index", "5", std::to_string(list.index(5)), "4");
}
