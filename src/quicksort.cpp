#include "util.hpp"
#include <vector>
#include <iostream>

using namespace std;

template <typename T>
void swap(T& a, T& b)
{
    cout << "swap " << a << ' ' << b << endl;
    T x = a;
    a = b;
    b = x;
}

template <typename T>
ssize_t partition(std::vector<T>& arr, ssize_t low, ssize_t high)
{
    T pivot = arr[high];
    ssize_t insert_index = low;

    for (ssize_t i = low; i < high; i++) {
        if (arr[i] < pivot) {
            ::swap<T>(arr[insert_index], arr[i]);
            insert_index += 1;
        }
    }
    ::swap<T>(arr[insert_index], arr[high] /*pivot index */);
    return insert_index;
}
static size_t counter = 0;

void quick_sort(std::vector<int>& arr, ssize_t low, ssize_t high)
{
    if (low < high) {
        ssize_t pivot_index = partition(arr, low, high);
        print(arr);
        quick_sort(arr, low, pivot_index-1);
        quick_sort(arr, pivot_index+1, high);
    }
}

int main()
{
    vector<int> arr = input_vector<int>();
    print(arr);
    quick_sort(arr, 0, arr.size()-1);
    print(arr);
    return 0;
}