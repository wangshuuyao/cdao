import random
import math

# 定义函数 f(x) = x^2 + 4x*sin(x)
def f(x):
    return x**2 + 4 * x * math.sin(x)

# 定义积分区间
a = 2
b = 3

# 设定采样点数量
num_samples = 1000000  # 可根据需要调整采样点数量

# 初始化累计和
integral_sum = 0

# 执行蒙特卡洛积分
for _ in range(num_samples):
    x = random.uniform(a, b)
    integral_sum += f(x)

# 计算估计的积分值
integral_estimate = (b - a) * (integral_sum / num_samples)

# 打印估计的积分值
print(f"估计的积分值: {integral_estimate:.6f}")
