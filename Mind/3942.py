from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        d = nums[1] - nums[0]
        if abs(d) != 1:
            d = nums[2] - nums[1]
            if abs(d) != 1:
                return -1
        p = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] != d:
                if p > 0:
                    return -1
                p = i
        if d == 1:
            return min(p, n - p + 2)
        return min(p, n - p) + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([0, 2, 1]))
    print(solution.minOperations([1, 0, 2]))
    print(solution.minOperations([2, 0, 1, 3]))
