from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[] for _ in range(len(strs))]
        str_idx_map = defaultdict(int)
        
        idx = 0
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in str_idx_map:
                str_idx_map[sorted_s] = idx
                idx += 1
            # print(str_idx_map[sorted_s], sorted_s, s, ans)
            ans[str_idx_map[sorted_s]].append(s)
        return ans[:len(str_idx_map)]

# 测试
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))