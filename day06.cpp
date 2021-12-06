#include <iostream>
#include <vector> 
#include <cmath>
#include <string>
#include "utils.cpp"

using namespace std; 

int main() {
    // Read in the comma seperated integers
    int size;
    int* data = inputIntegers(size);
    
    // Start of observation. How many lanternfish at each day of their cycle?
    unsigned long long lanternfish[9] = {0,0,0,0,0,0,0,0,0};
    for (int i=0; i<size; i++) {
        lanternfish[ data[i] ]++;
    }

    // Run the lanternfish through their spawning cycle for given number of days
    int numDays = 256;
    for (int day=0; day<numDays; day++) {
        unsigned long long spawning = lanternfish[0]; // How many are about to spawn?
        for (int i=1; i<=8; i++) { // Advance all the other lanternfish 1 day
            lanternfish[i-1] = lanternfish[i];
        }
        lanternfish[6] += spawning; // Reset spawning lanternfish to day 6
        lanternfish[8] = spawning; // Create new lanternfish at day 8
    }

    // End of observation. How many lanternfish now?
    unsigned long long total=0;
    for (int i=0; i<=8; i++) {
        cout << "At day " << i << " there are " << lanternfish[i] << " lanternfish\n";
        total += lanternfish[i];
    }
    cout << total << "\n";
}

/*
Puzzle input
4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2
*/