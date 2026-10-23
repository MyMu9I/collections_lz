import matplotlib.pyplot as plt #используем библиотеку, для графиков.
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7])# значения по оси Х
#Считаем значения для каждой функции
y_x2 = x ** 2 
y_x3 = x ** 3     
y_ex = np.exp(x) #Вычисляет экспоненту каждого элемента
y_ln = np.log(x) #Вычисляет натуральный логарифм
plt.figure("графики") # рисуем графики
plt.plot(x, y_x2, color='red', marker='s', label='x^2')# Рисуем x**2: цвет красный, точки — квадраты
plt.plot(x, y_ex, color='orange', marker='^', label='e^x')#Рисуем e**x: цвет оранжевый, точки — треугольники
plt.plot(x, y_ln, color='green', marker='o', label='ln(x)')#Рисуем ln(x): цвет зеленый, точки — кружочки
plt.plot(x, y_x3, color='blue', marker='x', label='x^3')# Рисуем x^3: цвет синий, точки — крестики
plt.xlabel("Ось X")  #подписываем ось Х
plt.ylabel("Ось Y") #подписываем ось Y
plt.grid(True)#сетка
plt.show() #Вывод
