list_4 = ['a', 23, 379, 29, 'bcd', 3.242, 'world', 58, 289]
n = int(input('Nhập 1 số nguyên dương n: '))
while n < 0 or n > len(list_4):
    n = int(input('Nhập 1 số nguyên dương n: '))
else:
    part_1 = list_4[:n]
    part_2 = list_4[n:]
    print(part_1)
    print(part_2)