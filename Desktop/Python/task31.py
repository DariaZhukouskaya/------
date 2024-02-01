'''Задача №31. Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ...,
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи

Input: 7
Output: 21'''

n = 9
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)  #фибоначи: 3 число = сумме двух предыдущих

print(fib(n))