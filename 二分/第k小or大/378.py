from typing import List
# https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def check(self, x: int, matrix: List[List[int]], k: int) -> bool:
        cnt = 0
        i, j = 0, len(matrix) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= x:
                cnt += j + 1
                i += 1
            else:
                j -= 1
        return cnt >= k

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")
            if self.check(mid, matrix, k):
                r = mid - 1
            else:
                l = mid + 1
        return l

# 测试案例
solution = Solution()

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(solution.kthSmallest(matrix, k)) # 13