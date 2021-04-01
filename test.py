from cython_tools.primes import integrate_f
import time
_start = time.time()
x = integrate_f(1,2,30000*300)
_end = time.time()
print(f'use Time:{(_end-_start):.03f}s')

_start = time.time()
x = integrate_f(1,2,30000*300)
_end = time.time()
print(f'use Time:{(_end-_start):.03f}s')