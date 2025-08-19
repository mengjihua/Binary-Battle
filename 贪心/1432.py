class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        max_num, min_num = num, num
        
        for c in str_num:
            if c != '9':
                max_num = int(str_num.replace(c, '9'))
                break
        
        if str_num[0] != '1':
            min_num = int(str_num.replace(str_num[0], '1'))
        else:
            for c in str_num:
                if c > '1':
                    min_num = int(str_num.replace(c, '0'))
                    break
        
        print(max_num, min_num)
        return max_num - min_num

# 测试
if __name__ == '__main__':
    num = 555
    s = Solution()
    print(s.maxDiff(num))
    num = 9
    print(s.maxDiff(num))
    num = 111
    print(s.maxDiff(num))
    num = 9288
    print(s.maxDiff(num))