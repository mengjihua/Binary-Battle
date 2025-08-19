from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        nums1, nums2 = nums.copy(), nums.copy()
        
        n = len(nums)
        judge = False
        
        cnt1 = 0 
        for i in range(n - 1):
            if nums1[i] == -1:
                nums1[i], nums1[i + 1] = nums1[i] * -1, nums1[i + 1] * -1
                cnt1 += 1
        if cnt1 <= k and nums1[n - 1] == 1:
            judge = True
        
        cnt2 = 0
        for i in range(n - 1):
            if nums2[i] == 1:
                nums2[i], nums2[i + 1] = nums2[i] * -1, nums2[i + 1] * -1
                cnt2 += 1
        if cnt2 <= k and nums2[n - 1] == -1:
            judge = True

        return judge

# 测试
if __name__ == '__main__':
    s = Solution()
    nums = [1,-1,1,-1,1]
    k = 3
    print(s.canMakeEqual(nums, k))
    