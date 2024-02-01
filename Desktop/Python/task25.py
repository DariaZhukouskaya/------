'''Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2'''

stroka = 'a a a b c a a d c d d'
spisok = stroka.split()
spisokOutput = []
count = 0
count1 = 1

for i in spisok:
    spisokOutput.insert(count, i)
    count += 2
    spisokOutput.insert(count1, spisokOutput.count(i))
    count1 += 2
print(spisokOutput)

#stroka= 'a a a b c a a d c d d'.split()
#strokaOutput = ''
#for i in stroka:
#    strokaOutput+=f"{i}_{strokaOutput.count(i)+1} "
#
#print(strokaOutput)

