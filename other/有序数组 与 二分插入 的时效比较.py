import timeit
import random
from sortedcontainers import SortedList
import bisect

def make_test_insort(m, rand_values):
    def test():
        sms = [0]
        sm = 0
        for i in range(m):
            sm += rand_values[i]
            bisect.insort(sms, sm)
        return len(sms)
    return test

def make_test_sortedlist(m, rand_values):
    def test():
        sms = SortedList([0])
        sm = 0
        for i in range(m):
            sm += rand_values[i]
            sms.add(sm)
        return len(sms)
    return test

# 参数设置
M_VALUES = [10, 50, 100, 200, 500, 1000, 5000, 10000, 20000]
REPEAT = 5
NUMBER = 10
SEED_BASE = 42

print(f"{'m':<6} {'insort (ms)':<15} {'SortedList (ms)':<15} {'Ratio':<10}")
print("-" * 50)

for m in M_VALUES:
    # 预生成随机数序列
    random.seed(SEED_BASE + m)
    rand_values = [random.randint(-10, 10) for _ in range(m)]

    test_insort_func = make_test_insort(m, rand_values)
    test_sortedlist_func = make_test_sortedlist(m, rand_values)

    # 测试
    times_insort = timeit.repeat(test_insort_func, repeat=REPEAT, number=NUMBER)
    avg_insort_ms = (min(times_insort) / NUMBER) * 1000

    times_sortedlist = timeit.repeat(test_sortedlist_func, repeat=REPEAT, number=NUMBER)
    avg_sortedlist_ms = (min(times_sortedlist) / NUMBER) * 1000

    ratio = avg_insort_ms / avg_sortedlist_ms if avg_sortedlist_ms > 0 else float('inf')
    
    print(f"{m:<6} {avg_insort_ms:<15.4f} {avg_sortedlist_ms:<15.4f} {ratio:<10.2f}x")