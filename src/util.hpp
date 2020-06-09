#pragma once

#include <vector>
#include <iostream>

template <typename T = int>
std::vector<T> input_vector()
{
    std::vector<T> arr;
    while (true) {
        T i;
        std::cin >> i;
        if (std::cin.eof()) {
            break;
        }
        arr.push_back(i);
    }

    return arr;
}

template <typename T = int>
void print(const std::vector<T>& arr)
{
    for(int i: arr) {
        std::cout << i << " ";
    }

    std::cout << std::endl;
}
