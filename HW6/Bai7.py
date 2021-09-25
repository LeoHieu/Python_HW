list_a = ['a', 1, 6, 7, 'b', 8, 'c']
list_b = ['d', 9, 6, 'a', 5, 34]
count = 0
for i in range(len(list_a)):
    for u in range(len(list_b)):
        if list_a[i] == list_b[u]:
            count += 1
if count >= 1:
    print('2 list có phần tử chung')
else:
    print('2 list k có phần tử chung')