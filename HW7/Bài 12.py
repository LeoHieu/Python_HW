set_1 = {1, 3, 5, 6, 7, 9, 10}
set_2 = {2, 4, 6, 8, 10}
set_1.difference_update(set_2)
print(set_1)

set_3 = {2, 3, 1, 87, 43, 6, 10}
set_4 = {99, 0, 87, 3, 8, 9}
set_3.intersection_update(set_4)
print(set_3)

print(set_1.isdisjoint(set_2))
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))
set_1.symmetric_difference_update(set_2)
print(set_1)