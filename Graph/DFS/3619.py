from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row: int, col: int) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            value = grid[row][col]
            grid[row][col] = 0
            return (
                value
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    ans += dfs(row, col) % k == 0
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.countIslands(
            [
                [0, 2, 1, 0, 0],
                [0, 5, 0, 0, 5],
                [0, 0, 1, 0, 0],
                [0, 1, 4, 7, 0],
                [0, 2, 0, 0, 8],
            ],
            5,
        )
    )
    print(solution.countIslands([[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3))
