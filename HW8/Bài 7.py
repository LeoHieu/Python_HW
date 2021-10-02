s = 'Stringings'
dict_7 = {}.fromkeys(s, 0)
for i in s:
    for j in dict_7:
        if i == j:
            dict_7[j] += 1
print(dict_7)