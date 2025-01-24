class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    if i > 0:
                        self.delete(grid, i-1, j)
                    if j > 0:
                        self.delete(grid, i, j-1)
                    if i < n-1:
                        self.delete(grid, i+1, j)
                    if j < m-1:
                        self.delete(grid, i, j+1)
        return count
    
    def delete(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"
        if x > 0:
            self.delete(grid, x-1, y)
        if y > 0:
            self.delete(grid, x, y-1)
        if x < n-1:
            self.delete(grid, x+1, y)
        if y < m-1:
            self.delete(grid, x, y+1)