import bisect

a = [1, 3, 3, 5, 7]
x = 7
print(bisect.bisect_left(a, x))  
print(bisect.bisect_right(a, x))  
print(pow(2, 16) * 16 * 16)

ans = 1
for i in range(1, 12):
    ans *= i
print(ans)

from math import log
print(log(10 ** 9, 2))


print(-1 % 26, 25 % 26)