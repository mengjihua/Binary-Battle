class Solution:
    def maxSubstrings(self, word: str) -> int:
        # 求首尾相同, 且长度>= minlength, 并且不能相交的子字符串个数
        n = len(word)
        chr_map = [[] for _ in range(26)]
        bound, ans = -1, 0
        for r, c in enumerate(word):
            if len(chr_map[ord(c) - ord('a')]) == 0:
                chr_map[ord(c) - ord('a')].append(r)
                continue
            else:
                idx = len(chr_map[ord(c) - ord('a')]) - 1
                l = chr_map[ord(c) - ord('a')][idx]
            while l > bound and r - l < 3 and idx > 0:
                idx -= 1
                l = chr_map[ord(c) - ord('a')][idx]
            if l > bound and r - l >= 3:
                ans += 1
                bound = r
            chr_map[ord(c) - ord('a')].append(r)
        return ans
                
# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubstrings("abcdeafdef"))
    print(s.maxSubstrings("bcdaaaab"))