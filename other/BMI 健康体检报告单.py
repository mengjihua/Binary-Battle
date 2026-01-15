name = input("请输入您的姓名：")
exam_id = int(input("请输入您的体检编号(整数, 如7): "))
height = float(input("请输入您的身高(米, 如1.75): "))
weight = float(input("请输入您的体重(千克, 如65.5): "))

bmi = weight / (height * height)

formatted_id = f"No.{exam_id:03d}"
formatted_bmi = f"{bmi:.1f}"

print(f"{name} | {formatted_id} | BMI:{formatted_bmi}")