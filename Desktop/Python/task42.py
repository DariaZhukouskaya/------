'''Функция map()'''


num = '1 2 4 7 8 9'.split()
print(num)
                        #вот тут return идет
num1 =list(map(lambda x: int(x) * 2, num))  # лямбда функция и функция map() сама ее вызывает
print(num1)
# Значения кратные 3:
num2 = list(filter(lambda x: x % 3, num1))
print(num2)