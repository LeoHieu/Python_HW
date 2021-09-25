import random
list = [1, 2, 9, [3, 4], 5, 'hello', 34]
a = random.choice(list)
new_list = []
while len(new_list) < 5:
    new_list.append(random.choice(list))
print(new_list)