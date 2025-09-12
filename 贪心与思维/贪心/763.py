from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c_num_map = [0] * 26
        for c in s:
            c_num_map[ord(c) - ord('a')] += 1

        n = len(s)
        ans = []
        l, r = 0, 0
        while l < n:
            for r in range(l, n):
                temp = s[l:r + 1]
                sub_map = [0] * 26
                for c in temp:
                    sub_map[ord(c) - ord('a')] += 1
                    
                judge = True
                for i in range(26):
                    if sub_map[i] != 0 and sub_map[i] != c_num_map[i]:
                        judge = False
                    
                if judge:
                    ans.append(temp)
                    l = r + 1
                    break
                else:
                    continue
            if not judge:
                l += 1
                  
        # print(ans)
        for i in range(len(ans)):
            ans[i] = len(ans[i])
        return ans
    
    def partitionLabels_plus(self, s: str) -> List[int]:
        c_num_map = [0] * 26
        for c in s:
            c_num_map[ord(c) - ord('a')] += 1

        n = len(s)
        ans = []
        l, r = 0, 0
        while l < n:
            sub_map = [0] * 26
            temp = ''
            for r in range(l, n):
                sub_map[ord(s[r]) - ord('a')] += 1
                temp += s[r]
                    
                judge = True
                for i in range(26):
                    if sub_map[i] != 0 and sub_map[i] != c_num_map[i]:
                        judge = False
                    
                if judge:
                    ans.append(temp)
                    l = r + 1
                    break
                else:
                    continue
            if not judge:
                l += 1
                  
        # print(ans)
        for i in range(len(ans)):
            ans[i] = len(ans[i])
        return ans
    
    def partitionLabels_plus_plus(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        ans = []
        l, r = 0, 0
        
        for i, c in enumerate(s):
            r = max(r, last[c])
            if i == r:
                ans.append(i - l + 1)
                l = i + 1
                
        return ans

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels_plus("ababcbacadefegdehijhklij"))