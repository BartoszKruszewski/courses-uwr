#include <iostream>
#include <float.h>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    Node(long long value) : key(value), left(nullptr), right(nullptr) {}
};

class BST {
private:
    Node* root;
    bool deleted;

    Node* insertRec(Node* root, long long key) {
        if (root == nullptr) return new Node(key);
        if (key < root->key) root->left = insertRec(root->left, key);
        else if (key > root->key) root->right = insertRec(root->right, key);
        return root;
    }

    Node* removeRec(Node* root, long long key) {
        if (root == nullptr) {
            return nullptr;
        }

        if (key < root->key) {
            root->left = removeRec(root->left, key);
        } else if (key > root->key) {
            root->right = removeRec(root->right, key);
        } else {
            deleted = true;
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = removeRec(root->right, temp->key);
        }
        return root;
    }

    int upperRec(Node* root, long long key) {
        if (root == nullptr) return ;
        if (key < root->key) root->left = insertRec(root->left, key);
        else if (key > root->key) root->right = insertRec(root->right, key);
        return root;
    }

    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current && current->left != nullptr) {
            current = current->left;
        }
        return current;
    }

    void inorderRec(Node* root) {
        if (root != nullptr) {
            inorderRec(root->left);
            cout << root->key << " ";
            inorderRec(root->right);
        }
    }

public:
    BST() : root(nullptr) {}

    void insert(long long key) {
        root = insertRec(root, key);
    }

    void inorder() {
        inorderRec(root);
    }

    void remove(long long key) {
        deleted = false;
        root = removeRec(root, key);
        if (deleted) cout << "OK" << endl;
        else cout << "BRAK" << endl;
    }
};

int main() {
    BST bst;

    int n;
    cin >> n;
    char op;
    long long x;
    for (int i = 0; i < n; i++) {
        cin >> op >> x;
        if (op == 'I') {
            bst.insert(x);
        }
        else if (op == 'D') {
            bst.remove(x);
        }
        else if (op == 'U') {
            
        }
        else if (op == 'L') {
            
        }
    }
    bst.inorder();

    return 0;
}
