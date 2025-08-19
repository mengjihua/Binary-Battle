from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        
        ans = 0
        cnt = defaultdict(int)
        for sj in pre_sum:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans