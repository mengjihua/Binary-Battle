# https://leetcode.cn/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            # print(i, dp[i], dp[i - zero], dp[i - one])
        return sum(dp[low:high + 1]) % (10 ** 9 + 7)

# Test the function
if __name__ == "__main__":
    solution = Solution()
    low = 2
    high = 3
    zero = 1
    one = 2
    print(solution.countGoodStrings(low, high, zero, one))