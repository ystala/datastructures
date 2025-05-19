import numpy as np
import time
from scipy.linalg.blas import cblas_zgemm

n = 2048
A = np.random.rand(n, n) + 1j * np.random.rand(n, n)
B = np.random.rand(n, n) + 1j * np.random.rand(n, n)
C = np.zeros((n, n), dtype=np.complex128)

start = time.time()
cblas_zgemm(1.0, A, B, 0.0, C, trans_a=0, trans_b=0)
end = time.time()

t = end - start
c = 2 * n**3
mflops = c / t * 1e-6

print(f"Время: {t:.2f} сек")
print(f"Производительность: {mflops:.2f} MFLOPS")
