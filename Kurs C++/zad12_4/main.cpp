#include <iostream>
#include <vector>
#include <functional>
#include "Triangle.hpp"

int main() {
    std::vector<Triangle> triangles = {
            Triangle(3.0, 4.0, 5.0, "Triangle 1"),
            Triangle(2.0, 2.0, 2.0, "Triangle 2"),
            Triangle(5.0, 12.0, 13.0, "Triangle 3"),
            Triangle(8.0, 15.0, 17.0, "Triangle 4"),
            Triangle(7.0, 7.0, 9.0, "Triangle 5"),
            Triangle(9.0, 40.0, 41.0, "Triangle 6"),
            Triangle(6.0, 8.0, 10.0, "Triangle 7"),
            Triangle(5.0, 5.0, 8.0, "Triangle 8"),
            Triangle(12.0, 16.0, 20.0, "Triangle 9"),
            Triangle(1000.0, 2000.0, 1001.0, "Triangle 10")
    };

    std::sort(triangles.begin(), triangles.end(), [](const Triangle& t1, const Triangle& t2) {
        return t1.perimeter() < t2.perimeter();
    });

    std::cout << "Sorted triangles by perimeter:" << std::endl;
    for (const auto& triangle : triangles) {
        std::cout << triangle << ", Perimeter: " << triangle.perimeter() << std::endl;
    }

    auto minMaxArea = std::minmax_element(triangles.begin(), triangles.end(), [](const Triangle& t1, const Triangle& t2) {
        return t1.area() < t2.area();
    });

    std::cout << "Triangle with minimum area: " << *minMaxArea.first << ", Area: " << (*minMaxArea.first).area() << std::endl;
    std::cout << "Triangle with maximum area: " << *minMaxArea.second << ", Area: " << (*minMaxArea.second).area() << std::endl;

    std::cout << "Acute triangles:" << std::endl;
    std::for_each(triangles.begin(), triangles.end(), [](const Triangle& triangle) {
        if (triangle.isAcuteTriangle()) {
            std::cout << triangle << std::endl;
        }
    });

    return 0;
}
