import timeit
import numpy as np  # 仅用于生成更复杂的访问模式，非必需

# ---------------------------- 配置测试参数 ----------------------------
# 数组大小（可以根据需要调整）
M, N = 1000, 1000  # 100万元素
# 测试循环次数
NUM_RUNS = 1000
# 访问模式：测试多少个随机位置
NUM_ACCESSES = 10000

# ---------------------------- 生成随机访问索引 ----------------------------
# 为了模拟真实访问，我们生成一组随机的 (i, j) 索引
np.random.seed(42)  # 固定随机种子，保证两次测试访问相同位置
access_indices = [(np.random.randint(0, M), np.random.randint(0, N)) 
                  for _ in range(NUM_ACCESSES)]

# ---------------------------- 测试函数 ----------------------------

def create_and_access_int_array():
    """创建 [[0]*n for _ in range(m)] 并进行多次访问"""
    # 创建数组
    vis = [[0] * N for _ in range(M)]
    # 模拟访问（读取和写入）
    for i, j in access_indices:
        # 读取
        _ = vis[i][j]
        # 写入（模拟标记访问）
        vis[i][j] = 1
    return vis

def create_and_access_bool_array():
    """创建 [[False]*n for _ in range(m)] 并进行多次访问"""
    # 创建数组
    vis = [[False] * N for _ in range(M)]
    # 模拟访问（读取和写入）
    for i, j in access_indices:
        # 读取
        _ = vis[i][j]
        # 写入（模拟标记访问）
        vis[i][j] = True
    return vis

def create_only_int_array():
    """仅测试创建 [[0]*n for _ in range(m)] 的速度"""
    vis = [[0] * N for _ in range(M)]
    return vis

def create_only_bool_array():
    """仅测试创建 [[False]*n for _ in range(m)] 的速度"""
    vis = [[False] * N for _ in range(M)]
    return vis

# ---------------------------- 运行测试 ----------------------------
print(f"测试配置: 数组大小 {M}x{N} = {M*N:,} 元素, 访问 {NUM_ACCESSES} 次, 运行 {NUM_RUNS} 轮")

# 测试创建 + 访问 的总时间
time_int_total = timeit.timeit(create_and_access_int_array, number=NUM_RUNS)
time_bool_total = timeit.timeit(create_and_access_bool_array, number=NUM_RUNS)

print(f"\n--- 测试: 创建 + 读写访问 ---")
print(f"int (0/1) 数组 总耗时: {time_int_total:.4f} 秒")
print(f"bool (F/T) 数组 总耗时: {time_bool_total:.4f} 秒")
print(f"差异: {((time_int_total - time_bool_total) / time_bool_total * 100):+.2f}% "
      f"({'int更快' if time_int_total < time_bool_total else 'bool更快'}，但差异极小)")

# 测试仅创建的时间（更纯粹地比较创建开销）
time_int_create = timeit.timeit(create_only_int_array, number=NUM_RUNS)
time_bool_create = timeit.timeit(create_only_bool_array, number=NUM_RUNS)

print(f"\n--- 测试: 仅创建数组 ---")
print(f"int (0/1) 数组 创建耗时: {time_int_create:.4f} 秒")
print(f"bool (F/T) 数组 创建耗时: {time_bool_create:.4f} 秒")
print(f"差异: {((time_int_create - time_bool_create) / time_bool_create * 100):+.2f}% "
      f"({'int更快' if time_int_create < time_bool_create else 'bool更快'}，但差异极小)")