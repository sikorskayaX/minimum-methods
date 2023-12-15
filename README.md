# Minimum search methods

 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## Install 
```bash
# pip

$ python -m pip install -U pip
$ pip install numpy


# git

$ git clone https://github.com/sikorskayaX/minimum-methods.git
```

## Description 

The code implements and compares three optimization algorithms for finding the minimum of a multivariate function:

<b>Coordinate descent (coordinate_descent.py):</b>

Iteratively optimizes one coordinate at a time while keeping others fixed.

<b>Gradient descent (grad_descent.py):</b>

Uses the gradient of the function to take steps in the direction of steepest descent.


<b>Newton's method (newton.py):</b>

Uses the gradient and Hessian (matrix of second derivatives) to compute the next step as the inverse of the Hessian multiplied by the gradient. This approximates the minimum as the inverse of the Hessian is the inverse of the curvature matrix.
Each method takes an initial point, tolerance, and max iterations as inputs.They iteratively optimize the point until the minimum is found or iterations exceed max.

The functions, gradients and Hessians (for Newton) are defined.Each method calls the appropriate optimization algorithm and prints the minimum found.

So in summary, it implements and compares three common multivariate optimization algorithms (coordinate descent, gradient descent, Newton's method) for finding the minimum of functions.
