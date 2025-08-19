import time
import matplotlib.pyplot as plt

start = time.time()

x = [0.95, 3, 4, 5.07, 6.03, 8.21, 8.85, 12.02, 15]
y = [5.1, 8.7, 11.5, 13, 15.3, 18, 21, 26.87, 32.5]

# 参数定义
w = 1.5
b = 1.5
learningRate = 0.01
length = len(x)

# 使用批量梯度下降法
for num in range(10000):
    derivative_b = 0  # 导数
    derivative_w = 0  # 导数
    # 求导
    for i in range(length):
        derivative_w += - (w * x[i] + b - y[i]) * x[i] / length
        derivative_b += - (w * x[i] + b - y[i]) / length
    # delta w，delta b = 学习率 * 偏导数
    w = w + learningRate * derivative_w
    b = b + learningRate * derivative_b
    # 当偏导数非常小时（接近0），说明已经收敛，提前退出循环
    if derivative_w <= pow(10, -13) and derivative_b <= pow(10, -13):
        break

print("最佳拟合直线: y = {:.6f}x + {:.6f}".format(w, b))
end = time.time()
print("耗时：{:.4f} 秒".format(end - start))

# 可视化部分
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='原始数据')
plt.plot(x, [w * xi + b for xi in x], color='red', label='拟合直线')
plt.title('一元线性回归拟合结果')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()