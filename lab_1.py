import math

def find_max_gcd_pair(N):
    if N % 2 == 0:
        return (N // 2, N // 2)
    else:
        max_d = 1
        for d in range(2, int(math.isqrt(N)) + 1):
            if N % d == 0:
                max_d = max(max_d, d, N // d)
        if max_d == 1:
            return (1, N - 1)
        else:
            return (max_d, N - max_d)

N = int(input())
A, B = find_max_gcd_pair(N)
print(A, B)
