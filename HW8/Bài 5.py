dict_5 = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
new_dict = dict_5.fromkeys(keys)
for i in new_dict:
    new_dict[i] = dict_5[i]
print(new_dict)