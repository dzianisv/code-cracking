// 23) Find the number which is not repeated in Array of integers, others are present for two times: https://www.geeksforgeeks.org/top-25-interview-questions/?ref=rp

#include "util.hpp"
#include <unordered_map>
#include <iostream>


using namespace std;

int main()
{
    vector<int> arr = input_vector<int>();
    print(arr);

    unordered_map<int, size_t> u;
    for (const auto& i: arr) {
        u[i]++;
    }

    for (const auto& [key, value]: u) {
        if (value == 1) {
            cout << key << endl;
        }
    }
}