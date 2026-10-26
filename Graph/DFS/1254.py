class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row: int, col: int) -> None:
            if grid[row][col] == 1:
                return
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                nonlocal closed
                closed = False

            grid[row][col] = 1
            if row < rows - 1:
                dfs(row + 1, col)
            if row > 0:
                dfs(row - 1, col)
            if col < cols - 1:
                dfs(row, col + 1)
            if col > 0:
                dfs(row, col - 1)

        ans = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] == 0:
                    closed = True
                    dfs(row, col)
                    ans += closed
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ]
        )
    )
    print(solution.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
    print(
        solution.closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ]
        )
    )
