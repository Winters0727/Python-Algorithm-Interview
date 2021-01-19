from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        stack = deque()
        dr, dc = [1,-1,0,0], [0,0,1,-1]
        answer = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not visited[r][c]:
                    visited[r][c] = 1
                    stack.append([r,c])
                    while stack:
                        s_r, s_c = stack.pop()
                        for k in range(4):
                            n_r, n_c = s_r + dr[k], s_c + dc[k]
                            if 0 <= n_r < row and 0 <= n_c < col and grid[n_r][n_c] == "1" and not visited[n_r][n_c]:
                                visited[n_r][n_c] = 1
                                stack.append([n_r, n_c])
                    answer += 1
        return answer