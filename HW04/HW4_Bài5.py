epsilon = float(input('Nhập số epsilon <1: epsilon = '))
while epsilon >= 1 or epsilon < 0:
    epsilon = float(input('Nhập số epsilon <1: epsilon = '))

max = 1/epsilon
e = 0
i = 1
factorial = 1
while factorial <= max:
    e = e + 1/factorial
    factorial *= i
    i += 1
print(f'Tổng = ', e)