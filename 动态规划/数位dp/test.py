from functools import lru_cache

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        low, high = str(num1), str(num2)
        n = len(high)
        low = '0' * (n - len(low)) + low

        @lru_cache(maxsize=None)
        def dfs(depth: int, limit_low: bool, limit_high: bool) -> int:
            if depth == n:
                return 1
            
            lo = low[depth] if limit_low else 0
            hi = high[depth] if limit_high else 9

            res = 0
            for i in range(max(lo, min_sum), min(hi, max_sum)):
                res += dfs(depth + 1, limit_low and i == int(lo), limit_high and i == int(hi))
            return res

        return dfs(0, True, True)