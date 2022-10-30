#include <iostream>
#include <vector>
#include <cmath> 
#include <fstream>

using namespace std;

int main() {
    vector<long> v = {0};
    long freq = 0;
    long loop = 0;
    long tmp;
    bool found = false;
    while (! found) {
        cout << "\nLoop " << loop++ << " Size of v " << v.size() << endl;
        ifstream file("2018-01-input.txt");
        while (! file.eof()) {
            file >> tmp;
            freq += tmp;
            if (count(v.begin(), v.end(), freq) > 0) {
                cout << "\nFound repeat: " << freq << endl;
                found = true;
                return 0;
            } else {
                // cout << freq << " " ;
                v.push_back(freq);
            }
        }
        //found = true;
    }
}
