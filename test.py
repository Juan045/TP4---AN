import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Example polynomial, can be replaced by any polynomial function
def P(x):
    return (-5.289e-11)*x**6 + (4.74e-08)*x**5 + (-1.604e-05)*x**4 + (0.002544)*x**3 + (-0.1906)*x**2 + (5.893)*x + 10

# Objective function to minimize the sum of P(xi) over 20 points
def objective(x):
    return sum(P(xi) for xi in x)

# Distance constraints: 10 <= xi+1 - xi <= 20 for all i
def distance_constraints_min(x):
    return [x[i+1] - x[i] - 10 for i in range(len(x)-1)]  # xi+1 >= xi + 10

def distance_constraints_max(x):
    return [20 - (x[i+1] - x[i]) for i in range(len(x)-1)]  # xi+1 <= xi + 20

# Boundary constraints: points must lie within [0, 300]
def boundary_constraints(x):
    return [xi for xi in x]  # All points must be >= 0

def upper_boundary_constraints(x):
    return [300 - xi for xi in x]  # All points must be <= 300

def plot_polynomial_and_points(polynomial, x_points):
    # Create a range of x values from 0 to 300 for plotting the polynomial
    x_range = np.linspace(0, 300, 500)
    y_values = polynomial(x_range)

    # Plot the polynomial
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_values, label='P(x)', color='blue', lw=2)

    # Plot the 20 points found by the optimization
    y_points = polynomial(x_points)
    plt.scatter(x_points, y_points, color='red', zorder=5, label='Optimal Points')

    # Annotate each point with its index for clarity
    for i, (x, y) in enumerate(zip(x_points, y_points)):
        plt.text(x, y, f'{i+1}', fontsize=9, verticalalignment='bottom')

    # Labels and title
    plt.title('Polynomial and Optimal Points', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('P(x)', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

# Initial guess (linearly spaced points)
x0 = np.linspace(0, 300, 20)

# Define the constraints
cons = [{'type': 'ineq', 'fun': lambda x: np.array(distance_constraints_min(x))},
        {'type': 'ineq', 'fun': lambda x: np.array(distance_constraints_max(x))},
        {'type': 'ineq', 'fun': lambda x: np.array(boundary_constraints(x))},
        {'type': 'ineq', 'fun': lambda x: np.array(upper_boundary_constraints(x))}]

# Minimize the objective function subject to the constraints
solution = minimize(objective, x0, method='SLSQP', constraints=cons)

# Output the optimized points
optimal_points = solution.x
optimal_value = solution.fun
print("Optimal Points:", optimal_points)
print("Minimum Sum:", optimal_value)
plot_polynomial_and_points(P, optimal_points)