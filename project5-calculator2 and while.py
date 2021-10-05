def high_num(numa, numb, numc):
    if numa >= numb and numa >= numc:
        return numa
    elif numb >= numa and numb >= numc:
        return numb
    else:
        return numc


print(high_num(1, 15, 8))

num1 = float(input("Enter a number: "))
operator = (input("Enter an operator: "))
num2 = float(input("Enter another number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Bad operator")

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(month_conversions["Aug"])
print(month_conversions.get("Feb"))
print(month_conversions.get("Hello", "Not valid"))

i = 1
while i <= 50:
    print(i)
    i += i

secret_word = "Cool"
guess = ""
count = 0
while guess != secret_word and count <= 10:
    guess = input("Enter your guess: ")
    count += 1
if count <= 10:
    print("You win!!")
else:
    print("You lose")
print("2:32:49")
