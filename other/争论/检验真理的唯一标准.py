import random

# 1. 初始化number为0（和Java的int number = 0完全一致）
number = 0
# 2. 循环条件：number不等于5（对应Java的number != 5）
while number != 5:
    # 3. 复刻Java的 (int)(Math.random() * 10) 逻辑：
    #    - random.random() → 生成 [0.0, 1.0) 浮点数（等价Java Math.random()）
    #    - * 10 → 缩放为 [0.0, 10.0) 浮点数
    #    - int() 强转 → 截断小数部分（等价Java的(int)强制类型转换）
    random_float = random.random()  # 对应Math.random()
    # print(random_float)  # 打印生成的随机浮点数，便于调试
    scaled_float = random_float * 10  # 对应*10
    number = int(scaled_float)  # 对应(int)强转
    # 4. 打印结果（对应Java的System.out.println(number)）
    print(number)