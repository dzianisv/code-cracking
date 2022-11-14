"""
Weighted Sampling (with replacement)
Given an array of weights []int and k int as the number of elements to sample, return an array of the sampled indices []int such that each index is weighted by the value in weights.
The function should stay true to the exact probabilities - without approximations.

You can assume that weights doesn't contain any negative numbers, and the sum is greater than 0. You can also assume that k isn't negative.
For example: f(weights = [5, 10], k = 1) means that index 0 has weight 5 and index 1 has weight 10. If we wanted to sample k=1 index from weights, index 0 would have a 5/(5+10) probability of being sampled and index 1 would have a 10/(5+10) probability of being sampled. This function should therefore return [0] with 33% probability and [1] with 66% probability.
Another few examples are: 

f(weights = [0, 1], k = 1) should return [1] with 100% probability

f(weights = [99, 1], k = 1) should return [0] with 99% probability and [1] with 1% probability

f(weights = [50, 50], k = 2) should return [0, 0], [0, 1], [1, 0], or [1, 1] all with 25% probability
"""
import random
import bisect

def weighted_sampling_1(weights): # O(log(N))
    total = 0
    new_weights = []
    for w in weights:
        total += w
        new_weights.append(total)

    x = random.randint(0, total-1) 
    return bisect.bisect_left(new_weights, x)

def weighted_sampling(weights, k): # O(kN)
    return [weighted_sampling_1(weights) for _ in range(k)]

if __name__ == "__main__":
    print(weighted_sampling([5,10], 1))
    print(weighted_sampling([0,1], 1))
    print(weighted_sampling([99,1], 1))
    print(weighted_sampling([50,50], 2))

    
