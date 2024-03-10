#include <bits/stdc++.h>
using namespace std;

vector<int> dijkstra(int u, vector<pair<int, int>> adj[], int n){
    vector<int> dist(n+1, -1);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, u});
    dist[u] = 0;
    while(!pq.empty()){
        int v = pq.top().second;
        int c = pq.top().first;
        pq.pop();
        for(auto e : adj[v]){
            int f = e.first;
            if(dist[f] == -1 || dist[f] > c + e.second){
                dist[f] = c + e.second;
                pq.push({dist[f], f}); 
            }
        }
    }
    return dist;
}

int main(){
    int n, m;
    cin >> n >> m;
    int u, v;
    cin >> u >> v;
    vector<pair<int, int>> adj[n+1];
    for(int i = 0; i < m; i++){
        int u, v, c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    vector<int> dist = dijkstra(v, adj, n);
    
    queue<int> q;
    q.push(u);
    int wynik = 0;
    while(!q.empty()){
        int k = q.front();
        q.pop();
        if(v == k){ 
            wynik++;
        }
        for(auto e : adj[k]){
            if(dist[e.first] < dist[k]){
                q.push(e.first);
            }
        }
    }
    cout << wynik << endl;

}