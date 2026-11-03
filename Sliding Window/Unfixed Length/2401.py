from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = left = or_ = 0
        for right, num in enumerate(nums):
            while or_ & num:
                or_ ^= nums[left]
                left += 1
            or_ |= num
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestNiceSubarray([1, 3, 8, 48, 10]))
    print(solution.longestNiceSubarray([3, 1, 5, 11, 13]))
