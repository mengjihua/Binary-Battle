from typing import List
from collections import defaultdict


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        
        dic_x = defaultdict(int)
        for idx in range(n):
            if x[idx] in dic_x:
                num = dic_x[x[idx]]
                if y[idx] > num:
                    dic_x[x[idx]] = y[idx]
                else:
                    continue
            else:
                dic_x[x[idx]] = y[idx]

        lst = sorted(dic_x.values(), reverse=True)
        if len(lst) < 3:
            return -1
        return lst[0] + lst[1] + lst[2]


# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.maxSumDistinctTriplet([1,2,1,3,2] , [5,3,4,6,2] ))
    x = [1,2,1,2]
    y = [4,5,6,7]
    print(s.maxSumDistinctTriplet(x, y))