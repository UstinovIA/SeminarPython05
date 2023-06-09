# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def SumNumbers(first_num, second_num):
    if second_num == 0: return first_num
    return SumNumbers(first_num+1, second_num-1)

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
result = SumNumbers(first_number, second_number)
print(f"Сумма чисел {first_number} и {second_number} равна {result}")