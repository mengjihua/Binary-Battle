from typing import List
# https://leetcode.cn/problems/maximum-sum-with-at-most-k-elements/

class Solution:
    def maxSum1(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        dic = [(i, x) for i, row in enumerate(grid) for x in row]
        dic.sort(key=lambda x: x[1], reverse=True)

        ans = 0
        for row, x in dic:
            if k == 0:
                break
            if limits[row] > 0:
                limits[row] -= 1
                k -= 1
                ans += x
        return ans
    
    def maxSum2(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        temp = []
        for row_idx, row in enumerate(grid):
            temp.extend(sorted(row, reverse=True)[:limits[row_idx]])
            # print(f"row_idx: {row_idx}, row: {row}, {sorted(row, reverse=True)[:limits[row_idx]]}")
        # print(temp)
        temp.sort(reverse=True)
        return sum(temp[:k])

# Example usage:
solution = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
limits = [2,1,0]
k = 3
print(solution.maxSum1(grid, limits, k))  # Output: 11