# A number is prime if and only if:
#
# - It is an integer greater than 1
# - It is evenly divisible only by 1 and by itself

# 100 => [2, 2, 5, 5]
# 9 => [3, 3]
# 10 => [2, 5]
# 17 => [17]
# 20 => [2, 2, 5]

# O(N)
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# O(N*N) => O(N^2)
def get_primes(max: int):
    result = []
    # O(N * N)
    for i in range(2, max+1):
        # o(2) o(3) o(4) o(5) ... O(N)
        # O(N/2)
        if is_prime(i):
            result.append(i)
    return result

# sum(1..n) => n * (n + 1) / 2
#           => (n^2 + n) / 2


def get_prime2(max: int):
    for i in range(2, max+1):
        if is_prime(i):
            yield i
    
    
# O(log N * N^2)
def factorize(num: int):
    """2
    20/2 = 10
    10 /2 = 5
    
    9/3 = 3
    
    100/2=50
    50/2=25
    25/5 = 5
    """
    
    primes = []
    a = num
    
    # 4  = [ 2, 2] = 2 times
    # 256 = [2,, 2, 2, 2, 2, 2, 2] = 8 times
    # O(N/2)
    while a != 1:
                     # O(N^2)
        for prime in get_prime2(a):
            print(a, prime)
            if a % prime == 0:
                primes.append(prime)
                a = a // prime
                break
    return primes


assert not is_prime(-127)
assert not is_prime(-1)
assert not is_prime(1)
assert not is_prime(0)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(5)
assert not is_prime(6)
assert is_prime(7)

assert get_primes(16) == [2,3,5,7,11,13]

assert factorize(100) == [2, 2, 5, 5]
assert factorize(20) == [2, 2, 5]
assert factorize(2) == [2]
assert factorize(17) == [17]

