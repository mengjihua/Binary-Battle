from typing import List
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 2  # 除掉最后一个元素，不影响结果
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r + 1]:
                r = mid - 1
            elif nums[mid] > nums[r + 1]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]

#测试
if __name__ == '__main__':
    s = Solution()
    nums = [3,1,3]
    print(s.findMin(nums))