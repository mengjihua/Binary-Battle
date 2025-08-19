from typing import List

class Solution:
    def check(self, x: int, days: int, weights: List[int]) -> bool:
        cnt = 0
        total = 0
        for i in range(len(weights)):
            total += weights[i]
            # print(f"i: {i}, total: {total}, cnt: {cnt}")
            if total > x:
                cnt += 1
                total = weights[i]
        if total > 0:
            cnt += 1
        return cnt <= days
            
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights.sort()
        # print(f"weights: {weights}")
        l, r = max(weights), sum(weights)
        # l, r = 6, 6
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}, judge: {self.check(mid, days, weights)}")
            if self.check(mid, days, weights):
                r = mid - 1
            else:
                l = mid + 1
        return l
    
# Example usage:
solution = Solution()
# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
# print(solution.shipWithinDays(weights, days))  # Output: 15
weights = [3,2,2,4,1,4]
days = 3
print(solution.shipWithinDays(weights, days))  # Output: 6