from typing import List

speed = True
for a in "Minecraft":
    print(a)
names = ["Karen", "Josh", "Marry"]
for name in names:
    print(name)
for index in range(10):
    print(index)
*hi, bye = range(12, 16)
for hello in hi:
    print(hello)
print()
print(bye)
for name in range(len(names)):
    print(names[name])
for text in range(3):
    if text == 0:
        print("first text")
    else:
        print("not first text")
print(3 ** 5)
if not speed:
    base_num = float(input("enter num:"))
    pow_num = float(input("enter power:"))


def raise_to_power():
    return base_num ** pow_num


if not speed:
    print(raise_to_power())


def raise_power(num1, num2):
    result = 1
    for b in range(num2):
        result = result * num1
    return result


print(raise_power(9.5, 8))
print("2:47:14")
formatting = f"hi {names[0]} how are you"
print(formatting)
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10]
]
print(num_grid[2][1])
for row in num_grid:
    for column in row:
        print(column)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiouy":
            if letter.isupper():
                translation = translation + "F"
            else:
                translation = translation + "f"
        else:
            translation = translation + letter
    return translation


if not speed:
    print(translate(input("Input a phrase: ")))
try:
    numa = int(input("Enter a number: "))
    numb = int(input("Enter a divider: "))
    numc = numa / numb
    print(numc)
except ValueError:
    print("Bad input")
except ZeroDivisionError as error:
    print(error)
