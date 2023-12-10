import numpy as np

# Определяем функцию
def f(x):
    return 9*x[0]**2 + x[1]**2 - 18*x[0] + 6*x[1] + 18

# Определяем градиент функции
def grad_f(x):
    return np.array([18*x[0] - 18, 2*x[1] + 6])

# Определяем Гессиан функции
def hessian_f(x):
    return np.array([[18, 0], [0, 2]])

def newton(x0, tolerance, max_iterations):
    x = x0
    for i in range(max_iterations):
        g = grad_f(x)
        H = hessian_f(x)
        x_new = x - np.dot(np.linalg.inv(H), g)
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
    return x

x0 = np.array([1, 1]) # Начальная точка 
tolerance = 1e-6 # Допустимая погрешность
max_iterations = 300 # Максимальное количество итераций

# Выполнение метода Ньютона
minimum = newton(x0, tolerance, max_iterations)

# Вывод результата
print("Минимум функции находится в точке:", "(", minimum[0], ",", minimum[1], ")")

