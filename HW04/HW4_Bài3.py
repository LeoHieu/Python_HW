n = int(input('Nhập 1 số nguyên dương n < 1000 : n = '))
while n >= 1000 or n < 0:
    n = int(input('Nhập 1 số nguyên dương n < 1000 : n = '))
a = n // 100
b = (n // 10) - a*10
c = n % 10
S = a + b +c
print(f'Tổng S =', S)