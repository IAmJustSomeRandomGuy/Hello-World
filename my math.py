"""
def prime_numbers(limit=1000000):
    yield 2
    sub_limit = int(limit**0.5)
    flags = [True, True] + [False] * (limit - 2)
    # Step through all the odd numbers
    for i in range(3, limit, 2):
        if flags[i]:
            continue
        yield i
        # Exclude further multiples of the current prime number
        if i <= sub_limit:
            for j in range(i*i, limit, i<<1):
                flags[j] = True


i = 1
already_seen = []
primes_history = []
idk = []
idk1 = 0
primes = 0

while primes <= 1:
    print(primes)
    primes = 0
    i += i
    for x in prime_numbers(i):
        if x not in already_seen:
            already_seen += [x]
            primes += 1
    primes_history += [primes]

print('hi')

for x, y in zip(primes_history[0:], primes_history[1:]):
    print(y/x)
    idk += [y/x]

for x in idk:
    idk1 += x

idk1 = idk1 / len(idk)
print('hello ' + str(idk1))

list1 = [2,3,5,7,9,11,13,17,19]
print(list1[::-1])
"""

kitten = 'kintent'

amount = 0
for x in range(len(kitten)-2):
    print(kitten[-2:])
    if kitten[x:x+2] == kitten[-2:]:
        amount += 1
print(amount)
