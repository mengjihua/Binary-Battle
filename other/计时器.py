from time import time

# 初始化计时相关变量
start_time = time()
elapsed_paused_time = 0  # 累计暂停时长
is_paused = False       # 暂停状态标记
pause_start = 0         # 暂停开始时间

def display_runtime():
    """计算并显示当前运行时间(排除暂停时段）"""
    if is_paused:
        current_elapsed = pause_start - start_time - elapsed_paused_time
    else:
        current_elapsed = time() - start_time - elapsed_paused_time
    
    # 精确计算分钟和秒(保留1位小数）
    minutes = int(current_elapsed // 60)
    seconds = current_elapsed % 60
    
    # 格式化输出(秒数保留1位小数, 更精准）
    print(f"\n运行时间: {minutes} 分钟 {seconds:.1f} 秒")

def pause_timer():
    """暂停计时"""
    global is_paused, pause_start
    if not is_paused:
        pause_start = time()
        is_paused = True
        print("\n⏸️  计时已暂停")

def resume_timer():
    """恢复计时"""
    global is_paused, elapsed_paused_time
    if is_paused:
        elapsed_paused_time += time() - pause_start
        is_paused = False
        print("\n▶️  计时已恢复")

# 显示操作说明
print("=" * 50)
print("        计时工具(支持暂停/继续）")
print("=" * 50)
print("操作说明:")
print("  按 Enter 键    - 查看当前运行时间")
print("  输入 p 并回车  - 暂停计时")
print("  输入 r 并回车  - 恢复计时")
print("  输入 q 并回车  - 退出程序")
print("=" * 50)

# 主循环
while True:
    # 根据暂停状态显示不同的提示符
    prompt = "输入指令: "
    s = input(prompt).strip().lower()  # 忽略大小写和首尾空格
    
    if s == "":
        # 按Enter键显示运行时间
        display_runtime()
    elif s == "p":
        # 暂停计时
        pause_timer()
    elif s == "r":
        # 恢复计时
        resume_timer()
    elif s == "q":
        # 退出程序
        print("\n👋 程序已退出")
        display_runtime()  # 退出时显示最终运行时间
        break
    else:
        # 无效指令提示
        print("\n❌ 无效指令！请输入以下指令：")
        print("  Enter - 查看时间 | p - 暂停 | r - 继续 | q - 退出")