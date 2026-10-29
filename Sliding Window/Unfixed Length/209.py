from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = s = 0
        ans = inf
        for right, num in enumerate(nums):
            s += num
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right - left + 1)
        return 0 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(4, [1, 4, 4]))
    print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
