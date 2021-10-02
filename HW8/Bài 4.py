dict_a = {
    1: 1,
    -1: 10,
    5: 6,
    4: 8
}
dict_b = {
    1: 1,
    -1: 5,
    2: 3,
    4: 8
}
for i in dict_a.keys():
    for j in dict_b.keys():
        if dict_a[i] == dict_b[j] and i == j:
            print(f'Phần tử xh trong 2 dict: {i}: {dict_a[i]}')