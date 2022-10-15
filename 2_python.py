from collections import defaultdict

data = defaultdict(list)

x = input('Вводите данные в формате, установленном условием задания: имя, '
          'пробел, число.\nЧтобы обозначить конец ввода, введите q\n')

while x != 'q':
    try:
        name, hours = x.rsplit(' ', 1)
    except ValueError:
        print('Некорректный формат ввода, должны быть как минимум 2 '
              'значения, разделённые пробелом')
        x = input()
        continue
    try:
        hours = int(hours)
    except ValueError:
        print('Часы должны быть целым числом')
        x = input()
        continue
    data[name].append(hours)
    x = input()

for name, hours in data.items():
    print(f'{name}: {", ".join(map(str, hours))}; sum: {sum(hours)}')
