# 初始猜测值
c = 10
x = c

# 定义迭代次数
iterations = 10  # 可以根据需要调整迭代次数

# 开始迭代
for _ in range(iterations):
    x = x - (x**3 - c) / (3 * x**2)

# 打印 c 的三次方根的近似值
print(f"{c}的三次方根的近似值: {x}")
