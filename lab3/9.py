A = []
B = []
n = int(input())
for i in range(n):
    A.append(int(input()))
for i in range(n):
    B[i] = 1
    for j in range(n):
        if j != i:
            B[i] *= A[j]
