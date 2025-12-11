print("100~1000之间的水仙花数有: ")
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    if hundreds ** 3 + tens ** 3 + units ** 3 == num:
        print(num)