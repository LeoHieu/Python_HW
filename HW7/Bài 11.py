str_11 = input('Nhập vào 1 câu: ')
list_11 = []
a = -1
for i in range(len(str_11)):
    if str_11[i] == ' ':
        list_11.append(str_11[a+1:i])
        a = i
list_11.append(str_11[a+1:])
max = 0
b = 0
print(list_11)
for i in range(len(list_11)):
    if max <= len(list_11[i]):
        max = len(list_11[i])
        b = i
print(list_11[b])