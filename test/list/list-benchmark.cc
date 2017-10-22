#include <iostream>
#include <random>
#include <list>
#include <vector>
#include <queue>

std::default_random_engine myRandom(10203);

const int n = 100000;
const int m = 3000000;

const int limitN = n + 5;

struct Edge {
	int v, w;
	constexpr Edge() : v(0), w(0) {}
	Edge(const int &_v, const int &_w) : v(_v), w(_w) {}
	Edge(const Edge &other) : v(other.v), w(other.w) {}
};

std::list<Edge> to[limitN];
std::queue<int> que;
bool inQueue[limitN] = {0};
int dist[limitN] = {0};

void ConstructGraph()
{
	std::uniform_int_distribution<int> vertex(1, n);
	std::uniform_int_distribution<int> weight(5, 1000);
	for (int i = 0; i < m; ++i) {
		int u = vertex(myRandom);
		int v;
		do {
			v = vertex(myRandom);
		} while (u == v);
		int w = weight(myRandom);
		to[u].push_back(Edge(v, w));
	}
}

void RemoveEdges()
{
	std::uniform_int_distribution<int> vertex(1, n);
	for (int i = 0; i < 1500000; ++i) {
		int u;
		do {
			u = vertex(myRandom);
		} while (to[u].size() == 0);

		std::uniform_int_distribution<int> which(0, to[u].size() - 1);
		int k = which(myRandom);
		std::list<Edge>::iterator iter = to[u].begin();
		for (int j = 0; j < k; ++j) {
			++iter;
		}
		to[u].erase(iter);
	}
}

void Spfa()
{
	std::fill(dist, dist + n + 1, ~0U >> 3);
	dist[1] = 0;
	inQueue[1] = true;
	que.push(1);
	while (!que.empty()) {
		int u = que.front();
		inQueue[u] = false;
		que.pop();
		for (std::list<Edge>::iterator it = to[u].begin(); it != to[u].end(); ++it) {
			if (dist[u] + it->w < dist[it->v]) {
				dist[it->v] = dist[u] + it->w;
				if (!inQueue[it->v]) {
					que.push(it->v);
					inQueue[it->v] = true;
				}
			}
		}
	}
}

int main()
{
	ConstructGraph();
	RemoveEdges();
	Spfa();
	for (int i = 1; i <= n; ++i) {
		std::cout << "dist[" << i << "]=" << dist[i] << std::endl;
	}
	return 0;
}