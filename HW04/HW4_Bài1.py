import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
#Giải nghiệm PT bậc 2: ax^2 + bx + c = 0 (Xét tất cả các trường hợp có thể xảy ra)

if a == 0:
    if b == 0 and c == 0:
        print('PT có vô số nghiệm')
    elif b == 0 and c != 0:
        print('Pt Lỗi')
    else:
        x = -c/b
        print('Pt có nghiệm x = ', x)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'x1 = ', x1)
        print(f'x2 = ', x2)
    elif delta == 0:
        x1 = x2 = -b / (2 * a)
        print(f'PT có nghiệm kép x1 = x2 = ', x1)
    else:
        print('PT vô nghiệm')