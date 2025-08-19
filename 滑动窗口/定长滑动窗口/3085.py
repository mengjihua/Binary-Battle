from collections import Counter
from bisect import bisect_right

class Solution:
    # def minimumDeletions(self, word: str, k: int) -> int:
    #     cnt = sorted(Counter(word).values())
    #     max_save = 0
    #     for i, base in enumerate(cnt):
    #         s = sum(min(c, base + k) for c in cnt[i:])
    #         max_save = max(max_save, s)
    #     return len(word) - max_save
    
    # 滑动窗口
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = sorted(Counter(word).values())
        n = len(cnt)
        
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + cnt[i - 1]
            
        # print(cnt, pre_sum)
        max_save = 0
        for l in range(n):
            base = cnt[l]
            r = bisect_right(cnt, base + k)
            max_save = max(max_save, pre_sum[r] - pre_sum[l] + (n - r) * (base + k)) 
            
        return len(word) - max_save

if __name__ == "__main__":
    s = Solution()
    print(s.minimumDeletions("dabdcbdcdcd", 2))  # 2
    print(s.minimumDeletions("aabbcc", 1))  # 0