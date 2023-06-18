#pragma once
#include "List.hpp"

namespace calc {
    template<typename T>
    class Stack : protected List<T> {
    public:
        void add(T value) { List<T>::addBack(value); };
        T pop() { return List<T>::popBack(); };
        using List<T>::isEmpty;
        using List<T>::length;

        friend std::ostream &operator<<(std::ostream &output, const Stack<T> &stack) {
            std::string result = "[";
            if (stack.isEmpty()) {
                result += "]";
            } else {
                int l = stack.length();
                for (int i = 0; i < l; i++) {
                    result += std::to_string(stack[i]);
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

