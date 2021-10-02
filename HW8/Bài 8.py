str_8 = input('Nhập 1 đoạn văn bản: ')
list_word = str_8.strip().split(' ')
dict_8 = {}.fromkeys(list_word, 0)
for i in list_word:
    for j in dict_8:
        if i == j:
            dict_8[j] += 1
print(dict_8)