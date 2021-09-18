import math
a = int(input('Nhập a = '))
b = int(input('Nhập b = '))
c = int(input('Nhập c = '))
if a <= 0 or b <= 0 or c <= 0:
    print('3 số trên không thể tạo thành 1 tam giác')
else:
    if a+b>c and b+c>a and a+c>b:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print('3 số trên tạo thành tam giác vuông')
        else:
            print('3 số trên tạo thành 1 tam giác')
    else:
        print('3 số trên không thể tạo thành 1 tam giác')