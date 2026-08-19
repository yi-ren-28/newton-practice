def f(x):
    return x + 1
def first_derivative(func, x):
    f_x = (f(x + epsilon) - f(x)) / epsilon
    return f_x

def second_derivative(func, x):
    f_xx = (first_derivative(func, x + epsilon) - first_derivative(func, x) )/ epsilon
    return f_xx

epsilon = 1e-5
second_derivative(f, 2)