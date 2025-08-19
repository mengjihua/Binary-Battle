class Solution:
    def answerString(self, s: str, k: int) -> str:
        if k == 1:
            return s
        n = len(s)
        return max(s[i: min(n, i + n - k + 1)] for i in range(n))

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.answerString("abacaba", 3))
    print(s.answerString("abcde", 2))
    print(s.answerString("aaaaaa", 4))
    print(s.answerString('xzr', 2))
    print(s.answerString("nbjnc", 2))
    print(s.answerString("gggg", 4))