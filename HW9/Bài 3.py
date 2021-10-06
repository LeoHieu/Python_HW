def is_perfect(n):
    list_3 = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            list_3.append(i)
    for j in list_3:
        sum += j
    if sum == n:
        print(f'{n} là số hoàn hảo: True')
    else:
        print(f'{n} là số hoàn hảo: False')

x = is_perfect(496)