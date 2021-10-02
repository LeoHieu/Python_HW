list_9 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(list_9)
dict_9 = {}
for i in list_9:
    dict_9.setdefault(i['item'], 0)
    dict_9[i['item']] += i['amount']
print(dict_9)