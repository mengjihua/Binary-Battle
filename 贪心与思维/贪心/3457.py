from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        num = n // 4
        # print(pizzas, num)
        odd_cnt, even_cnt = (num + 1) // 2, num // 2
        odd_sum = sum(pizzas[-odd_cnt:])
        p, even_sum = n - odd_cnt - 1, 0
        while even_cnt > 0:
            even_sum += pizzas[p - 1]
            p -= 2
            even_cnt -= 1
        return odd_sum + even_sum


# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.maxWeight([1, 2, 3, 4, 5, 6, 7, 8]))
    print(s.maxWeight([2, 1, 1, 1, 1, 1, 1, 1]))
    print(s.maxWeight([4, 2, 1, 5, 2, 5, 5, 4, 2, 3, 2, 1, 1, 2, 3, 4]))  
