def student_info(name, student_id, class_name="计算机1班", age=None, gender=None):
    return f"姓名: {name}，学号: {student_id}，班级: {class_name}，年龄: {age}，性别: {gender}"


def calculate_scores(student_name, *subjects, **scores):
    score_lines = []
    for sub in subjects:
        if sub in scores:
            score_lines.append(f"{sub}: {scores[sub]:.1f}")  # 保留1位小数

    total = sum(scores.values())
    avg = total / len(scores) if scores else 0

    result = f"学生: {student_name}\n"
    result += "\n".join(score_lines) + "\n"
    result += f"总成绩: {total:.2f}，平均成绩: {avg:.2f}"
    return result


print("=====成绩统计系统=====")
print("\n【调用学生信息函数】")

student1_info = student_info("张三", "2023001", age=18, gender="男")
print("第一名学生信息: ")
print(student1_info)

student2_info = student_info("李四", "2023002", "计算机三班", age=19, gender="男")
print("\n第二名学生信息: ")
print(student2_info)


print("\n【调用成绩计算函数】")
score1 = calculate_scores(
    "张三",
    "语文", "数学", "英语", "物理",
    语文=85.5, 数学=92.0, 英语=78.0, 物理=88.5
)
print(score1)

score2 = calculate_scores(
    "李四",
    "语文", "数学", "英语", "物理", "化学",
    语文=90.0, 数学=95.5, 英语=88.0, 物理=92.0, 化学=86.5
)
print("\n" + score2)


print("\n" + "="*50)
print("成绩统计完成")
