from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[l]

#测试
if __name__ == '__main__':
    nums = [3, 1, 2]
    s = Solution()
    print(s.findMin(nums))