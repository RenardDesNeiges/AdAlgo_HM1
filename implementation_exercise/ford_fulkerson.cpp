#include <vector>
#include <queue> 
#include <iostream>
#include <limits>
#include <string>

using namespace std;


int inf = std::numeric_limits<int>::max();

std::vector<long> splitStringByChar(std::string str, char split)
{
    std::string nb = "";
    std::vector<long> out;

    for (auto x : str) 
    {
        if (x == split)
        {
            out.push_back(std::stol(nb));
            nb = "";
        }
        else {
            nb = nb + x;
        }
    }
    out.push_back(std::stol(nb));
    return out;
}

int bfs(int s, int t, vector<int>& parent, vector<vector<int>> capacity, vector<vector<int> > adj, int n) {
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;
    queue<pair<int, int> > q;
    q.push({s, inf});

    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (parent[next] == -1 && capacity[cur][next]) {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                    return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0;
}

int maxflow(int s, int t, vector<vector<int> > capacity, vector<vector<int> > adj, int n) {
    int flow = 0;
    vector<int> parent(n);
    int new_flow;

    while (new_flow = bfs(s, t, parent, capacity, adj, n)) {
        flow += new_flow;
        int cur = t;
        while (cur != s) {
            int prev = parent[cur];
            capacity[prev][cur] -= new_flow;
            capacity[cur][prev] += new_flow;
            cur = prev;
        }
    }

    return flow;
}

int main() {
    int n;
    vector<vector<int> > capacity;
    vector<vector<int> > adj;

    // get the numbers of bridges and ports
    string line;
    getline(std::cin, line);
    vector<long> splitLine = splitStringByChar(line,' ');
    long nPorts = splitLine.at(0);
    long nBridges = splitLine.at(1);

    //now we know the size of the adjacency matrix (n_ports*2 + 1) x (n_ports*2 + 1)


    cout << nPorts << ";" << nBridges << endl;

    //
}