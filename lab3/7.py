x = int(input())
y = int(input())
if x > y:
    yu = 1
    while yu != 0:
        sh = x / y
        yu = x % y
        x = y
        y = yu
    print(x)
else:
    yu = 1
    while yu != 0:
        sh = y / x
        yu = y % x
        y = x
        x = yu
    print(y)
