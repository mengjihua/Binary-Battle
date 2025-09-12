from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        pre = float('-inf')
        for x in nums:
            x = min(max(x - k, pre + 1), x + k)
            if x > pre:
                ans += 1
                pre = x
            print(pre, end=' ')
        return ans

# 测试
if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1,1,1,1,5,5,5]
    k = 3
    result = s.maxDistinctElements(nums, k)
    print('\n' + str(result))  # 输出: 10