l = input()
s = []
for i in range(len(l)):
    if l[i] == ' ':
        continue
    s.append(l[i])
for i in range(len(s)):
    print(s[i],end='')
