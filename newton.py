def f(x):
    """Define the orginal function"""
    return x + 1
    
def first_derivative(func, x):
    """Define the first derivative of function f(x)"""
    f_x = (f(x + epsilon) - f(x)) / epsilon
    return f_x

def second_derivative(func, x):
    """Define the second derivative of function f(x)"""
    f_xx = (first_derivative(func, x + epsilon) - first_derivative(func, x) )/ epsilon
    return f_xx

epsilon = 1e-5
second_derivative(f, 2)

x = x_0 + 1

while abs(x - x_0) > 10e-5:
    x = x0
    x = x0 - f_x / f_xx
    