from typing import List                                  

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        ans = 0
        last_num = 0
        for i in range(n):
            num = 0
            for c in bank[i]:
                if c == '1':
                    num += 1
            ans += num * last_num
            if num > 0:
                last_num = num
        return ans