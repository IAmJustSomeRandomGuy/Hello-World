import random

point_max = 5
x = 0
results = []
iterations = 10000

while x < iterations:
    x += 1

    player1 = 0
    player2 = 0
    totalPoints = 100
    rounds = 0
    y = 0
    z = 0


    def questions(roll, points, player):
        if roll == 1:
            input("\nyou rolled a one!!!")
            return '0'

        print("\nyou rolled a", roll)
        print("total round score:", points)
        print("total player score:", player + points)
        while True:
            keep_playing = input("would you like to continue rolling? \n>").lower()

            if keep_playing == 'y' or keep_playing == 'yes':
                return 'True'
            elif keep_playing == 'n' or keep_playing == 'no':
                return 'False'


    def questionsPointRobot(roll, points, i):
        if roll == 1:
            return '0'

        if i >= point_max:
            return 'False'
        else:
            return 'True'


    def rolling(player):
        i = 0
        points = 0
        while True:
            i += 1
            roll = random.choice(range(6)) + 1
            points += roll

            proceed = questionsPointRobot(roll, points, i)

            if proceed == 'True':
                continue
            elif proceed == '0':
                points = 0
                break
            elif proceed == 'False':
                break
            else:
                raise NotImplementedError("invalid result")
        return points, i


    def isWinner(player):
        if player >= totalPoints:
            return True
        return False


    while True:
        players_temp = rolling(player1)
        player1 += players_temp[0]
        # print("\nplayer1 has", player1, "points\n")

        rounds += players_temp[1]

        y += 1
        if players_temp[0] != 0:
            z += 1

        if isWinner(player1):
            break

        # players_temp = rolling(player2)
        # player2 += players_temp[0]
        # print("\nplayer2 has", player2, "points\n")
        #
        # if isWinner(player2):
        #     print("player2 wins")
        #     break

    results.append([rounds, y, rounds/y, player1, z])
print(results)


avrage = 0
round_total = 0
player_score = 0
stuff = 0
stuff2 = 0
for c in results:
    avrage += c[2]
    round_total += c[0]
    player_score += c[3]
    stuff += c[4]
    stuff2 += c[1]

print("\n", avrage)
print(" throws in a round", avrage/iterations)
print("", round_total)
print(" rounds:", round_total/iterations)
print("", player_score)
print(" player score:", player_score/round_total)
print(stuff/iterations)
print(stuff2/iterations)
