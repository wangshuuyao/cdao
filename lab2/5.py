# 初始猜测值
c = 2  # 求解根号2
g = c / 2

# 定义迭代次数
iterations = 10  # 可以根据需要调整迭代次数

# 开始迭代
for _ in range(iterations):
    g = (g + c / g) / 2

# 打印根号c的近似值
print(f"根号{c}的近似值: {g}")
