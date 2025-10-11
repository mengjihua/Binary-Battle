import time
import random
from typing import List

# 生成随机短数组：长度 1~3，元素为 0~10 的整数
def generate_random_list() -> List[int]:
    length = random.randint(1, 3)
    return [random.randint(0, 10) for _ in range(length)]

# --- 使用 break ---
def use_break(arr: List[int], threshold: int = 5) -> int:
    total = 0
    for x in arr:
        if x > threshold:
            break  # 遇到第一个大于 threshold 的就退出
        total += x
    return total

# --- 使用 continue ---
def use_continue(arr: List[int], threshold: int = 5) -> int:
    total = 0
    for x in arr:
        if x > threshold:
            continue  # 跳过，但继续下一个（如果还有）
        total += x
    return total

# --- 测试函数 ---
def benchmark(n_trials: int = 1000000):
    print(f"Running {n_trials:,} trials...\n")
    
    # 预生成所有测试数据，避免 random 影响时间测量
    test_cases = [generate_random_list() for _ in range(n_trials)]
    
    # === 测试 break 版本 ===
    start = time.perf_counter()
    result_break = 0
    for arr in test_cases:
        result_break += use_break(arr)
    time_break = time.perf_counter() - start
    
    # === 测试 continue 版本 ===
    start = time.perf_counter()
    result_continue = 0
    for arr in test_cases:
        result_continue += use_continue(arr)
    time_continue = time.perf_counter() - start
    
    # === 输出结果 ===
    print(f"Results:")
    print(f"  break    total: {result_break}")
    print(f"  continue total: {result_continue}")
    print(f"  Results match? {result_break == result_continue}")
    
    print(f"\nPerformance:")
    print(f"  break      : {time_break * 1000:.2f} ms")
    print(f"  continue   : {time_continue * 1000:.2f} ms")
    print(f"  Difference : {abs(time_break - time_continue) * 1000:.2f} ms")
    
    if time_break < time_continue:
        print(f"✅ break is faster by {((time_continue / time_break) - 1)*100:.1f}%")
    else:
        print(f"✅ continue is faster by {((time_break / time_continue) - 1)*100:.1f}%")

# --- 运行测试 ---
if __name__ == "__main__":
    random.seed(42)  # 固定种子，保证可复现
    benchmark(1_000_000)