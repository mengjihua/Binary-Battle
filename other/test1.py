n, m = map(int, input().split())

x_lst = [[float('inf'), 0] for _ in range(n + 1)]
y_lst = [[float('inf'), 0] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    x_lst[x][0], x_lst[x][1] = min(x_lst[x][0], y), max(x_lst[x][1], y)
    y_lst[y][0], y_lst[y][1] = min(y_lst[y][0], x), max(y_lst[y][1], x)

ans = 0
print(x_lst, y_lst)
for i in range(1, n + 1):
#     if (x_lst[i][0] == float('inf') and x_lst[i][1] == 0) or (y_lst[i][0] == float('inf') and y_lst[i][1] == 0):
#         continue
    ans = max(ans, x_lst[i][1] - x_lst[i][0], y_lst[i][1] - y_lst[i][1])
print(ans)