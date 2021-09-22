s = input('Nhập vào 1 chuỗi: ')
max = s[0]
min = s[0]
for i in range(len(s)):
    if max < s[i]:
        max = s[i]
    if min > s[i]:
        min = s[i]
print(f'Ký tự lớn nhất trong chuỗi là: {max}' )
print(f'Ký tự nhỏ nhất trong chuỗi là: {min}')