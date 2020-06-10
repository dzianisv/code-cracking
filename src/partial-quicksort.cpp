/*
    Write a function that takes an array A and index i into A, and rearranges elements such that
    all elements that less than A[i] appear first, followed by elements that are equal to A[i],
    followed by elements that are greater than A[i]

    Time complexity is O(|A|), space complexity is O(1)
*/

#include "util.hpp"
#include <vector>
#include <iostream>

using namespace std;

template <typename T>
void swap(T& a, T& b)
{
    T x = a;
    a = b;
    b = x;
}

template <typename T>
void partition(std::vector<T>& arr, ssize_t low, ssize_t high)
{
    T pivot = arr[high];
    ssize_t j = low; /* where smaller element can be set */
    ssize_t k = low; /* where equal element can be set */

    for (ssize_t i = low; i < high; i++) {
        if (arr[i] < pivot) {

            if (i != k) { //to avoid double swap :)
                ::swap<T>(arr[j], arr[k]);
            }
            ::swap<T>(arr[i], arr[j]);

            j += 1;
            k += 1;
        } else if (arr[i] == pivot) {
            ::swap<T>(arr[i], arr[k]);
            k += 1;
        }

        print(arr);
        cout << j << " " << k << endl;
    }
    ::swap<T>(arr[k], arr[high] /*pivot index */);
}

int main()
{
    int pivot_index;
    cin >> pivot_index;

    vector<int> arr = input_vector<int>();
    print(arr);

    ::swap<int>(arr[arr.size()-1], arr[pivot_index]);
    partition<int>(arr, 0, arr.size()-1);

    print(arr);
    return 0;
}