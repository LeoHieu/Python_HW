n = int(input('Nhập vào số nguyên dương n: '))

def numbers(n):
  p = n + 1
  i = 2
  if p <= 1:
      return False
  elif p == 2:
      return p
  else:
      while i < p:
          if p % i == 0:
            p += 1
            i = 2
          else:
            i += 1
      return p


print(f'Số nguyên tố bé nhất lớn hơn n là: {numbers(n)}')
