from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        def dfs(i, num1, num2):
            if i == n and num1 == target and num2 == target:
                return True
            elif i == n:
                return False
            
            judge1, judge2 = False, False
            
            # print(target, num1, num2, nums[i])
            if (target // num1) % nums[i] == 0:
                judge1 = dfs(i + 1, num1 * nums[i], num2)
            if (target // num2) % nums[i] == 0:
                judge2 = dfs(i + 1, num1, num2 * nums[i])
            if not judge1 and not judge2:
                return False

            return judge1 or judge2

        return dfs(0, 1, 1) 
    
# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.checkEqualPartitions([11,22,5,10], 110))