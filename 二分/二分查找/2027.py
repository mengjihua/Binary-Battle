from typing import List
from bisect import bisect_right

# https://leetcode.cn/problems/most-beautiful-item-for-each-query/
def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid][0] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
        # print(items)
        ans = [0] * len(queries)
        for i in range(len(queries)):
            idx = bisect_right(items, queries[i], key=lambda item: item[0]) - 1
            # print(idx)
            if idx == -1:
                ans[i] = 0
            else:
                ans[i] = items[idx][1]
        return ans
    
# Example usage:
solution = Solution()
items = [[10,1000]]
queries = [5]
print(solution.maximumBeauty(items, queries))