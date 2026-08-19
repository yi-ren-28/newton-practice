def first_derivative(func, x):
    """Define the first derivative of function f(x)"""
    f_x = (f(x + epsilon) - f(x)) / epsilon
    return f_x


def second_derivative(func, x):
    """call the first derivative twice"""
    f_xx = (first_derivative(func, x + epsilon) - first_derivative(func, x)) / epsilon
    return f_xx


epsilon = 1e-5
second_derivative(f, 2)


def newton(f, x0):
    x = x0
    while abs(f_x) > 10e-5:
        x = x - f_x / f_xx
    return x


def f(x):
    """Define the orginal function"""
    return x + 1


result = newton(f, 0)
print(result)
