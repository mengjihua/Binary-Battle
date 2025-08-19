from typing import List
# https://leetcode.cn/problems/maximum-points-inside-the-square/

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        INF = float('inf')
        min1 = INF
        min2 = [INF] * 26
        for i in range(len(s)):
            x, y = points[i]
            alp = ord(s[i]) - ord('a')
            d = max(abs(x), abs(y))
            if d < min2[alp]:
                min1 = min(min1, min2[alp])
                min2[alp] = d
            elif d < min1:
                min1 = d
            # print(d, min1, min2[alp])
        return sum(d < min1 for d in min2)
    
# Example usage:
solution = Solution()
points = [[1,1],[-2,-2], [3,3],[-4,-4]]
s = "abcd"
print(solution.maxPointsInsideSquare(points, s))  # Output: 1