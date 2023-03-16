# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
from os import system
system("cls")

flag = True
while flag:
    try:
        n = int(input("Введите N: "))
        flag = False
    except:
        print("Это не число, попробуй ещё раз")

power = 0
while (2 ** power <= n):
    print(f"Степень {power}; Число {2 ** power}")
    power += 1
