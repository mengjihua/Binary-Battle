lst = []

print("=== 数字处理系统 ===")

while True:
    try:
        input_str = input("请输入一组整数, 用空格分隔：")
        lst = list(map(int, input_str.split()))
        break
    except ValueError:
        print("输入错误!请输入整数并以空格分隔~")
        
while True:
    print("\n" + "="*30)
    print("请选择操作：")
    print("1) 显示所有正数")
    print("2) 显示所有负数")
    print("3) 计算并显示所有偶数的平方")
    print("4) 计算并显示所有奇数的立方")
    print("5) 显示大于平均值的数字")
    print("6) 重新输入数字")
    print("7) 退出程序")
    print("="*30)
    
    choice = input("选择：")
    print('\n')
    
    if choice == "1":
        positives = [num for num in lst if num > 0]
        print(f"所有正数：{positives}")
    elif choice == "2":
        negatives = [num for num in lst if num < 0]
        print(f"所有负数：{negatives}")
    elif choice == "3":
        even_squares = [num**2 for num in lst if num % 2 == 0]
        print(f"偶数的平方：{even_squares}")
    elif choice == "4":
        odd_cubes = [num**3 for num in lst if num % 2 != 0]
        print(f"奇数的立方：{odd_cubes}")
    elif choice == "5":
        avg = sum(lst) / len(lst)
        above_avg = [num for num in lst if num > avg]
        print(f"平均值：{avg:.2f}")
        print(f"大于平均值的数字：{above_avg}")
    elif choice == "6":
        while True:
            try:
                input_str = input("请输入一组整数, 用空格分隔：")
                lst = list(map(int, input_str.split()))
                print(f"已更新数字列表：{lst}")
                break
            except ValueError:
                print("输入错误!请输入整数并以空格分隔~")
    elif choice == "7":
        print("感谢使用数字处理系统, 再见!")
        break
    else:
        print("选择无效!请输入1-7之间的数字~")