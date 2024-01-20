w, x, y, z = [int(i) for i in input().split()]
a = [w, x, y, z]
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i])
