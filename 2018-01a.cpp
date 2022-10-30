#include <iostream>
#include <vector>
#include <cmath> 
#include <fstream>

using namespace std;

int main() {
    ifstream file("2018-01a-input.txt");
    long freq = 0;
    long tmp;
    while (! file.eof()) {
        file >> tmp;
        freq += tmp;
    }
    cout << freq << endl;
}
