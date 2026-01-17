print("-" + "-"*26 + "-")
print("|  智能学习档案生成器v2.0  |")
print("-" + "-"*26 + "-")

name = input("请输入你的姓名：")

while True:
    try:
        age = int(input("请输入你的年龄："))
        if 0 < age < 150:
            birth_year = 2026 - age
            break
        else:
            print("年龄要在1到149之间哦！")
    except:
        print("输错啦，得是数字！")

major = input("请输入你的专业（如：云计算/计算机网络技术）：")

hobby_input = input("输入兴趣，多个用逗号分开：")
hobby_list = hobby_input.split(",")
hobbies = []
for h in hobby_list:
    if h.strip() != "":
        hobbies.append(h.strip())

print("-" + "-"*26 + "-")
print(f"| 姓名: {name}")
print(f"| 年龄: {age}岁({birth_year}年出生)")
print(f"| 专业: {major}")
print("-" + "-"*26 + "-")

print("-" + "-"*26 + "-")
print(f"| 兴趣标签: {' | '.join(hobbies) if hobbies else '暂无'}")
print("-" + "-"*26 + "-")

print("-" + "-"*26 + "-")
print("| 成绩统计:")

while True:
    try:
        python = float(input("Python基础成绩："))
        if 0 <= python <= 100:
            break
        else:
            print("成绩得在0到100之间！")
    except:
        print("输数字啊！")

while True:
    try:
        ds = float(input("数据结构成绩："))
        if 0 <= ds <= 100:
            break
        else:
            print("成绩得在0到100之间！")
    except:
        print("输数字啊！")

while True:
    try:
        db = float(input("数据库原理成绩："))
        if 0 <= db <= 100:
            break
        else:
            print("成绩得在0到100之间！")
    except:
        print("输数字啊！")

total = python + ds + db
avg = total / 3

print(f"| • Python基础: {python:.1f}")
print(f"| • 数据结构: {ds:.1f}")
print(f"| • 数据库原理: {db:.1f}")
print(f"| • 总分: {total:.1f}")
print(f"| • 平均分: {avg:.1f}")
print("-" + "-"*26 + "-")

while True:
    try:
        days = int(input("已学习天数："))
        total_days = int(input("总目标天数："))
        if days >= 0 and total_days > 0 and days <= total_days:
            break
        else:
            print("天数输入不合理，请重新输入！")
    except:
        print("输数字！")

percent = (days / total_days) * 100
bar_total = 10
filled = int(bar_total * (days / total_days))
progress_bar = "■" * filled + "□" * (bar_total - filled)

print("-" + "-"*26 + "-")
print(f"| 学习进度: [{progress_bar}] {percent:.0f}% ({days}/{total_days}天)")
print("-" + "-"*26 + "-")