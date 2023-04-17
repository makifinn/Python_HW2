# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random


numberOfCoins = int(input("Введите количество монет: "))

coins = []

for i in range(numberOfCoins):
    coin = random.randint(0,1)
    coins.append(coin)
print(coins)

zeros = 0
ones = 0
for i in coins:
    if i == 0:
        zeros += 1
    if i == 1:
        ones += 1

if zeros > ones:
    print(ones)
else:
    print(zeros)


# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))

if firstNumber <= 0 or firstNumber > 1000:
    print("введите число от 1 до 1000")
if secondNumber <= 0 or secondNumber > 1000:
    print("введите число от 1 до 1000")

s = firstNumber + secondNumber
p = firstNumber * secondNumber

print(s, p)

findFirst = 1
findSecond = s - 1

for i in range(s):
    while findFirst * findSecond != p:
        findFirst += 1
        findSecond -= 1

print(findFirst, findSecond)


# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

n = int(input("Введите число: "))

dup = 1
counter = 0

while i < n:
    if counter == 0:
        print(1)
    elif dup < n:
        print(dup)
    else:
        break
    dup *= 2
    counter += 1