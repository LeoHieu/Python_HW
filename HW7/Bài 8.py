tuple_8 = (1, 1, 1, 1)
count = 0
a = 1
for item in tuple_8:
    if item != 1:
        count += 1
if count == 0:
    print('Tất cả các phần tử trong tuple giống nhau')
else:
    print('Có phần tử khác nhau trong tuple')