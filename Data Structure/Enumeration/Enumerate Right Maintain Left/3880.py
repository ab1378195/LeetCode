from math import inf


class Solution:
    """这里维护0和1下标时用的是判断,可以进一步统一为异或操作"""

    def minAbsoluteDifference(self, nums: list[int]) -> int:
        latest_i = latest_j = inf
        ans = 101
        for i, num in enumerate(nums):
            if num == 1:
                ans = min(ans, abs(i - latest_j))
                latest_i = i
            elif num == 2:
                ans = min(ans, abs(i - latest_i))
                latest_j = i
        return -1 if ans == 101 else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minAbsoluteDifference([1, 0, 0, 2, 0, 1]))
    print(solution.minAbsoluteDifference([1, 0, 1, 0]))
