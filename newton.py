#define first derivateive
def first_derv(fun, x, h=1e-5):
    """Approximate the first derivative of a function at a point."""
    return (fun(x + h) - fun(x - h))/(2 * h) 

#second derivative
def second_derv(fun, x, h=1e-5):
    return (fun(x + h) - 2 * fun(x) + fun(x - h)) / h**2 

#use newton's method
def optimize(start, fun, tol=1e-5, max_iter=100):
    """Find a local minimum of a function using Newton's m"""
    x = start
   
    for _ in range(max_iter):
        x_t = x - first_derv(fun, x) / second_derv(fun, x)
        if abs(x_t - x) < tol:
           return x_t
        x = x_t
    return x
