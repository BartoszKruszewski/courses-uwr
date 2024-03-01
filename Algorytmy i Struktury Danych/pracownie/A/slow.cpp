#include <iostream>
#include <vector>
#include <map>

using namespace std;

map<int, vector<int> > mothers;
map<int, int> pre;
map<int, int> post;
int timer = 1;

void dfs(int s) {
    if (pre[s] == 0) {
        pre[s] = timer++;
        for (int v : mothers[s]) dfs(v);
        post[s] = timer++;
    }
}

bool check(int a, int b) {
    return pre[a] < pre[b] && post[a] > post[b];
}

int getRoot() {
    vector<int> roots;
    for (const auto& pair : mothers) roots.push_back(pair.first);
    for (int root : roots) {
        for (int v : mothers[root]) {
            if (v == root) 
                break;
            return root;
        }  
    }
    return -1;
}

int main() {
    int n, q;
    cin >> n >> q;
    
    for (int i = 1; i < n; i++) {
        int mother;
        cin >> mother;
        mothers[mother].push_back(i + 1);
    }
    
    int root = getRoot();
    if (root == -1) return 0;
    else dfs(root);

    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << (check(a,b) ? "TAK" : "NIE") << endl;
    }
    return 0;
}

