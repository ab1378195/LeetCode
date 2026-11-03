from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def maximumCoinsRight():
            """把滑动窗口的右端点对齐每个区间的右端点"""
            ans = cover = left = 0
            for tl, tr, c in coins:
                cover += (tr - tl + 1) * c
                bag_left = tr - k + 1
                while coins[left][1] < bag_left:
                    cover -= (coins[left][1] - coins[left][0] + 1) * coins[left][2]
                    left += 1
                uncover = max((bag_left - coins[left][0]) * coins[left][2], 0)
                ans = max(ans, cover - uncover)
            return ans

        coins.sort(key=lambda coin: coin[0])
        ans = maximumCoinsRight()
        # 由于无法事先知道左边窗口的coin数量多还是右边的多,所以先将滑动窗口对齐右侧算一次,再将滑动窗口对齐左侧算一次,
        # 尽量保证滑动窗口完整覆盖了coin数量最多的窗口
        coins.reverse()
        for t in coins:
            t[0], t[1] = -t[1], -t[0]
        return max(ans, maximumCoinsRight())


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumCoins([[8, 10, 1], [1, 3, 2], [5, 6, 4]], 4))
    print(solution.maximumCoins([[1, 10, 3]], 2))
    print(
        solution.maximumCoins(
            [
                [8, 12, 13],
                [29, 32, 2],
                [13, 15, 2],
                [40, 41, 18],
                [42, 48, 18],
                [33, 36, 11],
                [37, 38, 6],
            ],
            28,
        )
    )
