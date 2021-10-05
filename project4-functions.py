def hi(name, age):
    print("Hello " + name + " you are " + age)
    while name == "Adam" or name == "Dan":
        for x in range(0, 100000):
            print("ERROR")


login = False
if login:
    print("this is above")
    hi(input("Input your name: "), input("Input your age: "))
    print("this is bellow")


def cube(num):
    return num * num * num


yournum = cube(float((input("Input a number: "))))
coolnum = cube(21)
print(yournum)
print(coolnum)
if coolnum == yournum:
    def cube2(num1):
        num_a = float(num1) * float(num1) / 2
        num_b = float(num1) * float(num1) * float(num1)
        print(num_a)
        print(num_b)
        if num_a == num_b and num_a != 0:
            def cube3(num2, num3):
                num_a1 = float(num2) ** float(num3)
                num_b1 = float(num3) ** float(num2)
                print(num_a1)
                print(num_b1)
                if num_a1 == num_b1 and num2 != num3:
                    print("You win.")
                else:
                    print("Try again.")

            cube3(input("Input a number: "), input("Input a different number: "))
        else:
            print("Try again.")


    cube2(input("Input a number other then 0: "))
else:
    print("Try again.")


def restart():
    answer = input("If you want to try again input True or if you do not input False ")
    error = False
    if answer == "True":
        print("Press restart")
    elif answer == "False":
        print("Do not restart")
    else:
        print("Error")
        error = True
    while error:
        for x in range(0, 100000):
            print("ERROR")
