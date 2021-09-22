s = input('Nhập vào 1 chuỗi: ')
char = input('Nhập vào 1 ký tự: ')
for i in range(len(s)):
    if s[i] == char:
        print(f'Vị trí của ký tự {char} trong chuỗi là: {i}')