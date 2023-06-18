#pragma once
#include <iostream>

namespace calc {
    template<typename T>
    class List {
    private:
        class Node {
        public:
            Node(const T &v, Node *n = nullptr) : value(v), next(n) {};
            T value;
            Node *next;
        };
    public:
        List();
        ~List();
        List(const std::initializer_list<T> &il);
        List(const List &other);
        List(List &&other) noexcept;

        void add(T value, int pos);
        void addFront(T value);
        void addBack(T value);
        T pop(int pos);
        T popFront();
        T popBack();
        void remove(T value);
        void removeAll(T value);
        int index(T value) const;
        int count(T value) const;
        int length() const;
        bool isEmpty() const;

        T &operator[](int index) const;

        friend std::ostream &operator<<(std::ostream &output, const List<T> &list) {
            std::string result = "[";
            if (list.isEmpty()) {
                result += "]";
            } else {
                int l = list.length();
                for (int i = 0; i < l; i++) {
                    result += std::to_string(list[i]);
                    if (i != l - 1)
                        result += ", ";
                    else
                        result += "]";
                }
            }
            output << result;
            return output;
        }

    public:
        Node *front;
    };

    template<typename T, typename Compare>
    bool isSorted(List<T> &list, Compare compare);

    template<typename T, typename Compare>
    void sort(List<T> &list, Compare compare);
}



