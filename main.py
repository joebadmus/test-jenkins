# Import numpy for numerical computations
import numpy as np

# Define the function to be minimized


def f(x, y):
    return x**2 + y**2

# Define the gradient of the function


def grad_f(x, y):
    return np.array([2*x, 2*y])

# Define the gradient descent algorithm


def gradient_descent(f, grad_f, start, alpha, tol, max_iter):
    # Initialize the current point and the iteration counter
    x = start
    i = 0
    # Loop until the gradient is close to zero or the maximum number of iterations is reached
    while np.linalg.norm(grad_f(x[0], x[1])) > tol and i < max_iter:
        # Update the current point by moving in the opposite direction of the gradient
        x = x - alpha * grad_f(x[0], x[1])
        # Increment the iteration counter
        i += 1
    # Return the final point and the number of iterations
    return x, i


# Set the parameters
start = np.array([1, 1])
alpha = 0.1
tol = 1e-6
max_iter = 100

# Call the gradient descent function
x, i = gradient_descent(f, grad_f, start, alpha, tol, max_iter)

# Print the results
print(f"Final point: {x}")
print(f"Function value: {f(x[0], x[1])}")
print(f"Gradient norm: {np.linalg.norm(grad_f(x[0], x[1]))}")
print(f"Number of iterations: {i}")
