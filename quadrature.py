'''
This module provides some functions to compute definite integrals of functions
of a single parameter.
'''


def trapezoid(f, a, b, n):
    '''Computes a numerical approximation of the integral of f(x) for x 
    from a to b using n equally spaced intervals.'''
    h = (b - a) / n
    s = (f(a) + f(b)) * h / 2
    for i in range(1, n):
        s += f(a + i * h)
    return s * h


def trapezoid_iterative(f, a, b, precision):
    '''Computes a numerical approximation of the integral of f(x) for x
    from a to b with the given precision.'''
    MIN_ITER = 4
    MAX_ITER = 25
    curr_iter, N, h = 0, 1, (b - a)
    s = (f(a) + f(b)) * h / 2
    old_s = s + 2 * precision
    while abs(s - old_s) >= precision or curr_iter < MIN_ITER:
        curr_iter += 1
        if curr_iter > MAX_ITER:
            raise Exception('No convergence in quadrature.trapezoid_iterative')
        N, h = N * 2, h / 2
        old_s = s
        s = 0
        for i in range(1, N, 2):
            s += f(a + i * h)
        s = s * h + old_s / 2
    return s


if __name__ == '__main__':
    import math
    print(trapezoid(math.sin, 0, 2 * math.pi, 1000))
    print(trapezoid_iterative(math.sin, 0, 2 * math.pi, 1e-6))
