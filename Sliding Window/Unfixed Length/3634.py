from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = left = 0
        for right, num in enumerate(nums):
            while nums[left] * k < num:
                left += 1
            ans = max(ans, right - left + 1)
        return len(nums) - ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minRemoval([2, 1, 5], 2))
    print(solution.minRemoval([1, 6, 2, 9], 3))
