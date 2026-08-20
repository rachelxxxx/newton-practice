import numpy as np
#Multivariate Newton
def optimize_multivariate(gradient, hessian, x0, tol=1e-6, max_iterations=100,):
    x = np.asarray(x0, dtype=float)
    for _ in range(max_iter):
        h = np.asarray(hessian(x), dtype=float)
        g= np.asarray(gradient(x), dtype=float)

        step = np.linalg.solve(h, g)
        x_new = x - step

        if np.linalg.norm(step) <= tol