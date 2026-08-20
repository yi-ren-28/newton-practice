
    
def first_derivative(func, x, epsilon = 1e-5):
    """Define the first derivative of function f(x)"""
    return (f(x + epsilon) - f(x)) / epsilon

def second_derivative(func, x, epsilon = 1e-5):
    """Call the first derivative twice"""
    return (first_derivative(func, x + epsilon) - first_derivative(func, x) )/ epsilon


def optimize(x0, func, tal = 1e-4):
    x_new = x0 - first_derivative(func, x0) / second_derivative(func, x0)
    x = x0
    while abs(first_derivative(func, x0)) > tal:
        x = x_new
        x_new = x0 - first_derivative(func, x) / second_derivative(func, x)
    return {"x": x_new, 
           'value': f(x_new)}

