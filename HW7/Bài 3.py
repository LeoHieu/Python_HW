list_3 = [1, 2, 'a', 9, 3.14, ('z', 2), 6, 4]
count = 0
for item in list_3:
    if type(item) != tuple:
        count += 1
    elif type(item) == tuple:
        break
print(count)