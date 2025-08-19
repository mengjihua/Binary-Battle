from typing import List
# https://leetcode.cn/problems/split-array-largest-sum/

class Solution:
    def check(self, x: int, m: int, pre_sum: List[int]) -> bool:
        cnt = 0
        l, r = 1, 1
        while r < len(pre_sum):
            while r < len(pre_sum) and pre_sum[r] - pre_sum[l - 1] <= x:
                r += 1
            if r != len(pre_sum):
                # print(f"l: {l}, r: {r}, pre_sum[r]: {pre_sum[r]}, pre_sum[l - 1]: {pre_sum[l - 1]}, sum: {pre_sum[r] - pre_sum[l - 1]}")
                cnt += 1
                l = r
            if cnt >= m:
                break
        if r != len(pre_sum):
            return False
        return True

    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        l, r = max(max(nums), sum(nums) // m), sum(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        # print(f"pre_sum: {pre_sum}")
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")
            if self.check(mid, m, pre_sum):
                r = mid - 1
            else:
                l = mid + 1
        return l

# Example usage:
solution = Solution()
nums = [7,2,5,10,8]
m = 2
print(solution.splitArray(nums, m))  # Output: 18