class Solution:
    def robotWithString(self, s: str) -> str:
      n = len(s)
      # 计算后缀最小值
      suf_min = ['z'] * (n + 1)
      for i in range(n - 1, -1, -1):
          suf_min[i] = min(suf_min[i + 1], s[i])

      ans = []
      st = []
      for i, ch in enumerate(s):
          st.append(ch)
          while st and st[-1] <= suf_min[i + 1]:
              ans.append(st.pop())
      return ''.join(ans)