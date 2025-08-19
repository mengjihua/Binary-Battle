import timeit

# 测试用例
derived = [0, 1, 0, 1, 0, 1] * (10 ** 5)

# 测试 sum 方法
time_sum = timeit.timeit(lambda: sum(derived) % 2 == 0, number=1000)

# 测试 count 方法
time_count = timeit.timeit(lambda: derived.count(1) % 2 == 0, number=1000)

print(f"sum time: {time_sum:.6f}s")
print(f"count time: {time_count:.6f}s")
# 通常 time_sum < time_count
# 0 越多, time_sum 越小, time_count 越大