// /Users/pbaumgarten/Desktop/picosystem-v0.1.3-micropython-v1.19.uf2

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const char* path = "/Users/pbaumgarten/repos/advent-of-code/2022/day 14b.txt";

int main() {
    ifstream file (path, ios::in|ios::binary|ios::ate);
    if (file.is_open())
    {
        streampos size = file.tellg();
        char* data = new char[1024];
        long offset = 0; 
        while (offset<size) {
            file.seekg(offset, ios::beg);
            file.read(data, 1024);
            cout << "read from " << offset << endl;
            offset += 1024;
        }
        file.seekg(offset, ios::beg);
        file.read(data, 1024);
        cout << "read from " << offset << endl;
        string closer = data;
        cout << closer.substr(0, size % 1024) << endl;
        file.close();
        delete[] data;
    }
    else cout << "Unable to open file";
    return 0;
}

