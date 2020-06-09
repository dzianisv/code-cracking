
// 4) Reversing of Arrays (https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array/)


#include <vector>
#include <iostream>

using namespace std;

void reverse(vector<int>& arr)
{
    for (size_t i = 0; i <= (arr.size() / 2 - 1); i++) {
        size_t j = arr.size() - 1 -i;

        int x =  arr[i];
        arr[i] = arr[j];
        arr[j] = x;
    }
}

void print(const vector<int>& arr)
{
    for(int i: arr) {
        cout << i << " ";
    }

    cout << endl;
}

int main()
{
    vector<int> arr;
    while (true) {
        int i;
        cin >> i;
        if (cin.eof()) {
            break;
        }
        arr.push_back(i);
    }

    print(arr);
    reverse(arr);
    print(arr);
}