def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

class Solution(object):
    # def findTheDistanceValue(self, arr1, arr2, d):
    #     """
    #     :type arr1: List[int]
    #     :type arr2: List[int]
    #     :type d: int
    #     :rtype: int
    #     """
    #     count = 0
    #     for i in range(len(arr1)):
    #         judge = True
    #         for j in range(len(arr2)):
    #             if abs(arr1[i] - arr2[j]) <= d:
    #                 judge = False
    #                 break
    #         if judge: count += 1
    #     return count
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        for i in range(len(arr1)):
            idx = lower_bound(arr2, arr1[i] - d)
            if idx >= len(arr2) or arr2[idx] > d + arr1[i]:
                count += 1
        return count
    
    def findTheDistanceValue2(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        ans = j = 0
        for x in arr1:
            while j < len(arr2) and arr2[j] < x - d:
                j += 1
            if j == len(arr2) or arr2[j] > x + d:
                ans += 1
        return ans

if __name__ == '__main__':
    arr1 = [-8,-7]
    arr2 = [4,10,-4,5,2]
    d = 55
    print(Solution().findTheDistanceValue(arr1, arr2, d))
    print(Solution().findTheDistanceValue2(arr1, arr2, d))