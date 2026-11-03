class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        ans = cover = left = 0
        for tl, tr in tiles:
            cover += tr - tl + 1
            carpet_left = tr - carpetLen + 1
            # 该循环用于从左往右找到第一个和毯子有重叠区域的tile,即滑动窗口的"出"
            while tiles[left][1] < carpet_left:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # 第一个区间可能只有部分瓷砖被毯子覆盖
            uncover = max(carpet_left - tiles[left][0], 0)
            ans = max(ans, cover - uncover)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maximumWhiteTiles([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10)
    )
    print(solution.maximumWhiteTiles([[10, 11], [1, 1]], 2))
