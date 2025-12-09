from time import time
# 从运行开始, 如果按下enter键, 则显示运行时间: 多少分钟多少秒
start_time = time()

def display_runtime():
    elapsed_time = time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"运行时间: {minutes} 分钟 {seconds} 秒")

while True:
    s = input("按下Enter键显示运行时间..., 或输入其他内容退出: ")
    if s != "":
        break
    display_runtime()