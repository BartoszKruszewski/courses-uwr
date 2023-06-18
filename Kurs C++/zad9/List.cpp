#include "List.hpp"

template <typename T, typename Compare>
bool calc::isSorted(List<T>& list, Compare compare) {
    if (list.isEmpty() || list.length() == 1)
        return true;
    else {
        for (int i = 0; i < list.length() - 1; i++) {
            if (!compare(list[i], list[i + 1]))
                return false;
        }
        return true;
    }
}

template <typename T>
void swap(T* a, T* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

template <typename T, typename Compare>
int partition(calc::List<T>& list, int low, int high, Compare compare) {
    int pivot = list[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (compare(list[j], pivot)) {
            i++;
            swap(&list[i], &list[j]);
        }
    }
    swap(&list[i + 1], &list[high]);
    return (i + 1);
}

template <typename T, typename Compare>
void quicksort(calc::List<T>& list, int low, int high, Compare compare) {
    if (low < high) {
        int pivot = partition(list, low, high, compare);
        quicksort(list, low, pivot - 1, compare);
        quicksort(list, pivot + 1, high, compare);
    }
}

template <typename T, typename Compare>
void calc::sort(List<T>& list, Compare compare) {
    quicksort(list, 0, list.length() - 1, compare);
}

template <typename T>
bool calc::List<T>::isEmpty() const {
    return front == nullptr;
}

template <typename T>
int calc::List<T>::length() const {
    if (isEmpty()) {
        return 0;
    }
    int i = 1;
    Node *actualNode = front;
    while (actualNode->next != nullptr) {
        i++;
        actualNode = actualNode->next;
    }
    return i;
}

template <typename T>
int calc::List<T>::count(T value) const {
    int i = 0;
    Node *actualNode = front;
    while (actualNode->next != nullptr) {
        if (actualNode->value == value)
            i++;
        actualNode = actualNode->next;
    }
    if (actualNode->value == value)
        i++;
    return i;
}

template <typename T>
int calc::List<T>::index(T value) const {
    if (front->value == value)
        return 0;
    int i = 1;
    Node *actualNode = front;
    while (actualNode->next != nullptr && actualNode->next->value != value) {
        actualNode = actualNode->next;
        i++;
    }
    if (i == length())
        return -1;
    return i;
}

template <typename T>
void calc::List<T>::removeAll(T value) {
    Node *actualNode = front;
    while (actualNode->next != nullptr) {
        while (actualNode->next != nullptr && actualNode->next->value != value) {
            actualNode = actualNode->next;
        }
        if (actualNode->next != nullptr)
            actualNode->next = actualNode->next->next;
    }
}

template <typename T>
void calc::List<T>::remove(T value) {
    Node *actualNode = front;
    while (actualNode->next != nullptr && actualNode->next->value != value) {
        actualNode = actualNode->next;
    }
    if (actualNode->next != nullptr)
        actualNode->next = actualNode->next->next;
}

template <typename T>
T calc::List<T>::popBack() {
    if (isEmpty())
        throw std::range_error("Nie można usunąć ostatniego elementu z pustej listy!");
    Node *actualNode = front;
    if (actualNode->next == nullptr) {
        T returnValue = actualNode->value;
        front = nullptr;
        return returnValue;
    }
    while (actualNode->next->next != nullptr) {
        actualNode = actualNode->next;
    }
    T returnValue = actualNode->next->value;
    actualNode->next = nullptr;
    return returnValue;
}

template <typename T>
T calc::List<T>::popFront() {
    if (isEmpty())
        throw std::range_error("Nie można usunąć ostatniego elementu z pustej listy!");
    T returnValue = front->value;
    front = front->next;
    return returnValue;
}

template <typename T>
T calc::List<T>::pop(int pos) {
    if (isEmpty()) {
        throw std::range_error("Nie można usunąć elementu z pustej listy!");
    } else if (pos == 0) {
        return popFront();
    } else {
        if (pos >= length()) {
            throw std::range_error("Nie mozna usunac elementu z listy z podanej pozycji!");
        }
        int i = 1;
        Node *actualNode = front;
        while (i != pos) {
            actualNode = actualNode->next;
            i++;
        }
        T returnValue = actualNode->value;
        actualNode->next = actualNode->next->next;
        return returnValue;
    }
}

template <typename T>
void calc::List<T>::addBack(T value) {
    if (isEmpty()) {
        front = new Node(value);
    } else {
        Node *actualNode = front;
        while (actualNode->next != nullptr) {
            actualNode = actualNode->next;
        }
        actualNode->next = new Node(value);
    }
}

template <typename T>
void calc::List<T>::addFront(T value) {

    Node *newNode = new Node(value);
    if (!isEmpty()) {
        newNode->next = front;
    }
    front = newNode;
}

template <typename T>
void calc::List<T>::add(T value, int pos) {
    if (pos == 0)
        addFront(value);
    else {
        if (pos > length()) {
            throw std::range_error("Nie mozna dodac elementu do listy na podana pozycje!");
        }
        Node *newNode = new Node(value);
        int i = 1;
        Node *actualNode = front;
        while (i != pos) {
            actualNode = actualNode->next;
            i++;
        }
        newNode->next = actualNode->next;
        actualNode->next = newNode;
    }
}

template <typename T>
calc::List<T>::List(List<T> &&other) noexcept {
    front = other.front;
    other.front = nullptr;
}

template <typename T>
calc::List<T>::List(const std::initializer_list<T> &il) : List() {
    for (T e: il) {
        addBack(e);
    }
}

template <typename T>
calc::List<T>::List(const List<T> &other) : List() {
    Node* actualNode = other.front;
    while (actualNode->next != nullptr) {
        addBack(actualNode->value);
        actualNode = actualNode->next;
    }
}

template <typename T>
calc::List<T>::List() {
    front = nullptr;
}

template <typename T>
calc::List<T>::~List() {
    while (front) {
        Node *next = front->next;
        delete front;
        front = next;
    }
}

template <typename T>
T &calc::List<T>::operator[](int idx) const {
    if (isEmpty()) {
        throw std::range_error("Lista jest pusta!");
    } else if (idx == 0) {
        return front->value;
    } else {
        if (idx >= length()) {
            throw std::range_error("Nie ma na liscie elementu o podanej pozycji!");
        }
        int i = 0;
        Node *actualNode = front;
        while (i != idx) {
            actualNode = actualNode->next;
            i++;
        }
        return actualNode->value;
    }
}