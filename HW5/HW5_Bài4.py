s = input('Nhập 1 chuỗi: ')
s1 = ''
for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        s1 = s1 + s[i].upper()
    elif 'A' <= s[i] <= 'Z':
        s1 = s1 + s[i].lower()
    else:
        s1 = s1 + s[i]
print(s1)