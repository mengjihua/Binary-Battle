from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        
        if n == 1:
            return nums[1]
        
        # 第一种情况, 不偷第一个房子, 则偷第2个到最后一个房子
        dp1 = [0] * (n + 1)
        for i in range(2, n + 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        
        # 第二种情况, 偷第一个房子, 则偷第3个到倒数第2个房子
        dp2 = [0] * n
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2]+ nums[i])
            
        # 取两种情况的最大值
        # print(dp1, dp2)
        return max(dp1[n], dp2[n - 1])

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1]
    print(solution.rob(nums))  # Output: 3