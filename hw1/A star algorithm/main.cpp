//A* algorithm
//f(n) = g(n) + h(n)

#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;

string cityName[20] = { "Arad", "Bucharest", "Craiova", "Dobreta",
						"Eforie", "Fagaras", "Giurgiu", "Hirsova",
						"Iasi", "Lugoj", "Mehadia", "Neamt",
						"Oradea", "Pitesti", "RimnicuVilcea", "Sibiu",
						"Timisoara", "Urziceni", "Vaslui", "Zerind " };
int strDist2Buch[20] = { 366, 0, 160, 242, 161,
						 178, 77, 151, 226, 244,
						 241, 234, 380, 98, 193,
						 253, 329, 80, 199, 374 };

struct city {
	int id;
	int parent_id;
	int f;
	int g;
	int h;
	city(int id, int g) {
		this->id = id;
		this->parent_id = -1;
		this->g = g;
		this->h = 0;
		this->f = 0;
	}
	bool operator< (const city & another) const {
		return this->f > another.f;
	}
};

int map[20][20];
int visited[20];

void addPath(int start, int end, int length) {
	map[start][end] = map[end][start] = length;
}

void showCityAndId(){
    for(int i = 0; i < 20; i++)
        cout << i << " - " << cityName[i] << endl; 
}

void initMap() {
	memset(map, 0, sizeof(map));
	for (int i = 0; i < 20; i++)
		visited[i] = -2;
	addPath(0, 19, 75);
	addPath(19, 12, 71);
	addPath(12, 15, 151);
	addPath(15, 0, 140);
	addPath(0, 16, 118);
	addPath(16, 9, 111);
	addPath(9, 10, 70);
	addPath(10, 3, 75);
	addPath(3, 2, 120);
	addPath(2, 14, 146);
	addPath(15, 14, 80);
	addPath(15, 5, 99);
	addPath(14, 13, 97);
	addPath(2, 13, 138);
	addPath(13, 1, 101);
	addPath(5, 1, 211);
	addPath(1, 6, 90);
	addPath(1, 17, 85);
	addPath(17, 7, 98);
	addPath(7, 4, 86);
	addPath(17, 18, 142);
	addPath(18, 8, 92);
	addPath(11, 8, 87);
}

//h(x)
int calcH(int start, int end) {
	return abs(strDist2Buch[start] - strDist2Buch[end]);
}

int Astar(int start, int end) {
	priority_queue<city> q;
	q.push(city(start, 0));
	while (!q.empty()) {
		city current = q.top();
		visited[current.id] = current.parent_id;
		if (current.id == end)
			break;
		q.pop();
		for (int i = 0; i < 20; i++) {
			if (map[current.id][i] != 0 && visited[i] == -2) {
				city next(i, current.g + map[current.id][i]);
				next.h = calcH(next.id, end);
				next.f = next.g + next.h;
				next.parent_id = current.id;
				q.push(next);
			}
		}
		while (visited[q.top().id] != -2)
			q.pop();
	}
	return q.top().g;
}

void printPath(int end) {
	int point = end;
	stack<int> paths;
	while (point != -1) {
		paths.push(point);
		point = visited[point];
	}
	cout << cityName[paths.top()];
	paths.pop();
	while (!paths.empty()) {
		cout << " ==> " << cityName[paths.top()];
		paths.pop();
	}
	cout << endl << endl;
}

int main() {
    showCityAndId();
	int start, end;
	cout << "请选择起始城市的序号: "; cin >> start;
	cout << "请选择目的城市的序号: "; cin >> end;

	initMap();

	cout << "最短路径长度为: " << Astar(start, end) << " kilometers" << endl;
	cout << "完整的路线为: ";
	printPath(end);

	return 0;
}