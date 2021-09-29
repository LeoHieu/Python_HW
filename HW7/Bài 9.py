tuple_9 = (3.14, -2.1, 3.4, 5.17, 8.14)
max = tuple_9[0]
sum = 0
for item in tuple_9:
    sum += item
    if max <= item:
        max = item
print(f'Max = {max}')
print(f'Sum = {sum}')