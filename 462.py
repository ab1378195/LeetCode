from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        ans = 0
        for num in nums[: len(nums) // 2]:
            ans += median - num
        for num in nums[len(nums) // 2 + 1 :]:
            ans += num - median
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMoves2([1, 2, 3]))
    print(solution.minMoves2([1, 10, 2, 9]))
