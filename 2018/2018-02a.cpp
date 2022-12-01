#include <iostream>
#include <vector>
#include <cmath> 
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream file("2018-02-input.txt");
    long twos = 0, threes = 0;
    string line;
    char c;
    vector<string> id;
    while (! file.eof()) {
        vector<char> v;
        file >> line;
        id.push_back(line);
        bool two_found = false, three_found = false;
        for (int i=0; i<line.length(); i++) {
            c = line[i];
            int occur = count(line.begin(), line.end(), c);
            if (occur == 2) { two_found = true; }
            if (occur == 3) { three_found = true; }
        }
        if (two_found) { twos++; }
        if (three_found) { threes++; }
    }
    long check = twos * threes;
    cout << "Twos " << twos << " threes " << threes << endl;
    cout << "Checksum " << check << endl;
    // Part two
    for (int i=0; i<id.size(); i++) {
        for (int j=i+1; j<id.size(); j++) {
            // Calculate the "likeness" of id[i] and id[j]
            string tmp1 = id[i];
            string tmp2 = id[j];
            int diff = 0;
            for (int k=0; k<tmp1.size(); k++) {
                if (tmp1[k] != tmp2[k]) { diff++; }
            }
            if (diff == 1) {
                cout << "Found two strings 1 char apart\n" << tmp1 << "\n" << tmp2 << endl;
            }
        }
    }
}
