import random
import type_chart
while True:
    type_list = []
    type_list += type_chart.type_list
    type_list2 = [
    'normal',
    'fighting',
    'flying',
    'poison',
    'ground',
    'rock',
    'bug',
    'ghost',
    'steel',
    'fire',
    'water',
    'grass',
    'electric',
    'psychic',
    'ice',
    'dragon',
    'dark',
    'fairy']
    comp_a = random.choice(type_list)
    comp1 = type_list.index(comp_a)
    type_list.remove(comp_a)
    type_list2.remove(type_chart.type_list1[comp1])
    comp_b = random.choice(type_list)
    comp2 = type_list.index(comp_b)
    print('Your opponent chose ' + str(type_chart.type_list1[comp1]) + ' and ' + str(type_list2[comp2]))
    player = input('What is effective? ')
    if player in type_chart.type_list1:
        result = comp_a.get(player) * comp_b.get(player)
        if result == 4:
            print("It's Ultra Effective!!!")
        elif result == 2:
            print("It's Super Effective!!!")
        elif result == 1:
            print("It's Effective!")
        elif result == 0.5:
            print("It's Not Very Effective...")
        elif result == 0.25:
            print("It's Almost Not Effective...")
        elif result == 0:
            print("No Effect...")
        else:
            print(result)
