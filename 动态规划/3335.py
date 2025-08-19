class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        cnt = [0] * 27
        for c in s:
            cnt[ord(c) - ord('a') + 1] += 1
        
        for _ in range(t):
            new_cnt = [0] * 27
            new_cnt[1] = cnt[26]
            new_cnt[2] = (cnt[26] + cnt[1]) % mod
            for i in range(3, 27):
                new_cnt[i] = cnt[i - 1]
            cnt = new_cnt
        ans = sum(cnt) % mod
        return ans

# Example usage:
solution = Solution()
s = "abc"
t = 2
print(solution.lengthAfterTransformations(s, t))  # Output: 3