from libc.math cimport sin

def f(x):
    return x ** 2 - x

def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx

cdef double f_c(double x) except? -2:
    return sin(x)

def integrate_f_c(a,b,N):
    cdef int i
    cdef double s,dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_c(a + i * dx)
    return s * dx