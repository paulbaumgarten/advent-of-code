#include <iostream>
#include <vector>
#include <cmath> 
#include <fstream>
#include <string>

using namespace std;

class Claim {
    public:
        int id;
        int left, top, width, height;
        Claim(int id, int left, int top, int width, int height) {
            this->id = id;
            this->left = left;
            this->top = top;
            this->width = width;
            this->height = height;
        }
        void print() {
            cout << "claim id " << id << " left,top " << left << "," << top << " width x height " << width << "x" << height << "\n";
        }
};

int main() {
    // Read the file
    ifstream file("2018-03.txt");
    string tmp;
    vector<Claim> claims;
    while (file.good()) {
        file >> tmp; // id number
        int id = stoi(tmp.substr(1));
        file >> tmp; // @ symbol
        file >> tmp; // left,top
        int delim = tmp.find(',');
        int l = stoi(tmp.substr(0,delim));
        int t = stoi(tmp.substr(delim+1, tmp.length()-1));
        file >> tmp; // width x height;
        delim = tmp.find('x');
        int w = stoi(tmp.substr(0,delim));
        int h = stoi(tmp.substr(delim+1));
        if (file.good()) {
            Claim c (id,l,t,w,h);
            c.print();
            claims.push_back(c);
        }
    }
    file.close();
    cout << "\n";
    // Plot claims
    int coords[1000][1000];
    for (int y=0; y<1000; y++) {
        for (int x=0; x<1000; x++) {
            coords[y][x] = 0;
        }
    }
    for (Claim c : claims) {
        for (int y=c.top; y<(c.top+c.height); y++) {
            for (int x=c.left; x<c.left+c.width; x++) {
                coords[y][x]++;
            }
        }
    }
    // Find claim double-ups
    long doubles = 0;
    for (int y=0; y<1000; y++) {
        for (int x=0; x<1000; x++) {
            if (coords[y][x] > 1) doubles++;
        }
    }
    cout << "Double up claims: " << doubles << "\n";

    // Reset claims
    for (int y=0; y<1000; y++) {
        for (int x=0; x<1000; x++) {
            coords[y][x] = 0;
        }
    }
    vector<int> clashes;
    for (Claim c : claims) {
        for (int y=c.top; y<(c.top+c.height); y++) {
            for (int x=c.left; x<c.left+c.width; x++) {
                if (coords[y][x] == 0) {
                    coords[y][x] = c.id;
                } else {
                    clashes.push_back(coords[y][x]);
                    clashes.push_back(c.id);
                }
            }
        }
    }
    // Find which claims are not in `clashes`
    for (int i=1; i<=1295; i++) {
        if (count(clashes.begin(), clashes.end(), i) == 0) {
            cout << "No clash for id " << i << "\n";
        }
    }
}

