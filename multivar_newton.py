import numpy as np

def newton_method(grad, hessian, x0, tol=1e-6, max_iter=100):
    x = np.array(x0, dtype=float)

    for i in range(max_iter):
        # Newton method update: x_new = x - H(x)^(-1) grad(x)
        x_new = x - np.linalg.solve(hessian(x), grad(x))

        # stop when ||x_new - x|| is small
        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new

    return x