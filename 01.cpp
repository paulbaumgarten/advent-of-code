#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

const string filename = "01a.data";

int main() {
    cout << "Advent of code 2021\n";
    string line;
    ifstream myfile(filename);
    if (myfile.is_open()) {
        while ( getline (myfile,line) ) {
            cout << line << '\n';
        }
        myfile.close();
    } else 
        cout << "Unable to open file";
}

