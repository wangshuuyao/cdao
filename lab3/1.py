x = float(input())
zhen_part = int(x)
xiao_part = x - zhen_part
zhen_part = bin(zhen_part).replace("0b", "")
y = ""
maxfractiondigits = 10
while xiao_part > 0 and len(y) < maxfractiondigits:
    xiao_part *= 2
    y += str(int(xiao_part))
    xiao_part -= int(xiao_part)
if y == "":
    binary_representation = zhen_part
else:
    binary_representation = f"{zhen_part}.{y}"

print(f"十进制小数 {x} 的二进制表示为 {binary_representation}")
