import sympy as sp

def eval(n):
    s = 1 - n + pow(n,2) - pow(n,3) + pow(n,4) - pow(n,5) + pow(n,6) - pow(n,7) + pow(n,8) - pow(n,9) + pow(n,10)
    return s


def least_generating_polynomial(x_points, y_points):
    """
    Computes the least generating polynomial that passes through given data points.

    Args:
        x_points (list): The x-values of the data points.
        y_points (list): The y-values of the data points.

    Returns:
        sympy.Poly: The interpolating polynomial.
    """
    if len(x_points) != len(y_points):
        raise ValueError("The number of x and y points must be the same.")

    x = sp.symbols('x')
    polynomial = 0

    # Lagrange interpolation formula
    for i in range(len(x_points)):
        term = y_points[i]
        for j in range(len(x_points)):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        polynomial += term

    simplified_poly = sp.simplify(polynomial)
    poly_func = sp.lambdify(x, simplified_poly, 'numpy')  # Create a callable function for numerical evaluation

    return simplified_poly, poly_func


def main():
    y = []
    x = []
    func = []
    S = 0
    for i in range(1,11):
        y.append(eval(i))
        x.append(i)
        [f, g] = least_generating_polynomial(x,y)
        func.append(f)
        S += g(i+1)
    return S


main()
