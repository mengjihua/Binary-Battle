from typing import List
from bisect import bisect_right

class Solution:
    def count_inversions(self, arr: List[int]) -> int:
        def merge_sort_count(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort_count(arr[:mid])
            right, inv_right = merge_sort_count(arr[mid:])
            merged, inv_merge = merge(left, right)
            total_inv = inv_left + inv_right + inv_merge
            return merged, total_inv

        def merge(left, right):
            i = j = 0
            merged = []
            inversions = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    inversions += len(left) - i
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inversions

        _, count = merge_sort_count(arr)
        return count
    
    # def minSwaps(self, nums: List[int]) -> int:
    #     evens = [x for x in nums if x % 2 == 0]
    #     odds = [x for x in nums if x % 2 == 1]
    #     n = len(nums)

    #     if n % 2 == 0:
    #         if len(evens) != len(odds):
    #             return -1
    #     else:
    #         if abs(len(evens) - len(odds)) != 1:
    #             return -1

    #     def count_swaps(pattern):
    #         target_type = 0 if pattern else 1
    #         res_indices = []

    #         for i, num in enumerate(nums):
    #             if num % 2 == target_type:
    #                 res_indices.append(i)
    #             if len(res_indices) == (n + 1) // 2:
    #                 break

    #         return count_inversions(res_indices)

    #     def count_inversions(arr):
    #         max_val = max(arr) + 2
    #         tree = [0] * (max_val + 1)

    #         def update(x):
    #             while x < len(tree):
    #                 tree[x] += 1
    #                 x += x & -x

    #         def query(x):
    #             res = 0
    #             while x > 0:
    #                 res += tree[x]
    #                 x -= x & -x
    #             return res

    #         inv_count = 0
    #         for i in reversed(arr):
    #             inv_count += query(i - 1)
    #             update(i + 1)
    #         return inv_count

    #     res = float('inf')
    #     if len(evens) > len(odds):
    #         res = min(res, count_swaps(True))
    #     elif len(odds) > len(evens):
    #         res = min(res, count_swaps(False))
    #     else:
    #         res = min(count_swaps(True), count_swaps(False))

    #     return res
    
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        evens = []
        odds = []
        element_to_index = {}
        for idx, num in enumerate(nums):
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
            element_to_index[num] = idx
        
        count_even = len(evens)
        count_odd = len(odds)
        
        if n % 2 == 0:
            if count_even != count_odd:
                return -1
        else:
            if abs(count_even - count_odd) != 1:
                return -1
                
        min_swaps = float('inf')
        
        if n % 2 == 0 or count_even > count_odd:
            B = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    B[i] = evens[i // 2]
                else:
                    B[i] = odds[i // 2]
            pos_B = [element_to_index[B[i]] for i in range(n)]
            swaps_A = self.count_inversions(pos_B)
            min_swaps = min(min_swaps, swaps_A)
        
        if n % 2 == 0 or count_odd > count_even:
            B = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    B[i] = odds[i // 2]
                else:
                    B[i] = evens[i // 2]
            pos_B = [element_to_index[B[i]] for i in range(n)]
            swaps_B = self.count_inversions(pos_B)
            min_swaps = min(min_swaps, swaps_B)
        
        return min_swaps
    
if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps([2,4,6,5,7]))  # 输出: 3
    print(s.minSwaps([2,4,5,7]))    # 输出: 1
    print(s.minSwaps([1,2,3]))      # 输出: 0
    print(s.minSwaps([4,5,6,8]))    # 输出: -1