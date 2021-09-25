A = [1, 2, 5, 7, 22, 14, 56, 72, 11, 32, 3, 25]
count = 0
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] > A[j] and i < j:
            count += 1
print(f'Số tập thỏa mãn biểu thức trên là: {count}')