from math import inf


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis = set()
        ans = inf

        def dfs(row: int, col: int, xor: int) -> None:
            nonlocal ans
            if ans == 0 or row == rows or col == cols or (row, col, xor) in vis:
                return
            vis.add((row, col, xor))
            xor ^= grid[row][col]
            if row == rows - 1 and col == cols - 1:
                ans = min(ans, xor)
                return
            dfs(row + 1, col, xor)
            dfs(row, col + 1, xor)

        dfs(0, 0, 0)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCost([[1, 2], [3, 4]]))
    print(solution.minCost([[6, 7], [5, 8]]))
    print(solution.minCost([[2, 7, 5]]))
