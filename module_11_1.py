import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Библиотека request
'''

# # получение статус кода get запроса
# r = requests.get('https://ya.ru/search')
# print(r.status_code)

# # получение служебной информации от сайта браузеру
# print(r.headers)

# # получение HTML кода в виде текста
# print(r.text)

# # Получение get запроса с обращением по ключу (скопировать полученный вывод и записать в файл с расширением HTML,
# # открыть файл)
# params = {'q': 'cute hamsters'}
# r = requests.get('https://www.google.com/search', params=params)
# print(r.text)

# # Отправка POST запроса для регистрации/входа на сайте
# data = {'custname': 'dfdsfsd',
#         'custtel': '5235346462',
#         'custemail': 'grtrthfsh@mail.ru',
#         'size': 'medium',
#         'topping': 'bacon',
#         'delivery': 'comments'
#         }
# r = requests.post('https://httpbin.org/post', data=data)
# print(r.text)

'''
Библиотека pandas
'''

# # Создание обьекта со значениями в столбик к которым можно обращаться по индексу
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
#
# # Создание табличных данных путем передачи словаря объектов, где ключами являются заголовки столбцов, а значениями-
# # значения столбцов
# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )
# print(df2)
#
# # Просмотр таблиц начиная с верхних строк
# print(df2.head(1))
#
# # Просмотр таблиц начиная с нижних строк
# print(df2.tail(3))
#
# # Просмотр индексов таблицы
# print(df2.index)
#
# # Просмотр названия столбцов таблицы
# print(df2.columns)

'''
Библиотека matplotlib
'''
# Фигура 1 - Пустая
fig1 = plt.figure()

# Фигура 2.1 - С графиком и обычной линией
fig2_1, ax = plt.subplots()
ax.plot([1, 2, 7, 8, 3, 4], [1, 4, 2, 7, 2, 3])

# Фигура 2.2 - С графиком с штриховой линией и обычной
fig2_2, ax = plt.subplots()
ax.plot([1, 2, 7, 8, 3, 4], [1, 4, 2, 7, 2, 3], '--', [1, 2, 7], [1, 4, 2])
# Добавление сетки
plt.grid()

# Фигура 3 - создание фигур по количеству столбцов и строк
fig3, axs1 = plt.subplots(2, 3)

# Фигура 4 - создание фигур с передачей параметров
fig4, axs2 = plt.subplot_mosaic([['left', 'right_top'],
                                 ['left', 'right_bottom']])

np.random.seed(19680801)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

# Запуск программы
plt.show()
