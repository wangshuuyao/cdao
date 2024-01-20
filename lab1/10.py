l = input()

for i in range(len(l) - 1):
    if (l[i] == l[i + 1]):
        print("True")
        break
else:
    print("False")
