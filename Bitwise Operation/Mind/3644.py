from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums[0]:
            return 0
        ans = -1
        for i, num in enumerate(nums):
            if i != num:
                ans &= num
        return max(ans, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortPermutation([0, 3, 2, 1]))
    print(solution.sortPermutation([0, 1, 3, 2]))
    print(solution.sortPermutation([3, 2, 1, 0]))
