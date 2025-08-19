class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        one_limit_low = n - (limit * 2) if n - (limit * 2) > 0 else 0
        one_limit_high = min(n, limit)
        # print(one_limit_low, one_limit_high)
        
        ans = 0
        for i in range(one_limit_low, one_limit_high + 1):
            two_limit_low = max(0, n - i - limit)
            cnt = min(limit - two_limit_low, n - i - two_limit_low) + 1
            # print(i, two_limit_low, cnt)
            ans += cnt
        return ans

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies(3, 3))
    # print(s.distributeCandies(5, 2))
    # print(s.distributeCandies(7, 4))