from math import pi


class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return ((self.y2 - self.y1)**2 + (self.x2 - self.x1)**2)**0.5

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * pi * self.radius * self.height + 2 * pi * self.radius ** 2


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


class Account:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def __str__(self):
        return f'balance: {self.bal}\nowner:   {self.name}'

    def deposit(self, amount):
        self.bal = self.bal + amount
        print(f'you have deposited {amount}')

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal = self.bal - amount
            print(f'you have withdrawn {amount}')
        else:
            print("You don't have enough funds")
            print(f"You have {self.bal}")


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.name)
print(acct1.bal)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
