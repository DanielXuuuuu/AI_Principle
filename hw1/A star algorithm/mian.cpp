//A* algorithm
//f(n) = g(n) + h(n)

#include <iostream>
#include <queue>
#include <cctype>
#include <string>
#include <memory.h>
#include <algorithm>
using namespace std;

#define A 0 //Arad
#define B 1 //Bucharest
#define C 2 //Craiova
#define D 3 //Dobreta
#define E 4 //Eforie
#define F 5 //Fagaras
#define G 6 //Giurgiu
#define H 7 //Hirsova
#define I 8 //Iasi
#define L 9 //Lugoj
#define M 10 //Mehadia
#define N 11 //Neamt
#define O 12 //Oradea
#define P 13 //Pitesti
#define R 14 //RimnicuVilcea
#define S 15 //Sibiu
#define T 16 //Timisoara
#define U 17 //Urziceni
#define V 18 //Vaslui
#define Z 19 //Zerind

struct city{
    int name; //用首字母表示
    int f;
    int g;
    int h;
    city(int name, int g){
        this->name = name;
        this->g = g;
        this->h = 0;
        this->f = 0;
    }
    bool operator< (const city & another) const{
        return this->f > another.f;
    }
};

int map[20][20];
int visited[20];

void addPath(int start, int end, int length){
    map[start][end] = map[end][start] = length;
}

void initMap(){
    memset(map, 0, sizeof(map));
    memset(visited, 0, sizeof(visited));
    addPath(A, Z, 75);
    addPath(Z, O, 71);
    addPath(O, S, 151);
    addPath(S, A, 140);
    addPath(A, T, 118);
    addPath(T, L, 111);
    addPath(L, M, 70);
    addPath(M, D, 75);
    addPath(D, C, 120);
    addPath(C, R, 146);
    addPath(S, R, 80);
    addPath(S, F, 99);
    addPath(R, P, 97);
    addPath(C, P, 138);
    addPath(P, B, 101);
    addPath(F, B, 211);
    addPath(B, G, 90);
    addPath(B, U, 85);
    addPath(U, H, 98);
    addPath(H, E, 86);
    addPath(U, V, 142);
    addPath(V, I, 92);
    addPath(N, I, 87);
}


int calcH(int start, int end){
    return 0;
}

int Astar(int start, int end){
    priority_queue<city> q;
    q.push(city(start, 0));
    while(!q.empty()){
        city current = q.top();
        if(current.name == end)
            break;
        q.pop();
        visited[current.name] = 1;
        for(int i = 0; i < 20; i++){
            if(map[current.name][i] != 0 && !visited[i]){
                city next(i, current.g + map[current.name][i]);
                next.h = calcH(next.name, end);
                next.f = next.g + next.h;
                q.push(next);
            }
        }
        while(visited[q.top().name] == 1)
            q.pop();
    }
    return q.top().g;
}

int main(){
    string startCity, endCity;
    char start, end;
    cout << "Please input the name of start city: "; cin >> startCity; start = toupper(startCity[0]);  
    cout << "Please input the name of end city: "; cin >> endCity; end = toupper(endCity[0]);  
    
    initMap();  

    cout << "The length of shortest path is: " << Astar(, ) << " kilometers" << endl;

    return 0;
}