from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, m = len(s), len(wordDict)
        
        @lru_cache(maxsize = None)
        def dfs(depth: int) -> bool:
            if depth == n:
                return True
            
            for i in range(m):
                word = wordDict[i]
                word_len = len(word)
                
                if depth + word_len <= n and s[depth:depth + word_len] == word:
                    if dfs(depth + word_len):
                        return True
            return False
    
        return dfs(0)
    
# 测hi试
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))  # 输出: True