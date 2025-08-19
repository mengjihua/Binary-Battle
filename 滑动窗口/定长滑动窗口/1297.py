from typing import List
from collections import defaultdict

class Solution:
    # 哈希函数
    def Hash(self, t: str, mod: int) -> int:
        res = 0
        for c in t:
            res = (res * 26 + ord(c) - ord('a')) % mod
        return res
    
    # 计算t在s中出现的次数
    def count(self, s: str, t: str, hash: List[int], mod: int) -> int:
        m, n = len(t), len(s)
        res = 0
        numT = self.Hash(t, mod)
        p = pow(26, m, mod)
        for l in range(1, n + 1):
            r = l + m - 1
            if r > n:
                break
            if (hash[r] - hash[l - 1] * p % mod) % mod == numT:
                res += 1
        return res
    
    def del_out(self, dic: dict, out: str) -> None:
        dic[out] -= 1
        if dic[out] == 0:
            del dic[out]

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        mod = 10 ** 9 + 7 

        n = len(s)
        hash = [0]
        for c in s:
            hash.append((hash[-1] * 26 + ord(c) - ord('a')) % mod)
        
        dic = defaultdict(int)
        dic_cnt = defaultdict(int)
        ans = 0
        for r in range(n):
            dic[s[r]] += 1
            
            if r < minSize - 1:
                continue
    
            l = r - minSize + 1
            if len(dic) > maxLetters:
                self.del_out(dic, s[l])
                continue
            
            t = s[l:r + 1]
            dic_cnt[t] += 1
            ans = max(ans, dic_cnt[t])
            
            self.del_out(dic, s[l])
            
        return ans
            

s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
print(Solution().maxFreq(s, maxLetters, minSize, maxSize))