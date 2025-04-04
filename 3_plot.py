import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv('divans.csv')

prices = data['Цена']

# Находим и выводим среднюю цену
mean_price = prices.mean()
print(f"Средняя цена: {round(mean_price)}")

# Построение гистограммы
plt.hist(prices, bins=30, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()