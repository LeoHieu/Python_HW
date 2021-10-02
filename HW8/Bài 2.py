dict_2 = {
    1: 2,
    2: 42,
    3: 9,
    4: 99,
    -5: 148
}
max_k1 = max(dict_2.keys())
print(f'Phần tử có key lớn top 1 = {dict_2[max_k1]}')
dict_2.pop(max_k1)
max_k2 = max(dict_2.keys())
print(f'Phần tử có key lớn top 2 = {dict_2[max_k2]}')
dict_2.pop(max_k2)
max_k3 = max(dict_2.keys())
print(f'Phần tử có key lớn top 2 = {dict_2[max_k3]}')