# https://leetcode.cn/problems/count-number-of-ways-to-place-houses/

class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [2] + [0] * n
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)
            print(dp[i], dp[i - 1], dp[i - 2])
        return dp[n] * dp[n] % (10 ** 9 + 7)

if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.countHousePlacements(n))  # Output: 9