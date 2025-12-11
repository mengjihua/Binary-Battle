while True:
    try:
        year = int(input("请输入一个年份: "))
        break
    except ValueError:
        print("输入错误！请输入整数年份. ")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year!")
else:
    print("This is not a leap year!")