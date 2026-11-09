class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_cnt = [0] * len(grid)
        col_cnt = [0] * len(grid[0])
        for i, row in enumerate(grid):
            for j, is_server in enumerate(row):
                if is_server:
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        ans = 0
        for i, row in enumerate(grid):
            for j, is_server in enumerate(row):
                if is_server and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countServers([[1, 0], [0, 1]]))
    print(solution.countServers([[1, 0], [1, 1]]))
    print(
        solution.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    )
