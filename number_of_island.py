"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List
from collections import deque


class Solution:
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return 
            
            grid[i][j] = '0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        
        for i in range(m):
           for j in range(n): 
               if grid[i][j] == '1':
                   dfs(i, j)
                   count += 1

        return count
    
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        def bfs(i: int, j: int) -> None:
            queue = deque([(i, j)])
            grid[i][j] = '0'
            while queue:
                print(queue)
                i, j = queue.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        grid[ni][nj] = '0'  # Mark as visited
                        queue.append((ni, nj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        
        return count           

    def numIslandsBFS1(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        count = 0

        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def bfs(i, j):
            queue = deque([(i, j )])
            grid[i][j] = '0'
            while queue:
                i, j = queue.popleft()
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if  0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        grid[ni][nj] = '0'
                        queue.append((ni, nj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count

    def numIslandsDFS1(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


def main():
    solution = Solution()
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
    grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print(solution.numIslandsDFS1(grid))
    print(solution.numIslandsDFS1(grid1))
    # print('\n')
    # print(solution.numIslandsBFS1(grid))
    # print(solution.numIslandsBFS1(grid1))




if __name__ == '__main__':
    main()   