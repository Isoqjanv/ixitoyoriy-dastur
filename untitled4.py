# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19EfbyKUcWd4VQ7fLsODfR0yXGMOdh_hR
"""

# Pandas va Matplotlib kutubxonalarini import qilish
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Kun': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
    'New York': [22, 24, 23, 25, 26, 28, 29],
    'London': [15, 16, 17, 15, 14, 14, 13],
    'Tokyo': [30, 32, 33, 31, 30, 29, 28],
    'Moskva': [10, 9, 8, 7, 6, 5, 4]
}

df = pd.DataFrame(data)


print("Harorat ma'lumotlari:")
print(df)


plt.figure(figsize=(10, 6))


for city in df.columns[1:]:
    plt.plot(df['Kun'], df[city], label=city, marker='o')


plt.title('Turli Shaharlar Bo\'yicha Harorat O\'zgarishi')
plt.xlabel('Kunlar')
plt.ylabel('Harorat (°C)')
plt.xticks(rotation=45)
plt.legend(title='Shaharlar')
plt.grid(True)


plt.show()


max_temp_day = df.set_index('Kun').max(axis=0)
print("\nEng yuqori harorat kunlari:")
print(max_temp_day)


average_temperatures = df.set_index('Kun').mean(axis=0)
print("\nHar bir shahar bo'yicha o'rtacha harorat:")
print(average_temperatures)