// 23) Find the number which is not repeated in Array of integers, others are present for two times: https://www.geeksforgeeks.org/top-25-interview-questions/?ref=rp

#include "util.hpp"
#include <unordered_map>
#include <iostream>


using namespace std;
/*
 * Works if only one unique number in the array
 */
int main()
{
    vector<int> arr = input_vector<int>();
    print(arr);

    int x = 0;
    for (const auto& i: arr) {
        x ^= i;
    }
    std::cout << x << std::endl;
}