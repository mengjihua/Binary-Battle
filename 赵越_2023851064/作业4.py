def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("程序运行结果：")
for i in range(1, 21):
    print(f"{fibonacci(i):6}", end="")
    if i % 5 == 0:
        print()