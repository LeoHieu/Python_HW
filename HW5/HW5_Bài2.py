s = input('Nhập vào 1 chuỗi: ')
if len(s) < 2:
    pass
else:
    print(s[:2] + s[-2:])