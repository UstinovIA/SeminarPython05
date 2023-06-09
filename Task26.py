# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def PowerNumber(num, multi):
    if multi == 1: return num
    return num * PowerNumber(num, multi-1)

input_number = int(input("Введите число: "))
input_multi = int(input("Введите степень: "))
result = PowerNumber(input_number, input_multi)
print(f"{input_number} в степени {input_multi} равно {result}")