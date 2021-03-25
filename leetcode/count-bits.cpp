/*
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
*/

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (size_t i = 0; i < 32; i++) {
            if ((n >> i) & 0x1 == 0x1) {
                count += 1;
            }
        }
        return count;
    }
};