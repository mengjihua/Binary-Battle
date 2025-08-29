from collections import deque
from typing import List
from heapq import heappop, heappush

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        start_pos = None
        garbage_positions = []
        garbage_index_map = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_pos = (i, j)
                elif classroom[i][j] == 'L':
                    garbage_positions.append((i, j))
                    garbage_index_map[(i, j)] = len(garbage_positions) - 1

        num_L = len(garbage_positions)
        target_mask = (1 << num_L) - 1
        if target_mask == 0:
            return 0

        dp = [[[-1] * (1 << num_L) for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append((0, start_pos[0], start_pos[1], 0, energy))        # (steps, x, y, mask, energy_left)
        dp[start_pos[0]][start_pos[1]][0] = energy

        while q:
            steps, x, y, mask, curr_energy = q.popleft()
            
            if mask == target_mask:
                return steps

            # 尝试向四个方向移动
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    cell = classroom[nx][ny]
                    new_energy = curr_energy - 1
                    new_mask = mask

                    if cell == 'R' and new_energy >= 0:
                        new_energy = energy
                    if cell == 'L':
                        idx = garbage_index_map[(nx, ny)]
                        new_mask = mask | (1 << idx)

                    if new_energy >= 0 and dp[nx][ny][new_mask] < new_energy:
                        q.append((steps + 1, nx, ny, new_mask, new_energy))
                        dp[nx][ny][new_mask] = new_energy

        return -1

# 测试
# ["S.", "XL"]
# 2
# ["LS", "RL"]
# 4
# ["L.S", "RXL"]
# 3©leetcode
if __name__ == '__main__':
    s = Solution()
    # print(s.minMoves(["S.", "XL"], 2))  # 2
    # print(s.minMoves(["LS", "RL"], 4))  # 3
    # print(s.minMoves(["L.S", "RXL"], 3))  # -1
    print(s.minMoves(["L", "R", ".", "S", "."], 1))  # -1