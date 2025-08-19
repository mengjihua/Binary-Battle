from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(mid: int) -> bool:
            cnt = 0
            l, r = 0, 1
            while l < len(nums) -1:
                while r <= len(nums) - 1 and nums[r] - nums[l] <= mid:
                    r += 1
                # print(f'l: {l}, r: {r}, mid: {mid}, nums[r] - nums[l]: {nums[r] - nums[l]}')
                # if r <= len(nums) - 1:
                #     cnt += r - l - 1
                cnt += r - l - 1
                l += 1
            print(cnt, k)
            return cnt >= k

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
    
    
# 测试案例
if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    solution = Solution()
    print(solution.smallestDistancePair(nums, k))
    nums = [1,6,1]
    k = 3
    print(solution.smallestDistancePair(nums, k))