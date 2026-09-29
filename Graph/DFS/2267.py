from functools import cache


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ")" or grid[-1][-1] == "(":
            return False

        @cache
        def dfs(row: int, col: int, cnt: int) -> bool:
            # 右侧为剩余可走格数-1,-1是因为已经验证了最后一格为)
            if cnt > m - row + n - col - 1:
                return False
            if row == m - 1 and col == n - 1:
                return cnt == 1

            if grid[row][col] == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
            return (
                row < m - 1
                and dfs(row + 1, col, cnt)
                or col < n - 1
                and dfs(row, col + 1, cnt)
            )

        return dfs(0, 0, 0)


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.hasValidPath(
            [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]
        )
    )
    print(solution.hasValidPath([[")", ")"], ["(", "("]]))
