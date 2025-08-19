from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set_str = set('aeiou')
        n, ans = len(s), 0
        dp = [0] * (n - k + 1)
        for i in range(n):
            if i < k:
                if s[i] in set_str:
                    dp[0] += 1
            else:
                add = 0
                if s[i] in set_str:
                    add += 1
                if s[i - k] in set_str:
                    add -= 1
                dp[i - k + 1] = dp[i - k] + add
                
        # print(dp)
        return max(dp)

# Example usage:
s = "abciiidef"
k = 3
solution = Solution()
print(solution.maxVowels(s, k))