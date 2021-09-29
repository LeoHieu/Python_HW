tuple_a = (1, 2 , 3, 4, 5, 'abc')
tuple_b = ('xyz', 0, 32, 42, 91)
count = 0
for item in tuple_a:
    if item in tuple_b:
        count += 1
if count >= 1:
    print('2 tuple có phần tử chung')
else:
    print('2 tuple không có phần tử chung')