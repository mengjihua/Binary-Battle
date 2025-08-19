# from collections import Counter

def cal_f(letters):
    n = len(letters)
    res = [0] * n
    for i in range(n):
        s = sorted(letters[i])
        c, count = s[0], 0
        for j in range(len(s)):
            if s[j] == c:
                count += 1
            else:
                break
        letters[i] = count
    return letters
        

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        queries_f = cal_f(queries)
        words_f = sorted(cal_f(words))
        # print(queries_f, words_f)
        answer = [0] * len(queries_f)
        for i in range(len(queries_f)):
            num = queries_f[i]
            l, r = 0, len(words_f) - 1
            while l <= r:
                mid = (l + r) // 2
                if words_f[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            # print(l, r)
            answer[i] = len(words) - l
        return answer
    
    def f(self, s):
        cnt = 0
        ch = 'z'
        for c in s:
            if c < ch:
                ch = c
                cnt = 1
            elif c == ch:
                cnt += 1
        return cnt    

    def numSmallerByFrequency2(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        count = [0] * 12
        for s in words:
            count[self.f(s)] += 1
        for i in range(9, 0, -1):
            count[i] += count[i + 1]
        res = []
        for s in queries:
            res.append(count[self.f(s) + 1])
        return res

# Test case
if __name__ == "__main__":
    solution = Solution()
    queries = ["bbb","cc"]
    words = ["a","aa","aaa","aaaa"]
    print(solution.numSmallerByFrequency(queries, words))  # Output: [1]