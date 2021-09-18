n = int(input('Nhập số nguyên dương n = '))
x = float(input('Nhập số thực x = '))

#Lập chương trình tính các tổng sau:
#S_1 = 1 + x + x^2 + x^3 + ... + x^n
#S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
#S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!

S_1 = 0
for i in range(0,n+1):
    i = x**i
    S_1 = S_1 + i
print(f'Tổng S_1 = ',S_1)
S_2 = 0
for i in range(0,n+1):
    i = (-x)**i
    S_2 = S_2 +i
print(f'Tổng S_2 = ', S_2)
S_3 = 0
factorial = 1
for i in range(1,n+1):
    factorial *= i
    i = (x**i)/factorial
    S_3 = S_3 + i
print(f'Tổng S_3 = ', S_3+1)
