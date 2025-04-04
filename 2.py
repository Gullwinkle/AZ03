import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Набор данных X')
plt.ylabel('Набор данных Y')

plt.show()