from typing import List

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find_root(x):
            if root[x] == x:
                return root[x]
            root[x] = find_root(root[x])
            return root[x]
        
        def merge(x, y):
            root_x, root_y = find_root(x), find_root(y)
            if root_x < root_y:
                root[root_y] = root_x
            else:
                root[root_x] = root_y
        
        def query(x, y):
            return find_root(x) == find_root(y)

        root = [i for i in range(26)]
        n, m = len(s1), len(baseStr)
        for i in range(n):
            ord_c1, ord_c2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            merge(ord_c1, ord_c2)
        
        print(root)
        
        ans = [''] * m
        for i in range(m):
            ord_c = ord(baseStr[i]) - ord('a')
            root_c = find_root(ord_c)
            ans[i] = chr(root_c + ord('a'))
        return ''.join(ans)

# 测试
if __name__ == "__main__":
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(Solution().smallestEquivalentString(s1, s2, baseStr))  # 输出: "makkek"