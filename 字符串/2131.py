from typing import List
from collections import defaultdict
# https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/?envType=daily-question&envId=2025-05-25

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        temp = defaultdict(int)
        
        for word in words:
            if word[::-1] in temp:
                ans += 4
                temp[word[::-1]] -= 1
                if temp[word[::-1]] == 0:
                    del temp[word[::-1]]
            else:
                temp[word] += 1
        
        for word in temp:
            # print(word, temp[word])
            if word[0] == word[1]:
                ans += 2
                break
        
        return ans

# 测试
if __name__ == '__main__':
    words = ["lc", "cl", "gg"]
    print(Solution().longestPalindrome(words))