#include <iostream>
#include <vector>
#include <cmath> 
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream file("2018-01-input.txt");
    long freq = 0;
    long tmp;
    while (! file.eof()) {
        file >> tmp;
        freq += tmp;
    }
    cout << freq << endl;
}
