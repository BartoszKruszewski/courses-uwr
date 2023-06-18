#pragma once
#include "List.hpp"

namespace calc {
    template<typename T>
    class Queue : protected List<T> {
    public:
        void add(T value) { Queue<T>::addFront(value); };
        T pop() { return List<T>::popBack(); };
        using List<T>::isEmpty;
        using List<T>::length;

        friend std::ostream &operator<<(std::ostream &output, const Queue<T> &queue) {
            std::string result = "[";
            if (queue.isEmpty()) {
                result += "]";
            } else {
                int l = queue.length();
                for (int i = 0; i < l; i++) {
                    result += std::to_string(queue[i]);
                    if (i != l - 1)
                        result += ", ";
                    else
                        result += "]";
                }
            }
            output << result;
            return output;
        }
    };
}

