import type_chart

#    type_b = type_chart.type_list1.index(input('type1: '))
#    type_a = type_chart.type_list1.index(input('type2: '))

#    type1 = type_chart.type_list[type_a]
#    type2 = type_chart.type_list[type_b]

#    not needed
#    type1_nums = list(zip(type1.values()))
#    type2_nums = list(zip(type2.values()))

highest_super_weak = [0]
highest_weak = [0]
highest_strong = [0]
highest_resistant = [0]
highest_normal = [0]
highest_super_strong = [0]

for i in type_chart.type_list[::-1]:
    for n in type_chart.type_list[::-1]:
        result = ''
        super_weak = 0
        weak = 0
        strong = 0
        super_strong = 0
        resistant = 0
        normal = 0

        for x in i.keys():
            result += str(i.get(x) * n.get(x))
            result += ' '
        result_list = result.split(' ')
        result_list.pop()

        print(f'{type_chart.type_list1[type_chart.type_list.index(i)]} +'
              f' {type_chart.type_list1[type_chart.type_list.index(n)]}')

        for x in result_list:
            x = float(x)
            if x == 0:
                resistant += 1
            elif x == 0.25:
                super_strong += 1
            elif x == 0.5:
                strong += 1
            elif x == 1:
                normal += 1
            elif x == 2:
                weak += 1
            elif x == 4:
                super_weak += 1

        print(f'resistant: {resistant}\n'
              f'super weak: {super_weak}\n'
              f'weak: {weak}\n'
              f'normal: {normal}\n'
              f'strong: {strong}\n'
              f'super strong: {super_strong}\n')
        if super_weak > highest_super_weak[0]:
            highest_super_weak = [super_weak, type_chart.type_list1[type_chart.type_list.index(i)],
                                  type_chart.type_list1[type_chart.type_list.index(n)]]
        if weak > highest_weak[0]:
            highest_weak = [weak, type_chart.type_list1[type_chart.type_list.index(i)],
                            type_chart.type_list1[type_chart.type_list.index(n)]]
        if strong > highest_strong[0]:
            highest_strong = [strong, type_chart.type_list1[type_chart.type_list.index(i)],
                              type_chart.type_list1[type_chart.type_list.index(n)]]
        if super_strong > highest_super_strong[0]:
            highest_super_strong = [super_strong, type_chart.type_list1[type_chart.type_list.index(i)],
                                    type_chart.type_list1[type_chart.type_list.index(n)]]
        if resistant > highest_resistant[0]:
            highest_resistant = [resistant, type_chart.type_list1[type_chart.type_list.index(i)],
                                 type_chart.type_list1[type_chart.type_list.index(n)]]
        if normal > highest_normal[0]:
            highest_normal = [normal, type_chart.type_list1[type_chart.type_list.index(i)],
                              type_chart.type_list1[type_chart.type_list.index(n)]]
print('highest_super_weak', highest_super_weak,
      '\nhighest_weak', highest_weak,
      '\nhighest_strong', highest_strong,
      '\nhighest_super_strong', highest_super_strong,
      '\nhighest_resistant', highest_resistant,
      '\nhighest_normal', highest_normal)
