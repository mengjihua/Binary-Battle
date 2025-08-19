class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        n = len(s)
        ans = []
        for l in range(n):
            for r in range(l, n):
                num = int(s[l:r + 1])
                if is_prime(num):
                    ans.append(num)
        ans = list(set(ans)) 
        ans.sort(reverse=True)
        
        if len(ans) < 3:
            return sum(ans)
        else:
            return sum(ans[:3])