def count_upper_lower(str):
  count_a = 0
  count_A = 0
  for i in range(len(str)):
    if 'a' <= str[i] <= 'z':
      count_a += 1
    elif 'A' <= str[i] <= 'Z':
      count_A += 1
  print(f'Số chữ in thường à: {count_a}, Số chữ in hoa là: {count_A}')

print(count_upper_lower('Hieu'))