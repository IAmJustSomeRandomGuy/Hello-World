import type_chart

type_b = type_chart.type_list1.index(input('type1: '))
type_a = type_chart.type_list1.index(input('type2: '))

type1 = type_chart.type_list[type_a]
type2 = type_chart.type_list[type_b]

# not needed
type1_nums = list(zip(type1.values()))
type2_nums = list(zip(type2.values()))

result = ''
super_weak = 0
weak = 0
strong = 0
resistant = 0
normal = 0

for x in type1.keys():
    result += str(type1.get(x) * type2.get(x))
    result += ' '
result_list = result.split(' ')

for x in result_list:
    if x == 0:
        resistant += 1
    elif x == 0.25:
        super_weak += 1
    elif x == 0.5:
        weak += 1
    elif x == 1:
        normal += 1
    elif x == 2:
        strong += 1

print(f'resistant: {resistant} \n'
      f'super weak: {super_weak}\n'
      f'weak: {weak}\n'
      f'normal: {normal}\n'
      f'strong: {strong}')


print(
    'normal: ' + str(result_list[0]) + '\n'
    'fighting: ' + str(result_list[1]) + '\n'
    'flying: ' + str(result_list[2]) + '\n'
    'poison: ' + str(result_list[3]) + '\n'
    'ground: ' + str(result_list[4]) + '\n'
    'rock: ' + str(result_list[5]) + '\n'
    'bug: ' + str(result_list[6]) + '\n'
    'ghost: ' + str(result_list[7]) + '\n'
    'steel: ' + str(result_list[8]) + '\n'
    'fire: ' + str(result_list[9]) + '\n'
    'water: ' + str(result_list[10]) + '\n'
    'grass: ' + str(result_list[11]) + '\n'
    'electric: ' + str(result_list[12]) + '\n'
    'psychic: ' + str(result_list[13]) + '\n'
    'ice: ' + str(result_list[14]) + '\n'
    'dragon: ' + str(result_list[15]) + '\n'
    'dark: ' + str(result_list[16]) + '\n'
    'fairy: ' + str(result_list[17])
    )
