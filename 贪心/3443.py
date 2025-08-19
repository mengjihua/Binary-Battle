from collections import defaultdict

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans, dic = 0, defaultdict(int)
        for c in s:
            dic[c] += 1
            left = k
            def f(a: int, b: int) -> int:
                nonlocal left
                d = min(a, b, left)
                left -= d
                return abs(a - b) + d * 2
            ans = max(ans, f(dic['W'], dic['E']) + f(dic['N'], dic['S']))
        return ans             