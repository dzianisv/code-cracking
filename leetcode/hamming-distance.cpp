/* The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
*/

class Solution {
public:
    int countSetBits(int n) {
        int count = 0;
        for (size_t i = 0; i < sizeof(n) * 8; i++) {
            count += (n >> i & 0x1);
        }
        return count;
    }
    int hammingDistance(int x, int y) {
        return countSetBits(x ^ y);
    }
};