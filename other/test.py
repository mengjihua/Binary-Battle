from typing import List
import math

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digits_sum(num):
            return sum(map(int, str(num)))
        
        sorted_nums = sorted(nums, key=lambda x: (get_digits_sum(x), x))
        val_idx_map = {val: idx for idx, val in enumerate(sorted_nums)}
            
        n, cnt = len(nums), 0
        vis = [False] * n
        for i in range(n):
            if not vis[i]:
                j = i
                cycle_size = 0
                while not vis[j]:
                    vis[j] = True
                    j = val_idx_map[nums[j]]
                    cycle_size += 1
                if cycle_size > 0:
                    cnt += cycle_size - 1
        return cnt

if __name__ == '__main__':
    nums = [37,100]
    print(Solution().minSwaps(nums))
    
print(10 ** 8 * math.log(10 ** 8, 2))