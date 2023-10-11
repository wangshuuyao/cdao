# 初始猜测值
g = 1.0

# 容差
tolerance = 1e-5

# 循环直到找到所要的g
while abs(g * g - 2) > tolerance:
    g = (g + 2 / g) / 2

print(f"根号2的近似值: {g}")
