from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        # for i in range(n // 3):
        #     # print(i * 3 + 2)
        #     if nums[i * 3 + 2] - nums[i * 3] > k:
        #         return []
        #     ans.append(nums[i * 3:i * 3 + 3])
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i + 3])
        return ans

# 测试
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    k = 3
    print(Solution().divideArray(nums, k))
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    print(Solution().divideArray(nums, k))
    nums = [2,4,2,2,5,2]
    k = 2
    print(Solution().divideArray(nums, k))