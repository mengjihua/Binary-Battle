class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            for st in stacks:
                if st:
                    st.pop()
                    break
        
        n = len(s)
        ans = [''] * n
        for i in range(26):
            for idx in stacks[i]:
                ans[idx] = chr(i + ord('a'))
        return ''.join(ans)
    
    def clearStars(self, s: str) -> str:
        s = list(s)
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            for st in stacks:
                if st:
                    s[st.pop()] = '*'
                    break
        
        return ''.join(c if c != '*' else '' for c in s)