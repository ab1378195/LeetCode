from typing import List
from math import inf


class Solution:
    """解答用了一个dp数组,实际上只需维护前三级楼梯的状态即可,所以空间可以将数组优化为3个变量"""

    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp包含了n+1级楼梯,前三个0用于应对循环中的边界,相当于第0级
        dp = [inf] * (n + 3)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 0
        for i in range(3, n + 3):
            # i-3代表目标j台阶
            dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 4, dp[i - 3] + 9) + costs[i - 3]
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(4, [1, 2, 3, 4]))
    print(solution.climbStairs(4, [5, 1, 6, 2]))
    print(solution.climbStairs(3, [9, 8, 3]))
