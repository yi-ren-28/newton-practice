
    
def first_derivative(func, x, epsilon = 0.0001):
    """Define the first derivative of function f(x)"""
    f_x = (f(x + epsilon) - f(x)) / epsilon
    return f_x

def second_derivative(func, x, epsilon = 0.0001):
    """call the first derivative twice"""
    f_xx = (first_derivative(func, x + epsilon) - first_derivative(func, x) )/ epsilon
    return f_xx

def newton_func(func, x0):
    x = x0
    i = 0
    while abs(first_derivative(func, x, epsilon = 0.0001)) > 10e-5:
        x = x - first_derivative(func, x, epsilon = 0.0001) / second_derivative(func, x, epsilon = 0.0001)
        i = i + 1
    return x

def f(x):
    """Define the orginal function"""
    return (x + 3)**2
    
result = newton_func(f, 0)
print(result)