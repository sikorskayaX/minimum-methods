import numpy as np
# Определяем функцию
def f(x):
    return x[0]**2 + x[0]*x[1] + x[1]**2

# Покоординатный спуск
def coordinate_descent(x0, tolerance, max_iterations):
    x = x0
    for i in range(max_iterations):
        # Обновляем x1, фиксируя x2
        x[0] = -0.5 * x[1]
        # Обновляем x2, фиксируя x1
        x[1] = -0.5 * x[0]
        # Проверяем сходимость
        if f(x) < tolerance:
            break
    return x

x0 = np.array([1, 1]) # Начальная точка 
tolerance = 1e-6 # Допустимая погрешность
max_iterations = 300 # Максимальное количество итераций

# Выполнение метода покоординатного спуска
minimum = coordinate_descent(x0, tolerance, max_iterations)

# Вывод результата
print("Минимум функции находится в точке:", "(", minimum[0], ",", minimum[1], ")")

