class Solution:
    def canAliceWin(self, n: int) -> bool:
        for cur in range(10, -1, -1):
            if cur > n:
                if cur % 2 == 0:
                    return False
                else:
                    return True
            else:
                n -= cur


if __name__ == "__main__":
    solution = Solution()
    print(solution.canAliceWin(12))
    print(solution.canAliceWin(1))
