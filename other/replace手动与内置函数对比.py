import timeit

# 测试字符串
text = "a" * 1000 + "b" * 1000

# 内置 replace
def builtin_replace():
    return text.replace("b", "c")

# 手动实现 replace
def manual_replace(s, old, new):
    if old == "":
        return new.join(s[i:i+1] for i in range(len(s)+1))
    result = []
    start = 0
    while True:
        pos = s.find(old, start)
        if pos == -1:
            result.append(s[start:])
            break
        result.append(s[start:pos])
        result.append(new)
        start = pos + len(old)
    return ''.join(result)

def manual_replace_wrapper():
    return manual_replace(text, "b", "c")

# 测量时间
time_builtin = timeit.timeit(builtin_replace, number=10000)
time_manual = timeit.timeit(manual_replace_wrapper, number=10000)

print(f"内置 replace: {time_builtin:.4f} 秒")
print(f"手动 replace: {time_manual:.4f} 秒")
print(f"手动实现慢了 {time_manual / time_builtin:.2f} 倍")