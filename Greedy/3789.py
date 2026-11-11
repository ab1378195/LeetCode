class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        res1 = cost1 * need1 + cost2 * need2
        if need1 > need2:
            need1, need2 = need2, need1
            cost2 = cost1
        res2 = costBoth * need2
        res3 = costBoth * need1 + cost2 * (need2 - need1)
        return min(res1, res2, res3)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumCost(3, 2, 1, 3, 2))
    print(solution.minimumCost(5, 4, 15, 2, 3))
    print(solution.minimumCost(5, 4, 15, 0, 0))
