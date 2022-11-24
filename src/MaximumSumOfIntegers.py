"""
There is an array A consisting of N integers. What is the maximum sum of two integers from A that share their first and last digits? For example, 1007 and 167 share their first (1) and last (7) digits, whereas 2002 and 55 do not.

Write a function:
]def solution(A)]

that, given an array A consisting of N integers, returns the maximum sum of two integers that share their first and last digits. If there are no two integers that share their first and last digits, the function should return −1.

Examples:
1. Given A = [130, 191, 200, 10], the function should return 140. The only integers in A that share first and last digits are 130 and 10
"""

import math
import bisect

# naive
# def compute_key(num: int) -> int:
#     digits = list(map(int, str(num)))
#     key = digits[0] * 10 + digits[-1]
#     return key

def compute_key(num: int) -> int:
    digits_n = int(math.log10(num))+1
    return (num // 10**(digits_n-1)) * 10 + (num % 10)

def solution(A):
    brothers = dict()
    maximum = -1
    for num in A:
        key = compute_key(num)
        if key in brothers:
            twins = brothers[key]
            # naive
            # big_brother = max(twins)
            # twins.append(num)

            # if it has a lot of collisions, I would check perfomance of heap, max(array), binary tree and binary insert. I don't have much time to experiment now.
            big_brother = twins[-1]
            # insert item in the sorted array to avoid max(twins) O(len(twins)) on each collisoin. Effective in case if there is a lot of collisions 
            idx = bisect.bisect_left(twins, num)
            twins.insert(idx, num)
            maximum = max(big_brother + num, maximum)
        else:
            brothers[key] = [num]
    return maximum
        