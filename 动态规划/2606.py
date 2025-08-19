from typing import List
# https://leetcode.cn/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # def str_convert_to_list(s: str, val: List[int], chars: str) -> List[int]:
        #     set_chars = set(chars)
        #     res = []
        #     for c in s:
        #         if c in set_chars:
        #             res.append(val[chars.index(c)])
        #         else:
        #             res.append(ord(c) - ord('a') + 1)
        #     return res

        # s = str_convert_to_list(s, vals, chars)
        # n = len(s)
        # dp = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = max(dp[i - 1] + s[i - 1], s[i - 1])
        # return max(dp)
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if s[i - 1] in chars:
                val = vals[chars.index(s[i - 1])]
            else:
                val = ord(s[i - 1]) - ord('a') + 1
            dp[i] = max(dp[i - 1] + val, val)
        return max(dp)