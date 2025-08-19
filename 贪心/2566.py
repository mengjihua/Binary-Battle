class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = list(str(num))
        min_target = str_num[0]
        max_num, min_num = [], []
        for i in range(len(str_num)):
            if str_num[i] == min_target:
                min_num.append('0')
            else:
                min_num.append(str_num[i])
        max_target = str_num[0]
        for i in range(len(str_num)):
            if str_num[i] != '9':
                max_target = str_num[i]
                break
        for i in range(len(str_num)):
            if str_num[i] == max_target:
                max_num.append('9')
            else:
                max_num.append(str_num[i])
        # print(max_num, min_num)
        return int(''.join(max_num)) - int(''.join(min_num))

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.minMaxDifference(90))  
    print(s.minMaxDifference(11891))