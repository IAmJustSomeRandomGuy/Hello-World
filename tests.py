import random
lol = ''
for i in range(9):
    lol += str(random.randrange(1, 10))
print(lol)
num = [5, 4, 5, 3, 2, 3, 8, 9, 6, 6]
for x in num:
    a = num.index(x) + 1
    for y in num[a:]:
        if x == y:
            num.remove(y)
print(num)

rps_dic = {
    1: 'rock',
    2: 'paper',
    3: 'scissors'
}
rps_dic2 = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'r': 1,
    'p': 2,
    's': 3,
}

player_input = input('rock, paper or scissors: ')
player = rps_dic2.get(player_input)
print(player)
comp = random.randrange(1, 4)
print(comp)
outcome = comp - int(player)
print(outcome)
print('Your opponent choose: ' + rps_dic.get(comp))
if outcome == -1 or outcome == 2:
    print('You win! :)')
elif outcome == 0:
    print("It's a tie! :|")
else:
    print("You lose! :(")
