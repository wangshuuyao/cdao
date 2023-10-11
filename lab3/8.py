import random
import time


# 生成随机数列的函数
def generate_random_list(n):
    return [random.randint(0, 1000) for _ in range(n)]


# 选择排序算法
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# 归并排序算法
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 测试不同排序算法在不同长度数列下的运行效果
for n in [100, 500, 1000, 5000, 10000]:
    lst = generate_random_list(n)
    start = time.time()
    selection_sort(lst.copy())
    end = time.time()
    print(f"选择排序, 长度{n}, 时间{end - start:.6f}秒")

    lst = generate_random_list(n)
    start = time.time()
    merge_sort(lst.copy())
    end = time.time()
    print(f"归并排序, 长度{n}, 时间{end - start:.6f}秒")

# 对于大数据量的排序，归并排序的效果通常要优于选择排序，归并排序的时间复杂度为O(nlogn)，而选择排序的时间复杂度为O(n^2)。
