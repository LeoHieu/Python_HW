list_6 = ['a', 'dsanj', '82djsa', 3, 4384, 'asdr', 38, 3.52, 'a']
count = 0
for i in range(len(list_6)):
    if type(list_6[i]) == str:
        count += 1
print(count)