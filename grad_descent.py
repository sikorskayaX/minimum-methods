import numpy as np

# Определяем функцию и ее градиент
def f(x):
    return x[0]**2 + 2*x[1]**2 - 4*x[0] - 4*x[1]

def grad_f(x):
    return np.array([2*x[0] - 4, 4*x[1] - 4])

# Метод градиентного спуска
def gradient_descent(x0, learning_rate, tolerance, max_iterations):
    x = x0
    for i in range(max_iterations):
        gradient = grad_f(x)
        if np.linalg.norm(gradient) < tolerance:
            break
        x = x - learning_rate * gradient
    return x


x0 = np.array([0, 0]) # Начальная точка 
learning_rate = 0.1 # Скорость обучения
tolerance = 1e-6 # Допустимая погрешность
max_iterations = 300 # Максимальное количество итераций

# Выполнение метода градиентного спуска
minimum = gradient_descent(x0, learning_rate, tolerance, max_iterations)

# Вывод результата
print("Минимум функции находится в точке:", "(", minimum[0], ",", minimum[1], ")")

# Вывод с округлением
print("Минимум (округленный) функции находится в точке:", "(", round(minimum[0]), ",", round(minimum[1]), ")")
