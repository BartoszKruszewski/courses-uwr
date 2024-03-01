#include <iostream>

using namespace std;

const int MAX_N = 1000007;

int mothers[MAX_N][2];
int starts[MAX_N];
int pre[MAX_N];
int post[MAX_N];
int timer = 1;

void swap(int arr[][2], int a, int b) {
    int temp1 = arr[a][0];
    int temp2 = arr[a][1];
    arr[a][0] = arr[b][0];
    arr[a][1] = arr[b][1];
    arr[b][0] = temp1;
    arr[b][1] = temp2;
}

void heapify(int arr[][2], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left][0] > arr[largest][0])
        largest = left;

    if (right < n && arr[right][0] > arr[largest][0])
        largest = right;

    if (largest != i) {
        swap(arr, i, largest);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[][2], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        swap(arr, 0, i);
        heapify(arr, i, 0);
    }
}

void dfs() {
    int s = 1;
    int lastStack = 0;
    int stack[MAX_N];
    stack[lastStack] = s;
    while (lastStack != -1) {
        s = stack[lastStack];
        if (pre[s] == 0) {
            pre[s] = timer++;
            int i = starts[s];
            while (mothers[i][0] == s) {
                int kid = mothers[i++][1];
                if (pre[kid] == 0) stack[++lastStack] = kid;
            }
        } else if (post[s] == 0) {
            lastStack--;
            post[s] = timer++;
        } 
    }
}

void updateStarts(int n) {
    int last = mothers[0][0];
    starts[mothers[0][0]] = 0;
    for (int i = 0; i < n; i++) {
        int e = mothers[i][0];
        if (e != last) {
            starts[e] = i;
            last = e;
        }
    }
}

bool check(int a, int b) {
    return pre[a] < pre[b] && post[a] > post[b];
}

int main() {
    int n, q;
    cin >> n >> q;
    
    for (int i = 1; i < n; i++) {
        cin >> mothers[i - 1][0];
        mothers[i - 1][1] = i + 1;
    }

    heapSort(mothers, n - 1);
    updateStarts(n - 1);
    dfs();

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << (check(a,b) ? "TAK" : "NIE") << endl;
    }
    return 0;
}
