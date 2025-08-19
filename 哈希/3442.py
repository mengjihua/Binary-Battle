from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        dic = Counter(s)
        max_odd_cnt, min_even_cnt = -1, float('inf')
        for cnt in dic.values():
            if cnt % 2 == 1:
                max_odd_cnt = max(max_odd_cnt, cnt)
            else:
                min_even_cnt = min(min_even_cnt, cnt)
        return max_odd_cnt - min_even_cnt