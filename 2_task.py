#2'. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N 
# *Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input())
some_list = []
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    some_list.append(fact)
print(some_list)