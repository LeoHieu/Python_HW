import random

num_1 = random.randrange(1, 7)
num_2 = random.randrange(1, 7)
sum_1 = num_1 + num_2

def next_roll(sum_1):
  num_3 = random.randrange(1, 7)
  num_4 = random.randrange(1, 7)
  sum_n = num_3 + num_4
  if sum_n == sum_1:
    print('Người chơi THẮNG')
    return True
  elif sum_n == 7:
    print('Người chơi THUA')
    return True
  else:
    return False

def first_roll(sum_1):
  if sum_1 == 7 or sum_1 == 11:
    print('Người chơi THẮNG')
  elif sum_1 == 2 or sum_1 == 3 or sum_1 == 12:
    print('Người chơi THUA')
  else:
    while True:
      if next_roll(sum_1):
        return


a = first_roll(sum_1)
