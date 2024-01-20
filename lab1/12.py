def cube_root(x, epsilon=1e-6, max_iterations=100):
    guess = x / 3.0  # 初始猜测值

    for i in range(max_iterations):
        # 使用牛顿-拉弗森方法来更新猜测值
        guess = (2 * guess + x / (guess ** 2)) / 3.0

        # 检查是否已经足够接近
        if abs(guess ** 3 - x) < epsilon:
            return guess

    return guess  # 如果未达到足够接近的精度，返回当前猜测值


x = int(input())  # 要计算立方根的数
result = cube_root(x)
print(result)
