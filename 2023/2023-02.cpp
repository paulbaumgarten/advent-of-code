#include <iostream>
#include <vector>
#include <cmath> 
#include <fstream>
#include <string>

using namespace std;
const double pi = 3.14159265358979323846;

void part1() {
    ifstream file("./2023/2023-02.txt");
    if (! file.is_open()) {
        cout << "Error opening file. Terminating." << endl;
        return;
    }
    long freq = 0;
    long tmp;
    while (! file.eof()) {
        file >> tmp;
        freq += tmp;
    }
    cout << freq << endl;
}

void part2() {
}

int main() {
    cout << "Let's go" << endl;
    part1();
    part2();
    return 0;
}
