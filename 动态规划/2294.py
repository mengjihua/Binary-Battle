from typing import List

class Solution:
    # # 贪心不行
    # def partitionArray(self, nums: List[int], k: int) -> int:
    #     n, max_num, min_num = len(nums), [], []
    #     temp = [[] for _ in range(5)]

    #     for i in range(n):
    #         idx = 0
    #         while idx < len(max_num) and (max_num[idx] - nums[i] > k or nums[i] - min_num[idx] > k):
    #             idx += 1
    #         if idx >= len(max_num):
    #             max_num.append(nums[i])
    #             min_num.append(nums[i])
    #         else:
    #             max_num[idx] = max(max_num[idx], nums[i])
    #             min_num[idx] = min(min_num[idx], nums[i])
    #         temp[idx].append(nums[i])
                
    #     print(max_num, min_num)
    #     print(temp)
    #     return len(max_num)
    
    def partitionArray(self, nums: List[int], k: int) -> int:
        n, max_num = len(nums), max(nums)
        
        pre_sum = [0] * (max_num + 1)
        for i in range(n):
            pre_sum[nums[i]] += 1
        for i in range(1, max_num + 1):
            pre_sum[i] += pre_sum[i - 1]
    
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, start = 1, nums[0]
        for x in nums:
            if x - start > k:
                count += 1
                start = x
        return count
    

# 测试
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    print(Solution().partitionArray(nums, k))
    nums = [1, 2, 3]
    k = 1
    print(Solution().partitionArray(nums, k))
    nums = [16,8,17,0,3,17,8,20]
    k = 10
    print(Solution().partitionArray(nums, k))