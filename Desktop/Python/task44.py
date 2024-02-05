'''Задача 44:
 В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
 Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()'''


import pandas as pd 
df = pd.read_csv('Pokemon.csv')
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
 
unique_values = data['whoAmI'].unique()    # получаем уникальное значение из столбика whoAmI
one_hot_data = pd.DataFrame()              # создаем пустой DataFrame

for value in unique_values:                # для каждого уникального значения создаем новый столбик и заполняем его(0 и 1)
    one_hot_data = (data['whoAmI'] == value).astype(int)
one_hot_data.head()