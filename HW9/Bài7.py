def body_mass_index(m, h):
  BMI = m / (h * 2)
  print(f'Chỉ số BMI: {BMI}')
  return BMI

def bmi_information(m, h):
  BMI = m / (h * 2)
  if BMI < 18.5:
    print('Gầy')
  elif 18.5 <= BMI <= 24.9:
    print('Bình thường')
  elif 24.9 < BMI <= 29.9:
    print('Béo phì độ 1')
  elif 29.9 < BMI:
    print('Béo phì độ 2')

x = body_mass_index(56, 1.67)
y = bmi_information(56, 1.67)