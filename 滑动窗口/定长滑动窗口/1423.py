from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans, s, n = 0, 0, len(cardPoints)
        for i in range(k):
            s += cardPoints[i]
            ans += cardPoints[i]
        
        for i in range(k):
            s -= cardPoints[k - 1 - i]
            s += cardPoints[n - i - 1]
            print(cardPoints[i], cardPoints[n - i - 1], s)
            ans = max(ans, s)
        
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxScore([1,79,80,1,1,1,200,1], 3))