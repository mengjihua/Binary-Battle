from typing import List

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        def isPrime(n):
            vis = [False] * (n + 1)
            primes = []
            for i in range(2, n + 1):
                if not vis[i]:
                    primes.append(i)
                    vis[i] = True
                for prime in primes:
                    if i * prime > n: break
                    vis[i * prime] = True
                    if i % prime == 0: break
            return primes
        
        nums.sort()
        max_num = nums[-1]
        prime_set = set(isPrime(max_num))
        
        ans, l
        min_prime, max_prime = float('inf'), float('-inf')
        while r < len(nums):
            min_prime = min(min_prime, nums[r])
            max_prime = max(max_prime, nums[r])
            while l < r and nums[r] - nums[l] > k:
                l += 1
            if nums[r] - nums[l] <= k and nums[r] in prime_set:
                ans += 1
            r += 1
        return ans