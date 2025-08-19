from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low, high = str(start), str(finish)
        n = len(high)
        low = '0' * (n - len(low)) + low
        diff = n - len(s)
        
        @lru_cache(None)
        def dfs(depth: int, limit_low: bool, limit_high: bool) -> int:
            if depth == n:
                return 1
        
            lo = int(low[depth]) if limit_low else 0
            hi = int(high[depth]) if limit_high else 9
            
            res = 0
            if depth < diff:
                for i in range(lo, min(hi, limit) + 1):
                    res += dfs(depth + 1, limit_low and i == lo, limit_high and i == hi)
            else:
                # print(i, diff, i - diff)
                x = int(s[depth - diff])
                if lo <= x <= min(hi, limit):
                    res = dfs(depth + 1, limit_low and x == lo, limit_high and x == hi)
            return res
        
        return dfs(0, True, True)

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.numberOfPowerfulInt(1, 6000, 4, '124'))