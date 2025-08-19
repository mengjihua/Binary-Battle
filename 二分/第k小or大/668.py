# https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def check(self, x: int, m: int, n: int, k: int) -> bool:
        cnt = 0
        for i in range(1, m + 1):
            cnt += min(x // i, n)
            # print(cnt, x // i, n)
        return cnt >= k

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, n * m
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")
            if self.check(mid, m, n, k):
                r = mid - 1
            else:
                l = mid + 1
        return l

# Example usage:
solution = Solution()
n, m, k = 3, 3, 5
print(solution.findKthNumber(n, m, k)) # Output: 3