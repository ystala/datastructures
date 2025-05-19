import numpy as np
import time
from numba import njit, prange

@njit(parallel=True, fastmath=True)
def matmul_blocked(A, B, C, block_size=64):
    n = A.shape[0]
    for i in prange(0, n, block_size):
        for j in range(0, n, block_size):
            for k in range(0, n, block_size):
                for ii in range(i, min(i + block_size, n)):
                    for kk in range(k, min(k + block_size, n)):
                        for jj in range(j, min(j + block_size, n)):
                            C[ii, jj] += A[ii, kk] * B[kk, jj]

n = 2048
A = np.random.rand(n, n) + 1j * np.random.rand(n, n)
B = np.random.rand(n, n) + 1j * np.random.rand(n, n)
C = np.zeros((n, n), dtype=np.complex128)

start = time.time()
matmul_blocked(A, B, C)
end = time.time()

t = end - start
c = 2 * n**3
mflops = c / t * 1e-6

print(f"Время: {t:.2f} сек")
print(f"Производительность: {mflops:.2f} MFLOPS")
