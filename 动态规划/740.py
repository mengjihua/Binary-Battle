from typing import List
from functools import cache
# https://leetcode.cn/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        
        lst = []
        cnt, last = 1, nums[0]
        for i in range(1, len(nums)):
            if last != nums[i]:
                lst.append((last, cnt))
                last = nums[i]
                cnt = 1
            else:
                cnt += 1
        lst.append((last, cnt))
        # print(lst)
        
        # @cache
        # def f(depth, num, n, delnum):
        #     if depth == n:
        #         return num

        #     if lst[depth][0] == delnum:
        #         return f(depth + 1, num, n, delnum)
        #     # 选择删除
        #     a = f(depth + 1, num + lst[depth][0] * lst[depth][1], n, lst[depth][0] + 1)
        #     # 不删除
        #     b = f(depth + 1, num, n, delnum)

        #     return max(a, b)
        # return f(0, 0, len(lst), -1)
        n = len(lst)
        dp = [0] * (n + 1)
        dp[1] = lst[0][0] * lst[0][1]
        last = lst[0][0]
        for i in range(2, n + 1):
            if lst[i - 1][0] == last + 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + lst[i - 1][0] * lst[i - 1][1])
            else:
                dp[i] = dp[i - 1] + lst[i - 1][0] * lst[i - 1][1]
            last = lst[i - 1][0]
        # haiwaifgangnima1le1
        return dp[n]

# Test the function
if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,3,3,3,4]
    result = solution.deleteAndEarn(nums)
    print(result)  # Output: 9