class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        stones.sort()
        n = len(stones)
        e1 = stones[-2] - stones[0] - n + 2
        e2 = stones[-1] - stones[1] - n + 2
        max_move = max(e1, e2)
        # 没有空位
        if e1 == 0 or e2 == 0:
            return [min(2, max_move), max_move]
        max_cnt = left = 0
        for right, stone in enumerate(stones):
            while stone - stones[left] + 1 > n:
                left += 1
            max_cnt = max(max_cnt, right - left + 1)
        return [n - max_cnt, max_move]


if __name__ == "__main__":
    solution = Solution()
    print(solution.numMovesStonesII([7, 4, 9]))
    print(solution.numMovesStonesII([6, 5, 4, 3, 10]))
