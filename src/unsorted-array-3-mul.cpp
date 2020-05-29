#include <array>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;



int main(int argc, char** argv)
{
    vector<int> src;
    array<int, 3> positive = {0, 0, 0};
    array<int, 2> negative = {0, 0};

    do {
        int i;
        cin >> i;
        if (cin.eof()) {
            break;
        }
        src.push_back(i);
    } while (true);

    for (auto& n: src) {
        if (n > 0) {
            auto element = std::min_element(positive.begin(), positive.end());
            *element = std::max(*element, n);
        } else if (n < 0) {
            auto element = std::max_element(negative.begin(), negative.end());
            *element = std::min(*element, n);
        }
    }

    cout << std::max(positive[0] * positive[1] * positive[2], negative[0] * negative[1] * *std::max_element(positive.begin(), positive.end())) << endl;
}