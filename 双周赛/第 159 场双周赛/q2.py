from typing import List

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        n = len(coords)
        if n < 3:
            return -1
        
        max_x = max_y = float('-inf')
        min_x = min_y = float('inf')
        for x, y in coords:
            max_x, min_x = max(max_x, x), min(min_x, x)
            max_y, min_y = max(max_y, y), min(min_y, y)
        
        y_group = {}
        x_group = {}
        for x, y in coords:
            if y not in y_group:
                y_group[y] = []
            y_group[y].append(x)
            
            if x not in x_group:
                x_group[x] = []
            x_group[x].append(y)
        
        ans = 0
        for y, x_lst in y_group.items():
            if len(x_lst) < 2:
                continue
            base = max(x_lst) - min(x_lst)
            height = max(abs(y - min_y), abs(y - max_y))
            candidate = base * height
            if candidate > ans:
                ans = candidate
        
        for x, y_lst in x_group.items():
            if len(y_lst) < 2:
                continue
            base = max(y_lst) - min(y_lst)
            width = max(abs(x - min_x), abs(x - max_x))
            candidate = base * width
            if candidate > ans:
                ans = candidate
        
        return ans if ans > 0 else -1

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([[1, 1], [2, 2], [3, 3]]))
    print(s.maxArea([[1, 2], [2, 3], [2, 4], [4, 5]]))
    print(s.maxArea([[1, 1], [2, 1], [2, 2], [4, 5]]))
    print(s.maxArea([[1,1],[1,2],[3,2],[3,3]]))