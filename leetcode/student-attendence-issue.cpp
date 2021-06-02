#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Solution
{
private:
    size_t mem[100000][2][3] = {O};

    size_t g(size_t day, size_t absentCount, size_t lateCount)
    {
        if (day == 0)
        {
            return 1;
        }

        if (mem[day][absentCount][lateCount] != 0)
        {
            return mem[day][absentCount][lateCount];
        }

        size_t res = 0;
        if (absentCount == 0)
        {
            res = (res + g(day - 1, absentCount + 1, 0));
        }

        if (lateCount < 2)
        {
            res = (res + g(day- 1, absentCount, lateCount + 1));
        }

        res = res + g(day - 1, absentCount, 0);
        mem[day][absentCount][lateCount] = res;
        return res;
    }

public:
    int checkRecord(int n)
    {
        return g(n, 0, 0);
    }
};

int main(int argc, char** argv) {
    if (argc != 2) {
        return -1;
    }

    size_t days = std::stoll(argv[1]);

    cout << std::pow(3, days) - Solution().checkRecord(days) << endl;
}